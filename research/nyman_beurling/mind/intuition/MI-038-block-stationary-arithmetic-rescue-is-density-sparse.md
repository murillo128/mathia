# MI-038 — Height adaptation pays a Poisson-resolution refresh tariff before arithmetic rescue can persist

**Evidence level:** literature+derived synthesis from [NB-167](../../findings/NB-167-capped-poisson-transport-unifies-conditioning-and-wasserstein-conservation.md) through [NB-170](../../findings/NB-170-bounded-variation-height-adaptation-pays-a-poisson-resolution-refresh-tariff.md). Montgomery--Vaughan mean-value theory is classical external input; the capped-transport reduction, refresh accounting and bounded-variation quantization are line-specific.

NB-167 leaves a source-specific possibility after generic Poisson geometry is exhausted: the actual values of `zeta'/zeta` could align with a signed compact sampler and produce a completed conservation defect much larger than the worst-case bounded-Lipschitz estimate suggests.

NB-168 separates **persistent mechanism** from **rare resonance** for a stationary template. If one signed offset shape is translated through `[T,2T]`, its Euler defect satisfies

`int_T^(2T) |E_T(t)|^2 dt << T_T^2 (T+a_T^(-2))`.

With `Xi_T=T_T/q_T`, logarithmic rescue therefore occupies density `o(1)` whenever `Xi_T sqrt(1+(T a_T^2)^(-1))=o(log T)`. A fixed observation geometry can align with the source at exceptional centers without providing a block-wide mechanism.

NB-169 prices piecewise adaptation. For templates on `M_T` height cells, the mean-square bookkeeping contains a refresh term `R_T=(T a_T^2)^(-1) sum_j Xi_j^2`. Under a uniform cap `Xi_j<=X_T`, positive-density logarithmic rescue with `X_T=o(log T)` requires at least

`M_T ≳ T a_T^2 log^2 T / X_T^2`

distinguishable refreshes.

NB-170 replaces the literal number of cells by the **variation actually visible at Poisson resolution**. Let `V_T` be the normalized total variation of the path `t -> nu_(T,t)` in capped transport and

`H_T=min(a_T^(-1), log T/log log T)`.

Because `zeta'/zeta` has bounded-Lipschitz size `H_T` on one Poisson window, two templates separated by less than `q_T log T/H_T` in capped transport cannot change a `q_T log T` rescue by more than a fixed fraction. A BV path therefore has only

`M_eff(T) ≍ 1 + V_T H_T/log T`

source-distinguishable templates at the destination scale. Substituting this effective count into NB-169 yields the density bound

`density(rescue) << X_T^2/log^2 T * (1 + 1/(T a_T^2) + V_T H_T/(T a_T^2 log T))`.

Under a subcritical stationary baseline, positive-density rescue consequently forces

`V_T ≳ T a_T^2 log^3 T/(X_T^2 H_T)`.

The important correction is that **continuous adaptation is not a free infinity of templates**. Tiny changes that the source cannot resolve merge into one effective template; only cumulative motion across the capped-transport resolution buys another refresh. The complexity currency is therefore not update count but path length measured in the same metric and at the same resolution that the arithmetic source actually sees.

This sharpens the distinction between source-specific adaptation and source-specific coincidence. Stationary and finite-piecewise families are special cases of one persistence budget: to follow arithmetic phases across positive density, the sampler must spend enough Poisson-resolution motion for the refresh penalty to compete with the logarithmic destination. A mechanism that changes representation continuously still has to pay in the family norm used to claim persistence.

The remaining compact escape is correspondingly narrower: allow very large or infinite capped-transport variation, concentrate on a genuinely sparse exceptional sequence, or exploit a source-specific resonance not reducible to bounded-Lipschitz proximity of nearby templates. A further generalization would need entropy/modulus control for families beyond BV rather than simply granting arbitrary pointwise feedback.

**Boundary.** NB-170 is still a density statement, not pointwise exclusion. A sparse zero-selected architecture may sit entirely in the exceptional set. It does not control merely measurable families of infinite capped-transport variation, and the quantitative tariff remains tied to the current Euler/Poisson reduction and Montgomery--Vaughan mean-value input. Nothing here proves a zero-spacing theorem or RH.