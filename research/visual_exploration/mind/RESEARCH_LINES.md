# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate nonlinear slowdown under the exact log-product quotient before interpreting a prime residual

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-028-fiber-variance-certifies-nonlinear-heat-bath-slowdown`.

VIS-237--VIS-247 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance. Conditioning on `Lambda=sum_i log X_i` gives the exact parameter-free coarea law on each regular level while leaving the cut-averaged tent statistic nonconstant.

VIS-248 gives an exact `m=3` conditional benchmark. VIS-249 lifts it to an exact random-scan three-coordinate heat-bath kernel in arbitrary dimension. VIS-250 proves each regular level is connected and the exact chain irreducible; VIS-251 rules out dominant-label trapping as the high-`|lambda|` explanation.

VIS-252--VIS-253 supply two exact additive-invariant calibrations. Every ordinary contrast `x_i-x_j` and every logarithmic contrast `log x_i-log x_j` is an eigenmode with `rho_m=(m-3)/(m-1)` and integrated autocorrelation time `m-2` triple updates.

VIS-254 adds an exact nonlinear lower-bound diagnostic. For any fixed-weight exact heat-bath chain, the averaged conditional fiber variance `D_f` is the Dirichlet form and `delta_f=D_f/Var(f)` satisfies `tau_int(f)>=2/delta_f-1`. For the present triple chain the linear families have `delta=2/(m-1)` with equality in the bound. Therefore `delta_(bar T)<2/(m-1)` rigorously certifies that `bar T` has integrated autocorrelation strictly larger than `m-2`, using only the exact three-coordinate fibers for the inner variance.

The live operational question is now narrower. A frozen implementation must reproduce VIS-248 and both linear/log eigenmode families, then estimate the stationary target-law ratio `delta_(bar T)` before expensive long-lag interpretation. If it certifies slowdown, the sampler budget must reflect that nonlinear scale; if it does not, separated-start and long-lag checks remain necessary because a large one-step dissipation does not prove fast mixing. Only after these gates should `bar T` be compared with the prime data.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The exact log-product quotient and VIS-248--VIS-254 heat-bath theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes require their own sufficient coordinates or independently frozen nuisance parameters.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.
