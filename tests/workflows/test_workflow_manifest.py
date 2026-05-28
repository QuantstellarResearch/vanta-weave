from __future__ import annotations

import json
from types import SimpleNamespace

import workflows.run_eon_workflow as workflow


def test_write_workflow_manifest_writes_minimal_metadata(tmp_path):
    output_path = tmp_path / "workflow_manifest.json"

    workflow.write_workflow_manifest(
        output_path=output_path,
        problem_id="eon_grid_expansion",
        scenario_id="baseline",
        scenario_name="Baseline",
        solver_name="highs",
        budget_ratio=0.15,
        candidate_count=12,
        run_dir=tmp_path,
    )

    payload = json.loads(output_path.read_text(encoding="utf-8"))

    assert payload["problem_id"] == "eon_grid_expansion"
    assert payload["scenario_id"] == "baseline"
    assert payload["scenario_name"] == "Baseline"
    assert payload["solver_name"] == "highs"
    assert payload["budget_ratio"] == 0.15
    assert payload["candidate_count"] == 12
    assert payload["run_dir"] == str(tmp_path)


def test_run_eon_workflow_writes_workflow_manifest(monkeypatch, tmp_path):
    captured = {}

    monkeypatch.setattr(workflow, "OUTPUT_DIR", tmp_path)
    monkeypatch.setattr(workflow, "JSON_PATH", tmp_path / "selected_lines.json")
    monkeypatch.setattr(workflow, "CSV_PATH", tmp_path / "selected_lines.csv")
    monkeypatch.setattr(workflow, "load_data", lambda: SimpleNamespace())
    monkeypatch.setattr(workflow, "generate_candidates", lambda data, config: [])
    monkeypatch.setattr(workflow, "write_candidate_list", lambda candidates: None)

    def fake_run_optimization(*, data, candidates, config):
        captured["solver_name"] = config.solver_name
        return SimpleNamespace(
            objective_value=1.0,
            execution_metadata=SimpleNamespace(
                solver_name=config.solver_name,
                solve_time_seconds=0.1,
            ),
            selected_candidate_ids=[],
        )

    monkeypatch.setattr(workflow, "run_optimization", fake_run_optimization)
    monkeypatch.setattr(workflow, "_write_outputs", lambda payload: None)

    workflow.run_eon_workflow()

    manifest_path = tmp_path / "workflow_manifest.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert captured["solver_name"] == "highs"
    assert payload["problem_id"] == "eon_grid_expansion"
    assert payload["solver_name"] == "highs"
    assert payload["candidate_count"] == 0
