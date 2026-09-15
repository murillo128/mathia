# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders. A useful theorem needs a predeclared joint complexity/height law or source information outside the sampled phase-clock state.

## Calibrate critical dependence on a representation-matched monotone object

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-023-dirichlet-gap-controls-separate-dependence-from-count-and-intensity`.

VIS-227--VIS-236 separate collision baselines, conditional sigma-fields and the monotone support of actual prime-coordinate cells. In that representation, exact first-order transition conditioning is degenerate: the labels are nondecreasing and the apparent lag-two escape reduces to an occupancy functional.

VIS-237 supplies a representation-faithful quotient instead of manufacturing label freedom. Randomizing the grid origin and averaging the same-cell collision count gives the exact triangular pair functional

`sum_(a<b) (1-|x_b-x_a|/ell)_+`.

VIS-238 removes Poisson count noise by calibrating the observed fixed-count geometry directly. VIS-239 then removes any **independently specified** one-point intensity through cumulative-intensity coordinates, while showing that same-sample empirical-CDF flattening is degenerate because it replaces the geometry by a deterministic rank lattice.

VIS-240 now supplies the missing first dependence family. Symmetric Dirichlet cyclic gaps with an independent uniform rotation keep the point count exactly `m`, keep every one-point marginal exactly uniform, and after cutting/sorting remain on the same monotone ordered-point support. The parameter `alpha` changes short-gap dependence without changing those nuisance variables: `alpha=1` is exactly the iid-uniform circular-spacing model, `alpha>1` regularizes gaps and `alpha<1` clusters them.

For the triangular tent statistic, the finite-sample mean is explicit through beta aggregation of consecutive Dirichlet gaps. This makes the iid-uniform center one point in a broader **fixed-count, uniform-intensity, representation-matched dependence null** rather than the final baseline.

The live calibration question is now quantitative rather than conceptual: with `alpha` fixed independently of confirmation data, derive or independently validate the variance/covariance or full finite-sample law of the tent statistic under this family. Only then test whether the prime configuration has a residual outside the dependence envelope and translate any survivor back through the signed prime-phase kernel. Fitting `alpha` on the same statistic without propagating estimation uncertainty would merely move the conditioning problem into the null.

## Keep nuisance quotienting, count calibration, marginal normalization, dependence law and arithmetic residual separate

**Linked intuitions:** `MI-022-cumulative-intensity-normalization-removes-a-specified-marginal-but-in-sample-flattening-erases-the-geometry`, `MI-023-dirichlet-gap-controls-separate-dependence-from-count-and-intensity`.

A valid confirmation test must distinguish the operations being performed. Removing grid-origin phase is an exact representation quotient; fixing the observed sample count removes Poissonization noise; transforming by an independently specified cumulative intensity removes a one-point marginal; choosing `alpha` or another gap law is a dependence model; and conditioning can still erase the statistic.

VIS-240 is useful precisely because it changes dependence while preserving the preceding quotients. It does not model prime gaps by assertion and its exact mean is not yet a complete null. Future visual statistics should therefore be tested against frozen representation-faithful dependence families, with parameter uncertainty accounted for whenever parameters are learned. Only a residual surviving count, intensity and dependence controls can be interpreted as a candidate source signal, and even then RH relevance still requires a signed prime-phase bridge.