# MI-008 — Moving comparators need uniform family coherence, not finite-prefix imitation plus per-object cancellation

**Evidence level:** supported by MC-053--MC-056; the fixed-class transfers and Burgess coherence bound are theorem-level in their stated hypotheses

## Core intuition

Allowing the comparator to depend on the observation scale is a real escape from fixed-comparator transfer theorems, but finite-prefix agreement and a good exponent for each frozen object are still too weak. The missing resource is a **uniform, scale-coherent cancellation certificate whose dependence on the moving arithmetic object is cheaper than the Möbius estimate being sought**.

Quadratic characters make this boundary exact. One can reproduce every Möbius coefficient through a chosen scale while each frozen comparator has square-root cancellation, yet uniform constants and changes of interpolant carry global arithmetic costs that the finite prefix does not reveal.

## Strongest justified principle

MC-053 closes fixed complex square-free-supported comparators: under global Möbius closeness, a boundary zero, and a power bound, conjugate-square positivity transfers the same zeta zero-free half-plane. MC-054 closes the fixed bounded completely multiplicative Liouville-close class by the corresponding Venturini mechanism. Complex phases alone therefore do not evade exponent transfer when the comparator is fixed.

MC-055 constructs the moving escape sharply. For every finite `X`, a quadratic character can be chosen with `chi(p)=-1` for all primes `p<=X`, so `mu^2 chi` agrees exactly with Möbius on every `n<=X`. Each frozen character has an unconditional square-root summatory exponent, but its usable constant may depend strongly on the conductor; any family-uniform critical certificate is bounded below by the normalized Mertens value on the very prefix being imitated. Per-object exponents therefore do not assemble into a uniform theorem.

MC-056 adds unconditional multiscale coherence. If two distinct prime-conductor quadratic interpolants both agree on the whole prefix through `X`, their product character is principal on that interval. Burgess then forces `q_1 q_2 >= X^{4-o(1)}`. Distinct exact-prefix certificates cannot be replaced freely while keeping uniformly mild conductor complexity.

## What remains possible

A moving-comparator strategy may still work if one comparator remains valid across a long scale range, if conductor growth is accompanied by estimates uniform enough in that growth, or if successive comparators satisfy a stronger source-forced relation than shared finite-prefix values. Those are genuine family theorems, not consequences of local interpolation.

## Status / novelty

The analytic transfer mechanisms, quadratic-character interpolation, Pólya--Vinogradov/Burgess bounds, and character conductor theory are classical or literature-backed. The synthesis is the uniformity gate: **a moving family must pay for both cancellation constants and arithmetic coherence across scale**.

## Falsification criterion

Construct a scale-dependent comparator family with exact or sufficiently strong Möbius fidelity and a uniform cancellation/coherence budget provably weaker than the desired Mertens bound, or show that the Burgess/coefficient-prefix obstructions do not apply under its stated hypotheses.

## Lean-formalizable core

- Fixed-comparator exponent-transfer implication.
- Exact finite-prefix quadratic interpolation.
- Lower bound of family cancellation constant by prefix Mertens data.
- Product-character prefix agreement and conductor-coherence inequality.
