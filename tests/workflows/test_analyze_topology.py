from __future__ import annotations

import json
from dataclasses import dataclass
from types import SimpleNamespace

import networkx as nx
import pytest

import workflows.analyze_topology as topology_analysis
from problems.eon_grid_expansion.infrastructure import InfrastructureState
from src.optimization.topology.graph import (
    build_operational_graph,
    project_solution_overlay,
    project_to_networkx,
)


@dataclass
class _AnalysisStub:
    label: str


def test_analyze_topology_requires_required_artifacts(tmp_path):
    with pytest.raises(FileNotFoundError):
        topology_analysis.analyze_topology(run_dir=tmp_path / "missing")


def test_analyze_topology_writes_deterministic_outputs(tmp_path, monkeypatch):
    run_dir = tmp_path / "run-001"
    output_dir = tmp_path / "analysis"
    run_dir.mkdir()

    (run_dir / "selected_lines.json").write_text(
        json.dumps(
            {
                "objective_value": 12.3,
                "solver_name": "highs",
                "solve_time_seconds": 0.5,
                "selected_count": 1,
                "selected_candidates": [
                    {
                        "candidate_id": "cand_1",
                        "from_bus": "1",
                        "to_bus": "2",
                        "capacity_mva": 500.0,
                        "build_cost": 10.0,
                        "voltage_kv": 110.0,
                    }
                ],
                "assumptions": {
                    "candidates": "heuristic",
                    "costs": "proxy",
                    "budget": "ratio",
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (run_dir / "candidate_list.json").write_text(
        json.dumps(
            {
                "generator": "generate_candidates",
                "count": 1,
                "candidates": [
                    {
                        "candidate_id": "cand_1",
                        "from_bus": "1",
                        "to_bus": "2",
                        "capacity_mva": 500.0,
                        "build_cost": 10.0,
                        "length_km": 10.0,
                        "voltage_kv": 110.0,
                    }
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (run_dir / "workflow_manifest.json").write_text(
        json.dumps(
            {
                "scenario_id": "baseline",
                "scenario_name": "Baseline",
                "budget_ratio": 0.15,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        topology_analysis,
        "_build_infrastructure_state",
        lambda data: InfrastructureState([], [], [], [], [], []),
    )
    monkeypatch.setattr(
        topology_analysis,
        "build_operational_graph",
        lambda infrastructure, candidate_lines: SimpleNamespace(
            infrastructure=infrastructure,
            candidate_lines=candidate_lines,
        ),
    )
    monkeypatch.setattr(
        topology_analysis,
        "project_to_networkx",
        lambda topology_graph: topology_analysis.GraphProjectionArtifacts(
            topology_graph=topology_graph,
            networkx_graph=nx.Graph(),
        ),
    )
    monkeypatch.setattr(
        topology_analysis,
        "project_solution_overlay",
        lambda projection, solution: nx.Graph(),
    )
    monkeypatch.setattr(
        topology_analysis,
        "build_optimization_analytics",
        lambda solution: _AnalysisStub(label="analytics"),
    )
    monkeypatch.setattr(
        topology_analysis,
        "analyze_topology_congestion",
        lambda projection, solution: _AnalysisStub(label="congestion"),
    )
    monkeypatch.setattr(
        topology_analysis,
        "analyze_network_resilience",
        lambda projection, solution: _AnalysisStub(label="resilience"),
    )
    monkeypatch.setattr(
        topology_analysis,
        "build_topology_metrics_report",
        lambda projection, solution, congestion, resilience: _AnalysisStub(label="metrics"),
    )
    monkeypatch.setattr(
        topology_analysis,
        "build_operational_reasoning_report",
        lambda solution, analytics, congestion, resilience: _AnalysisStub(label="reasoning"),
    )
    payload = topology_analysis.analyze_topology(
        run_dir=run_dir,
        output_dir=output_dir,
        data=SimpleNamespace(mapped={}),
    )

    assert payload["analysis_scope"]["mode"] == "topology_heuristic"
    assert payload["run_metadata"]["selected_count"] == 1
    assert (output_dir / "topology_analysis.json").exists()
    assert (output_dir / "topology_summary.json").exists()
    assert (output_dir / "topology_report.md").exists()


def test_project_solution_overlay_normalizes_node_ids():
    infrastructure = InfrastructureState([], [], [], [], [], [])
    topology_graph = build_operational_graph(
        infrastructure=infrastructure,
        candidate_lines=[],
    )
    projection = project_to_networkx(topology_graph)

    solution = topology_analysis.OptimizationSolution(
        problem_id="eon_grid_expansion",
        scenario_id="baseline",
        generated_at=topology_analysis.datetime.now(topology_analysis.UTC),
        expansion_plan=topology_analysis.InfrastructureExpansionPlan(
            selected_expansions=[
                topology_analysis.SelectedExpansionDecision(
                    candidate_id="cand_1",
                    from_bus="1",
                    to_bus="2",
                    capacity_mva=500.0,
                    build_cost=10.0,
                    voltage_kv=110.0,
                    decision_score=1.0,
                )
            ],
            total_expansion_cost=10.0,
            total_added_capacity_mva=500.0,
        ),
        execution_summary=topology_analysis.OptimizationExecutionSummary(
            solver_name="highs",
            objective_value=1.0,
            solve_time_seconds=0.1,
            termination_condition="optimal",
        ),
    )

    overlay = project_solution_overlay(projection, solution)

    assert 1 not in overlay.nodes
    assert "1" in overlay.nodes
    assert 2 not in overlay.nodes
    assert "2" in overlay.nodes
