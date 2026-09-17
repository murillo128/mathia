# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-251 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance, then establish the exact conditional benchmark and irreducible random-scan three-coordinate heat-bath chain. VIS-252--VIS-255 give exact linear contrast modes and nonlinear slowdown certificates from conditional fiber variance and the second dissipation moment. The operational question remains to reproduce those exact benchmarks in a frozen implementation and test them on the cut-averaged tent statistic before interpreting any apparent prime residual.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The log-product quotient and current heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes need their own sufficient coordinates or independently frozen nuisance parameters.

## Treat low-frequency cancellation as an exact source-moment, conditioning and source-selectivity problem

**Linked intuitions:** `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`, `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning`, `MI-030-low-frequency-arithmetic-jets-are-physical-moments`.

VIS-145--VIS-147 show that cancelling successive polynomial moments raises both Taylor order and total-variation cost. VIS-256 identifies the sine-kernel/CUE support-edge cusp `min(|q|,1)`, so ordinary polynomial moment cancellation is not the right first coordinate.

VIS-257--VIS-259 solve the cusp-adapted packet ladder sharply. After cancelling mass, `|q|` and preceding even moments, unit `2m`-th signal costs exactly `E_m^(-1)b^(-2m)` in total variation, where `E_m` is the uniform-approximation distance of `t^(2m)` from the lower nuisance span on `[0,1]`.

VIS-260 attaches a rigorous transfer scale. Under RH, Rodgers' fixed-margin smooth pair-correlation theorem gives uniform error `O_delta(T^(-delta))` for every fixed `delta<epsilon/2`. Packetization multiplies this by the sharp conditioning bill, so for `b=T^(-beta)` the theorem can pay an order-`2m` packet only in the fixed-margin regime `beta<epsilon/(4m)`.

VIS-261 identifies the source-side Taylor dictionary: if `D_T(u)` is the physical-space Bogomolny--Keating-minus-matched-GUE kernel and `R_T(alpha)` its frequency transform, then `R_T^(2j)(0)=(-1)^j log(T)^(2j) int u^(2j)D_T(u)du`. VIS-262 evaluates the fixed-margin diagonal reduction far enough to show that every fixed even moment converges to an explicit `t`-independent functional `C_(2m)(omega)=int u^(2m)omega(u)F(u)du`, and some admissible fixed real even band-limited weights have `C_2(omega)!=0`.

VIS-263 is the necessary adversarial correction to the interpretation of that nonzero carrier. It constructs an explicit normalized admissible weight whose Fourier support lies strictly below the first nonzero prime frequency and proves exactly

`C_2(omega_*)=1/(2 pi^2)`.

For this weight every nonconstant zeta/`B` Dirichlet frequency is annihilated; the entire quadratic coefficient comes from the zero-frequency pole-compensating term. The associated sharp quadratic packet still has the certified main difference `-(1/(4 pi^2))(log T)^2+o((log T)^2)` in the fixed-margin RH-conditional transfer regime. Thus **a nonzero quadratic carrier in Rodgers' admissible class is not by itself evidence of prime-frequency arithmetic selectivity**.

The existence and explicit-calibration question is therefore closed, but the source-selectivity question is sharper. For a frozen weight that is mathematically faithful to the intended support-edge observable, decompose the quadratic coefficient into its zero-frequency/pole-compensation part and its nonconstant prime-frequency part, then show that a residual source-specific contribution survives with the required conditioning and theorem-error budget. This is already the mathematical core of the accepted `CLUE-zeta-montgomery-support-edge-arithmetic-residual`; VIS-263 supplies a new exact matched-background control for that question rather than a reason to create a duplicate clue.

The moving support edge remains separate because it needs theorem uniformity as `epsilon_T->0` or the weight/window changes. The original edge--edge statistic remains further away because it also needs a four-level covariance law.