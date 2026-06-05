from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BaselineMetrics:
    """
    Baseline grid metrics extracted from the
    original network state before any expansion.
    """

    max_loading_percent: float

    average_loading_percent: float

    overloaded_line_count: int

    overload_severity: float

@dataclass(frozen=True)
class CandidateMetrics:
    """
    Physical grid metrics after applying
    a single candidate line.
    """

    max_loading_percent: float

    average_loading_percent: float

    overloaded_line_count: int

    overload_severity: float


@dataclass(frozen=True)
class CongestionReliefMetrics:
    """
    Delta metrics relative to the baseline state.
    """

    max_loading_reduction: float

    average_loading_reduction: float

    overloaded_line_reduction: int

    overload_severity_reduction: float


@dataclass(frozen=True)
class CandidateEvaluation:
    """
    Complete evaluation result for a candidate line.

    This artifact becomes the bridge between:
    - candidate generation
    - physical simulation
    - optimization
    """

    candidate_id: str

    baseline: BaselineMetrics

    candidate: CandidateMetrics

    relief: CongestionReliefMetrics

    objective_value: float

    evaluation_runtime_seconds: float

@dataclass(frozen=True)
class EvaluationDataset:

    baseline_metrics: BaselineMetrics

    evaluations: list[CandidateEvaluation]