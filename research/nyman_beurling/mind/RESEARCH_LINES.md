# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, while NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun. NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale, and NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

The unresolved operator transition lies in the genuinely intermediate window `N<<m<=O(N^2)`: determine whether coherent centered shell modes survive there or whether the rank-one mixing picture can be pushed down to that scale. That source-side theorem is still not the destination theorem. Any useful singular direction must also be occupied by the actual moving first-free datum after the sampling/null decomposition, lower-section conditioning and off-critical contraction. Operator norm or support mass alone does not imply a Nyman target gain.

## Close the primitive lower-bound gap in the Hilbert norm, not in the Cesaro shell count

NB-316--NB-317 isolate the multiplicative loss in the centered primitive estimate more sharply. For the centered Cesaro shell factor `D_N`, NB-317 proves the sharp growth

`||D_N||_2^2 = Theta(N^3)`, hence `||D_N||_2 = Theta(N^(3/2))`.

The first multiplicative factor is therefore no longer a loose coefficient-count artifact. The remaining gap in the primitive lower-bound route is entirely in the comparison between the oscillatory shell energy and the actual Hilbert norm of the corresponding `H_(N,a)` object. Tightening the raw coefficient count of `D_N`, or replacing it by another estimate with the same shell information, cannot close that gap.

The live question is to identify the **phase-space or window-incidence geometry that controls `||H_(N,a)||_2` relative to the sharp shell energy**, uniformly in the regime consumed by the final theorem. A successful estimate must exploit genuine Hilbert-space cancellation or concentration; an argument that only improves scalar shell bookkeeping is now excluded by the sharp `N^(3/2)` factor.
