# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Test a frozen prime-gap residual only after exact representation-matched nuisance calibration

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-025-gap-concentration-identifies-dirichlet-nuisance-but-same-sample-plugin-remains-coupled`.

VIS-237--VIS-241 quotient grid-origin phase, Poisson count noise, independently specified one-point intensity and endpoint-cut phase while preserving the spacing geometry to be tested. Symmetric Dirichlet cyclic gaps with independent rotation provide a fixed-count, exactly uniform-intensity dependence family; `alpha=1` is precisely iid-uniform circular spacing.

VIS-242--VIS-243 make the fixed-`alpha` tent calibration explicit. VIS-244 identifies the Dirichlet nuisance coordinate through the complete-gap concentration `C=m sum_i X_i^2-1`, with exact expectation and variance. VIS-245 now supplies the missing cross term: `Cov(C,bar T)` reduces exactly to one-dimensional truncated beta moments through degree four. The complete fixed-`alpha` mean/covariance matrix of `(C,bar T)` is therefore explicit.

The remaining same-sample gate is no longer unknown covariance. It is the **conditional/full joint calibration** needed after applying the nonlinear estimator `alpha_hat(C)` on the same configuration. Exact second moments do not determine `Law(bar T | C)` and do not justify treating the fitted `alpha` as fixed.

The confirmation fork is consequently sharp. Either freeze `alpha` from theory or genuinely held-out information and use the fixed-parameter null, or derive/validate the joint/conditional calibration that carries `C -> alpha_hat(C)` through the same-sample test. Only after that nuisance gate is passed should a predeclared prime statistic be compared across increasing scales.

A surviving point-process residual is still not an RH mechanism. It must translate back through the signed prime-phase kernel and survive the earlier moment-null, amplitude and representation controls.

## Keep endpoint semantics and nuisance estimation outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel from VIS-241. If `alpha` is estimated from the same configuration, carry its conditional uncertainty rather than switching to a fixed-parameter law after observing `C`.

VIS-243's half-circle quotient depends specifically on complement symmetry and must not be transferred to oriented or endpoint-sensitive statistics without re-derivation. VIS-245 likewise belongs to the symmetric Dirichlet family and does not license a Gaussian or linear-regression nuisance correction by itself.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.