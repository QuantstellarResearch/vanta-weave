"""
Optimization objective semantics for the E.ON grid expansion problem.

This module defines declarative optimization goals used by the
GridExpansionProblem abstraction.

IMPORTANT:
- This layer is semantic-only.
- No Pyomo/QUBO expressions belong here.
- No solver-specific logic belongs here.
- Mathematical encoding is handled in formulation layers.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CongestionReductionObjective:
    """
    Represents the intent to reduce network congestion
    and transmission overload stress.
    """

    weight: float = 1.0


@dataclass(frozen=True)
class ExpansionCostObjective:
    """
    Represents the intent to minimize infrastructure
    expansion investment cost.
    """

    weight: float = 1.0


@dataclass(frozen=True)
class MultiObjectiveDefinition:
    """
    Declarative composition of optimization objectives.

    This structure defines the relative importance of
    congestion reduction and expansion cost minimization.
    """

    congestion_reduction: CongestionReductionObjective
    expansion_cost: ExpansionCostObjective