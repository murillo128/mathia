# MI-009 — Dirichlet factorization is a gauge torsor; splitting the inverse does not split the cancellation burden

**Evidence level:** supported through MC-081 by exact Dirichlet-convolution identities, rigidity of locally finite multiplicative factorizations, and literature-backed Selberg--Delange asymptotics

## Core intuition

Factoring the Möbius inverse into two arithmetic pieces does not automatically distribute the hard cancellation. The complete recovery identity `a*k=mu` is algebraically exact for an enormous gauge family: one factor can be prescribed and the other adjusted by convolution. Without an independently source-forced gauge, apparent balance between the factors is therefore representation choice rather than new arithmetic information.

The natural gauges tested so far do not evade this. Symmetric/fractional zeta factorizations, near-identity moving gauges, residue-class prime allocations, and locally finite prime-power splittings either inherit only logarithmic Selberg--Delange behavior, move the hard endpoint into one factor, or rigidify to a partition of the prime set. A useful factorization must expose a **non-tautological coupled residual or source-selected interaction**, not merely rewrite `mu` as a product whose exponents still add to the original singularity.

## Strongest justified principle

MC-073 identifies the decisive algebraic boundary. For any Dirichlet factorization `a*k=mu`, the full coupled recovery of the corresponding partial sums reconstructs `M(X)` exactly. The complete coupled identity is therefore not by itself a mechanism for proving cancellation; it is a re-expression of the target.

MC-074 shows that the nonuniqueness is structural. Dirichlet factorizations form a torsor under convolution units, so one factor can be changed arbitrarily while compensating in the other. A useful split needs an external arithmetic condition that fixes or sharply restricts this gauge before the desired cancellation is inspected.

MC-075--MC-077 test canonical-looking analytic gauges. The symmetric fractional split is governed by `zeta(s)^(-1/2)` and gives only logarithmic-scale cancellation; moving the fractional parameter toward an identity factor merely shifts the tautological burden; and a broad near-identity harmonic class cannot divide a fixed Mertens power saving into two easier power-saving estimates.

MC-078--MC-080 test prime-side gauges. Regular residue allocations remain Selberg--Delange objects. Exact square-free multiplicative factorizations of `mu` are prime partitions, and the same rigidity persists for locally finite prime-power factorizations; a genuinely non-prime split requires infinite local tails and hence a different analytic burden.

MC-081 gives the asymptotic accounting law for regular prime-average factorizations: their Selberg--Delange exponents form a resonance budget whose sum is fixed at `-1`. Generic factors therefore retain nonzero classical leading terms even though their product is `1/zeta`. The singularity has been allocated, not removed.

## What remains possible

A live factorization route must derive a gauge from source structure and then prove cancellation in something strictly weaker than the full tautological recovery: a truncated or annular coupled residual, a nonlocal recurrence, an interaction between factors that is invisible to their separate partial sums, or a gauge whose defining constraint itself carries new signed arithmetic information.

The exact factorization identities remain useful as diagnostics because they show where cancellation can hide. They are not evidence that the burden has been reduced until the surviving coupled term is bounded without assuming a Mertens-equivalent estimate for either factor or for the full recovery.

## Status / novelty

Dirichlet convolution, Euler products, fractional powers of zeta, prime partitions, and Selberg--Delange asymptotics are classical. The persisted synthesis is the gauge principle: **Dirichlet factorization has large noncanonical freedom, locally finite multiplicative splits rigidify to prime allocation, and regular analytic splits conserve the total resonance budget rather than distribute away the Mertens difficulty**.

## Falsification criterion

Exhibit a source-canonical factorization in the covered regular/local categories whose factors both satisfy genuinely weaker power estimates that combine to a Mertens power saving without importing an equivalent zero-free statement; or violate the prime-partition/resonance-budget identities under their stated hypotheses.

## Lean-formalizable core

- Dirichlet factorization torsor identity.
- Exact coupled recovery tautology.
- Square-free/local prime-partition rigidity.
- Conservation of regular prime-average Selberg--Delange exponents.
