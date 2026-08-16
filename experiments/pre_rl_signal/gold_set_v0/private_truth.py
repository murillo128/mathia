from __future__ import annotations

import math


def _mul(a: int, n: int) -> list[int]:
    return [(a * x) % n for x in range(n)]


def _aff(a: int, b: int, n: int) -> list[int]:
    return [(a * x + b) % n for x in range(n)]


def _collision(values: list[object]) -> list[int] | None:
    seen: dict[object, int] = {}
    for x, value in enumerate(values):
        if value in seen:
            return [seen[value], x]
        seen[value] = x
    return None


def _sols(a: int, b: int, n: int) -> list[int]:
    return [x for x in range(n) if (a * x - b) % n == 0]


def _orbit_distinct(a: int, n: int, start: int) -> int:
    seen: set[int] = set()
    x = start
    while x not in seen:
        seen.add(x)
        x = (a * x) % n
    return len(seen)


def _crt_solutions(rm: int, rn: int, m: int, n: int) -> list[int]:
    return [x for x in range(m * n) if x % m == rm and x % n == rn]


def _fixed_points(values: list[int]) -> int:
    return sum(value == x for x, value in enumerate(values))


def _entry(value: object, **params: int) -> dict[str, object]:
    return {"value": value, "params": params}


def build_private() -> dict[str, object]:
    answers: dict[str, dict[str, dict[str, object]]] = {}

    rev_specs = [(1,15,4),(2,15,5),(3,16,3),(4,16,6),(5,21,8),(6,21,7),(7,35,12),(8,35,10)]
    subsets = {
        1:[8,11,14,5], 2:[3,6,9,12], 3:[5,8,11,14], 4:[3,4,11,12],
        5:[7,10,13,16], 6:[3,4,5,6], 7:[3,6,9,12], 8:[3,4,5,6],
    }
    starts = {1:7, 2:11, 3:15, 4:3, 5:7, 6:6, 7:31, 8:5}
    recovery_inputs = {1:11, 3:7, 5:14, 7:12}
    for i, n, a in rev_specs:
        target = (i * 7 + 4) % n
        values = _mul(a, n)
        unit = math.gcd(a, n) == 1
        t4 = (
            _entry(recovery_inputs[i])
            if unit
            else _entry(_collision(values), a=a, n=n)
        )
        answers[f"R{i:02d}"] = {
            "T1": _entry(len(_sols(a, target, n))),
            "T2": _entry(len({(a * x) % n for x in subsets[i]})),
            "T3": _entry(_orbit_distinct(a, n, starts[i])),
            "T4": t4,
        }

    gcd_specs = [(9,84,30,2),(10,91,26,-2),(11,144,54,3),(12,221,52,5)]
    deltas = {9:1, 10:2, 11:3, 12:5}
    reconstruction_specs = {9:(71,22,-3), 10:(109,31,4), 11:(137,40,-2), 12:(203,47,5)}
    two_step_specs = {9:(96,37,2,-1), 10:(104,34,3,2), 11:(150,57,2,-2), 12:(225,55,4,3)}
    for i, a, b, q in gcd_specs:
        q2 = q + 2
        c2, d2 = b, a - q2 * b
        delta = deltas[i]
        bad_c, bad_d = b, a - q * b + delta
        hidden_u, hidden_v, hidden_q = reconstruction_specs[i]
        transformed_v, transformed_delta = hidden_v, hidden_u - hidden_q * hidden_v
        probe_u, probe_v, probe_q1, probe_q2 = two_step_specs[i]
        first_u, first_v = probe_v, probe_u - probe_q1 * probe_v
        final_u, final_v = first_v, first_u - probe_q2 * first_v
        answers[f"G{i:02d}"] = {
            "T1": _entry(math.gcd(c2, d2)),
            "T2": _entry(math.gcd(bad_c, bad_d)),
            "T3": _entry(transformed_delta + hidden_q * transformed_v),
            "T4": _entry(math.gcd(final_u, final_v)),
        }

    reconstruction_targets = {13:7, 14:23, 15:17, 16:10}
    polynomial_specs = {13:(2,1), 14:(3,2), 15:(4,3), 16:(5,1)}
    relation_specs = {13:(3,1,1), 14:(4,2,3), 15:(5,2,4), 16:(4,1,2)}
    replacement_moduli = {13:6, 14:6, 15:10}
    for i, m, n in [(13,3,5),(14,4,9),(15,5,8),(16,4,6)]:
        modulus = m * n
        coprime = math.gcd(m, n) == 1
        x0 = reconstruction_targets[i]
        rm, rn = x0 % m, x0 % n
        linear_c, constant_d = polynomial_specs[i]
        relation_modulus, relation_weight, relation_target = relation_specs[i]
        values = [(x % m, x % n) for x in range(modulus)]
        compatible = _crt_solutions(rm, rn, m, n)
        polynomial_pair = [
            (rm * rm + linear_c * rm + constant_d) % m,
            (rn * rn + linear_c * rn + constant_d) % n,
        ]
        relation_count = sum(
            ((x % m) + relation_weight * (x % n)) % relation_modulus == relation_target
            for x in range(modulus)
        )
        if coprime:
            replacement_n = replacement_moduli[i]
            replacement_values = {(x % m, x % replacement_n) for x in range(m * replacement_n)}
            answers[f"C{i:02d}"] = {
                "T1": _entry(compatible[0]),
                "T2": _entry(polynomial_pair),
                "T3": _entry(relation_count),
                "T4": _entry(len(replacement_values)),
            }
        else:
            answers[f"C{i:02d}"] = {
                "T1": _entry(len(compatible)),
                "T2": _entry(polynomial_pair),
                "T3": _entry(_collision(values), m=m, n=n),
                "T4": _entry(relation_count),
            }

    for i, n, a, b, c, d in [(17,12,5,2,7,0),(18,15,6,5,4,1),(19,20,3,0,7,0),(20,18,5,1,6,4)]:
        f_values = _aff(a, b, n)
        g_values = _aff(c, d, n)
        composed = [g_values[f_values[x]] for x in range(n)]
        answers[f"M{i:02d}"] = {
            "T1": _entry(len(set(f_values))),
            "T2": _entry(_fixed_points(f_values)),
            "T3": _entry(len(set(composed))),
            "T4": _entry(_fixed_points(composed)),
        }

    return {"version": "gold-set-v0", "answers": answers}
