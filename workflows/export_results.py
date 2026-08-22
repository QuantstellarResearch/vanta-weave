from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


DEFAULT_INPUT = Path("outputs/selected_lines.json")
DEFAULT_OUTPUT = Path("outputs/report.md")


def generate_report(
    json_path: Path = DEFAULT_INPUT,
    output_path: Path = DEFAULT_OUTPUT,
) -> str:
    payload = _load_payload(json_path)
    report = _render_markdown(payload)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    output_path.write_text(
        report,
        encoding="utf-8",
    )
    return report


def _load_payload(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing workflow output: {path}"
        )
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def _render_markdown(payload: dict) -> str:
    objective = payload.get("objective_value")
    solver = payload.get("solver_name", "unknown")
    selected = payload.get("selected_candidates", [])
    selected_count = payload.get(
        "selected_count", len(selected)
    )
    assumptions = payload.get("assumptions", {})

    timestamp = datetime.now(UTC).isoformat()

    lines = [
        "# Vanta Weave Workflow Report",
        "",
        f"Generated: {timestamp} UTC",
        "",
        "## Summary",
        f"- Solver: {solver}",
        f"- Objective: {objective}",
        f"- Selected lines: {selected_count}",
        "",
    ]

    if not selected:
        lines.extend(
            [
                "## Selected Lines",
                "No lines selected under current budget.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Selected Lines",
                "| candidate_id | from_bus | to_bus | capacity_mva | build_cost | voltage_kv |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in selected:
            lines.append(
                "| {candidate_id} | {from_bus} | {to_bus} | {capacity_mva} | {build_cost} | {voltage_kv} |".format(
                    candidate_id=row.get("candidate_id", ""),
                    from_bus=row.get("from_bus", ""),
                    to_bus=row.get("to_bus", ""),
                    capacity_mva=row.get("capacity_mva", ""),
                    build_cost=row.get("build_cost", ""),
                    voltage_kv=row.get("voltage_kv", ""),
                )
            )
        lines.append("")

    lines.extend(
        [
            "## Assumptions",
            f"- candidates: {assumptions.get('candidates', 'unknown')}",
            f"- costs: {assumptions.get('costs', 'unknown')}",
            f"- budget: {assumptions.get('budget', 'unknown')}",
            "",
            "## Notes",
            "- Adjust budget ratio to explore alternative portfolios.",
            "- Validate recommendations with engineering review.",
            "",
        ]
    )

    return "\n".join(lines)


if __name__ == "__main__":
    generate_report()
