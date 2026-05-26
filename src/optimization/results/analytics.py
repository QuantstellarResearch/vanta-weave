from __future__ import annotations

from dataclasses import dataclass

from src.optimization.results.solution import (
    OptimizationSolution,
)


# =========================================================
# CAPACITY METRICS
# =========================================================

@dataclass(frozen=True)
class InfrastructureCapacityMetrics:
    """
    Infrastructure expansion capacity metrics.
    """

    total_added_capacity_mva: float

    average_capacity_per_expansion: float

    max_capacity_expansion_mva: float


# =========================================================
# COST EFFICIENCY METRICS
# =========================================================

@dataclass(frozen=True)
class CostEfficiencyMetrics:
    """
    Infrastructure investment efficiency metrics.
    """

    total_expansion_cost: float

    average_cost_per_expansion: float

    cost_per_added_mva: float


# =========================================================
# EXPANSION IMPACT METRICS
# =========================================================

@dataclass(frozen=True)
class ExpansionImpactMetrics:
    """
    Infrastructure expansion impact metrics.
    """

    num_selected_expansions: int

    total_network_reinforcement_score: float

    average_decision_score: float


# =========================================================
# SCENARIO SENSITIVITY
# =========================================================

@dataclass(frozen=True)
class ScenarioSensitivityMetrics:
    """
    Scenario-level optimization sensitivity metrics.
    """

    scenario_id: str

    stress_adjusted_cost_efficiency: float

    stress_adjusted_capacity_gain: float


# =========================================================
# CANONICAL ANALYTICS ARTIFACT
# =========================================================

@dataclass(frozen=True)
class OptimizationAnalytics:
    """
    Canonical optimization analytics artifact.

    Represents:
    - infrastructure intelligence
    - planning analytics
    - investment metrics
    - operational optimization insights
    """

    capacity_metrics: (
        InfrastructureCapacityMetrics
    )

    cost_efficiency_metrics: (
        CostEfficiencyMetrics
    )

    expansion_impact_metrics: (
        ExpansionImpactMetrics
    )

    scenario_sensitivity_metrics: (
        ScenarioSensitivityMetrics
    )


# =========================================================
# CAPACITY ANALYTICS
# =========================================================

def build_capacity_metrics(
    solution: OptimizationSolution,
) -> InfrastructureCapacityMetrics:
    """
    Build infrastructure capacity analytics.
    """

    expansions = (
        solution
        .expansion_plan
        .selected_expansions
    )

    total_capacity = sum(
        expansion.capacity_mva
        for expansion in expansions
    )

    average_capacity = (
        total_capacity / len(expansions)
        if expansions
        else 0.0
    )

    max_capacity = max(
        (
            expansion.capacity_mva
            for expansion in expansions
        ),
        default=0.0,
    )

    return InfrastructureCapacityMetrics(
        total_added_capacity_mva=(
            total_capacity
        ),

        average_capacity_per_expansion=(
            average_capacity
        ),

        max_capacity_expansion_mva=(
            max_capacity
        ),
    )


# =========================================================
# COST ANALYTICS
# =========================================================

def build_cost_efficiency_metrics(
    solution: OptimizationSolution,
) -> CostEfficiencyMetrics:
    """
    Build infrastructure investment efficiency metrics.
    """

    expansions = (
        solution
        .expansion_plan
        .selected_expansions
    )

    total_cost = (
        solution
        .expansion_plan
        .total_expansion_cost
    )

    average_cost = (
        total_cost / len(expansions)
        if expansions
        else 0.0
    )

    total_capacity = (
        solution
        .expansion_plan
        .total_added_capacity_mva
    )

    cost_per_added_mva = (
        total_cost / total_capacity
        if total_capacity > 0
        else 0.0
    )

    return CostEfficiencyMetrics(
        total_expansion_cost=(
            total_cost
        ),

        average_cost_per_expansion=(
            average_cost
        ),

        cost_per_added_mva=(
            cost_per_added_mva
        ),
    )


# =========================================================
# IMPACT ANALYTICS
# =========================================================

def build_expansion_impact_metrics(
    solution: OptimizationSolution,
) -> ExpansionImpactMetrics:
    """
    Build infrastructure reinforcement impact metrics.
    """

    expansions = (
        solution
        .expansion_plan
        .selected_expansions
    )

    average_decision_score = (
        sum(
            expansion.decision_score
            for expansion in expansions
        )
        / len(expansions)
        if expansions
        else 0.0
    )

    total_reinforcement_score = sum(
        expansion.decision_score
        *
        expansion.capacity_mva

        for expansion in expansions
    )

    return ExpansionImpactMetrics(
        num_selected_expansions=(
            len(expansions)
        ),

        total_network_reinforcement_score=(
            total_reinforcement_score
        ),

        average_decision_score=(
            average_decision_score
        ),
    )


# =========================================================
# SCENARIO ANALYTICS
# =========================================================

def build_scenario_sensitivity_metrics(
    solution: OptimizationSolution,
) -> ScenarioSensitivityMetrics:
    """
    Build scenario-aware optimization metrics.

    Current phase:
    simplified scenario heuristics.
    """

    total_capacity = (
        solution
        .expansion_plan
        .total_added_capacity_mva
    )

    total_cost = (
        solution
        .expansion_plan
        .total_expansion_cost
    )

    stress_adjusted_capacity_gain = (
        total_capacity * 1.15
    )

    stress_adjusted_cost_efficiency = (
        total_capacity / total_cost
        if total_cost > 0
        else 0.0
    )

    return ScenarioSensitivityMetrics(
        scenario_id=solution.scenario_id,

        stress_adjusted_cost_efficiency=(
            stress_adjusted_cost_efficiency
        ),

        stress_adjusted_capacity_gain=(
            stress_adjusted_capacity_gain
        ),
    )


# =========================================================
# PUBLIC ANALYTICS API
# =========================================================

def build_optimization_analytics(
    solution: OptimizationSolution,
) -> OptimizationAnalytics:
    """
    Canonical optimization analytics pipeline.

    Converts:
        optimization solution
            ↓
        infrastructure intelligence
    """

    return OptimizationAnalytics(
        capacity_metrics=(
            build_capacity_metrics(
                solution
            )
        ),

        cost_efficiency_metrics=(
            build_cost_efficiency_metrics(
                solution
            )
        ),

        expansion_impact_metrics=(
            build_expansion_impact_metrics(
                solution
            )
        ),

        scenario_sensitivity_metrics=(
            build_scenario_sensitivity_metrics(
                solution
            )
        ),
    )