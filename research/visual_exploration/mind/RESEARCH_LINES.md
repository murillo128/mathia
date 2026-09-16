# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-251 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance, then establish the exact conditional benchmark and irreducible random-scan three-coordinate heat-bath chain. VIS-252--VIS-253 give exact ordinary and logarithmic contrast eigenmodes with integrated autocorrelation time `m-2` triple updates.

VIS-254--VIS-255 provide exact nonlinear slowdown certificates. The averaged conditional fiber variance gives the Dirichlet ratio `delta_f` and `tau_int(f)>=2/delta_f-1`; the second dissipation moment `eta_f` gives the sharper two-moment lower bound `B2(delta_f,eta_f)`. The operational question remains to reproduce the exact benchmarks in a frozen implementation and test these moment gates on the cut-averaged tent statistic before interpreting any apparent prime residual. Failure of both gates does not certify fast mixing and still requires separated-start/long-lag checks.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The log-product quotient and current heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes need their own sufficient coordinates or independently frozen nuisance parameters.

## Treat low-frequency suppression as a kernel-regularity problem, not a moment-count problem

**Linked intuition:** `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-145--VIS-147 show that for smooth finite-window corrections, cancelling successive polynomial moments moves the response to higher Taylor order but simultaneously raises the total-variation/conditioning bill; packet rescaling cannot improve the resulting signal-to-error ratio.

VIS-256 adds a different obstruction at the sine-kernel/CUE support edge. The limiting centered profile has the nonanalytic cusp `T(q)=min(|q|,1)`. For every fixed cancellation order there is a bounded-normalization symmetric signed packet on a shrinking interval that annihilates all ordinary moments through that order yet pairs with the cusp at exactly `Theta(b)`. Thus zero mass, symmetry and any fixed finite set of polynomial vanishing moments do **not** force the universal `O(b)` low-frequency null to become `o(b)`.

A stronger support-safe companion must therefore control a cusp-adapted quantity such as the `|q|` pairing, prove a quantitatively uniform finite-window smoothing scale that survives the source-window limit, or use a source-specific identity that changes the destination observable. Growing moment order remains a separate conditioning problem. The older deterministic selector-clock and low-frequency matched controls remain relevant: visually distinctive structure is not evidence until it survives the exact quotient and is consumed by a source-sensitive destination.
