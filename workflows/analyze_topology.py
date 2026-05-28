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

    # Try to import analyzers from src/optimization/topology
    metrics_result = {}
    viz_written = False
    try:
        # Local import because this module may be heavy
        from src.optimization.topology import graph as topology_graph
        from src.optimization.topology import congestion as topology_congestion
        from src.optimization.topology import resilience as topology_resilience
        from src.optimization.topology import metrics as topology_metrics

        # Attempt to build operational graph if mapped data available
        try:
            infrastructure = None
            if mapped_data_path:
                with open(mapped_data_path, 'r', encoding='utf-8') as f:
                    infrastructure = json.load(f)
            op_graph = topology_graph.build_operational_graph(infrastructure, candidates)
            projection = topology_graph.project_solution_overlay(op_graph, solution)

            cong = topology_congestion.analyze_topology_congestion(projection, solution)
            res = topology_resilience.analyze_network_resilience(projection, solution)
            cent = topology_metrics.compute_topology_centrality(projection)

            metrics_result = {
                "congestion": cong if isinstance(cong, dict) else getattr(cong, '_asdict', lambda: cong)(),
                "resilience": res if isinstance(res, dict) else getattr(res, '_asdict', lambda: res)(),
                "centrality": cent,
            }

            # try drawing using projection -> networkx
            try:
                G = projection.to_networkx()
                import networkx as nx
                import matplotlib.pyplot as plt

                pos = {n: (d.get('x', i), d.get('y', i)) for i, (n, d) in enumerate(G.nodes(data=True))}
                plt.figure(figsize=(12, 8))
                nx.draw(G, pos=pos, node_size=20, edge_color='grey')
                # highlight selected candidate edges if available
                sel_edges = []
                for u, v, data in G.edges(data=True):
                    if data.get('candidate_id') in selected:
                        sel_edges.append((u, v))
                if sel_edges:
                    nx.draw_networkx_edges(G, pos=pos, edgelist=sel_edges, edge_color='red', width=2)
                plt.savefig(Path(out_dir) / 'topology_viz.png')
                plt.close()
                viz_written = True
            except Exception:
                LOG.exception("Visualization using projection failed")

        except Exception:
            LOG.exception("Topology graph build/analysis failed; falling back to minimal viz")
            # fallthrough to minimal viz below

    except Exception:
        LOG.info("Topology analyzers not available; using minimal visualization fallback")

    # If analyzers unavailable or failed, produce a minimal NetworkX visualization from candidate specs
    if not viz_written:
        try:
            import networkx as nx
            import matplotlib.pyplot as plt

            G = nx.Graph()
            for c in candidates:
                spec = c.get('spec', {})
                u = spec.get('from') or spec.get('f') or f"{c['candidate_id']}_u"
                v = spec.get('to') or spec.get('t') or f"{c['candidate_id']}_v"
                G.add_node(u)
                G.add_node(v)
                G.add_edge(u, v, candidate_id=c['candidate_id'])

            pos = None
            try:
                pos = nx.spring_layout(G, seed=0)
            except Exception:
                pos = {n: (i * 0.1, i * 0.1) for i, n in enumerate(G.nodes())}

            plt.figure(figsize=(12, 8))
            nx.draw(G, pos=pos, node_size=50, edge_color='grey')
            sel_edges = [e for e in G.edges() if G.edges[e].get('candidate_id') in selected]
            if sel_edges:
                nx.draw_networkx_edges(G, pos=pos, edgelist=sel_edges, edge_color='red', width=2)
            plt.savefig(out_dir_p / 'topology_viz.png')
            plt.close()
            viz_written = True
            metrics_result = metrics_result or {}
        except Exception:
            LOG.exception("Minimal visualization fallback failed")

    report['metrics'] = metrics_result

    # Write JSON and Markdown
    with open(out_dir_p / 'topology_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    md = f"# Topology Report\n\nSelected {len(selected)} of {len(candidates)} candidates."
    with open(out_dir_p / 'topology_report.md', 'w', encoding='utf-8') as f:
        f.write(md)

    LOG.info("Wrote topology report to %s", out_dir_p)
    # Write provenance (timezone-aware timestamp)
    try:
        import hashlib
        import subprocess
        import sys
        from datetime import datetime, timezone

        def file_sha256(path: Path) -> str:
            h = hashlib.sha256()
            with open(path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    h.update(chunk)
            return h.hexdigest()

        inputs = {}
        for p in [("candidate_list", candidate_list_path), ("selected", selected_path)]:
            try:
                pp = Path(p[1])
                inputs[p[0]] = {"path": str(pp), "sha256": file_sha256(pp) if pp.exists() else None}
            except Exception:
                inputs[p[0]] = {"path": str(p[1]), "sha256": None}

        git_rev = None
        try:
            git_rev = subprocess.check_output(["git", "rev-parse", "--verify", "HEAD"]).decode().strip()
        except Exception:
            git_rev = None

        prov = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "git_commit": git_rev,
            "python_version": sys.version,
            "inputs": inputs,
            "config": {
                "candidate_list_path": candidate_list_path,
                "selected_path": selected_path,
                "mapped_data_path": mapped_data_path,
                "validate_top_n": validate_top_n,
            },
        }

        with open(out_dir_p / 'topology_report.prov.json', 'w', encoding='utf-8') as f:
            json.dump(prov, f, indent=2)
    except Exception:
        LOG.exception("Failed to write provenance file")

    return report


if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument('--candidate-list', default='outputs/candidate_list.json')
    p.add_argument('--selected', default='outputs/selected_lines.json')
    p.add_argument('--out', default='outputs')
    p.add_argument('--validate-top-n', default=0, type=int,
                   help='If >0, run pandapower AC validation for top-N candidates (disabled by default)')
    args = p.parse_args()
    run_topology_report(candidate_list_path=args.candidate_list, selected_path=args.selected, out_dir=args.out,
                        validate_top_n=args.validate_top_n)
