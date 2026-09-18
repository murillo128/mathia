# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Leave fixed-aperture projective compressibility and retain source-specific signed covariance

**Linked intuitions:** `MI-036-exact-zero-density-locks-bow-reciprocal-scale-at-riemann-siegel-length` through `MI-046-uniformly-analytic-features-preserve-fixed-aperture-compressibility`.

WI-331--WI-342 classify ordinary local Gowers smallness and its scalar repairs at the bow scale. Matched-energy Rademacher sources survive below the relevant deterministic walls; deleting diagonals, sparse geometric deletion, deterministic scalar reweighting, linear mixing of orders and canonical multiplicative-derivative coupling all remain inside generic Walsh/cube quotients rather than forcing the distinguished `Lambda-Lambda^sharp` covariance sign.

WI-343--WI-344 add a source-height dimension obstruction. A carrier family supported in logarithmic aperture `Delta` across height width `H` has factorial low-rank approximation controlled by the product `H Delta`, and arbitrary bounded height-independent **linear** preprocessing cannot manufacture extensive normalized height diversity without losing transmitted scale. On the natural Gallagher window `H Delta=1`, power-growing sample count is still compatible with bounded effective dimension.

WI-345 closes fixed-degree polynomial/tensor enrichment, and WI-346 extends the obstruction to uniformly analytic height-independent maps with fixed radius, bounded coefficient budget and nonvanishing transmission. These results show that simply increasing channel count or using smooth nonlinear features does not create extensive height information from a fixed aperture.

WI-347 identifies the real boundary behind those special cases. Let `w_U` be the normalized source carrier and `h_U` the normalized output of an arbitrary height-independent feature map. If the map is uniformly projectively continuous on the source family, so every output tolerance `epsilon` has a `T`-independent source radius `rho_epsilon`, then the sampled output Gram matrix has spectral tail bounded after rank

`N_epsilon = 1+ceil(H Delta/(2 rho_epsilon))`.

At `H Delta<=1`, every such family therefore has bounded effective dimension, without assuming linearity, polynomial structure or analyticity. Conversely, if a fixed fraction of Gram mass must survive beyond rank `r(T)->infinity`, the required projective resolution satisfies `rho=O(H Delta/r(T))`: the feature map must resolve progressively smaller source differences.

The live theorem must now violate this projective-continuity boundary or bypass generic feature rank altogether. Genuine escapes include a continuity modulus whose useful radius collapses with height, diverging Lipschitz/Hölder constants, vanishing transmission, growing aperture, explicit height dependence, essential global-phase sensitivity, cross-window/cross-scale coupling, or a direct arithmetic signed-covariance identity. Calling a feature map nonsmooth is not enough; it must become quantitatively source-resolving at the scale demanded by the target rank.

The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` remains the clean destination test: prove the needed negative off-diagonal contribution with `Lambda^sharp` retained in the same norm, or prove that the proposed statistic cannot force it.

## Keep diagonal removal, feature resolution, aperture, transmission scale and covariance sign separate

Diagonal-free does not mean destination-sensitive. Scalar cube refinements can reduce a generic chaos floor without reaching the distinguished source sign. Likewise, nonlinear does not mean high-dimensional: WI-345--WI-347 show that fixed-degree, uniformly analytic, and in fact any uniformly projectively continuous height-independent feature family remains compressed at fixed aperture and fixed output tolerance.

A proposed bridge should therefore state the source-start quantifier, exact carrier/feature family, normalization, the physical logarithmic aperture, the projective resolution modulus actually available at height `T`, transmitted amplitude, and the exact off-diagonal covariance sign it forces. A large number of channels or a complicated feature map is not new source information unless its **resolution on the physical carrier family** scales strongly enough and the destination receives that information without losing the distinguished sign.