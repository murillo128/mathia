# MI-027 — Polynomially near-confluent simple clusters are target-poor by total diameter, not by their internal gap pattern

**Evidence level:** exact finite-window matched-control splice from [NB-137](../../findings/NB-137-superill-conditioned-simple-clusters-can-converge-to-a-target-poor-confluent-state-space.md), made quantitatively polynomial by [NB-138](../../findings/NB-138-polynomially-tight-simple-clusters-inherit-the-target-poor-confluent-barrier.md), and extended to arbitrary internal node geometry by [NB-139](../../findings/NB-139-arbitrary-polynomial-crowding-inherits-the-target-poor-confluent-barrier.md), combining the confluent state-space geometry of NB-108--NB-111 with the simple-cluster conditioning obstruction NB-136

NB-136 shows that distinct simple packets can make the ordinary natural-prefix power basis superpolynomially ill-conditioned. NB-137 identifies why that alone cannot be interpreted as target difficulty: the bad conditioning can be a coordinate singularity that survives even when the **entire represented state space is asymptotically irrelevant to the canonical Nyman target**.

NB-137 originally used an existentially small split spacing to make the simple cluster Grassmann-close to its confluent jet space. NB-138 removes that escape for an equally spaced packet. For logarithmic packet rank `d_G=floor(c log G)`, a uniform holomorphic tube and Laguerre-normalized coercivity give an explicit perturbation bound. If

`epsilon_G G^(c log D_a) (log G)^(25/2) -> 0`,  with `D_a=4/a-3`,

then the normalized projection of the Nyman target onto the split simple-state span tends to zero. In particular fixed polynomial spacing `epsilon_G=G^(-B)` with `B>c log D_a` already inherits the target-poor confluent limit.

NB-139 shows that equal spacing is not load-bearing either. Let the `d_G` simple nodes be arbitrary and pairwise distinct inside `|h_j|<=Delta_G`. Newton divided differences span exactly the same simple-state space as the original evaluations, while the Hermite--Genocchi formula represents each divided difference as an average of the corresponding derivative over the convex hull of the nodes. This yields a direct subspace perturbation estimate with **no reciprocal minimum-gap factor**. Under

`Delta_G G^(c log D_a) (log G)^(25/2) -> 0`,

the full simple-state span remains target-poor. Thus every arbitrary simple packet inside the polynomial cell `|h_j|<=G^(-B)`, `B>c log D_a`, inherits the same barrier even if its adjacent gaps are wildly nonuniform or much smaller than the cell diameter.

The correct geometric variable is therefore the **diameter of the whole confluence cell together with its logarithmic occupancy**, not raw Vandermonde conditioning and not a nearest-neighbour gap statistic. Passing to divided-difference or jet coordinates can regularize the chart while leaving the represented subspace target-poor; changing the internal node pattern cannot help while the packet remains inside the same target-poor Grassmann neighborhood.

The matched zero-count control also survives this strengthening. The coarse right-half zero-count and zero-free-region laws used by the line do not exclude `Theta(log G)` formal right-half points in a polynomially shrinking vertical cell. A source-side repair must therefore prevent that **local occupancy** for the actual zeta zeros, or directly force nonvanishing target occupation despite it. Occasional large gaps, average-spacing information, non-equal spacing, or a better-conditioned coordinate system do not answer the quantified obstruction.

**Boundary.** NB-137--NB-139 are matched finite-window constructions under coarse zero-count/zero-free envelopes, not assertions that actual zeta zeros form such polynomial clusters. The threshold `B>c log D_a` is sufficient rather than claimed sharp, and small target projection of one packet does not prove the full Nyman distance is large. The result isolates the missing source law: exclude logarithmic occupancy of the relevant polynomial confluence cells or supply target-bearing information not captured by the current state span.
