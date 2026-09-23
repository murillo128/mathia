# VIS-394 — replicated Gaussian packet blocks give an exact normalized-gamma qutrit control

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-393`. Let

`0 < q_1 < q_2 < q_3`

be the three positive support points of the intrinsic source-subspace commutator Laplacian, and let the positive tangent space split into the three real two-dimensional root sectors `H_1,H_2,H_3`.

Fix an integer `k>=1`. In each sector take `k` independent centered circular Gaussian packet replicas with sector-specific rate `lambda_i>0`, normalized so that every squared replica amplitude is exponential with that rate. Thus

`Y_i = sum_(r=1)^k |Z_(i,r)|^2 ~ Gamma(k, rate=lambda_i)`

independently across `i=1,2,3`. Define

`T=Y_1+Y_2+Y_3`,

`w_i=Y_i/T`.

Then on the open probability simplex the exact weight density is

`f_k(w)`
` = [Gamma(3k)/Gamma(k)^3]`
`   * (lambda_1 lambda_2 lambda_3)^k`
`   * (w_1 w_2 w_3)^(k-1)`
`   / (lambda_1 w_1+lambda_2 w_2+lambda_3 w_3)^(3k)`.

For `k=1` this is exactly the sector-anisotropic scaled-Dirichlet law of `VIS-391`. For equal rates it reduces to the ordinary symmetric `Dirichlet(k,k,k)` law.

Now fix an interior first moment

`x=m_1=sum_i q_i w_i`

and use the same affine residual coordinate `0<u<1` as `VIS-389`--`VIS-391`, so

`w(u)=(1-u)w^L(x)+u w^U(x)`.

Because this slice is affine and its geometric Jacobian is constant, the exact conditional residual density is

`p_k(u | x,q,lambda)`
` proportional_to [w_1(u)w_2(u)w_3(u)]^(k-1)`
`                / [lambda_1 w_1(u)+lambda_2 w_2(u)+lambda_3 w_3(u)]^(3k)`.

The normalization is the one-dimensional integral over `0<u<1`, so its conditional CDF gives an exact probability-integral-transform uniformizer for every fixed `k,q,lambda`.

A useful negative consequence is immediate. If the sector rates are equal, the denominator is constant on the simplex, but for every nondegenerate fixed-`m_1` slice the product `w_1(u)w_2(u)w_3(u)` is nonconstant. Hence for every `k>1` the residual `u` is **not** uniform even under fully isotropic replicated Gaussian packets. The uniform conditional null of `VIS-390` is the special one-replica case `k=1`, not a generic consequence of isotropy.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE MECHANISTIC CONTROL + CLASSICAL NORMALIZED-GAMMA/SCALED-DIRICHLET PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY FAMILY`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Replica aggregation fixes the Gamma shape

The point of this extension is not to fit a more flexible simplex density. The shape parameter `k` is tied to an explicit source-free mechanism: each sector energy is the sum of `k` independent Gaussian packet-replica energies.

For a centered circular complex Gaussian replica in sector `i`, the squared amplitude has exponential density

`lambda_i exp(-lambda_i y)`.

Summing `k` independent replicas gives

`f_(Y_i)(y)`
` = lambda_i^k y^(k-1) exp(-lambda_i y)/Gamma(k)`

for `y>0`. The three sector energies remain independent when the packet replicas are independent across sectors.

This is a strictly stronger nuisance family than the one-replica Gaussian ladder only when the repeated-packet mechanism is independently justified. Treating `k` as a post-hoc residual-shape parameter would destroy the intended calibration boundary.

## 2. Exact normalized-Gamma simplex density

Write

`Y_i=T w_i`,

with `w_1+w_2+w_3=1`. The simplex change of variables has Jacobian `T^2`. Multiplying the three Gamma densities therefore gives the joint density in `(T,w)` proportional to

`T^(3k-1) (w_1w_2w_3)^(k-1)`
` * exp[-T A(w)]`,

where

`A(w)=lambda_1w_1+lambda_2w_2+lambda_3w_3`.

The exact prefactor before integrating `T` is

`(lambda_1lambda_2lambda_3)^k/Gamma(k)^3`.

Since

`integral_0^infinity T^(3k-1) exp[-A(w)T] dT`
` = Gamma(3k)/A(w)^(3k)`,

the stated simplex density follows.

Two checks are immediate. At `k=1`, `Gamma(3)=2` and the polynomial factor disappears, recovering `VIS-391`. If all rates are equal, `A(w)` is constant because the weights sum to one; the remaining density is exactly the symmetric Dirichlet density with concentration vector `(k,k,k)`.

## 3. Conditioning on the qutrit first moment

`VIS-389` shows that fixing `m_1=x` leaves one affine degree of freedom. The residual coordinate `u` parametrizes the segment between the lower and upper feasible second-moment endpoints,

`w(u)=(1-u)w^L(x)+u w^U(x)`.

The map from `u` to that line segment has constant speed, so conditioning the simplex density on the slice changes it only by an `u`-independent factor. This gives

`p_k(u|x,q,lambda)`
` = C_k(x,q,lambda)`
`   [prod_i w_i(u)]^(k-1)`
`   / A(w(u))^(3k)`,

where `C_k` is the reciprocal of the integral of the displayed shape over the admissible interval.

For integer `k`, the numerator is a polynomial in `u` and the denominator is an affine function raised to an integer power. The one-dimensional normalization and CDF are therefore exact elementary integrals; a closed symbolic expression is not needed for the calibration because the defining integral is already explicit and deterministic.

The probability-integral transform

`v_k = F_(k,lambda)(u|x,q)`

is exactly uniform under the specified replicated-packet null.

## 4. Isotropy no longer means a uniform residual

Set

`lambda_1=lambda_2=lambda_3=lambda`.

Then `A(w)=lambda` on the simplex and

`p_k(u|x,q) proportional_to [w_1(u)w_2(u)w_3(u)]^(k-1)`.

For a nondegenerate qutrit slice, at least two barycentric coordinates vary affinely with `u`; their product, and hence the full three-coordinate product, cannot be constant on an open interval. Therefore `p_k` is nonuniform for every `k>1`.

This removes another false-positive route. A structured nonuniform residual after the `VIS-390` isotropic one-replica calibration can arise from source-free repeated-packet aggregation even when all three sectors have identical scale. It need not reflect arithmetic orientation or source coupling.

Conversely, the effect is falsifiable because the whole residual law is fixed once the replica count and sector rates are fixed independently of the candidate residual.

## 5. Consequence for the Wang localization clue

`VIS-393` showed that source-stabilizer symmetry alone cannot select any informative non-Gaussian residual law. The present finding supplies a first larger non-Gaussian family whose restriction comes from an explicit mechanism rather than symmetry: finite aggregation of independent Gaussian packet replicas.

A legitimate Wang control can therefore pre-register a replica architecture `k` and independently calibrate the rate ratios `lambda_i`, then transform the observed qutrit residual with the exact conditional CDF above. The candidate source family must remain exceptional after this correction before any source-specific interpretation is considered.

This does not finish the accepted Wang clue. Correlated replicas, unequal sector replica counts, non-Gaussian packet amplitudes, admissibility-induced dependence, and other source-free mechanisms remain outside the family. The value of this result is that those extensions now have to be justified by concrete mechanism rather than added merely to absorb the observed residual.

## Prior-art and novelty audit

The probability construction is classical. Normalizing equal-scale independent Gamma variables gives the ordinary Dirichlet family, and allowing unequal scales gives the scaled-Dirichlet/normalized-Gamma extension. Monti, Mateu-Figueras, and Pawlowsky-Glahn, **Notes on the Scaled Dirichlet Distribution**, in *Compositional Data Analysis: Theory and Applications* (Wiley, 2011), pp. 128--138, DOI `10.1002/9781119976462.ch10`, is an explicit prior-art anchor for that scaled-Dirichlet construction. `VIS-391` already used this source for the `k=1` qutrit specialization.

No novelty is claimed for Gamma summation, normalized independent Gamma vectors, Dirichlet or scaled-Dirichlet densities, affine conditioning, or the probability-integral transform.

The Mathia-specific contribution is the exact placement of the common integer Gamma shape inside the qutrit Wang control hierarchy: a literal `k`-replica Gaussian packet mechanism forces the displayed simplex law and its fixed-`m_1` residual law, and it proves that isotropic source-free aggregation with `k>1` already destroys the uniform residual used by the one-replica null.

## Boundaries

- `k` is a mechanism parameter, not a free goodness-of-fit parameter. If the packet architecture does not independently specify or constrain the replica count, this family is not a valid stronger null.
- The derivation assumes independent replicas and independent sectors, with a common replica count `k` and a scalar rate within each sector. Correlated blocks, unequal shapes, heavy tails, and nonlinear admissibility constraints are not covered.
- The source support `{q_1,q_2,q_3}` and the conditioning value `m_1` are fixed. The finding does not calibrate source-spectrum variation.
- Equal rates imply symmetric `Dirichlet(k,k,k)` weights, but for `k>1` that does not imply a uniform fixed-`m_1` residual.
- Rejection of this null does not identify arithmetic structure; it only removes one explicit source-free repeated-packet mechanism.
- No retained visualization is needed because the result is an exact representation-independent probability calculation once the qutrit reduction is fixed.
