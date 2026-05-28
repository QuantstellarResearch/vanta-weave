from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from problems.eon_grid_expansion.constraints import (
    BudgetConstraint,
    BinaryDecisionConstraint,
    ThermalLimitConstraint,
    TopologyConstraint,
    VoltageLimitConstraint,
)
from problems.eon_grid_expansion.decision_space import (
    CandidateLine,
    DecisionSpace,
)
from problems.eon_grid_expansion.formulation import (
    ConstraintFormulation,
    ExpansionDecisionVariable,
    GridExpansionFormulation,
    ObjectiveFormulation,
)
from problems.eon_grid_expansion.infrastructure import (
    InfrastructureState,
)
from problems.eon_grid_expansion.metadata import (
    ProblemMetadata,
)
from problems.eon_grid_expansion.objectives import (
    CongestionReductionObjective,
    ExpansionCostObjective,
    MultiObjectiveDefinition,
)
from problems.eon_grid_expansion.problem import (
    GridExpansionProblem,
)
from problems.eon_grid_expansion.scenarios import (
    ScenarioContext,
)
from src.optimization.pyomo.builders import (
    build_pyomo_model,
)
from src.solvers.classical.solve import (
    OptimizationSolveResult,
    solve_optimization_problem,
)


@dataclass(frozen=True)
class OptimizationRunConfig:
    solver_name: str = "highs"
    budget_ratio: float = 0.15
    scenario_id: str = "baseline"
    scenario_name: str = "Baseline"
    stress_level: float = 1.0


def run_optimization(
    *,
    data,
    candidates: list[CandidateLine],
    config: OptimizationRunConfig | None = None,
) -> OptimizationSolveResult:
    """
    Build and solve the grid expansion optimization
    problem using a default CPLEX solver.
    """

    config = config or OptimizationRunConfig()

    budget = _estimate_budget(
        candidates=candidates,
        budget_ratio=config.budget_ratio,
    )

    problem = _build_problem(
        data=data,
        candidates=candidates,
        budget=budget,
        config=config,
    )

    formulation = _build_formulation(
        candidates=candidates,
    )

    execution_artifacts = build_pyomo_model(
        problem=problem,
        formulation=formulation,
    )

    return solve_optimization_problem(
        execution_artifacts=execution_artifacts,
        solver_name=config.solver_name,
    )


def _estimate_budget(
    *,
    candidates: list[CandidateLine],
    budget_ratio: float,
) -> float:
    total_cost = sum(
        candidate.build_cost
        for candidate in candidates
    )
    return float(total_cost * budget_ratio)


def _build_problem(
    *,
    data,
    candidates: list[CandidateLine],
    budget: float,
    config: OptimizationRunConfig,
) -> GridExpansionProblem:
    mapped = data.mapped

    metadata = ProblemMetadata(
        problem_id="eon_grid_expansion",
        name="E.ON Grid Expansion",
        dataset_name="ieee118",
        source_network="pandapower",
        scenario_id=config.scenario_id,
        stress_level=config.stress_level,
        num_candidate_lines=len(candidates),
        created_at=datetime.now(UTC),
    )

    infrastructure = InfrastructureState(
        buses=mapped["buses"],
        bus_states=mapped["bus_states"],
        lines=mapped["lines"],
        line_flows=mapped["line_flows"],
        loads=mapped["loads"],
        generators=mapped["generators"],
    )

    decision_space = DecisionSpace(
        candidate_lines=list(candidates)
    )

    budget_constraint = BudgetConstraint(
        max_budget=budget
    )
    thermal_constraint = ThermalLimitConstraint(
        enabled=True
    )
    voltage_constraint = VoltageLimitConstraint(
        min_voltage_pu=0.95,
        max_voltage_pu=1.05,
    )
    topology_constraint = TopologyConstraint(
        enforce_connectivity=True
    )
    binary_constraint = BinaryDecisionConstraint(
        enabled=True
    )

    scenario = ScenarioContext(
        scenario_id=config.scenario_id,
        name=config.scenario_name,
        load_growth_factor=1.0,
        renewable_generation_factor=1.0,
        regional_stress_factor=1.0,
        line_outage_probability=0.0,
        description="Baseline scenario",
    )

    objectives = MultiObjectiveDefinition(
        congestion_reduction=CongestionReductionObjective(
            weight=1.0
        ),
        expansion_cost=ExpansionCostObjective(
            weight=1.0
        ),
    )

    return GridExpansionProblem(
        metadata=metadata,
        infrastructure=infrastructure,
        decision_space=decision_space,
        budget_constraint=budget_constraint,
        thermal_constraint=thermal_constraint,
        voltage_constraint=voltage_constraint,
        topology_constraint=topology_constraint,
        binary_constraint=binary_constraint,
        scenario=scenario,
        objectives=objectives,
    )


def _build_formulation(
    *,
    candidates: list[CandidateLine],
) -> GridExpansionFormulation:
    decision_variables = [
        ExpansionDecisionVariable(
            variable_id=(
                f"expansion_{candidate.candidate_id}"
            ),
            candidate_id=candidate.candidate_id,
        )
        for candidate in candidates
    ]

    objective_formulation = ObjectiveFormulation(
        minimize_congestion=True,
        minimize_expansion_cost=True,
    )

    constraint_formulation = ConstraintFormulation(
        enforce_budget_constraint=True,
        enforce_thermal_limits=True,
        enforce_voltage_limits=True,
        enforce_topology_constraints=True,
        enforce_binary_decisions=True,
    )

    return GridExpansionFormulation(
        decision_variables=decision_variables,
        objectives=objective_formulation,
        constraints=constraint_formulation,
    )
