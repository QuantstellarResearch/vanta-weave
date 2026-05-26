from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

import pyomo.environ as pyo

from pyomo.opt import SolverFactory
from pyomo.opt import SolverStatus
from pyomo.opt import TerminationCondition

from src.optimization.pyomo.builders import (
    PyomoExecutionArtifacts,
)


# =========================================================
# EXECUTION METADATA
# =========================================================

@dataclass(frozen=True)
class SolverExecutionMetadata:
    """
    Canonical optimization execution metadata.

    IMPORTANT:
    Runtime-only execution information.
    """

    solver_name: str

    solve_time_seconds: float

    solver_status: str

    termination_condition: str


# =========================================================
# NORMALIZED SOLUTION RESULT
# =========================================================

@dataclass(frozen=True)
class OptimizationSolveResult:
    """
    Canonical normalized optimization result.

    IMPORTANT:
    This layer normalizes:
    - solver outputs
    - execution results
    - selected infrastructure decisions

    Independent of:
    - Pyomo internals
    - solver-specific APIs
    """

    objective_value: float

    selected_candidate_ids: list[str]

    execution_metadata: SolverExecutionMetadata


# =========================================================
# VALIDATION
# =========================================================

def validate_solver_termination(
    results,
) -> None:
    """
    Validate solver execution status.
    """

    status = results.solver.status
    termination = (
        results.solver.termination_condition
    )

    if status != SolverStatus.ok:
        raise RuntimeError(
            f"Solver execution failed: {status}"
        )

    acceptable_terminations = {
        TerminationCondition.optimal,
        TerminationCondition.feasible,
    }

    if termination not in acceptable_terminations:
        raise RuntimeError(
            "Unexpected solver termination: "
            f"{termination}"
        )


# =========================================================
# EXTRACTION HELPERS
# =========================================================

def extract_selected_candidate_ids(
    execution_artifacts: PyomoExecutionArtifacts,
) -> list[str]:
    """
    Extract selected infrastructure expansion decisions.
    """

    model = (
        execution_artifacts
        .optimization_model
        .model
    )

    selected_candidate_ids = []

    for variable_id in (
        model.EXPANSION_DECISION_VARIABLES
    ):

        variable_value = pyo.value(
            model.expansion_decision_variables[
                variable_id
            ]
        )

        if variable_value >= 0.5:

            selected_candidate_ids.append(
                variable_id
            )

    return selected_candidate_ids


def extract_objective_value(
    execution_artifacts: PyomoExecutionArtifacts,
) -> float:
    """
    Extract normalized objective value.
    """

    model = (
        execution_artifacts
        .optimization_model
        .model
    )

    return float(
        pyo.value(
            model.total_objective
        )
    )


# =========================================================
# SOLVER EXECUTION
# =========================================================

def solve_with_highs(
    execution_artifacts: PyomoExecutionArtifacts,
) -> OptimizationSolveResult:
    """
    Execute optimization using HiGHS solver.

    Recommended default for:
    - E.ON challenge
    - QC4SG workflows
    - open-source reproducibility
    """

    model = (
        execution_artifacts
        .optimization_model
        .model
    )

    solver = SolverFactory("highs")

    start_time = perf_counter()

    results = solver.solve(
        model,
        tee=False,
    )

    end_time = perf_counter()

    validate_solver_termination(
        results=results,
    )

    execution_metadata = (
        SolverExecutionMetadata(
            solver_name="HiGHS",
            solve_time_seconds=(
                end_time - start_time
            ),
            solver_status=str(
                results.solver.status
            ),
            termination_condition=str(
                results.solver
                .termination_condition
            ),
        )
    )

    return OptimizationSolveResult(
        objective_value=(
            extract_objective_value(
                execution_artifacts
            )
        ),

        selected_candidate_ids=(
            extract_selected_candidate_ids(
                execution_artifacts
            )
        ),

        execution_metadata=execution_metadata,
    )


def solve_with_gurobi(
    execution_artifacts: PyomoExecutionArtifacts,
) -> OptimizationSolveResult:
    """
    Execute optimization using Gurobi solver.

    Recommended for:
    - larger MILP instances
    - benchmarking
    - advanced optimization studies
    """

    model = (
        execution_artifacts
        .optimization_model
        .model
    )

    solver = SolverFactory("gurobi")

    start_time = perf_counter()

    results = solver.solve(
        model,
        tee=False,
    )

    end_time = perf_counter()

    validate_solver_termination(
        results=results,
    )

    execution_metadata = (
        SolverExecutionMetadata(
            solver_name="Gurobi",
            solve_time_seconds=(
                end_time - start_time
            ),
            solver_status=str(
                results.solver.status
            ),
            termination_condition=str(
                results.solver
                .termination_condition
            ),
        )
    )

    return OptimizationSolveResult(
        objective_value=(
            extract_objective_value(
                execution_artifacts
            )
        ),

        selected_candidate_ids=(
            extract_selected_candidate_ids(
                execution_artifacts
            )
        ),

        execution_metadata=execution_metadata,
    )


def solve_with_cplex(
    execution_artifacts: PyomoExecutionArtifacts,
) -> OptimizationSolveResult:
    """
    Execute optimization using CPLEX solver.

    Recommended for:
    - commercial-grade MILP performance
    - large-scale benchmark runs
    """

    model = (
        execution_artifacts
        .optimization_model
        .model
    )

    solver = SolverFactory("cplex")

    start_time = perf_counter()

    results = solver.solve(
        model,
        tee=False,
    )

    end_time = perf_counter()

    validate_solver_termination(
        results=results,
    )

    execution_metadata = (
        SolverExecutionMetadata(
            solver_name="CPLEX",
            solve_time_seconds=(
                end_time - start_time
            ),
            solver_status=str(
                results.solver.status
            ),
            termination_condition=str(
                results.solver
                .termination_condition
            ),
        )
    )

    return OptimizationSolveResult(
        objective_value=(
            extract_objective_value(
                execution_artifacts
            )
        ),

        selected_candidate_ids=(
            extract_selected_candidate_ids(
                execution_artifacts
            )
        ),

        execution_metadata=execution_metadata,
    )


# =========================================================
# PUBLIC EXECUTION API
# =========================================================

def solve_optimization_problem(
    execution_artifacts: PyomoExecutionArtifacts,
    solver_name: str = "highs",
) -> OptimizationSolveResult:
    """
    Canonical public optimization execution API.

    Supports:
    - E.ON challenge workflows
    - QC4SG workflows
    - benchmark execution
    - future hybrid optimization workflows
    """

    normalized_solver_name = (
        solver_name.lower().strip()
    )

    if normalized_solver_name == "highs":
        return solve_with_highs(
            execution_artifacts
        )

    if normalized_solver_name == "gurobi":
        return solve_with_gurobi(
            execution_artifacts
        )

    if normalized_solver_name == "cplex":
        return solve_with_cplex(
            execution_artifacts
        )

    raise ValueError(
        f"Unsupported solver: {solver_name}"
    )
