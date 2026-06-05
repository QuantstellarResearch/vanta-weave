from __future__ import annotations

from src.evaluation.models import (
    EvaluationDataset,
)

from src.evaluation.evaluator import (
    build_baseline_metrics_from_data,
    evaluate_candidates,
    rank_candidates,
)


# =========================================================
# WORKFLOW
# =========================================================

def evaluate_candidates_workflow(
    *,
    data,
    candidates,
) -> EvaluationDataset:
    """
    Evaluate all candidate transmission lines.

    Workflow:

        baseline line flows
                ↓
        baseline metrics
                ↓
        candidate simulations
                ↓
        candidate evaluations
                ↓
        ranking
                ↓
        EvaluationDataset
    """

    baseline_metrics = (
        build_baseline_metrics_from_data(
            line_flows=
            data.mapped["line_flows"],
        )
    )

    evaluations = (
        evaluate_candidates(
            baseline_metrics=
            baseline_metrics,

            net=
            data.raw_net,

            candidates=
            candidates,

            reference_lines=
            data.mapped["lines"],
        )
    )

    ranked_evaluations = (
        rank_candidates(
            evaluations
        )
    )

    return EvaluationDataset(
        baseline_metrics=
        baseline_metrics,

        evaluations=
        ranked_evaluations,
    )

if __name__ == "__main__":

    from datasets.load_ieee118 import (
        load_data,
    )

    from workflows.generate_candidates import (
        CandidateGenerationConfig,
        generate_candidates,
    )

    print(
        "\nLoading IEEE118 dataset..."
    )

    data = load_data()

    print(
        f"Loaded "
        f"{len(data.mapped['buses'])} buses | "
        f"{len(data.mapped['lines'])} lines"
    )

    print(
        "\nGenerating candidate lines..."
    )

    candidates = generate_candidates(
        data=data,
        config=CandidateGenerationConfig(),
    )

    print(
        f"Generated "
        f"{len(candidates)} candidates"
    )

    print(
        "\nRunning evaluation workflow..."
    )

    dataset = (
        evaluate_candidates_workflow(
            data=data,
            candidates=candidates,
        )
    )

    print(
        "\nBaseline Metrics"
    )

    print(
        dataset.baseline_metrics
    )

    print(
        "\nTop 10 Candidates"
    )

    for evaluation in dataset.evaluations[:10]:

        print(
            f"{evaluation.candidate_id}"
            f" | severity reduction="
            f"{evaluation.relief.overload_severity_reduction:.4f}"
            f" | overloaded lines reduction="
            f"{evaluation.relief.overloaded_line_reduction}"
            f" | max loading reduction="
            f"{evaluation.relief.max_loading_reduction:.4f}"
        )