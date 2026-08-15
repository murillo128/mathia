from __future__ import annotations

from math import gcd
from typing import Iterable


def _check_modulus(n: int) -> None:
    if n < 2:
        raise ValueError("modulus must be >= 2")


def residues(n: int) -> range:
    _check_modulus(n)
    return range(n)


def mul_map(a: int, n: int) -> tuple[int, ...]:
    _check_modulus(n)
    return tuple((a * x) % n for x in residues(n))


def affine_map(a: int, b: int, n: int) -> tuple[int, ...]:
    _check_modulus(n)
    return tuple((a * x + b) % n for x in residues(n))


def is_permutation(values: Iterable[int], n: int) -> bool:
    _check_modulus(n)
    vals = tuple(values)
    return len(vals) == n and set(vals) == set(residues(n))


def multiplication_is_permutation(a: int, n: int) -> bool:
    return is_permutation(mul_map(a, n), n)


def affine_is_permutation(a: int, b: int, n: int) -> bool:
    return is_permutation(affine_map(a, b, n), n)


def cancellation_is_valid(a: int, n: int) -> bool:
    """Whether ax ≡ ay (mod n) implies x ≡ y (mod n) for all residues."""
    _check_modulus(n)
    images = mul_map(a, n)
    return len(set(images)) == n


def cancellation_counterexample(a: int, n: int) -> tuple[int, int] | None:
    """Return x != y with ax ≡ ay (mod n), or None if cancellation is valid."""
    _check_modulus(n)
    seen: dict[int, int] = {}
    for x, image in enumerate(mul_map(a, n)):
        if image in seen:
            return seen[image], x
        seen[image] = x
    return None


def linear_congruence_solutions(a: int, b: int, n: int) -> tuple[int, ...]:
    _check_modulus(n)
    return tuple(x for x in residues(n) if (a * x - b) % n == 0)


def functional_graph_all_vertices_on_cycles(a: int, n: int) -> bool:
    """For x -> ax mod n, test whether every vertex is on a directed cycle."""
    _check_modulus(n)
    f = mul_map(a, n)
    for start in residues(n):
        path: list[int] = []
        index: dict[int, int] = {}
        x = start
        while x not in index:
            index[x] = len(path)
            path.append(x)
            x = f[x]
        cycle_start = index[x]
        if start not in path[cycle_start:]:
            return False
    return True


def gcd_reduction(a: int, b: int, q: int) -> tuple[int, int]:
    return b, a - q * b


def gcd_reduction_preserves(a: int, b: int, q: int) -> bool:
    before = gcd(a, b)
    c, d = gcd_reduction(a, b, q)
    return before == gcd(c, d)


def crt_map(m: int, n: int) -> tuple[tuple[int, int], ...]:
    _check_modulus(m)
    _check_modulus(n)
    modulus = m * n
    return tuple((x % m, x % n) for x in range(modulus))


def crt_map_is_bijection(m: int, n: int) -> bool:
    values = crt_map(m, n)
    codomain = {(i, j) for i in range(m) for j in range(n)}
    return len(set(values)) == m * n and set(values) == codomain


def crt_collision(m: int, n: int) -> tuple[int, int] | None:
    """Return x != y mod mn with the same pair of residues, if one exists."""
    values = crt_map(m, n)
    seen: dict[tuple[int, int], int] = {}
    for x, pair in enumerate(values):
        if pair in seen:
            return seen[pair], x
        seen[pair] = x
    return None
