from dataclasses import dataclass
from vanta_lattice.domains.energy.models import (
    BusNode,
    LineEdge,
    LoadNode,
    GeneratorNode,
    LineFlow,
    BusState,
)


@dataclass(frozen=True)
class InfrastructureState:
    buses: list[BusNode]
    bus_states: list[BusState]
    lines: list[LineEdge]
    line_flows: list[LineFlow]
    loads: list[LoadNode]
    generators: list[GeneratorNode]
