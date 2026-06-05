from __future__ import annotations

from dataclasses import dataclass

import networkx as nx

from src.optimization.topology.graph import (
    GraphProjectionArtifacts,
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

    bridge_edges = set(nx.bridges(graph))
    edge_betweenness = nx.edge_betweenness_centrality(graph)

    aggregated: dict[tuple[str, str], CriticalInfrastructureEdge] = {}

    for (from_node, to_node, edge_data) in graph.edges(data=True):
        u, v = sorted([str(from_node), str(to_node)])
        key = (u, v)

        bridge_edge = ((from_node, to_node) in bridge_edges) or ((to_node, from_node) in bridge_edges)

        betweenness_score = edge_betweenness.get((from_node, to_node), edge_betweenness.get((to_node, from_node), 0.0))

        criticality_score = betweenness_score * (2.0 if bridge_edge else 1.0)

        if criticality_score < 0.1:
            continue

        edge_id = edge_data.get("edge_id", f"{u}_{v}")

        existing = aggregated.get(key)
        if existing is None:
            aggregated[key] = CriticalInfrastructureEdge(
                edge_id=edge_id,
                from_node=u,
                to_node=v,
                bridge_edge=bridge_edge,
                edge_betweenness=betweenness_score,
                criticality_score=criticality_score,
            )
        else:
            # merge: OR bridge flag, take max betweenness & criticality
            merged_bridge = existing.bridge_edge or bridge_edge
            merged_betweenness = max(existing.edge_betweenness, betweenness_score)
            merged_criticality = max(existing.criticality_score, criticality_score)

            aggregated[key] = CriticalInfrastructureEdge(
                edge_id=existing.edge_id or edge_id,
                from_node=u,
                to_node=v,
                bridge_edge=merged_bridge,
                edge_betweenness=merged_betweenness,
                criticality_score=merged_criticality,
            )

    return list(aggregated.values())


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

    vulnerabilities_map: dict[str, TopologyVulnerability] = {}

    for node in articulation_points:
        degree = graph.degree(node)

        fragmentation_risk = min(degree / 10.0, 1.0)

        severity_level = "HIGH" if fragmentation_risk >= 0.5 else "MODERATE"

        connected_edges = [f"{node}_{neighbor}" for neighbor in graph.neighbors(node)]

        vuln_id = f"vulnerability_{node}"

        existing = vulnerabilities_map.get(vuln_id)
        if existing is None:
            vulnerabilities_map[vuln_id] = TopologyVulnerability(
                vulnerability_id=vuln_id,
                affected_nodes=[node],
                affected_edges=connected_edges,
                fragmentation_risk=fragmentation_risk,
                severity_level=severity_level,
            )
        else:
            # merge sets
            merged_nodes = list(dict.fromkeys(existing.affected_nodes + [node]))
            merged_edges = list(dict.fromkeys(existing.affected_edges + connected_edges))
            merged_risk = max(existing.fragmentation_risk, fragmentation_risk)
            merged_severity = existing.severity_level if existing.severity_level == "HIGH" else severity_level

            vulnerabilities_map[vuln_id] = TopologyVulnerability(
                vulnerability_id=vuln_id,
                affected_nodes=merged_nodes,
                affected_edges=merged_edges,
                fragmentation_risk=merged_risk,
                severity_level=merged_severity,
            )

    return list(vulnerabilities_map.values())