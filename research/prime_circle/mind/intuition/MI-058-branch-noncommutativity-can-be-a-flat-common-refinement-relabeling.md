# MI-058 — Branch noncommutativity can be a flat common-refinement relabeling

**Evidence level:** exact operator/dynamical synthesis from [PC-379](../../findings/PC-379-branch-resolved-chebyshev-refinement-is-a-flat-tent-cuntz-system.md), following the Chebyshev reduction of PC-372--PC-378. This closes the canonical branch-resolved refinement system, not every matrix-valued Prime-Circle construction.

Keeping every inverse branch before scalar averaging does retain information that the transfer operator discards, and the resulting branch operators are genuinely noncommuting. But noncommutativity alone is not an invariant source resource. In the canonical angle coordinate, degree-`m` Chebyshev refinement is exactly the full `m`-fold tent map and its branch operators form a Cuntz family.

Composing a degree-`m` branch with a degree-`n` branch produces exactly one branch of the common degree-`mn` refinement. The two factorization orders therefore differ only by a reflected mixed-radix permutation of labels. Label every path by its final geometric branch and all factorization transition maps become identity coboundaries; every closed factorization loop has trivial holonomy.

The intrinsic orientation sign and half-density/Jacobian amplitude do not restore curvature. They multiply exactly under refinement and are determined by the same final branch. Thus the canonical branch-resolved system is a generic tent/Cuntz covering with a flat coherence law, even though its generators do not commute before relabeling.

The reusable test is to quotient a proposed matrix cocycle by the **common final refinement** before crediting noncommutativity. If every path lands in the same final branch and transition matrices only compare path labels, spectra or determinants of those permutations are coordinate artifacts. A surviving Prime-Circle matrix mechanism must attach additional source data to the branches or use an interaction that cannot be trivialized by the common-refinement label.

**Boundary.** PC-379 does not rule out primitive-shell, chord or cyclotomic amplitudes attached to branches, nonlinear interactions before final-branch identification, or source-forced domains/topologies outside the tent correspondence. It shows only that the complete canonical Chebyshev branch label, orientation and Jacobian normalization carry no intrinsic cross-level holonomy.