# MI-025 — Gap concentration identifies but does not remove Dirichlet nuisance; the log-product is sufficient

**Evidence level:** exact Dirichlet-moment and exponential-family calibration from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), [VIS-245](../../findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md), and [VIS-246](../../findings/VIS-246-concentration-conditioning-retains-dirichlet-alpha.md), within the representation-matched null of VIS-240--VIS-243.

For symmetric cyclic Dirichlet gaps `X=(X_1,...,X_m)`, define

`H=sum_i X_i^2`,  `C=mH-1`.

VIS-244 gives `E[C]=(m-1)/(m alpha+1)`, strictly decreasing in `alpha`, together with an exact finite-sample variance. Thus `C` is a concrete nuisance-estimation channel. VIS-245 quantifies its dependence on the cut-averaged tent statistic `bar T`: Dirichlet neutrality reduces `Cov(C,bar T)` exactly to one-dimensional truncated beta moments, so the fixed-`alpha` mean/covariance block is explicit.

VIS-246 separates **identification** from **elimination**. Conditioning on `H=h` restricts the gap vector to the simplex-sphere slice `sum X_i=1`, `sum X_i^2=h`. The tangent coarea factor is constant on that slice, so the conditional density remains

`P_alpha(dX | H=h) proportional to (prod_i X_i)^(alpha-1) d sigma_h`.

For every `m>=3`, a concentration sphere contains configurations with different coordinate products, hence their conditional likelihood ratio depends on `alpha`. Therefore neither `H` nor `C` is a sufficient statistic for `alpha`, and **`Law(bar T | C)` is not automatically nuisance-free**. The exact exception is `m=2`, where `X_1 X_2=(1-H)/2` makes the product a function of the concentration.

The one-parameter Dirichlet density instead factors through

`L(X)=sum_i log X_i = log(prod_i X_i)`,

`f_alpha(X)=K(alpha) exp((alpha-1)L(X))`.

By Fisher--Neyman factorization, `L` is sufficient for `alpha`; consequently `Law(bar T | L)` is independent of `alpha` wherever the regular conditional law is defined. This is an exact same-configuration nuisance quotient, not a plug-in approximation.

The new gate is therefore geometric rather than statistical-identification ambiguity: determine whether conditioning on `L` leaves a tractable, nondegenerate tent statistic and whether the candidate prime residual survives that quotient. A sufficient statistic can remove signal together with nuisance. The alternative remains to freeze `alpha` from theory or genuinely held-out information and use the fixed-parameter null. Using `alpha_hat(C)` on the same sample still requires a full joint calibration or a controlled approximation; the exact covariance alone is insufficient.

**Boundary.** The symmetric Dirichlet family is a representation-matched null, not a theorem about prime gaps. `L` sufficiency does not give a closed form for `bar T | L`, does not prove power against a prime alternative, and does not transfer to asymmetric Dirichlet, mixture, hard-core or renewal families without re-deriving their nuisance structure.