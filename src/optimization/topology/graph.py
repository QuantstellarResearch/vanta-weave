from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import networkx as nx

from problems.eon_grid_expansion.infrastructure import (
    InfrastructureState,
)

from problems.eon_grid_expansion.decision_space import (
    CandidateLine,
)

from src.optimization.results.solution import (
    OptimizationSolution,
)


# =========================================================
# TOPOLOGY NODE
# =========================================================

@dataclass(frozen=True)
class TopologyNode:
    """
    Canonical infrastructure topology node.

    Represents:
    - operational bus
    - infrastructure node
    - graph projection vertex
    """

    node_id: str

    voltage_kv: float

    region: str | None = None


# =========================================================
# TOPOLOGY EDGE
# =========================================================

@dataclass(frozen=True)
class TopologyEdge:
    """
    Canonical infrastructure topology edge.

    Represents:
    - operational transmission line
    - infrastructure connectivity
    - graph relationship
    """

    edge_id: str

    from_node: int
    to_node: int

    capacity_mva: float

    active: bool = True


# =========================================================
# EXPANSION OVERLAY
# =========================================================

@dataclass(frozen=True)
class CandidateExpansionOverlay:
    """
    Candidate infrastructure expansion overlay.

    Represents:
    - optional future transmission lines
    - optimization action space
    """

    candidate_id: str

    from_node: str
    to_node: str

    capacity_mva: float

    build_cost: float


# =========================================================
# CANONICAL GRAPH
# =========================================================

@dataclass(frozen=True)
class OperationalTopologyGraph:
    """
    Canonical operational infrastructure graph.

    IMPORTANT:
    This layer is:
    - graph-runtime-agnostic
    - infrastructure-centric
    - canonical

    NOT:
    - NetworkX-specific
    - Neo4j-specific
    """

    nodes: list[TopologyNode]

    edges: list[TopologyEdge]

    candidate_overlays: list[
        CandidateExpansionOverlay
    ]


# =========================================================
# RUNTIME GRAPH PROJECTION
# =========================================================

@dataclass(frozen=True)
class GraphProjectionArtifacts:
    """
    Runtime graph projection artifacts.
    """

    topology_graph: (
        OperationalTopologyGraph
    )

    networkx_graph: nx.Graph


# =========================================================
# NODE BUILDERS
# =========================================================

def build_topology_nodes(
    infrastructure: InfrastructureState,
) -> list[TopologyNode]:
    """
    Build canonical topology nodes from infrastructure.
    """

    topology_nodes = []

    for bus in infrastructure.buses:

        topology_nodes.append(
            TopologyNode(
                node_id=bus.bus_id,

                voltage_kv=bus.voltage_kv,

                region=getattr(
                    bus,
                    "region",
                    None,
                ),
            )
        )

    return topology_nodes


# =========================================================
# EDGE BUILDERS
# =========================================================

def build_topology_edges(
    infrastructure: InfrastructureState,
) -> list[TopologyEdge]:
    """
    Build canonical operational topology edges.
    """

    topology_edges = []

    for line in infrastructure.lines:

        topology_edges.append(
            TopologyEdge(
                edge_id=line.line_id,

                from_node=line.from_bus,

                to_node=line.to_bus,

                capacity_mva=line.capacity_mva,

                active=True,
            )
        )

    return topology_edges


# =========================================================
# CANDIDATE OVERLAY BUILDERS
# =========================================================

def build_candidate_overlays(
    candidate_lines: Iterable[
        CandidateLine
    ],
) -> list[CandidateExpansionOverlay]:
    """
    Build candidate infrastructure overlays.
    """

    overlays = []

    for candidate in candidate_lines:

        overlays.append(
            CandidateExpansionOverlay(
                candidate_id=(
                    candidate.candidate_id
                ),

                from_node=(
                    candidate.from_bus
                ),

                to_node=(
                    candidate.to_bus
                ),

                capacity_mva=(
                    candidate.capacity_mva
                ),

                build_cost=(
                    candidate.build_cost
                ),
            )
        )

    return overlays


# =========================================================
# GRAPH BUILDERS
# =========================================================

def build_operational_graph(
    infrastructure: InfrastructureState,
    candidate_lines: Iterable[
        CandidateLine
    ],
) -> OperationalTopologyGraph:
    """
    Build canonical operational topology graph.
    """

    return OperationalTopologyGraph(
        nodes=build_topology_nodes(
            infrastructure
        ),

        edges=build_topology_edges(
            infrastructure
        ),

        candidate_overlays=(
            build_candidate_overlays(
                candidate_lines
            )
        ),
    )


# =========================================================
# NETWORKX PROJECTION
# =========================================================

def project_to_networkx(
    topology_graph: (
        OperationalTopologyGraph
    ),
) -> GraphProjectionArtifacts:
    """
    Project canonical topology graph into
    executable NetworkX graph runtime.
    """

    graph = nx.Graph()

    for node in topology_graph.nodes:

        graph.add_node(
            node.node_id,

            voltage_kv=node.voltage_kv,

            region=node.region,
        )

    for edge in topology_graph.edges:

        graph.add_edge(
            edge.from_node,
            edge.to_node,

            edge_id=edge.edge_id,

            capacity_mva=edge.capacity_mva,

            active=edge.active,
        )

    return GraphProjectionArtifacts(
        topology_graph=topology_graph,

        networkx_graph=graph,
    )


# =========================================================
# EXPANSION PLAN PROJECTION
# =========================================================

def project_solution_overlay(
    projection: GraphProjectionArtifacts,
    solution: OptimizationSolution,
) -> nx.Graph:
    """
    Project selected infrastructure expansion
    decisions onto graph runtime.
    """

    graph = projection.networkx_graph.copy()

    for expansion in (
        solution
        .expansion_plan
        .selected_expansions
    ):

        graph.add_edge(
            expansion.from_bus,
            expansion.to_bus,

            candidate_id=(
                expansion.candidate_id
            ),

            capacity_mva=(
                expansion.capacity_mva
            ),

            build_cost=(
                expansion.build_cost
            ),

            expansion_selected=True,
        )

    return graph