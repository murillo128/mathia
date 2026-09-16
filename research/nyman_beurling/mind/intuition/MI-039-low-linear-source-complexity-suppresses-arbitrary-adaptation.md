# MI-039 — Low linear source complexity suppresses arbitrary height adaptation

**Evidence level:** exact source-side synthesis from [NB-168](../../findings/NB-168-stationary-arithmetic-rescue-is-density-sparse.md) through [NB-173](../../findings/NB-173-low-source-rank-suppresses-arbitrarily-adaptive-height-selection.md).

The adaptive compact-sampler problem has a linear structure that metric entropy and path variation do not see. Suppose every height-dependent template can be written as

`nu_(T,t) = sum_(j=1)^m beta_j(t) tau_j`,

where each stationary direction `tau_j` has capped Poisson transport at most `q_T` and the coefficient vector satisfies `sum_j |beta_j(t)|^2 <= Y_T^2`. The selector may depend arbitrarily on height and even on the local arithmetic source; no continuity, measurability or variation assumption is needed.

Linearity of `zeta'/zeta` turns the adaptive response into the same coefficient combination of `m` stationary responses. Pointwise Cauchy--Schwarz followed by the scalar stationary mean-square theorem gives

`rescue density << (m Y_T^2/log^2 T) * (1 + 1/(T a_T^2))`.

Thus positive-density logarithmic rescue requires `mY_T^2` at least of order `log^2 T` outside the already-known ultra-thin regime. The source can choose coefficients adversarially at every height, but it cannot obtain more response energy than the Euclidean energy already present in the stationary dictionary.

Optimizing over all capped-transport-normalized stationary representations defines an intrinsic linear source complexity `mathfrak L_T`. This removes arbitrary basis rescaling and duplication. It also satisfies

`X_T^2 <= mathfrak L_T`,

where `X_T` is the largest instantaneous capped-transport amplitude in the adaptive range. Linear source complexity therefore refines rather than replaces the pointwise-amplitude currency.

This creates a strict separation from the earlier adaptation controls. A rank-one family `beta_T(t) tau_T` can sweep a continuum of amplitudes, have a large covering number at source resolution, and oscillate with infinite `p`-variation for every finite `p`; NB-173 still prices it only by the coefficient-energy scale `Y_T^2`. Conversely, a geometrically compact range may require many nearly independent stationary directions. **Temporal roughness, metric repertoire and linear source span are different resources.**

The useful surviving escape is now more specific. An adaptive arithmetic rule that hopes to cancel the logarithmic zero-packet debt on positive density must generate genuinely large normalized source dimension/energy, not merely many parameter values or fast switching. A concise nonlinear rule could still do that; description length is not a bound on `mathfrak L_T`.

The next conceptual step is to understand whether source-natural nonlinear families force lower bounds on this linear complexity and how `mathfrak L_T` compares with capped-transport covering entropy at the exact Poisson resolution. Such a comparison would connect the unordered repertoire and linear-span currencies without assuming they coincide.

**Boundary.** NB-173 is a density obstruction inherited from the stationary mean-square theorem. It does not rule out deliberately selected sparse exceptional heights, does not improve the `a_T \lesssim T^(-1/2)` ultra-thin regime, and gives no lower bound showing the rank-energy estimate is sharp for arbitrary dictionaries. It is a source-persistence theorem, not a Nyman target-conditioning theorem.