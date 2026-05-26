from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import pyomo.environ as pyo

from problems.eon_grid_expansion.formulation import (
    ExpansionDecisionVariable,
)


# =========================================================
# VARIABLE REGISTRY
# =========================================================

@dataclass(frozen=True)
class PyomoVariableRegistry:
    """
    Runtime registry for executable Pyomo variables.

    IMPORTANT:
    This layer is executable/runtime-only.

    It does NOT own:
    - optimization semantics
    - engineering meaning
    - domain logic

    It only stores references to executable Pyomo variables.
    """

    expansion_decision_variables: pyo.Var


# =========================================================
# INTERNAL HELPERS
# =========================================================

def build_binary_variable_domain() -> pyo.Binary:
    """
    Returns the executable Pyomo binary domain.

    Centralized for:
    - readability
    - future extensibility
    - hybrid variable support later
    """

    return pyo.Binary


def extract_variable_ids(
    decision_variables: Iterable[ExpansionDecisionVariable],
) -> list[str]:
    """
    Extract stable executable variable IDs.

    Example:
        expansion_candidate_line_001
        expansion_candidate_line_002
    """

    return [
        variable.variable_id
        for variable in decision_variables
    ]


# =========================================================
# VARIABLE BUILDERS
# =========================================================

def build_expansion_decision_variables(
    model: pyo.ConcreteModel,
    decision_variables: Iterable[ExpansionDecisionVariable],
) -> pyo.Var:
    """
    Build executable binary expansion variables.

    Semantic mapping:
        ExpansionDecisionVariable
            ->
        Pyomo executable variable

    IMPORTANT:
    This layer is runtime-only.

    No:
    - congestion logic
    - topology logic
    - engineering constraints
    - objective semantics
    """

    variable_ids = extract_variable_ids(
        decision_variables=decision_variables,
    )

    return pyo.Var(
        variable_ids,
        domain=build_binary_variable_domain(),
        initialize=0,
    )


def attach_decision_variables_to_model(
    model: pyo.ConcreteModel,
    decision_variables: Iterable[ExpansionDecisionVariable],
) -> PyomoVariableRegistry:
    """
    Attach executable decision variables to model.

    Canonical attachment point for:
    - builders.py
    - constraints.py
    - objectives.py
    """

    model.expansion_decision_variables = (
        build_expansion_decision_variables(
            model=model,
            decision_variables=decision_variables,
        )
    )

    return PyomoVariableRegistry(
        expansion_decision_variables=(
            model.expansion_decision_variables
        )
    )