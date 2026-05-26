# AGENTS.md

## Commands (uv)
- Install: `uv sync`
- Tests: `uv run pytest`
- Lint: `uv run ruff check .`
- Typecheck: `uv run mypy`
- If using an external env: prefix commands with `uv run --active ...` to avoid creating `.venv` in repo

## Architecture snapshot
- E.ON grid expansion semantic layer (problem, constraints, objectives, formulation): `problems/eon_grid_expansion/*`
- Pyomo executable pipeline (model/build/constraints/objectives/solve): `src/optimization/pyomo/*`
- Primary Pyomo build entrypoint: `src/optimization/pyomo/builders.py` (`build_pyomo_model`)
- Primary solve entrypoint: `src/optimization/pyomo/solve.py` (`solve_optimization_problem`)
- Normalized results artifacts: `src/optimization/results/*`
