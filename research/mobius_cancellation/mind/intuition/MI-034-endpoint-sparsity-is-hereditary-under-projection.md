# MI-034 — Endpoint sparsity is hereditary, but low-cost source cuts cannot beat the half-occupancy barrier

**Evidence level:** exact endpoint-projection/source-complexity obstruction from [MC-307](../../findings/MC-307-hereditary-endpoint-projection-polynomial-source-cost.md), dualized by [MC-308](../../findings/MC-308-dual-source-cut-endpoint-occupancy.md), and sharply restricted in the low-source-cost regime by [MC-309](../../findings/MC-309-landau-page-half-occupancy-low-cost-source-cuts.md)

MC-307 shows that the one-defect endpoint law remains exponentially sparse after forgetting selected **target coordinates**. For any `k` retained endpoint functionals, at most the all-minus cell and the `k` one-defect cells survive. If `P_I` is the common radical of minimum lower-prime representatives for those directions, Brun--Titchmarsh forces

`P_I >= y^(1-(2+o(1))(k+1)/2^k)e^(-O(1))`.

So source complexity cannot be supplied only in aggregate by many cheap almost-disjoint coordinates: it must survive restriction to small endpoint subfamilies.

MC-308 identifies the dual invariant when one instead forgets **source primes**. Attach to each source prime `p` its incidence column `a_p in F_2^k`. For a retained source set `J`, quotient the endpoint space by the span of the omitted source columns. If the quotient has dimension `t_J` and the images of `0,e_1,...,e_k` occupy `h_J` distinct states, then the exact endpoint occupies the fraction

`h_J / 2^(t_J)`

of source-sign assignments modulo `P_J=prod_(p in J)p`. Brun--Titchmarsh gives

`P_J >= y^(1-(2+o(1)) h_J/2^(t_J)) e^(-O(1))`.

MC-309 shows that the tempting next move — find a low-product source cut with large quotient rank but occupancy below one half — is blocked by the same low-cost character theory that underlies Landau--Page. When `P_J` lies below the Landau--Page source threshold, every nonzero quotient frequency except at most one exceptional mode has bias `epsilon_y << (log y)^-2`. Parseval then forces essentially full occupancy if no exceptional mode occurs and, in general, at least half occupancy whenever `2^(t_J) epsilon_y=o(1)`. In particular this covers `2^(t_J)=o((log y)^2)`, including the logarithmic-size quotient relevant to the critical-rank window.

That half-occupancy threshold is exactly where the MC-308 Brun--Titchmarsh exponent loses positivity. A single uncontrolled Fourier mode can support the sharp index-two obstruction, so the argument cannot be repaired by a better triangle inequality inside the same low-product/moderate-rank regime.

The two-sided hereditary principle therefore survives but its useful source-cut regime is narrower than MC-308 alone suggested. A closing theorem must force at least one genuine escape: a retained source product beyond the Landau--Page band, quotient dimension large enough to outrun the low-bias estimate, stronger simultaneous cancellation that also controls the exceptional mode, or additional incidence structure that converts the half-occupancy boundary into a contradiction by another route.

**Boundary.** These are necessary restrictions on the exact one-defect endpoint partition, not an impossibility theorem for the actual Legendre incidence system. MC-309 does not identify the exceptional mode, rule out high-product cuts, or prove Möbius cancellation; it closes the specific low-source-cost moderate-rank source-cut route to a positive MC-308 exponent.