# AGENTS.md Design

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a compact but precise `AGENTS.md` that only captures repo-specific facts an agent would likely miss, with enough detail to prevent common missteps.

**Architecture:** Keep two sections: commands (uv-based workflows) and an architecture snapshot pointing to semantic, Pyomo execution, and results layers, plus the key public entrypoints within the Pyomo pipeline.

**Tech Stack:** Python 3.12, uv, Pyomo.

---

## Design Summary

The file should remain minimal and high-signal, but include enough precision to prevent confusion about where to make changes or how to run checks. Include only:
- Exact uv-based commands for install and verification (avoid pip/poetry guesses).
- A short architecture snapshot describing the semantic layer (`problems/eon_grid_expansion/*`), the Pyomo executable pipeline (`src/optimization/pyomo/*`), the normalized results layer (`src/optimization/results/*`), and the primary Pyomo build/solve entrypoints.

Exclude generic guidance, full file trees, and anything not verified in the repo.

## Proposed AGENTS.md Content

```
# AGENTS.md

## Commands (uv)
- Install: `uv sync`
- Tests: `uv run pytest`
- Lint: `uv run ruff`
- Typecheck: `uv run mypy`

## Architecture snapshot
- E.ON grid expansion semantic layer (problem, constraints, objectives, formulation): `problems/eon_grid_expansion/*`
- Pyomo executable pipeline (model/build/constraints/objectives/solve): `src/optimization/pyomo/*`
- Primary Pyomo build entrypoint: `src/optimization/pyomo/builders.py` (`build_pyomo_model`)
- Primary solve entrypoint: `src/optimization/pyomo/solve.py` (`solve_optimization_problem`)
- Normalized results artifacts: `src/optimization/results/*`
```

## Open Questions

None.
