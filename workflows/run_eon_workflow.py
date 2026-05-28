from __future__ import annotations

import csv
import json
from datetime import UTC, datetime
from pathlib import Path

from datasets.load_ieee118 import load_data
from workflows.generate_candidates import (
    CandidateGenerationConfig,
    generate_candidates,
    write_candidate_list,
)
from workflows.run_optimization import (
    OptimizationRunConfig,
    run_optimization,
)


OUTPUT_DIR = Path("outputs")
JSON_PATH = OUTPUT_DIR / "selected_lines.json"
CSV_PATH = OUTPUT_DIR / "selected_lines.csv"


def write_workflow_manifest(
    *,
    output_path: Path,
    problem_id: str,
    scenario_id: str,
    scenario_name: str,
    solver_name: str,
    budget_ratio: float,
    candidate_count: int,
    run_dir: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "problem_id": problem_id,
        "scenario_id": scenario_id,
        "scenario_name": scenario_name,
        "solver_name": solver_name,
        "budget_ratio": budget_ratio,
        "candidate_count": candidate_count,
        "generated_at": datetime.now(UTC).isoformat(),
        "run_dir": str(run_dir),
    }

    output_path.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )


def run_eon_workflow(
    solver_name: str = "highs",
) -> dict:
    data = load_data()

    candidates = generate_candidates(
        data=data,
        config=CandidateGenerationConfig(),
    )

    write_candidate_list(candidates)

    write_workflow_manifest(
        output_path=OUTPUT_DIR / "workflow_manifest.json",
        problem_id="eon_grid_expansion",
        scenario_id="baseline",
        scenario_name="Baseline",
        solver_name=solver_name,
        budget_ratio=0.15,
        candidate_count=len(candidates),
        run_dir=OUTPUT_DIR,
    )

    result = run_optimization(
        data=data,
        candidates=candidates,
        config=OptimizationRunConfig(
            solver_name=solver_name,
        ),
    )

    selected = _select_candidates(
        candidates=candidates,
        selected_ids=set(result.selected_candidate_ids),
    )

    payload = _build_output_payload(
        result=result,
        selected_candidates=selected,
    )

    _write_outputs(payload=payload)

    print(
        f"Selected {payload['selected_count']} lines "
        f"(objective={payload['objective_value']:.4f})."
    )

    return payload


def _select_candidates(
    *,
    candidates,
    selected_ids: set[str],
):
    normalized_ids = {
        _normalize_candidate_id(
            selected_id
        )
        for selected_id in selected_ids
    }
    return [
        candidate
        for candidate in candidates
        if candidate.candidate_id in normalized_ids
    ]


def _normalize_candidate_id(
    selected_id: str,
) -> str:
    if selected_id.startswith("expansion_"):
        return selected_id.replace(
            "expansion_",
            "",
            1,
        )
    return selected_id


def _build_output_payload(
    *,
    result,
    selected_candidates,
) -> dict:
    return {
        "objective_value": result.objective_value,
        "solver_name": result.execution_metadata.solver_name,
        "solve_time_seconds": (
            result.execution_metadata.solve_time_seconds
        ),
        "selected_count": len(selected_candidates),
        "selected_candidates": [
            {
                "candidate_id": candidate.candidate_id,
                "from_bus": candidate.from_bus,
                "to_bus": candidate.to_bus,
                "capacity_mva": candidate.capacity_mva,
                "build_cost": candidate.build_cost,
                "voltage_kv": candidate.voltage_kv,
            }
            for candidate in selected_candidates
        ],
        "assumptions": {
            "candidates": "heuristic",
            "costs": "proxy",
            "budget": "ratio",
        },
    }


def _write_outputs(*, payload: dict) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    JSON_PATH.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )

    fieldnames = [
        "candidate_id",
        "from_bus",
        "to_bus",
        "capacity_mva",
        "build_cost",
        "voltage_kv",
    ]

    with CSV_PATH.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
        )
        writer.writeheader()
        for row in payload["selected_candidates"]:
            writer.writerow(row)


if __name__ == "__main__":
    run_eon_workflow()
