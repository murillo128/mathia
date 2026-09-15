# MI-025 — Gap concentration identifies the Dirichlet nuisance parameter, but same-sample plug-in remains coupled

**Evidence level:** exact Dirichlet-moment calibration from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), extending the representation-matched null of VIS-240--VIS-243.

For symmetric cyclic Dirichlet gaps `X=(X_1,...,X_m)`, define

`H=sum_i X_i^2`,  `C=mH-1`.

Because the complete gap vector has empirical mean exactly `1/m`, `C` is the squared empirical coefficient of variation across gaps. Its first moment is

`E[C]=(m-1)/(m alpha+1)`,

which is strictly decreasing in `alpha` and therefore identifies the one-parameter dependence coordinate in expectation. The corresponding method-of-moments inversion is

`alpha_hat=(m-1-C)/(mC)`

for `C>0`. VIS-244 also gives the exact finite-sample variance

`Var(C)=2m^2 alpha(alpha+1)(m-1)/[(m alpha+1)^2(m alpha+2)(m alpha+3)]`.

This creates a nuisance-parameter channel that is distinct from the cut-averaged tent statistic `bar T`. But distinct statistics are not independent statistics: both are functions of the same gap vector. Estimating `alpha` from `C` on the same configuration and then treating `bar T` as if it came from a fixed known-`alpha` law silently discards fit uncertainty and the covariance between the two channels.

There are therefore two honest confirmation geometries. Either freeze `alpha` from theory or genuinely held-out information and use the fixed-parameter VIS-242--VIS-243 calibration, or derive/calibrate the joint law of `(C,bar T)` and carry the nuisance fit through the same-sample test. Exact identifiability of a nuisance parameter is not the same thing as nuisance-free confirmation.

**Boundary.** The Dirichlet family remains only a representation-matched null, not a theorem about prime gaps. `alpha_hat` is not claimed unbiased or sufficient, and VIS-244 does not supply the joint `(C,bar T)` law. The finding narrows the calibration fork; it does not report a prime residual.