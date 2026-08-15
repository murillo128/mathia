from __future__ import annotations

"""Hand-selected public fixtures for gold-set-v0.

This module intentionally contains no exact hidden-task answers.
"""


def _rev_context(n: int) -> dict[str, str]:
    return {
        "factual": f"The examples compare multiplication modulo {n}; some multipliers repeat outputs and others hit every residue once.",
        "procedural": "For a new case, enumerate the residue map or compute gcd(multiplier, modulus); for congruences, enumerate solutions if needed.",
        "structural": "The central issue is information loss. Multiplication modulo n is reversible exactly for units: when the multiplier has an inverse the map can be undone; nonunits collapse distinctions that no later step can recover.",
        "sterile": "Modular arithmetic reveals a pleasing balance between periodicity and symmetry; residue classes reorganize arithmetic into finite recurring patterns.",
        "wrong": "The decisive property is whether the modulus is prime; composite moduli inherently prevent multiplication from behaving reversibly.",
    }


def _gcd_context() -> dict[str, str]:
    return {
        "factual": "Several pairs are replaced by (b, a-qb), and the numerical gcd remains unchanged in the displayed examples.",
        "procedural": "Apply Euclid's algorithm: replace the larger entry by a remainder, repeat, and read off the final nonzero value.",
        "structural": "The transformation preserves the set of common divisors: any divisor of a and b also divides a-qb, and conversely a=(a-qb)+qb. The numbers change, but the divisibility information relevant to gcd does not.",
        "sterile": "Euclid's algorithm is elegant because a long arithmetic question collapses through a sequence of smaller pairs until a simple terminal form appears.",
        "wrong": "The gcd is preserved only when q is the quotient from ordinary Euclidean division and the new remainder is nonnegative and smaller than b.",
    }


def _crt_context(coprime: bool) -> dict[str, str]:
    structural = (
        "Recording residues modulo two coprime moduli loses no information modulo their product: the two components are independent coordinates, so each compatible pair identifies exactly one class modulo mn."
        if coprime
        else "Two residue coordinates need not be independent. Shared factors create compatibility constraints and duplicate descriptions; uniqueness modulo the product fails unless the moduli are coprime."
    )
    wrong = (
        "Any two moduli give independent residue coordinates; the pair of residues always determines a unique class modulo the product."
        if coprime
        else "The pair of residues always determines a unique class modulo the product, even when the moduli share factors."
    )
    return {
        "factual": "The visible table records each integer by its pair of residues under two smaller moduli and shows the coordinate pattern.",
        "procedural": "Enumerate x modulo mn and compare the pairs (x mod m, x mod n); to reconstruct, scan for an x satisfying both congruences.",
        "structural": structural,
        "sterile": "Chinese-remainder style coordinates replace one cyclic description by several smaller periodic views, exposing a useful arithmetic decomposition.",
        "wrong": wrong,
    }


def _composition_context() -> dict[str, str]:
    return {
        "factual": "The visible maps are affine or multiplicative maps on a finite residue system, and their compositions can be computed explicitly.",
        "procedural": "Compose the formulas, reduce coefficients modulo n, then enumerate outputs to check whether the result is a permutation.",
        "structural": "Reversibility is stable under composition: composing bijections cannot lose information. For affine maps, the translation changes positions but the linear coefficient controls whether information is lost.",
        "sterile": "Composing modular maps creates intricate cyclic patterns whose repeated action can reveal hidden regularity in a finite system.",
        "wrong": "Adding a translation term is what makes an affine map reversible; a suitable offset can repair a noninvertible multiplier.",
    }


def _sample_mul(a: int, n: int) -> list[list[int]]:
    return [[x, (a * x) % n] for x in range(min(n, 10))]


def _sample_crt(m: int, n: int) -> list[list[object]]:
    return [[x, [x % m, x % n]] for x in range(min(m * n, 12))]


def _task(task_id: str, task_type: str, distance: str, prompt: str, answer_kind: str) -> dict[str, str]:
    return {"id": task_id, "type": task_type, "distance": distance, "prompt": prompt, "answer_kind": answer_kind}


def build_public() -> dict[str, object]:
    situations: list[dict[str, object]] = []

    rev_specs = [(1, 15, 4), (2, 15, 5), (3, 16, 3), (4, 16, 6), (5, 21, 8), (6, 21, 7), (7, 35, 12), (8, 35, 10)]
    for i, n, a in rev_specs:
        import math
        g = math.gcd(a, n)
        unit = g == 1
        b = (i * 3 + 1) % n
        target_b = (i * 5 + 2) % n
        tasks = [
            _task("T1", "prediction", "near", f"Without enumerating all residues, does x -> {a}x mod {n} permute all residue classes? Answer true/false.", "bool"),
            _task("T2", "transfer", "medium", f"Does the affine map x -> {a}x+{b} mod {n} permute all residues? Answer true/false.", "bool"),
            _task("T3", "counterfactual", "medium", f"For congruence {a}x ≡ {target_b} (mod {n}), how many residue-class solutions are there?", "int"),
        ]
        tasks.append(
            _task("T4", "representation-transfer", "far", f"In the functional graph of x -> {a}x mod {n}, is every vertex already on a directed cycle (no transient tails)? Answer true/false.", "bool")
            if unit
            else _task("T4", "counterexample", "far", f"Give two distinct residues [x,y] modulo {n} with {a}x ≡ {a}y (mod {n}).", "witness_pair")
        )
        situations.append({
            "id": f"R{i:02d}", "cluster": "reversibility", "title": f"Reversibility modulo {n} with multiplier {a}",
            "visible": {"statement": f"On residues modulo {n}, inspect x -> {a}x mod {n}.", "sample_mapping": _sample_mul(a, n), "modulus_is_prime": False, "multiplier_gcd_with_modulus": g if i in (2, 4) else None, "note": "This case exposes gcd explicitly as an anchor." if i in (2,4) else "The gcd is intentionally omitted in most situations."},
            "contexts": _rev_context(n), "shuffled_structural_from": "G09" if i % 2 else "C13", "hidden_tasks": tasks,
        })

    gcd_specs = [(9, 107, 35, 3), (10, 91, 26, -2), (11, 84, 30, 4), (12, 221, 52, 5)]
    import math
    for i, a, b, q in gcd_specs:
        c, d = b, a - q * b
        q2 = q + 2
        c2, d2 = b, a - q2 * b
        q3 = -3
        e, f = d2, c2 - q3 * d2
        situations.append({
            "id": f"G{i:02d}", "cluster": "gcd_invariance", "title": f"GCD-preserving change of representation {i}",
            "visible": {"statement": f"Compare gcd({a},{b}) with gcd({c},{d}), obtained from (a,b)->(b,a-qb) using q={q}.", "before_pair": [a,b], "after_pair": [c,d], "before_gcd": math.gcd(a,b), "after_gcd": math.gcd(c,d)},
            "contexts": _gcd_context(), "shuffled_structural_from": "R01" if i % 2 else "C14",
            "hidden_tasks": [
                _task("T1", "counterfactual", "near", f"If q is changed from {q} to {q2}, must gcd({a},{b}) still equal gcd({c2},{d2})? Answer true/false.", "bool"),
                _task("T2", "prediction", "medium", f"What is gcd({c2},{d2})?", "int"),
                _task("T3", "transfer", "far", f"Starting from ({c2},{d2}), apply the same form with q={q3}, giving ({e},{f}). What is gcd({e},{f})?", "int"),
                _task("T4", "diagnosis", "far", "Is nonnegative-small remainder an essential condition for gcd preservation in the transformation (a,b)->(b,a-qb)? Answer true/false.", "bool"),
            ],
        })

    crt_specs = [(13,3,5), (14,4,9), (15,5,8), (16,4,6)]
    for i, m, n in crt_specs:
        cop = math.gcd(m,n) == 1
        x0 = (7*i + 3) % (m*n); rm = x0 % m; rn = x0 % n
        tasks = [
            _task("T1", "prediction", "near", f"Is x -> (x mod {m}, x mod {n}) a bijection from residues mod {m*n} to all {m*n} pairs? Answer true/false.", "bool"),
            _task("T2", "reconstruction", "medium", f"How many x modulo {m*n} satisfy x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n})?", "int"),
        ]
        if cop:
            tasks.extend([
                _task("T3", "transfer", "far", f"Give the unique residue x in [0,{m*n-1}] with x ≡ {rm} (mod {m}) and x ≡ {rn} (mod {n}).", "int"),
                _task("T4", "counterfactual", "far", "If one modulus were replaced so the two moduli shared a factor, would uniqueness modulo the product still be guaranteed? Answer true/false.", "bool"),
            ])
        else:
            tasks.extend([
                _task("T3", "counterexample", "far", f"Give two distinct residues [x,y] modulo {m*n} with the same pair (mod {m}, mod {n}).", "witness_pair"),
                _task("T4", "diagnosis", "far", f"How many solutions modulo {m*n} satisfy x ≡ 0 (mod {m}) and x ≡ 1 (mod {n})?", "int"),
            ])
        situations.append({"id": f"C{i:02d}", "cluster": "crt_decomposition", "title": f"Residue-coordinate decomposition mod {m} and {n}", "visible": {"statement": f"Encode x modulo {m*n} by the pair (x mod {m}, x mod {n}).", "moduli": [m,n], "sample_pairs": _sample_crt(m,n), "domain_size": m*n}, "contexts": _crt_context(cop), "shuffled_structural_from": "R03" if cop else "G10", "hidden_tasks": tasks})

    comp_specs = [(17,12,5,2,7,0), (18,15,6,5,4,1), (19,20,3,0,7,0), (20,18,5,1,6,4)]
    for i, n, a, b, c, d in comp_specs:
        comp_a = (c*a) % n; comp_b = (c*b+d) % n
        situations.append({
            "id": f"M{i:02d}", "cluster": "composition", "title": f"Composition and affine reversibility mod {n}",
            "visible": {"statement": f"On residues mod {n}, compare f(x)={a}x+{b} and g(x)={c}x+{d}.", "composition_formula_observed": f"g(f(x)) = {comp_a}x+{comp_b} (mod {n})"},
            "contexts": _composition_context(), "shuffled_structural_from": "C15" if i % 2 else "G11",
            "hidden_tasks": [
                _task("T1", "prediction", "near", "Is f a permutation of all residues? Answer true/false.", "bool"),
                _task("T2", "prediction", "near", "Is g a permutation of all residues? Answer true/false.", "bool"),
                _task("T3", "composition", "medium", "Is g∘f a permutation of all residues? Answer true/false.", "bool"),
                _task("T4", "diagnosis", "far", f"Could changing only the translation term of f, while keeping multiplier {a}, change whether f is a permutation modulo {n}? Answer true/false.", "bool"),
            ],
        })

    assert len(situations) == 20
    return {"version": "gold-set-v0", "situations": situations}
