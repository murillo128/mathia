# WP-014 Schiffer formalization validation

Validation was run on 2026-08-29 in the Mathia issue #73 worktree after Gate 0
received an independent `PASS`.

## Environment

```text
Lean:    v4.32.2, commit f3b06c705e6c85f5314019d5d3baab0fec5b580c
mathlib: v4.32.2, commit 905b95818eb32af7874a58b427f50c1711a5e96c
```

The root `lean-toolchain`, `lakefile.toml`, and `lake-manifest.json` pin the
checked dependency graph.

## Checks

The repository-native focused command passed:

```bash
lake env lean formalization/WP014SchifferIndefinite.lean
```

The five public theorem signatures elaborated unchanged from the Gate-0 frozen
surface:

- `Mathia.WP014.abs_delta_mem`;
- `Mathia.WP014.schifferScalar_gt_one_third`;
- `Mathia.WP014.det_twoPointGram`;
- `Mathia.WP014.det_twoPointGram_neg`;
- `Mathia.WP014.twoPointGram_not_posSemidef`.

`#print axioms` reported the same standard mathlib trust footprint for each
public theorem:

```text
[propext, Classical.choice, Quot.sound]
```

A word-boundary scan of the Lean source found no `sorry`, `admit`, `axiom`,
`unsafe`, or `native_decide` marker.  `git diff --check` also passed.

## Evidence boundary

The proof uses exact ordered-field, calculus, trigonometric, polynomial, and
matrix reasoning.  The numerical Gate-0 falsification samples do not appear in
the Lean source and are not proof premises.  No external dependency beyond
mathlib, generated certificate, floating-point premise, or new axiom is used.

The accepted Lean boundary remains the specialized finite two-point
indefiniteness claim.  The source takes the PF-085 specialized kernel and
diagonal extension as inputs; it does not establish the upstream Schiffer
specialization, trace/Schatten claims, global Weil positivity, or an RH
consequence.

## Research handoff triage

No new material mathematical observation arose during local implementation.
The fifth-order-sine simplification was already recorded and disposed in
Mathia issue #73 as implementation-only evidence that does not change WP-014.
