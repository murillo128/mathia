# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the post-calibration growing-window quartic source moment

**Linked intuitions:** `MI-001-visual-residuals-must-survive-exact-coordinate-controls`, `MI-006-nonlocal-information-and-macroscopic-amplitude-are-separate-gates`, `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-130--VIS-144 reduce the restricted-support edge companion to a shrinking low-frequency packet and propose vanishing second moment as a way to cancel the universal finite-CUE quadratic response. VIS-145 closes the hoped-for quadratic selectivity: the same moment condition annihilates the quadratic response of **every** smooth finite-window source correction represented through the same centered-cosine transform. Any surviving deterministic distinction begins at quartic order or through a failure of that common representation/uniformity.

VIS-146 prices the resulting normalization exactly. A packet supported in `[-b,b]` has `|m_{2j}| <= b^(2j)||nu||_TV`; after `m_2=0`, unit quartic response costs at least `b^-4` total variation. Because theorem/transfer errors bounded in sup norm are amplified by the same variation, packet rescaling cannot improve the robust signal/error ratio. A quartic carrier requires the underlying error to beat `|A_4| b^4` before optimization matters.

VIS-147 shows that the familiar finite-height pair-correlation corrections do not yet provide `A_4`. The displayed `rho_bar^-2` and `rho_bar^-3` terms are absorbed by the standard effective finite-CUE size/scale calibration, while the actual observable integrates over a source window of unfolded radius `Theta(L)`. Fixed-spacing `O(rho_bar^-4)` control gives no fourth-moment bound on that growing window.

The live theorem is therefore source-side, not packet-design: derive the zeta-minus-calibrated-finite-CUE residual in the exact frozen bounded-source representation and control its weighted fourth moment together with an error envelope strong enough for the `VIS-146` gate. Only if that deterministic quartic channel survives should variance and four-level covariance become the next bottlenecks.

## Treat moment cancellation, rescaling, and effective-CUE lower-order terms as controls

Second-moment cancellation removes all common quadratic finite-window response, not just the null. Increasing packet weights amplifies total-variation-linear uncertainty at the same rate as the desired moment. And the standard first finite-height corrections are calibration directions rather than an already-isolated arithmetic residual. A viable companion must expose information after all three controls.
