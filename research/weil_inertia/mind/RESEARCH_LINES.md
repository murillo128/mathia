# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Control the finite negative sector against the now-uniform clipped source-tail gap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-032-reserve-lifting-converts-the-frozen-essential-obstruction-into-a-finite-negative-index-problem`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime already creates an essential negative band. WI-307 changes the architecture: because the unit-window archimedean symbol is unbounded above, the exterior reserve can be lifted at every fixed aperture, moving the essential spectrum positive and leaving only a finite discrete negative sector. WI-308 restores the omitted source exactly by clipping the source symbol, producing a positive tail multiplier with qualitative bottom `c_(chi,B)>0`.

WI-309 closes the tail-gap half of the quantitative gate. Instead of fixing a smooth localizer while the clipping reserve grows, choose an aperture-adaptive compactly supported `L^2` localizer whose endpoint singularity approaches the square-integrability threshold. Its Fourier tail then decays only just fast enough, and the shrinking normalization cancels against the integrated tail. With the explicit reserve `B_L=P_L+1`, the exact decomposition satisfies

`Q=D_(L,chi_L,B_L)+T_(chi_L,B_L)`,

`sigma_ess(D_(L,chi_L,B_L)) subset [1,infinity)`,

`T_(chi_L,B_L) >= c_0 I`,  `c_0=1/(64 pi e)`,

uniformly in the finite aperture. Under an RH failure, the first-crossing mode therefore forces `lambda_min(D)<=-c_0`: the clipped-tail witness cannot collapse to zero merely because the aperture grows.

The remaining obstruction has moved again. The endpoint-singular localizer makes its singularity exponent approach the `L^2` boundary, and the compact correction in `D` degenerates correspondingly. The live theorem is **uniform control of the finite negative spectrum for this adaptive family**, not a better lower bound on the tail multiplier. A successful construction must show `lambda_min(D_L)>=-c_0` (or an equivalent finite-sector domination) uniformly enough for the global limit; an impossibility result must show that the compact/discrete sector necessarily defeats every admissible adaptive reserve/localizer choice.

## Track localizer singularity and compact-sector complexity as the remaining price

WI-309 shows that a uniform positive tail reserve can be bought by moving the localizer toward the endpoint-singular `y^-1/2` profile. That purchase is not free: the localization-defect kernel remains compact for every finite aperture, but its regularity worsens as the singularity exponent approaches the endpoint. Future estimates must therefore track the norm, negative eigenvalue depth/multiplicity, or another effective spectral descriptor of that compact correction jointly with the active prime translations.

Reusing the old frozen `beta_0=1/16` essential-band obstruction or treating the uniform tail gap as a proof of positivity both miss the current architecture.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The source-exact decomposition now supplies a fixed positive margin, but an arbitrary finite-rank patch chosen after observing negative modes is still not source-valid. Any certificate must be derived from the actual adaptive localized Weil operator and survive the aperture limit.

## Preserve the signed-density quotient

Even a successful reserve-lifted/tail-retaining architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
