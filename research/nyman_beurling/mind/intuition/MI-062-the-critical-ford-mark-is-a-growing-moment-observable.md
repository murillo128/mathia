# MI-062 — Critical Ford decay is a depth-marked carrier pair-energy problem, not an absolute-phase reconstruction problem

**Evidence level:** exact positive reduction plus matched controls and source-specific detector audits from [NB-234](../../findings/NB-234-growing-depth-moment-hierarchy-reconstructs-critical-ford-mark.md)--[NB-244](../../findings/NB-244-ramachandra-revesz-clustering-turns-on-beyond-the-ford-window.md), building on NB-230--NB-233.

NB-234--NB-237 identify the critical coefficient first as a growing depth--phase moment observable and then as a microlocal pairing with the `R`-normalized logarithmic derivative. The `1/R` first-order normalization is not automatic decay because `Theta(J)` poles can sit at spacing `Theta(1/R)` with carrier phases locked.

NB-238--NB-242 show how easily relevant information is coarse-grained. Half-isolated-zero clumps, mesoscopic zero forcing, published short-interval pair correlation and translation-invariant statistics can all fail to reconstruct the **signed** anchored coefficient at the required scale. In particular, a half-period translate can reverse the carrier phase while preserving every relative ordinate statistic.

NB-243 separates reconstruction from decay. Writing the exact Ford coefficient as `J^-1 sum_j b_j exp(i X(gamma_j-t))`, its squared modulus is exactly

`J^-2 sum_(j,k) b_j conjugate(b_k) exp(i X(gamma_j-gamma_k))`.

The selected height disappears from the oscillatory phase, while the source localization and Ford-depth/profile marks remain. The diagonal is `O(1/J)`. Hence proving `R_J=o(1)` only requires the marked off-diagonal carrier energy to be `o(1)`; no absolute `U(1)` phase reference is needed. The half-period twins both have order-one energy, which is exactly the behavior a decay theorem must exclude.

NB-244 then tests a pointwise near-one clustering theorem against this corrected target. Ramachandra--Révész clustering turns on only at radii much larger than the full Ford window in the transition regime, so it remains quantitatively silent where the marked energy lives. This reinforces a resolution gate without reinstating the unnecessary absolute-phase requirement.

The reusable audit is therefore: identify the exact norm needed by the destination; preserve the marks and selected window defining that norm; reduce to the weakest sufficient correlation statistic; and then compare every source theorem with the carrier frequency and localization scale before crediting it. Source specificity without matching resolution is insufficient, but signed reconstruction can also demand strictly more information than decay.

**Boundary.** The pair-energy identity is exact but tautological at the estimate level: it supplies no new zero correlation theorem. Published pair-correlation and clustering results audited here do not furnish the required uniform marked local estimate. If a later destination needs the argument of the Ford coefficient rather than only small modulus, the absolute-phase obstruction returns. None of these findings proves a new Nyman--Beurling distance bound or RH.