# Remediation after the independent gold-set-v0 audit

The issue-8 independent audit was merged from PR #20 with verdict **REVISE**. No Qwen or other solver result existed at that point, so the freeze rule allowed correcting `gold-set-v0` in place.

This note records the corrections without rewriting the original audit evidence in `INDEPENDENT_AUDIT.md`.

## 1. Semantic leakage removed

- Reversibility cases no longer expose enough map rows to contain the stored collision witness or an obvious duplicate-output proof. Explicit gcd anchors were removed.
- GCD cases no longer publish `before_gcd` / `after_gcd`; hidden tasks use unseen legal and perturbed transformations.
- CRT reconstruction targets are chosen outside the small visible sample table.
- Composition cases no longer publish the composed affine formula, so the identity case does not reveal the composition task.

## 2. Witness scoring made semantic

The generic `witness_pair` kind was replaced by mechanism-specific kinds:

- `mul_collision_pair`
- `crt_collision_pair`

`private_truth.py` now stores private mechanism parameters and `scoring.py` verifies the submitted pair mathematically. The validator checks canonical answers, alternative valid witnesses, reversed orderings, and non-canonical residue representatives through modular semantics.

## 3. Shuffled control made mechanism-orthogonal

The original shuffled control borrowed structural text from another gold-set cluster. The audit found that gcd/unit language could still help CRT or affine tasks.

The corrected fixture uses a fixed pool of unrelated mathematical mechanisms (similarity, derivatives, expectation, inclusion-exclusion, convergence). Each situation selects a pool entry deterministically through `shuffled_context_id`; assignment is not based on answer subtype.

## 4. Authored controls cleaned and length-balanced

- The gcd `sterile` text no longer describes a solution procedure.
- The coprime CRT `wrong` context is now wrong for the current coprime cases rather than accidentally giving their local conclusion.
- Structural/factual/procedural/sterile/wrong texts were rewritten to roughly comparable lengths. `validate.py` rejects extreme authored-context length imbalance.

## 5. Ceiling/redundancy reduced

The original fixture had 51 Boolean tasks and deterministic duplicates such as reversibility T1=T2, gcd T2=T3, and composition T3=T1∧T2.

The corrected 80 tasks use more heterogeneous outputs and interventions:

- congruence solution counts;
- functional-graph transfer;
- image-size counterfactuals;
- modular inverses and semantic witnesses;
- gcd values after legal and deliberately perturbed transformations;
- CRT distinct-coordinate counts and reconstruction;
- affine image sizes and composition coefficients;
- diagnosis questions retained where they directly test the conceptual claim.

This does not prove that Qwen3-8B will avoid ceiling; that remains an empirical risk for the frozen-model run.

## Validation performed during remediation

The corrected fixture was independently instantiated in a local Python scratch environment and its validator completed with:

```text
validated corrected gold-set-v0: 20 situations / 80 hidden tasks / semantic witness scoring
```

The committed validator is the authoritative reproducible check. A fresh-context independent re-audit is required before #9 freezes the evaluation manifest.
