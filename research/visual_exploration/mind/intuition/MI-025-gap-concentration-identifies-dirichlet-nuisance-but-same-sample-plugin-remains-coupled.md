# MI-025 — The log-product removes symmetric-Dirichlet nuisance by an explicit coarea law without forcing tent degeneracy

**Evidence level:** exact Dirichlet-moment and exponential-family calibration from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), [VIS-245](../../findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md), [VIS-246](../../findings/VIS-246-concentration-conditioning-retains-dirichlet-alpha.md), sharpened by the exact coarea disintegration and nondegeneracy witness [VIS-247](../../findings/VIS-247-log-product-conditioning-alpha-free-coarea-law.md).

For symmetric cyclic Dirichlet gaps, the concentration statistic `C=m sum_i X_i^2-1` identifies the nuisance parameter `alpha`, but VIS-246 proves that conditioning on `C` does not remove it for `m>=3`: the conditional slice density still carries `(prod_i X_i)^(alpha-1)`. Identification and elimination are different operations.

The exact sufficient coordinate is

`Lambda(X)=sum_i log X_i=log(prod_i X_i)`.

VIS-247 makes the resulting regular conditional law explicit. On a level `Lambda=lambda<-m log m`, let

`J(x)^2=sum_i x_i^(-2)-(1/m)(sum_i x_i^(-1))^2`.

Then

`P_alpha(dx | Lambda=lambda)=Z(lambda)^(-1) J(x)^(-1) d sigma_lambda(x)`.

The exponential-family factor `exp((alpha-1)lambda)` is constant on the level and cancels under normalization, so the conditional surface law is **exactly independent of `alpha`**. The quotient is not uniform surface measure; the coarea Jacobian is part of the correct calibration.

The same geometry gives a direct signal-retention test. At a regular point, the tangent space to the conditioned surface is orthogonal to both `1=(1,...,1)` and `q=(1/x_i)`. Hence a differentiable statistic `F` varies locally on the level whenever

`grad F notin span{1,q}`.

For the cut-averaged tent statistic, VIS-247 supplies an exact three-gap pair with the same sum and product but different `bar T`, and both points lie in regular regions of positive conditional surface density. Thus exact nuisance removal through `Lambda` does **not** structurally force the tent statistic to collapse.

The live gate is consequently empirical/geometric at the actual frozen scale: can the high-dimensional conditional coarea law be evaluated or sampled accurately enough, and does the predeclared prime statistic retain a residual under that exact quotient? This is narrower than asking whether a sufficient statistic exists, and cleaner than same-sample plug-in calibration through `alpha_hat(C)`.

**Boundary.** The result is exact only for the one-parameter symmetric Dirichlet family and regular levels below the equal-gap maximum. It does not prove useful power in the critical prime regime, does not give a closed form for the full conditional distribution of `bar T`, and does not transfer automatically to asymmetric, mixture, renewal or hard-core nulls. A confirmed conditional residual would still need an independent bridge to the RH-sensitive prime-phase destination.
