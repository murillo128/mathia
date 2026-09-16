# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Leave sublogarithmically conditioned exterior samplers after boundary normalization and vertical spreading

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-032-zero-mass-poisson-cancellation-exports-an-equal-negative-lobe`.

NB-123--NB-147 classify the positive exterior-Poisson resource and its reflection-closure budget. NB-148 identifies the natural signed escape: a zero-mass exterior sampler cancels the universal Hadamard logarithm but necessarily exports equal integrated negative Poisson mass. NB-149 shows that Jordan/total-variation domination simply restores the positive logarithmic budget.

NB-150 closes the growing mesoscopic two-point horizontal route. For `1<<L_G=o(G)`, ordinary zero density fills both signs of the rescaled kernel with `Theta(log G)` actual-zero mass while a target packet inside `o(L_G)` becomes negligible.

NB-151 closes the fixed-scale loophole for the two-point geometry when the target packet itself has logarithmic rank. Horizontal differencing of `xi'/xi` gives an absolutely convergent signed sum over the actual zeros with total charge only `O(1)`. A target packet of `Omega(log G)` positive charge must therefore be balanced by `Omega(log G)` negative charge in a bounded neighboring ordinate window.

NB-152 removes the two-point restriction for fixed horizontal compact support under bounded conditioning. NB-153 removes the bounded-vertical and bounded-conditioning restrictions up to the logarithmic threshold on any fixed compact exterior set. With `C_G=V_G/q_G`, every family with `C_G=o(log G)` still exports `Omega(q_G log G)` adverse charge, a fixed fraction within ordinate radius `O(C_G)`, carried by at least `Omega(log G/C_G)` adverse zeros.

NB-154 closes the simplest moving-boundary loophole. If the sampler support may approach `Re w=0` with minimum horizontal gap `a_G`, then the Euler-product remainder and the maximum pointwise Poisson amplification both worsen by the same factor `1/a_G`. The effective condition number is `D_G=C_G/a_G=V_G/(a_G q_G)`. Whenever `D_G=o(log G)`, the same logarithmic sign debt survives.

NB-155 closes sublinear vertical support growth as an independent escape. Allow the support half-width `B_G` to tend to infinity with `B_G=o(G)`. A fixed fraction of the compensating adverse charge remains inside `|gamma-G|=O(B_G+C_G)`, so vertical spreading changes the localization radius but not the `D_G` conditioning threshold.

NB-156 now crosses the macroscopic-support boundary. For `B_G<G` with lowest sampled ordinate `H_G=G-B_G -> infinity`, completed-function conservation introduces the extra Gamma-profile tariff

`E_G = D_G + C_G log(G/H_G)`.

If `E_G=o(log G)`, the same `Omega(q_G log G)` adverse charge persists; a fixed fraction lies in `|gamma-G| <= B_G+O(C_G+1)`, and the window still contains `Omega(log G/D_G)` adverse zeros. Thus `B_G/G` may approach a positive constant, or even `1`, without creating an escape as long as the sampler does not descend so far that the logarithmic Gamma variation itself spends the missing budget. The relevant vertical resource is the logarithmic depth `log(G/H_G)`, not the coarse distinction `B_G=o(G)` versus `B_G asymp G`.

The surviving exterior-sampler route must therefore spend at least logarithmic **combined** budget `E_G`, descend toward ordinates where `H_G` no longer tends to infinity and a genuinely different completed-function regime begins, obtain signed prime-side cancellation sharper than the absolute Euler bound, or couple directly to target-bearing Nyman/prime data before the signed zero charges are separated. Moving toward `Re s=1`, widening through a sublinear cloud, or occupying a macroscopic fraction of height is not a new escape by itself.

## Treat reflection closure, signed conservation, boundary amplification, vertical Gamma variation, conditioning radius and adverse occupation as distinct currencies

Positive sampling pays the Hadamard budget. Zero-mass sampling cancels that scalar term but creates a sign debt. Jordan domination forgets location and pays the budget again. NB-150 shows mesoscopic actual-zero background fills both lobes; NB-151--NB-153 show that compact exterior sampling cannot isolate a logarithmic target packet at sublogarithmic conditioning.

NB-154 identifies the boundary-normalized conditioning variable `D_G=C_G/a_G`. NB-155 separates vertical transport `B_G` from conditioning below the height scale. NB-156 refines that transport further: once the cloud becomes macroscopic, the completed Gamma background charges `C_G log(G/H_G)` according to the lowest sampled ordinate. A future sampler must therefore state how target charge, total variation, boundary gap, vertical diameter and lowest ordinate scale simultaneously, and how the adverse part is controlled **without** reverting to total variation or spending the logarithmic Gamma tariff implicitly.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
