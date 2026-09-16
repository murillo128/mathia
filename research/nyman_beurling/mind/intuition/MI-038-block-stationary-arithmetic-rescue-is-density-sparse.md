# MI-038 — Height adaptation pays an explicit refresh penalty before it can make arithmetic rescue persistent

**Evidence level:** literature+derived synthesis from [NB-167](../../findings/NB-167-capped-poisson-transport-unifies-conditioning-and-wasserstein-conservation.md) through [NB-169](../../findings/NB-169-piecewise-adaptive-templates-pay-a-refresh-penalty.md). Montgomery--Vaughan mean-value theory is classical external input; the capped-transport reduction and refresh accounting are line-specific.

NB-167 leaves a source-specific possibility after generic Poisson geometry is exhausted: the actual values of `zeta'/zeta` could align with a signed compact sampler and produce a completed conservation defect much larger than the worst-case bounded-Lipschitz estimate suggests.

NB-168 separates **persistent mechanism** from **rare resonance** for a stationary template. If one signed offset shape is translated through `[T,2T]`, its Euler defect satisfies

`int_T^(2T) |E_T(t)|^2 dt << T_T^2 (T+a_T^(-2))`.

With `Xi_T=T_T/q_T`, logarithmic rescue therefore occupies density `o(1)` whenever `Xi_T sqrt(1+(T a_T^2)^(-1))=o(log T)`. A fixed observation geometry can align with the source at exceptional centers without providing a block-wide mechanism.

NB-169 prices the obvious escape: let the template change on a partition of `[T,2T]` into `M_T` intervals. If `Xi_j` is the normalized capped transport on cell `j`, the exact mean-square bookkeeping splits into

`A_T=(1/T) sum_j Xi_j^2 H_j`

for ordinary within-cell energy and

`R_T=(1/(T a_T^2)) sum_j Xi_j^2`

for the **refresh penalty**. A positive-density set of `q_T log T`-scale Euler rescues requires `A_T+R_T` to be at least logarithmic-square scale. Under the uniform cap `Xi_j<=X_T`, the exceptional density is bounded by

`X_T^2/(eta^2 log^2 T) * (1+M_T/(T a_T^2))`.

Hence

`X_T sqrt(1+M_T/(T a_T^2))=o(log T)`

still forces rescue to density zero. When `X_T=o(log T)`, positive-density rescue needs at least

`M_T ≳ T a_T^2 log^2 T / X_T^2`

refreshes. Height adaptation is therefore a real resource, but not a free one: the source can only be tracked persistently by spending enough template changes relative to the shrinking Poisson width.

This turns the former qualitative loophole “allow the shape to adapt with height” into a quantitative complexity axis. Stationary templates correspond to `M_T=1`; piecewise adaptation only escapes once its refresh rate reaches the scale at which the `a_T^(-2)` boundary term can compete with the logarithmic destination. The next honest generalization is not arbitrary pointwise adaptation but a continuously varying family with a controlled variation/entropy budget and a theorem converting that budget into an analogue of `R_T`.

The reusable distinction is between **source-specific adaptation** and **source-specific coincidence**, with an explicit switching cost. A mechanism that changes representation from cell to cell must pay for those changes in the same family norm used to claim persistence; otherwise free switching can fit rare arithmetic phases without producing a uniform destination theorem.

**Boundary.** NB-169 still gives a density statement, not pointwise exclusion. A sparse zero-selected architecture may sit entirely in the exceptional set. The piecewise model does not yet cover continuously varying or source-feedback templates except through future complexity bounds, and the constants remain tied to the current Euler/Poisson reduction. Nothing here proves a zero-spacing theorem or RH.