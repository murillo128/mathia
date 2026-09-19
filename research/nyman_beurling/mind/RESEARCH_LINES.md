# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Replace separable population/depth/phase control by genuinely joint residue information

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-060-fixed-power-phase-cancellation-is-not-enough-at-the-ford-boundary`.

NB-218--NB-224 isolate the exact source-side carrier. Keeping source and Mellin kernel coupled removes artificial primitive tariffs; generic strip analyticity is sharp for the ambient class; the actual zeta singularity spectrum plus Bellotti density reaches almost to Ford height; and a proportional logarithmic source shell narrows the vertical carrier enough to reach the exact Ford denominator.

NB-225 proves that the linear shell width is the sharp transition for the current **population-only** mechanism. Every genuinely sublinear `H=o(R)` permits an abstract near-one packet compatible with the zero-free, density and local-count inputs while retaining an order-one moving-shell contribution.

NB-226 shows that an unweighted fixed-power phase theorem does not repair this. For every fixed `0<vartheta<1`, the packet can satisfy `O(m^vartheta)` cancellation on every consecutive vertical subpacket and move horizontally until the Ford damping `e^(-YD)` compensates the allowed phase bias.

NB-227 closes a much broader separable repair. Even if the raw phase estimate is strengthened by an arbitrary predetermined depth-only factor,

`|sum_I e^(iX(gamma-t))| << 1 + |I|^vartheta/Q(D)`,

with `Q(D)` finite at every fixed depth, the packet can choose a depth `D=D(M)->infinity` slowly enough that `Q(D)e^(YD) <= M^(vartheta/2)`, distribute a bias of size `~e^(YD)` across the packet, satisfy the strengthened bound on every consecutive subpacket, and still leave an order-one residue after horizontal damping. No fixed depth-only penalty multiplying a fixed positive population power can therefore control the exact-Ford sublinear-shell regime uniformly.

The live source-side question is now sharper: the missing theorem must couple population, horizontal depth and phase **nonseparably**, remove the admissible population as depth changes, constrain nested depth slabs jointly, or control the actual residue-weighted sum directly. A theorem of the schematic form `M^vartheta/Q(D)` is insufficient no matter how fast the fixed function `Q` grows.

## Keep source width, population, depth and weighted phase as separate currencies

The relevant currencies include logarithmic source width `H`, carrier width `1/H`, local zero population, normalized horizontal depth `D`, raw phase bias, the damping `e^(-YD)`, residue weights and the norm in which cancellation is asserted. NB-225--NB-227 show that these cannot be optimized independently and then multiplied after the fact.

A future source-side improvement must therefore state a joint admissible region in `(M,D)` or act on the weighted residues themselves. A depth-sensitive theorem is not useful merely because it becomes arbitrarily strong for each fixed `D`: the matched control can let `D` diverge on a diagonal slower than that fixed-depth strengthening becomes effective relative to the available population.

This remains source-side information. The matched packets are logical controls compatible with the audited zero information, not constructions of actual zeta zeros, and the results do not by themselves give a quantitative Nyman--Beurling distance theorem. Any destination claim must preserve that bridge explicitly.
