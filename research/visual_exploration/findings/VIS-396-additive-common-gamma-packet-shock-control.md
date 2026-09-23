# VIS-396 — additive common-gamma packet shocks give an exact dependent qutrit nuisance family

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-395`, with positive commutator-Laplacian support

`0 < q_1 < q_2 < q_3`

and positive tangent sectors `H_1,H_2,H_3`.

Let the source-free packet energies contain both sector-specific Gaussian replicas and a shared packet block. For independently specified integers `k_i>=1`, `k_0>=1`, and a common rate `lambda>0`, take independent

`X_i ~ Gamma(k_i, rate=lambda)`,

`C ~ Gamma(k_0, rate=lambda)`,

and define the dependent sector energies

`Y_i = X_i + C`.

Then each marginal is `Gamma(k_i+k_0,lambda)` while, for `i!=j`,

`Cov(Y_i,Y_j)=Var(C)=k_0/lambda^2 > 0`.

Thus this is a genuine cross-sector dependence mechanism not covered by the independent-Gamma ladder of `VIS-391`, `VIS-394`, and `VIS-395`.

Write

`S=X_1+X_2+X_3`, `K=k_1+k_2+k_3`,

`p_i=X_i/S`,

and normalize the dependent energies by

`w_i=Y_i/(Y_1+Y_2+Y_3)`.

Because the `X_i` have a common rate,

`p=(p_1,p_2,p_3) ~ Dirichlet(k_1,k_2,k_3)`

and `p` is independent of `S`. If

`r = 3C/(S+3C)`,

then `p` is independent of `r` and the normalized weights have the exact random-shrinkage representation

`w_i = (1-r)p_i + r/3`.

The shared packet block therefore pulls an ordinary Dirichlet draw toward the simplex barycenter by an independent random amount.

The shrinkage variable has exact density

`f_R(r)`
` = [Gamma(K+k_0)/(Gamma(K)Gamma(k_0) 3^k_0)]`
`   * r^(k_0-1) (1-r)^(K-1)`
`   / (1-2r/3)^(K+k_0)`,

for `0<r<1`.

Equivalently, the exact normalized-weight density on the open simplex is the one-dimensional mixture

`f_W(w)`
` = Gamma(K+k_0)/(Gamma(k_0) prod_i Gamma(k_i) 3^k_0)`
`   * integral_0^(3 min_i w_i)`
`       [r^(k_0-1) prod_i (w_i-r/3)^(k_i-1)]`
`       / (1-2r/3)^(K+k_0) dr`.

Fixing the qutrit first moment

`x=m_1=sum_i q_i w_i`

and using the affine residual coordinate `w(u)` from `VIS-389`, the conditional residual density is therefore exactly

`p(u | x,q,k,k_0) proportional_to f_W(w(u))`.

Its one-dimensional normalization and CDF give an exact probability-integral-transform uniformizer for this additive common-shock control whenever `(k_1,k_2,k_3,k_0)` is fixed independently of the candidate residual.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE DEPENDENT MECHANISTIC CONTROL + CLASSICAL COMMON-COMPONENT MULTIVARIATE-GAMMA PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY FAMILY`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Shared packet energy is genuine dependence, not a scale gauge

A common multiplicative packet scale would disappear after normalizing the three sector energies, so it cannot enlarge the residual-shape null. An additive shared packet block behaves differently.

With `Y_i=X_i+C`, each pair shares the same positive random contribution. Since the idiosyncratic `X_i` are mutually independent and independent of `C`,

`Cov(Y_i,Y_j)=Var(C)=k_0/lambda^2`.

The dependence is therefore explicit and source-free. At the same time each marginal remains gamma because the common and idiosyncratic pieces have the same rate:

`Y_i ~ Gamma(k_i+k_0,lambda)`.

This is the classical common-component multivariate-gamma construction associated with Cheriyan and Ramabhadran. The use here is only as a qutrit nuisance mechanism; no novelty is claimed for the multivariate probability family.

## 2. Exact random shrinkage toward the barycenter

Because `S=sum_i X_i ~ Gamma(K,lambda)`, standard gamma-Dirichlet factorization gives

`p_i=X_i/S`,

`p ~ Dirichlet(k_1,k_2,k_3)`,

with `p` independent of `S`. Since `C` is also independent, `p` is independent of every function of `(S,C)`, in particular of

`r=3C/(S+3C)`.

Now

`Y_1+Y_2+Y_3=S+3C`,

so

`w_i=(Sp_i+C)/(S+3C)=(1-r)p_i+r/3`.

Thus the common shock does not create an arbitrary dependent law. It creates a very specific random contraction of the Dirichlet simplex toward its barycenter. This is a falsifiable source-free restriction.

## 3. Exact law of the shrinkage variable

Use the change of variables

`S=(1-r)t`,

`C=rt/3`,

where `t=S+3C`. Its Jacobian is `t/3`. Multiplying the independent gamma densities gives a factor

`t^(K+k_0-1) r^(k_0-1)(1-r)^(K-1) 3^(-k_0)`

with exponential term

`exp[-lambda t(1-2r/3)]`.

Integrating `t` over `(0,infinity)` yields

`f_R(r)`
` = [Gamma(K+k_0)/(Gamma(K)Gamma(k_0) 3^k_0)]`
`   * r^(k_0-1)(1-r)^(K-1)`
`   / (1-2r/3)^(K+k_0)`.

The rate `lambda` cancels. Hence the normalized control depends only on the independently specified packet counts, exactly as a scale-free nuisance family should.

## 4. Exact simplex density

Conditional on `r`, the map from the Dirichlet draw to the normalized dependent weights is

`w = (1-r)p + r(1,1,1)/3`.

Its support is the shrunken simplex `w_i>r/3`, and its two-dimensional Jacobian contributes `(1-r)^(-2)`. Substituting

`p_i=(w_i-r/3)/(1-r)`

into the Dirichlet density gives

`f(w|r)`
` = [Gamma(K)/prod_i Gamma(k_i)]`
`   * prod_i (w_i-r/3)^(k_i-1)`
`   / (1-r)^(K-1)`.

For fixed interior `w`, admissible `r` satisfies

`0<r<3 min_i w_i`.

Multiplying by `f_R(r)` cancels the factor `(1-r)^(K-1)` exactly and gives the stated one-dimensional integral for `f_W(w)`.

This integral is finite and deterministic for positive integer packet counts. It therefore supplies a concrete dependent null rather than an unconstrained symmetry family.

## 5. Conditioning on the qutrit first moment

On the fixed-source qutrit simplex, `m_1=x` cuts the simplex by the same affine segment used in `VIS-389`--`VIS-395`. Parametrize it by `0<u<1` as `w(u)`. The slice Jacobian is constant, so restricting the exact simplex density changes it only by an `u`-independent factor:

`p(u|x,q,k,k_0) proportional_to f_W(w(u))`.

Hence the additive common-shock family admits an exact conditional CDF and probability-integral transform just like the independent-Gamma controls, although the density now contains one additional finite integral over the latent shared-energy fraction `r`.

A candidate qutrit residual that only rejects the independent-Gamma ladder of `VIS-395` is therefore still not source evidence if a shared source-free packet block is architecturally admissible.

## 6. Consequence for the Wang localization clue

`VIS-395` left cross-sector dependence as one obvious uncalibrated nuisance direction. This finding closes the simplest such direction: a shared additive Gaussian-packet energy with independently fixed replica count.

The next stronger null must use genuinely additional structure, for example non-Gaussian packet amplitudes, a more structured dependence law than one additive common gamma block, or a Wang admissibility constraint that derives a coupled distribution. As before, every extra nuisance parameter must be fixed from architecture or independent controls rather than fitted to the candidate residual.

## Prior-art and novelty audit

The common-component gamma construction is classical. Cheriyan, **A bivariate correlated gamma-type distribution function**, *Journal of the Indian Mathematical Society* 5 (1941), 133--144, studies the bivariate shared-component construction. Ramabhadran, **A multivariate gamma-type distribution**, *Sankhya* 11 (1951), 45--46, gives the multivariate extension. Modern reference treatments list the Cheriyan--Ramabhadran family among standard multivariate gamma models.

The gamma-Dirichlet factorization, beta/gamma ratio changes of variables, and conditioning of a density on an affine simplex slice are likewise classical probability operations.

No novelty is claimed for any of those probability constructions. The Mathia-specific result is the exact placement of this **additive shared Gaussian-packet mechanism** inside the qutrit Wang nuisance hierarchy and the resulting conclusion that independently calibrated cross-sector correlation and barycentric concentration can be source-free.

## Boundaries

- The shared component is additive and identical in all three sector energies. A common multiplicative scale cancels after normalization and is not a new control.
- The derivation assumes a common gamma rate `lambda` for the idiosyncratic and shared components. Unequal common/idiosyncratic rates lead to a broader family not derived here.
- Counts `(k_1,k_2,k_3,k_0)` are mechanism parameters tied to packet multiplicity; fitting them to the candidate residual would invalidate the calibration.
- This control models one shared latent packet block. More general cross-sector covariance, copula structure, non-Gaussian amplitudes, or admissibility-induced coupling is not exhausted.
- Source support `{q_1,q_2,q_3}` and the conditioning value `m_1` are fixed.
- Rejecting this dependent null does not identify arithmetic structure; it removes only one further explicit source-free mechanism.
- No retained visualization is required because the useful result is an exact representation-independent probability decomposition once the qutrit reduction is fixed.
