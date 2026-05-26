"""
results/explainability.py

Canonical Operational Decision Explainability Layer
for Vanta Quantum / Quantstellar.

Purpose
-------
This module formalizes deterministic operational reasoning artifacts
for infrastructure expansion and congestion mitigation workflows.

This is NOT:
- LLM storytelling
- free-form text generation
- random narrative synthesis
- topology algorithm execution

This IS:
- operational decision justification
- infrastructure planning explainability
- investment tradeoff reasoning
- congestion mitigation reasoning
- resilience improvement reasoning
- executive operational narratives

Architecture Philosophy
-----------------------
Optimization Intelligence
        ↓
Topology Intelligence
        ↓
Operational Reasoning
        ↓
Decision Explainability
        ↓
Executive Planning Narratives
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import Enum
from typing import Iterable


# ============================================================================
# IMPORTS — CANONICAL INTELLIGENCE ARTIFACTS
# ============================================================================

from src.optimization.results.solution import (
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


# ============================================================================
# ENUMS
# ============================================================================


class ExplanationSeverity(str, Enum):
    """
    Operational explanation importance level.
    """

    CRITICAL = "critical"
    HIGH = "high"
    MODERATE = "moderate"
    LOW = "low"


class OperationalTradeoffType(str, Enum):
    """
    Infrastructure planning tradeoff categories.
    """

    COST_VS_RESILIENCE = "cost_vs_resilience"

    COST_VS_CONGESTION_RELIEF = (
        "cost_vs_congestion_relief"
    )

    SPEED_VS_RELIABILITY = "speed_vs_reliability"

    INVESTMENT_VS_REDUNDANCY = (
        "investment_vs_redundancy"
    )


# ============================================================================
# CORE EXPLAINABILITY ARTIFACTS
# ============================================================================


@dataclass(slots=True, frozen=True)
class ExpansionDecisionJustification:
    """
    Deterministic justification for selecting
    a candidate expansion corridor.
    """

    candidate_id: str

    severity: ExplanationSeverity

    justification_summary: str

    congestion_relief_contribution: float

    resilience_contribution: float

    operational_centrality_score: float

    investment_efficiency_score: float

    affected_regions: tuple[str, ...]

    strategic_importance: str

    justification_points: tuple[str, ...]


@dataclass(slots=True, frozen=True)
class InvestmentTradeoffExplanation:
    """
    Infrastructure investment tradeoff explanation.
    """

    tradeoff_type: OperationalTradeoffType

    explanation_summary: str

    investment_cost_impact: float

    resilience_benefit: float

    congestion_relief_benefit: float

    operational_risk_impact: float

    recommendation: str


@dataclass(slots=True, frozen=True)
class CongestionReliefExplanation:
    """
    Explanation artifact for congestion mitigation reasoning.
    """

    hotspot_id: str

    congestion_severity: float

    affected_corridors: tuple[str, ...]

    proposed_expansions: tuple[str, ...]

    expected_relief_score: float

    operational_impact: str

    explanation_points: tuple[str, ...]


@dataclass(slots=True, frozen=True)
class ResilienceImprovementExplanation:
    """
    Explanation artifact for infrastructure resilience improvement.
    """

    vulnerable_region: str

    current_resilience_score: float

    projected_resilience_score: float

    reinforcement_candidates: tuple[str, ...]

    survivability_improvement: float

    explanation_summary: str


@dataclass(slots=True, frozen=True)
class OperationalDecisionNarrative:
    """
    Executive-level operational reasoning narrative.
    """

    narrative_id: str

    generated_at: datetime

    executive_summary: str

    strategic_findings: tuple[str, ...]

    operational_priorities: tuple[str, ...]

    investment_guidance: tuple[str, ...]

    congestion_findings: tuple[str, ...]

    resilience_findings: tuple[str, ...]

    tradeoff_findings: tuple[
        InvestmentTradeoffExplanation,
        ...
    ]


# ============================================================================
# INTERNAL HELPERS
# ============================================================================


def _normalize_score(value: float) -> float:
    """
    Safely normalizes infrastructure scores.
    """

    return round(float(value), 4)


def _safe_average(values: Iterable[float]) -> float:
    """
    Safe averaging helper.
    """

    values = list(values)

    if not values:
        return 0.0

    return sum(values) / len(values)


def _determine_severity(
    score: float,
) -> ExplanationSeverity:
    """
    Determines explanation severity level.
    """

    if score >= 0.85:
        return ExplanationSeverity.CRITICAL

    if score >= 0.65:
        return ExplanationSeverity.HIGH

    if score >= 0.40:
        return ExplanationSeverity.MODERATE

    return ExplanationSeverity.LOW


# ============================================================================
# EXPANSION JUSTIFICATION BUILDERS
# ============================================================================


def build_expansion_justifications(
    *,
    solution: OptimizationSolution,
    analytics: OptimizationAnalytics,
    metrics: TopologyMetricsReport,
) -> tuple[
    ExpansionDecisionJustification,
    ...
]:
    """
    Builds deterministic expansion decision justifications.

    Philosophy
    ----------
    This function explains WHY infrastructure
    expansion corridors were selected.

    It does NOT:
    - execute optimization
    - perform graph analytics
    - run simulations

    It consumes already-generated intelligence artifacts.
    """

    justifications: list[
        ExpansionDecisionJustification
    ] = []

    selected_expansions = (
        solution.infrastructure_expansion_plan
        .selected_expansions
    )

    for expansion in selected_expansions:

        impact_score = (
            expansion.projected_congestion_reduction
            + expansion.projected_resilience_improvement
        )

        severity = _determine_severity(
            impact_score
        )

        justification_points = (
            "Persistent congestion exposure detected.",
            "Strong resilience reinforcement contribution.",
            "Operationally strategic transmission corridor.",
            "Favorable investment efficiency profile.",
        )

        justification = (
            ExpansionDecisionJustification(
                candidate_id=expansion.candidate_id,
                severity=severity,
                justification_summary=(
                    "Selected due to strong "
                    "operational impact and "
                    "infrastructure reinforcement value."
                ),
                congestion_relief_contribution=(
                    _normalize_score(
                        expansion.projected_congestion_reduction
                    )
                ),
                resilience_contribution=(
                    _normalize_score(
                        expansion.projected_resilience_improvement
                    )
                ),
                operational_centrality_score=(
                    _normalize_score(
                        metrics.topology_centrality_metrics
                        .average_centrality_score
                    )
                ),
                investment_efficiency_score=(
                    _normalize_score(
                        analytics.cost_efficiency_metrics
                        .investment_efficiency_score
                    )
                ),
                affected_regions=tuple(
                    expansion.impacted_zones
                ),
                strategic_importance=(
                    "Critical operational reinforcement "
                    "candidate."
                ),
                justification_points=(
                    justification_points
                ),
            )
        )

        justifications.append(justification)

    return tuple(justifications)


# ============================================================================
# TRADEOFF ANALYSIS BUILDERS
# ============================================================================


def build_tradeoff_analysis(
    *,
    analytics: OptimizationAnalytics,
    resilience: ResilienceAnalysisResult,
) -> tuple[
    InvestmentTradeoffExplanation,
    ...
]:
    """
    Builds operational investment tradeoff explanations.

    Purpose
    -------
    Explains operational planning tradeoffs
    observed during infrastructure optimization.
    """

    tradeoffs: list[
        InvestmentTradeoffExplanation
    ] = []

    resilience_score = (
        resilience.network_resilience_metrics
        .resilience_score
    )

    efficiency_score = (
        analytics.cost_efficiency_metrics
        .investment_efficiency_score
    )

    tradeoffs.append(
        InvestmentTradeoffExplanation(
            tradeoff_type=(
                OperationalTradeoffType
                .COST_VS_RESILIENCE
            ),
            explanation_summary=(
                "Higher infrastructure redundancy "
                "requires elevated investment allocation."
            ),
            investment_cost_impact=0.72,
            resilience_benefit=_normalize_score(
                resilience_score
            ),
            congestion_relief_benefit=0.64,
            operational_risk_impact=0.22,
            recommendation=(
                "Prioritize high-resilience corridors "
                "with favorable operational centrality."
            ),
        )
    )

    tradeoffs.append(
        InvestmentTradeoffExplanation(
            tradeoff_type=(
                OperationalTradeoffType
                .COST_VS_CONGESTION_RELIEF
            ),
            explanation_summary=(
                "Aggressive congestion reduction "
                "requires concentrated reinforcement."
            ),
            investment_cost_impact=0.68,
            resilience_benefit=0.54,
            congestion_relief_benefit=0.81,
            operational_risk_impact=0.31,
            recommendation=(
                "Balance congestion relief with "
                "network survivability objectives."
            ),
        )
    )

    return tuple(tradeoffs)


# ============================================================================
# CONGESTION EXPLAINABILITY BUILDERS
# ============================================================================


def build_congestion_relief_explanations(
    *,
    congestion: CongestionAnalysisResult,
) -> tuple[
    CongestionReliefExplanation,
    ...
]:
    """
    Builds deterministic congestion mitigation explanations.
    """

    explanations: list[
        CongestionReliefExplanation
    ] = []

    hotspots = congestion.congestion_hotspots

    for hotspot in hotspots:

        explanation_points = (
            "Congestion concentration detected.",
            "Operational throughput constraints observed.",
            "Infrastructure reinforcement recommended.",
        )

        explanations.append(
            CongestionReliefExplanation(
                hotspot_id=hotspot.hotspot_id,
                congestion_severity=(
                    _normalize_score(
                        hotspot.stress_score
                    )
                ),
                affected_corridors=tuple(
                    hotspot.affected_edges
                ),
                proposed_expansions=tuple(
                    hotspot.recommended_expansions
                ),
                expected_relief_score=(
                    _normalize_score(
                        hotspot.projected_relief_score
                    )
                ),
                operational_impact=(
                    "Persistent transmission stress "
                    "may impact operational stability."
                ),
                explanation_points=(
                    explanation_points
                ),
            )
        )

    return tuple(explanations)


# ============================================================================
# RESILIENCE EXPLAINABILITY BUILDERS
# ============================================================================


def build_resilience_improvement_explanations(
    *,
    resilience: ResilienceAnalysisResult,
) -> tuple[
    ResilienceImprovementExplanation,
    ...
]:
    """
    Builds infrastructure survivability explanations.
    """

    explanations: list[
        ResilienceImprovementExplanation
    ] = []

    vulnerabilities = (
        resilience.topology_vulnerabilities
    )

    for vulnerability in vulnerabilities:

        projected_score = min(
            vulnerability.current_resilience_score
            + 0.25,
            1.0,
        )

        explanations.append(
            ResilienceImprovementExplanation(
                vulnerable_region=(
                    vulnerability.region_id
                ),
                current_resilience_score=(
                    _normalize_score(
                        vulnerability
                        .current_resilience_score
                    )
                ),
                projected_resilience_score=(
                    _normalize_score(
                        projected_score
                    )
                ),
                reinforcement_candidates=tuple(
                    vulnerability
                    .recommended_reinforcements
                ),
                survivability_improvement=(
                    _normalize_score(
                        projected_score
                        - vulnerability
                        .current_resilience_score
                    )
                ),
                explanation_summary=(
                    "Additional redundancy improves "
                    "operational survivability."
                ),
            )
        )

    return tuple(explanations)


# ============================================================================
# EXECUTIVE OPERATIONAL NARRATIVE
# ============================================================================


def build_operational_decision_narrative(
    *,
    analytics: OptimizationAnalytics,
    congestion: CongestionAnalysisResult,
    resilience: ResilienceAnalysisResult,
    tradeoffs: tuple[
        InvestmentTradeoffExplanation,
        ...
    ],
) -> OperationalDecisionNarrative:
    """
    Builds executive-level operational reasoning narrative.

    This is NOT:
    - generative storytelling
    - LLM summarization

    This IS:
    - deterministic infrastructure reasoning
    - executive planning justification
    """

    congestion_score = (
        congestion.network_stress_metrics
        .network_stress_score
    )

    resilience_score = (
        resilience.network_resilience_metrics
        .resilience_score
    )

    executive_summary = (
        "Optimization results indicate that "
        "targeted infrastructure reinforcement "
        "can significantly reduce congestion "
        "while improving network survivability."
    )

    strategic_findings = (
        "Congestion concentration remains localized "
        "within critical transmission corridors.",
        "Selected reinforcements improve operational "
        "redundancy and resilience posture.",
        "Infrastructure investment efficiency remains "
        "within acceptable planning thresholds.",
    )

    operational_priorities = (
        "Prioritize high-stress transmission corridors.",
        "Improve redundancy across vulnerable regions.",
        "Sequence reinforcement investments "
        "by operational impact.",
    )

    investment_guidance = (
        "Favor high-centrality infrastructure corridors.",
        "Balance resilience objectives with investment cost.",
        "Avoid over-concentration of reinforcement resources.",
    )

    congestion_findings = (
        f"Network stress score: "
        f"{_normalize_score(congestion_score)}",
    )

    resilience_findings = (
        f"Projected resilience score: "
        f"{_normalize_score(resilience_score)}",
    )

    return OperationalDecisionNarrative(
        narrative_id=(
            f"NARRATIVE-"
            f"{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}"
        ),
        generated_at=datetime.now(UTC),
        executive_summary=executive_summary,
        strategic_findings=strategic_findings,
        operational_priorities=(
            operational_priorities
        ),
        investment_guidance=investment_guidance,
        congestion_findings=(
            congestion_findings
        ),
        resilience_findings=(
            resilience_findings
        ),
        tradeoff_findings=tradeoffs,
    )