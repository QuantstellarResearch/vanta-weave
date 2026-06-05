from __future__ import annotations

import hashlib
import json
from typing import Any, Tuple


def _canonical_pair(
    a: Any,
    b: Any,
) -> Tuple[str, str]:
    """
    Return canonical ordered pair as strings.
    """

    try:
        ai = int(a)
        bi = int(b)

        if ai <= bi:
            return str(ai), str(bi)

        return str(bi), str(ai)

    except Exception:

        sa = str(a)
        sb = str(b)

        if sa <= sb:
            return sa, sb

        return sb, sa


def _short_hash(
    key: object,
    length: int = 6,
) -> str:
    """
    Return deterministic short hash.
    """

    payload = json.dumps(
        key,
        sort_keys=True,
        separators=(",", ":"),
    )

    return hashlib.sha1(
        payload.encode("utf-8")
    ).hexdigest()[:length]


# =========================================================
# CANDIDATE IDS
# =========================================================

def make_candidate_id(
    kind: str,
    from_bus: Any,
    to_bus: Any,
    reference_line_id: int,
    build_cost: float,
    length_km: float | None = None,
    variant_index: int | None = None,
    add_hash: bool = True,
) -> str:
    """
    Build deterministic candidate id.

    Example:

        cand_parallel_7_8_ref73_c331_h895858

    Structure:

        cand
        kind
        bus pair
        reference asset
        cost
        hash
    """

    a, b = _canonical_pair(
        from_bus,
        to_bus,
    )

    cost = int(
        round(
            float(build_cost or 0.0) * 100.0
        )
    )

    base = (
        f"cand_{kind}"
        f"_{a}_{b}"
        f"_ref{reference_line_id}"
        f"_c{cost}"
    )

    if variant_index is not None:

        base = (
            f"{base}"
            f"_v{int(variant_index)}"
        )

    if add_hash:

        key = {
            "kind": kind,
            "pair": (a, b),
            "reference_line_id":
                int(reference_line_id),
            "cost": cost,
            "length":
                None
                if length_km is None
                else int(round(length_km)),
        }

        base = (
            f"{base}"
            f"_h{_short_hash(key)}"
        )

    return base


# =========================================================
# DEDUPLICATION
# =========================================================

def canonical_base_key(
    kind: str,
    from_bus: Any,
    to_bus: Any,
    reference_line_id: int,
    build_cost: float,
) -> Tuple:
    """
    Canonical deduplication key.

    Candidates are considered equivalent if:

    - same generation strategy
    - same endpoints
    - same reference asset
    - same build cost
    """

    a, b = _canonical_pair(
        from_bus,
        to_bus,
    )

    cost = int(
        round(
            float(build_cost or 0.0) * 100.0
        )
    )

    return (
        kind,
        a,
        b,
        int(reference_line_id),
        cost,
    )


# =========================================================
# VARIANT SORTING
# =========================================================

def sort_key_for_variant(
    item: dict,
) -> Tuple:
    """
    Deterministic variant ordering.

    Prefer:

        lower cost
        shorter length
        smaller reference id

    This function is used only when
    multiple equivalent candidates exist.
    """

    cost = int(
        round(
            float(
                item.get("build_cost")
                or 0.0
            ) * 100.0
        )
    )

    length = int(
        round(
            float(
                item.get("length_km")
                or 0.0
            )
        )
    )

    reference_line_id = int(
        item.get("reference_line_id")
        or 0
    )

    return (
        cost,
        length,
        reference_line_id,
    )