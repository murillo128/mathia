# MI-005 — Test-family fidelity is governed by measured span, scale, and admissibility

**Evidence level:** supported by exact reconstruction, aliasing, closed-span, local-programming, and constrained-cone results

## Core intuition

The raw number of tests is not the decisive variable. For linear source measurements, fidelity is controlled by the closed linear span of the functions that are actually measured, together with the spatial scale on which they live and the source class on which injectivity is required. An infinite analytically coupled family can be complete, while an infinite regularly sampled family can have an exact alias horizon. Admissibility constraints help only when they shrink this measured quotient rather than merely the ambient function class.

## Strongest justified principle

AF-020 gives the complete endpoint: the full Weil functional determines the generalized-prime measure on its visible support. AF-021--AF-023 show that a fixed finite family leaves positive-dimensional local collision fibers at regular source points. AF-024--AF-027 show the opposite danger: a flexible smooth or double-positive test class can retain enough local response freedom to manufacture finite-order isolation, so singularity or positivity alone does not certify arithmetic specificity.

AF-028 supplies the first exact infinite-family positive repair. A fixed compact double-positive modulation family indexed by frequencies with a finite accumulation point determines every finite signed measure on the visible interval, by analytic continuation of its cosine transform. Thus finite-dimensional nonidentifiability does not extend automatically to an infinite family whose parameter set is analytically complete.

AF-029 shows that infinitude alone is still insufficient. Sampling the same modulation family on the lattice `nh` retains only the pushforward through `x -> cos(hx)` and is faithful on `(0,B)` exactly up to the Nyquist-type threshold `hB<=pi`; beyond that threshold exact cosine aliases occur. The corresponding generalized-prime norm horizon is `exp(pi/h)`.

AF-030 gives the invariant formulation. For a scalar test family `F` on compact `X`, the complete linear measurement map on finite signed measures has kernel exactly the annihilator of

`V_F = closure(span F) subset C(X)`.

It is injective on all signed measures exactly when `V_F=C(X)`, and on a restricted source class `S` exactly when `(S-S) intersect V_F^perp={0}`. Functions obtainable only by multiplication or another generated-algebra operation do not count unless those functions are themselves measured or their values are derivable from the observed linear data.

## What remains possible

A mathematically forced nonlocal or infinite test family can defeat the local Beurling programming obstruction if its actual measured span is complete on the declared source category. Conversely, a global-looking family may still have exact aliases, an incomplete closed span, or a large source-restricted annihilator. The useful next step for any proposed explicit-formula family is therefore to compute `V_F`, its annihilator, and any scale-dependent alias fibers before interpreting numerical injectivity or positivity.

## Status / novelty

The measure duality, identity-theorem, cosine aliasing, constant-rank, and positive-definite modulation ingredients are classical or exact persisted results. Their synthesis is an exact measured-span gate for Mathia fidelity, not a theorem about every possible nonlinear observation scheme.

## Falsification criterion

Exhibit a linear test family whose measurements determine all finite signed measures while its closed measured span is a proper subspace of `C(X)`, or a source pair in `S` differing by a nonzero element of `V_F^perp` yet separated by the same measurement vector. For an infinite family, a positive advance must identify the exact completeness mechanism rather than appeal only to cardinality.

## Lean-formalizable core

- Annihilator characterization of the linear measurement kernel.
- Restricted-source injectivity criterion.
- Cosine-map alias criterion on a bounded interval.
- Finite-test Jacobian/fiber dimension and exact scale horizon.
