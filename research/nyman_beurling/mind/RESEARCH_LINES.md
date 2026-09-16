# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the one-Poisson-width interlaced signed-sampler regime

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-038-block-stationary-arithmetic-rescue-is-density-sparse`.

NB-148--NB-160 show that zero-mass signed exterior sampling removes the universal Hadamard logarithm only by exporting sign debt. Mesoscopic spreading, finite atomic repair and even arbitrary signed Borel samplers with Jordan supports separated by many Poisson widths still force an adverse `Omega(log G)` zero reservoir under bounded effective conditioning.

NB-161--NB-164 isolate the opposite, finely interlaced regime. Total variation and ordinary Jordan `W_1` identify two useful source budgets but each overcharges part of the geometry: total variation ignores local cancellation, while uncapped transport keeps charging distance after the Poisson response has saturated.

NB-165--NB-166 insert the actual high-ordinate zeta source before absolute values. The verified pointwise bound and Cauchy differentiation give the scale

`E_G=min{a_G^(-1), log G/log log G}`

and the transport budget `Theta_G=C_G ell_G/a_G`, yielding signed conservation cost `O(q_G Theta_G E_G)`.

NB-167 identifies the compact metric that unifies both predecessor currencies. With truncated Poisson cost

`d_a(s,t)=min{1,|s-t|/a}`

and optimal Jordan transport mass `T_G`, define `Xi_G=T_G/q_G`. Then

`Xi_G <= (1/2) min{C_G,Theta_G}`

and the full completed conservation remainder is `O(q_G Xi_G E_G)`. The same `Xi_G` controls every Poisson response pointwise: `|Q_G(rho)|<=T_G/x_rho`, so every target zero requires `Xi_G>=x_rho`.

NB-168 attacks the remaining source-specific cancellation loophole for a **height-stationary compact template**. If one signed offset shape is translated through a dyadic block, its Euler defect satisfies

`int_T^(2T) |E_T(t)|^2 dt << T_T^2 (T+a_T^(-2))`.

Hence `q_T log T`-scale arithmetic rescue occupies relative measure

`<< Xi_T^2 (log T)^(-2) (1+(T a_T^2)^(-1))`.

In the natural regime `T a_T^2 -> infinity`, every block-stationary template with `Xi_T=o(log T)` can produce logarithmic rescue only on a density-zero set of centers. This is substantially stronger than the worst-case pointwise NB-167 threshold for persistent use: arithmetic phase alignment cannot be a block-wide mechanism unless the capped mismatch itself reaches logarithmic scale.

The compact frontier is therefore split cleanly. Persistent rescue must use a shape that adapts to height, raise `Xi_T` to logarithmic size, enter the ultra-thin `a_T \lesssim T^(-1/2)` layer where the present mean-square error ceases to be negligible, or target a genuinely sparse exceptional sequence of centers. NB-168 does **not** exclude the last possibility without a robustness interval around each selected target packet.

## Keep the source and destination currencies separate

A future sampler must expose target charge, total variation, boundary gap, ordinary Jordan transport, capped Poisson transport `T_G`, `Xi_G`, local moment order, support growth, whether the signed template is stationary or height-adaptive, the actual high-ordinate logarithmic-derivative input, exceptional-height density, localization radius and adverse-zero population. `C_G` and `Theta_G` remain useful diagnostics, but NB-167--NB-168 show that the source test class sees capped transport directly and that persistence in height is an additional quantifier not captured by a pointwise bound.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
