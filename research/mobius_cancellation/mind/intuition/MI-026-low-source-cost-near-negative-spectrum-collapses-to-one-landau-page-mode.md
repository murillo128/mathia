# MI-026 — Page balance prices a whole subset spectrum, and overlap is the only finite-harmonic rescue

**Evidence level:** exact line-specific consequence of [MC-293](../../findings/MC-293-landau-page-low-source-cost-near-negative-spectrum.md)--[MC-297](../../findings/MC-297-pair-overlap-stability-of-endpoint-page-spectrum.md). MC-293 imports classical Landau--Page uniqueness and low-conductor real-character balance; MC-294--MC-297 add finite coding and exact Boolean/Walsh identities. No arithmetic impossibility theorem for the actual Legendre shell and no bound for `M(x)` is claimed.

For a nonzero shell functional `lambda`, let `Q(lambda)` be the minimum lower-prime product cost realizing it. Below the quasi-subpower threshold `D_y`, MC-293 shows that every generated mode is asymptotically balanced except possibly one Landau--Page exceptional functional. MC-294 turns many selected near-negative directions into a high-cost quotient-dimension bill, while MC-295 shows that a generic fixed-weight model can still pay that bill.

MC-296 strengthens the endpoint geometry from basis cost to **subset-spectrum cost**. For independent selected functionals with disjoint defect sets of masses `d_i`, every subset sum has

`x_(lambda_I)=(-1)^|I| (1-2 d(I))`, `d(I)=sum_(i in I)d_i`.

Therefore every noncentral subset outside the Page half-mass window is forced high-cost, apart from the possible single exceptional mode. Equal endpoint defects make almost the entire selected Fourier subspace expensive.

MC-297 identifies exactly how this statement survives imperfect geometry. Shell coverage is not load-bearing: pairwise disjointness already gives the MC-296 formula even if a common preferred-sign region is unused. If defects overlap, then exactly

`x_(lambda_I)=(-1)^|I| (1-2d(I)+4 Omega_I)`,

with `0<=Omega_I<=B_I`, where `B_I` is the total pair-intersection mass among the defects in `I`. This correction is one-sided. If `d(I)<1/2`, overlap can only increase the normalized bias, so a lower-half mode outside the Page window remains expensive **without any overlap bound**. If `d(I)>1/2`, a cheap mode must spend overlap of order `2d(I)-1`; a global overlap budget then bounds how many upper-layer subsets can remain cheap.

The surviving arithmetic resource is therefore sharper than “expensive basis rank.” Endpoint saturation asks for a large expensive subset spectrum, and overlap is the only finite-harmonic mechanism available to soften its upper half. A closing theorem may attack either side: prove that the actual Legendre-shell defect family has too little pair/parity overlap to rescue enough modes, or prove that the lower-prime source cannot collectively realize the resulting exponential family of Page-high-cost characters.

**Boundary.** Pair overlap controls `Omega_I` only from above and does not determine it. Forcing many subset modes above `D_y` still does not imply a dimension contradiction. MC-297 supplies no arithmetic estimate for actual Legendre overlaps. The durable conclusion is the separation: incomplete coverage is harmless, overlap is the finite-harmonic rescue currency, and collective arithmetic realizability remains the final source-side gate.