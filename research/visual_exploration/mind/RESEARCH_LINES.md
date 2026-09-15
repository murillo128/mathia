# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders. A useful theorem needs a predeclared joint complexity/height law or source information outside the sampled phase-clock state.

## Calibrate critical dependence after quotienting endpoint phase explicitly

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-023-dirichlet-gap-controls-separate-dependence-from-count-and-intensity`.

VIS-227--VIS-236 separate collision baselines, conditional sigma-fields and the monotone support of actual prime-coordinate cells. VIS-237 then gives a representation-faithful grid-origin quotient: averaging the same-cell collision count over origin is exactly a triangular pair-gap functional. VIS-238 removes Poisson count noise by calibrating the observed fixed-count geometry, and VIS-239 removes an independently specified one-point intensity through cumulative-intensity coordinates while showing that same-sample empirical-CDF flattening destroys the spacing geometry.

VIS-240 supplies a representation-matched dependence family. Symmetric Dirichlet cyclic gaps with an independent uniform rotation keep the point count exactly `m`, keep every one-point marginal exactly uniform, and remain on the same monotone ordered-point support after cutting. The parameter `alpha` changes short-gap dependence without changing those nuisance variables; `alpha=1` is exactly the iid-uniform circular-spacing model. The tent statistic has an explicit finite-sample mean under this family.

VIS-241 now separates the still-missing variance calibration into two exact channels. For a fixed circular configuration and a uniform cut phase `Theta`, the post-cut tent statistic can be written as a weighted arc-coverage count. Its cut average is the intrinsic circular pair functional

`bar T=sum_(i<j) (1-delta_ij/ell)_+ (1-delta_ij/L)`,

and its conditional cut variance `V_cut` is an explicit quadratic form in the minor-arc overlap lengths. Under a random gap configuration `G`,

`Var_(G,Theta)(T)=Var_G(bar T)+E_G[V_cut]`.

Thus random-cut endpoint phase and dependent circular gap geometry are not one undifferentiated null fluctuation. **The endpoint convention must be frozen before confirmation.** If the interval endpoints are nuisance, use `bar T` and the remaining mathematical target is `Var_G(bar T)` or a stronger finite-sample law under a predeclared `alpha`. If physical endpoints are part of the signal, retain the exact additional `E_G[V_cut]` channel and calibrate both pieces.

The live dependence question is therefore narrower than after VIS-240: derive or independently validate the fluctuation law of the intrinsic circular pair functional under fixed external `alpha`, with the cut-phase contribution included only when the endpoint model requires it. Only then test whether the prime configuration has a residual outside the representation-matched dependence envelope and translate any survivor back through the signed prime-phase kernel. Fitting `alpha` or the endpoint convention on the same confirmation statistic would merely move the conditioning problem into the null.

## Keep nuisance quotienting, count calibration, marginal normalization, endpoint convention, dependence law and arithmetic residual separate

**Linked intuitions:** `MI-022-cumulative-intensity-normalization-removes-a-specified-marginal-but-in-sample-flattening-erases-the-geometry`, `MI-023-dirichlet-gap-controls-separate-dependence-from-count-and-intensity`.

A valid confirmation test must distinguish the operations being performed. Removing grid-origin phase is one exact representation quotient; fixing the observed sample count removes Poissonization noise; transforming by an independently specified cumulative intensity removes a one-point marginal; symmetric Dirichlet gaps vary dependence at fixed count and marginal; and VIS-241 shows that opening a stationary circle into a finite interval introduces a separate endpoint-phase variance channel.

If endpoint phase is a nuisance, averaging over it is another exact quotient and leaves the intrinsic circular statistic `bar T`. If endpoints are mathematically distinguished, averaging would erase real structure and `V_cut` belongs to the null. This choice is semantic, not a numerical tuning parameter.

Only a residual surviving the frozen count, intensity, endpoint and dependence controls can be interpreted as a candidate source signal, and even then RH relevance still requires a signed prime-phase bridge.