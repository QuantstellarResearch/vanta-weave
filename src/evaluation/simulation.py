from __future__ import annotations

import copy

import pandapower as pp

from problems.eon_grid_expansion.decision_space import (
    CandidateLine,
)

from vanta_lattice.domains.energy.models import (
    LineEdge,
    LineFlow,
)


# =========================================================
# PUBLIC API
# =========================================================

def simulate_candidate(
    *,
    net,
    candidate: CandidateLine,
    reference_lines: list[LineEdge],
) -> list[LineFlow]:
    """
    Simulate a single candidate expansion.

    Workflow

        CandidateLine
                ↓
        Reference Line
                ↓
        Materialization
                ↓
        DC Power Flow
                ↓
        LineFlow Results

    Notes
    -----
    This layer evaluates a candidate using
    physical parameters inherited from a
    reference transmission asset.

    CandidateLine itself is NOT a physical
    line model.
    """

    working_net = _clone_network(net)

    from_bus_idx, to_bus_idx = (
        _resolve_bus_indices(
            candidate=candidate,
        )
    )

    reference_line = (
        _find_reference_line(
            candidate=candidate,
            reference_lines=reference_lines,
        )
    )

    _materialize_candidate_line(
        net=working_net,
        candidate=candidate,
        reference_line=reference_line,
        from_bus_idx=from_bus_idx,
        to_bus_idx=to_bus_idx,
    )

    _run_powerflow(
        working_net,
    )

    return _extract_line_flows(
        working_net,
    )


# =========================================================
# NETWORK HELPERS
# =========================================================

def _clone_network(net):
    """
    Create isolated simulation copy.
    """

    return copy.deepcopy(net)


def _resolve_bus_indices(
    *,
    candidate: CandidateLine,
) -> tuple[int, int]:
    """
    IEEE118 invariant:

        BusNode.id
            ==
        pandapower bus index
    """

    return (
        int(candidate.from_bus),
        int(candidate.to_bus),
    )


# =========================================================
# REFERENCE ASSET
# =========================================================

def _find_reference_line(
    *,
    candidate: CandidateLine,
    reference_lines: list[LineEdge],
) -> LineEdge:
    """
    Resolve physical asset reference.

    Reference assignment happens during
    candidate generation.

    Simulation must never attempt to
    re-discover a reference line.
    """

    lookup = {
        int(line.id): line
        for line in reference_lines
        if line.id is not None
    }

    try:
        return lookup[
            int(candidate.reference_line_id)
        ]

    except KeyError as exc:
        raise ValueError(
            f"Reference line "
            f"{candidate.reference_line_id} "
            f"not found."
        ) from exc


# =========================================================
# MATERIALIZATION
# =========================================================

def _materialize_candidate_line(
    *,
    net,
    candidate: CandidateLine,
    reference_line: LineEdge,
    from_bus_idx: int,
    to_bus_idx: int,
) -> None:
    """
    Materialize CandidateLine into
    a physical pandapower line.

    Physical parameters are inherited
    from the reference asset.
    """

    if (
        reference_line.resistance_ohm_per_km
        is None
    ):
        raise ValueError(
            "Reference line missing resistance."
        )

    if (
        reference_line.reactance_ohm_per_km
        is None
    ):
        raise ValueError(
            "Reference line missing reactance."
        )

    if (
        reference_line.max_current_ka
        is None
    ):
        raise ValueError(
            "Reference line missing current rating."
        )

    pp.create_line_from_parameters(
        net,

        from_bus=from_bus_idx,
        to_bus=to_bus_idx,

        length_km=float(
            candidate.length_km
        ),

        r_ohm_per_km=float(
            reference_line
            .resistance_ohm_per_km
        ),

        x_ohm_per_km=float(
            reference_line
            .reactance_ohm_per_km
        ),

        max_i_ka=float(
            reference_line
            .max_current_ka
        ),

        c_nf_per_km=0.0,

        name=candidate.candidate_id,
    )


# =========================================================
# POWER FLOW
# =========================================================

def _run_powerflow(
    net,
) -> None:
    """
    Candidate evaluation path.

    Current:
        DC Power Flow

    Future:
        AC Benchmark Validation
    """

    pp.rundcpp(net)


# =========================================================
# RESULT EXTRACTION
# =========================================================

def _extract_line_flows(
    net,
) -> list[LineFlow]:
    """
    Convert pandapower results into
    canonical LineFlow objects.

    Notes
    -----
    DC power flow does not provide:

        - reactive power
        - bus voltages
        - line currents

    These fields will be populated
    during AC benchmark validation.
    """

    line_table = net.line
    result_table = net.res_line

    line_flows: list[LineFlow] = []

    for line_id in result_table.index:

        line_row = line_table.loc[line_id]
        result_row = result_table.loc[line_id]

        line_flows.append(
            LineFlow(
                source="pandapower",

                component_type="line_flow",

                line_id=int(line_id),

                from_bus=int(
                    line_row["from_bus"]
                ),

                to_bus=int(
                    line_row["to_bus"]
                ),

                active_power_from_mw=float(
                    result_row["p_from_mw"]
                ),

                reactive_power_from_mvar=0.0,

                active_power_to_mw=float(
                    result_row["p_to_mw"]
                ),

                reactive_power_to_mvar=0.0,

                loading_percent=float(
                    result_row[
                        "loading_percent"
                    ]
                ),

                current_ka=0.0,

                current_from_ka=0.0,

                current_to_ka=0.0,

                voltage_from_pu=1.0,

                voltage_to_pu=1.0,

                power_loss_mw=float(
                    result_row.get(
                        "pl_mw",
                        0.0,
                    )
                ),

                reactive_power_loss_mvar=0.0,
            )
        )

    return line_flows


# =========================================================
# LOCAL TEST
# =========================================================

if __name__ == "__main__":

    from datasets.load_ieee118 import (
        load_data,
    )

    from workflows.generate_candidates import (
        CandidateGenerationConfig,
        generate_candidates,
    )

    data = load_data()

    candidates = generate_candidates(
        data=data,
        config=CandidateGenerationConfig(),
    )

    candidate = candidates[0]

    flows = simulate_candidate(
        net=data.raw_net,
        candidate=candidate,
        reference_lines=data.mapped["lines"],
    )

    print(flows[-1])