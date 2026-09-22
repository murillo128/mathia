# VIS-386 — self-defect spectral windows need a Gram-tangent scale quotient

## Claim

Let `Delta_S` be the intrinsic positive semidefinite source-subspace commutator Laplacian from `VIS-384`, let `P_0` project onto `ker Delta_S`, and set

`g=(I-P_0)G`.

Assume `g != 0` and define

`epsilon_S(G)^2=<G,Delta_S G>=<g,Delta_S g>`.

The raw defect-squared localization statistic introduced in `VIS-384`,

`A_(G,S)(alpha)=||P_(0,alpha epsilon_S(G)^2]^(Delta_S) G||_F`,

is **not invariant under rescaling of the Gram tangent**. For every nonzero scalar `c`,

`epsilon_S(cG)^2=c^2 epsilon_S(G)^2`

and therefore

`A_(cG,S)(alpha)`
` = |c| ||P_(0,alpha c^2 epsilon_S(G)^2]^(Delta_S) g||_F`.

Thus changing only the tangent amplitude changes both the measured vector and the spectral window. In fixed finite dimension, if `epsilon_S(G)>0`, sufficiently small `|c|` excludes every positive spectral component of `g`, while sufficiently large `|c|` includes all of them. Raw low-mode mass at threshold `alpha epsilon_S(G)^2` is therefore not a representation-stable source statistic unless the tangent scale is fixed independently.

There is a canonical scale quotient. Define the positive-spectrum mean eigenvalue seen by `g`,

`m_S(G)=epsilon_S(G)^2/||g||_F^2`,

and the normalized cumulative low-mode mass

`F_(G,S)(alpha)`
` = ||P_(0,alpha m_S(G)]^(Delta_S) g||_F^2 / ||g||_F^2`.

Then `m_S(cG)=m_S(G)` and `F_(cG,S)(alpha)=F_(G,S)(alpha)` for every `c != 0`.

However this scale-invariant repair has its own exact universal baseline. For every `alpha>1`,

`F_(G,S)(alpha) >= 1-1/alpha`.

This is the spectral Markov bound applied to the probability measure of `Delta_S` induced by the normalized vector `g/||g||_F`, whose mean is exactly `m_S(G)`. Consequently **order-one mass below a fixed multiple larger than one of the self-defect mean is automatic and is not evidence of source-specific localization**.

A discriminating test must therefore either examine sub-mean windows, compare the full normalized spectral distribution against matched controls, or use another independently fixed spectral scale. The orientation-adapted threshold of `VIS-382` is not invalidated: its factor `omega(C)^2/q^2` makes that threshold homogeneous under `G -> cG`. The present finding targets only the later simplification to a raw self-defect window.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-QUOTIENT + UNIVERSAL-SPECTRAL-BASELINE + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No arithmetic localization, source-specific excess, Wang destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Tangent amplitude moves the raw spectral window

Because `Delta_S` is independent of `G`, rescaling the tangent gives

`epsilon_S(cG)^2=<cG,Delta_S cG>=c^2 epsilon_S(G)^2`.

The kernel component never contributes to positive spectral projectors, so

`P_(0,tau]^(Delta_S)G=P_(0,tau]^(Delta_S)g`.

Hence

`A_(cG,S)(alpha)`
` = ||P_(0,alpha c^2 epsilon_S(G)^2] c g||_F`
` = |c| ||P_(0,alpha c^2 epsilon_S(G)^2] g||_F`.

Write the positive eigenvalues of `Delta_S` on the spectral support of `g` as a finite set. If `epsilon_S(G)>0`, that support is nonempty. Let `lambda_min(G)>0` and `lambda_max(G)` be its smallest and largest values. Then

`alpha c^2 epsilon_S(G)^2 < lambda_min(G)`

implies `A_(cG,S)(alpha)=0`, while

`alpha c^2 epsilon_S(G)^2 >= lambda_max(G)`

implies

`A_(cG,S)(alpha)=|c| ||g||_F`.

Nothing about `S`, its commutant, or its arithmetic content changed. Only the arbitrary amplitude assigned to the tangent changed. Therefore the raw self-defect cutoff cannot be compared across families whose tangent normalization is allowed to drift.

## 2. Quotient the tangent amplitude by its positive-spectrum norm

The natural probability spectral measure of `Delta_S` seen by `g` is

`mu_G(B)=||P_B^(Delta_S) g||_F^2/||g||_F^2`

for Borel subsets `B` of the positive spectrum. Its first moment is

`int lambda d mu_G(lambda)`
` = <g,Delta_S g>/||g||_F^2`
` = m_S(G)`.

Both `mu_G` and `m_S(G)` are unchanged by `G -> cG`. The cumulative statistic

`F_(G,S)(alpha)=mu_G((0,alpha m_S(G)])`

therefore removes the tangent-amplitude gauge exactly.

This quotient is separate from `VIS-384`. `VIS-384` removed changes of coordinates in the **source-generator presentation** while keeping the source subspace fixed. The present quotient removes a scalar presentation freedom in the **Gram tangent amplitude**. Both are needed before a low-mode comparison can be interpreted geometrically across families.

## 3. The self-normalized super-mean window has a universal mass floor

For `alpha>1`, Markov's inequality applied to the nonnegative random variable `lambda` under `mu_G` gives

`mu_G((alpha m_S(G),infty)) <= 1/alpha`.

Therefore

`F_(G,S)(alpha)`
` = 1-mu_G((alpha m_S(G),infty))`
` >= 1-1/alpha`.

At `alpha=2`, at least one half of the positive-spectrum Gram mass lies below twice its own mean spectral value for **every** source subspace and every nonzero tangent. More generally the lower bound tends to one as `alpha` grows.

This does not say the normalized spectral profile is useless. It says that absolute statements such as "an order-one fraction lies below `alpha m_S`" are nondiscriminating for `alpha>1`. Source information can only reside in excess shape relative to the universal floor and to stronger matched controls, in sub-mean concentration, or in geometry of the corresponding spectral subspaces.

No positive lower bound of this form is forced for `0<alpha<=1`: a spectral measure may place all mass above `alpha m_S`. Those windows can therefore be more discriminating, provided `alpha` is fixed before confirmation data and numerical rank/spectral resolution are controlled.

## 4. Relation to the orientation theorem

`VIS-382` uses the orientation-adapted threshold

`tau_beta = beta omega(C)^2 epsilon_G^2/q^2`,

where `q=||[G,C]||_F`. Under `G -> cG`, both `epsilon_G^2` and `q^2` scale by `c^2`, so `tau_beta` is unchanged. Its conclusion is therefore homogeneous in the tangent amplitude.

The present obstruction arises only when that theorem is converted into the simpler exploratory statistic `P_(0,alpha epsilon_S(G)^2]G` without carrying an independent tangent normalization or the orientation factor. The exact theorem remains valid; the exploratory diagnostic needs one more representation quotient.

## Controls and boundaries

If `g=0`, then `epsilon_S(G)=0` and there is no positive-spectrum tangent component to localize. This is the exact-commutant case and should be handled separately rather than assigning a normalized statistic.

The quotient by `||g||_F` does not make the source subspace, ambient Hilbert metric, numerical rank rule, spectral threshold, or matched-control ensemble free resources. `VIS-383`--`VIS-385` continue to govern those layers.

When stronger controls resample both `S` and `G`, compare them through the same normalization rule. Holding `G` fixed, as in the first-stage Haar-Grassmann calibration of `VIS-385`, already removes the tangent-scale ambiguity for that specific null. The present issue becomes essential when comparing different tangents, truncations, packet families, or source-derived controls.

## Prior-art and novelty audit

The argument is elementary finite-dimensional spectral calculus. The scale quotient is just normalization of a vector-induced spectral measure, and the mass floor is the standard Markov/Chebyshev tail estimate already used explicitly in `VIS-382`. No novelty is claimed for the homogeneity calculation, spectral measure normalization, or Markov inequality.

The Mathia-specific consequence is narrower: after `VIS-384` quotients generator coordinates and `VIS-385` calibrates the isotropic source-subspace defect energy, the accepted Wang localization test still has a tangent-amplitude representation freedom. Quotienting it exposes an additional universal baseline that must be removed before defect-normalized low-mode mass can be credited as source-specific structure.

## Dependencies

- `VIS-382`: the homogeneous orientation-adapted defect-squared localization theorem.
- `VIS-384`: intrinsic Hilbert-Schmidt source-subspace Laplacian and the raw exploratory profile.
- `VIS-385`: exact fixed-`G` isotropic source-subspace defect-energy calibration.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose decisive test uses the low-mode profile.

## Research consequence

Future tests of the accepted Wang localization clue should not compare raw `A_(G,S)(alpha)` across objects with different tangent scales. Remove the exact commutant component, normalize by `||g||_F`, and compare the resulting spectral CDF on a pre-registered scale. For `alpha>1`, treat `1-1/alpha` as a universal non-arithmetic floor rather than as evidence; a useful signal must be excess relative to matched controls or concentration in a genuinely discriminating spectral region.
