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

Conversely, when `X_T=o(log T)`, positive-density rescue requires at least `M_T ≳ T a_T^2 log^2 T/X_T^2` template changes. The former escape “adapt the shape with height” is therefore no longer qualitative: adaptation must cross an explicit refresh-rate threshold relative to the Poisson width.

The compact frontier is now split into three genuinely different possibilities. A mechanism may spend logarithmic capped transport, target a genuinely sparse exceptional sequence, or use adaptation whose switching/variation complexity reaches the critical refresh scale. The next source-side question is to replace piecewise switching by a continuously varying family and identify a bounded-variation/entropy quantity whose mean-square bill reduces to the NB-169 refresh term on step functions.

## Keep the source and destination currencies separate

A future sampler must expose target charge, total variation, boundary gap, ordinary Jordan transport, capped Poisson transport `T_G`, `Xi_G`, local moment order, support growth, the **height-adaptation complexity** of the signed template, the actual high-ordinate logarithmic-derivative input, exceptional-height density, localization radius and adverse-zero population. Persistence is a family quantifier: free switching between individually cheap templates is not itself a cheap family.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.