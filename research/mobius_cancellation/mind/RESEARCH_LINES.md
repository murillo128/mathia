# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exclude one of three rigid shell escapes: near-injectivity, affine obstruction, or exponentially sparse non-affine occupancy

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`, `MI-022-positive-shell-envelopes-erase-the-phase-cancellation-needed-below-the-blind-atom`, `MI-023-negative-witness-collapse-trades-rowwise-simplicity-for-source-depth`, `MI-024-arithmetic-image-blind-exclusion-is-directional-leverage`.

MC-281--MC-284 reduce blind exclusion to arithmetic-image Christoffel leverage and show that moderate-conductor shadows can already realize the full Boolean cube. MC-285 kills the even-weight branch unless occupancy is nearly injective. MC-286 identifies the odd affine obstruction exactly.

MC-288 sharpens MC-287's half-cube alternative. In the collision-rich regime `N-K>=t-1`, absence of an odd target row forces odd girth greater than `t`. Geelen's sharp finite-geometric theorem then implies either

`0 notin aff(S)`

or

`K/2^r <= (t+2)/2^(t+1)`,

where `r=dim span(S)`. Combining this with the collision-poor case gives the live trichotomy

`N-K<=t-2`  or  `0 notin aff(S)`  or  `K/2^r<=(t+2)/2^(t+1)`.

At `t~(log log y)/log 2`, the non-affine density is at most `(log y)^(-1+o(1))`. The arithmetic theorem no longer needs full Boolean universality or even a half-cube lower bound. It can instead rule out the exact constant-negative product-character branch, prove that the actual Legendre image cannot become this sparse in its own span, or show that near-injective encoding is incompatible with the admissible conductor/support scale.

## Keep parity, affine obstruction, rank-relative density, collision excess and conductor separate

Even weights are killed by equal-cell pairing. Odd weights require an odd nucleus plus pair capacity. MC-288 separates the collision-rich odd branch into a one-character affine obstruction and an exponentially sparse non-affine support; neither is interchangeable with large ambient dimension or large conductor.

A theorem improving occupancy must state whether its density is measured in the ambient cube or the actual rank-`r` span. A theorem killing the affine branch must genuinely exclude the constant-negative generated character rather than merely show many patterns occur.

## Preserve source-depth and matched controls as falsifiers

The Geelen threshold is sharp for arbitrary binary matroids, so further progress must use arithmetic properties of the Legendre shell rather than generic finite geometry. Separated-prime controls, moderate-conductor universality and the actual localized shell remain complementary tests for whether a proposed inverse is using source-native collective information.
