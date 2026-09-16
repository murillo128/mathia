# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate the frozen prime-gap residual under the exact log-product quotient

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-026-dominant-label-mobility-does-not-certify-continuous-mixing`.

VIS-237--VIS-247 progressively quotient grid phase, count noise, one-point intensity, endpoint phase and symmetric-Dirichlet nuisance. Conditioning on `Lambda=sum_i log X_i` gives the exact parameter-free coarea law on each regular level while leaving the cut-averaged tent statistic nonconstant.

VIS-248 gives an exact `m=3` conditional benchmark. VIS-249 lifts it to an exact random-scan three-coordinate heat-bath kernel in arbitrary dimension. VIS-250 proves each regular level is connected and that the exact chain is irreducible, removing disconnected support and hidden block invariants as structural explanations of failure.

VIS-251 removes another tempting bottleneck. In the strong-dominance cone `x_j>3 max_(k!=j)x_k`, uniform triple scanning switches the identity of the maximum with exact probability `2/m`, independent of `lambda`. Increasingly extreme log-product conditioning therefore cannot slow the chain merely by trapping the dominant **label**. Any high-dimensional slowdown must live in continuous within-label geometry, narrow fibres, another conductance cut, a collective coordinate or numerical implementation error.

The live question is now quantitative. Implement the frozen exact block kernel, verify every one-block sampler against VIS-248, and estimate convergence at the actual `(m,lambda)` using continuous observables that are relevant to `bar T`, not just dominant-label motion. Monte Carlo, initialization and numerical uncertainty must be materially below the predeclared residual scale before the prime configuration is inspected.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The exact log-product quotient and VIS-248--VIS-251 block theory belong to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes require their own sufficient coordinates or independently frozen nuisance parameters.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.
