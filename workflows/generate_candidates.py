from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

from problems.eon_grid_expansion.decision_space import (
    CandidateLine,
    DecisionSpace,
)


@dataclass(frozen=True)
class CandidateGenerationConfig:
    overload_threshold: float = 1.0
    parallel_capacity_scale: float = 1.2
    top_k_buses: int = 10
    max_candidates: int = 50


def generate_candidates(
    data,
    config: CandidateGenerationConfig | None = None,
) -> list[CandidateLine]:
    """
    Generate candidate transmission lines using
    deterministic heuristics.

    This is a proxy workflow intended for MVP
    pipeline validation. It does NOT model
    AC power flow or N-1 reliability.
    """

    config = config or CandidateGenerationConfig()

    mapped = data.mapped
    lines = mapped["lines"]
    line_flows = mapped["line_flows"]
    loads = mapped["loads"]
    generators = mapped["generators"]
    buses = mapped["buses"]

    line_by_id = {line.id: line for line in lines}
    bus_voltage_by_id = {
        bus.id: bus.voltage_kv
        for bus in buses
    }

    existing_edges = _build_existing_edges(lines)

    candidates: list[CandidateLine] = []

    candidates.extend(
        _build_parallel_candidates(
            line_flows=line_flows,
            line_by_id=line_by_id,
            bus_voltage_by_id=bus_voltage_by_id,
            existing_edges=existing_edges,
            config=config,
        )
    )

    if len(candidates) < config.max_candidates:
        candidates.extend(
            _build_shortcut_candidates(
                loads=loads,
                generators=generators,
                bus_voltage_by_id=bus_voltage_by_id,
                existing_edges=existing_edges,
                config=config,
                remaining=(
                    config.max_candidates
                    - len(candidates)
                ),
            )
        )

    return candidates[: config.max_candidates]


def build_decision_space(
    candidates: Iterable[CandidateLine],
) -> DecisionSpace:
    return DecisionSpace(
        candidate_lines=list(candidates)
    )


def _build_existing_edges(lines) -> set[tuple[int, int]]:
    edges = set()
    for line in lines:
        edges.add((line.from_bus, line.to_bus))
        edges.add((line.to_bus, line.from_bus))
    return edges


def _build_parallel_candidates(
    *,
    line_flows,
    line_by_id,
    bus_voltage_by_id,
    existing_edges,
    config: CandidateGenerationConfig,
) -> list[CandidateLine]:
    candidates: list[CandidateLine] = []

    for flow in line_flows:
        if flow.loading_percent < config.overload_threshold:
            continue

        line = line_by_id.get(flow.line_id)
        if line is None:
            continue

        from_bus = line.from_bus
        to_bus = line.to_bus

        if (from_bus, to_bus) not in existing_edges:
            existing_edges.add((from_bus, to_bus))

        capacity_mva = _safe_capacity(line) * (
            config.parallel_capacity_scale
        )
        voltage_kv = _estimate_voltage_kv(
            from_bus,
            to_bus,
            bus_voltage_by_id,
        )
        length_km = getattr(line, "length_km", 1.0)
        build_cost = _estimate_cost(
            length_km=length_km,
            voltage_kv=voltage_kv,
            max_current_ka=getattr(
                line, "max_current_ka", None
            ),
        )

        candidate_id = (
            f"cand_parallel_{from_bus}_{to_bus}_"
            f"{len(candidates)}"
        )

        candidates.append(
            CandidateLine(
                candidate_id=candidate_id,
                from_bus=str(from_bus),
                to_bus=str(to_bus),
                capacity_mva=capacity_mva,
                build_cost=build_cost,
                length_km=length_km,
                voltage_kv=voltage_kv,
            )
        )

    return candidates


def _build_shortcut_candidates(
    *,
    loads,
    generators,
    bus_voltage_by_id,
    existing_edges,
    config: CandidateGenerationConfig,
    remaining: int,
) -> list[CandidateLine]:
    candidates: list[CandidateLine] = []

    bus_scores: dict[int, float] = {}
    for load in loads:
        bus_scores[load.bus] = (
            bus_scores.get(load.bus, 0.0)
            + load.active_power_mw
        )
    for generator in generators:
        bus_scores[generator.bus] = (
            bus_scores.get(generator.bus, 0.0)
            + generator.active_power_mw
        )

    top_buses = [
        bus_id
        for bus_id, _ in sorted(
            bus_scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )[: config.top_k_buses]
    ]

    for from_bus, to_bus in combinations(
        top_buses, 2
    ):
        if len(candidates) >= remaining:
            break
        if (from_bus, to_bus) in existing_edges:
            continue

        existing_edges.add((from_bus, to_bus))
        existing_edges.add((to_bus, from_bus))

        voltage_kv = _estimate_voltage_kv(
            from_bus,
            to_bus,
            bus_voltage_by_id,
        )
        length_km = 1.0
        capacity_mva = _default_capacity(
            voltage_kv
        )
        build_cost = _estimate_cost(
            length_km=length_km,
            voltage_kv=voltage_kv,
            max_current_ka=None,
        )

        candidate_id = (
            f"cand_shortcut_{from_bus}_{to_bus}_"
            f"{len(candidates)}"
        )

        candidates.append(
            CandidateLine(
                candidate_id=candidate_id,
                from_bus=str(from_bus),
                to_bus=str(to_bus),
                capacity_mva=capacity_mva,
                build_cost=build_cost,
                length_km=length_km,
                voltage_kv=voltage_kv,
            )
        )

    return candidates


def _safe_capacity(line) -> float:
    return float(
        getattr(line, "capacity_mva", 0.0)
        or 0.0
    )


def _default_capacity(voltage_kv: float) -> float:
    if voltage_kv >= 220.0:
        return 1000.0
    return 500.0


def _estimate_voltage_kv(
    from_bus: int,
    to_bus: int,
    bus_voltage_by_id: dict[int, float],
) -> float:
    from_voltage = bus_voltage_by_id.get(
        from_bus, 110.0
    )
    to_voltage = bus_voltage_by_id.get(
        to_bus, from_voltage
    )
    return float((from_voltage + to_voltage) / 2.0)


def _estimate_cost(
    *,
    length_km: float,
    voltage_kv: float,
    max_current_ka: float | None,
) -> float:
    if voltage_kv >= 220.0:
        unit_cost = 2.0
    else:
        unit_cost = 1.0
    current_factor = 1.0
    if max_current_ka is not None:
        current_factor = max(
            float(max_current_ka) / 10.0,
            0.5,
        )
    return float(length_km * unit_cost * current_factor)
