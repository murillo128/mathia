# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-sensitive low-frequency statistic that survives moment-null normalization

**Linked intuitions:** `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-150 show that support-safe companions enter a shrinking low-frequency channel where finite signed moment-null packets can erase finite-order response. Decisive evidence must come from a source-side lower-order term that survives the matched null, not from a visually striking residual after universal control subtraction.

## Treat every fixed finite-order Gram-phase mixing test as a deterministic clock control

**Linked intuition:** `MI-008-fixed-dimensional-gram-lags-are-a-newton-clock-null`.

VIS-150--VIS-160 show that deterministic selectors can mimic arbitrarily high fixed mixing orders. A useful theorem needs a predeclared joint complexity/height law or source information outside the sampled phase-clock state.

## Calibrate critical dependence on a representation-matched monotone object

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-021-fixed-count-pair-calibration-removes-poissonization-noise`.

VIS-227--VIS-236 separate collision baselines, conditional sigma-fields and the monotone support of actual prime-coordinate cells. In that representation, exact first-order transition conditioning is degenerate: the labels are nondecreasing and the apparent lag-two escape reduces to an occupancy functional.

VIS-237 supplies a representation-faithful quotient instead of manufacturing label freedom. Randomizing the grid origin and averaging the same-cell collision count gives the exact triangular pair functional

`sum_(a<b) (1-|x_b-x_a|/ell)_+`.

Origin averaging therefore removes nuisance grid phase while preserving the ordered point geometry. It does **not** create a new stochastic null and does not by itself reveal prime specificity; it converts the cell statistic into a compactly supported two-point gap observable.

VIS-238 then removes a second nuisance that belongs to the calibration law rather than the representation. At critical occupancy `kappa=m ell/L=Theta(1)`, the fixed-count uniform ordered-point model has tent-pair variance `m kappa/3+O(1)`, whereas an unconditioned Poisson model adds a leading `m kappa^2` channel coming only from fluctuations of the total count. Because the observed prime-coordinate sample already fixes its count, that Poissonization variance is artificial for this statistic.

The live question is now narrower: after quotienting grid origin and conditioning on the observed count, freeze an independently justified ordered-point/gap baseline that captures any remaining nonuniform intensity or short-gap structure, then ask whether the tent-kernel pair statistic or a nearby source-sensitive statistic has a residual that couples to the signed prime-phase kernel. Origin robustness and excess variance against an unconditioned Poisson process are no longer evidence.

## Keep nuisance quotienting, count calibration, stochastic law, sigma-field and arithmetic residual separate

A valid confirmation test must distinguish the operations being performed. Removing grid-origin phase is an exact representation quotient; fixing the observed sample count removes Poissonization noise; choosing the remaining ordered-point/gap law is a modeling step; conditioning can still erase the statistic; and only a residual against the frozen representation-matched baseline can be interpreted as source-sensitive.

For the prime-coordinate critical scale, future visual statistics should therefore be expressed directly on monotone geometric data—ordered gaps, counts, within-cell positions or pair kernels—and audited against a fixed-count, representation-faithful null before any arithmetic interpretation.