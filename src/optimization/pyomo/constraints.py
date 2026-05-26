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
# CONSTRAINT REGISTRY
# =========================================================

@dataclass(frozen=True)
class PyomoConstraintRegistry:
    """
    Runtime registry for executable Pyomo constraints.

    IMPORTANT:
    This layer stores executable equations only.

    It does NOT own:
    - engineering semantics
    - optimization intent
    - business meaning
    """

    budget_constraints: pyo.Constraint

    binary_constraints: pyo.Constraint


# =========================================================
# BUDGET CONSTRAINTS
# =========================================================

def build_budget_constraints(
    optimization_model: PyomoOptimizationModel,
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> pyo.Constraint:
    """
    Build executable budget constraints.

    Mathematical meaning:

        Σ(build_cost_i * x_i) <= total_budget

    IMPORTANT:
    This is executable encoding only.
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

    budget_limit = (
        problem.budget_constraint.max_budget
    )

    def budget_constraint_rule(model: pyo.ConcreteModel):

        total_expansion_cost = sum(
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

        return total_expansion_cost <= budget_limit

    return pyo.Constraint(
        rule=budget_constraint_rule
    )


# =========================================================
# BINARY CONSTRAINTS
# =========================================================

def build_binary_constraints(
    optimization_model: PyomoOptimizationModel,
) -> pyo.Constraint:
    """
    Build executable binary decision constraints.

    IMPORTANT:
    Pyomo binary domains already enforce this.

    This layer exists for:
    - explicit architecture
    - future extensibility
    - hybrid formulations later
    """

    model = optimization_model.model

    def binary_constraint_rule(
        model: pyo.ConcreteModel,
        variable_id: str,
    ):

        variable = (
            model.expansion_decision_variables[
                variable_id
            ]
        )

        return (
            0 <= variable,
            variable <= 1,
        )

    return pyo.Constraint(
        model.EXPANSION_DECISION_VARIABLES,
        rule=binary_constraint_rule,
    )


# =========================================================
# ATTACHMENT
# =========================================================

def attach_constraints_to_model(
    optimization_model: PyomoOptimizationModel,
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> PyomoConstraintRegistry:
    """
    Attach executable constraints to model.

    Canonical executable attachment point.
    """

    model = optimization_model.model

    model.budget_constraints = (
        build_budget_constraints(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    model.binary_constraints = (
        build_binary_constraints(
            optimization_model=optimization_model,
        )
    )

    return PyomoConstraintRegistry(
        budget_constraints=(
            model.budget_constraints
        ),
        binary_constraints=(
            model.binary_constraints
        ),
    )