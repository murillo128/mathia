# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Test a frozen prime-gap residual only after an exact representation-matched nuisance quotient

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-025-gap-concentration-identifies-dirichlet-nuisance-but-same-sample-plugin-remains-coupled`.

VIS-237--VIS-241 quotient grid-origin phase, Poisson count noise, independently specified one-point intensity and endpoint-cut phase while preserving the spacing geometry to be tested. Symmetric Dirichlet cyclic gaps with independent rotation provide a fixed-count, exactly uniform-intensity dependence family; `alpha=1` is precisely iid-uniform circular spacing.

VIS-242--VIS-243 make the fixed-`alpha` tent calibration explicit. VIS-244 identifies the Dirichlet nuisance through the complete-gap concentration `C=m sum_i X_i^2-1`, and VIS-245 gives the exact cross-covariance `Cov(C,bar T)`. VIS-246 now closes the tempting shortcut “condition on the observed concentration.” For `m>=3`, the conditional density on a fixed-`C` simplex-sphere slice is proportional to `(prod_i X_i)^(alpha-1)`, so `Law(bar T | C)` still depends on `alpha` in general. The two-gap case is the exact low-dimensional exception.

The same finding identifies the exact nuisance coordinate instead. The log-product

`L=sum_i log X_i`

is a sufficient statistic for the one-parameter symmetric-Dirichlet family, hence the conditional law of **any** gap statistic given `L` is independent of `alpha`. The live exact same-configuration route is therefore to determine whether the predeclared tent statistic has a tractable and nondegenerate `Law(bar T | L)` and whether this quotient retains the candidate prime-specific geometry. A held-out/theoretical `alpha` with the fixed-parameter null remains the clean alternative. Plug-in calibration through `alpha_hat(C)` is still possible only with an independently justified full joint approximation; conditioning on `C` itself is not nuisance elimination.

A surviving point-process residual is still not an RH mechanism. It must translate back through the signed prime-phase kernel and survive the earlier moment-null, amplitude and representation controls.

## Keep endpoint semantics and nuisance estimation outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel from VIS-241. If `alpha` is estimated from the same configuration through `C`, carry its full uncertainty rather than switching to a fixed-parameter law after observing `C`. If the exact sufficient-statistic route is used, predeclare conditioning on `L` and audit whether the resulting conditional statistic still has useful variation.

VIS-243's half-circle quotient depends specifically on complement symmetry and must not be transferred to oriented or endpoint-sensitive statistics without re-derivation. VIS-246's `L` sufficiency likewise belongs specifically to the symmetric one-parameter Dirichlet family; richer/asymmetric gap laws require their own nuisance factorization.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.