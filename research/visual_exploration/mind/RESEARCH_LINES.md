# Visual-exploration research lines

This file records current mathematical questions for the visual-exploration line. It is a mutable synthesis, not a task queue or history.

## Keep Wang branchwise occupancy closed and return to the fixed-power source arithmetic

**Linked intuition:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`.

VIS-317--VIS-324 identify faithful unimodular Wang coordinates, reduce frozen branches to fixed-gap affine runs and close polynomially long first-level runs with the classical two-linear-form Selberg upper-bound sieve. VIS-325--VIS-328 then show how center-gap renormalization and short Diophantine vectors control the maximally fragmented regime.

VIS-329 removes the center-gap split from the load-bearing upper bound. Working directly with the original period `m=max(u,v)`, the approximation lattice

`Lambda_(c,m)={(s,e): e=cs (mod m)}`

has determinant `m`, so Minkowski supplies `s,|e|=O(sqrt(m))`. An `s`-step has one fixed nondegenerate Wang displacement except at at most `|e|` edges; deleting those edges leaves at most `s+|e|` affine runs, while the same short vector controls the two-form resultant and conductor. At the natural window `L asymp M/log log M`, the classical Selberg upper-bound sieve gives

`P_j << L (log log M)^2/log^2 M`

uniformly in the center gap `k=|u-v|`. Thus `A_M=O((log log M)^2)` throughout the original subperiod regime `L<m`, inside the taper budget isolated by VIS-316.

The moving-upper simultaneous-prime occupancy channel is therefore no longer a live branchwise obstruction at the required upper-bound scale. The former transition `k<=L`, `k=M^(1-o(1))` was an artifact of an intermediate denominator-`k` representation, not a surviving obstruction of the original candidate set.

The live question is now the distinct fixed-power source route already isolated in the accepted Wang clue: is there a real-axis property of the squared-von-Mangoldt source measure that is strictly weaker than the RH-equivalent half-plane pole exclusion of VIS-293, yet quantitatively strong enough to improve the complete Wang source budget at the natural window? Any such gain must survive the source, gamma, localization, cross-term and moving-upper bookkeeping rather than reopen a branchwise occupancy regime already closed by VIS-329.

## Keep source arithmetic, occupancy closure and the final Wang destination distinct

Direct original-period decimation is a representation simplification with a real quantitative consequence: it preserves the two-prime sieve dimension while simultaneously controlling packet length, exceptional edges and arithmetic conductor. It does not produce a prime-pair asymptotic, lower bound or full Wang theorem.

Future work should therefore treat the moving-upper occupancy estimate as an available input and concentrate on the unresolved source-sensitive fixed-power term or on a genuinely later global bookkeeping obstruction. Center-gap/Christoffel refinements remain mathematically useful structure, but they should not be promoted back to the critical path without identifying a flaw in VIS-329 or a destination quantity not controlled by the VIS-316 excess criterion.