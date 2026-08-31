# MI-007 — Pointing breaks the Möbius gauge, but the first critical positive-cone scale exposes classical additive correlations

**Evidence level:** supported by exact Gram identities, matched controls, and literature-backed correlation reductions

## Core intuition

The positive exponent cone does contain more structure than the signed prime-character group, and a fixed target can break the Möbius torus gauge that defeats unpointed statistics. But at the first nontrivial finite-horizon scale `N~T`, those gains do not produce a new RH selector: the geometry is a universal sinc-resolution transition, and the arithmetic that survives pointing is organized by familiar additive correlations.

## Strongest justified principle

PL-072 establishes the ambient resolution scale. For positive-cone characters `n^{-it}` observed on `[0,T]`, the Gram matrix is asymptotically the identity for `N=o(T)`, adjacent top characters become unresolved for `N/T->infinity`, and the local `N~T` transition is a universal sinc kernel coming only from `log(n+k)-log(n+j)~(k-j)/n`. Prime factorization does not enter this first phase transition.

PL-073 then isolates the coefficient issue. On the square-free hypercube, multiplying coefficients by `mu(n)` is exactly translation by the prime-torus element with every coordinate `-1`. Haar value distributions and every unpointed Gram spectral invariant are therefore unchanged. The Möbius orientation is invisible unless the observable keeps a fixed target or another gauge-breaking datum.

PL-074 computes what the simplest pointing reveals at the critical scale. Fixed additive lags survive. For square-free support `mu^2`, their constants are Mirsky's square-free-pair singular series; for the Möbius orientation `mu`, they are fixed-shift Chowla correlations. The gauge has been broken, but the recovered variable has landed in classical additive-correlation theory rather than a new exponent-lattice spectral invariant.

PL-075 sharpens the critical-line caution. If a coefficient sequence has a nonzero fixed-lag correlation density, inserting `n^{-sigma}` gives a deterministic fixed-lag scale `T^{1-2 sigma}`. Hence `sigma=1/2` is the unique order-one weight for **any** such system. Mirsky's square-free control realizes the same half-weight transition unconditionally, while the von Mangoldt channel reduces, conditionally, to Hardy--Littlewood prime-pair constants. The appearance of `1/2` at fixed lag is therefore a Fourier/correlation balance, not a zero-selection mechanism.

## What remains possible

These results do not classify the full lag sum, lags growing with `T`, mesoscopic windows, Montgomery-type pair correlation, or another genuinely global coefficient coupling. A surviving positive-cone mechanism must live beyond the universal fixed-lag resolution law and must distinguish the rational-prime norm system from matched generalized-prime or coefficient controls without merely restating Chowla, Hardy--Littlewood, or another existing correlation problem.

Pointing remains mathematically meaningful: it converts a gauge-invariant quotient into a target-relative observable. The lesson is that **breaking the gauge and obtaining arithmetic sensitivity are separate from obtaining a new arithmetic mechanism**.

## Status / novelty

Montgomery--Vaughan mean-value estimates, Kronecker/torus gauge ideas, Mirsky square-free correlations, and Chowla/Hardy--Littlewood problems are classical prior art as recorded in the persisted findings. The exact placement of the gauge break, sinc transition, and fixed-lag half-weight boundary is the supported Prime Lattice synthesis.

## Falsification criterion

Produce a fixed-lag pointed positive-cone invariant at `N~T` whose limiting value is not determined by the universal sinc kernel together with the corresponding additive coefficient correlation, or show that the `sigma=1/2` order-one transition fails for a coefficient system with a nonzero fixed-lag density. A positive advance would instead derive a genuinely global/growing-lag invariant that passes matched non-Riemann controls.

## Lean-formalizable core

- Diagonal-unitary equivalence of Möbius-oriented and unoriented Gram matrices.
- Finite-horizon Gram kernel and local sinc limit.
- Fixed-lag scaling `T^{1-2 sigma}` from a correlation-density hypothesis.
- Torus-translation identity for completely multiplicative unimodular coefficient gauges.