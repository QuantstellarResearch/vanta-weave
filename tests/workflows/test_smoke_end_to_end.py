# tests/workflows/test_smoke_end_to_end.py
import json
from pathlib import Path

from workflows.analyze_topology import run_topology_report


def test_smoke_end_to_end(tmp_path):
    cand = [{"candidate_id": "c1", "spec": {"from": "n1", "to": "n2", "length": 10}}]
    selected = {"selected_candidates": ["c1"]}
    cand_file = tmp_path / "candidate_list.json"
    sel_file = tmp_path / "selected_lines.json"
    cand_file.write_text(json.dumps(cand))
    sel_file.write_text(json.dumps(selected))

    out = tmp_path / "out"
    out.mkdir()

    report = run_topology_report(candidate_list_path=str(cand_file), selected_path=str(sel_file), out_dir=str(out))

    assert (out / "topology_report.json").exists()
    assert (out / "topology_report.md").exists()
    assert (out / "topology_viz.png").exists()
    assert (out / "topology_report.prov.json").exists()
    assert "metrics" in report
