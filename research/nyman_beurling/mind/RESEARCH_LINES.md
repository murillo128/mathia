# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Force target-bearing geometry, not merely visibility or a well-conditioned coordinate chart

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal` through `MI-027-ordinary-near-confluent-conditioning-can-be-arbitrarily-bad-while-the-whole-state-space-is-target-poor`.

NB-123--NB-132 build the source-faithful recurrence/phase route and show that actual zero counting can put a narrow polynomial-height packet below a recurrence-visibility rank budget. NB-133--NB-136 then separate visibility, representation supply and conditioning: matched clustered packets can make scalar annihilators, finitely many geometric bases, and even the full natural-prefix evaluation matrix superpolynomially ill-conditioned under the same coarse source envelopes.

NB-137 shows that ordinary conditioning is still not the endpoint quantity. A simple cluster may converge in the Grassmannian to a confluent jet state space while its raw power-basis condition number becomes arbitrarily worse, yet the **whole state span** has vanishing normalized projection of the canonical Nyman target. Divided-difference/confluent coordinates can remove a chart singularity without creating target relevance.

NB-138 makes that obstruction quantitative at an ordinary polynomial scale. For logarithmic packet rank, the split simple-state space already inherits the target-poor confluent limit when `epsilon_G=G^(-B)` with fixed `B>c log(4/a-3)`, while the ordinary natural-prefix matrix can still have `log kappa_2(V_G) >= (cB+o(1))(log G)^2`.

NB-139 removes the remaining equal-spacing artifact. For arbitrary pairwise-distinct nodes inside a cell `|h_j|<=Delta_G`, Newton divided differences and the Hermite--Genocchi formula compare the **subspace itself** with the confluent jet space without any inverse minimum-gap factor. If

`Delta_G G^(c log(4/a-3)) (log G)^(25/2) -> 0`,

then the normalized target projection still tends to zero. In particular every arbitrary simple packet inside `|h_j|<=G^(-B)` with `B>c log(4/a-3)` inherits the target-poor barrier, no matter how irregular or tiny its internal gaps are. The relevant geometric parameter is the total cluster diameter, not an adjacent-gap pattern or a preferred Vandermonde chart.

Inside the same coarse zero-count/zero-free envelope, `Theta(log G)` formal right-half points can still fit in such a polynomially shrinking cell. The live theorem must therefore constrain a target-bearing invariant of the **actual** zero packet: a source law forcing at most `o(log G)` relevant occupancy in every forbidden polynomial confluence cell, a direct lower bound on target projection, coefficient occupation of target-bearing singular sectors, or another representation whose margin is defined directly against the Nyman target. Proving merely that zeros are not equally spaced, controlling one minimum gap, or stabilizing a coordinate basis does not address NB-139.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, translation resolution, coordinate conditioning, subspace geometry and target occupation separate

NB-128 buys local resolution for one common phase translation by growing the natural prefix. NB-132 restores rank visibility in a concrete actual-zero regime. NB-133--NB-136 show that those facts do not give a conditioned packet representation. NB-137 shows that catastrophic raw conditioning can coexist with a well-defined confluent subspace that is simply target-poor; NB-138 places that separation at explicit polynomial spacing; NB-139 shows that even the internal spacing geometry can be arbitrary once the whole packet lies in the relevant polynomial cell.

The surviving discriminator is representation-invariant. A proposal must state which subspace or quotient is physically meaningful, how the actual target occupies it, what **cluster-scale** source law prevents that occupation from vanishing, and why the law applies to the actual zeta packet rather than only to a chosen coordinate chart. Numerical conditioning of one basis, average-gap information, or a spacing lower bound that still permits logarithmic occupancy of the polynomial confluence cell is secondary unless it changes the target-bearing state geometry.
