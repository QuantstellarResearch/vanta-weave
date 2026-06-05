from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


# =========================================================
# SELECTED INFRASTRUCTURE DECISION
# =========================================================

@dataclass(frozen=True)
class SelectedExpansionDecision:

    candidate_id: str

    from_bus: str
    to_bus: str

    reference_line_id: int

    build_cost: float

    decision_score: float


# =========================================================
# INFRASTRUCTURE EXPANSION PLAN
# =========================================================

@dataclass(frozen=True)
class InfrastructureExpansionPlan:
    """
    Canonical infrastructure expansion plan.

    Represents:
    - selected expansion portfolio
    - executable infrastructure recommendations
    """

    selected_expansions: list[
        SelectedExpansionDecision
    ]

    total_expansion_cost: float

    total_added_capacity_mva: float


# =========================================================
# EXECUTION SUMMARY
# =========================================================

@dataclass(frozen=True)
class OptimizationExecutionSummary:
    """
    Canonical optimization execution summary.
    """

    solver_name: str

    objective_value: float

    solve_time_seconds: float

    termination_condition: str


# =========================================================
# CANONICAL SOLUTION
# =========================================================

@dataclass(frozen=True)
class OptimizationSolution:
    """
    Canonical optimization solution artifact.

    IMPORTANT:
    This layer represents:
    - infrastructure optimization outcome
    - decision intelligence
    - execution summary
    - operational recommendation set

    NOT:
    - raw solver output
    - Pyomo internals
    - solver-specific structures
    """

    problem_id: str

    scenario_id: str

    generated_at: datetime

    expansion_plan: (
        InfrastructureExpansionPlan
    )

    execution_summary: (
        OptimizationExecutionSummary
    )