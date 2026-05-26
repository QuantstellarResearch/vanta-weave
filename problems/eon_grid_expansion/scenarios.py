"""
Scenario semantics for the E.ON grid expansion problem.

This module defines future operational contexts used for
grid expansion planning, congestion stress analysis,
and benchmark generation.

IMPORTANT:
- This layer is semantic-only.
- No simulation logic belongs here.
- No Pyomo/QUBO/solver logic belongs here.
- No runtime execution logic belongs here.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ScenarioContext:
    """
    Declarative description of a future grid operating condition.

    Scenarios represent stressed or evolving operational futures
    used for expansion planning and optimization benchmarking.
    """

    scenario_id: str
    name: str

    load_growth_factor: float

    renewable_generation_factor: float

    regional_stress_factor: float

    line_outage_probability: float

    description: str