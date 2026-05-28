from __future__ import annotations

from types import SimpleNamespace

import workflows.run_eon_workflow as workflow


def test_run_eon_workflow_defaults_to_highs(monkeypatch):
    captured = {}

    monkeypatch.setattr(workflow, "load_data", lambda: SimpleNamespace())
    monkeypatch.setattr(
        workflow,
        "generate_candidates",
        lambda data, config: [],
    )
    monkeypatch.setattr(workflow, "write_candidate_list", lambda candidates: None)

    def fake_run_optimization(*, data, candidates, config):
        captured["solver_name"] = config.solver_name
        return SimpleNamespace(
            objective_value=1.0,
            execution_metadata=SimpleNamespace(solver_name=config.solver_name, solve_time_seconds=0.1),
            selected_candidate_ids=[],
        )

    monkeypatch.setattr(workflow, "run_optimization", fake_run_optimization)
    monkeypatch.setattr(workflow, "_write_outputs", lambda payload: None)

    payload = workflow.run_eon_workflow()

    assert captured["solver_name"] == "highs"
    assert payload["solver_name"] == "highs"


def test_run_eon_workflow_accepts_solver_override(monkeypatch):
    captured = {}

    monkeypatch.setattr(workflow, "load_data", lambda: SimpleNamespace())
    monkeypatch.setattr(
        workflow,
        "generate_candidates",
        lambda data, config: [],
    )
    monkeypatch.setattr(workflow, "write_candidate_list", lambda candidates: None)

    def fake_run_optimization(*, data, candidates, config):
        captured["solver_name"] = config.solver_name
        return SimpleNamespace(
            objective_value=1.0,
            execution_metadata=SimpleNamespace(solver_name=config.solver_name, solve_time_seconds=0.1),
            selected_candidate_ids=[],
        )

    monkeypatch.setattr(workflow, "run_optimization", fake_run_optimization)
    monkeypatch.setattr(workflow, "_write_outputs", lambda payload: None)

    payload = workflow.run_eon_workflow(solver_name="cplex")

    assert captured["solver_name"] == "cplex"
    assert payload["solver_name"] == "cplex"
