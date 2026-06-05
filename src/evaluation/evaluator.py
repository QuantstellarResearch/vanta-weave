from __future__ import annotations

from time import perf_counter

from problems.eon_grid_expansion.decision_space import (
    CandidateLine,
)

from src.evaluation.models import (
    BaselineMetrics,
    CandidateEvaluation,
)

from src.evaluation.metrics import (
    build_baseline_metrics,
    build_candidate_metrics,
    compute_congestion_relief_metrics,
    compute_congestion_relief_score,
)

from src.evaluation.simulation import (
    simulate_candidate,
)

from vanta_lattice.domains.energy.models import (
    LineEdge,
)


# =========================================================
# BASELINE
# =========================================================

def build_baseline_metrics_from_data(
    line_flows,
) -> BaselineMetrics:
    """
    Build baseline metrics from the
    original simulated grid state.
    """

    return build_baseline_metrics(
        line_flows=line_flows,
    )


# =========================================================
# SINGLE CANDIDATE
# =========================================================

def evaluate_candidate(
    *,
    baseline_metrics: BaselineMetrics,
    net,
    candidate: CandidateLine,
    reference_lines: list[LineEdge],
) -> CandidateEvaluation:
    """
    Evaluate a single candidate.

    Workflow

        Candidate
            ↓

        simulate_candidate()

            ↓

        CandidateMetrics

            ↓

        ReliefMetrics

            ↓

        CandidateEvaluation
    """

    start_time = perf_counter()

    candidate_line_flows = (
        simulate_candidate(
            net=net,
            candidate=candidate,
            reference_lines=reference_lines,
        )
    )

    candidate_metrics = (
        build_candidate_metrics(
            line_flows=candidate_line_flows,
        )
    )

    relief_metrics = (
        compute_congestion_relief_metrics(
            baseline=baseline_metrics,
            candidate=candidate_metrics,
        )
    )

    objective_value = (
        compute_congestion_relief_score(
            relief=relief_metrics,
        )
    )

    runtime_seconds = (
        perf_counter()
        - start_time
    )

    return CandidateEvaluation(
        candidate_id=
        candidate.candidate_id,

        baseline=
        baseline_metrics,

        candidate=
        candidate_metrics,

        relief=
        relief_metrics,

        objective_value=
        objective_value,

        evaluation_runtime_seconds=
        runtime_seconds,
    )


# =========================================================
# BATCH EVALUATION
# =========================================================

def evaluate_candidates(
    *,
    baseline_metrics: BaselineMetrics,
    net,
    candidates: list[CandidateLine],
    reference_lines: list[LineEdge],
) -> list[CandidateEvaluation]:
    """
    Evaluate all candidate lines.
    """

    evaluations: list[
        CandidateEvaluation
    ] = []

    for candidate in candidates:

        evaluations.append(
            evaluate_candidate(
                baseline_metrics=
                baseline_metrics,

                net=net,

                candidate=
                candidate,

                reference_lines=
                reference_lines,
            )
        )

    return evaluations


# =========================================================
# RANKING
# =========================================================

def rank_candidates(
    evaluations: list[
        CandidateEvaluation
    ],
) -> list[
    CandidateEvaluation
]:
    """
    Rank candidates by physical
    congestion relief impact.
    """

    return sorted(
        evaluations,
        key=lambda evaluation:
        evaluation.relief
        .overload_severity_reduction,
        reverse=True,
    )