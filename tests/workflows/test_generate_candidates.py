from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace

from workflows.generate_candidates import (
    CandidateGenerationConfig,
    generate_candidates,
)


@dataclass
class _Bus:
    id: int
    voltage_kv: float
    geo: str | None


def test_shortcut_candidate_length_uses_bus_geo_distance():
    data = SimpleNamespace(
        mapped={
            "buses": [
                _Bus(
                    id=1,
                    voltage_kv=110.0,
                    geo='{"coordinates": [106.6297, 10.8231]}',
                ),
                _Bus(
                    id=2,
                    voltage_kv=110.0,
                    geo='{"coordinates": [106.7000, 10.9000]}',
                ),
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

    candidates = generate_candidates(
        data,
        CandidateGenerationConfig(max_candidates=10, top_k_buses=2),
    )

    shortcut = next(c for c in candidates if c.from_bus == "1" and c.to_bus == "2")

    assert shortcut.length_km is not None
    assert shortcut.length_km > 1.0
