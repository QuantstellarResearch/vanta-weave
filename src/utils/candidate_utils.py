from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable, Tuple


def _canonical_pair(a: Any, b: Any) -> Tuple[str, str]:
    """Return canonical ordered pair as strings."""
    try:
        ai = int(a)
        bi = int(b)
        if ai <= bi:
            return str(ai), str(bi)
        return str(bi), str(ai)
    except Exception:
        # fallback to string ordering
        sa, sb = str(a), str(b)
        if sa <= sb:
            return sa, sb
        return sb, sa


def _short_hash(key: object, length: int = 6) -> str:
    """Return short hex hash for a JSON-serializable key."""
    payload = json.dumps(key, sort_keys=True, separators=(",", ":"))
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:length]


def make_candidate_id(
    kind: str,
    from_bus: Any,
    to_bus: Any,
    capacity_mva: float,
    build_cost: float,
    length_km: float | None = None,
    variant_index: int | None = None,
    add_hash: bool = True,
) -> str:
    """
    Build a deterministic, readable candidate id with optional short hash suffix.

    Format: cand_{kind}_{minBus}_{maxBus}_cap{capacity}_c{cost}[_v{index}][_h{hash}]
    - capacity: rounded to nearest integer
    - cost: scaled by 100 and rounded to integer (two decimals preserved)
    - pair ordering is canonical (min,max)
    - variant_index appended if provided
    - short hash appended if add_hash=True to avoid rare collisions
    """

    a, b = _canonical_pair(from_bus, to_bus)

    cap = int(round(float(capacity_mva or 0.0)))
    cost = int(round(float(build_cost or 0.0) * 100.0))

    base = f"cand_{kind}_{a}_{b}_cap{cap}_c{cost}"

    if variant_index is not None:
        base = f"{base}_v{int(variant_index)}"

    if add_hash:
        key = {
            "kind": kind,
            "pair": (a, b),
            "cap": cap,
            "cost": cost,
            "length": None if length_km is None else int(round(length_km)),
        }
        h = _short_hash(key)
        base = f"{base}_h{h}"

    return base


def canonical_base_key(kind: str, from_bus: Any, to_bus: Any, capacity_mva: float, build_cost: float) -> Tuple:
    """
    Return a hashable canonical base key for deduplication grouping.
    """
    a, b = _canonical_pair(from_bus, to_bus)
    cap = int(round(float(capacity_mva or 0.0)))
    cost = int(round(float(build_cost or 0.0) * 100.0))
    return (kind, a, b, cap, cost)


def sort_key_for_variant(item: dict) -> Tuple:
    """
    Deterministic sort key for variants of same base key.

    Prefer higher capacity, lower cost, shorter length, higher voltage.
    """
    cap = int(round(float(item.get("capacity_mva") or 0.0)))
    cost = int(round(float(item.get("build_cost") or 0.0) * 100.0))
    length = int(round(float(item.get("length_km") or 0.0)))
    # voltage may be None
    voltage = float(item.get("voltage_kv") or 0.0)
    # sort: capacity desc, cost asc, length asc, voltage desc
    return (-cap, cost, length, -voltage)
