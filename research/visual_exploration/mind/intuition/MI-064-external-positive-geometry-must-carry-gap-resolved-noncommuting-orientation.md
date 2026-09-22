# MI-064 — External positive geometry must carry gap-resolved noncommuting orientation

**Evidence level:** exact finite-dimensional matrix-analysis synthesis from [VIS-372](../../findings/VIS-372-commuting-external-hermitian-structure-remains-joint-spectral.md), [VIS-373](../../findings/VIS-373-small-commutator-is-gap-weighted-near-preconditioning.md), and [VIS-374](../../findings/VIS-374-near-degenerate-gram-cluster-orientation-is-spectrally-cheap.md), extending the one-Gram preconditioning audit of MI-063.

Adding independently supplied Hermitian structure does not leave the spectral-filter class merely because more than one matrix is present. VIS-372 shows that if the external Hermitian operators commute with the baseline Gram and with each other, every simultaneous-unitary-equivariant positive metric constructor is scalar on their joint eigenspaces. The resulting metric is only joint spectral reweighting.

Genuine noncommutation is a necessary first gate, but VIS-373 shows that it is not quantitatively sufficient. If `G=sum lambda_alpha P_alpha` and `C>0`, Gram-block pinching produces an exactly commuting positive `C_0`, with off-block distance controlled by the gap-normalized commutator. Across resolved Gram gaps `delta_G`, a metric bounded below by `mI` has its whole modified singular spectrum perturbatively close to the commuting/preconditioning class when `||[G,C]||_F/(sqrt(m)delta_G)` is small.

VIS-374 closes the near-degenerate-cluster loophole left by that estimate for bounded positive metrics. Cluster the spectrum of `G`, let `eta` be the within-cluster width, `gamma` the inter-cluster gap, and assume `mI<=C<=MI`. There exists an exactly `G`-commuting positive metric `C_*` with the same eigenvalue multiset as the cluster-pinched metric inside every cluster such that every squared singular value differs by at most

`||G||_op sqrt(M/m) ||[G,C]||_F/gamma + 2M eta`.

If `C` is already block diagonal across the clusters, only the `2M eta` term remains. Hence a large eigenvector rotation hidden inside a collapsing Gram cluster is spectrally cheap by the same small width that made the commutator insensitive to it. Near-degeneracy does not provide a free orientation resource.

The meaningful resource is therefore **orientation that survives a complete spectral-scale ledger**. A bounded positive-Hilbert candidate must pay through substantial cross-cluster orientation across resolved gaps, non-negligible cluster width that itself reaches the destination, or metric degeneration/condition-number growth large enough to compensate those small scales. Formal noncommutation, rapidly rotating eigenvectors, or a tiny commutator inside an almost scalar cluster do not establish new arithmetic leverage.

A surviving candidate must also justify the provenance of the external geometry. Even an order-one gap-resolved orientation is only a new arithmetic mechanism if it is fixed by physical coefficient/destination topology, source information, or another independently justified operator and then survives the remaining destination reductions. Otherwise it remains engineered preconditioning.

**Boundary.** VIS-372--VIS-374 are finite-dimensional positive-Hilbert statements. They do not classify indefinite/non-Hilbert forms, nonlinear source coupling, noncompact/global geometry, or controlled infinite-dimensional limits. Metric degeneration is not ruled out, but its factors `M` and `sqrt(M/m)` must be charged. No Chebyshev-theta, zeta-zero or RH estimate follows from these structural tests alone.