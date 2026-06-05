from __future__ import annotations

from src.evaluation.models import (
    BaselineMetrics,
    CandidateMetrics,
    CongestionReliefMetrics,
)


# =========================================================
# BASIC LOADING METRICS
# =========================================================

def compute_max_loading_percent(
    line_flows,
) -> float:
    """
    Compute the maximum line loading percentage.

    Represents the worst congestion point
    in the network.
    """

    if not line_flows:
        return 0.0

    return max(
        float(flow.loading_percent)
        for flow in line_flows
    )


def compute_average_loading_percent(
    line_flows,
) -> float:
    """
    Compute the average loading percentage
    across all transmission lines.
    """

    if not line_flows:
        return 0.0

    return (
        sum(
            float(flow.loading_percent)
            for flow in line_flows
        )
        / len(line_flows)
    )


def compute_overload_severity(
    line_flows,
    threshold: float = 100.0,
) -> float:

    severity = 0.0

    for flow in line_flows:

        loading = float(
            flow.loading_percent
        )

        severity += max(
            0.0,
            loading - threshold,
        )

    return severity


def count_overloaded_lines(
    line_flows,
    threshold: float = 100.0,
) -> int:
    """
    Count lines whose loading exceeds
    the overload threshold.
    """

    return sum(
        1
        for flow in line_flows
        if float(flow.loading_percent)
        >= threshold
    )


# =========================================================
# METRIC BUILDERS
# =========================================================

def build_baseline_metrics(
    line_flows,
    overload_threshold: float = 100.0,
) -> BaselineMetrics:
    """
    Build baseline grid metrics from
    the original network state.
    """

    return BaselineMetrics(
        max_loading_percent=
        compute_max_loading_percent(
            line_flows
        ),

        average_loading_percent=
        compute_average_loading_percent(
            line_flows
        ),

        overloaded_line_count=
        count_overloaded_lines(
            line_flows,
            threshold=overload_threshold,
        ),

        overload_severity=
        compute_overload_severity(
            line_flows,
            threshold=overload_threshold,
        ),
    )


def build_candidate_metrics(
    line_flows,
    overload_threshold: float = 100.0,
) -> CandidateMetrics:
    """
    Build candidate grid metrics after
    applying a candidate line.
    """

    return CandidateMetrics(
        max_loading_percent=
        compute_max_loading_percent(
            line_flows
        ),

        average_loading_percent=
        compute_average_loading_percent(
            line_flows
        ),

        overloaded_line_count=
        count_overloaded_lines(
            line_flows,
            threshold=overload_threshold,
        ),

        overload_severity=
        compute_overload_severity(
            line_flows,
            threshold=overload_threshold,
        ),
    )


# =========================================================
# RELIEF METRICS
# =========================================================

def compute_congestion_relief_metrics(
    baseline: BaselineMetrics,
    candidate: CandidateMetrics,
) -> CongestionReliefMetrics:
    """
    Compute congestion improvements relative
    to the baseline grid state.

    Positive values indicate improvement.
    Negative values indicate degradation.
    """

    return CongestionReliefMetrics(

        max_loading_reduction=
        (
            baseline.max_loading_percent
            -
            candidate.max_loading_percent
        ),

        average_loading_reduction=
        (
            baseline.average_loading_percent
            -
            candidate.average_loading_percent
        ),

        overloaded_line_reduction=
        (
            baseline.overloaded_line_count
            -
            candidate.overloaded_line_count
        ),

        overload_severity_reduction=
        (
                baseline.overload_severity
                -
                candidate.overload_severity
        )
    )


# =========================================================
# RELIEF SCORING
# =========================================================

def compute_congestion_relief_score(
    relief: CongestionReliefMetrics,
) -> float:
    """
    Compute a simple congestion relief score.

    IMPORTANT:
    This score is only an optimization proxy.

    Physical metrics remain the primary source
    of truth for evaluation and explainability.
    """

    return (
        relief.overload_severity_reduction
    )