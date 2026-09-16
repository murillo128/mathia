# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-251 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance, then establish the exact conditional benchmark and irreducible random-scan three-coordinate heat-bath chain. VIS-252--VIS-253 give exact ordinary and logarithmic contrast eigenmodes with integrated autocorrelation time `m-2` triple updates.

VIS-254--VIS-255 provide exact nonlinear slowdown certificates. The averaged conditional fiber variance gives the Dirichlet ratio `delta_f` and `tau_int(f)>=2/delta_f-1`; the second dissipation moment `eta_f` gives the sharper two-moment lower bound `B2(delta_f,eta_f)`. The operational question remains to reproduce the exact benchmarks in a frozen implementation and test these moment gates on the cut-averaged tent statistic before interpreting any apparent prime residual. Failure of both gates does not certify fast mixing and still requires separated-start/long-lag checks.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The log-product quotient and current heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes need their own sufficient coordinates or independently frozen nuisance parameters.

## Treat low-frequency suppression as a destination-regularity and conditioning problem

**Linked intuition:** `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-145--VIS-147 show that for smooth finite-window corrections, cancelling successive polynomial moments moves the response to higher Taylor order but simultaneously raises the total-variation/conditioning bill; packet rescaling cannot improve the resulting signal-to-error ratio.

VIS-256 shows why finite polynomial moments are the wrong coordinates at the sine-kernel/CUE support edge. The limiting centered profile has the nonanalytic cusp `T(q)=min(|q|,1)`, and bounded-normalization shrinking packets can annihilate any fixed finite polynomial jet while retaining an exact `Theta(b)` cusp response.

VIS-257 supplies the natural cusp-adapted escape and prices it sharply. A symmetric signed packet on `[-b,b]` with zero mass and zero `|q|` pairing satisfies

`|m_2(nu)| <= (b^2/8)||nu||_TV`,

with equality for the explicit three-radius packet `delta_0-2 sigma_(b/2)+sigma_b`. Thus normalizing the quadratic moment to order one costs at least `8/b^2` total variation. The limiting cusp is killed exactly, but the finite-window CUE correction has a quadratic channel of size `Theta(mu_2 b^2)`; under `bM->0` that channel remains the correct null-scale contribution.

The low-frequency design fork is therefore explicit. Either retain nonzero `m_2` and calibrate both source and finite-window null to `o(b^2)` after the sharp `b^(-2)` conditioning amplification, or also cancel `m_2` and move to a quartic/higher-order gate with its own conditioning bill. Merely saying “cusp-adapted” no longer removes the quantitative problem.

The older deterministic selector-clock and low-frequency matched controls remain relevant: visually distinctive structure is not evidence until it survives the exact quotient and is consumed by a source-sensitive destination.
