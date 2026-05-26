from __future__ import annotations

from dataclasses import dataclass

import pyomo.environ as pyo

from problems.eon_grid_expansion.formulation import (
    GridExpansionFormulation,
)

from problems.eon_grid_expansion.problem import (
    GridExpansionProblem,
)

from src.optimization.pyomo.variables import (
    PyomoVariableRegistry,
    attach_decision_variables_to_model,
)


# =========================================================
# EXECUTABLE MODEL CONTAINER
# =========================================================

@dataclass(frozen=True)
class PyomoOptimizationModel:
    """
    Canonical executable optimization container.

    IMPORTANT:
    This object wraps:
    - executable model
    - runtime registries
    - optimization context

    This is NOT:
    - semantic layer
    - formulation layer
    - result layer
    """

    model: pyo.ConcreteModel

    variable_registry: PyomoVariableRegistry


# =========================================================
# MODEL INITIALIZATION
# =========================================================

def create_concrete_model() -> pyo.ConcreteModel:
    """
    Create canonical executable Pyomo model.

    Centralized creation point for:
    - runtime consistency
    - future instrumentation
    - debugging
    - execution orchestration
    """

    return pyo.ConcreteModel()


def initialize_model_metadata(
    model: pyo.ConcreteModel,
    problem: GridExpansionProblem,
) -> None:
    """
    Attach runtime-readable metadata.

    IMPORTANT:
    Metadata is attached for:
    - debugging
    - explainability
    - analytics
    - execution tracing

    NOT for semantic ownership.
    """

    model.problem_id = problem.metadata.problem_id
    model.problem_name = problem.metadata.name

    model.dataset_name = problem.metadata.dataset_name
    model.scenario_id = problem.metadata.scenario_id


def initialize_model_sets(
    model: pyo.ConcreteModel,
    formulation: GridExpansionFormulation,
) -> None:
    """
    Initialize executable Pyomo index sets.

    IMPORTANT:
    Sets are executable indexing structures,
    not semantic domain models.
    """

    variable_ids = [
        variable.variable_id
        for variable in formulation.decision_variables
    ]

    model.EXPANSION_DECISION_VARIABLES = pyo.Set(
        initialize=variable_ids,
        ordered=True,
    )


# =========================================================
# VARIABLE ATTACHMENT
# =========================================================

def attach_variable_registry(
    model: pyo.ConcreteModel,
    formulation: GridExpansionFormulation,
) -> PyomoVariableRegistry:
    """
    Attach executable variable registry to model.
    """

    return attach_decision_variables_to_model(
        model=model,
        decision_variables=formulation.decision_variables,
    )


# =========================================================
# COMPOSITION ROOT
# =========================================================

def build_empty_model(
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> PyomoOptimizationModel:
    """
    Build canonical executable optimization model.

    IMPORTANT:
    This function ONLY builds:
    - executable container
    - executable sets
    - executable variables

    It does NOT build:
    - objectives
    - constraints
    - solve logic

    Those belong downstream.
    """

    model = create_concrete_model()

    initialize_model_metadata(
        model=model,
        problem=problem,
    )

    initialize_model_sets(
        model=model,
        formulation=formulation,
    )

    variable_registry = attach_variable_registry(
        model=model,
        formulation=formulation,
    )

    return PyomoOptimizationModel(
        model=model,
        variable_registry=variable_registry,
    )