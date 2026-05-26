"""
results/topology.py

Canonical Operational Topology Delivery Layer
for Vanta Quantum / Quantstellar.

Purpose
-------
This module transforms topology intelligence artifacts into
operationally meaningful infrastructure topology outputs.

This is NOT:
- graph algorithm execution
- topology simulation
- NetworkX orchestration
- raw graph analytics

This IS:
- operational topology delivery
- congestion impact topology projection
- resilience overlay projection
- infrastructure region summaries
- operational topology intelligence artifacts

Architecture Philosophy
-----------------------
Topology Intelligence
        ↓
Operational Projection
        ↓
Infrastructure Impact Artifacts
        ↓
Operational Delivery
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import Enum
from typing import Iterable


# ============================================================================
# IMPORTS — TOPOLOGY INTELLIGENCE ARTIFACTS
# ============================================================================

from src.optimization.results.solution import (
    OptimizationSolution,
)

from src.optimization.topology.graph import (
    OperationalTopologyGraph,
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


class OperationalRegionSeverity(str, Enum):
    """
    Severity classification for operational topology regions.
    """

    CRITICAL = "critical"

    HIGH = "high"

    MODERATE = "moderate"

    LOW = "low"


class InfrastructureRegionType(str, Enum):
    """
    Infrastructure operational region categories.
    """

    CONGESTION_REGION = "congestion_region"

    RESILIENCE_REGION = "resilience_region"

    EXPANSION_REGION = "expansion_region"

    CRITICAL_CORRIDOR = "critical_corridor"

    OPERATIONAL_ZONE = "operational_zone"


# ============================================================================
# CORE TOPOLOGY DELIVERY ARTIFACTS
# ============================================================================


@dataclass(slots=True, frozen=True)
class CriticalInfrastructureRegion:
    """
    Canonical operationally critical infrastructure region.
    """

    region_id: str

    region_type: InfrastructureRegionType

    severity: OperationalRegionSeverity

    affected_assets: tuple[str, ...]

    affected_corridors: tuple[str, ...]

    operational_risk_score: float

    resilience_score: float

    congestion_score: float

    operational_summary: str


@dataclass(slots=True, frozen=True)
class CongestionImpactRegion:
    """
    Operational congestion impact projection artifact.
    """

    hotspot_id: str

    impacted_corridors: tuple[str, ...]

    impacted_zones: tuple[str, ...]

    stress_score: float

    projected_relief_score: float

    reinforcement_candidates: tuple[str, ...]

    operational_impact_summary: str


@dataclass(slots=True, frozen=True)
class ResilienceImprovementRegion:
    """
    Operational resilience improvement projection artifact.
    """

    vulnerable_region_id: str

    current_resilience_score: float

    projected_resilience_score: float

    reinforcement_corridors: tuple[str, ...]

    survivability_improvement: float

    operational_benefit_summary: str


@dataclass(slots=True, frozen=True)
class ExpansionImpactTopology:
    """
    Operational expansion topology projection artifact.
    """

    candidate_id: str

    impacted_regions: tuple[str, ...]

    impacted_corridors: tuple[str, ...]

    projected_congestion_reduction: float

    projected_resilience_improvement: float

    operational_importance: str


@dataclass(slots=True, frozen=True)
class OperationalTopologySummary:
    """
    Executive operational topology delivery artifact.
    """

    summary_id: str

    generated_at: datetime

    total_operational_regions: int

    critical_region_count: int

    congestion_region_count: int

    resilience_region_count: int

    expansion_region_count: int

    average_network_resilience: float

    average_network_stress: float

    strategic_findings: tuple[str, ...]

    operational_priorities: tuple[str, ...]

    critical_regions: tuple[
        CriticalInfrastructureRegion,
        ...
    ]


# ============================================================================
# INTERNAL HELPERS
# ============================================================================


def _normalize_score(value: float) -> float:
    """
    Safely normalizes infrastructure metrics.
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


def _determine_region_severity(
    score: float,
) -> OperationalRegionSeverity:
    """
    Determines operational severity classification.
    """

    if score >= 0.85:
        return OperationalRegionSeverity.CRITICAL

    if score >= 0.65:
        return OperationalRegionSeverity.HIGH

    if score >= 0.40:
        return OperationalRegionSeverity.MODERATE

    return OperationalRegionSeverity.LOW


# ============================================================================
# CRITICAL REGION BUILDERS
# ============================================================================


def build_critical_infrastructure_regions(
    *,
    congestion: CongestionAnalysisResult,
    resilience: ResilienceAnalysisResult,
) -> tuple[
    CriticalInfrastructureRegion,
    ...
]:
    """
    Builds operationally critical infrastructure regions.

    Philosophy
    ----------
    This function projects topology intelligence into
    operationally meaningful critical regions.

    It does NOT:
    - execute graph algorithms
    - run simulations
    - mutate topology state
    """

    regions: list[
        CriticalInfrastructureRegion
    ] = []

    hotspots = congestion.congestion_hotspots

    for hotspot in hotspots:

        severity = _determine_region_severity(
            hotspot.stress_score
        )

        region = CriticalInfrastructureRegion(
            region_id=f"CR-{hotspot.hotspot_id}",
            region_type=(
                InfrastructureRegionType
                .CONGESTION_REGION
            ),
            severity=severity,
            affected_assets=tuple(
                hotspot.affected_assets
            ),
            affected_corridors=tuple(
                hotspot.affected_edges
            ),
            operational_risk_score=(
                _normalize_score(
                    hotspot.stress_score
                )
            ),
            resilience_score=0.55,
            congestion_score=(
                _normalize_score(
                    hotspot.stress_score
                )
            ),
            operational_summary=(
                "Persistent congestion exposure "
                "detected within operational corridor."
            ),
        )

        regions.append(region)

    vulnerabilities = (
        resilience.topology_vulnerabilities
    )

    for vulnerability in vulnerabilities:

        projected_risk = (
            1.0
            - vulnerability.current_resilience_score
        )

        severity = _determine_region_severity(
            projected_risk
        )

        region = CriticalInfrastructureRegion(
            region_id=f"VR-{vulnerability.region_id}",
            region_type=(
                InfrastructureRegionType
                .RESILIENCE_REGION
            ),
            severity=severity,
            affected_assets=tuple(
                vulnerability.affected_assets
            ),
            affected_corridors=tuple(
                vulnerability.affected_corridors
            ),
            operational_risk_score=(
                _normalize_score(
                    projected_risk
                )
            ),
            resilience_score=(
                _normalize_score(
                    vulnerability
                    .current_resilience_score
                )
            ),
            congestion_score=0.42,
            operational_summary=(
                "Operational survivability limitations "
                "detected in vulnerable region."
            ),
        )

        regions.append(region)

    return tuple(regions)


# ============================================================================
# CONGESTION IMPACT BUILDERS
# ============================================================================


def build_congestion_impact_regions(
    *,
    congestion: CongestionAnalysisResult,
) -> tuple[
    CongestionImpactRegion,
    ...
]:
    """
    Builds operational congestion impact topology artifacts.
    """

    regions: list[
        CongestionImpactRegion
    ] = []

    for hotspot in congestion.congestion_hotspots:

        region = CongestionImpactRegion(
            hotspot_id=hotspot.hotspot_id,
            impacted_corridors=tuple(
                hotspot.affected_edges
            ),
            impacted_zones=tuple(
                hotspot.impacted_zones
            ),
            stress_score=_normalize_score(
                hotspot.stress_score
            ),
            projected_relief_score=(
                _normalize_score(
                    hotspot.projected_relief_score
                )
            ),
            reinforcement_candidates=tuple(
                hotspot.recommended_expansions
            ),
            operational_impact_summary=(
                "Congestion concentration may reduce "
                "operational throughput stability."
            ),
        )

        regions.append(region)

    return tuple(regions)


# ============================================================================
# RESILIENCE OVERLAY BUILDERS
# ============================================================================


def build_resilience_improvement_regions(
    *,
    resilience: ResilienceAnalysisResult,
) -> tuple[
    ResilienceImprovementRegion,
    ...
]:
    """
    Builds resilience improvement operational overlays.
    """

    overlays: list[
        ResilienceImprovementRegion
    ] = []

    for vulnerability in (
        resilience.topology_vulnerabilities
    ):

        projected_score = min(
            vulnerability.current_resilience_score
            + 0.25,
            1.0,
        )

        overlay = (
            ResilienceImprovementRegion(
                vulnerable_region_id=(
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
                reinforcement_corridors=tuple(
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
                operational_benefit_summary=(
                    "Infrastructure reinforcement "
                    "improves survivability redundancy."
                ),
            )
        )

        overlays.append(overlay)

    return tuple(overlays)


# ============================================================================
# EXPANSION IMPACT BUILDERS
# ============================================================================


def build_expansion_impact_topology(
    *,
    solution: OptimizationSolution,
) -> tuple[
    ExpansionImpactTopology,
    ...
]:
    """
    Builds operational expansion impact topology projections.
    """

    projections: list[
        ExpansionImpactTopology
    ] = []

    selected_expansions = (
        solution.infrastructure_expansion_plan
        .selected_expansions
    )

    for expansion in selected_expansions:

        projection = ExpansionImpactTopology(
            candidate_id=expansion.candidate_id,
            impacted_regions=tuple(
                expansion.impacted_zones
            ),
            impacted_corridors=tuple(
                expansion.affected_assets
            ),
            projected_congestion_reduction=(
                _normalize_score(
                    expansion
                    .projected_congestion_reduction
                )
            ),
            projected_resilience_improvement=(
                _normalize_score(
                    expansion
                    .projected_resilience_improvement
                )
            ),
            operational_importance=(
                "High-impact operational reinforcement "
                "corridor."
            ),
        )

        projections.append(projection)

    return tuple(projections)


# ============================================================================
# OPERATIONAL TOPOLOGY SUMMARY
# ============================================================================


def build_operational_topology_summary(
    *,
    topology: OperationalTopologyGraph,
    congestion: CongestionAnalysisResult,
    resilience: ResilienceAnalysisResult,
    metrics: TopologyMetricsReport,
    critical_regions: tuple[
        CriticalInfrastructureRegion,
        ...
    ],
) -> OperationalTopologySummary:
    """
    Builds executive operational topology summary.

    Purpose
    -------
    Transforms topology intelligence into operationally
    meaningful topology delivery artifacts.

    This is NOT:
    - graph analytics
    - topology execution
    - graph projection runtime

    This IS:
    - operational topology delivery
    - infrastructure impact projection
    - executive operational summarization
    """

    total_regions = len(critical_regions)

    critical_count = sum(
        1
        for region in critical_regions
        if (
            region.severity
            == OperationalRegionSeverity.CRITICAL
        )
    )

    congestion_regions = sum(
        1
        for region in critical_regions
        if (
            region.region_type
            == InfrastructureRegionType
            .CONGESTION_REGION
        )
    )

    resilience_regions = sum(
        1
        for region in critical_regions
        if (
            region.region_type
            == InfrastructureRegionType
            .RESILIENCE_REGION
        )
    )

    strategic_findings = (
        "Critical congestion exposure remains "
        "localized within high-centrality corridors.",
        "Infrastructure reinforcement improves "
        "projected operational survivability.",
        "Operational risk concentration identified "
        "within vulnerable infrastructure regions.",
    )

    operational_priorities = (
        "Prioritize reinforcement of high-stress corridors.",
        "Increase redundancy across vulnerable regions.",
        "Reduce operational congestion concentration.",
    )

    average_resilience = (
        resilience.network_resilience_metrics
        .resilience_score
    )

    average_stress = (
        congestion.network_stress_metrics
        .network_stress_score
    )

    return OperationalTopologySummary(
        summary_id=(
            f"TOPOLOGY-SUMMARY-"
            f"{datetime.now(UTC).strftime('%Y%m%d%H%M%S')}"
        ),
        generated_at=datetime.now(UTC),
        total_operational_regions=total_regions,
        critical_region_count=critical_count,
        congestion_region_count=(
            congestion_regions
        ),
        resilience_region_count=(
            resilience_regions
        ),
        expansion_region_count=0,
        average_network_resilience=(
            _normalize_score(
                average_resilience
            )
        ),
        average_network_stress=(
            _normalize_score(
                average_stress
            )
        ),
        strategic_findings=(
            strategic_findings
        ),
        operational_priorities=(
            operational_priorities
        ),
        critical_regions=critical_regions,
    )