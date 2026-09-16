# MI-038 — Height adaptation pays source-resolution complexity in both path order and geometric repertoire

**Evidence level:** literature+derived synthesis from [NB-167](../../findings/NB-167-capped-poisson-transport-unifies-conditioning-and-wasserstein-conservation.md) through [NB-172](../../findings/NB-172-small-template-entropy-suppresses-arbitrarily-rough-height-adaptation.md). Montgomery--Vaughan mean-value theory is classical external input; the capped-transport reduction and adaptation tariffs are line-specific.

NB-167 leaves a source-specific possibility after generic Poisson geometry is exhausted: actual values of `zeta'/zeta` could align with a compact signed sampler and produce a completed defect much larger than the worst-case bounded-Lipschitz estimate. NB-168 shows that one stationary template can achieve such logarithmic rescue only on a sparse set under the subcritical source budget.

The first adaptation currency is **ordered distinguishability**. NB-169 prices piecewise refreshes; NB-170 replaces literal switch count by capped-transport total variation; NB-171 identifies the ordered template number `M_T(epsilon)` at source resolution. Finite `p`-variation gives

`M_T(epsilon) << 1 + (V_(p,T)/epsilon)^p`,

so under a subcritical stationary baseline positive-density rescue forces a corresponding power-law lower bound on `V_(p,T)`. Infinite `1`-variation is not an escape if some higher finite variation remains controlled.

NB-172 adds a logically different currency: **unordered range entropy**. Let `N_T(epsilon)` be the least number of actual family templates whose capped-transport balls cover the whole height-dependent range. At logarithmic rescue resolution `epsilon_T~log T/H_T`, arbitrary height dependence obeys

`density(rescue) << N_T(epsilon_T) X_T^2/log^2 T * (1 + 1/(T a_T^2))`.

No continuity, variation bound, measurable selector or interval decomposition is needed. A sampler may jump on a dense set and have infinite `p`-variation for every finite `p`; if it repeatedly chooses from only a small source-resolution repertoire, it still reduces to finitely many stationary exceptional sets.

Ordered and unordered complexity are complementary rather than successive approximations to one quantity. A path can traverse many distinct states with small structured variation, where the ordered theorem is efficient, or switch violently among a few recurrent shapes, where range entropy is decisive. Positive-density arithmetic rescue must have enough complexity in whichever currency remains cheap: it cannot be obtained merely by making the height dependence rough.

The durable principle is therefore **source-resolution adaptation complexity**, with at least two coordinates: how many genuinely different templates exist, and how the path moves among them. The natural next escape is a genuinely arithmetic selector with simultaneously large Poisson-resolution repertoire and enough ordered refresh complexity, a sparse exceptional-height mechanism, or the ultra-thin regime where the stationary mean-square input itself loses force.

**Boundary.** These are density estimates, not pointwise exclusions. A selected sparse sequence may lie entirely inside the exceptional set. The quantitative bounds inherit the compact-support Euler/Poisson reduction and Montgomery--Vaughan limitations, especially when `T a_T^2` is too small. Neither ordered variation nor range entropy alone is claimed necessary in every adaptive architecture.