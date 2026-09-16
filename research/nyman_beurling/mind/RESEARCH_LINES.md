# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Leave sublogarithmically conditioned exterior samplers after boundary normalization and sublinear vertical spreading

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-032-zero-mass-poisson-cancellation-exports-an-equal-negative-lobe`.

NB-123--NB-147 classify the positive exterior-Poisson resource and its reflection-closure budget. NB-148 identifies the natural signed escape: a zero-mass exterior sampler cancels the universal Hadamard logarithm but necessarily exports equal integrated negative Poisson mass. NB-149 shows that Jordan/total-variation domination simply restores the positive logarithmic budget.

NB-150 closes the growing mesoscopic two-point horizontal route. For `1<<L_G=o(G)`, ordinary zero density fills both signs of the rescaled kernel with `Theta(log G)` actual-zero mass while a target packet inside `o(L_G)` becomes negligible.

NB-151 closes the fixed-scale loophole for the two-point geometry when the target packet itself has logarithmic rank. Horizontal differencing of `xi'/xi` gives an absolutely convergent signed sum over the actual zeros with total charge only `O(1)`. A target packet of `Omega(log G)` positive charge must therefore be balanced by `Omega(log G)` negative charge in a bounded neighboring ordinate window.

NB-152 removes the two-point restriction for fixed horizontal compact support under bounded conditioning. NB-153 removes the bounded-vertical and bounded-conditioning restrictions up to the logarithmic threshold on any fixed compact exterior set. With `C_G=V_G/q_G`, every family with `C_G=o(log G)` still exports `Omega(q_G log G)` adverse charge, a fixed fraction within ordinate radius `O(C_G)`, carried by at least `Omega(log G/C_G)` adverse zeros.

NB-154 closes the simplest moving-boundary loophole. If the sampler support may approach `Re w=0` with minimum horizontal gap `a_G`, then the Euler-product remainder and the maximum pointwise Poisson amplification both worsen by the same factor `1/a_G`. The effective condition number is

`D_G=C_G/a_G=V_G/(a_G q_G)`.

Whenever `D_G=o(log G)`, the same logarithmic sign debt survives and at least `Omega(log G/D_G)` adverse zeros are required. Boundary proximity amplifies useful and adverse/source terms together.

NB-155 now closes sublinear vertical support growth as an independent escape. Allow the support half-width `B_G` to tend to infinity with `B_G=o(G)`. The total signed zero sum is still `O_A(V_G/a_G)`, so the same `D_G=o(log G)` threshold forces `Omega(q_G log G)` adverse charge. A fixed fraction must lie inside

`|gamma-G| <= 2B_G+4+M C_G=o(G)`,

and that window contains `Omega(log G/D_G)` adverse zeros. Vertical growth below the height scale therefore changes only the **localization radius** of the compensating debt, not the conditioning threshold or forced adverse population.

The surviving exterior-sampler route must now spend at least logarithmic gap-normalized conditioning, use vertical support on a scale not covered by `B_G=o(G)`, obtain signed prime-side cancellation sharper than the absolute Euler bound, or couple directly to target-bearing Nyman/prime data before the signed zero charges are separated. Neither moving toward `Re s=1` nor letting a compact-width sampler drift through an `o(G)` vertical cloud is a new escape by itself.

## Treat reflection closure, signed conservation, boundary amplification, conditioning radius and adverse occupation as distinct currencies

Positive sampling pays the Hadamard budget. Zero-mass sampling cancels that scalar term but creates a sign debt. Jordan domination forgets location and pays the budget again. NB-150 shows mesoscopic actual-zero background fills both lobes; NB-151--NB-153 show that compact exterior sampling cannot isolate a logarithmic target packet at sublogarithmic conditioning.

NB-154 identifies the correct boundary-normalized conditioning variable `D_G=C_G/a_G`. NB-155 adds a separate transport variable `B_G`: under `B_G=o(G)`, widening the support only enlarges the window carrying the compensating charge from `O(C_G)` to `O(B_G+C_G)`. It does not improve the `D_G` threshold. A future sampler must therefore state how target charge, total variation, boundary gap and vertical diameter scale simultaneously, and how the adverse part is controlled **without** reverting to total variation or to the sublogarithmic/sublinear geometry already covered.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
