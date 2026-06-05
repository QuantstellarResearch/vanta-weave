from dataclasses import dataclass


@dataclass(frozen=True)
class CandidateAnalytics:

    overload_severity_reduction: dict[
        str,
        float,
    ]