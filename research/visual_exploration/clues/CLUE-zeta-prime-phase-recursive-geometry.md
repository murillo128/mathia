---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
  - research/visual_exploration/findings/VIS-064-hybrid-independent-scale-transfer-error-bound.md
  - research/visual_exploration/findings/VIS-065-hybrid-contrast-single-factor-residual-coordinate.md
  - research/visual_exploration/findings/VIS-066-hybrid-joint-field-factor-residual-shear.md
  - research/visual_exploration/findings/VIS-071-finite-prime-vertical-flow-shared-phase-haar-law.md
  - research/visual_exploration/findings/VIS-083-gram-point-prime-phase-haar-equidistribution.md
  - research/visual_exploration/findings/VIS-084-gram-short-block-prime-phase-freezing.md
  - research/visual_exploration/findings/VIS-085-gram-local-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-086-quadratic-gram-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-087-finite-order-gram-clock-null-hierarchy.md
  - research/visual_exploration/findings/VIS-088-polynomial-sensitivity-observables-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-089-inverse-polynomial-decision-margins-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-090-consecutive-gram-superlog-prime-torus-haar.md
  - research/visual_exploration/findings/VIS-091-gram-log-lag-increment-clock-collapse.md
  - research/visual_exploration/findings/VIS-150-gram-superlog-lag-second-clock-transition.md
  - research/visual_exploration/findings/VIS-151-gram-exact-lag-shear-haar.md
  - research/visual_exploration/findings/VIS-152-gram-joint-lag-finite-difference-threshold.md
  - research/visual_exploration/findings/VIS-153-gram-critical-lag-newton-product-law.md
  - research/visual_exploration/findings/VIS-154-gram-fixed-irregular-lag-vandermonde-threshold.md
  - research/visual_exploration/findings/VIS-155-gram-irregular-critical-haar-fiber-curve.md
  - research/visual_exploration/findings/VIS-156-gram-fixed-affine-subsampling-clock-null.md
  - research/visual_exploration/findings/VIS-157-quadratic-gram-index-pairwise-haar-triple-clock.md
  - research/visual_exploration/findings/VIS-158-polynomial-gram-index-d-wise-haar-threshold.md
  - research/visual_exploration/findings/VIS-159-power-law-gram-index-ceiling-haar-threshold.md
---

# Can a zeta visual statistic leave the prime-torus information class after the full Gram-clock quotient?

## Observation

The prime-phase program has progressively removed representation and sampling effects that can look arithmetically structured without adding a new information source. `VIS-064`--`VIS-066` show that hybrid factor/residual recombinations related by an invertible shear do not create information, while the later Gram-sequence results show that an independently defined sampling clock can generate a surprisingly rich visual vocabulary on the same prime-phase data.

`VIS-083` gives full-population fixed-prime Haar behavior. `VIS-084`--`VIS-091` classify local freezing, deterministic inverse-clock arcs and finite-order corrections, growing-support collapse, and the separation between unordered long-block population and fixed local lag structure. `VIS-150`--`VIS-155` close the complete fixed-dimensional commensurate lag hierarchy: fixed equal or irregular integer-node delays are subcritical coherent, critical Haar-on-fibers over one deterministic inverse-clock curve, or supercritical Haar according to the order of the deepest finite-difference/Vandermonde character.

`VIS-156` closes fixed affine starting-index thinning. Restricting Gram indices to `a+q n` preserves fixed-prime Haar population and the complete fixed-node lag classification; fixed congruence-class sparsity is only a deterministic clock reparameterization.

`VIS-157` showed that the quadratic selector `g_(n^2)` is pairwise Haar but not three-wise Haar on fixed prime support. `VIS-158` generalized that mechanism to every fixed integer polynomial selector `P` of degree `d`: all fixed joint prime-phase views through order `d` are Haar, while `d+1` samples recover a deterministic moment-null product character.

`VIS-159` now closes the most obvious non-polynomial extension. For `k_n=floor(n^alpha)` with fixed noninteger `alpha>1`, every fixed view through order `ceil(alpha)` is Haar, while one more sample recovers the deterministic clock. Together with the integer-power case from `VIS-158`, the entire fixed power-law family has the unified threshold `ceil(alpha)`. Noninteger Piatetski-Shapiro-style sparsity therefore does not escape the prime-phase/clock information class merely by looking less algebraic.

## Research question

After quotienting the prime-torus population law, the complete fixed finite commensurate Gram-clock hierarchy, fixed affine thinning, all fixed-degree polynomial Gram-index selectors, and the complete fixed power-law family `floor(n^alpha)`, does any independently anchored or genuinely changing-complexity visual statistic expose information not already determined by the prime phases, the observation window, and deterministic sampling geometry?

The remaining routes must change a real hypothesis. Candidate escapes include selector exponent or complexity growing with height with quantitative uniformity, genuinely non-power/non-polynomial or data-dependent subsequences with their own induced null, genuinely noncommensurate real-time offsets, or an analytic coordinate such as `Z`, derivatives, zero occupancy, or nearby-zero geometry whose joint information is not determined by the prime-phase/clock state.

## Why it may matter

The visual false-positive space is now unusually constrained. The same fixed-prime data can appear as a cluster, deterministic arc, Haar population, coherent lag field, mixed Haar-times-curve critical law, irregular delay cloud, sparse residue-class sample, polynomially sparse sequence, or noninteger power-law sparse sequence with arbitrarily convincing finite-order Haar appearance. None of those appearances alone establishes a new arithmetic source.

A surviving statistic would be materially more informative because it would have to leave this deterministic information class rather than merely make a plot look more irregular, sparse, mixed, nonlinear, or high dimensional.

## Decisive test

For consecutive fixed-prime lag populations, use `VIS-150`--`VIS-151`. For every fixed equal-step `r`-lag vector use `VIS-152`--`VIS-153`; below the order-`r` threshold a top finite-difference character remains coherent, at criticality the Newton coordinates are Haar in the transverse directions over one deterministic top-difference curve, and above threshold the fixed joint characters cancel.

For every fixed distinct integer lag-ratio set use `VIS-154`--`VIS-155`; changing a finite commensurate node geometry only changes the primitive Vandermonde character and deterministic winding constants. For fixed arithmetic-progression starting indices use `VIS-156`; fixed stride is only a sampled-clock reparameterization.

For every fixed integer polynomial selector `P` of degree `d`, use `VIS-158`: every fixed `r<=d` prime-phase sample is jointly Haar, but any `d+1` distinct fixed offsets have a coherent order-`d` moment-null product character. `VIS-157` is the `d=2` specialization.

For every fixed power selector `k_n=floor(n^alpha)`, use `VIS-158` when `alpha` is an integer and `VIS-159` when it is not. The largest fixed sample order with Haar appearance is `ceil(alpha)`; one additional sample exposes a deterministic moment-null clock character. Do not treat noninteger power-law sparsity or finite-order decorrelation under it as source evidence.

A surviving sampling route must therefore change the fixed-complexity power-law hypothesis and derive its own null before interpreting visual randomness. For exponent or selector complexity growing with height, obtain quantitative uniformity in the changing derivative/character class. For a genuinely non-power, non-polynomial, or data-dependent selector, derive the induced sampled-clock law instead of declaring independence from index-set irregularity. For an added analytic coordinate, test whether its joint law contains information not measurable from the prime-phase/clock state.

Kill a route if its apparent signal is reproduced by the corresponding deterministic point/curve/Newton/Vandermonde/polynomial/power-clock law, disappears after an explicit invertible clock quotient, or depends only on a fixed finite transformation of the same prime-phase state.

## Evidence boundary

`VIS-150`--`VIS-155` classify fixed-dimensional prime-phase lag populations over consecutive Gram indices across subcritical, critical, and supercritical scales. `VIS-156` extends the control to fixed affine index subsequences. `VIS-157` treats the quadratic selector explicitly, `VIS-158` closes every fixed polynomial degree, and `VIS-159` closes every fixed noninteger power selector `floor(n^alpha)`, `alpha>1`. Together the last two give a `ceil(alpha)` sample-order threshold for the full fixed power family.

These results do not provide uniformity when delay dimension, polynomial degree, selector exponent, selector coefficients, node geometry, sampling stride, prime support, Fourier complexity, or character coefficients grow with height. They do not classify arbitrary non-power/non-polynomial/data-dependent subsequences or genuinely noncommensurate real-time offsets.

They also do not classify any joint law involving zeta values, Hardy `Z`, derivatives, zero occupancy, or nearby-zero coordinates. The Gram-clock hierarchy is a sampling control, not a zeta approximation, stochastic-mixing theorem, stronger zeta criterion, or RH consequence.

## Research disposition

Accepted in further narrowed form. Fixed finite commensurate lag geometry, fixed affine thinning, every fixed-degree polynomial Gram-index selector, and every fixed power-law selector `floor(n^alpha)`, `alpha>1`, are closed as positive information escapes on fixed prime support. Deterministic sampling geometry can manufacture Haar appearance through the exact fixed order `ceil(alpha)` while retaining a clock relation one order higher. Continue only through a genuinely hypothesis-changing route such as changing selector complexity with quantitative uniformity, a separately derived non-power/data-dependent or noncommensurate sampling law, or an independently informative analytic source.