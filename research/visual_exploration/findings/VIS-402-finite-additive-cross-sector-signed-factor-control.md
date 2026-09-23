# VIS-402 — finite additive cross-sector signed factors remain exactly calibratable after squaring

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-401`, with positive commutator-Laplacian support

`0 < q_1 < q_2 < q_3`

and normalized positive spectral weights `W=(W_1,W_2,W_3)`.

Let `L` be a fixed finite-dimensional latent random vector with probability law `R`, and let `A_1,A_2,A_3` be mutually independent real random variables, independent of `L`, with absolutely continuous densities `f_i`. Fix loading vectors `b_i` independently of the candidate residual and form cross-sector coherent signed amplitudes

`S_i = A_i + <b_i,L>`,

then energies and normalized weights

`Y_i=S_i^2`,

`W_i=Y_i/(Y_1+Y_2+Y_3)`

whenever the total energy is positive.

The `Y_i` are generally dependent because the same latent `L` enters several sectors. Nevertheless, conditional on `L=l`, the sector amplitudes are independent shifted variables. Their exact conditional energy densities are

`h_i(y|l) = [f_i(sqrt(y)-<b_i,l>) + f_i(-sqrt(y)-<b_i,l>)]/[2 sqrt(y)]`, `y>0`.

Hence the unconditional normalized-weight density on the open simplex is exactly

`g(w) = integral R(dl) integral_0^infinity t^2 prod_(i=1)^3 h_i(t w_i|l) dt`.

Conditioning further on the qutrit first moment

`m_1=sum_i q_i w_i=x`

again gives a completely specified one-dimensional residual law along the affine slice `w(u)` of `VIS-389`:

`p(u|x) proportional_to g(w(u))`.

Therefore **a finite additive signed latent shared coherently across sectors does create cross-sector dependence, but it does not by itself create an uncontrolled Wang residual**. If the latent law, loadings and idiosyncratic amplitude laws are fixed independently of the candidate, the entire normalized qutrit residual remains a source-free calibratable mixture.

In the scalar centered-idiosyncratic specialization

`S_i=A_i+c_i L`, `E[A_i]=0`,

with finite second moments for `A_i` and finite fourth moment for `L`, the raw sector-energy covariance is exactly

`Cov(Y_i,Y_j)=c_i^2 c_j^2 Var(L^2) >= 0`, `i!=j`.

Thus the simplest common-factor interference model has both an exact residual calibration and a sharp raw-energy sign constraint. The sign constraint is only a diagnostic: zero covariance need not imply independence, and normalized simplex weights may have either-sign dependence because of the common denominator.

**Evidence/status:** `EXACT-DERIVED + FINITE LATENT-FACTOR CONTROL + NEGATIVE CALIBRATION + CLASSICAL CONDITIONING/CHANGE-OF-VARIABLES + NO-NOVELTY-CLAIM FOR LATENT-FACTOR OR COMPOSITIONAL PROBABILITY`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Conditioning restores sector independence

Fix `L=l`. Then

`S_i | (L=l) = A_i + <b_i,l>`.

Because the `A_i` are mutually independent and independent of `L`, the conditional signed amplitudes are independent with densities

`F_i(s|l)=f_i(s-<b_i,l>)`.

The shared factor has therefore changed the unconditional dependence architecture, but it has not destroyed conditional independence once its finite latent state is exposed.

This is the exact distinction left open by `VIS-401`. Sector-local signed interference was conditionally independent given packet counts. Here the positive sector energies remain dependent even after any local packet counts are fixed, but they become independent after conditioning on the common latent itself.

## 2. Squaring and radial normalization give the exact simplex law

For fixed `l`, the map `s -> y=s^2` has two inverse branches, so

`h_i(y|l)=[F_i(sqrt(y)|l)+F_i(-sqrt(y)|l)]/[2 sqrt(y)]`.

Conditional on `L=l`, the positive vector `Y` has product density

`prod_i h_i(y_i|l)`.

Now write

`y_i=t w_i`, `t>0`, `w_i>0`, `sum_i w_i=1`.

The Jacobian is `t^2`, hence

`g(w|l)=integral_0^infinity t^2 prod_i h_i(t w_i|l) dt`.

Marginalizing the independently specified latent gives

`g(w)=integral g(w|l) R(dl)`.

Nothing in this derivation requires Gaussianity, a Gamma energy law, equal sector scales, or a scalar latent. A finite discrete latent is handled by replacing the outer integral with a finite/countable sum; mixed latent laws are handled measure-theoretically in the same way. If an idiosyncratic sector law has atoms, the corresponding simplex-face or lower-dimensional components must be retained rather than hidden inside an interior density.

For the generic qutrit fixed-`m_1` slice, `w=w(u)` is affine. Its line Jacobian is constant, so the residual density is proportional to the already specified `g(w(u))`. Numerical quadrature may be required, but no residual-fitting degree of freedom is introduced by the integration itself.

## 3. A scalar shared factor forces nonnegative raw energy covariance

Take the specialization

`S_i=A_i+c_iL`

with mutually independent centered `A_i`, independent of `L`. Put `v_i=E[A_i^2]`, `m_2=E[L^2]`, and `m_4=E[L^4]`. Then

`E[Y_i]=v_i+c_i^2 m_2`.

For `i!=j`, expanding `Y_iY_j` and using independence plus `E[A_i]=E[A_j]=0` kills every term containing an odd idiosyncratic factor. The surviving terms give

`E[Y_iY_j] = v_i v_j + v_i c_j^2 m_2 + v_j c_i^2 m_2 + c_i^2 c_j^2 m_4`.

Subtracting `E[Y_i]E[Y_j]` yields

`Cov(Y_i,Y_j)=c_i^2 c_j^2(m_4-m_2^2)=c_i^2 c_j^2 Var(L^2) >= 0`.

For a Gaussian scalar factor with variance `tau^2`, this becomes

`Cov(Y_i,Y_j)=2 c_i^2 c_j^2 tau^4`.

This sign constraint is useful only for this centered scalar additive architecture. It must not be promoted to a universal property of cross-sector interference. In particular, more general interacting amplitudes, vector factors with non-Gaussian structure, nonzero idiosyncratic means, or normalization to `W` can remove any simple covariance-sign diagnostic.

## 4. Consequence for the Wang packet-localization clue

`VIS-401` left a signed latent shared coherently across sectors as the sharp next dependence test. The present result closes the broadest elementary additive version of that escape.

A shared finite latent is not enough if it merely acts as a pre-specified common factor added to otherwise independent sector amplitudes. The apparent cross-sector dependence can be disintegrated over the latent state, squared sectorwise, radially normalized, and then mixed back exactly. Rejecting an independent-sector null while fitting this common-factor class would therefore not establish arithmetic source information.

The surviving question must now earn something stronger: a source-derived restriction on the latent law/loadings, interactions that do not reduce to conditionally independent sector amplitudes given a pre-specified finite latent state, a nontrivial infinite/continuum scaling limit with independently frozen structure, or a direct Wang admissibility theorem that forces a narrower residual family. Allowing an arbitrary latent representation fitted to the observed residual would be vacuous rather than a stronger test.

## Prior-art and novelty audit

The ingredients are classical probability and multivariate-statistics constructions: common latent factors induce dependence through shared variation, conditional independence is recovered after conditioning on the factor in the present model, and normalization of a positive vector places the result on the simplex. The compositional/simplex prior-art anchors already recorded in `SOURCES.md` (Aitchison; Rayens--Srinivasan) bound novelty for the normalized-weight law. Standard factor-analysis literature likewise treats shared latent factors as classical multivariate dependence models.

No new theorem about factor analysis, conditional mixtures, squared random variables, copulas, or compositional distributions is claimed. The Mathia-specific content is the exact falsification boundary: **finite additive cross-sector signed coherence, when independently specified, remains a calibratable nuisance for the qutrit Wang residual rather than source evidence**.

## Boundaries

- The latent dimension is finite and its law `R` is fixed independently of the candidate residual.
- The loadings `b_i` and idiosyncratic laws `f_i` are fixed independently; they may not be selected by inspecting the residual being judged.
- Conditional on the latent, the sector amplitudes are additive shifts of mutually independent idiosyncratic variables. This conditional-independence structure is load-bearing.
- The displayed interior density assumes absolutely continuous idiosyncratic laws and positive total energy almost surely; atoms require the corresponding mixed/face measure terms.
- Exact calibration may require numerical integration over total energy and latent state. Computational cost is not a free statistical parameter.
- The nonnegative covariance formula is only for the scalar common-factor specialization with centered independent idiosyncratic amplitudes and finite moments. It is not asserted for the full latent-vector class or for normalized weights.
- An unrestricted latent law/loading family can become arbitrarily flexible. Such post-hoc flexibility is not an admissible source-free null and cannot be used to explain away a candidate after inspection.
- The result does not cover genuinely interacting sector amplitudes that remain dependent after conditioning on the admitted latent state, cross-sector phase dynamics outside an additive real-factor representation, nontrivial infinite-dimensional/continuum latent limits, or Wang-admissibility constraints tied to arithmetic source data.
- No retained visualization is required because the useful result is an exact representation-independent probability decomposition once the qutrit reduction is fixed.
