# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Leave compact sublogarithmically conditioned exterior samplers after boundary normalization

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-032-zero-mass-poisson-cancellation-exports-an-equal-negative-lobe`.

NB-123--NB-147 classify the positive exterior-Poisson resource and its reflection-closure budget. NB-148 identifies the natural signed escape: a zero-mass exterior sampler cancels the universal Hadamard logarithm but necessarily exports equal integrated negative Poisson mass. NB-149 shows that Jordan/total-variation domination simply restores the positive logarithmic budget.

NB-150 closes the growing mesoscopic two-point horizontal route. For `1<<L_G=o(G)`, ordinary zero density fills both signs of the rescaled kernel with `Theta(log G)` actual-zero mass while a target packet inside `o(L_G)` becomes negligible.

NB-151 closes the fixed-scale loophole for the two-point geometry when the target packet itself has logarithmic rank. Horizontal differencing of `xi'/xi` gives an absolutely convergent signed sum over the actual zeros with total charge only `O(1)`. A target packet of `Omega(log G)` positive charge must therefore be balanced by `Omega(log G)` negative charge in a bounded neighboring ordinate window.

NB-152 removes the two-point restriction for fixed horizontal compact support under bounded conditioning. NB-153 removes the bounded-vertical and bounded-conditioning restrictions up to the logarithmic threshold on any fixed compact exterior set. With `C_G=V_G/q_G`, every family with `C_G=o(log G)` still exports `Omega(q_G log G)` adverse charge, a fixed fraction within ordinate radius `O(C_G)`, carried by at least `Omega(log G/C_G)` adverse zeros.

NB-154 closes the simplest moving-boundary loophole. If the sampler support may approach `Re w=0` with minimum horizontal gap `a_G`, then the Euler-product remainder and the maximum pointwise Poisson amplification both worsen by the same factor `1/a_G`. The effective condition number is therefore

`D_G=C_G/a_G=V_G/(a_G q_G)`.

Whenever `D_G=o(log G)`, the same logarithmic sign debt survives: `Omega(q_G log G)` adverse charge remains, a fixed fraction lies within ordinate radius `O(1+C_G)`, and at least `Omega(log G/D_G)` actual adverse zeros are required. Merely moving the sampler toward `Re s=1` is therefore not a new escape while it remains well-conditioned relative to the boundary amplification.

The surviving compact-sampler route must spend at least logarithmic **gap-normalized** conditioning, obtain signed prime-side cancellation sharper than the absolute Euler bound, let support diameter grow, or couple directly to target-bearing Nyman/prime data before the signed zero charges are separated. The threshold `D_G~log G` is only where this obstruction stops deciding the question; it is not an isolating construction.

## Treat reflection closure, signed conservation, boundary amplification, conditioning radius and adverse occupation as distinct currencies

Positive sampling pays the Hadamard budget. Zero-mass sampling cancels that scalar term but creates a sign debt. Jordan domination forgets location and pays the budget again. NB-150 shows mesoscopic actual-zero background fills both lobes; NB-151--NB-153 show that compact exterior sampling cannot isolate a logarithmic target packet at sublogarithmic conditioning.

NB-154 adds a calibration rule for boundary approach. The raw ratio `C_G=V_G/q_G` is no longer the correct currency when the horizontal gap shrinks; both useful charge and worst-case source/adverse amplification scale against `a_G`. The invariant obstruction variable is `D_G=C_G/a_G`. A future boundary sampler must therefore state not only that `a_G->0`, but how its useful target charge, total variation and signed Euler remainder scale after this normalization.

A future signed sampler must state which conservation identity it uses, how much coefficient variation it spends relative to target charge and boundary gain, and how the adverse part is controlled **without** reverting to total variation or to a compact sublogarithmically gap-conditioned geometry already covered above. The logarithmic `D_G` threshold is a necessary escape scale for this argument, not evidence that an isolating sampler exists there.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route remains distinct from the zero-packet Poisson budgets above.
