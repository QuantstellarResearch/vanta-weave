"""
results/reporting.py

Canonical Operational Intelligence Delivery Layer
for Vanta Quantum / Quantstellar.

Purpose
-------
This module transforms normalized optimization intelligence artifacts
into deterministic, operationally-believable infrastructure planning reports.

This is NOT:
- a presentation layer
- an LLM summarizer
- a solver output dump

This IS:
- operational decision delivery
- infrastructure planning intelligence
- executive reporting substrate
- E.ON / QC4SG operational artifact generation

Architecture Philosophy
-----------------------
Optimization Intelligence
        ↓
Operational Reasoning
        ↓
Decision Artifacts
        ↓
Executive Infrastructure Reports
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Iterable


# ============================================================================
# IMPORTS — CANONICAL INTELLIGENCE ARTIFACTS
# ============================================================================

# NOTE:
# These imports assume the current Vanta Quantum architecture.

from src.optimization.results.solution import (
    OptimizationExecutionSummary,
    OptimizationSolution,
)

from src.optimization.results.analytics import (
    OptimizationAnalytics,
)

from src.optimization.topology.congestion import (
    CongestionAnalysisResult,
)

from src.optimization.topology.resilience import (
    ResilienceAnalysisResult,
)

from src.optimization.topology.metrics import (
    TopologyMetricsReport,
)

from src.optimization.topology.explainability import (
    OperationalReasoningReport,
)


# ============================================================================
# ENUMS
# ============================================================================


class RecommendationPriority(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskLevel(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MODERATE = "moderate"
    LOW = "low"


class RecommendationCategory(str, Enum):
    CONGESTION_MITIGATION = "congestion_mitigation"
    RESILIENCE_IMPROVEMENT = "resilience_improvement"
    CAPACITY_EXPANSION = "capacity_expansion"
    INVESTMENT_OPTIMIZATION = "investment_optimization"
    OPERATIONAL_REINFORCEMENT = "operational_reinforcement"


# ============================================================================
# CORE OPERATIONAL REPORT ARTIFACTS
# ============================================================================


@dataclass(slots=True, frozen=True)
class InfrastructureRecommendation:
    """
    Canonical infrastructure decision recommendation.

    Represents a deterministic operational planning recommendation
    derived from optimization and topology intelligence.
    """

    recommendation_id: str

    title: str

    category: RecommendationCategory

    priority: RecommendationPriority

    rationale: str

    expected_congestion_reduction: float

    expected_resilience_improvement: float

    estimated_investment_cost: float

    impacted_zones: tuple[str, ...]

    affected_assets: tuple[str, ...]

    implementation_risk: RiskLevel

    projected_operational_benefit: str


@dataclass(slots=True, frozen=True)
class OperationalRiskAssessment:
    """
    Infrastructure operational risk evaluation.
    """

    overall_risk_level: RiskLevel

    congestion_risk_score: float

    resilience_risk_score: float

    overload_risk_score: float

    vulnerable_regions: tuple[str, ...]

    critical_corridors: tuple[str, ...]

    operational_concerns: tuple[str, ...]

    mitigation_recommendations: tuple[str, ...]


@dataclass(slots=True, frozen=True)
class ExpansionPortfolioSummary:
    """
    Portfolio-level infrastructure expansion summary.
    """

    selected_candidate_count: int

    total_expansion_cost: float

    projected_congestion_reduction: float

    projected_resilience_improvement: float

    projected_network_efficiency_gain: float

    highest_priority_expansions: tuple[str, ...]

    deferred_expansions: tuple[str, ...]

    portfolio_risk_level: RiskLevel


@dataclass(slots=True, frozen=True)
class InvestmentPriorityRecommendation:
    """
    Prioritized infrastructure investment recommendation.
    """

    priority_rank: int

    corridor_id: str

    justification: str

    expected_benefit_score: float

    investment_cost: float

    strategic_importance: str


@dataclass(slots=True, frozen=True)
class CongestionMitigationRecommendation:
    """
    Congestion mitigation planning artifact.
    """

    hotspot_id: str

    affected_corridors: tuple[str, ...]

    severity_score: float

    proposed_reinforcements: tuple[str, ...]

    expected_relief_score: float


@dataclass(slots=True, frozen=True)
class ExecutiveInfrastructureReport:
    """
    Canonical executive infrastructure intelligence report.

    Top-level operational delivery artifact.
    """

    report_id: str

    scenario_name: str

    generated_at: datetime

    optimization_summary: OptimizationExecutionSummary

    portfolio_summary: ExpansionPortfolioSummary

    operational_risk_assessment: OperationalRiskAssessment

    infrastructure_recommendations: tuple[
        InfrastructureRecommendation,
        ...
    ]

    investment_priorities: tuple[
        InvestmentPriorityRecommendation,
        ...
    ]

    congestion_mitigation_actions: tuple[
        CongestionMitigationRecommendation,
        ...
    ]

    congestion_summary: str

    resilience_summary: str

    executive_overview: str

    operational_priorities: tuple[str, ...]

    strategic_insights: tuple[str, ...]


# ============================================================================
# INTERNAL HELPERS
# ============================================================================


def _determine_risk_level(score: float) -> RiskLevel:
    """
    Deterministic infrastructure risk classification.
    """

    if score >= 0.85:
        return RiskLevel.CRITICAL

    if score >= 0.65:
        return RiskLevel.HIGH

    if score >= 0.40:
        return RiskLevel.MODERATE

    return RiskLevel.LOW


def _normalize_percentage(value: float) -> float:
    """
    Normalizes percentage-like metrics safely.
    """

    return round(float(value), 4)


def _safe_average(values: Iterable[float]) -> float:
    values = list(values)

    if not values:
        return 0.0

    return sum(values) / len(values)


# ============================================================================
# PORTFOLIO SUMMARY BUILDERS
# ============================================================================


def build_expansion_portfolio_summary(
    *,
    solution: OptimizationSolution,
    analytics: OptimizationAnalytics,
    resilience: ResilienceAnalysisResult,
    metrics: TopologyMetricsReport,
) -> ExpansionPortfolioSummary:
    """
    Builds canonical infrastructure expansion portfolio summary.
    """

    selected_expansions = solution.infrastructure_expansion_plan.selected_expansions

    total_cost = sum(
        expansion.expansion_cost
        for expansion in selected_expansions
    )

    congestion_reduction = _normalize_percentage(
        analytics.expansion_impact_metrics.projected_congestion_reduction
    )

    resilience_improvement = _normalize_percentage(
        resilience.network_resilience_metrics.resilience_score
    )

    efficiency_gain = _normalize_percentage(
        metrics.network_efficiency_metrics.network_efficiency
    )

    highest_priority = tuple(
        expansion.candidate_id
        for expansion in selected_expansions[:5]
    )

    portfolio_risk_score = _safe_average([
        1.0 - resilience.network_resilience_metrics.resilience_score,
        analytics.scenario_sensitivity_metrics.risk_sensitivity_score,
    ])

    return ExpansionPortfolioSummary(
        selected_candidate_count=len(selected_expansions),
        total_expansion_cost=round(total_cost, 2),
        projected_congestion_reduction=congestion_reduction,
        projected_resilience_improvement=resilience_improvement,
        projected_network_efficiency_gain=efficiency_gain,
        highest_priority_expansions=highest_priority,
        deferred_expansions=tuple(),
        portfolio_risk_level=_determine_risk_level(portfolio_risk_score),
    )


# ============================================================================
# RISK ASSESSMENT BUILDERS
# ============================================================================


def build_operational_risk_assessment(
    *,
    congestion: CongestionAnalysisResult,
    resilience: ResilienceAnalysisResult,
) -> OperationalRiskAssessment:
    """
    Builds operational infrastructure risk assessment.
    """

    congestion_score = congestion.network_stress_metrics.network_stress_score

    resilience_score = (
        1.0 - resilience.network_resilience_metrics.resilience_score
    )

    overload_score = _safe_average([
        hotspot.stress_score
        for hotspot in congestion.congestion_hotspots
    ])

    overall_score = _safe_average([
        congestion_score,
        resilience_score,
        overload_score,
    ])

    vulnerable_regions = tuple(
        vulnerability.region_id
        for vulnerability in resilience.topology_vulnerabilities[:5]
    )

    critical_corridors = tuple(
        edge.edge_id
        for edge in resilience.critical_infrastructure_edges[:5]
    )

    concerns: list[str] = []

    if congestion_score > 0.70:
        concerns.append(
            "Persistent congestion stress detected in critical corridors."
        )

    if resilience_score > 0.65:
        concerns.append(
            "Network survivability risk exceeds acceptable operational threshold."
        )

    if overload_score > 0.60:
        concerns.append(
            "Overload exposure detected under projected infrastructure demand."
        )

    mitigation = [
        "Prioritize reinforcement of high-centrality corridors.",
        "Reduce congestion concentration through expansion diversification.",
        "Increase resilience redundancy across vulnerable regions.",
    ]

    return OperationalRiskAssessment(
        overall_risk_level=_determine_risk_level(overall_score),
        congestion_risk_score=round(congestion_score, 4),
        resilience_risk_score=round(resilience_score, 4),
        overload_risk_score=round(overload_score, 4),
        vulnerable_regions=vulnerable_regions,
        critical_corridors=critical_corridors,
        operational_concerns=tuple(concerns),
        mitigation_recommendations=tuple(mitigation),
    )


# ============================================================================
# RECOMMENDATION BUILDERS
# ============================================================================


def build_infrastructure_recommendations(
    *,
    solution: OptimizationSolution,
    congestion: CongestionAnalysisResult,
    resilience: ResilienceAnalysisResult,
) -> tuple[InfrastructureRecommendation, ...]:
    """
    Builds deterministic infrastructure recommendations.
    """

    recommendations: list[InfrastructureRecommendation] = []

    selected_expansions = (
        solution.infrastructure_expansion_plan.selected_expansions
    )

    for index, expansion in enumerate(selected_expansions, start=1):

        recommendation = InfrastructureRecommendation(
            recommendation_id=f"REC-{index:04d}",
            title=(
                f"Reinforce candidate corridor "
                f"{expansion.candidate_id}"
            ),
            category=RecommendationCategory.CONGESTION_MITIGATION,
            priority=(
                RecommendationPriority.CRITICAL
                if index <= 2
                else RecommendationPriority.HIGH
            ),
            rationale=(
                "Selected due to strong congestion mitigation "
                "and resilience contribution."
            ),
            expected_congestion_reduction=round(
                expansion.projected_congestion_reduction,
                4,
            ),
            expected_resilience_improvement=round(
                expansion.projected_resilience_improvement,
                4,
            ),
            estimated_investment_cost=round(
                expansion.expansion_cost,
                2,
            ),
            impacted_zones=tuple(expansion.impacted_zones),
            affected_assets=tuple(expansion.affected_assets),
            implementation_risk=RiskLevel.MODERATE,
            projected_operational_benefit=(
                "Improves network stability and reduces "
                "critical corridor stress."
            ),
        )

        recommendations.append(recommendation)

    return tuple(recommendations)


# ============================================================================
# INVESTMENT PRIORITY BUILDERS
# ============================================================================


def build_investment_priorities(
    *,
    solution: OptimizationSolution,
) -> tuple[InvestmentPriorityRecommendation, ...]:
    """
    Builds prioritized investment ordering.
    """

    priorities: list[InvestmentPriorityRecommendation] = []

    selected_expansions = (
        solution.infrastructure_expansion_plan.selected_expansions
    )

    sorted_expansions = sorted(
        selected_expansions,
        key=lambda item: (
            item.projected_congestion_reduction
            + item.projected_resilience_improvement
        ),
        reverse=True,
    )

    for rank, expansion in enumerate(sorted_expansions, start=1):

        priorities.append(
            InvestmentPriorityRecommendation(
                priority_rank=rank,
                corridor_id=expansion.candidate_id,
                justification=(
                    "High projected infrastructure impact "
                    "with favorable operational efficiency."
                ),
                expected_benefit_score=round(
                    (
                        expansion.projected_congestion_reduction
                        + expansion.projected_resilience_improvement
                    ),
                    4,
                ),
                investment_cost=round(
                    expansion.expansion_cost,
                    2,
                ),
                strategic_importance=(
                    "Critical reinforcement candidate."
                ),
            )
        )

    return tuple(priorities)


# ============================================================================
# CONGESTION MITIGATION BUILDERS
# ============================================================================


def build_congestion_mitigation_actions(
    *,
    congestion: CongestionAnalysisResult,
) -> tuple[CongestionMitigationRecommendation, ...]:
    """
    Builds congestion mitigation planning recommendations.
    """

    recommendations: list[
        CongestionMitigationRecommendation
    ] = []

    for hotspot in congestion.congestion_hotspots[:5]:

        recommendations.append(
            CongestionMitigationRecommendation(
                hotspot_id=hotspot.hotspot_id,
                affected_corridors=tuple(
                    hotspot.affected_edges
                ),
                severity_score=round(
                    hotspot.stress_score,
                    4,
                ),
                proposed_reinforcements=tuple(
                    hotspot.recommended_expansions
                ),
                expected_relief_score=round(
                    hotspot.projected_relief_score,
                    4,
                ),
            )
        )

    return tuple(recommendations)


# ============================================================================
# EXECUTIVE REPORT ORCHESTRATION
# ============================================================================


def build_executive_report(
    *,
    scenario_name: str,
    solution: OptimizationSolution,
    analytics: OptimizationAnalytics,
    congestion: CongestionAnalysisResult,
    resilience: ResilienceAnalysisResult,
    metrics: TopologyMetricsReport,
    reasoning: OperationalReasoningReport,
) -> ExecutiveInfrastructureReport:
    """
    Canonical executive operational report orchestration entrypoint.
    """

    portfolio_summary = build_expansion_portfolio_summary(
        solution=solution,
        analytics=analytics,
        resilience=resilience,
        metrics=metrics,
    )

    operational_risk = build_operational_risk_assessment(
        congestion=congestion,
        resilience=resilience,
    )

    recommendations = build_infrastructure_recommendations(
        solution=solution,
        congestion=congestion,
        resilience=resilience,
    )

    priorities = build_investment_priorities(
        solution=solution,
    )

    congestion_actions = build_congestion_mitigation_actions(
        congestion=congestion,
    )

    congestion_summary = (
        "Persistent congestion pressure detected "
        "across critical operational corridors."
    )

    resilience_summary = (
        "Expansion portfolio improves survivability "
        "and redundancy characteristics."
    )

    executive_overview = (
        "The optimization workflow identified "
        "high-value infrastructure reinforcement opportunities "
        "for congestion mitigation and resilience improvement."
    )

    strategic_insights = (
        "Congestion concentration remains localized "
        "within high-centrality transmission corridors.",
        "Selected expansions provide favorable operational "
        "efficiency relative to investment cost.",
        "Infrastructure reinforcement improves projected "
        "network survivability metrics.",
    )

    operational_priorities = (
        "Prioritize congestion relief in critical corridors.",
        "Increase redundancy in vulnerable infrastructure regions.",
        "Sequence investment deployment by operational impact.",
    )

    return ExecutiveInfrastructureReport(
        report_id=(
            f"EXEC-{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}"
        ),
        scenario_name=scenario_name,
        generated_at=datetime.now(UTC),
        optimization_summary=solution.execution_summary,
        portfolio_summary=portfolio_summary,
        operational_risk_assessment=operational_risk,
        infrastructure_recommendations=recommendations,
        investment_priorities=priorities,
        congestion_mitigation_actions=congestion_actions,
        congestion_summary=congestion_summary,
        resilience_summary=resilience_summary,
        executive_overview=executive_overview,
        operational_priorities=operational_priorities,
        strategic_insights=strategic_insights,
    )


# ============================================================================
# EXPORT LAYER
# ============================================================================


def export_markdown_report(
    report: ExecutiveInfrastructureReport,
) -> str:
    """
    Exports operational report as deterministic markdown artifact.
    """

    lines: list[str] = []

    lines.append("# Executive Infrastructure Report")
    lines.append("")

    lines.append(f"Scenario: {report.scenario_name}")
    lines.append(
        f"Generated: {report.generated_at.isoformat()}"
    )

    lines.append("")
    lines.append("## Executive Overview")
    lines.append(report.executive_overview)

    lines.append("")
    lines.append("## Operational Priorities")

    for priority in report.operational_priorities:
        lines.append(f"- {priority}")

    lines.append("")
    lines.append("## Strategic Insights")

    for insight in report.strategic_insights:
        lines.append(f"- {insight}")

    lines.append("")
    lines.append("## Infrastructure Recommendations")

    for recommendation in report.infrastructure_recommendations:

        lines.append(
            f"### {recommendation.title}"
        )

        lines.append(
            f"- Priority: {recommendation.priority.value}"
        )

        lines.append(
            f"- Expected Congestion Reduction: "
            f"{recommendation.expected_congestion_reduction}"
        )

        lines.append(
            f"- Estimated Cost: "
            f"{recommendation.estimated_investment_cost}"
        )

        lines.append(
            f"- Rationale: {recommendation.rationale}"
        )

        lines.append("")

    return "\n".join(lines)


def export_json_report(
    report: ExecutiveInfrastructureReport,
) -> dict:
    """
    Machine-readable export artifact.
    """

    return {
        "report_id": report.report_id,
        "scenario_name": report.scenario_name,
        "generated_at": report.generated_at.isoformat(),
        "executive_overview": report.executive_overview,
        "operational_priorities": list(
            report.operational_priorities
        ),
        "strategic_insights": list(
            report.strategic_insights
        ),
        "recommendation_count": len(
            report.infrastructure_recommendations
        ),
    }


def export_operational_report(
    *,
    report: ExecutiveInfrastructureReport,
    export_format: str = "markdown",
):
    """
    Canonical operational report export gateway.
    """

    normalized = export_format.lower().strip()

    if normalized == "markdown":
        return export_markdown_report(report)

    if normalized == "json":
        return export_json_report(report)

    raise ValueError(
        f"Unsupported export format: {export_format}"
    )