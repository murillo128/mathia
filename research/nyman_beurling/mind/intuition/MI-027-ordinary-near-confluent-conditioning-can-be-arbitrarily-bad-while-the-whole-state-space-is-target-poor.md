# MI-027 — Polynomial confluence cells are target-poor by total complex diameter, not internal gap geometry

**Evidence level:** exact finite-window matched-control splice from [NB-137](../../findings/NB-137-superill-conditioned-simple-clusters-can-converge-to-a-target-poor-confluent-state-space.md), made quantitatively polynomial by [NB-138](../../findings/NB-138-polynomially-tight-simple-clusters-inherit-the-target-poor-confluent-barrier.md), extended to arbitrary vertical node geometry by [NB-139](../../findings/NB-139-arbitrary-polynomial-crowding-inherits-the-target-poor-confluent-barrier.md), and extended to arbitrary two-dimensional complex zero motion by [NB-140](../../findings/NB-140-arbitrary-two-dimensional-polynomial-crowding-inherits-the-target-poor-confluent-barrier.md)

NB-136 shows that distinct simple packets can make the ordinary natural-prefix power basis superpolynomially ill-conditioned. NB-137 identifies why this cannot by itself be interpreted as target difficulty: the coordinate chart can become singular while the **entire represented state space is asymptotically irrelevant to the canonical Nyman target**.

NB-138 makes the Grassmann obstruction quantitative at polynomial spacing. For logarithmic packet rank `d_G=floor(c log G)`, if a split cluster has diameter `Delta_G` with

`Delta_G G^(c log D_a) (log G)^(25/2) -> 0`,  `D_a=4/a-3`,

then the normalized projection of the Nyman target onto the simple-state span tends to zero.

NB-139 removes all dependence on the internal vertical gap pattern. Newton divided differences span the same evaluation space, and Hermite--Genocchi comparison with the confluent jet introduces no inverse minimum-gap factor. Arbitrarily irregular pairwise-distinct nodes inside the same polynomial cell therefore inherit the target-poor limit.

NB-140 removes the remaining fixed-real-part escape. The state family is holomorphic in a **complex** displacement `z=x+iy`; `x` moves the zero ordinate and `y` moves its horizontal depth. Complex Newton divided differences give the same gap-free comparison. Hence every pairwise-distinct simple packet in the two-dimensional disk

`|z_j| <= G^(-B)`,  `B>c log D_a`,

inherits the target-poor confluent barrier, independently of direction, anisotropy, ordering and internal pairwise gaps. In physical zero coordinates, both `Re rho` and `Im rho` may vary by `O(G^-B)`.

The correct geometric variable is therefore the **total complex diameter of the confluence cell together with its logarithmic occupancy**, not a nearest-neighbour gap, vertical alignment or the condition number of one coordinate chart. Passing to divided-difference/jet coordinates can regularize the representation without creating target occupation; allowing small horizontal motion does not escape the same target-poor Grassmann neighborhood.

The matched coarse source controls still do not exclude `Theta(log G)` formal right-half points inside such a two-dimensional polynomial cell. A source-side repair must therefore forbid that local complex occupancy for actual zeta zeros, or directly force target-bearing projection despite it. Average spacing, occasional gaps, nonvertical geometry or basis stabilization are secondary unless they change this representation-invariant subspace statement.

**Boundary.** NB-137--NB-140 are matched finite-window constructions compatible with coarse zero-count/zero-free envelopes, not assertions that actual zeta zeros realize these clusters. The polynomial threshold is sufficient rather than claimed sharp. Small target projection of one packet does not prove the full Nyman distance is large; it isolates the source law that the current representation lacks.