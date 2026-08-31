# MI-005 — Finite test families have independent scale and dimension fidelity gates

**Evidence level:** supported by exact reconstruction, convex-geometric collisions, and local Beurling deformation fibers

## Core intuition

A test family can fail in two mathematically different ways. Restricting where tests are allowed to live creates a **scale horizon**; restricting how many independent tests are retained creates a **resolution horizon inside the visible scale**. Infinite numerical precision in finitely many test values does not remove the second obstruction.

## Strongest justified principle

AF-020 gives the positive endpoint for the Weil prime-power measure. The complete functional on `C_c^\infty(0,\infty)` determines the measure and hence the unordered generator-norm multiset. Restricting all tests to `(0,A)` has an exact interpretation: it determines precisely the generators below `e^A` and is completely blind to generators beyond that horizon.

AF-021 shows that replacing the complete test family by `d` scalar tests creates a different loss. On unrestricted positive atomic measures, every `d+2` source points force an exact same-test pair, and Tverberg gives arbitrarily large same-test families. This is not a precision issue but finite-dimensional affine compression.

AF-022 realizes the same phenomenon inside a genuine generalized-prime model rather than only in the ambient moment cone: varying `d+1` Beurling generator norms in an arbitrarily small chamber produces exact collisions for any fixed `d` Weil tests. AF-023 strengthens the statement at the source point itself. Whenever the finite-test Jacobian has full row rank at a selected `N>d` generator tuple, its exact same-test fiber is locally a positive-dimensional manifold. In particular, a rational-prime center satisfying that regularity lies on an exact generalized-prime collision fiber.

Thus any exceptional pointwise rigidity of the ordinary primes under finitely many tests must come from a singular or otherwise structurally constrained admissible locus; it cannot be inferred from exact arithmetic provenance or from arbitrarily accurate test values.

## What remains possible

A finite test family may still be faithful on a much narrower arithmetic class if independent structure makes the parameterization identifiable or forces the rational-prime point onto a genuinely rigid singular stratum. Positivity, Fourier support, Paley--Wiener restrictions, evenness, or another intrinsic test constraint can also change the regularity analysis. Those hypotheses must be part of the actual admissible category and audited there.

## Status / novelty

Measure determination by a complete test family, Radon/Tverberg-type affine dependence, and constant-rank/submersion arguments are classical. The persisted findings supply the exact Weil-measure scale filtration and the Beurling realization of finite-test fibers. The two-gate scale-versus-dimension synthesis is supported, not a theorem about every constrained explicit-formula test class.

## Falsification criterion

Prove local injectivity at a regular `N>d` generalized-prime deformation point, contradicting AF-023, or prove a natural constrained Weil-test family whose admissible geometry forces the rational-prime point to be isolated despite the surrounding Beurling degrees of freedom. A weaker finite-test claim must state exactly which source restrictions create that rigidity.

## Lean-formalizable core

- Affine-independence criterion for finite moment maps.
- Radon collision for `d+2` source points.
- Exact support-horizon statement for locally finite atomic measures.
- Finite-dimensional Jacobian/fiber calculation for the Beurling deformation map.