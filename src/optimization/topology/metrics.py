from __future__ import annotations

from dataclasses import dataclass

import networkx as nx

from src.optimization.topology.graph import (
    GraphProjectionArtifacts,
)

from src.optimization.results.solution import (
    OptimizationSolution,
)

from src.optimization.topology.congestion import (
    CongestionAnalysisResult,
)

from src.optimization.topology.resilience import (
    ResilienceAnalysisResult,
)


# =========================================================
# TOPOLOGY CENTRALITY METRICS
# =========================================================

@dataclass(frozen=True)
class TopologyCentralityMetrics:
    """
    Canonical topology centrality metrics.

    Represents:
    - structural importance
    - topology influence
    - graph-central infrastructure regions
    """

    average_degree_centrality: float

    max_degree_centrality: float

    average_betweenness_centrality: float

    max_betweenness_centrality: float


# =========================================================
# NETWORK EFFICIENCY METRICS
# =========================================================

@dataclass(frozen=True)
class NetworkEfficiencyMetrics:
    """
    Canonical operational network efficiency metrics.

    Represents:
    - topology flow quality
    - operational path efficiency
    - graph-level infrastructure performance
    """

    average_shortest_path_length: float

    graph_density: float

    network_efficiency_score: float


# =========================================================
# INFRASTRUCTURE ROBUSTNESS METRICS
# =========================================================

@dataclass(frozen=True)
class InfrastructureRobustnessMetrics:
    """
    Canonical infrastructure survivability metrics.

    Represents:
    - operational robustness
    - survivability quality
    - topology redundancy
    """

    resilience_score: float

    congestion_stability_score: float

    critical_edge_ratio: float

    articulation_point_ratio: float


# =========================================================
# EXPANSION EFFECTIVENESS METRICS
# =========================================================

@dataclass(frozen=True)
class ExpansionEffectivenessMetrics:
    """
    Canonical expansion reinforcement metrics.

    Represents:
    - infrastructure reinforcement quality
    - congestion relief contribution
    - survivability improvement effectiveness
    """

    average_expansion_capacity: float

    average_expansion_cost_efficiency: float

    average_resilience_gain: float

    average_relief_score: float


# =========================================================
# TOPOLOGY METRICS REPORT
# =========================================================

@dataclass(frozen=True)
class TopologyMetricsReport:
    """
    Canonical operational topology KPI artifact.

    Represents:
    - graph intelligence KPIs
    - operational infrastructure metrics
    - benchmarkable topology intelligence
    """

    centrality_metrics: (
        TopologyCentralityMetrics
    )

    efficiency_metrics: (
        NetworkEfficiencyMetrics
    )

    robustness_metrics: (
        InfrastructureRobustnessMetrics
    )

    expansion_metrics: (
        ExpansionEffectivenessMetrics
    )


# =========================================================
# CENTRALITY ANALYSIS
# =========================================================

def compute_topology_centrality(
    projection: GraphProjectionArtifacts,
) -> TopologyCentralityMetrics:
    """
    Compute graph-central infrastructure metrics.

    Current strategy:
    - graph-native
    - topology-aware
    - infrastructure-centric
    """

    graph = projection.networkx_graph

    degree_centrality = (
        nx.degree_centrality(graph)
    )

    betweenness_centrality = (
        nx.betweenness_centrality(graph)
    )

    average_degree = (
        sum(degree_centrality.values())
        / len(degree_centrality)
        if degree_centrality
        else 0.0
    )

    average_betweenness = (
        sum(
            betweenness_centrality.values()
        )
        / len(betweenness_centrality)
        if betweenness_centrality
        else 0.0
    )

    return TopologyCentralityMetrics(
        average_degree_centrality=(
            average_degree
        ),

        max_degree_centrality=max(
            degree_centrality.values(),
            default=0.0,
        ),

        average_betweenness_centrality=(
            average_betweenness
        ),

        max_betweenness_centrality=max(
            betweenness_centrality.values(),
            default=0.0,
        ),
    )


# =========================================================
# NETWORK EFFICIENCY ANALYSIS
# =========================================================

def compute_network_efficiency(
    projection: GraphProjectionArtifacts,
) -> NetworkEfficiencyMetrics:
    """
    Compute operational topology efficiency metrics.

    Current phase:
    graph-structural efficiency estimation.
    """

    graph = projection.networkx_graph

    density = nx.density(graph)

    if nx.is_connected(graph):

        avg_shortest_path = (
            nx.average_shortest_path_length(
                graph
            )
        )

    else:
        avg_shortest_path = float(
            graph.number_of_nodes()
        )

    efficiency_score = (
        density
        /
        max(avg_shortest_path, 1.0)
    )

    return NetworkEfficiencyMetrics(
        average_shortest_path_length=(
            avg_shortest_path
        ),

        graph_density=density,

        network_efficiency_score=(
            efficiency_score
        ),
    )


# =========================================================
# ROBUSTNESS ANALYSIS
# =========================================================

def compute_infrastructure_robustness(
    projection: GraphProjectionArtifacts,
    congestion_analysis: (
        CongestionAnalysisResult
    ),
    resilience_analysis: (
        ResilienceAnalysisResult
    ),
) -> InfrastructureRobustnessMetrics:
    """
    Compute survivability and robustness KPIs.
    """

    graph = projection.networkx_graph

    num_edges = max(
        graph.number_of_edges(),
        1,
    )

    num_nodes = max(
        graph.number_of_nodes(),
        1,
    )

    critical_edge_ratio = (
        resilience_analysis
        .resilience_metrics
        .num_critical_edges
        / num_edges
    )

    articulation_point_ratio = (
        resilience_analysis
        .resilience_metrics
        .num_articulation_points
        / num_nodes
    )

    congestion_stability_score = (
        1.0
        -
        congestion_analysis
        .network_stress_metrics
        .average_network_stress
    )

    return InfrastructureRobustnessMetrics(
        resilience_score=(
            resilience_analysis
            .resilience_metrics
            .resilience_score
        ),

        congestion_stability_score=(
            congestion_stability_score
        ),

        critical_edge_ratio=(
            critical_edge_ratio
        ),

        articulation_point_ratio=(
            articulation_point_ratio
        ),
    )


# =========================================================
# EXPANSION EFFECTIVENESS ANALYSIS
# =========================================================

def compute_expansion_effectiveness(
    solution: OptimizationSolution,
    congestion_analysis: (
        CongestionAnalysisResult
    ),
    resilience_analysis: (
        ResilienceAnalysisResult
    ),
) -> ExpansionEffectivenessMetrics:
    """
    Compute infrastructure reinforcement effectiveness.

    Represents:
    - reinforcement quality
    - survivability improvement
    - congestion relief contribution
    """

    expansions = (
        solution
        .expansion_plan
        .selected_expansions
    )

    if not expansions:

        return ExpansionEffectivenessMetrics(
            average_expansion_capacity=0.0,

            average_expansion_cost_efficiency=0.0,

            average_resilience_gain=0.0,

            average_relief_score=0.0,
        )

    average_capacity = (
        sum(
            expansion.capacity_mva
            for expansion in expansions
        )
        / len(expansions)
    )

    average_cost_efficiency = (
        sum(
            (
                expansion.capacity_mva
                /
                max(
                    expansion.build_cost,
                    1.0,
                )
            )
            for expansion in expansions
        )
        / len(expansions)
    )

    average_resilience_gain = (
        sum(
            impact.resilience_gain_score
            for impact in (
                resilience_analysis
                .expansion_impacts
            )
        )
        / max(
            len(
                resilience_analysis
                .expansion_impacts
            ),
            1,
        )
    )

    average_relief_score = (
        sum(
            impact.relief_score
            for impact in (
                congestion_analysis
                .expansion_relief_impacts
            )
        )
        / max(
            len(
                congestion_analysis
                .expansion_relief_impacts
            ),
            1,
        )
    )

    return ExpansionEffectivenessMetrics(
        average_expansion_capacity=(
            average_capacity
        ),

        average_expansion_cost_efficiency=(
            average_cost_efficiency
        ),

        average_resilience_gain=(
            average_resilience_gain
        ),

        average_relief_score=(
            average_relief_score
        ),
    )


# =========================================================
# PUBLIC METRICS API
# =========================================================

def build_topology_metrics_report(
    projection: GraphProjectionArtifacts,
    solution: OptimizationSolution,
    congestion_analysis: (
        CongestionAnalysisResult
    ),
    resilience_analysis: (
        ResilienceAnalysisResult
    ),
) -> TopologyMetricsReport:
    """
    Canonical operational topology KPI pipeline.

    Converts:
        topology intelligence
            ↓
        infrastructure KPIs
            ↓
        benchmarkable operational metrics

    IMPORTANT:
    This layer is:
    - graph-native
    - deterministic
    - explainable
    - optimization-compatible

    NOT:
    - raw graph metric dumping
    - visualization logic
    """

    centrality_metrics = (
        compute_topology_centrality(
            projection
        )
    )

    efficiency_metrics = (
        compute_network_efficiency(
            projection
        )
    )

    robustness_metrics = (
        compute_infrastructure_robustness(
            projection,
            congestion_analysis,
            resilience_analysis,
        )
    )

    expansion_metrics = (
        compute_expansion_effectiveness(
            solution,
            congestion_analysis,
            resilience_analysis,
        )
    )

    return TopologyMetricsReport(
        centrality_metrics=(
            centrality_metrics
        ),

        efficiency_metrics=(
            efficiency_metrics
        ),

        robustness_metrics=(
            robustness_metrics
        ),

        expansion_metrics=(
            expansion_metrics
        ),
    )