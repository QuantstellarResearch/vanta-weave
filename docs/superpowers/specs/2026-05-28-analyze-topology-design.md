# Analyze Topology Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a standalone post-workflow topology analysis CLI that replays a completed run from a specific run directory and generates reproducible topology, congestion, resilience, and explainability reports for selected expansion lines.

**Architecture:** `workflows/analyze_topology.py` is a thin orchestrator. It loads a completed run's artifacts from a caller-provided path, rebuilds the operational topology using the existing topology modules in `src/optimization/topology/*`, then renders deterministic JSON and markdown outputs under the same run directory or a caller-provided output directory. The workflow does not invoke Pyomo or solver code, and it never infers missing run context silently.

**Tech Stack:** Python 3.12, `pathlib`, `json`, `networkx`, `pytest`, existing `src/optimization/topology/*` and `src/optimization/results/*` modules.

---

### Task 1: Define the run-directory contract

**Files:**
- Modify: `workflows/analyze_topology.py`
- Modify: `workflows/run_eon_workflow.py`
- Test: `tests/workflows/test_analyze_topology.py`

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path

def test_analyze_topology_requires_run_dir(tmp_path):
    with pytest.raises(FileNotFoundError):
        analyze_topology(run_dir=tmp_path / "missing")
```

```python
def test_analyze_topology_loads_selected_and_candidate_lists(tmp_path, monkeypatch):
    run_dir = tmp_path / "run-001"
    run_dir.mkdir()
    (run_dir / "selected_lines.json").write_text("{}", encoding="utf-8")
    (run_dir / "candidate_list.json").write_text("{}", encoding="utf-8")

    # The function should at least open both required artifacts before analysis.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --active pytest tests/workflows/test_analyze_topology.py -v`

Expected: FAIL because `analyze_topology.py` is currently empty and the contract does not exist yet.

- [ ] **Step 3: Write minimal implementation**

```python
from pathlib import Path

def analyze_topology(*, run_dir: Path, output_dir: Path | None = None):
    selected_path = run_dir / "selected_lines.json"
    candidate_path = run_dir / "candidate_list.json"
    if not selected_path.exists():
        raise FileNotFoundError(selected_path)
    if not candidate_path.exists():
        raise FileNotFoundError(candidate_path)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run --active pytest tests/workflows/test_analyze_topology.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add workflows/analyze_topology.py workflows/run_eon_workflow.py tests/workflows/test_analyze_topology.py
git commit -m "feat(workflows): add topology analysis entrypoint contract"
```

### Task 2: Rebuild topology analysis from stored artifacts

**Files:**
- Modify: `workflows/analyze_topology.py`
- Test: `tests/workflows/test_analyze_topology.py`

- [ ] **Step 1: Write the failing test**

```python
def test_analyze_topology_builds_graph_from_run_artifacts(tmp_path, monkeypatch):
    # Arrange a minimal run_dir with candidate_list.json and selected_lines.json.
    # Patch the topology builders so the test asserts they are called with the
    # reconstructed infrastructure and candidate overlays.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --active pytest tests/workflows/test_analyze_topology.py -v`

Expected: FAIL until the function constructs `InfrastructureState`, `OperationalTopologyGraph`, and `GraphProjectionArtifacts` using the existing topology builders.

- [ ] **Step 3: Write minimal implementation**

```python
from src.optimization.topology.graph import (
    build_operational_graph,
    project_to_networkx,
    project_solution_overlay,
)
from src.optimization.topology.metrics import (
    compute_topology_centrality,
    compute_network_efficiency,
    compute_infrastructure_robustness,
    compute_expansion_effectiveness,
)
from src.optimization.topology.resilience import (
    identify_critical_infrastructure_edges,
    analyze_topology_vulnerabilities,
)
from src.optimization.topology.congestion import (
    build_congestion_edge_states,
    identify_congestion_hotspots,
)
from src.optimization.topology.explainability import (
    build_operational_reasoning_report,
)
```

```python
def analyze_topology(*, run_dir: Path, output_dir: Path | None = None):
    # load selected_lines.json and candidate_list.json
    # reconstruct candidate lines
    # build topology graph from current infrastructure + candidate overlays
    # project to networkx
    # compute topology metrics, congestion, resilience, explainability
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run --active pytest tests/workflows/test_analyze_topology.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add workflows/analyze_topology.py tests/workflows/test_analyze_topology.py
git commit -m "feat(workflows): analyze topology from workflow artifacts"
```

### Task 3: Emit deterministic analysis artifacts

**Files:**
- Modify: `workflows/analyze_topology.py`
- Test: `tests/workflows/test_analyze_topology_outputs.py`

- [ ] **Step 1: Write the failing test**

```python
def test_analyze_topology_writes_json_and_markdown(tmp_path, monkeypatch):
    # Given a complete run_dir, analyze_topology writes:
    # - topology_analysis.json
    # - topology_report.md
    # with stable content for the same inputs.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --active pytest tests/workflows/test_analyze_topology_outputs.py -v`

Expected: FAIL because artifact writing is not implemented yet.

- [ ] **Step 3: Write minimal implementation**

```python
def _write_topology_outputs(*, output_dir: Path, payload: dict) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "topology_analysis.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    (output_dir / "topology_report.md").write_text(_render_topology_markdown(payload), encoding="utf-8")
```

```python
def _render_topology_markdown(payload: dict) -> str:
    # deterministic markdown summary of metrics, hotspots, critical edges,
    # and selected candidate impacts
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run --active pytest tests/workflows/test_analyze_topology_outputs.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add workflows/analyze_topology.py tests/workflows/test_analyze_topology_outputs.py
git commit -m "feat(workflows): persist topology analysis artifacts"
```

### Task 4: Integrate topology analysis into the workflow entrypoint

**Files:**
- Modify: `workflows/run_eon_workflow.py`
- Modify: `workflows/analyze_topology.py`
- Test: `tests/workflows/test_run_eon_workflow.py`

- [ ] **Step 1: Write the failing test**

```python
def test_run_eon_workflow_can_optionally_trigger_topology_analysis(monkeypatch):
    # Use a flag or separate call path to ensure the workflow can invoke
    # analyze_topology after write_candidate_list and solve.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --active pytest tests/workflows/test_run_eon_workflow.py -v`

Expected: FAIL until the workflow has an explicit integration point.

- [ ] **Step 3: Write minimal implementation**

```python
def run_eon_workflow(*, solver_name: str = "highs", analyze: bool = False) -> dict:
    ...
    write_candidate_list(candidates)
    ...
    if analyze:
        analyze_topology(run_dir=OUTPUT_DIR)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run --active pytest tests/workflows/test_run_eon_workflow.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add workflows/run_eon_workflow.py workflows/analyze_topology.py tests/workflows/test_run_eon_workflow.py
git commit -m "feat(workflows): wire topology analysis into workflow"
```

### Task 5: Verify critical-infrastructure guardrails

**Files:**
- Modify: `workflows/analyze_topology.py`
- Test: `tests/workflows/test_analyze_topology_guardrails.py`

- [ ] **Step 1: Write the failing test**

```python
def test_analyze_topology_marks_results_as_heuristic_not_physical_simulation(tmp_path):
    # Output must explicitly state that the analysis is graph/topology-based,
    # not a full AC power-flow or N-1 validation.
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --active pytest tests/workflows/test_analyze_topology_guardrails.py -v`

Expected: FAIL until the output schema includes the disclaimer fields.

- [ ] **Step 3: Write minimal implementation**

```python
payload["analysis_scope"] = {
    "mode": "topology_heuristic",
    "physical_power_flow": False,
    "n_minus_one_validation": False,
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run --active pytest tests/workflows/test_analyze_topology_guardrails.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add workflows/analyze_topology.py tests/workflows/test_analyze_topology_guardrails.py
git commit -m "feat(workflows): add topology analysis guardrails"
```
