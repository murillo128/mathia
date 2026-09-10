# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the cross-height covariance law needed to average a support-edge residual

**Linked intuitions:** `MI-001-visual-residuals-must-survive-exact-coordinate-controls`, `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`.

VIS-130--VIS-132 fix the bounded-source mean convention and remove the realized diagonal common mode exactly. VIS-133--VIS-135 then show that the remaining fixed-window off-diagonal statistic has an order-one normalized covariance and a Gaussian terminal packet with a strictly positive variance floor; a single matched CUE window does not self-average to the `1/L` arithmetic scale.

VIS-136 identifies the missing currency: the covariance tail across source windows determines how many windows are required to average the residual. VIS-137 shows that translated fixed-ratio CUE windows provide only `O(1)` disjoint samples on one circle, so they cannot manufacture a growing independent pool. VIS-138 proves that exact single-window CUE marginals do not determine this cross-window averaging law.

VIS-139 sharpens the information requirement. For disjoint quadratic pair statistics, cross-window covariance is a four-level functional after lower-order contractions vanish; even exact one-, two-, and three-level marginals do not determine it in general. The live theorem must therefore provide a zeta-side four-level/structural-closure estimate or a direct cross-height mixing bound under the actual moving window geometry.

## Treat one-window CUE calibration and pair correlation as completed controls

The finite-CUE mean and one-window stochastic null can be calibrated exactly, but neither pair correlation nor any collection of lower-order single-window marginals determines the cross-height averaging exponent. Arithmetic interpretation begins only after the required multi-window dependence law is proved and finite-height transfer is controlled.