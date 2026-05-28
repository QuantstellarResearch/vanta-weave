from __future__ import annotations

import json
from dataclasses import dataclass

from workflows.generate_candidates import write_candidate_list


@dataclass
class _Candidate:
    candidate_id: str
    from_bus: str
    to_bus: str
    capacity_mva: float
    build_cost: float
    length_km: float
    voltage_kv: float


def test_write_candidate_list_writes_expected_payload(tmp_path):
    output_path = tmp_path / "candidate_list.json"
    candidates = [
        _Candidate(
            candidate_id="cand_1",
            from_bus="1",
            to_bus="2",
            capacity_mva=500.0,
            build_cost=12.34,
            length_km=5.6,
            voltage_kv=110.0,
        )
    ]

    write_candidate_list(candidates, output_path=output_path)

    payload = json.loads(output_path.read_text(encoding="utf-8"))

    assert payload["generator"] == "generate_candidates"
    assert payload["count"] == 1
    assert payload["candidates"][0]["candidate_id"] == "cand_1"
    assert payload["candidates"][0]["length_km"] == 5.6
