from __future__ import annotations

from workflows.run_optimization import OptimizationRunConfig


def test_optimization_run_config_defaults_to_highs():
    config = OptimizationRunConfig()

    assert config.solver_name == "highs"
