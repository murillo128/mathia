# VIS-400 — fixed-budget exclusive positive packets remain exactly calibratable beyond Gamma

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-399`, with positive commutator-Laplacian support

`0 < q_1 < q_2 < q_3`

and normalized positive sector weights `W=(W_1,W_2,W_3)`.

The Gamma assumption in `VIS-399` is **not** load-bearing for exact calibration of a fixed-budget exclusive packet mechanism.

Fix a packet budget `N>=1`. For each packet `n=1,...,N`, choose exactly one sector

`Z_n in {1,2,3}`

independently with

`P(Z_n=i)=p_i`, `p_i>0`, `sum_i p_i=1`.

Conditional on `Z_n=i`, give that packet an independent positive amplitude with an independently specified density

`A_n | (Z_n=i) ~ h_i(a) da`, `a>0`,

and finite mean

`mu_i = integral_0^infinity a h_i(a) da`.

Define

`Y_i=sum_(n:Z_n=i) A_n`,

`W_i=Y_i/(Y_1+Y_2+Y_3)`,

and counts

`K_i=#{n:Z_n=i}`.

Then `K=(K_1,K_2,K_3)` is multinomial exactly as in `VIS-399`. Conditional on `K=k`, for every occupied sector `i` the sum `Y_i` has density

`f_(i,k_i)=h_i^{*k_i}`,

the `k_i`-fold convolution of the sector amplitude density, and the occupied sector sums are mutually independent.

For a full-occupancy component `k_i>=1`, the normalized weight vector has exact density on the open simplex

`g_k(w)=integral_0^infinity t^2 prod_(i=1)^3 f_(i,k_i)(t w_i) dt`.

Therefore the full-occupancy interior law is the finite exact mixture

`f_int(w)=sum_(k_i>=1, sum k_i=N) pi_k g_k(w)`,

with multinomial weights `pi_k=P(K=k)` up to the common full-occupancy conditioning constant. Count vectors with empty sectors give the corresponding lower-dimensional pushforwards on simplex faces; if `r` sectors are occupied, the radial Jacobian is `t^(r-1)`.

The raw sector energies still satisfy, for every `i!=j`,

`Cov(Y_i,Y_j)=-N p_i p_j mu_i mu_j < 0`,

which depends only on exclusivity and first moments, not on Gamma closure.

Fixing the qutrit first moment

`x=m_1=sum_i q_i w_i`

and using the affine residual coordinate `w(u)` from `VIS-389`, the full-occupancy residual density is exactly

`p(u | x, full occupancy) proportional_to f_int(w(u))`.

If empty-sector events are retained, the residual law is again a finite mixed continuous/discrete law with explicitly determined face contributions. Thus **genuinely non-Gamma positive packet amplitudes do not by themselves create an uncontrolled Wang residual inside the fixed-budget exclusive architecture**. Once the amplitude laws are fixed independently, the null is exactly specified by finite convolution plus a one-dimensional radial integral for each count component.

**Evidence/status:** `EXACT-DERIVED + GENERAL POSITIVE-AMPLITUDE FIXED-BUDGET CONTROL + CLASSICAL COMPOSITIONAL/SIMPLEX PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY TRANSFORMATION`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Conditioning on counts removes assignment-label dependence

The count vector is multinomial because the packets choose sectors independently.

Fix a count vector `k`. Conditional on one particular assignment pattern with those counts, sector `i` contains `k_i` independent amplitudes with common density `h_i`. Hence its total has density

`f_(i,k_i)=h_i^{*k_i}`

for `k_i>=1`, and is zero identically for `k_i=0`.

Different sector totals use disjoint independent packet amplitudes, so they are independent conditional on the assignment pattern. Crucially, their joint law depends on the assignment pattern only through the count vector `k`. Averaging over all assignments with the same `k` therefore leaves the same product law

`prod_(i:k_i>0) f_(i,k_i)(y_i)`.

Gamma closure in `VIS-399` made these convolutions elementary; it was not needed for conditional independence or exact specification.

## 2. Normalization of arbitrary positive sector sums

Assume first `k_i>=1` for all three sectors. The conditional joint density of the positive sector totals is

`prod_i f_(i,k_i)(y_i)`.

Use the standard simplex/radial change of variables

`y_i=t w_i`, `t>0`, `w_i>0`, `sum_i w_i=1`.

In three dimensions the Jacobian is `t^2`, so integrating out total scale gives

`g_k(w)=integral_0^infinity t^2 prod_i f_(i,k_i)(t w_i) dt`.

This is already a normalized density because it is obtained by an exact change of variables from the conditional product density. No parametric family is required.

When the amplitudes are Gamma, the convolution densities remain Gamma and the radial integral evaluates to the normalized-Gamma formula in `VIS-399`. For non-Gamma `h_i`, the same law remains exact even when the convolution or radial integral requires numerical evaluation.

If only an active set `I` of `r` sectors is occupied, the identical argument on that simplex face gives Jacobian `t^(r-1)`. A single occupied sector gives a vertex atom. Therefore the unconditioned normalized law remains a finite exact mixture over interior and face components.

## 3. Negative dependence is distribution-free inside this architecture

For one packet define

`V_i=A 1_(Z=i)`.

For `i!=j`, exclusivity gives

`V_i V_j=0`

almost surely. Also

`E[V_i]=p_i mu_i`.

Hence

`Cov(V_i,V_j)=-p_i p_j mu_i mu_j`.

The packets are independent, so summing over `N` packets yields

`Cov(Y_i,Y_j)=-N p_i p_j mu_i mu_j`.

No higher moment or Gamma identity enters. Thus the negative raw-energy dependence isolated in `VIS-399` is a structural consequence of fixed-budget exclusivity, not of the packet-amplitude family.

## 4. Exact qutrit residual calibration survives non-Gamma amplitudes

For fixed generic qutrit support and interior first moment `x`, the constraint

`sum_i q_i w_i=x`

cuts the open simplex in the same affine segment used from `VIS-389` onward. Let `w(u)` be its affine parametrization.

Because the line Jacobian is constant,

`p(u|x,k,full occupancy) proportional_to g_k(w(u))`.

Averaging with the fixed multinomial component weights gives the exact full-occupancy residual density. Face components intersect the fixed-`m_1` slice in lower-dimensional pieces, generically points in the qutrit case, and therefore contribute exact atoms or lower-dimensional terms. A randomized CDF can again uniformize the resulting mixed law.

"Exact" here means mathematically specified without asymptotic approximation or fitted residual freedom. It does not mean every convolution or CDF has an elementary closed form. Deterministic quadrature or convolution algorithms may be needed for evaluation, but those are numerical implementation details of a fixed null rather than extra nuisance degrees of freedom.

## 5. Consequence for the Wang localization clue

`VIS-399` left genuinely non-Gamma packet amplitudes as one candidate escape from the source-free nuisance ladder. Within the fixed-budget exclusive architecture, that escape collapses.

Changing Gamma amplitudes to any independently specified positive absolutely continuous packet law changes the component densities, possibly very strongly, but it does not make the qutrit residual unspecified. The count mixture, normalized-simplex law, negative covariance, and fixed-`m_1` residual all remain exact through convolution and radial integration.

The next useful mechanism must therefore alter more than the one-packet positive amplitude family. Examples include signed or interfering latent contributions before energy formation, packet interactions that destroy conditional independence given counts, continuous/infinite latent structures with a nontrivial scaling law, or a Wang admissibility condition that couples packet structure to the arithmetic source.

## Prior-art and novelty audit

The surrounding probability language is classical. J. Aitchison, **The Statistical Analysis of Compositional Data**, *Journal of the Royal Statistical Society, Series B* 44:2 (1982), 139--160, DOI `10.1111/j.2517-6161.1982.tb01195.x`, is a foundational reference for probability laws and dependence on the simplex of proportions.

William S. Rayens and Cidambi Srinivasan, **Dependence Properties of Generalized Liouville Distributions on the Simplex**, *Journal of the American Statistical Association* 89:428 (1994), 1465--1470, DOI `10.1080/01621459.1994.10476885`, provides direct prior art for rich non-Dirichlet dependence families on the simplex. The broader Liouville literature likewise treats positive-vector/radial constructions and their normalized proportions.

`VIS-399` already anchors compound multinomial/proportion prior art through Mosimann (1962). The present radial-density identity is an elementary change-of-variables formula and is not claimed as a new theorem in probability or compositional statistics. The Mathia-specific content is the falsification boundary: non-Gamma positive amplitudes alone do not rescue source specificity in this fixed-budget Wang qutrit null when their laws are independently specified.

## Boundaries

- The packet budget `N` is finite and fixed independently of the candidate residual.
- Packets choose exactly one sector independently with fixed probabilities `p_i`.
- Conditional on its sector, each packet amplitude is positive, independent across packets, and drawn from a fixed sector law with an absolutely continuous density `h_i` and finite mean.
- The amplitude densities may be independently estimated or fixed by architecture, but they may not be selected or tuned using the candidate residual being tested.
- Arbitrary positive densities can make convolution and radial integration numerically expensive; exact specification does not imply an elementary closed form.
- Mixed or purely discrete positive amplitude laws admit an analogous measure-pushforward treatment, but that extension is not needed for the stated density result and is not claimed here.
- The result does not cover signed/interfering latent contributions before energy formation, packet interactions, shared latent variables that destroy conditional independence given counts, infinite packet budgets with nontrivial limits, arbitrary copulas, or Wang-admissibility constraints tied to arithmetic source data.
- No retained visualization is required because the useful result is a representation-independent probability decomposition once the qutrit reduction is fixed.
