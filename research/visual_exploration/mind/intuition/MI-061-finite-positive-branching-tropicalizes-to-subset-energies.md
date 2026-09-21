# MI-061 — Finite positive branching tropicalizes to subset energies

**Evidence level:** exact finite-dimensional synthesis from [VIS-365](../../findings/VIS-365-finite-weighted-vandermonde-subset-energy-spectrum.md), subsuming the one-scale Hermite and nested Newton ledgers of VIS-362--VIS-364.

For a fixed finite positive weighted polynomial-sampling family, branching does not require choosing one preferred hierarchy. Exterior powers price the whole geometry at once. If `sqrt(pi_i) asymp epsilon^(a_i)` and `|t_i-t_j| asymp epsilon^(kappa_ij)`, every `k`-volume has the unavoidable weighted Vandermonde cost

`E(I)=sum_(i in I)a_i + sum_(i<j in I)kappa_ij`.

The cheapest subset energy `Gamma_k=min_(|I|=k)E(I)` gives

`prod_(r<=k)s_r asymp epsilon^(Gamma_k)`

and therefore the individual singular exponent is `Gamma_k-Gamma_(k-1)`. Different `k` can choose different minimizing branches; no nested branch assumption is needed.

This turns finite positive branching into a **global tropical volume ledger**. Vanishing mass and geometric collision are the same kind of cost at the exterior-volume level, and switching the active branch as scale changes does not create a free direction so long as the family remains fixed finite and all relevant scales have stable power valuations.

The reusable test is therefore not “is the cluster tree complicated?” but “does the proposed family leave the finite subset-energy category?” Growing support/depth, non-power asymptotics, signed or non-diagonal coefficient topology, source-dependent arithmetic choices and infinite/global phase geometry are genuine changed hypotheses; a more elaborate finite positive branch tree is not.

**Boundary.** VIS-365 is finite-dimensional: `N` and `q` are fixed. The norm equivalence for compound matrices need not be uniform when either grows, and the theorem assumes positive weights, compact nodes and stable power valuations of actual pair separations. It proves a conditioning classification, not a stronger estimate for the arithmetic source.