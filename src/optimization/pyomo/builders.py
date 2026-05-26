from __future__ import annotations

from dataclasses import dataclass

from problems.eon_grid_expansion.problem import (
    GridExpansionProblem,
)

from problems.eon_grid_expansion.formulation import (
    GridExpansionFormulation,
)

from src.optimization.pyomo.model import (
    PyomoOptimizationModel,
    build_empty_model,
)

from src.optimization.pyomo.constraints import (
    PyomoConstraintRegistry,
    attach_constraints_to_model,
)

from src.optimization.pyomo.objectives import (
    PyomoObjectiveRegistry,
    attach_objectives_to_model,
)


# =========================================================
# EXECUTION ARTIFACTS
# =========================================================

@dataclass(frozen=True)
class PyomoExecutionArtifacts:
    """
    Canonical executable optimization runtime artifacts.

    IMPORTANT:
    This object represents:
    - executable runtime state
    - assembly outputs
    - execution-ready optimization system

    NOT:
    - semantic ownership
    - engineering meaning
    """

    optimization_model: PyomoOptimizationModel

    constraint_registry: PyomoConstraintRegistry

    objective_registry: PyomoObjectiveRegistry


# =========================================================
# VALIDATION
# =========================================================

def validate_variable_alignment(
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> None:
    """
    Validate formulation variable alignment.

    Ensures:
    - all formulation variables map correctly
    - candidate references exist
    - executable projection consistency
    """

    candidate_ids = {
        candidate.candidate_id
        for candidate in (
            problem.decision_space.candidate_lines
        )
    }

    formulation_candidate_ids = {
        variable.candidate_id
        for variable in (
            formulation.decision_variables
        )
    }

    missing_candidates = (
        formulation_candidate_ids
        - candidate_ids
    )

    if missing_candidates:
        raise ValueError(
            "Formulation references unknown "
            f"candidate lines: "
            f"{sorted(missing_candidates)}"
        )


def validate_formulation_consistency(
    formulation: GridExpansionFormulation,
) -> None:
    """
    Validate executable formulation consistency.
    """

    variable_ids = [
        variable.variable_id
        for variable in (
            formulation.decision_variables
        )
    ]

    duplicate_variable_ids = {
        variable_id
        for variable_id in variable_ids
        if variable_ids.count(variable_id) > 1
    }

    if duplicate_variable_ids:
        raise ValueError(
            "Duplicate executable variable IDs "
            f"detected: "
            f"{sorted(duplicate_variable_ids)}"
        )


# =========================================================
# EXECUTION BUILD PIPELINE
# =========================================================

def build_executable_runtime(
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> PyomoExecutionArtifacts:
    """
    Build canonical executable optimization runtime.

    Assembly order:

        validation
            ↓
        model creation
            ↓
        variable attachment
            ↓
        constraint attachment
            ↓
        objective attachment

    IMPORTANT:
    This is:
    - deterministic
    - explicit
    - infrastructure-grade
    """

    validate_variable_alignment(
        problem=problem,
        formulation=formulation,
    )

    validate_formulation_consistency(
        formulation=formulation,
    )

    optimization_model = build_empty_model(
        problem=problem,
        formulation=formulation,
    )

    constraint_registry = (
        attach_constraints_to_model(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    objective_registry = (
        attach_objectives_to_model(
            optimization_model=optimization_model,
            problem=problem,
            formulation=formulation,
        )
    )

    return PyomoExecutionArtifacts(
        optimization_model=optimization_model,
        constraint_registry=constraint_registry,
        objective_registry=objective_registry,
    )


# =========================================================
# PUBLIC ENTRYPOINT
# =========================================================

def build_pyomo_model(
    problem: GridExpansionProblem,
    formulation: GridExpansionFormulation,
) -> PyomoExecutionArtifacts:
    """
    Canonical public entrypoint for executable
    optimization model construction.

    This is the official executable assembly API
    for:
    - MILP workflows
    - E.ON challenge execution
    - QC4SG workflows
    - future hybrid quantum pipelines
    """

    return build_executable_runtime(
        problem=problem,
        formulation=formulation,
    )