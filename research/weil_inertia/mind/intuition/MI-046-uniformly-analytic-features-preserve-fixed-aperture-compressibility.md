# MI-046 — Uniformly analytic features preserve fixed-aperture compressibility

**Evidence level:** exact synthesis from [WI-345](../../findings/WI-345-fixed-degree-polynomial-carriers-remain-compressible.md) and [WI-346](../../findings/WI-346-uniformly-analytic-bow-features-remain-compressible.md). The broad preservation of Kolmogorov-width decay under holomorphic maps is prior art; the Mathia content is the explicit fixed-aperture bow specialization and conditioning barrier.

WI-344 proves that one bounded logarithmic source aperture cannot support an extensive family of scale-preserving height directions after fixed height-independent linear preprocessing. WI-345 shows that passing to a fixed-degree polynomial/tensor algebra does not change this: degree `p` only enlarges the residual log-frequency aperture by a finite factor, so at fixed `H Delta` and nonvanishing transmission the normalized family still has bounded effective rank.

WI-346 closes the uniformly analytic extension. Suppose a height-independent feature map has an absolutely convergent bi-homogeneous tensor expansion on the unit carrier sphere with one fixed analytic radius `R>1`, coefficient budget `M_R`, and output norm bounded below by `mu>0`. For any normalized Gram-tail tolerance `tau`, when `H Delta<=1` its effective rank is bounded by

`O_R((1+log(M_R/(mu sqrt(tau))))^2)`,

independently of height, source-set size, output dimension and number of sampled ordinates.

The contrapositive is the useful resource statement. If a fixed-aperture construction really needs effective rank `r(T)->infinity` while retaining a fixed tail fraction, then some apparently secondary feature parameter must itself become expensive: the analytic radius can shrink toward one, the coefficient budget relative to transmitted amplitude can diverge, the polynomial/feature complexity can grow, the source aperture can grow, or the map can become nonsmooth or explicitly height-dependent. Under the uniform analytic hypotheses, maintaining rank beyond `r` already forces `M_R/mu` at least `exp(c_R sqrt(r))` up to fixed constants.

Thus `use nonlinear features` is not a generic escape from time--bandwidth compression. Smooth nonlinear enrichment remains information-limited unless its **complexity or conditioning scales with the problem**. The alternative is a source-specific arithmetic cancellation identity whose usefulness does not depend on manufacturing many generic carrier directions at all.

**Boundary.** The theorem does not cover shrinking analytic radius, unbounded coefficient budgets, hard thresholds/branch singularities, height-dependent maps, growing aperture, or direct signed arithmetic covariance. It is a compression theorem for a declared feature class, not an impossibility theorem for the bow program and not a zero-location result.