from dataclasses import dataclass

@dataclass(frozen=True)
class CandidateLine:

    candidate_id: str

    from_bus: int
    to_bus: int

    length_km: float

    reference_line_id: int

    build_cost: float

@dataclass
class DecisionSpace:
    candidate_lines: list[CandidateLine]