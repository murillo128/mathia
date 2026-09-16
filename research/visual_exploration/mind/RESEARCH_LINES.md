# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Calibrate the frozen prime-gap residual under the exact log-product quotient

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-025-gap-concentration-identifies-dirichlet-nuisance-but-same-sample-plugin-remains-coupled`.

VIS-237--VIS-245 progressively quotient grid-origin phase, Poisson count noise, one-point intensity, endpoint-cut phase and fixed-parameter Dirichlet nuisance while making the tent statistic and its concentration covariance explicit. VIS-246 shows that concentration `C=m sum X_i^2-1` identifies the symmetric-Dirichlet nuisance but does not eliminate it for `m>=3`; the exact sufficient coordinate is instead

`Lambda=sum_i log X_i=log(prod_i X_i)`.

VIS-247 closes the structural quotient question. On every regular level `Lambda=lambda<-m log m`, coarea gives the exact parameter-free conditional law

`P_alpha(dx | Lambda=lambda)=Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`,

with

`J(x)^2=sum_i x_i^(-2)-(1/m)(sum_i x_i^(-1))^2`.

All `alpha` dependence cancels exactly, and an exact three-gap same-product pair proves that the cut-averaged tent statistic need not be constant on the level.

VIS-248 supplies the exact low-dimensional audit law. For `m=3`, write `P=X_1X_2X_3=p` and `Q=X_1X_2+X_2X_3+X_3X_1`. Conditional on `P=p`,

`f(Q=q | P=p) proportional Delta_p(q)^(-1/2)`

on its discriminant interval, with the unordered triple recovered as the roots of `t^3-t^2+qt-p`. The cosine parametrization removes the endpoint singularities and gives a deterministic quadrature benchmark.

VIS-249 now removes the abstract high-dimensional sampler-existence gap. Conditional on the complement of any coordinate triple, that block's sum and product are fixed, so its normalized full conditional is exactly the VIS-248 three-gap law. Random-scan exact heat-bath updates over triples with fixed state-independent positive selection probabilities are therefore reversible for the VIS-247 target. At every regular state, the corresponding three-coordinate sum/product-preserving tangent directions span the entire `(m-2)`-dimensional conditioned tangent space, ruling out an infinitesimal rank defect.

The live question is now global and numerical rather than structural. Implement the frozen block kernel, require each one-block sampler to reproduce the exact VIS-248 distribution, and then test stationarity/mixing from deliberately separated admissible starting states at the actual `m` and `lambda`. Only after numerical and Monte Carlo error are materially below the residual scale should the predeclared `bar T` statistic be compared with the prime configuration. Full local tangent rank does not establish irreducibility, a spectral gap, useful mixing time or implementation accuracy.

A surviving point-process residual is still not an RH mechanism. It must translate back through the signed prime-phase kernel and survive the earlier moment-null, amplitude and representation controls.

## Keep endpoint semantics and richer nuisance families outside post-hoc tuning

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel. The exact log-product quotient and VIS-249 block kernel belong specifically to the one-parameter symmetric Dirichlet family. Asymmetric Dirichlet models, mixtures, renewal laws and hard-core processes require their own sufficient coordinates or independently frozen nuisance parameters.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad visual/mixing effects. Any confirmed spacing residual must survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.
