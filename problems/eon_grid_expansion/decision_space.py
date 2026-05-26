from dataclasses import dataclass

@dataclass(frozen=True)
class CandidateLine:
    candidate_id: str

    from_bus: str
    to_bus: str

    capacity_mva: float
    build_cost: float

    length_km: float
    voltage_kv: float


@dataclass
class DecisionSpace:
    candidate_lines: list[CandidateLine]