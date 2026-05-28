from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace

from src.utils.distance_length import tinh_khoang_cach_bus


@dataclass
class _Bus:
    id: int
    geo: str | None


def test_tinh_khoang_cach_bus_looks_up_bus_by_id_and_uses_geo_coordinates():
    data = SimpleNamespace(
        mapped={
            "buses": [
                _Bus(
                    id=10,
                    geo='{"coordinates": [106.6297, 10.8231]}',
                ),
                _Bus(
                    id=20,
                    geo='{"coordinates": [106.7000, 10.9000]}',
                ),
            ]
        }
    )

    distance = tinh_khoang_cach_bus(data, 10, 20)

    assert distance is not None
    assert distance > 0
