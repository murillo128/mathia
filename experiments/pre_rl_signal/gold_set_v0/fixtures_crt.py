from __future__ import annotations

import math

from contexts import crt_context, pool_id


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def _sample_crt(m: int, n: int) -> list[list[object]]:
    return [[x, [x % m, x % n]] for x in range(min(m * n, 4))]


def build() -> list[dict[str, object]]:
    situations: list[dict[str, object]] = []
    specs = [(13, 3, 5), (14, 4, 9), (15, 5, 8), (16, 4, 6)]
    reconstruction_targets = {13: 7, 14: 23, 15: 17, 16: 10}
    polynomial_specs = {13: (2, 1), 14: (3, 2), 15: (4, 3), 16: (5, 1)}
    relation_specs = {13: (3, 1, 1), 14: (4, 2, 3), 15: (5, 2, 4), 16: (4, 1, 2)}
    replacement_moduli = {13: 6, 14: 6, 15: 10}

    for i, m, n in specs:
        coprime = math.gcd(m, n) == 1
        modulus = m * n
        x0 = reconstruction_targets[i]
        rm, rn = x0 % m, x0 % n
        linear_c, constant_d = polynomial_specs[i]
        relation_modulus, relation_weight, relation_target = relation_specs[i]

        if coprime:
            tasks = [
                _task("T1", "reconstruction", "near", f"Give the unique residue x in [0,{modulus-1}] with x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n}).", "int"),
                _task("T2", "coordinate-operation", "medium", f"Let x satisfy x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n}). For P(x)=x^2+{linear_c}x+{constant_d}, return [P(x) mod {m}, P(x) mod {n}].", "int_pair"),
                _task("T3", "coupled-coordinate", "far", f"How many residues x modulo {modulus} satisfy ((x mod {m}) + {relation_weight}(x mod {n})) mod {relation_modulus} = {relation_target}?", "int"),
            ]
            replacement_n = replacement_moduli[i]
            tasks.append(
                _task("T4", "counterfactual-representation", "far", f"Replace modulus {n} by {replacement_n}. How many distinct pairs (x mod {m}, x mod {replacement_n}) occur as x ranges modulo {m * replacement_n}?", "int")
            )
        else:
            tasks = [
                _task("T1", "compatibility-count", "near", f"How many residues x modulo {modulus} satisfy x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n})?", "int"),
                _task("T2", "coordinate-operation", "medium", f"For any x satisfying x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n}), let P(x)=x^2+{linear_c}x+{constant_d}. Return [P(x) mod {m}, P(x) mod {n}].", "int_pair"),
                _task("T3", "counterexample", "far", f"Give two distinct residues [x,y] modulo {modulus} with the same pair of residues modulo {m} and modulo {n}.", "crt_collision_pair"),
                _task("T4", "coupled-coordinate", "far", f"How many residues x modulo {modulus} satisfy ((x mod {m}) + {relation_weight}(x mod {n})) mod {relation_modulus} = {relation_target}?", "int"),
            ]

        situations.append({
            "id": f"C{i:02d}",
            "cluster": "crt_decomposition",
            "title": f"Residue-coordinate decomposition mod {m} and {n}",
            "visible": {
                "statement": f"Encode x modulo {modulus} by the pair (x mod {m}, x mod {n}).",
                "moduli": [m, n],
                "sample_pairs": _sample_crt(m, n),
                "domain_size": modulus,
            },
            "contexts": crt_context(coprime),
            "shuffled_context_id": pool_id(i),
            "hidden_tasks": tasks,
        })
    return situations
