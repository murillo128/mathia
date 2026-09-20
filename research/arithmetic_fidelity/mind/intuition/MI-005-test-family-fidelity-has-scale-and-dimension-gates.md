# MI-005 — Test-family fidelity is governed by measured span, scale, admissibility, and source-law rank

**Evidence level:** supported by exact reconstruction, aliasing, closed-span, local-programming, constrained-cone, and finite-atomic moment results through [AF-444](../../findings/AF-444-one-surplus-consecutive-moment-sharply-restores-unit-atom-fidelity.md)

## Core intuition

The raw number of tests is not the decisive variable. For linear source measurements, fidelity is controlled by the closed linear span of the functions that are actually measured, together with the spatial scale and the source class on which injectivity is required. In finite-dimensional latent-source models, measurement rank matters only relative to the admitted deformation dimension and source laws: equal rank can leave a programmable collision fibre, while a surplus measurement becomes decisive only when the source category supplies an invariant that the extra coordinate exposes.

## Strongest justified principle

AF-020 gives the complete endpoint: the full Weil functional determines the generalized-prime measure on its visible support. AF-021--AF-023 show that a fixed finite family leaves positive-dimensional local collision fibres at regular source points. AF-024--AF-027 show the opposite danger: a flexible smooth or double-positive test class can retain enough local response freedom to manufacture finite-order isolation, so singularity or positivity alone does not certify arithmetic specificity.

AF-028 supplies an exact infinite-family positive repair. A fixed compact double-positive modulation family indexed by frequencies with a finite accumulation point determines every finite signed measure on the visible interval by analytic continuation of its cosine transform. AF-029 shows that infinitude alone is insufficient: lattice sampling retains only the pushforward through `x -> cos(hx)` and is faithful on `(0,B)` exactly up to the alias threshold `hB<=pi`.

AF-030 gives the invariant linear formulation. For a scalar test family `F` on compact `X`, the complete linear measurement map on finite signed measures has kernel exactly the annihilator of `V_F=closure(span F)`. It is injective on all signed measures exactly when `V_F=C(X)`, and on a restricted source class `S` exactly when `(S-S) intersect V_F^perp={0}`. Functions obtainable only by multiplication or another generated-algebra operation do not count unless those functions are themselves measured or derivable from the observed linear data.

AF-439--AF-444 sharpen the restricted finite-dimensional side. AF-443 proves that `K` independently movable positive support coordinates can locally absorb a remote mark flip while preserving any fixed `K` reciprocal-power moments. AF-444 then shows that one consecutive surplus moment becomes globally decisive for positive **unit-weight** atoms: the first `K+1` power sums determine the top Newton--Girard coefficient, which is zero for a `K`-atom source padded by zero and strictly positive for the corresponding `(K+1)`-atom source. Thus “more measurements” becomes meaningful only together with the source law that converts the surplus rank into a discriminator.

## What remains possible

A mathematically forced nonlocal or infinite test family can defeat local programming when its actual measured span is complete on the declared source category. A finite family can also become exact on a structured finite-dimensional source class when the observation surplus exposes an algebraic invariant. Conversely, a global-looking or high-rank family may still have aliases, an incomplete span, or a nuisance fibre if source freedom grows with observation rank.

For any proposed explicit-formula or moment family, compute the measured quotient on the **declared source class**: identify the span/alias structure, compare observation rank with effective latent dimension, and state the source relation that removes the remaining fibre. Cardinality alone is not evidence of fidelity.

## Status / novelty

The measure duality, identity-theorem, cosine aliasing, constant-rank, Newton--Girard and finite-atomic reconstruction ingredients are classical or exact persisted results. Their synthesis is a measured-span/source-law gate for Mathia fidelity, not a theorem about every nonlinear observation scheme.

## Falsification criterion

Exhibit a covered linear test family whose measurements determine all finite signed measures while its closed measured span is a proper subspace of `C(X)`, a source pair in `S` differing by a nonzero element of `V_F^perp` yet separated by the same measurement vector, or positive unit-weight `K`- and `(K+1)`-atom multisets sharing their first `K+1` power sums. For a claimed finite-dimensional repair, a positive advance must identify the exact source law or invariant that kills the nuisance fibre rather than appeal only to rank.

## Lean-formalizable core

- Annihilator characterization of the linear measurement kernel.
- Restricted-source injectivity criterion.
- Cosine-map alias criterion on a bounded interval.
- Finite-test Jacobian/fibre dimension and exact scale horizon.
- Newton--Girard separation of positive unit-weight `K`- and `(K+1)`-atom moment classes.