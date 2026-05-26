from __future__ import annotations

from dataclasses import dataclass

import networkx as nx

from src.optimization.topology.graph import (
    GraphProjectionArtifacts,
)

from src.optimization.results.solution import (
    OptimizationSolution,
)


# =========================================================
# EDGE STRESS STATE
# =========================================================

@dataclass(frozen=True)
class CongestionEdgeState:
    """
    Canonical congestion state for topology edge.

    Represents:
    - infrastructure stress
    - congestion pressure
    - utilization estimation
    """

    edge_id: str

    from_node: str
    to_node: str

    utilization_ratio: float

    congestion_score: float

    critical: bool


# =========================================================
# CONGESTION HOTSPOT
# =========================================================

@dataclass(frozen=True)
class CongestionHotspot:
    """
    Canonical congestion hotspot.

    Represents:
    - stressed transmission corridor
    - critical operational bottleneck
    """

    hotspot_id: str

    affected_edges: list[str]

    average_congestion_score: float

    severity_level: str


# =========================================================
# NETWORK STRESS METRICS
# =========================================================

@dataclass(frozen=True)
class NetworkStressMetrics:
    """
    Graph-level network congestion metrics.
    """

    average_network_stress: float

    max_network_stress: float

    num_critical_edges: int

    congestion_distribution_score: float


# =========================================================
# EXPANSION RELIEF IMPACT
# =========================================================

@dataclass(frozen=True)
class ExpansionReliefImpact:
    """
    Infrastructure expansion congestion relief impact.
    """

    candidate_id: str

    relief_score: float

    estimated_stress_reduction: float

    strategic_importance: float


# =========================================================
# CANONICAL CONGESTION ANALYSIS
# =========================================================

@dataclass(frozen=True)
class CongestionAnalysisResult:
    """
    Canonical congestion intelligence artifact.

    Represents:
    - topology congestion reasoning
    - infrastructure stress analysis
    - reinforcement intelligence
    """

    edge_states: list[
        CongestionEdgeState
    ]

    hotspots: list[
        CongestionHotspot
    ]

    network_stress_metrics: (
        NetworkStressMetrics
    )

    expansion_relief_impacts: list[
        ExpansionReliefImpact
    ]


# =========================================================
# EDGE STRESS ANALYSIS
# =========================================================

def compute_edge_congestion_score(
    graph: nx.Graph,
    from_node: str,
    to_node: str,
) -> float:
    """
    Compute heuristic congestion score.

    Current phase:
    - topology-aware
    - centrality-informed
    - graph-native heuristic
    """

    edge_betweenness = (
        nx.edge_betweenness_centrality(
            graph
        )
    )

    return edge_betweenness.get(
        (from_node, to_node),
        edge_betweenness.get(
            (to_node, from_node),
            0.0,
        ),
    )


def build_congestion_edge_states(
    projection: GraphProjectionArtifacts,
) -> list[CongestionEdgeState]:
    """
    Build canonical edge stress states.
    """

    graph = projection.networkx_graph

    edge_states = []

    for (
        from_node,
        to_node,
        edge_data,
    ) in graph.edges(data=True):

        congestion_score = (
            compute_edge_congestion_score(
                graph,
                from_node,
                to_node,
            )
        )

        utilization_ratio = min(
            congestion_score * 4.0,
            1.0,
        )

        critical = (
            utilization_ratio >= 0.75
        )

        edge_states.append(
            CongestionEdgeState(
                edge_id=edge_data.get(
                    "edge_id",
                    f"{from_node}_{to_node}",
                ),

                from_node=from_node,

                to_node=to_node,

                utilization_ratio=(
                    utilization_ratio
                ),

                congestion_score=(
                    congestion_score
                ),

                critical=critical,
            )
        )

    return edge_states


# =========================================================
# HOTSPOT ANALYSIS
# =========================================================

def identify_congestion_hotspots(
    edge_states: list[
        CongestionEdgeState
    ],
) -> list[CongestionHotspot]:
    """
    Identify critical congestion hotspots.
    """

    critical_edges = [
        edge
        for edge in edge_states
        if edge.critical
    ]

    if not critical_edges:
        return []

    average_score = (
        sum(
            edge.congestion_score
            for edge in critical_edges
        )
        / len(critical_edges)
    )

    severity_level = (
        "HIGH"
        if average_score >= 0.3
        else "MODERATE"
    )

    hotspot = CongestionHotspot(
        hotspot_id="primary_hotspot",

        affected_edges=[
            edge.edge_id
            for edge in critical_edges
        ],

        average_congestion_score=(
            average_score
        ),

        severity_level=severity_level,
    )

    return [hotspot]


# =========================================================
# NETWORK STRESS ANALYSIS
# =========================================================

def compute_network_stress_metrics(
    edge_states: list[
        CongestionEdgeState
    ],
) -> NetworkStressMetrics:
    """
    Compute graph-level congestion metrics.
    """

    if not edge_states:

        return NetworkStressMetrics(
            average_network_stress=0.0,

            max_network_stress=0.0,

            num_critical_edges=0,

            congestion_distribution_score=0.0,
        )

    stress_values = [
        edge.utilization_ratio
        for edge in edge_states
    ]

    average_stress = (
        sum(stress_values)
        / len(stress_values)
    )

    max_stress = max(stress_values)

    critical_edges = [
        edge
        for edge in edge_states
        if edge.critical
    ]

    congestion_distribution = (
        len(critical_edges)
        / len(edge_states)
    )

    return NetworkStressMetrics(
        average_network_stress=(
            average_stress
        ),

        max_network_stress=(
            max_stress
        ),

        num_critical_edges=(
            len(critical_edges)
        ),

        congestion_distribution_score=(
            congestion_distribution
        ),
    )


# =========================================================
# EXPANSION RELIEF ANALYSIS
# =========================================================

def score_expansion_relief(
    solution: OptimizationSolution,
) -> list[ExpansionReliefImpact]:
    """
    Score congestion relief contribution
    from selected infrastructure expansions.
    """

    impacts = []

    for expansion in (
        solution
        .expansion_plan
        .selected_expansions
    ):

        relief_score = (
            expansion.capacity_mva
            /
            max(
                expansion.build_cost,
                1.0,
            )
        ) * 1000

        estimated_stress_reduction = min(
            relief_score * 0.2,
            1.0,
        )

        strategic_importance = (
            expansion.decision_score
            *
            estimated_stress_reduction
        )

        impacts.append(
            ExpansionReliefImpact(
                candidate_id=(
                    expansion.candidate_id
                ),

                relief_score=(
                    relief_score
                ),

                estimated_stress_reduction=(
                    estimated_stress_reduction
                ),

                strategic_importance=(
                    strategic_importance
                ),
            )
        )

    return impacts


# =========================================================
# PUBLIC CONGESTION API
# =========================================================

def analyze_topology_congestion(
    projection: GraphProjectionArtifacts,
    solution: OptimizationSolution,
) -> CongestionAnalysisResult:
    """
    Canonical topology congestion analysis API.

    Converts:
        operational topology
            ↓
        congestion intelligence
            ↓
        reinforcement reasoning
    """

    edge_states = (
        build_congestion_edge_states(
            projection
        )
    )

    hotspots = (
        identify_congestion_hotspots(
            edge_states
        )
    )

    stress_metrics = (
        compute_network_stress_metrics(
            edge_states
        )
    )

    relief_impacts = (
        score_expansion_relief(
            solution
        )
    )

    return CongestionAnalysisResult(
        edge_states=edge_states,

        hotspots=hotspots,

        network_stress_metrics=(
            stress_metrics
        ),

        expansion_relief_impacts=(
            relief_impacts
        ),
    )