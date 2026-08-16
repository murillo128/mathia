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


def _all_cycles(values: list[int]) -> bool:
    for start in range(len(values)):
        path: list[int] = []
        pos: dict[int, int] = {}
        x = start
        while x not in pos:
            pos[x] = len(path)
            path.append(x)
            x = values[x]
        if start not in path[pos[x]:]:
            return False
    return True


def _crt_solutions(rm: int, rn: int, m: int, n: int) -> list[int]:
    return [x for x in range(m * n) if x % m == rm and x % n == rn]


def _entry(value: object, **params: int) -> dict[str, object]:
    return {"value": value, "params": params}


def build_private() -> dict[str, object]:
    answers: dict[str, dict[str, dict[str, object]]] = {}

    for i, n, a in [(1,15,4),(2,15,5),(3,16,3),(4,16,6),(5,21,8),(6,21,7),(7,35,12),(8,35,10)]:
        b = (i * 3 + 1) % n
        target = (i * 5 + 2) % n
        alt_a = (a + i + 1) % n or 1
        values = _mul(a, n)
        unit = math.gcd(a, n) == 1
        t4 = (
            _entry(next(x for x in range(n) if (a * x) % n == 1))
            if unit
            else _entry(_collision(values), a=a, n=n)
        )
        answers[f"R{i:02d}"] = {
            "T1": _entry(len(_sols(a, target, n))),
            "T2": _entry(_all_cycles(values)),
            "T3": _entry(len(set(_aff(alt_a, b, n)))),
            "T4": t4,
        }

    gcd_specs = [(9,84,30,2),(10,91,26,-2),(11,144,54,3),(12,221,52,5)]
    deltas = {9:1, 10:2, 11:3, 12:5}
    for i, a, b, q in gcd_specs:
        q2 = q + 2
        c2, d2 = b, a - q2 * b
        delta = deltas[i]
        bad_c, bad_d = b, a - q * b + delta
        base = math.gcd(a, b)
        answers[f"G{i:02d}"] = {
            "T1": _entry(math.gcd(c2, d2)),
            "T2": _entry(math.gcd(bad_c, bad_d)),
            "T3": _entry(False),
            "T4": _entry(math.gcd(a, b - q2 * a) == base),
        }

    for i, m, n in [(13,3,5),(14,4,9),(15,5,8),(16,4,6)]:
        modulus = m * n
        coprime = math.gcd(m, n) == 1
        x0 = modulus - 2
        rm, rn = x0 % m, x0 % n
        values = [(x % m, x % n) for x in range(modulus)]
        compatible = _crt_solutions(rm, rn, m, n)
        if coprime:
            answers[f"C{i:02d}"] = {
                "T1": _entry(len(set(values))),
                "T2": _entry(len(compatible)),
                "T3": _entry(compatible[0]),
                "T4": _entry(False),
            }
        else:
            answers[f"C{i:02d}"] = {
                "T1": _entry(len(set(values))),
                "T2": _entry(len(compatible)),
                "T3": _entry(_collision(values), m=m, n=n),
                "T4": _entry(len(_crt_solutions(0, 1, m, n))),
            }

    for i, n, a, b, c, d in [(17,12,5,2,7,0),(18,15,6,5,4,1),(19,20,3,0,7,0),(20,18,5,1,6,4)]:
        answers[f"M{i:02d}"] = {
            "T1": _entry(len(set(_aff(a, b, n)))),
            "T2": _entry(len(set(_aff(c, d, n)))),
            "T3": _entry((c * a) % n),
            "T4": _entry(False),
        }

    return {"version": "gold-set-v0", "answers": answers}
