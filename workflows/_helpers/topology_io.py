# workflows/_helpers/topology_io.py
import json
from typing import List, Dict


def read_candidate_list(path: str) -> List[Dict]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def read_selected_lines(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Accept either {"selected_candidates": [...]} or a list
    if isinstance(data, dict) and 'selected_candidates' in data:
        return data['selected_candidates']
    if isinstance(data, list):
        return data
    raise ValueError("Unsupported selected_lines.json format")


def build_minimal_solution(candidates: List[Dict], selected_ids: List[str]) -> Dict:
    # Simple structure consumed by the topology projection/analysis code
    cand_map = {c['candidate_id']: c for c in candidates}
    return {"selected_ids": selected_ids, "candidates": cand_map}
