from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from enum import Enum
from pathlib import Path
from typing import Any

from datasets.load_ieee118 import load_data
from problems.eon_grid_expansion.decision_space import CandidateLine
from problems.eon_grid_expansion.infrastructure import InfrastructureState
from src.optimization.results.analytics import build_optimization_analytics
from src.optimization.results.solution import (
    InfrastructureExpansionPlan,
    OptimizationExecutionSummary,
    OptimizationSolution,
    SelectedExpansionDecision,
)
from src.optimization.topology.congestion import analyze_topology_congestion
from src.optimization.topology.explainability import (
    build_operational_reasoning_report,
)
from src.optimization.topology.graph import (
    GraphProjectionArtifacts,
    build_operational_graph,
    project_solution_overlay,
    project_to_networkx,
)
from src.optimization.topology.metrics import (
    build_topology_metrics_report,
)
from src.optimization.topology.resilience import (
    analyze_network_resilience,
)


def analyze_topology(
    *,
    run_dir: Path,
    output_dir: Path | None = None,
    data=None,
) -> dict[str, Any]:
    run_dir = Path(run_dir)
    output_dir = Path(output_dir) if output_dir is not None else run_dir

    selected_path = run_dir / "selected_lines.json"
    candidate_path = run_dir / "candidate_list.json"
    manifest_path = run_dir / "workflow_manifest.json"

    _require_file(selected_path)
    _require_file(candidate_path)

    selected_payload = _load_json(selected_path)
    candidate_payload = _load_json(candidate_path)
    manifest_payload = _load_optional_json(manifest_path)

    data = data or load_data()
    infrastructure = _build_infrastructure_state(data)

    candidate_lookup = {
        row["candidate_id"]: _candidate_from_payload(row)
        for row in candidate_payload.get("candidates", [])
    }

    selected_rows = selected_payload.get("selected_candidates", [])
    selected_candidates = [
        _selected_candidate_from_row(row, candidate_lookup)
        for row in selected_rows
    ]

    solution = _build_solution(
        run_dir=run_dir,
        selected_payload=selected_payload,
        selected_candidates=selected_candidates,
        manifest_payload=manifest_payload,
    )

    topology_graph = build_operational_graph(
        infrastructure=infrastructure,
        candidate_lines=selected_candidates,
    )
    projection = GraphProjectionArtifacts(
        topology_graph=topology_graph,
        networkx_graph=project_to_networkx(topology_graph).networkx_graph,
    )
    projected_graph = GraphProjectionArtifacts(
        topology_graph=topology_graph,
        networkx_graph=project_solution_overlay(
            projection,
            solution,
        ),
    )

    analytics = build_optimization_analytics(solution)
    congestion = analyze_topology_congestion(
        projected_graph,
        solution,
    )
    resilience = analyze_network_resilience(
        projected_graph,
        solution,
    )
    metrics = build_topology_metrics_report(
        projected_graph,
        solution,
        congestion,
        resilience,
    )
    reasoning = build_operational_reasoning_report(
        solution,
        analytics,
        congestion,
        resilience,
    )

    scenario_name = _scenario_name(run_dir, manifest_payload)

    payload = {
        "analysis_scope": {
            "mode": "topology_heuristic",
            "physical_power_flow": False,
            "n_minus_one_validation": False,
            "run_dir": str(run_dir),
            "output_dir": str(output_dir),
        },
        "run_metadata": {
            "scenario_name": scenario_name,
            "scenario_id": solution.scenario_id,
            "solver_name": selected_payload.get("solver_name", "unknown"),
            "budget_ratio": manifest_payload.get("budget_ratio") if manifest_payload else None,
            "selected_count": len(selected_candidates),
            "candidate_count": len(candidate_lookup),
            "generated_at": datetime.now(UTC),
        },
        "selected_candidates": selected_candidates,
        "optimization_solution": solution,
        "analytics": analytics,
        "congestion_analysis": congestion,
        "resilience_analysis": resilience,
        "topology_metrics": metrics,
        "reasoning_report": reasoning,
    }

    serialized_payload = _to_jsonable(payload)
    _write_outputs(output_dir=output_dir, payload=serialized_payload)
    return serialized_payload


def _require_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(path)


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_optional_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return _load_json(path)


def _build_infrastructure_state(data) -> InfrastructureState:
    mapped = data.mapped
    return InfrastructureState(
        buses=mapped["buses"],
        bus_states=mapped["bus_states"],
        lines=mapped["lines"],
        line_flows=mapped["line_flows"],
        loads=mapped["loads"],
        generators=mapped["generators"],
    )


def _candidate_from_payload(row: dict[str, Any]) -> CandidateLine:
    return CandidateLine(
        candidate_id=row["candidate_id"],
        from_bus=str(row["from_bus"]),
        to_bus=str(row["to_bus"]),
        capacity_mva=float(row["capacity_mva"]),
        build_cost=float(row["build_cost"]),
        length_km=float(row["length_km"]),
        voltage_kv=float(row["voltage_kv"]),
    )


def _selected_candidate_from_row(
    row: dict[str, Any],
    candidate_lookup: dict[str, CandidateLine],
) -> CandidateLine:
    candidate_id = row["candidate_id"]
    candidate = candidate_lookup.get(candidate_id)
    if candidate is None:
        raise ValueError(f"Selected candidate not found in candidate list: {candidate_id}")
    return candidate


def _build_solution(
    *,
    run_dir: Path,
    selected_payload: dict[str, Any],
    selected_candidates: list[CandidateLine],
    manifest_payload: dict[str, Any],
) -> OptimizationSolution:
    scenario_id = manifest_payload.get("scenario_id") or run_dir.name

    candidate_scores = _normalise_candidate_scores(
        candidate for candidate in selected_candidates
    )

    selected_expansions = [
        SelectedExpansionDecision(
            candidate_id=candidate.candidate_id,
            from_bus=candidate.from_bus,
            to_bus=candidate.to_bus,
            capacity_mva=candidate.capacity_mva,
            build_cost=candidate.build_cost,
            voltage_kv=candidate.voltage_kv,
            decision_score=candidate_scores[candidate.candidate_id],
        )
        for candidate in selected_candidates
    ]

    expansion_plan = InfrastructureExpansionPlan(
        selected_expansions=selected_expansions,
        total_expansion_cost=sum(candidate.build_cost for candidate in selected_candidates),
        total_added_capacity_mva=sum(candidate.capacity_mva for candidate in selected_candidates),
    )

    execution_summary = OptimizationExecutionSummary(
        solver_name=selected_payload.get("solver_name", "unknown"),
        objective_value=float(selected_payload.get("objective_value", 0.0)),
        solve_time_seconds=float(selected_payload.get("solve_time_seconds", 0.0)),
        termination_condition=str(selected_payload.get("termination_condition", "unknown")),
    )

    return OptimizationSolution(
        problem_id="eon_grid_expansion",
        scenario_id=scenario_id,
        generated_at=datetime.now(UTC),
        expansion_plan=expansion_plan,
        execution_summary=execution_summary,
    )


def _normalise_candidate_scores(candidates: list[CandidateLine]) -> dict[str, float]:
    raw_scores = {
        candidate.candidate_id: _raw_candidate_score(candidate)
        for candidate in candidates
    }
    if not raw_scores:
        return {}

    values = list(raw_scores.values())
    min_score = min(values)
    max_score = max(values)
    if max_score - min_score <= 1e-9:
        return {candidate_id: 1.0 for candidate_id in raw_scores}

    return {
        candidate_id: (score - min_score) / (max_score - min_score)
        for candidate_id, score in raw_scores.items()
    }


def _raw_candidate_score(candidate: CandidateLine) -> float:
    return float(candidate.capacity_mva / max(candidate.build_cost, 1.0))


def _scenario_name(run_dir: Path, manifest_payload: dict[str, Any]) -> str:
    return str(manifest_payload.get("scenario_name") or run_dir.name)


def _write_outputs(*, output_dir: Path, payload: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "topology_analysis.json").write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )

    summary = {
        "analysis_scope": payload["analysis_scope"],
        "run_metadata": payload["run_metadata"],
        "topology_metrics": payload["topology_metrics"],
    }
    (output_dir / "topology_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    (output_dir / "topology_report.md").write_text(
        _render_topology_markdown(payload),
        encoding="utf-8",
    )


def _render_topology_markdown(payload: dict[str, Any]) -> str:
    analysis_scope = payload["analysis_scope"]
    run_metadata = payload["run_metadata"]
    topology_metrics = payload["topology_metrics"]
    congestion = payload["congestion_analysis"]
    resilience = payload["resilience_analysis"]
    reasoning = payload["reasoning_report"]

    lines = [
        "# Topology Analysis Report",
        "",
        "This analysis is graph-topology-based and heuristic-first.",
        "It is not a physical AC power-flow simulation or an N-1 study.",
        "",
        f"Run Dir: {analysis_scope['run_dir']}",
        f"Scenario: {run_metadata['scenario_name']}",
        f"Selected Candidates: {run_metadata['selected_count']}",
        f"Candidate Count: {run_metadata['candidate_count']}",
        "",
        "## Metrics",
        json.dumps(topology_metrics, indent=2),
        "",
        "## Congestion",
        json.dumps(congestion, indent=2),
        "",
        "## Resilience",
        json.dumps(resilience, indent=2),
        "",
        "## Reasoning",
        json.dumps(reasoning, indent=2),
    ]
    return "\n".join(lines)


def _to_jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return _to_jsonable(asdict(value))
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _to_jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_to_jsonable(item) for item in value]
    if isinstance(value, tuple):
        return [_to_jsonable(item) for item in value]
    return value


def _to_object(value: Any) -> Any:
    if isinstance(value, dict):
        return type("_Obj", (), {key: _to_object(item) for key, item in value.items()})()
    if isinstance(value, list):
        return [_to_object(item) for item in value]
    return value


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Analyze topology artifacts for a completed workflow run.")
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    analyze_topology(run_dir=args.run_dir, output_dir=args.output_dir)


if __name__ == "__main__":
    main()
