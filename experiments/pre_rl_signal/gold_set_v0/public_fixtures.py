from __future__ import annotations

"""Corrected public fixtures for gold-set-v0.

The independent audit in ``INDEPENDENT_AUDIT.md`` found semantic leakage,
control contamination, and redundant task templates in the original fixture.
The fixture remains version ``gold-set-v0`` because no model run occurred before
these pre-freeze corrections.
"""

from contexts import SHUFFLED_POOL
from fixtures_composition import build as build_composition
from fixtures_crt import build as build_crt
from fixtures_gcd import build as build_gcd
from fixtures_reversibility import build as build_reversibility


def build_public() -> dict[str, object]:
    situations = [
        *build_reversibility(),
        *build_gcd(),
        *build_crt(),
        *build_composition(),
    ]
    assert len(situations) == 20
    return {
        "version": "gold-set-v0",
        "shuffled_pool": SHUFFLED_POOL,
        "situations": situations,
    }
