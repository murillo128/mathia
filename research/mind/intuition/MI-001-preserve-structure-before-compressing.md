# MI-001 — Preserve the discriminating structure before compressing

**Evidence level:** supported, with exact deterministic and statistical-sufficiency theorems in several categories

## Core intuition

Across Mathia, the recurring failure is not spectralization, positivity, or taking a scalar in the abstract. It is applying a transformation whose induced indistinguishability relation already identifies states or models that the later arithmetic claim needs to distinguish. Arithmetic Fidelity turns this into exact model theorems: recoverability is fiberwise, admissible observables define a maximal quotient, statistical compression is governed by likelihood-ratio sufficiency, and downstream processing cannot recreate information absent from the complete retained statistic.

## Strongest current principle

AF-001 proves `d=r∘T` exactly when `d` is constant on `T`-fibers; AF-003 says the joint map of all admissible observables is the maximal quotient available to a constrained repair. AF-012--AF-013 add the stochastic analogue: for a finite family of probability models, the reference-relative likelihood-ratio vector is the complete statistic, and zero loss of one strictly convex multidistribution divergence is equivalent to statistical sufficiency for the whole experiment. Subsequent garbling only adds nonnegative loss.

AF-014 prevents an opposite overstatement. Quadratic/positive data are not automatically information-poor: a full-rank Gram matrix retains all relative maximal-minor signs and loses only one global orientation torsor relative to `SO(d)`. The right audit is therefore always the **exact fiber of the actual destination**, not a generic slogan about sign or positivity.

AF-015--AF-017 add a source/category dimension. Bare multiplication remembers prime type but not rational-prime norms; adjoining a norm can restore them; retaining the exact Euler-product function can be faithful to the unordered norm multiset; retaining only the divisor can lose that information again through zero-free factors. AF-016 adds that breaking base-model automorphisms is only an escape condition unless the observable category has a completeness theorem.

The branch evidence instantiates these rules. Prime Flute's compact-resolvent clone shows a spectral quotient can identify prime/non-prime geometry; Prime Circle's finite Hardy Calkin algebra loses mixed arithmetic while the relative trace sector retains more; Weil Inertia separates local-main/conditioning information from optimization; Weil Positivity shows positive determinant carriers can retain arithmetic before a later completion or polar repair externalizes it.

## Consequence for synthesis

The order of operations is

`derive admissible category -> compute complete retained statistic/fibers -> test source specificity -> only then optimize, spectralize, complete, or prove positivity`.

A repair that adds a target-carrying mark or a normalization chosen after inspecting the desired zeros has not passed this gate.

## Status / novelty

The component fidelity theorems are persisted findings with classical ingredients. Their use as a cross-branch order-of-operations principle is a supported synthesis.

## Falsification criterion

Find a canonical pipeline where the target varies inside the complete admissible fiber/statistic at some stage, no later stage receives new admissible information, yet the final invariant recovers the target. Within the audited categories this would contradict persisted fidelity results.

## Lean-formalizable core

- Fiberwise factorization and post-processing monotonicity.
- Maximal admissible quotient.
- Likelihood-ratio/Jensen equality and statistical sufficiency.
- Gram fiber modulo `O(d)` and orientation-torsor refinement.