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
# CRITICAL INFRASTRUCTURE EDGE
# =========================================================

@dataclass(frozen=True)
class CriticalInfrastructureEdge:
    """
    Canonical critical infrastructure edge.

    Represents:
    - fragile transmission corridor
    - operationally important edge
    - survivability-sensitive connection

    IMPORTANT:
    This is topology intelligence,
    not physical power-flow simulation.
    """

    edge_id: str

    from_node: str
    to_node: str

    bridge_edge: bool

    edge_betweenness: float

    criticality_score: float


# =========================================================
# TOPOLOGY VULNERABILITY
# =========================================================

@dataclass(frozen=True)
class TopologyVulnerability:
    """
    Canonical topology vulnerability artifact.

    Represents:
    - structural fragility
    - graph fragmentation risk
    - infrastructure survivability weakness
    """

    vulnerability_id: str

    affected_nodes: list[str]

    affected_edges: list[str]

    fragmentation_risk: float

    severity_level: str


# =========================================================
# NETWORK RESILIENCE METRICS
# =========================================================

@dataclass(frozen=True)
class NetworkResilienceMetrics:
    """
    Canonical graph-level resilience metrics.

    Represents:
    - overall network survivability
    - redundancy quality
    - graph robustness
    """

    network_connectivity_score: float

    redundancy_score: float

    resilience_score: float

    num_critical_edges: int

    num_articulation_points: int


# =========================================================
# EXPANSION RESILIENCE IMPACT
# =========================================================

@dataclass(frozen=True)
class ExpansionResilienceImpact:
    """
    Infrastructure expansion survivability impact.

    Represents:
    - resilience reinforcement contribution
    - survivability improvement estimation
    """

    candidate_id: str

    resilience_gain_score: float

    redundancy_improvement: float

    survivability_contribution: float


# =========================================================
# CANONICAL RESILIENCE ANALYSIS
# =========================================================

@dataclass(frozen=True)
class ResilienceAnalysisResult:
    """
    Canonical infrastructure survivability artifact.

    Represents:
    - topology resilience reasoning
    - survivability intelligence
    - infrastructure robustness analysis
    """

    critical_edges: list[
        CriticalInfrastructureEdge
    ]

    vulnerabilities: list[
        TopologyVulnerability
    ]

    resilience_metrics: (
        NetworkResilienceMetrics
    )

    expansion_impacts: list[
        ExpansionResilienceImpact
    ]


# =========================================================
# CRITICAL EDGE ANALYSIS
# =========================================================

def identify_critical_infrastructure_edges(
    projection: GraphProjectionArtifacts,
) -> list[CriticalInfrastructureEdge]:
    """
    Identify operationally critical infrastructure edges.

    Current strategy:
    - graph-native
    - topology-aware
    - centrality-informed
    """

    graph = projection.networkx_graph

    bridge_edges = set(
        nx.bridges(graph)
    )

    edge_betweenness = (
        nx.edge_betweenness_centrality(
            graph
        )
    )

    critical_edges = []

    for (
        from_node,
        to_node,
        edge_data,
    ) in graph.edges(data=True):

        bridge_edge = (
            (from_node, to_node)
            in bridge_edges
        ) or (
            (to_node, from_node)
            in bridge_edges
        )

        betweenness_score = (
            edge_betweenness.get(
                (from_node, to_node),
                edge_betweenness.get(
                    (to_node, from_node),
                    0.0,
                ),
            )
        )

        criticality_score = (
            betweenness_score
            * (2.0 if bridge_edge else 1.0)
        )

        if criticality_score >= 0.1:

            critical_edges.append(
                CriticalInfrastructureEdge(
                    edge_id=edge_data.get(
                        "edge_id",
                        f"{from_node}_{to_node}",
                    ),

                    from_node=from_node,

                    to_node=to_node,

                    bridge_edge=bridge_edge,

                    edge_betweenness=(
                        betweenness_score
                    ),

                    criticality_score=(
                        criticality_score
                    ),
                )
            )

    return critical_edges


# =========================================================
# TOPOLOGY VULNERABILITY ANALYSIS
# =========================================================

def analyze_topology_vulnerabilities(
    projection: GraphProjectionArtifacts,
) -> list[TopologyVulnerability]:
    """
    Analyze structural topology vulnerabilities.

    Current phase:
    - articulation-point analysis
    - fragmentation-risk heuristics
    """

    graph = projection.networkx_graph

    articulation_points = list(
        nx.articulation_points(graph)
    )

    vulnerabilities = []

    for node in articulation_points:

        degree = graph.degree(node)

        fragmentation_risk = min(
            degree / 10.0,
            1.0,
        )

        severity_level = (
            "HIGH"
            if fragmentation_risk >= 0.5
            else "MODERATE"
        )

        connected_edges = []

        for neighbor in graph.neighbors(node):

            connected_edges.append(
                f"{node}_{neighbor}"
            )

        vulnerabilities.append(
            TopologyVulnerability(
                vulnerability_id=(
                    f"vulnerability_{node}"
                ),

                affected_nodes=[node],

                affected_edges=connected_edges,

                fragmentation_risk=(
                    fragmentation_risk
                ),

                severity_level=(
                    severity_level
                ),
            )
        )

    return vulnerabilities


# =========================================================
# NETWORK RESILIENCE METRICS
# =========================================================

def compute_network_resilience_metrics(
    projection: GraphProjectionArtifacts,
    critical_edges: list[
        CriticalInfrastructureEdge
    ],
) -> NetworkResilienceMetrics:
    """
    Compute graph-level resilience metrics.

    Current phase:
    - structural survivability
    - topology robustness
    - redundancy heuristics
    """

    graph = projection.networkx_graph

    connectivity_score = nx.node_connectivity(
        graph
    )

    density_score = nx.density(graph)

    articulation_points = list(
        nx.articulation_points(graph)
    )

    resilience_score = (
        (
            connectivity_score
            * 0.5
        )
        +
        (
            density_score
            * 0.5
        )
    )

    return NetworkResilienceMetrics(
        network_connectivity_score=float(
            connectivity_score
        ),

        redundancy_score=float(
            density_score
        ),

        resilience_score=float(
            resilience_score
        ),

        num_critical_edges=len(
            critical_edges
        ),

        num_articulation_points=len(
            articulation_points
        ),
    )


# =========================================================
# EXPANSION RESILIENCE ANALYSIS
# =========================================================

def score_expansion_resilience(
    solution: OptimizationSolution,
) -> list[ExpansionResilienceImpact]:
    """
    Score survivability contribution from
    selected infrastructure expansions.

    Current phase:
    heuristic resilience estimation.
    """

    impacts = []

    for expansion in (
        solution
        .expansion_plan
        .selected_expansions
    ):

        redundancy_improvement = min(
            expansion.capacity_mva / 1000.0,
            1.0,
        )

        resilience_gain = (
            expansion.decision_score
            * redundancy_improvement
        )

        survivability_contribution = (
            resilience_gain * 1.25
        )

        impacts.append(
            ExpansionResilienceImpact(
                candidate_id=(
                    expansion.candidate_id
                ),

                resilience_gain_score=(
                    resilience_gain
                ),

                redundancy_improvement=(
                    redundancy_improvement
                ),

                survivability_contribution=(
                    survivability_contribution
                ),
            )
        )

    return impacts


# =========================================================
# PUBLIC RESILIENCE API
# =========================================================

def analyze_network_resilience(
    projection: GraphProjectionArtifacts,
    solution: OptimizationSolution,
) -> ResilienceAnalysisResult:
    """
    Canonical infrastructure survivability API.

    Converts:
        operational topology
            ↓
        survivability intelligence
            ↓
        infrastructure resilience reasoning

    IMPORTANT:
    This layer is:
    - graph-native
    - heuristic-first
    - explainable
    - optimization-compatible

    NOT:
    - nonlinear contingency simulation
    - AC power system engine
    """

    critical_edges = (
        identify_critical_infrastructure_edges(
            projection
        )
    )

    vulnerabilities = (
        analyze_topology_vulnerabilities(
            projection
        )
    )

    resilience_metrics = (
        compute_network_resilience_metrics(
            projection,
            critical_edges,
        )
    )

    expansion_impacts = (
        score_expansion_resilience(
            solution
        )
    )

    return ResilienceAnalysisResult(
        critical_edges=critical_edges,

        vulnerabilities=vulnerabilities,

        resilience_metrics=(
            resilience_metrics
        ),

        expansion_impacts=(
            expansion_impacts
        ),
    )