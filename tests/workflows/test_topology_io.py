# tests/workflows/test_topology_io.py
import json
from pathlib import Path

from workflows._helpers.topology_io import read_candidate_list, read_selected_lines, build_minimal_solution

def test_minimal_solution_roundtrip(tmp_path):
    cand = [{"candidate_id": "c1", "spec": {"length": 10}}]
    selected = {"selected_candidates": ["c1"]}
    cand_file = tmp_path / "candidate_list.json"
    sel_file = tmp_path / "selected_lines.json"
    cand_file.write_text(json.dumps(cand))
    sel_file.write_text(json.dumps(selected))

    candidates = read_candidate_list(str(cand_file))
    selected_ids = read_selected_lines(str(sel_file))
    solution = build_minimal_solution(candidates, selected_ids)

    assert solution["selected_ids"] == ["c1"]
    assert "candidates" in solution
