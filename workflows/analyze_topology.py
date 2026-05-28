"""Orchestrator to run topology analyses and emit reports.

Design: keep minimal and reuse src/optimization/topology functions where available.
"""
from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import Optional

from workflows._helpers.topology_io import read_candidate_list, read_selected_lines, build_minimal_solution

LOG = logging.getLogger(__name__)


def run_topology_report(candidate_list_path: str = 'outputs/candidate_list.json',
                        selected_path: str = 'outputs/selected_lines.json',
                        mapped_data_path: Optional[str] = None,
                        out_dir: str = 'outputs',
                        validate_top_n: int = 0,
                        overwrite: bool = False) -> dict:
    out_dir_p = Path(out_dir)
    out_dir_p.mkdir(parents=True, exist_ok=True)

    candidates = read_candidate_list(candidate_list_path)
    selected = read_selected_lines(selected_path)
    solution = build_minimal_solution(candidates, selected)

    # Placeholder analysis: assemble a simple report
    report = {
        "summary": {
            "num_candidates": len(candidates),
            "num_selected": len(selected),
        },
        "selected": selected,
    }

    # Write JSON and Markdown
    with open(out_dir_p / 'topology_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    md = f"# Topology Report\n\nSelected {len(selected)} of {len(candidates)} candidates."
    with open(out_dir_p / 'topology_report.md', 'w', encoding='utf-8') as f:
        f.write(md)

    LOG.info("Wrote topology report to %s", out_dir_p)
    return report


if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument('--candidate-list', default='outputs/candidate_list.json')
    p.add_argument('--selected', default='outputs/selected_lines.json')
    p.add_argument('--out', default='outputs')
    args = p.parse_args()
    run_topology_report(candidate_list_path=args.candidate_list, selected_path=args.selected, out_dir=args.out)
