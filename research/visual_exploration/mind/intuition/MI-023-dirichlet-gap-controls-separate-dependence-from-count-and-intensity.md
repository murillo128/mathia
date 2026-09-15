# MI-023 — Dirichlet gap controls separate dependence from count and intensity; random-cut variance is a distinct endpoint channel

**Evidence level:** exact finite-sample calibration from [VIS-240](../../findings/VIS-240-rotation-randomized-dirichlet-gaps-give-fixed-count-uniform-intensity-dependence-null.md), sharpened by the exact endpoint-phase variance decomposition [VIS-241](../../findings/VIS-241-random-cut-separates-endpoint-phase-variance.md), extending the representation and nuisance controls in [VIS-237](../../findings/VIS-237-origin-averaged-collision-count-is-a-triangular-pair-gap-functional.md)--[VIS-239](../../findings/VIS-239-cumulative-intensity-gauge-uniformizes-specified-iid-intensity.md).

After grid origin, total-count randomness and a specified one-point intensity have been quotiented out, the remaining pair statistic still needs a dependence null that lives on the same monotone ordered-point representation. VIS-240 supplies one without reintroducing those nuisance variables.

Take `m` cyclic gaps on a circle of length `L` with

`(G_1,...,G_m)/L ~ Dirichlet(alpha,...,alpha)`

and add an independent uniform rotation before cutting and sorting the points. The count is exactly `m`; every one-point marginal is exactly uniform for every `alpha`; and every realization remains one strictly increasing ordered configuration after the cut. What changes with `alpha` is gap dependence and heterogeneity. The family contains the iid-uniform fixed-count model exactly at `alpha=1`.

VIS-240 gives an exact finite-sample mean for the triangular tent statistic, but its random rotation/cut initially leaves dependence fluctuation and endpoint phase mixed together. VIS-241 separates them exactly. For a fixed circular configuration, let `delta_p` be the shorter circular distance of pair `p`, `w_p=(1-delta_p/ell)_+`, and let `A_p` be its minor arc. Then the post-cut statistic is a weighted arc-coverage count, and averaging the uniform cut gives

`bar T=sum_p w_p(1-delta_p/L)`.

The conditional cut variance `V_cut` is an explicit quadratic form in the arc lengths and pairwise arc overlaps. If the circular gap configuration is random with data `G`, the law of total variance becomes

`Var_(G,Theta)(T)=Var_G(bar T)+E_G[V_cut]`.

This decomposition identifies a new nuisance boundary. **Dependence geometry and endpoint phase are different random resources even when both arise from the same rotation-randomized construction.** If the circle is only an auxiliary stationary representation and the finite cut is arbitrary, `bar T` is the cleaner confirmation statistic because it removes endpoint phase exactly. If physical interval endpoints are mathematically distinguished, the cut channel is part of the model and must not be quotiented away.

The resulting audit rule is stricter than after VIS-240. Freeze the endpoint semantics before looking at the confirmation statistic. For an endpoint-invariant test, the remaining target is `Var_G(bar T)` or a stronger finite-sample law under a predeclared `alpha`; for an endpoint-sensitive test, add the exact `E_G[V_cut]` contribution. In either case, fitting `alpha` or choosing the endpoint convention on the same statistic can absorb the residual by construction.

The key conceptual gain is that a representation-matched null can often be **factorized by nuisance source** rather than calibrated as one opaque variance. Removing an exact nuisance channel reduces the stochastic problem only when that channel is genuinely irrelevant to the mathematical source. The remaining dependence law, not the act of normalization itself, is where a potential prime-specific residual must survive.

**Boundary.** The symmetric Dirichlet family remains a calibration family, not a theorem about prime gaps. VIS-241 does not compute `Var_G(bar T)`, does not show `E_G[V_cut]` is small or large, and does not supply a prime-specific residual. A single `alpha` does not encode arbitrary long-range arithmetic dependence, and endpoint-phase averaging is valid only when the endpoints are genuinely nuisance.