# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Change source resource beyond positive exterior Poisson sampling

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-031-euler-product-poisson-mass-is-a-local-confluence-budget`.

NB-123--NB-143 separate recurrence visibility, conditioning, target occupation and generic xi-type realizability. NB-144 then supplies a genuinely arithmetic local discriminator: for a polynomially small right-half packet centered at `beta=1-epsilon`, the Euler-product half-plane plus zero-side Poisson positivity gives

`d_G <= (epsilon(1-epsilon)/2+o(1)) log G`,

and gives `d_G=o(log G)` in the moving near-one regime `epsilon_G->0`, `epsilon_G log G->infinity`.

The withdrawn NB-145 overstated the endpoint of the associated minimax theorem by counting a reflected zero as distinct at the critical line. NB-146 corrects the orbit bookkeeping. For packets separated from `Re s=1/2`, arbitrary positive exterior sampling with only Poisson positivity and the pointwise absolute Euler-product majorant cannot beat the NB-144 coefficient; one sample already attains it. At a symmetric critical-line-centered packet, however, reflection is self-dual or already inside the count, and the exact positive-sampling floor is instead `1/4 log G`. The formal off-line limit `1/8 log G` does not extend to that boundary.

The fixed-interior problem is therefore still outside the positive cone, but the boundary regime must be stated correctly. A new theorem must use a different source resource: signed/oscillatory combinations with controlled zero-side indefiniteness, prime-side cancellation/correlation beyond the pointwise majorant, a stronger local moment or pair law, or a theorem forcing every surviving actual packet to be Nyman-target-bearing.

## Keep separated reflection orbits and self-dual packets distinct

Positive-Poisson occupancy is an orbit-counting argument as well as a kernel estimate. A right-half packet separated from the line can charge the positive mass of a distinct reflected partner without increasing the packet count; a line-centered symmetric packet cannot. Any interpolation toward the critical line must therefore track whether the reflected zero remains outside the counted cell. Kernel continuity alone does not justify continuity of the resulting occupancy coefficient.

## Push canonical shell discrepancy independently

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate being targeted. This route is distinct from the zero-packet Poisson budget above.