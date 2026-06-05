from __future__ import annotations

from dataclasses import dataclass

import pyomo.environ as pyo

from problems.eon_grid_expansion.problem import (
    GridExpansionProblem,
)

from problems.eon_grid_expansion.formulation import (
    GridExpansionFormulation,
)

from src.optimization.pyomo.model import (
    PyomoOptimizationModel,
)


# =========================================================
# OBJECTIVE REGISTRY
# =========================================================

@dataclass(frozen=True)
class PyomoObjectiveRegistry:
    """
    Runtime registry for executable optimization objectives.

    IMPORTANT:
    This layer stores executable objective expressions only.

    It does NOT own:
    - optimization semantics
    - engineering meaning
    - business strategy
    """

    total_objective: pyo.Objective


# =========================================================
# EXPANSION COST OBJECTIVE
# =========================================================

def build_expansion_cost_expression(
    optimization_model: PyomoOptimizationModel,
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
):
    """
    Build executable expansion cost expression.

    Mathematical meaning:

        Σ(build_cost_i * x_i)
    """

    model = optimization_model.model

    candidate_line_map = {
        candidate.candidate_id: candidate
        for candidate in (
            problem.decision_space.candidate_lines
        )
    }

    variable_map = {
        variable.variable_id: variable
        for variable in formulation.decision_variables
    }

    return sum(
        candidate_line_map[
            variable_map[variable_id].candidate_id
        ].build_cost
        *
        model.expansion_decision_variables[
            variable_id
        ]

        for variable_id in (
            model.EXPANSION_DECISION_VARIABLES
        )
    )

# =========================================================
# CONGESTION REDUCTION OBJECTIVE
# =========================================================

def build_congestion_reduction_expression(
        optimization_model: PyomoOptimizationModel,
        problem: GridExpansionProblem,
        formulation: GridExpansionFormulation,
):
    model = optimization_model.model

    severity_map = (
        problem.analytics
        .overload_severity_reduction
    )

    variable_map = {
        variable.variable_id: variable
        for variable in formulation.decision_variables
    }

    return sum(

        severity_map[
            variable_map[
                variable_id
            ].candidate_id
        ]

        *

        model.expansion_decision_variables[
            variable_id
        ]

        for variable_id in (
            model.EXPANSION_DECISION_VARIABLES
        )
    )

# =========================================================
# MULTI-OBJECTIVE COMPOSITION
# =========================================================

def build_multi_objective_expression(
    optimization_model: PyomoOptimizationModel,
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
):
    """
    Build executable weighted multi-objective expression.

    Current strategy:
    - maximize congestion relief proxy
    - minimize infrastructure expansion cost

    IMPORTANT:
    This is intentionally:
    - linear
    - interpretable
    - MILP-friendly
    - QUBO-projectable later
    """

    congestion_weight = 1.0
    expansion_cost_weight = 0.05

    congestion_expression = (
        build_congestion_reduction_expression(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    expansion_cost_expression = (
        build_expansion_cost_expression(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    return (
        congestion_weight
        * congestion_expression
    ) - (
        expansion_cost_weight
        * expansion_cost_expression
    )


# =========================================================
# OBJECTIVE BUILDERS
# =========================================================

def build_total_objective(
    optimization_model: PyomoOptimizationModel,
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> pyo.Objective:
    """
    Build canonical executable optimization objective.
    """

    objective_expression = (
        build_multi_objective_expression(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    return pyo.Objective(
        expr=objective_expression,
        sense=pyo.maximize,
    )


# =========================================================
# ATTACHMENT
# =========================================================

def attach_objectives_to_model(
    optimization_model: PyomoOptimizationModel,
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> PyomoObjectiveRegistry:
    """
    Attach executable objectives to model.
    """

    model = optimization_model.model

    model.total_objective = (
        build_total_objective(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    return PyomoObjectiveRegistry(
        total_objective=model.total_objective
    )