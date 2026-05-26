"""
Mathematical formulation abstractions for the E.ON
grid expansion optimization problem.

This module defines canonical mathematical optimization
projections derived from semantic problem definitions.

IMPORTANT:
- This layer is mathematical-only.
- No solver-specific logic belongs here.
- No Pyomo/QUBO execution logic belongs here.
- No runtime execution belongs here.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExpansionDecisionVariable:
    """
    Canonical binary decision variable representing
    whether a candidate transmission line is built.

    Semantic meaning:
        x_i ∈ {0,1}
    """

    variable_id: str

    candidate_id: str

    binary: bool = True


@dataclass(frozen=True)
class ObjectiveFormulation:
    """
    Mathematical optimization objective configuration.

    This structure defines which optimization objectives
    are included in the projected optimization problem.
    """

    minimize_congestion: bool = True

    minimize_expansion_cost: bool = True


@dataclass(frozen=True)
class ConstraintFormulation:
    """
    Mathematical constraint configuration for the
    projected optimization problem.
    """

    enforce_budget_constraint: bool = True

    enforce_thermal_limits: bool = True

    enforce_voltage_limits: bool = True

    enforce_topology_constraints: bool = True

    enforce_binary_decisions: bool = True


@dataclass(frozen=True)
class GridExpansionFormulation:
    """
    Canonical mathematical optimization formulation
    for the E.ON grid expansion problem.

    This abstraction represents the mathematical
    optimization structure projected from the semantic
    GridExpansionProblem definition.
    """

    decision_variables: list[ExpansionDecisionVariable]

    objectives: ObjectiveFormulation

    constraints: ConstraintFormulation