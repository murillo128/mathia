# MI-025 — The log-product removes symmetric-Dirichlet nuisance by an explicit coarea law, with an exact three-gap audit distribution

**Evidence level:** exact Dirichlet-moment and exponential-family calibration from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), [VIS-245](../../findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md), [VIS-246](../../findings/VIS-246-concentration-conditioning-retains-dirichlet-alpha.md), sharpened by the exact coarea disintegration/nondegeneracy witness [VIS-247](../../findings/VIS-247-log-product-conditioning-alpha-free-coarea-law.md) and the exact three-gap discriminant benchmark [VIS-248](../../findings/VIS-248-three-gap-log-product-discriminant-audit.md).

For symmetric cyclic Dirichlet gaps, the concentration statistic `C=m sum_i X_i^2-1` identifies the nuisance parameter `alpha`, but VIS-246 proves that conditioning on `C` does not remove it for `m>=3`: the conditional slice density still carries `(prod_i X_i)^(alpha-1)`. Identification and elimination are different operations.

The exact sufficient coordinate is

`Lambda(X)=sum_i log X_i=log(prod_i X_i)`.

VIS-247 makes the resulting regular conditional law explicit. On a level `Lambda=lambda<-m log m`, let

`J(x)^2=sum_i x_i^(-2)-(1/m)(sum_i x_i^(-1))^2`.

Then

`P_alpha(dx | Lambda=lambda)=Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`.

The exponential-family factor `exp((alpha-1)lambda)` is constant on the level and cancels under normalization, so the conditional surface law is **exactly independent of `alpha`**. The quotient is not uniform surface measure; the coarea Jacobian is part of the correct calibration.

The same geometry gives a direct signal-retention test. At a regular point, the tangent space to the conditioned surface is orthogonal to both `1=(1,...,1)` and `q=(1/x_i)`. Hence a differentiable statistic `F` varies locally on the level whenever `grad F notin span{1,q}`. VIS-247 supplies an exact three-gap same-product pair with different `bar T`, proving that exact nuisance removal through `Lambda` does not structurally force the tent statistic to collapse.

VIS-248 turns the `m=3` quotient into an exact sampler audit. Put `P=X_1X_2X_3=p` and `Q=X_1X_2+X_2X_3+X_3X_1`. On the conditional level `P=p`, the unordered gap triple is recovered as the roots of

`t^3-t^2+Qt-p`,

and the conditional density of `Q` is

`f(q | p)=Z(p)^(-1) Delta_p(q)^(-1/2)`

on the discriminant interval, with

`Delta_p(q)=q^2-4q^3-4p-27p^2+18pq`.

This law is again exactly `alpha`-free. Its inverse-square-root endpoint behavior is removed by the cosine parametrization of the interval, giving deterministic one-dimensional quadrature. The low-dimensional benchmark is therefore not a visual sanity check: it is an exact distribution against which a coarea implementation can be tested before high-dimensional use.

The live gate is consequently empirical/geometric at the actual frozen scale, but with a hard validation precursor: reproduce the VIS-248 `m=3` law first, then test whether the high-dimensional conditional sampler/evaluator is accurate enough and whether the predeclared prime statistic retains a residual under that exact quotient. This is narrower than asking whether a sufficient statistic exists, and cleaner than same-sample plug-in calibration through `alpha_hat(C)`.

**Boundary.** The exact quotient statements apply to the one-parameter symmetric Dirichlet family and regular log-product levels. VIS-248 is a three-gap audit law, not validation of a high-dimensional algorithm or evidence for a prime residual. None of these results transfers automatically to asymmetric, mixture, renewal or hard-core nulls, and a confirmed conditional residual would still need an independent bridge to the RH-sensitive prime-phase destination.
