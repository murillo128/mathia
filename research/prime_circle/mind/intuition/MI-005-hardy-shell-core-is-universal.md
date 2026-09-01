# MI-005 — Canonical Hardy conductor limits classicalize into universal Hilbert/Carleman channels

**Evidence level:** supported by exact finite-trace reductions, trace-ideal classifications, and canonical conductor-limit calculations

## Core intuition

The Hardy interior/exterior split genuinely escapes finite cotangent endpoint closure, but the most canonical ways of taking that nonlocal structure to large conductor now classicalize as well. Fixed-shell data are trace class with the wrong zero-density scale; prime-conductor strong and microlocal limits become universal Hilbert/Carleman operators; affine rescaling is only unitary dilation plus a trace-class cocycle; and Möbius birth extraction repeats radical blocks unitarily. Even the canonical one-new-prime joint strong limit merely inflates the old fixed-conductor residual by reflection.

## Strongest justified principle

PC-075 and PC-081 classify the essential finite-family layer as universal Hilbert channels plus compact remainders. PC-100--PC-106 then close ordinary finite traces and fixed-shell relative moments inside cyclotomic hyperlogarithmic period algebras. PC-107 adds a categorical obstruction: a fixed-shell trace-class Fredholm determinant has reciprocal-summable zeros and `o(R)` counting, incompatible with Riemann's `T log T` zero density under an asymptotically linear normalization.

PC-108 tests the singular prime-conductor escape. The trace-class remainder `T_p` loses uniform nuclear control, but all logarithmically divergent Hilbert--Schmidt mass sits in the lowest Hardy coordinate and converges strongly to the classical Hilbert matrix. After that corner is removed, the residual stays `S_2` bounded and tends strongly to zero.

PC-109 recovers the escaping residual by the canonical mesh `r/p -> x`. The limit is the universal Carleman--Hilbert discretization defect `D=C-VHV*`; the off-origin compact part is independent of the prime conductor. PC-110 strengthens the classification: that off-origin part is actually trace class, so its `det_2` zero divisor collapses back to the same nuclear sparsity obstruction as PC-107.

PC-111--PC-112 close the natural affine-scale and exact-order repairs. Every scale defect is a unitary dilation of one universal object, pairwise scale differences are trace class, and Möbius births satisfy a radical-unitary factorization. Along a prime-power tower the whole compact spectral block repeats unitarily while only the scalar trace recovers the classical von Mangoldt identity. Dirichlet weighting restores convergence only by importing the classical zeta multiplier.

PC-113 finally checks one canonical genuinely joint limit before single-conductor scalarization. Adjoining a new prime `p` to fixed `q` and resolving the new fiber microlocally gives `reflection tensor R_q` in the strong limit. It preserves the old `q` arithmetic residual only by infinite-multiplicity inflation and creates no new discrete spectral locations. The term that tends strongly to zero may still carry norm or Schatten mass, so the result is a boundary rather than a theorem about every cross-level coupling.

## What remains possible

A surviving Hardy route must couple levels **before** they fall into the single-conductor universal models. It must be genuinely non-affine or cross-level and should identify information carried by norm/Schatten mass, incidence, provenance, or another joint invariant that is absent from the Hilbert/Carleman/reflection controls.

Merely taking `p -> infinity`, rescaling the conductor mesh, choosing another fixed affine scale, Möbius-inverting the scale cocycle, or replacing `det` by `det_2` no longer qualifies as an escape. A positive mechanism must also supply an independent RH-relevant selector or sign theorem; a new infinite product assembled from already-classicalized blocks is not sufficient.

## Status / novelty

Hilbert and Carleman operators, trace ideals, Fredholm determinants, dilation covariance, and Möbius inversion are classical. The persisted Prime-Circle contribution is the exact way the canonical Hardy remainder enters those classes and the resulting localization of any surviving arithmetic information to a genuinely cross-level pre-universalization sector.

## Falsification criterion

Produce a canonical prime-conductor or affine/Möbius limit covered by PC-108--PC-113 whose nonzero spectral data depends on the prime level beyond the stated unitary/universal models. A positive advance should instead isolate a joint all-shell observable that survives matched endpoint/Fourier controls and cannot be reduced to fixed-conductor residuals plus universal Hilbert/Carleman channels.

## Lean-formalizable core

- Prime-conductor Hilbert-corner decomposition.
- Microlocal step-kernel convergence to the Carleman--Hilbert defect.
- Trace-class classification of the off-origin defect.
- Dilation-cocycle and radical-unitary Möbius factorization.
