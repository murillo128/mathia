# MI-008 — All fixed finite-order Gram-phase mixing can be a deterministic clock null

**Evidence level:** proved

## Core intuition

A finite collection of Gram-point prime-phase samples can display coherence, Haar marginals, or full joint Haar behavior without introducing new arithmetic randomness. This remains true for fixed irregular lags, affine index thinning, polynomial and noninteger-power sparse selectors, and even for one deterministic selector whose complexity grows so that **every fixed finite-order finite-prime Haar test eventually passes**.

The useful discriminator is therefore not high finite-order mixing. It is quantitative control when test complexity grows jointly with height, or information living outside the admitted deterministic phase/clock representation.

## Strongest justified claim

VIS-150--VIS-156 classify fixed commensurate lag geometries through finite differences/Vandermonde moments of the inverse Gram clock. Critical laws are Haar on fibers of an exact deterministic quotient; fixed affine subsampling changes constants but not the hierarchy.

VIS-157--VIS-159 extend this to nonlinear sparse selectors. Degree-`d` polynomial sampling is Haar through `d` fixed samples and fails at `d+1` through an exact higher-difference character. The analogous threshold for `floor(n^alpha)` is `ceil(alpha)`.

VIS-160 diagonalizes these controls. By using increasingly high polynomial degrees on increasingly long stages, one deterministic increasing selector can make every fixed finite-prime, fixed-offset, fixed-order character average tend to zero. Stage boundaries have zero density, so all fixed finite-dimensional Haar tests pass simultaneously in the eventual sense.

## Synthesis of evidence

“Let the selector become more complicated with height” is not by itself an escape. Complexity can grow adversarially while remaining entirely deterministic and while defeating every fixed test one at a time. A meaningful sampling theorem must freeze a **joint growth regime**: sample order, offsets, prime support, character complexity, required accuracy, and selector complexity must be controlled together.

This moves the line from qualitative equidistribution to quantitative uniformity. A natural pre-specified selector may still exhibit genuinely source-sensitive behavior, but the evidence must show that it outperforms the diagonal clock control in the same growing test class.

## Counterevidence / boundary cases

VIS-160 is existential and diagonal. It supplies no useful rate for its stage boundaries and does not classify a natural explicit growing-degree selector. It also does not treat tests whose complexity grows with the observation height.

The theorem concerns finite prime-phase observables. Adding a separately normalized analytic coordinate may leave the clock null, but VIS-161--VIS-162 show that “not obviously a phase function” is not enough; stable decoder complexity must be tested separately.

## Epistemic status

**Exact fixed-test control:** every predetermined finite collection—and indeed every fixed finite-order test in a countable family—can be asymptotically passed by a deterministic growing-complexity Gram selector. Only jointly growing tests or a different information category remain viable.

## Novelty/prior-art status

The construction uses classical Weyl criteria, polynomial clock laws, diagonalization, and the broader deterministic completely-uniform-distribution phenomenon. Finding-level prior-art boundaries apply.

## Falsification criterion

Produce a fixed finite-dimensional prime-phase character test that the VIS-160 selector construction cannot include, or find a positive-density stage-boundary obstruction. Strategically, prove a quantitative growing-complexity law for a natural source-defined selector that separates it from all such deterministic controls.
