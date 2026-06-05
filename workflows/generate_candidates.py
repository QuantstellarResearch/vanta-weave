from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterable

from problems.eon_grid_expansion.decision_space import (
    CandidateLine,
    DecisionSpace,
)

from src.utils.candidate_ids import (
    make_candidate_id,
    canonical_base_key,
    sort_key_for_variant,
)
import json
from pathlib import Path

from src.utils.distance_length import tinh_khoang_cach_bus


@dataclass(frozen=True)
class CandidateGenerationConfig:
    overload_threshold: float = 70.0
    planning_stress_factor: float = 30.0

    parallel_capacity_scale: float = 1.2

    top_k_buses: int = 10

    top_congested_lines: int = 10
    relief_neighbors_per_side: int = 2

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

    # Collect raw candidate dicts from multiple generators
    raw_candidates: list[dict] = []

    raw_candidates.extend(
        [
            {
                "kind": "parallel",
                "from_bus": str(c.from_bus),
                "to_bus": str(c.to_bus),
                "build_cost": c.build_cost,
                "length_km": c.length_km,
                "reference_line_id": c.reference_line_id,
            }
            for c in _build_parallel_candidates(
                line_flows=line_flows,
                line_by_id=line_by_id,
                bus_voltage_by_id=bus_voltage_by_id,
                existing_edges=existing_edges,
                config=config,
            )
        ]
    )

    if len(raw_candidates) < config.max_candidates:
        raw_candidates.extend(
            [
                {
                    "kind": "shortcut",
                    "from_bus": str(c.from_bus),
                    "to_bus": str(c.to_bus),
                    "build_cost": c.build_cost,
                    "length_km": c.length_km,
                    "reference_line_id": c.reference_line_id,
                }
                for c in _build_shortcut_candidates(
                    data=data,
                    loads=loads,
                    generators=generators,
                    buses=buses,
                    lines=lines,
                    bus_voltage_by_id=bus_voltage_by_id,
                    existing_edges=existing_edges,
                    config=config,
                    remaining=(
                        config.max_candidates
                        - len(raw_candidates)
                    ),
                )
            ]
        )

    if len(raw_candidates) < config.max_candidates:
        raw_candidates.extend(
            [
                {
                    "kind": "relief",
                    "from_bus": str(c.from_bus),
                    "to_bus": str(c.to_bus),
                    "build_cost": c.build_cost,
                    "length_km": c.length_km,
                    "reference_line_id": c.reference_line_id,
                }
                for c in _build_congestion_relief_candidates(
                data=data,
                line_flows=line_flows,
                lines=lines,
                bus_voltage_by_id=bus_voltage_by_id,
                existing_edges=existing_edges,
                config=config,
                remaining=(
                        config.max_candidates
                        - len(raw_candidates)
                ),
            )
            ]
        )

    # Group by canonical base key to deduplicate and prepare variant lists
    groups: dict = {}
    for item in raw_candidates:
        key = canonical_base_key(
            item["kind"],
            item["from_bus"],
            item["to_bus"],
            item["reference_line_id"],
            item["build_cost"],
        )
        groups.setdefault(key, []).append(item)

    # For each group, sort variants deterministically and assign variant indices
    canonical_candidates: list[CandidateLine] = []
    for key, variants in groups.items():
        variants_sorted = sorted(variants, key=sort_key_for_variant)
        for idx, var in enumerate(variants_sorted):
            candidate_id = make_candidate_id(
                kind=var["kind"],
                from_bus=var["from_bus"],
                to_bus=var["to_bus"],
                reference_line_id=var["reference_line_id"],
                build_cost=var["build_cost"],
                length_km=var.get("length_km"),
                variant_index=(idx if len(variants_sorted) > 1 else None),
                add_hash=True,
            )

            canonical_candidates.append(
                CandidateLine(
                    candidate_id=candidate_id,
                    from_bus=var["from_bus"],
                    to_bus=var["to_bus"],
                    build_cost=var["build_cost"],
                    length_km=var["length_km"],
                    reference_line_id=var["reference_line_id"],
                )
            )

    # Keep deterministic order: sort by candidate_id
    canonical_candidates = sorted(canonical_candidates, key=lambda c: c.candidate_id)

    # Trim to max_candidates
    final = canonical_candidates[: config.max_candidates]

    return final


def write_candidate_list(
    candidates: list[CandidateLine],
    output_path: Path = Path("outputs/candidate_list.json"),
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "generator": "generate_candidates",
        "count": len(candidates),
        "candidates": [
            {
                "candidate_id": c.candidate_id,
                "from_bus": c.from_bus,
                "to_bus": c.to_bus,
                "build_cost": c.build_cost,
                "length_km": c.length_km,
            }
            for c in candidates
        ],
    }

    output_path.write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )


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

def _build_bus_lookup(
    buses,
) -> dict[int, object]:

    return {
        int(bus.id): bus
        for bus in buses
        if bus.id is not None
    }


def _build_line_lookup(
    lines,
) -> dict[int, object]:

    return {
        int(line.id): line
        for line in lines
        if line.id is not None
    }


def _assign_parallel_reference_line(
    line,
) -> int:

    if line.id is None:
        raise ValueError(
            "Parallel candidate requires "
            "a valid line id."
        )

    return int(line.id)


def _assign_relief_reference_line(
    flow,
) -> int:

    return int(flow.line_id)


def _assign_shortcut_reference_line(
    *,
    buses,
    lines,
    from_bus: int,
    to_bus: int,
) -> int:

    bus_lookup = _build_bus_lookup(
        buses
    )

    target_voltage = max(
        float(
            bus_lookup[from_bus]
            .voltage_kv
        ),
        float(
            bus_lookup[to_bus]
            .voltage_kv
        ),
    )

    best_line = None
    best_score = float("inf")

    for line in lines:

        if (
            line.from_bus is None
            or line.to_bus is None
        ):
            continue

        from_voltage = float(
            bus_lookup[
                line.from_bus
            ].voltage_kv
        )

        to_voltage = float(
            bus_lookup[
                line.to_bus
            ].voltage_kv
        )

        line_voltage = max(
            from_voltage,
            to_voltage,
        )

        score = abs(
            line_voltage
            - target_voltage
        )

        if score < best_score:

            best_score = score
            best_line = line

    if best_line is None:
        raise ValueError(
            "Unable to find "
            "reference line."
        )

    return int(best_line.id)


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
        effective_loading = (
                flow.loading_percent
                * config.planning_stress_factor
        )
        if effective_loading < config.overload_threshold:
            continue

        line = line_by_id.get(flow.line_id)
        if line is None:
            continue

        from_bus = line.from_bus
        to_bus = line.to_bus

        if (from_bus, to_bus) not in existing_edges:
            existing_edges.add((from_bus, to_bus))

        reference_line_id = (
            _assign_parallel_reference_line(
                line
            )
        )

        length_km = getattr(line, "length_km", 1.0)

        voltage_kv = max(
            float(bus_voltage_by_id[from_bus]),
            float(bus_voltage_by_id[to_bus]),
        )

        build_cost = _estimate_cost(
            length_km=length_km,
            voltage_kv=voltage_kv,
            max_current_ka=getattr(
                line, "max_current_ka", None
            ),
        )

        # Note: candidate_id generation is deferred to top-level to ensure deterministic ids
        candidates.append(
            CandidateLine(
                candidate_id="",
                from_bus=from_bus,
                to_bus=to_bus,
                reference_line_id=
                    reference_line_id,
                build_cost=build_cost,
                length_km=length_km,
            )
        )

    return candidates


def _build_shortcut_candidates(
    *,
    data,
    buses,
    lines,
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

        reference_line_id = (
            _assign_shortcut_reference_line(
                buses=buses,
                lines=lines,
                from_bus=from_bus,
                to_bus=to_bus,
            )
        )
        length_km = tinh_khoang_cach_bus(data, from_bus, to_bus)
        if length_km is None:
            length_km = 1.0

        reference_line = next(
            line
            for line in lines
            if line.id
            == reference_line_id
        )

        reference_voltage = (
            _get_reference_voltage(
                reference_line=reference_line,
                bus_voltage_by_id=
                bus_voltage_by_id,
            )
        )

        build_cost = _estimate_cost(
            length_km=length_km,
            voltage_kv=reference_voltage,
            max_current_ka=None,
        )

        candidates.append(
            CandidateLine(
                candidate_id="",
                from_bus=from_bus,
                to_bus=to_bus,
                reference_line_id=
                    reference_line_id,
                build_cost=build_cost,
                length_km=length_km,
            )
        )

    return candidates

def _build_congestion_relief_candidates(
    *,
    data,
    line_flows,
    lines,
    bus_voltage_by_id,
    existing_edges,
    config: CandidateGenerationConfig,
    remaining: int,
) -> list[CandidateLine]:

    candidates: list[CandidateLine] = []

    adjacency = _build_bus_adjacency(lines)

    congested_flows = sorted(
        line_flows,
        key=lambda flow: (
            flow.loading_percent
            * config.planning_stress_factor
        ),
        reverse=True,
    )[: config.top_congested_lines]

    for flow in congested_flows:

        if len(candidates) >= remaining:
            break

        from_bus = int(flow.from_bus)
        to_bus = int(flow.to_bus)

        from_neighbors = list(
            adjacency.get(from_bus, set())
        )[: config.relief_neighbors_per_side]

        to_neighbors = list(
            adjacency.get(to_bus, set())
        )[: config.relief_neighbors_per_side]

        for left_bus in from_neighbors:
            for right_bus in to_neighbors:

                if len(candidates) >= remaining:
                    break

                if left_bus == right_bus:
                    continue

                if (
                    left_bus,
                    right_bus,
                ) in existing_edges:
                    continue

                reference_line_id = (
                    _assign_relief_reference_line(
                        flow
                    )
                )

                length_km = (
                    tinh_khoang_cach_bus(
                        data,
                        left_bus,
                        right_bus,
                    )
                )

                if length_km is None:
                    length_km = 1.0

                reference_line = next(
                    line
                    for line in lines
                    if line.id
                    == reference_line_id
                )

                reference_voltage = (
                    _get_reference_voltage(
                        reference_line=reference_line,
                        bus_voltage_by_id=
                        bus_voltage_by_id,
                    )
                )

                build_cost = (
                    _estimate_cost(
                        length_km=length_km,
                        voltage_kv=reference_voltage,
                        max_current_ka=None,
                    )
                )

                existing_edges.add(
                    (left_bus, right_bus)
                )
                existing_edges.add(
                    (right_bus, left_bus)
                )

                candidates.append(
                    CandidateLine(
                        candidate_id="",
                        from_bus=left_bus,
                        to_bus=right_bus,
                        reference_line_id=
                            reference_line_id,
                        build_cost=build_cost,
                        length_km=length_km,
                    )
                )

    return candidates


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


def _build_bus_adjacency(lines) -> dict[int, set[int]]:
    adjacency: dict[int, set[int]] = {}

    for line in lines:
        adjacency.setdefault(
            line.from_bus,
            set(),
        ).add(line.to_bus)

        adjacency.setdefault(
            line.to_bus,
            set(),
        ).add(line.from_bus)

    return adjacency


def _get_reference_voltage(
    *,
    reference_line,
    bus_voltage_by_id,
) -> float:

    return max(
        bus_voltage_by_id[
            reference_line.from_bus
        ],
        bus_voltage_by_id[
            reference_line.to_bus
        ],
    )

