from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace

import workflows.generate_candidates as candidate_workflow


@dataclass
class _Bus:
    id: int
    voltage_kv: float
    geo: str | None


def test_generate_candidates_does_not_write_candidate_list_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    data = SimpleNamespace(
        mapped={
            "buses": [
                _Bus(id=1, voltage_kv=110.0, geo='{"coordinates": [106.0, 10.0]}'),
                _Bus(id=2, voltage_kv=110.0, geo='{"coordinates": [106.1, 10.1]}'),
            ],
            "lines": [],
            "line_flows": [],
            "loads": [
                SimpleNamespace(bus=1, active_power_mw=10.0),
                SimpleNamespace(bus=2, active_power_mw=10.0),
            ],
            "generators": [],
        }
    )

    candidate_workflow.generate_candidates(data)

    assert not (tmp_path / "outputs" / "candidate_list.json").exists()
