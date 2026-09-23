# VIS-397 — unequal packet rates preserve exact common-gamma qutrit calibration

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-396`, with positive commutator-Laplacian support

`0 < q_1 < q_2 < q_3`

and positive tangent sectors `H_1,H_2,H_3`.

Let the source-free packet energies contain sector-specific Gamma blocks with independently specified rates together with one shared additive Gamma block. For independently specified integers `k_i>=1`, `k_0>=1` and positive rates `lambda_i,lambda_0`, take independent

`X_i ~ Gamma(k_i, rate=lambda_i)`,

`C ~ Gamma(k_0, rate=lambda_0)`,

and define

`Y_i = X_i + C`.

Normalize by

`W_i = Y_i/(Y_1+Y_2+Y_3)`.

Write

`K=k_1+k_2+k_3`, `M=K+k_0`.

Then the normalized weight vector `W=(W_1,W_2,W_3)` has the exact density on the open simplex

`f_W(w)`
` = [Gamma(M) lambda_0^k_0 prod_i lambda_i^k_i]`
`   / [3^k_0 Gamma(k_0) prod_i Gamma(k_i)]`
`   * integral_0^(3 min_i w_i)`
`       r^(k_0-1) prod_i (w_i-r/3)^(k_i-1)`
`       / A(w,r)^M dr`,

where

`A(w,r)=sum_i lambda_i w_i + (r/3)(lambda_0-sum_i lambda_i)`

or, equivalently,

`A(w,r)=lambda_0 r/3 + sum_i lambda_i (w_i-r/3)`.

The second form makes positivity transparent on the integration domain.

Thus allowing independently specified sector rates and a different shared-block rate does **not** make the additive common-shock nuisance analytically uncontrolled. It removes the simple independent-Dirichlet/random-shrinkage factorization of `VIS-396`, but the normalized law remains a finite-dimensional exact one-integral family.

For `i!=j`,

`Cov(Y_i,Y_j)=Var(C)=k_0/lambda_0^2>0`,

so the model retains genuine source-free cross-sector dependence. When all rates coincide,

`lambda_1=lambda_2=lambda_3=lambda_0=lambda`,

the density reduces exactly to `VIS-396`.

Fixing the qutrit first moment

`x=m_1=sum_i q_i w_i`

and using the affine residual coordinate `w(u)` from `VIS-389`, the conditional residual density is exactly

`p(u | x,q,k,k_0,lambda,lambda_0) proportional_to f_W(w(u))`.

Its one-dimensional normalization and CDF therefore give an exact probability-integral-transform uniformizer whenever the packet counts and rate ratios are fixed independently of the candidate residual.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE DEPENDENT MECHANISTIC CONTROL + CLASSICAL GAMMA-CONVOLUTION PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY INGREDIENTS`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Unequal rates create a real extension

`VIS-396` assumed one common rate. That special case has two simplifying properties: each marginal `Y_i=X_i+C` remains Gamma, and gamma-Dirichlet factorization makes the idiosyncratic proportions independent of their total. With unequal rates, neither simplification is generally available.

The dependence mechanism itself survives unchanged. Because the `X_i` are mutually independent and independent of `C`,

`Cov(Y_i,Y_j)=Var(C)=k_0/lambda_0^2`.

So this is not a scale reparameterization of the independent-Gamma ladder. It is the same additive shared-component mechanism with a larger, independently interpretable nuisance surface.

## 2. Exact normalized density

Start from the joint density of `Y`. For positive `y_i`, introduce the latent shared contribution `c`:

`f_Y(y)=integral_0^(min_i y_i) f_C(c) prod_i f_Xi(y_i-c) dc`.

Now write

`y_i=t w_i`, `sum_i w_i=1`, `t>0`,

and parameterize the shared fraction by

`c=t r/3`.

The support condition `0<c<min_i y_i` becomes

`0<r<3 min_i w_i`.

The transformation from `(w_1,w_2,t,r)` to `(y_1,y_2,y_3,c)` has absolute Jacobian `t^3/3`. The Gamma power factors contribute

`t^(K-3) * t^(k_0-1)`,

so after the Jacobian the total scale power is `t^(M-1)`. The exponential factor is

`exp[-t A(w,r)]`,

with

`A(w,r)=lambda_0 r/3 + sum_i lambda_i(w_i-r/3)`.

Integrating the scale variable gives

`integral_0^infinity t^(M-1) exp[-A t] dt = Gamma(M)/A^M`,

which yields the stated simplex density.

This derivation uses only ordinary Gamma densities and a change of variables; no asymptotic approximation is involved.

## 3. Equal-rate specialization recovers VIS-396

If all four rates equal `lambda`, then

`A(w,r)=lambda[1-2r/3]`.

The factor `lambda^M` in the numerator cancels `A(w,r)^M`, leaving

`f_W(w)`
` = Gamma(M)/[3^k_0 Gamma(k_0) prod_i Gamma(k_i)]`
`   * integral_0^(3 min_i w_i)`
`       r^(k_0-1) prod_i(w_i-r/3)^(k_i-1)`
`       /(1-2r/3)^M dr`,

which is exactly the normalized-weight density in `VIS-396`.

This specialization is a direct consistency check on the unequal-rate formula.

## 4. Conditioning on the qutrit residual coordinate

For fixed qutrit source support `q_1<q_2<q_3`, the condition

`m_1=x=sum_i q_i w_i`

cuts the simplex by the affine segment already used in `VIS-389`--`VIS-396`. Parametrize that segment by the normalized residual coordinate `0<u<1`, giving an affine map `w(u)`.

Because the slice Jacobian is constant in `u`, the exact conditional density is proportional to `f_W(w(u))`. Numerical quadrature of one finite integral in `r`, followed by one-dimensional normalization in `u`, is therefore sufficient to obtain the exact nuisance CDF to arbitrary numerical precision. No fit to the candidate residual is required or allowed.

The extra rate ratios are legitimate nuisance parameters only when architecture, calibration data, or matched controls fix them independently. Allowing them to be optimized against the same residual being judged would turn a mechanistic control into post-hoc fitting.

## 5. Consequence for the Wang localization clue

Rejecting the common-rate shared-block model of `VIS-396` is not source evidence when unequal sector or shared rates are independently plausible. The exact family above absorbs that extension without surrendering falsifiability.

The next useful source-free extension must therefore add genuinely different structure rather than another rate relaxation of the same one-shared-block Gamma mechanism. Examples include non-Gamma packet-amplitude laws, several shared latent blocks coupling different sector subsets, or a Wang admissibility constraint that derives a coupled law from the construction itself.

Those are separate research questions. This finding closes only the unequal-rate version of the single additive common-Gamma block and does not pursue the next mechanism in the same investigation.

## Prior-art and novelty audit

Shared-component multivariate-Gamma constructions are classical; `VIS-396` already records the Cheriyan--Ramabhadran lineage for the common-component model. Sums of independent Gamma variables with unequal parameters are also classical. P. G. Moschopoulos, **The distribution of the sum of independent gamma random variables**, *Annals of the Institute of Statistical Mathematics* 37 (1985), 541--544, gives an exact treatment of sums of independent Gamma variates with different parameters.

The Mathia-specific contribution here is not a new multivariate-Gamma family or a new theorem about Gamma convolutions. It is the exact normalized-simplex density obtained after applying the unequal-rate shared-component mechanism to the qutrit nuisance geometry, together with the resulting conclusion that this larger source-free family remains exactly conditionally calibratable.

## Boundaries

- The model contains exactly one additive common Gamma block shared equally by all three sector energies. Several shared blocks or subset-specific shocks are not covered.
- Sector and shared rates are arbitrary positive constants but must be independently specified or calibrated outside the candidate residual.
- For unequal rates, the marginals `Y_i` are generally Gamma convolutions rather than single Gamma laws; no stronger marginal-Gamma claim is made.
- Packet counts are kept as positive integers to preserve the Gaussian-replica interpretation, although the density derivation itself extends to positive Gamma shapes.
- The qutrit source support and conditioning value `m_1` are fixed.
- Exact calibratability does not imply that this null is physically or architecturally appropriate for a particular Wang construction; that justification is separate.
- Rejecting this family does not identify arithmetic structure. It removes only the unequal-rate single-common-block nuisance mechanism.
- No retained visualization is required because the useful result is an exact representation-independent probability decomposition once the qutrit reduction is fixed.
