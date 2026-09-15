# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Test a frozen prime-gap residual only after exact representation-matched nuisance calibration

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-025-gap-concentration-identifies-dirichlet-nuisance-but-same-sample-plugin-remains-coupled`.

VIS-237--VIS-241 quotient grid-origin phase, Poisson count noise, independently specified one-point intensity and endpoint-cut phase while preserving the spacing geometry to be tested. Symmetric Dirichlet cyclic gaps with independent rotation provide a fixed-count, exactly uniform-intensity dependence family; `alpha=1` is precisely iid-uniform circular spacing.

VIS-242 reduces the cut-averaged tent variance to low-dimensional Dirichlet overlap expectations. VIS-243 closes the deterministic displacement bookkeeping by complement symmetry and exact overlap multiplicities, leaving a finite explicit calibration for every predeclared `alpha`.

VIS-244 resolves the remaining nuisance-identification ambiguity without resolving confirmation itself. The complete-gap concentration

`C=m sum_i X_i^2-1`

satisfies `E[C]=(m-1)/(m alpha+1)` with exact finite-sample variance, so it provides a concrete method-of-moments channel for `alpha` that does not reuse `bar T`. But `C` and `bar T` are computed from the same gap vector and are generally dependent.

The confirmation fork is therefore exact. Either freeze `alpha` from theory or genuinely held-out information and use the fixed-parameter VIS-242--VIS-243 null, or derive/validate the joint `(C,bar T)` calibration before estimating `alpha` and testing `bar T` on the same configuration. A naive plug-in `alpha_hat(C)` treated as fixed is not a calibrated residual.

Only after this nuisance gate is passed should the predeclared prime statistic be compared across increasing scales. A surviving point-process residual is still not an RH mechanism; it must be translated back through the signed prime-phase kernel and survive the earlier moment-null and amplitude controls.

## Keep endpoint semantics and nuisance estimation outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel from VIS-241. If `alpha` is estimated from the same configuration, carry its joint uncertainty rather than switching to a fixed-parameter law after observing `C`. Representation choices, endpoint semantics and the nuisance rule must all be frozen before interpreting the confirmation residual.

VIS-243's half-circle quotient depends specifically on the complement symmetry `q_u(s)=q_u(1-s)` and must not be transferred to oriented or endpoint-sensitive statistics without re-derivation.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.