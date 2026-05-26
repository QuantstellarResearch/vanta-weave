from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProblemMetadata:
    problem_id: str
    name: str

    dataset_name: str
    source_network: str

    scenario_id: str
    stress_level: float

    num_candidate_lines: int

    created_at: datetime