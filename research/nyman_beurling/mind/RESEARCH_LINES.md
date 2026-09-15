# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Turn source-specific recurrence visibility into a quantitatively conditioned target margin

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal` through `MI-025-the-current-zero-count-rank-budget-caps-the-fully-visible-geometric-base-alphabet`.

NB-123--NB-129 build the source-faithful recurrence/phase route and expose its amplitude cost. NB-130--NB-131 show that arbitrary formal rank can interpolate finite prefixes. NB-132 separates that formal class from genuine zeta zeros in a narrow polynomial-height regime by forcing actual-zero rank below the recurrence-visibility budget.

NB-133 blocks the obvious conditioning splice: the same numerical rank allowance and Vinogradov--Korobov radial-depth constraint permit a formal `Theta(log R)` phase cluster whose full recurrence is visible but whose normalized annihilator margin is superpolynomially small. NB-134 shows that every fixed finite family of integer bases can suffer this collapse simultaneously.

NB-135 now closes the naive growing-base repair under the same source gate. At height at most `R^A` and fixed ordinate width `W`, the current right-half zero-count budget is

`d(F) <= C_(A,W) log R + 0.24460 log log R + O(1)`,

`C_(A,W)=A(W/(4*pi)+0.10076)`.

A `q`-geometric trace supplies only `(log R)/(log q)+O(1)` recurrence depth, so full recurrence is uniformly certified only if `C_(A,W)<1/log q`. For fixed `A,W` the fully visible integer-base alphabet is finite, and even as fixed `W->0` the explicit endpoint error leaves the cap `q<exp(1/(0.10076A))`.

Inside the NB-132 regime, the live theorem must therefore obtain **more conditioned information per unit of zero-count rank** rather than more separately scalarized full recurrences. Candidate mechanisms are actual-zero arrangement/spacing, a stronger short-band rank law, a joint certificate built from growing partial traces, richer natural-grid phase geometry, or a target functional whose conditioning is not a product of the same clustered root distances. Outside the regime, especially at superpolynomial height or growing ordinate width, rank visibility itself remains open.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, natural-prefix resolution, target angle, radial depth, phase arrangement, representation count, conditioning and provenance separate

NB-128 buys local phase stability by growing the observation prefix. NB-129 shows that target visibility still costs reciprocal-height amplitude accuracy. NB-130--NB-131 show that arbitrary formal rank can defeat finite-prefix and height-blind descriptors. NB-132 shows that actual-zero counting can restore rank visibility in a concrete source-faithful regime. NB-133 shows that coarse population and horizontal-depth information leave a visible annihilator arbitrarily ill-conditioned through angular clustering. NB-134 shows that finitely many fixed phase representations can suffer that collapse simultaneously. NB-135 shows that the current zero-count gate supplies only finitely many bases on which a separate **full** recurrence is certifiably visible.

The surviving discriminator is therefore not “more views” by itself. One must state which source law limits effective rank and relative phase arrangement, how representation complexity grows with scale, whether each view contributes a full recurrence or only a partial trace, and why the final joint certificate remains conditioned after the same cluster is seen through all admitted observations.