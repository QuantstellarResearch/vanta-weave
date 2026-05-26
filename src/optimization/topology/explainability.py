from __future__ import annotations

from dataclasses import dataclass

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


# =========================================================
# EXPANSION DECISION EXPLANATION
# =========================================================

@dataclass(frozen=True)
class ExpansionDecisionExplanation:
    """
    Canonical infrastructure expansion explanation.

    Represents:
    - why expansion was selected
    - operational reinforcement reasoning
    - infrastructure planning justification
    """

    candidate_id: str

    explanation: str

    reinforcement_priority: str

    strategic_importance: float


# =========================================================
# CONGESTION EXPLANATION
# =========================================================

@dataclass(frozen=True)
class CongestionExplanation:
    """
    Canonical congestion reasoning explanation.

    Represents:
    - hotspot reasoning
    - operational stress interpretation
    - bottleneck explanation
    """

    hotspot_id: str

    explanation: str

    severity_level: str


# =========================================================
# RESILIENCE EXPLANATION
# =========================================================

@dataclass(frozen=True)
class ResilienceExplanation:
    """
    Canonical survivability reasoning explanation.

    Represents:
    - vulnerability interpretation
    - redundancy reasoning
    - infrastructure survivability insight
    """

    vulnerability_id: str

    explanation: str

    survivability_risk: str


# =========================================================
# OPERATIONAL REASONING REPORT
# =========================================================

@dataclass(frozen=True)
class OperationalReasoningReport:
    """
    Canonical operational infrastructure reasoning artifact.

    Represents:
    - infrastructure decision intelligence
    - operational reasoning
    - explainable infrastructure planning
    """

    expansion_explanations: list[
        ExpansionDecisionExplanation
    ]

    congestion_explanations: list[
        CongestionExplanation
    ]

    resilience_explanations: list[
        ResilienceExplanation
    ]

    executive_summary: str


# =========================================================
# EXPANSION EXPLANATIONS
# =========================================================

def explain_expansion_selection(
    solution: OptimizationSolution,
    analytics: OptimizationAnalytics,
) -> list[
    ExpansionDecisionExplanation
]:
    """
    Explain infrastructure expansion selections.

    Current strategy:
    - deterministic reasoning
    - topology-aware explanations
    - operational reinforcement framing
    """

    explanations = []

    average_cost_efficiency = (
        analytics
        .cost_efficiency_metrics
        .cost_per_added_mva
    )

    for expansion in (
        solution
        .expansion_plan
        .selected_expansions
    ):

        strategic_importance = (
            expansion.decision_score
        )

        if strategic_importance >= 0.8:
            reinforcement_priority = (
                "CRITICAL"
            )

        elif strategic_importance >= 0.5:
            reinforcement_priority = (
                "HIGH"
            )

        else:
            reinforcement_priority = (
                "MODERATE"
            )

        explanation = (
            f"Expansion candidate "
            f"{expansion.candidate_id} "
            f"was selected to improve "
            f"network reinforcement capacity "
            f"between {expansion.from_bus} "
            f"and {expansion.to_bus}. "
            f"The expansion contributes "
            f"{expansion.capacity_mva:.1f} MVA "
            f"of additional transmission capacity "
            f"with a strategic decision score "
            f"of {expansion.decision_score:.2f}. "
            f"This reinforcement supports "
            f"topology robustness and congestion "
            f"relief objectives while maintaining "
            f"infrastructure investment efficiency."
        )

        explanations.append(
            ExpansionDecisionExplanation(
                candidate_id=(
                    expansion.candidate_id
                ),

                explanation=explanation,

                reinforcement_priority=(
                    reinforcement_priority
                ),

                strategic_importance=(
                    strategic_importance
                ),
            )
        )

    return explanations


# =========================================================
# CONGESTION EXPLANATIONS
# =========================================================

def explain_congestion_hotspots(
    congestion_analysis: (
        CongestionAnalysisResult
    ),
) -> list[CongestionExplanation]:
    """
    Explain operational congestion hotspots.
    """

    explanations = []

    for hotspot in (
        congestion_analysis.hotspots
    ):

        explanation = (
            f"Congestion hotspot "
            f"{hotspot.hotspot_id} "
            f"represents a stressed operational "
            f"transmission corridor affecting "
            f"{len(hotspot.affected_edges)} "
            f"infrastructure edges. "
            f"The hotspot exhibits an average "
            f"congestion score of "
            f"{hotspot.average_congestion_score:.2f}, "
            f"indicating elevated topology stress "
            f"and increased bottleneck pressure "
            f"within the operational network."
        )

        explanations.append(
            CongestionExplanation(
                hotspot_id=(
                    hotspot.hotspot_id
                ),

                explanation=explanation,

                severity_level=(
                    hotspot.severity_level
                ),
            )
        )

    return explanations


# =========================================================
# RESILIENCE EXPLANATIONS
# =========================================================

def explain_resilience_vulnerabilities(
    resilience_analysis: (
        ResilienceAnalysisResult
    ),
) -> list[
    ResilienceExplanation
]:
    """
    Explain topology survivability vulnerabilities.
    """

    explanations = []

    for vulnerability in (
        resilience_analysis
        .vulnerabilities
    ):

        explanation = (
            f"Topology vulnerability "
            f"{vulnerability.vulnerability_id} "
            f"indicates structural infrastructure "
            f"fragility affecting "
            f"{len(vulnerability.affected_nodes)} "
            f"critical network nodes. "
            f"The vulnerability exhibits a "
            f"fragmentation risk score of "
            f"{vulnerability.fragmentation_risk:.2f}, "
            f"suggesting elevated survivability "
            f"risk under infrastructure failure "
            f"or stressed operating conditions."
        )

        explanations.append(
            ResilienceExplanation(
                vulnerability_id=(
                    vulnerability
                    .vulnerability_id
                ),

                explanation=explanation,

                survivability_risk=(
                    vulnerability
                    .severity_level
                ),
            )
        )

    return explanations


# =========================================================
# EXECUTIVE SUMMARY
# =========================================================

def build_executive_summary(
    solution: OptimizationSolution,
    analytics: OptimizationAnalytics,
    congestion_analysis: (
        CongestionAnalysisResult
    ),
    resilience_analysis: (
        ResilienceAnalysisResult
    ),
) -> str:
    """
    Build operational executive summary.

    IMPORTANT:
    Deterministic infrastructure reasoning only.
    """

    num_expansions = len(
        solution
        .expansion_plan
        .selected_expansions
    )

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

    num_hotspots = len(
        congestion_analysis.hotspots
    )

    resilience_score = (
        resilience_analysis
        .resilience_metrics
        .resilience_score
    )

    return (
        f"The optimization workflow identified "
        f"{num_expansions} strategic infrastructure "
        f"expansion decisions contributing "
        f"{total_capacity:.1f} MVA of additional "
        f"network reinforcement capacity. "
        f"The resulting infrastructure plan "
        f"maintains a total expansion investment "
        f"cost of {total_cost:.2f} while improving "
        f"topology robustness, congestion relief, "
        f"and operational survivability. "
        f"The operational analysis identified "
        f"{num_hotspots} congestion hotspot regions "
        f"and achieved an estimated resilience "
        f"score of {resilience_score:.2f}."
    )


# =========================================================
# PUBLIC EXPLAINABILITY API
# =========================================================

def build_operational_reasoning_report(
    solution: OptimizationSolution,
    analytics: OptimizationAnalytics,
    congestion_analysis: (
        CongestionAnalysisResult
    ),
    resilience_analysis: (
        ResilienceAnalysisResult
    ),
) -> OperationalReasoningReport:
    """
    Canonical operational infrastructure
    reasoning pipeline.

    Converts:
        optimization intelligence
            ↓
        operational reasoning
            ↓
        explainable infrastructure planning

    IMPORTANT:
    This layer is:
    - deterministic
    - graph-aware
    - explainable
    - operationally grounded

    NOT:
    - LLM-generated storytelling
    - hallucination-prone summarization
    """

    expansion_explanations = (
        explain_expansion_selection(
            solution,
            analytics,
        )
    )

    congestion_explanations = (
        explain_congestion_hotspots(
            congestion_analysis
        )
    )

    resilience_explanations = (
        explain_resilience_vulnerabilities(
            resilience_analysis
        )
    )

    executive_summary = (
        build_executive_summary(
            solution,
            analytics,
            congestion_analysis,
            resilience_analysis,
        )
    )

    return OperationalReasoningReport(
        expansion_explanations=(
            expansion_explanations
        ),

        congestion_explanations=(
            congestion_explanations
        ),

        resilience_explanations=(
            resilience_explanations
        ),

        executive_summary=(
            executive_summary
        ),
    )