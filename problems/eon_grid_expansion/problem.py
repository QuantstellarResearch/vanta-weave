"""
Canonical semantic composition for the E.ON grid expansion problem.

This module defines the root optimization problem abstraction
used throughout the Vanta Weave workflow.

IMPORTANT:
- This layer is semantic-only.
- No solver logic belongs here.
- No Pyomo/QUBO encoding belongs here.
- No runtime execution logic belongs here.
"""

from dataclasses import dataclass

from problems.eon_grid_expansion.metadata import ProblemMetadata
from problems.eon_grid_expansion.infrastructure import InfrastructureState
from problems.eon_grid_expansion.decision_space import DecisionSpace

from problems.eon_grid_expansion.constraints import (
    BudgetConstraint,
    ThermalLimitConstraint,
    VoltageLimitConstraint,
    TopologyConstraint,
    BinaryDecisionConstraint,
)
from problems.eon_grid_expansion.analytics import CandidateAnalytics

from problems.eon_grid_expansion.scenarios import ScenarioContext

from problems.eon_grid_expansion.objectives import MultiObjectiveDefinition


@dataclass(frozen=True)
class GridExpansionProblem:
    """
    Canonical semantic representation of the E.ON
    transmission grid expansion optimization problem.

    This abstraction composes:
    - operational infrastructure state
    - candidate expansion decisions
    - engineering constraints
    - future operating scenarios
    - optimization objectives

    IMPORTANT:
    This class is semantic-only and execution-free.
    """

    metadata: ProblemMetadata

    infrastructure: InfrastructureState

    decision_space: DecisionSpace

    budget_constraint: BudgetConstraint
    thermal_constraint: ThermalLimitConstraint
    voltage_constraint: VoltageLimitConstraint
    topology_constraint: TopologyConstraint
    binary_constraint: BinaryDecisionConstraint

    scenario: ScenarioContext

    objectives: MultiObjectiveDefinition

    analytics: CandidateAnalytics