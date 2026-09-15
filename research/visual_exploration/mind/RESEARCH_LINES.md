# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate the frozen prime-gap residual under the exact log-product quotient

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-025-gap-concentration-identifies-dirichlet-nuisance-but-same-sample-plugin-remains-coupled`.

VIS-237--VIS-245 progressively quotient grid-origin phase, Poisson count noise, one-point intensity, endpoint-cut phase and fixed-parameter Dirichlet nuisance while making the tent statistic and its concentration covariance explicit. VIS-246 shows that concentration `C=m sum X_i^2-1` identifies the symmetric-Dirichlet nuisance but does not eliminate it for `m>=3`; the exact sufficient coordinate is instead

`Lambda=sum_i log X_i=log(prod_i X_i)`.

VIS-247 closes the two structural questions left by that result. On every regular level `Lambda=lambda<-m log m`, coarea gives the exact conditional law

`P_alpha(dx | Lambda=lambda)=Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`,

with

`J(x)^2=sum_i x_i^(-2)-(1/m)(sum_i x_i^(-1))^2`.

All `alpha` dependence cancels exactly. The law is not generally uniform on the level surface, but it is explicit and parameter-free. Moreover the quotient does not automatically destroy the tent statistic: a differential criterion detects variation along the level, and VIS-247 gives an exact three-gap same-product pair with different `bar T`, proving genuine conditional nondegeneracy in at least one regular configuration.

The live question is now application-specific rather than another nuisance-identification problem. For the frozen high-dimensional critical prime configuration, evaluate or independently validate this exact coarea conditional law accurately enough to calibrate the predeclared `bar T`, then test whether a prime-specific residual survives. A held-out/theoretical fixed `alpha` remains a clean alternative. Same-sample plug-in through `alpha_hat(C)` still requires its own joint calibration and should not be confused with exact conditioning.

A surviving point-process residual is still not an RH mechanism. It must translate back through the signed prime-phase kernel and survive the earlier moment-null, amplitude and representation controls.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The exact log-product quotient belongs specifically to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes require their own sufficient coordinates or independently frozen nuisance parameters.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.
