# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Change source resource beyond positive exterior Poisson sampling

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-031-euler-product-poisson-mass-is-a-local-confluence-budget`.

NB-123--NB-143 separate recurrence visibility, conditioning, target occupation and generic xi-type realizability. NB-144 supplies a genuinely arithmetic local discriminator: for a polynomially small right-half packet centered at `beta=1-epsilon`, the Euler-product half-plane plus zero-side Poisson positivity gives the sharp separated-packet coefficient, and in the moving near-one regime it yields `o(log G)` occupancy.

NB-146 corrected the reflection-orbit bookkeeping at the critical line. NB-147 now closes the arbitrary tight interior packet geometry by identifying the exact invariant: the **reflection closure** `Chat=C union J(C)`. Positive exterior Poisson sampling with only the pointwise absolute Euler-product majorant yields

`sum_(rho in Chat) 1/(1-Re rho) <= (1/2+o(1)) log G`,

and one exterior sample asymptotically saturates this bound. Thus the whole positive-sampling architecture is minimax-classified by the weighted reflection closure, not by the packet center.

For near-critical packets, if `d_G=|C_G|` and `b_G` counts packet occurrences whose reflected partner is absent, the closure law becomes

`d_G+b_G <= (1/4+o(1)) log G`.

Writing `q_G=b_G/d_G`, the packet coefficient is `1/[4(1+q_G)]`: `1/4` for reflection-saturated/self-dual packets, `1/8` for fully one-sided packets, and a continuous interpolation between them. The apparent boundary jump of NB-146 was therefore a change in orbit exposure, not a discontinuity of the Poisson kernel.

The fixed-interior problem remains outside the positive cone. A new theorem must use a different source resource: signed/oscillatory combinations with controlled zero-side indefiniteness, prime-side cancellation/correlation beyond the pointwise majorant, higher local moments/pair laws, or a theorem forcing every surviving reflection-saturated packet to be Nyman-target-bearing.

## Treat reflection closure, not packet center, as the occupancy currency

Any packet approaching the critical line must track which functional-equation partners are already included. Near maximal `1/4 log G` occupancy forces `b_G=o(log G)`, so a nearly saturated packet is itself nearly reflection-saturated. This is useful structure, but it still allows `Theta(log G)` local zero packets and does not supply target coercivity.

Future local zero arguments should therefore formulate their positive Poisson budget on the closure before comparing geometries. Adding more positive exterior samples cannot improve that weighted invariant; any stronger occupancy theorem must leave the classified proof cone.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route is distinct from the zero-packet Poisson budget above.