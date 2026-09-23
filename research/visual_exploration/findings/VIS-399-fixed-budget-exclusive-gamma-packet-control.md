# VIS-399 — fixed-budget exclusive Gamma packets give an exact negative-dependence qutrit control

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-398`, with positive commutator-Laplacian support

`0 < q_1 < q_2 < q_3`

and normalized positive sector weights `W=(W_1,W_2,W_3)`.

A source-free mechanism can generate **negative cross-sector dependence** without creating an uncontrolled residual law.

Fix a packet budget `N>=1`. For each packet `n=1,...,N`, choose exactly one sector

`Z_n in {1,2,3}`

independently with

`P(Z_n=i)=p_i`, `p_i>0`, `sum_i p_i=1`.

Conditional on `Z_n=i`, give that packet an independent positive amplitude

`A_n ~ Gamma(alpha_i, rate=lambda_i)`.

Define sector energies

`Y_i=sum_(n: Z_n=i) A_n`

and normalized weights

`W_i=Y_i/(Y_1+Y_2+Y_3)`.

Let

`K_i=#{n: Z_n=i}`.

Then `K=(K_1,K_2,K_3)` is multinomial:

`P(K=k)=N!/(k_1!k_2!k_3!) prod_i p_i^(k_i)`, `sum_i k_i=N`.

Conditional on `K=k`, the sector energies are independent with

`Y_i | K=k ~ Gamma(a_i(k), rate=lambda_i)`,

where

`a_i(k)=alpha_i k_i`,

with `k_i=0` interpreted as the degenerate value `Y_i=0`.

For every full-occupancy component `k_i>=1`, the normalized weight vector has the exact density on the open simplex

`g_k(w)`
` = Gamma(A_k) prod_i [lambda_i^(a_i(k))/Gamma(a_i(k))]`
`   * prod_i w_i^(a_i(k)-1)`
`   / [sum_i lambda_i w_i]^A_k`,

where

`A_k=sum_i a_i(k)`.

Hence the full-occupancy interior law is the finite exact mixture

`f_int(w)=sum_(k_i>=1, sum k_i=N) pi_k g_k(w)`,

with multinomial weights `pi_k=P(K=k)` up to the common full-occupancy conditioning constant. Components with one or more `k_i=0` give explicit lower-dimensional normalized-Gamma laws on simplex faces.

The raw sector energies are negatively correlated for every `i!=j`:

`Cov(Y_i,Y_j)=-N p_i p_j mu_i mu_j < 0`,

where

`mu_i=E[A_n | Z_n=i]=alpha_i/lambda_i`.

Thus **negative cross-sector dependence, nonuniform residual shape, skewness, concentration, and boundary mass can all arise from a finite source-free packet-budget mechanism whose qutrit residual law is exactly calibratable** when `N`, `p_i`, `alpha_i`, and `lambda_i` are fixed independently of the candidate residual.

Fixing the qutrit first moment

`x=m_1=sum_i q_i w_i`

and using the affine residual coordinate `w(u)` from `VIS-389`, the full-occupancy conditional density is exactly

`p(u | x, full occupancy) proportional_to f_int(w(u))`.

If empty-sector events are retained instead of conditioning them away, the fixed-`m_1` residual law is still exact: it is the same continuous interior component together with finitely many explicitly computable boundary atoms from the face components. A randomized probability-integral transform handles those atoms without approximation.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE FIXED-BUDGET NEGATIVE-DEPENDENCE CONTROL + CLASSICAL MULTINOMIAL/DIRICHLET-GAMMA PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY CONSTRUCTION`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Conditional count decomposition

The count vector is multinomial because each of the `N` packets chooses exactly one sector independently.

Condition on `K=k`. For a fixed allocation realizing those counts, sector `i` contains exactly `k_i` independent Gamma variables with common shape `alpha_i` and rate `lambda_i`, so their sum is

`Gamma(alpha_i k_i, lambda_i)`.

The three sector sums are independent because they use disjoint independent packet amplitudes. The conditional joint law depends only on the count vector, not on which packet labels realize it, so averaging over allocations with the same `k` leaves the same product-Gamma law.

This gives an exact finite latent decomposition indexed by the multinomial count vectors.

## 2. Normalization gives a finite normalized-Gamma mixture

For a full-occupancy count vector, write

`Y_i=t w_i`, `t>0`, `w_i>0`, `sum_i w_i=1`.

The simplex Jacobian is `t^2`. The product-Gamma density contributes

`t^(A_k-3) prod_i w_i^(a_i(k)-1)`

and exponential factor

`exp[-t sum_i lambda_i w_i]`.

After multiplying by the Jacobian and integrating out `t`,

`integral_0^infinity t^(A_k-1) exp[-t sum_i lambda_i w_i] dt`
` = Gamma(A_k)/[sum_i lambda_i w_i]^A_k`,

which proves `g_k(w)`.

Averaging over the finitely many multinomial count vectors gives the stated mixture. When all rates are equal, each full-occupancy component reduces to an ordinary Dirichlet law with parameters `(alpha_1 k_1,alpha_2 k_2,alpha_3 k_3)`. Unequal rates give the scaled normalized-Gamma density already familiar from `VIS-391` and `VIS-395`.

The novelty boundary is therefore clear: fixed-budget exclusivity changes the **mixture over sector occupancies** and the dependence mechanism, not the conditional normalized-Gamma algebra inside each count component.

## 3. Exclusive allocation forces negative raw-energy covariance

For one packet define its sector contribution

`V_i=A 1_{Z=i}`.

For `i!=j`, one packet cannot contribute to both sectors, so

`V_i V_j=0` almost surely.

Also

`E[V_i]=p_i mu_i`.

Therefore

`Cov(V_i,V_j)= -p_i p_j mu_i mu_j`.

The `N` packets are independent, hence

`Cov(Y_i,Y_j)=N Cov(V_i,V_j)`
`             =-N p_i p_j mu_i mu_j`.

This mechanism is qualitatively different from the nonnegative additive shared-shock networks of `VIS-396`--`VIS-398`, whose common latent blocks generate nonnegative cross-sector covariance. A fixed packet budget with mutually exclusive allocation supplies a source-free negative-dependence channel instead.

Negative covariance by itself is therefore not evidence of source-specific orientation.

## 4. Exact fixed-`m_1` residual calibration

For fixed generic qutrit support and interior first moment `x`, the constraint

`sum_i q_i w_i=x`

cuts the simplex in the affine segment used throughout `VIS-389`--`VIS-398`. Parametrize its interior by `0<u<1` with affine map `w(u)`.

The slice Jacobian is constant, so under full occupancy

`p(u|x) proportional_to sum_k pi_k g_k(w(u))`,

where the sum runs over `k_i>=1`, `sum_i k_i=N`.

Thus the exact conditional CDF is a finite sum followed by a one-dimensional normalization integral. No simulation asymptotic is needed to define the null.

If empty sectors are permitted, count vectors with `k_i=0` live on simplex faces. For generic `x`, each relevant face meets the fixed-`m_1` slice in at most one point, so those components become explicit atoms in the residual coordinate. The resulting mixed discrete-continuous law is still fully specified. Standard randomized-CDF calibration may be used if a uniformized diagnostic is desired.

As in the preceding nuisance ladder, calibration is valid only when the packet budget, assignment probabilities, amplitude shapes, and rates are fixed by architecture, independent data, or a pre-declared matched control. Choosing them after seeing the candidate residual would make the null post-hoc.

## 5. Consequence for the Wang localization clue

`VIS-398` left signed or negative-dependence mechanisms as one of the next qualitatively different source-free branches. Fixed-budget exclusive allocation closes a substantial part of that branch.

A negative covariance pattern, a skewed fixed-`m_1` residual, or even boundary mass is not enough to claim source information if a plausible source-free mechanism has a fixed packet budget and exclusive sector assignment. The exact finite mixture above provides the appropriate nuisance calibration.

The next useful extension must change mechanism again: genuinely non-Gamma packet amplitudes, signed linear combinations not reducible to exclusive positive allocation, continuous or infinite latent mixtures, admissibility-induced dependence, or another independently justified structure. Those are separate questions and are not pursued here.

## Prior-art and novelty audit

The probability ingredients are classical. Eugene Lukacs, **A Characterization of the Gamma Distribution**, *The Annals of Mathematical Statistics* 26:2 (1955), 319--324, DOI `10.1214/aoms/1177728549`, is a classical anchor for Gamma sum/proportion structure underlying normalized-Gamma and Dirichlet constructions.

James E. Mosimann, **On the compound multinomial distribution, the multivariate beta-distribution, and correlations among proportions**, *Biometrika* 49:1--2 (1962), 65--82, DOI `10.1093/biomet/49.1-2.65`, is direct prior art for compound multinomial/multivariate-beta constructions and correlation among proportions.

No novelty is claimed for multinomial allocation, Gamma aggregation, Dirichlet/normalized-Gamma mixtures, or negative dependence induced by exclusive finite allocation. The Mathia-specific result is the exact placement of this classical source-free mechanism inside the one-dimensional qutrit residual calibration ladder and the resulting falsification boundary: negative dependence and boundary/skew effects do not constitute Wang source evidence when this independently specified packet-budget null is admissible.

## Boundaries

- The packet budget `N` is finite and fixed independently of the candidate residual.
- Each packet chooses exactly one sector; this is the source of the negative raw-energy covariance.
- Packet choices are independent across packets with fixed probabilities `p_i`.
- Conditional packet amplitudes are Gamma with fixed positive shapes and rates; genuinely non-Gamma amplitudes remain open.
- Parameters may be independently estimated or fixed by architecture, but they may not be tuned to the residual being tested.
- Full occupancy gives a purely continuous simplex mixture; allowing empty sectors adds exact lower-dimensional face components and fixed-`m_1` boundary atoms.
- The result does not cover arbitrary negative-dependence copulas, signed latent factors, packet interactions, infinite packet budgets with nontrivial scaling limits, or Wang-admissibility constraints that couple packet allocation to arithmetic source data.
- Exact finite-mixture specification means the null can be calibrated to arbitrary numerical precision; it does not imply a closed-form elementary CDF for every parameter choice.
- No retained visualization is required because the useful result is an exact representation-independent probability decomposition once the qutrit reduction is fixed.
