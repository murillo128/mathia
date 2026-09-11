# MI-008 — Fixed finite commensurate Gram geometry is a deterministic clock null

**Evidence level:** proved

## Core intuition

A fixed finite collection of Gram-point prime-phase lags can display coherence, deterministic curves, Haar marginals, or full joint Haar behavior without introducing new arithmetic randomness. The exact inverse Gram clock generates all of these regimes. This remains true after replacing equal-step lags by any fixed finite commensurate integer-node geometry and after restricting the starting Gram indices to any fixed arithmetic progression.

Visual complexity in such a finite delay embedding is therefore not evidence of a new prime-phase source unless it survives the deterministic clock quotient appropriate to its node set and sampling stride.

## Strongest justified claim

VIS-150--VIS-153 classify consecutive equal-step lag vectors. Every fixed joint character has a first nonzero lag moment of order at most the dimension; the deepest finite difference determines the transition `h^r ~ N^(r-1)(log N)^2`. At critical scaling, an exact integer change of coordinates produces Haar in the first `r-1` directions and one deterministic top clock curve.

VIS-154 extends the threshold to every fixed set of distinct positive integer lag ratios `b_1,...,b_r`. The Vandermonde moment matrix is nonsingular, so every nontrivial character has a first surviving moment of order at most `r`, and a primitive Lagrange/Vandermonde character realizes the deepest order. The threshold exponent is unchanged.

VIS-155 resolves the irregular critical window. The primitive deepest character defines a canonical quotient; the limiting law is Haar on its codimension-one fibers and deterministic on the quotient curve. Equal-step Newton coordinates are only one special basis for this general finite-node structure.

VIS-156 then fixes a nonconsecutive sampling control. For every fixed affine index subsequence `a+q n`, the finite-prime population remains Haar and the same fixed-node lag hierarchy survives. The fixed stride changes only deterministic clock constants, including the critical quotient winding.

## Synthesis of evidence

The deterministic-null family now includes fixed equal-step and irregular commensurate node sets, their subcritical/critical/supercritical regimes, and fixed arithmetic-progression thinning of the starting indices. Adding finite irregularity, choosing a critical scale, or selecting one fixed congruence class does not create a new source; it only changes the finite-difference/Vandermonde coordinates of the same smooth inverse clock.

A credible residual must leave this class by changing a genuine asymptotic hypothesis: growing dimension/node geometry/prime or Fourier support, a stride changing with `N`, genuinely non-affine or data-dependent sampling, noncommensurate real-time offsets, or an independently informative analytic coordinate such as Hardy `Z`, derivatives, or zero occupancy.

## Counterevidence / boundary cases

All current theorems fix the delay dimension, node set, sampling stride, prime support, and tested character as `N->infinity`. They do not give quantitative uniformity when any of these complexities grow.

Fixed affine subsampling is not a theorem for arbitrary sparse or selected Gram subsequences. Fixed integer-node lags are not a theorem for genuinely noncommensurate continuous-time offsets. Haar convergence is deterministic fixed-character equidistribution, not stochastic independence.

## Epistemic status

**Exact fixed-finite clock classification:** fixed commensurate lag geometries, including irregular integer nodes and fixed affine Gram-index sampling, are governed by the inverse Gram clock with coherent, Haar-fiber critical, and Haar regimes determined by the corresponding Vandermonde shear scale.

## Novelty/prior-art status

The findings use classical Gram asymptotics, uniform-distribution/exponential-sum tools, Vandermonde interpolation, and compact-group Fourier criteria and make no broad novelty claim. This intuition records their role as a Mathia control family.

## Falsification criterion

Exhibit a fixed finite commensurate node set or fixed affine Gram-index subsequence satisfying the stated hypotheses whose fixed-character limiting behavior is not captured by VIS-154--VIS-156. Alternatively, show that the primitive critical quotient or Haar-fiber law fails for an admissible character.