# tests/workflows/test_analyze_topology.py
import json
from pathlib import Path

from workflows.analyze_topology import run_topology_report


def test_run_topology_report_creates_outputs(tmp_path):
    # Prepare minimal inputs
    cand = [{"candidate_id": "c1", "spec": {"length": 10}}]
    selected = {"selected_candidates": ["c1"]}
    cand_file = tmp_path / "candidate_list.json"
    sel_file = tmp_path / "selected_lines.json"
    cand_file.write_text(json.dumps(cand))
    sel_file.write_text(json.dumps(selected))

    out = tmp_path / "out"
    out.mkdir()

    run_topology_report(candidate_list_path=str(cand_file), selected_path=str(sel_file), out_dir=str(out))

    assert (out / "topology_report.json").exists()
    assert (out / "topology_report.md").exists()
