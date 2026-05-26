"""
Semantic constraint definitions for the E.ON grid expansion problem.

This module defines declarative engineering and operational constraints
used by the GridExpansionProblem abstraction.

IMPORTANT:
- This layer is semantic-only.
- No solver-specific logic belongs here.
- No Pyomo/QUBO/quantum execution logic belongs here.
- Mathematical encoding is handled in formulation/execution layers.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BudgetConstraint:
    """
    Limits the total investment cost allowed for grid expansion.

    This constraint represents the economic planning boundary
    for candidate line construction.
    """

    max_budget: float


@dataclass(frozen=True)
class ThermalLimitConstraint:
    """
    Enforces thermal operating limits on transmission lines.

    This represents congestion and thermal rating boundaries
    used during optimization and power flow evaluation.
    """

    enabled: bool = True


@dataclass(frozen=True)
class VoltageLimitConstraint:
    """
    Enforces operational voltage boundaries across buses.

    Voltage stability and operational feasibility constraints
    may later be projected into optimization formulations.
    """

    min_voltage_pu: float = 0.95
    max_voltage_pu: float = 1.05


@dataclass(frozen=True)
class TopologyConstraint:
    """
    Represents topology-level validity requirements.

    This may include:
    - connectivity preservation
    - operational compatibility
    - valid network expansion structure
    """

    enforce_connectivity: bool = True


@dataclass(frozen=True)
class BinaryDecisionConstraint:
    """
    Declares that candidate expansion decisions are binary.

    IMPORTANT:
    This class does NOT encode binary variables mathematically.
    It only expresses the semantic requirement that candidate
    lines are either built or not built.
    """

    enabled: bool = True