# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-251 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance, then establish the exact conditional benchmark and irreducible random-scan three-coordinate heat-bath chain. VIS-252--VIS-255 give exact linear contrast modes and nonlinear slowdown certificates from conditional fiber variance and the second dissipation moment. The operational question remains to reproduce those exact benchmarks in a frozen implementation and test them on the cut-averaged tent statistic before interpreting any apparent prime residual.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The log-product quotient and current heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes need their own sufficient coordinates or independently frozen nuisance parameters.

## Treat low-frequency cancellation as an exact source-moment, conditioning and theorem-accuracy problem

**Linked intuitions:** `MI-007-moment-null-packets-pay-an-order-matched-variation-gate`, `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning`, `MI-030-low-frequency-arithmetic-jets-are-physical-moments`.

VIS-145--VIS-147 show that cancelling successive polynomial moments raises both Taylor order and total-variation cost. VIS-256 identifies the sine-kernel/CUE support-edge cusp `min(|q|,1)`, so ordinary polynomial moment cancellation is not the right first coordinate.

VIS-257--VIS-259 solve the cusp-adapted packet ladder sharply. After cancelling mass, `|q|` and preceding even moments, unit `2m`-th signal costs exactly `E_m^(-1)b^(-2m)` in total variation, where `E_m` is the uniform-approximation distance of `t^(2m)` from the lower nuisance span on `[0,1]`.

VIS-260 attaches a rigorous transfer scale. Under RH, Rodgers' fixed-margin smooth pair-correlation theorem gives uniform error `O_delta(T^(-delta))` for every fixed `delta<epsilon/2`. Packetization multiplies this by the sharp conditioning bill, so for `b=T^(-beta)` the theorem can pay an order-`2m` packet only in the fixed-margin regime `beta<epsilon/(4m)`.

VIS-261 identifies the source carrier: if `D_T(u)` is the physical-space Bogomolny--Keating-minus-matched-GUE kernel and `R_T(alpha)` its frequency transform, then `R_T^(2j)(0)=(-1)^j log(T)^(2j) int u^(2j)D_T(u)du`. VIS-262 now evaluates the fixed-margin source side far enough to cross the first nonzero-carrier gate. Rodgers' diagonal reduction makes every fixed even moment converge to an explicit `t`-independent functional `C_(2m)(omega)=int u^(2m) omega(u)F(u)du`, and because `F` is not identically zero there exist fixed admissible real even band-limited weights with `C_2(omega)!=0`.

For such a frozen weight the sharp quadratic cusp packet has main term `-(C_2(omega)/2)(log T)^2`; its Taylor remainder is `O(b^2(log T)^4)` and the RH-conditional Rodgers transfer contributes `O(T^(-delta)b^(-2))`. Choosing `b=T^(-beta)` with `0<2beta<delta<epsilon/2` makes both errors lower order. Thus the fixed-margin smooth-test class contains a rigorously calibrated nonzero quadratic arithmetic carrier; there is no universal need to climb to `M_4`.

The next fixed-margin task is now narrower: choose and persist one explicit application weight, compute or bound its concrete `C_2(omega)` from the displayed Rodgers kernel, and establish whether that same weight has a mathematically faithful dictionary to the original support-edge observable. The moving support edge remains separate because it needs theorem uniformity as `epsilon_T->0` or the weight/window changes. The original edge--edge statistic remains further away because it needs a four-level covariance law.