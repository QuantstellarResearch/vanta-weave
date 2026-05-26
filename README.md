# Vanta Quantum

## Project Overview
Vanta Quantum is a transmission line expansion planning system focused on congestion relief and cost-aware investment decisions.
It models grid expansion as a combinatorial optimization problem: selecting candidate lines to build in order to reduce overload risk while controlling capital expenditure.
The architecture separates semantic problem definition, mathematical formulation, and executable Pyomo optimization, with a results layer for analytics and explainability.

## Why It Matters
- Grid congestion directly impacts reliability and operational risk.
- Expansion planning is a high-stakes CapEx decision that benefits from transparent, data-driven optimization.
- Critical infrastructure decisions require explainable, auditable recommendations.
- Vanta Quantum targets practical, decision-grade outputs rather than black-box predictions.

## Architecture Overview
Semantic -> Formulation -> Pyomo Execution -> Results/Topology

- **Semantic layer**: domain objects for grid expansion (problem, constraints, objectives, scenarios).
- **Formulation**: mathematical structure (binary decision variables, constraint/objective toggles).
- **Pyomo pipeline**: build model, attach variables/constraints/objectives, solve via HiGHS/Gurobi.
- **Results/Topology**: normalized solution artifacts, analytics, and explainability signals.

## Core Modules
- `problems/eon_grid_expansion/*`
  Semantic definitions: problem, constraints, objectives, decision space, scenarios.

- `src/optimization/pyomo/*`
  Executable pipeline: model build, variable/constraint/objective attachment, solve.

- `src/optimization/results/*`
  Normalized solution artifacts and analytics.

- `src/optimization/topology/*`
  Topology metrics and explainability heuristics.

## Status / MVP Scope
- Pyomo build + solve pipeline is operational.
- Results and topology layers provide explainability and planning-grade analytics.
- Semantic constraints (thermal/voltage/topology) are defined and progressively being encoded in Pyomo.
- The MVP goal is an end-to-end workflow that produces candidate line recommendations with explainable rationale.

## Roadmap (Short)
- Candidate line generation (heuristic + data-driven).
- Scenario-aware optimization (multi-scenario planning).
- Encode thermal/voltage/topology constraints into Pyomo.
- Strengthen reporting and explainability outputs.

## Dependencies
- Pyomo, HiGHS/Gurobi
- vanta_lattice (domain data models)
