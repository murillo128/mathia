# MI-025 — Gap concentration identifies the Dirichlet nuisance, and its covariance with the tent statistic is explicit

**Evidence level:** exact Dirichlet-moment calibration from [VIS-244](../../findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md), strengthened by the exact cross-covariance formula [VIS-245](../../findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md), within the representation-matched null of VIS-240--VIS-243.

For symmetric cyclic Dirichlet gaps `X=(X_1,...,X_m)`, define

`H=sum_i X_i^2`,  `C=mH-1`.

VIS-244 gives `E[C]=(m-1)/(m alpha+1)`, strictly decreasing in `alpha`, together with an exact finite-sample variance. Thus `C` is a concrete nuisance-parameter channel for the symmetric Dirichlet dependence coordinate.

VIS-245 now quantifies its dependence on the cut-averaged tent statistic `bar T`. Conditioning on one cyclic arc mass `S` makes `E[H|S=s]` a quadratic polynomial by Dirichlet neutrality. Multiplying by the piecewise-quadratic tent kernel reduces `E[H q_u(S)]` to one-dimensional truncated beta moments through degree four. Summing the cyclic arc classes yields an exact closed formula for `Cov(C,bar T)` at every fixed `(m,alpha,u)`.

Together with VIS-242--VIS-244, the complete fixed-`alpha` mean/covariance block for `(C,bar T)` is therefore explicit. This removes the ambiguity about whether the fitting and confirmation channels are coupled: they generally are, and the strength of that coupling is exactly computable.

But covariance is not the same thing as nuisance-free calibration. The method-of-moments map `alpha_hat(C)` is nonlinear, and the conditional law of `bar T` given `C` is not determined by the covariance matrix. A same-configuration test still needs the full/conditional joint calibration, or an independently justified approximation whose error is controlled. The clean alternative remains to freeze `alpha` from theory or genuinely held-out information and use the fixed-parameter tent law.

**Boundary.** The symmetric Dirichlet family is a representation-matched null, not a theorem about prime gaps. VIS-245 does not give the joint law, an exact distribution for `alpha_hat`, a prime residual or an RH consequence. It narrows the remaining nuisance problem from unknown dependence to a specific higher-order conditional-calibration gate.