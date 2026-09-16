# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate the frozen prime-gap residual under the exact log-product quotient

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-027-uniform-triple-gibbs-has-mandatory-linear-relaxation`.

VIS-237--VIS-247 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance. Conditioning on `Lambda=sum_i log X_i` gives the exact parameter-free coarea law on each regular level while leaving the cut-averaged tent statistic nonconstant.

VIS-248 gives an exact `m=3` conditional benchmark. VIS-249 lifts it to an exact random-scan three-coordinate heat-bath kernel in arbitrary dimension. VIS-250 proves each regular level is connected and that the exact chain is irreducible, removing disconnected support and hidden block invariants as structural explanations of failure.

VIS-251 removes dominant-label trapping as a high-`|lambda|` explanation: in the strong-dominance cone, uniform triple scanning switches the identity of the maximum with exact probability `2/m`, independent of `lambda`.

VIS-252 supplies the first global quantitative calibration that follows from the scan itself. Every centered coordinate `x_i-1/m` and every contrast `x_i-x_j` is an exact eigenfunction with `rho_m=(m-3)/(m-1)`. Hence `gap(P)<=2/(m-1)`, the stationary contrast autocorrelation is exactly `rho_m^t`, and its integrated autocorrelation time is `m-2` triple updates. This benchmark is independent of `lambda` and the detailed fibre density.

The live question is now sharply nonlinear: after an implementation reproduces the exact `rho_m^t` law and `m-2` calibration, determine whether `bar T` or other statistic-relevant collective observables mix substantially more slowly from separated admissible starts. Any additional slowdown then belongs to continuous conditioned geometry, a nonlinear conductance bottleneck or numerics—not to disconnected support, dominant-label trapping or the elementary scan-refresh rate.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The exact log-product quotient and VIS-248--VIS-252 block theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes require their own sufficient coordinates or independently frozen nuisance parameters.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.
