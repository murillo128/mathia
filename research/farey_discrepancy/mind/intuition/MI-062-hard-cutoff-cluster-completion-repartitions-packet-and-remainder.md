# MI-062 — Hard-cut cluster completion repartitions packet and remainder exactly

**Evidence level:** exact synthesis from [FD-279](../../findings/FD-279-hard-cut-boundary-clusters-can-be-completed-at-negligible-spectral-power-cost.md) and [FD-280](../../findings/FD-280-cluster-completion-forces-an-equal-and-opposite-remainder-jump.md), with the complete-cluster conditioning mechanism inherited from FD-274--FD-278.

FD-279 establishes a geometric fact about a simple critical zero cluster intersected by an analyst-controlled hard spectral cutoff. In the low-height range relevant to the existing exponent ledger, the component diameter is only `O(1/log log x)`, so moving the cutoff just beyond the cluster restores the complete divided-difference packet without changing the spectral-height exponent. This removes a partial boundary cluster as an independent power-scale resource.

FD-280 identifies the exact bookkeeping cost of that move. Whenever the hard-truncated explicit representation is written

`A = C + P_T + E_T`,

the total object `A-C` is independent of the analyst's cutoff. Hence for any two admissible cutoffs

`E_(T_1)-E_(T_0) = -(P_(T_1)-P_(T_0))`.

The identity survives the consecutive-difference and divisor-replication maps used by the Farey destination. In particular the transformed packet jump and transformed remainder jump have equal `l^1` norm. Completing a close cluster can therefore replace a badly conditioned partial residue sum by a well-conditioned divided difference while the complementary remainder moves by the exact opposite amount.

The important distinction is between **conditioning of a component representation** and **continuity of the decomposed source object**. Small movement of the cutoff controls spectral location, but it does not control the packet increment: a close cluster may carry large inverse-gap residues before completion. Because the remainder is defined as the exact complement, it cannot remain approximately fixed when that packet changes substantially. Improved packet coordinates are real, but they are obtained by repartitioning the same exact object rather than by manufacturing a new small perturbation.

This changes the correct remainder question. One should estimate the remainder at a cluster-complete cutoff directly, or move the decomposition boundary earlier and group the contour remainder with the boundary cluster before taking absolute values. A continuity estimate of the form “tiny cutoff displacement implies tiny remainder displacement” cannot be the bridge, because the exact transfer identity gives an adversarial countermechanism whenever the inserted packet is large.

**Boundary.** The equal-and-opposite transfer is an exact hard-truncation identity, not a lower bound showing that the completed-cut remainder is itself large. It does not rule out a direct small remainder estimate at cluster-complete cutoffs or a grouped contour construction with better cancellation. The surrounding spectral-height tariffs remain conditional on RH and simple zeros where those assumptions entered; FD-280's algebraic repartition identity itself is more elementary.