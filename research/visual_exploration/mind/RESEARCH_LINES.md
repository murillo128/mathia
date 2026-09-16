# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-251 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance, then establish the exact conditional benchmark and irreducible random-scan three-coordinate heat-bath chain. VIS-252--VIS-255 give exact linear contrast modes and nonlinear slowdown certificates from conditional fiber variance and the second dissipation moment. The operational question remains to reproduce those exact benchmarks in a frozen implementation and test them on the cut-averaged tent statistic before interpreting any apparent prime residual.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The log-product quotient and current heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes need their own sufficient coordinates or independently frozen nuisance parameters.

## Treat low-frequency cancellation as an exact dual-conditioning problem

**Linked intuition:** `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`.

VIS-145--VIS-147 show that for smooth finite-window corrections, cancelling successive polynomial moments moves the response to higher Taylor order while raising the total-variation/conditioning bill. VIS-256 shows why polynomial moments alone are the wrong coordinates at the sine-kernel/CUE support edge: the limiting centered profile has the nonanalytic cusp `min(|q|,1)`.

VIS-257--VIS-258 solve the first two cusp-adapted stages sharply. After cancelling mass and the `|q|` cusp, unit quadratic signal costs exactly `8b^(-2)` variation. Cancelling the quadratic channel as well makes unit quartic signal cost `E_*^(-1)b^(-4)`, with `E_*=0.06346155...`.

VIS-259 closes the **entire generic cancellation ladder**. After zero mass, exact cusp cancellation and the preceding even moments, the sharp capacity for the first retained `2m`-th moment is

`|m_(2m)(nu)| <= E_m b^(2m) ||nu||_TV`,

where `E_m` is exactly the uniform-approximation distance from `t^(2m)` to `span{1,t,t^2,t^4,...,t^(2m-2)}` on `[0,1]`. Hahn--Banach/Riesz duality proves that the constant is attained over all finite signed measures. Hence the optimal unit-carrier conditioning cost is exactly `E_m^(-1)b^(-2m)` at every order.

This removes higher packet-shape optimization as a generic research direction. Computing `E_3,E_4,...` or adding more universal moment cancellations cannot create a free source channel. A `2m`-th-order route is interesting only after the actual zeta-minus-null destination supplies a nonzero coefficient `A_(2m)` and the transfer/covariance error beats the matching scale `E_m |A_(2m)| b^(2m)`.

The live support-edge fork is therefore source-side rather than packet-side: retain the quadratic carrier and prove/calibrate error below the sharp quadratic scale, or cancel it only if a genuine quartic source coefficient and `o(b^4)`-level error/covariance theorem exist. Higher orders should wait for evidence that the source actually contains the corresponding carrier.