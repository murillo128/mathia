# VIS-017 — overlap connectivity collapses local phase freedom

## Claim

Let `D_1,...,D_m` be disks and let `F` and `G` be holomorphic on neighborhoods of their closures. Assume that on every `D_j`:

1. `F` and `G` have exactly the same zeros, with the same multiplicities;
2. neither function has a zero on `partial D_j`; and
3. `|F|=|G|` on `partial D_j`.

Then there is one unimodular constant for each connected component of the disk-overlap graph. More precisely, if vertices `i,j` are adjacent when `D_i intersect D_j` is nonempty, then for every overlap-graph component `C` there is a constant `c_C` with `|c_C|=1` such that

`F = c_C G`

on every disk belonging to `C`.

In particular, if the overlap graph is connected, **all local phase ambiguities glue to a single global phase**. Conversely, if the union has `k` disconnected overlap components and no additional bridge data are supplied, the local zero-set plus boundary-modulus data leave exactly `k` independent `U(1)` phase factors.

**Evidence/status:** `CLASSICAL-COMPLEX-ANALYSIS + EXACT-DERIVED + DECISIVE-NEGATIVE/BASELINE`.

This is an elementary gluing consequence of the single-disk uniqueness statement in `VIS-016`; no novelty is claimed for the underlying identity theorem or maximum-modulus argument. The Mathia consequence is that merely moving from one center to an overlapping atlas of centers does not create a new phase-information channel.

## Exact derivation

Apply `VIS-016` on each disk `D_j`. Its hypotheses give a constant `c_j` with `|c_j|=1` such that

`F = c_j G`

throughout `D_j`.

Suppose `D_i` and `D_j` overlap. Their intersection is open. Because a nonzero holomorphic function has isolated zeros, there is a point `w` in the overlap with `G(w) != 0`. At that point,

`c_i G(w) = F(w) = c_j G(w)`,

so `c_i=c_j`.

Equality therefore propagates along every path in the overlap graph. All disks in one connected graph component share one phase constant. If the graph is connected, one constant works on the entire covered region.

The converse is also sharp at the level of the supplied local data. If the covered region splits into `k` disconnected overlap components, independently multiplying the function on component `C_l` by an arbitrary unimodular constant `exp(i alpha_l)` changes neither its local zero sets nor any boundary modulus. Without data coupling distinct components, those relative phases cannot be recovered from the local disk records alone.

Thus the residual phase freedom has dimension exactly equal to the number of connected components of the overlap graph, not the number of centers.

## What this closes

A natural escape after `VIS-016` was to hope that several local phase/domain-coloring portraits might carry extra information through their relative alignment. Overlap itself does not provide such a carrier. On every nonempty overlap the two local phase gauges must agree, and connected overlaps reduce the entire atlas to the same one-dimensional global `U(1)` ambiguity already present in a single disk.

Consequently, the following do not create a new invariant when the complete local zero sets and boundary moduli are already retained:

- adding more centers whose disks form a connected overlap cover;
- aligning domain-coloring hue across those overlaps;
- comparing unwrapped local phases after the common zero factors are removed;
- propagating phase through chains of overlapping regular disks.

The correct information accounting is topological but elementary: **one phase gauge per connected overlap component**.

## Visual inspection

The retained artifact

`research/visual_exploration/visualizations/overlap-cover-phase-gluing.md`

shows the two exact combinatorial regimes. In the connected three-disk cover, pairwise overlap paths force all local constants to coincide. In the disconnected cover, two overlap components leave two independent local phases because no supplied datum bridges them.

The image is explanatory only. The finding is proved by the exact single-disk uniqueness theorem plus equality on overlaps.

## Prior art and novelty assessment

The mathematics is classical. `VIS-016` already reduces each disk to one unimodular ambiguity using the maximum-modulus principle. Equality of those constants on a nonempty overlap is an immediate application of ordinary holomorphic uniqueness: two formulas for the same holomorphic field must agree wherever both are defined, and a nonzero holomorphic denominator cannot vanish on an open overlap.

This is also the elementary scalar form of a familiar gluing/gauge principle: local representatives differing by constants have transition constants, and connected overlap consistency collapses them to one global constant. No new theorem of sheaf theory, analytic continuation, or phase retrieval is claimed.

The durable contribution is the negative-control specialization for Mathia's visual program. It removes **overlap-connected multi-center phase alignment** from the list of candidate independent channels after the local zero and boundary-modulus data have already been counted.

## Boundary conditions and falsification

The result requires the full hypotheses used disk by disk in `VIS-016`: complete interior zero multisets with multiplicity, full boundary modulus, no boundary zeros, and holomorphic regularity across each closed disk.

Disconnected local patches deserve careful interpretation. If `F` is known a priori to be one global entire function on a larger connected domain, analytic continuation through the omitted region does of course relate the patches. The statement here is narrower: **the retained local data on a disconnected union do not themselves contain that bridge**. Recovering the relative phase then requires additional information from the connecting region or another observable.

Likewise, sparse boundary samples, incomplete zero data, noisy phase retrieval, non-holomorphic observables, monodromy on non-simply-connected domains, or matrix/vector-valued fields are outside the claim.

Most importantly, the theorem says nothing about higher-order statistics of the zero configuration itself. Cross-center observables that depend on genuinely source-specific relations among zeros, rather than on redundant reconstruction of the same holomorphic field, remain live.

## Research consequence

The accepted multiscale clue has now lost another apparent escape. `VIS-013`–`VIS-015` classify complete concentric log-modulus shells as zero sources plus harmonic boundary data. `VIS-016` shows that adding phase on one regular disk contributes only one global constant. `VIS-017` shows that adding **overlapping centers** contributes no further phase degrees of freedom once the cover is connected.

A future cross-center visual candidate must therefore identify information not reconstructible from the same locally complete holomorphic data. The live directions are sharper:

- source-sensitive statistics of the zero configuration tested against matched point processes;
- explicitly incomplete or separated-region bridge observables whose missing coupling is itself measurable;
- relations among several centers that depend on more than gluing one underlying holomorphic field;
- non-holomorphic or higher-order constructions with a clear source-specific residual.

Merely replacing one disk by a connected overlapping atlas, or treating phase alignment across that atlas as a new signal, is now closed as an independent route.
