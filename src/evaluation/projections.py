from __future__ import annotations

from src.evaluation.models import (
    EvaluationDataset,
)

def build_candidate_severity_reduction_map(
    evaluation_dataset: EvaluationDataset,
) -> dict[str, float]:

    return {
        evaluation.candidate_id:
        (
            evaluation
            .relief
            .overload_severity_reduction
        )

        for evaluation in (
            evaluation_dataset.evaluations
        )
    }