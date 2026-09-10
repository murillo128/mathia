# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Test arithmetic selectivity of moment-null shrinking companions at the support edge

**Linked intuitions:** `MI-001-visual-residuals-must-survive-exact-coordinate-controls`, `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`.

VIS-130--VIS-141 establish the finite-window CUE null, the nondegenerate one-window fluctuation floor, the genuinely four-level nature of disjoint-window covariance, and the Rudnick--Sarnak support obstruction to edge-edge covariance. If one pair factor approaches the Montgomery edge, a support-safe independent companion must collapse toward zero frequency.

VIS-142--VIS-144 price that collapse instead of treating it as a harmless DC mode. A bounded-normalization companion has centered finite-CUE mean at most `O(b)` uniformly, and in the finite-window regime `Mb->0` the response is genuinely `Theta(M b^2)` for a single mode. Keeping that deterministic scale macroscopic therefore requires growing normalization, which must also amplify transfer error and variance. However, VIS-144 identifies a sharper redesign: a signed packet with vanishing second frequency moment cancels the universal quadratic CUE mean while preserving the restricted support budget.

The decisive local question is now whether the zeta-specific lower-order contribution has a component **outside the same universal quadratic moment functional**. Derive the arithmetic low-frequency expansion for the frozen observable and test a moment-null packet while controlling its total variation, stochastic variance, finite-height transfer, and theorem remainder. If the arithmetic term shares the same leading moment, the redesign dies; if it survives at a cheaper order than the amplified null/error, it gives a concrete restricted-support escape. Direct cross-height covariance or genuinely wider-support four-level information remain independent routes.

## Treat one-window calibration, positive shrinking packets, and null-mean cancellation as separate gates

Support admissibility does not imply useful amplitude, and canceling the deterministic CUE mean does not imply arithmetic selectivity or variance reduction. Any support-safe replacement must specify the packet normalization and finite-window regime, prove that the arithmetic residual survives the imposed moment cancellation, and carry the same normalization through all transfer and covariance errors.
