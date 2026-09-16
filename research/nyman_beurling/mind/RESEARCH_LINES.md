# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the one-Poisson-width interlaced signed-sampler regime

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-038-block-stationary-arithmetic-rescue-is-density-sparse`.

NB-148--NB-160 show that zero-mass signed exterior sampling removes the universal Hadamard logarithm only by exporting sign debt. Mesoscopic spreading, finite atomic repair and even arbitrary signed Borel samplers with Jordan supports separated by many Poisson widths still force an adverse `Omega(log G)` zero reservoir under bounded effective conditioning.

NB-161--NB-167 isolate the finely interlaced regime and identify capped Poisson transport as the common source currency. With `d_a(s,t)=min{1,|s-t|/a}`, optimal Jordan transport mass `T_G` and `Xi_G=T_G/q_G`, the same `Xi_G` controls every Poisson response and gives completed conservation remainder `O(q_G Xi_G E_G)`.

NB-168 attacks source-specific cancellation for a height-stationary compact template. Its Euler defect has mean square `O(T_T^2(T+a_T^(-2)))`, so logarithmic rescue is confined to density zero when `Xi_T sqrt(1+(T a_T^2)^(-1))=o(log T)`.

NB-169 extends this to **piecewise adaptive** templates. Partition `[T,2T]` into `M_T` cells and let `Xi_j` be the normalized capped transport on cell `j`. The mean-square budget separates ordinary cell energy from a refresh term

`R_T=(1/(T a_T^2)) sum_j Xi_j^2`.

Under `Xi_j<=X_T`, logarithmic rescue still has density `o(1)` if

`X_T sqrt(1+M_T/(T a_T^2))=o(log T)`.

Conversely, when `X_T=o(log T)`, positive-density rescue requires at least `M_T ≳ T a_T^2 log^2 T/X_T^2` template changes.

NB-170 replaces literal refresh counting by **bounded variation in capped Poisson transport**. If `V_T` is the normalized path variation of `t -> nu_{T,t}` and

`H_T=min(a_T^(-1), log T/log log T)`, 

then a BV family has only

`M_eff(T) ≍ 1 + V_T H_T/log T`

source-distinguishable templates at the `q_T log T` rescue scale. The NB-169 estimate therefore remains valid with this effective refresh count. Under a subcritical stationary baseline, positive-density rescue forces

`V_T ≳ T a_T^2 log^3 T/(X_T^2 H_T)`.

Thus continuous adaptation is no longer a qualitative escape. The compact frontier is now split into three genuinely different possibilities: spend logarithmic capped transport, target a genuinely sparse exceptional sequence, or use very large/infinite Poisson-resolution variation. The remaining source-side question is whether a genuinely arithmetic height-selection mechanism can supply that much variation while preserving target gain, or whether an entropy/modulus argument can control families beyond bounded variation.

## Keep the source and destination currencies separate

A future sampler must expose target charge, total variation, boundary gap, ordinary Jordan transport, capped Poisson transport `T_G`, `Xi_G`, local moment order, support growth, the **Poisson-resolution height variation** of the signed template, the actual high-ordinate logarithmic-derivative input, exceptional-height density, localization radius and adverse-zero population. Persistence is a family quantifier: free switching between individually cheap templates is not itself a cheap family.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.