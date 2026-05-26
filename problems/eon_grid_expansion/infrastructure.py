from dataclasses import dataclass
from vanta_lattice.domains.energy.models import (
    BusNode,
    LineEdge,
    LoadNode,
    GeneratorNode
)


@dataclass(frozen=True)
class InfrastructureState:
    buses: list[BusNode]
    lines: list[LineEdge]
    loads: list[LoadNode]
    generators: list[GeneratorNode]