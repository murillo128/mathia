# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-251 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance, then establish the exact conditional benchmark and irreducible random-scan three-coordinate heat-bath chain. VIS-252--VIS-255 give exact linear contrast modes and nonlinear slowdown certificates from conditional fiber variance and the second dissipation moment. The operational question remains to reproduce those exact benchmarks in a frozen implementation and test them on the cut-averaged tent statistic before interpreting any apparent prime residual.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The log-product quotient and current heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes need their own sufficient coordinates or independently frozen nuisance parameters.

## Treat low-frequency cancellation as an exact dual-conditioning and theorem-accuracy problem

**Linked intuitions:** `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`, `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning`.

VIS-145--VIS-147 show that for smooth finite-window corrections, cancelling successive polynomial moments moves the response to higher Taylor order while raising the total-variation/conditioning bill. VIS-256 shows why polynomial moments alone are the wrong coordinates at the sine-kernel/CUE support edge: the limiting centered profile has the nonanalytic cusp `min(|q|,1)`.

VIS-257--VIS-258 solve the first two cusp-adapted stages sharply. After cancelling mass and the `|q|` cusp, unit quadratic signal costs exactly `8b^(-2)` variation. Cancelling the quadratic channel as well makes unit quartic signal cost `E_*^(-1)b^(-4)`, with `E_*=0.06346155...`.

VIS-259 closes the **entire generic cancellation ladder**. After zero mass, exact cusp cancellation and the preceding even moments, the sharp capacity for the first retained `2m`-th moment is

`|m_(2m)(nu)| <= E_m b^(2m) ||nu||_TV`,

where `E_m` is exactly the uniform-approximation distance from `t^(2m)` to `span{1,t,t^2,t^4,...,t^(2m-2)}` on `[0,1]`. Hahn--Banach/Riesz duality proves that the constant is attained over all finite signed measures. Hence the optimal unit-carrier conditioning cost is exactly `E_m^(-1)b^(-2m)` at every order.

VIS-260 now attaches a real theorem-accuracy scale to that conditioning bill. Under RH, Rodgers' fixed-margin smooth pair-correlation theorem gives a uniform error `O_delta(T^(-delta))` on `|alpha|<1-epsilon` for fixed `epsilon`, fixed smooth weight and every `delta<epsilon/2`. Applying an optimal cusp-adapted order-`2m` packet multiplies that error by exactly the `b^(-2m)` total-variation cost, so the certified transfer error is

`O(T^(-delta) E_m^(-1)b^(-2m))`.

For `b=T^(-beta)`, the published theorem can therefore pay the packet conditioning precisely when `beta<epsilon/(4m)`: quadratic packets admit `beta<epsilon/4`, quartic packets `beta<epsilon/8`. This is a genuine positive calibration inside a **fixed** support margin. It does not extend to `epsilon_T -> 0`, a varying weight, or the four-level covariance needed by the original edge--edge statistic.

This removes both higher packet-shape optimization and vague claims that a polynomial theorem error is automatically enough. A `2m`-th-order route is interesting only after the actual zeta-minus-null destination supplies a nonzero coefficient `A_(2m)` and the available theorem error, after multiplication by `E_m^(-1)b^(-2m)`, is asymptotically smaller than that carrier.

The live support-edge fork is therefore source/theorem-side rather than packet-side. For a fixed-margin smooth pair statistic, compute the first nonzero Taylor coefficient of the explicit Bogomolny--Keating-minus-matched-null prediction after the declared cusp cancellations and compare it with the VIS-260 transfer gate. For the moving edge, separately prove a theorem uniform in the shrinking support margin and any changing window; for the original cross-window statistic, separately supply the missing four-level covariance law. None of those can be inferred from Rodgers' fixed-test result.