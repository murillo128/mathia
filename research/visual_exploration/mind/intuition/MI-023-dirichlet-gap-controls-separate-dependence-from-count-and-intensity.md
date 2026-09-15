# MI-023 — Dirichlet gap controls separate dependence from fixed count and one-point intensity

**Evidence level:** exact finite-sample calibration from [VIS-240](../../findings/VIS-240-rotation-randomized-dirichlet-gaps-give-fixed-count-uniform-intensity-dependence-null.md), extending the representation and nuisance controls in [VIS-237](../../findings/VIS-237-origin-averaged-collision-count-is-a-triangular-pair-gap-functional.md)--[VIS-239](../../findings/VIS-239-cumulative-intensity-gauge-uniformizes-specified-iid-intensity.md).

After grid origin, total-count randomness and a specified one-point intensity have been quotiented out, the remaining pair statistic still needs a dependence null that lives on the same monotone ordered-point representation. VIS-240 supplies one without reintroducing those nuisance variables.

Take `m` cyclic gaps on an interval/circle of length `L` with

`(G_1,...,G_m)/L ~ Dirichlet(alpha,...,alpha)`

and add an independent uniform rotation before cutting and sorting the points. The count is exactly `m`; every one-point marginal is exactly uniform for every `alpha`; and every realization is still one strictly increasing ordered point configuration after the cut. What changes with `alpha` is gap dependence and heterogeneity.

This family contains the iid-uniform fixed-count model exactly at `alpha=1`. Larger `alpha` suppresses gap variation and approaches regular spacing; smaller `alpha` produces more uneven clustered gaps. The coefficient of variation of a normalized gap is explicit,

`CV^2=(m-1)/(m alpha+1)`,

so the dependence axis is interpretable rather than an arbitrary label randomization.

For the triangular tent statistic, consecutive-gap aggregation makes each cyclic arc fraction beta distributed. Randomizing the cut converts that arc into the correct linear separation, and the finite-sample mean becomes an explicit sum of incomplete-beta terms. Hence the iid-uniform calibration center is not privileged: it is one point on an exact representation-matched dependence family with the same count and intensity.

The resulting audit rule is strict. A prime residual against iid-uniform spacing is not source evidence until it survives a frozen dependence family that preserves the acquisition sigma-field. Conversely, fitting `alpha` on the same confirmation statistic without carrying parameter uncertainty can absorb the residual by construction and is not an independent null.

The next mathematical object is the fluctuation law, not another mean correction. Derive or independently calibrate the variance/covariance of the tent statistic for fixed external `alpha`, or obtain a finite-sample distributional control strong enough to compare the observed prime configuration. Only a residual outside that dependence envelope is worth translating back to the signed prime-phase kernel.

**Boundary.** The symmetric Dirichlet family is a calibration family, not a theorem about prime gaps. VIS-240 gives the exact center but not the dependent variance or full law. A single `alpha` does not encode arbitrary long-range arithmetic dependence, and random rotation must be re-audited if physical interval endpoints become mathematically distinguished.