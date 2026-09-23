# VIS-395 — unequal packet replica counts give the full integer-shape normalized-gamma qutrit ladder

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-394`. Let

`0 < q_1 < q_2 < q_3`

be the three positive support points of the intrinsic source-subspace commutator Laplacian, and let the positive tangent space split into the three real two-dimensional root sectors `H_1,H_2,H_3`.

For each sector choose an independently specified positive integer replica count `k_i>=1` and rate `lambda_i>0`. Let

`Y_i = sum_(r=1)^(k_i) |Z_(i,r)|^2 ~ Gamma(k_i, rate=lambda_i)`

independently across `i=1,2,3`, where the replicas are centered circular Gaussians. Define

`T=Y_1+Y_2+Y_3`,

`w_i=Y_i/T`,

and `K=k_1+k_2+k_3`.

Then the exact normalized sector-weight density on the open simplex is

`f_(k,lambda)(w)`
` = [Gamma(K)/prod_i Gamma(k_i)]`
`   * [prod_i lambda_i^(k_i) w_i^(k_i-1)]`
`   / [sum_i lambda_i w_i]^K`.

Thus `VIS-394` is exactly the diagonal subfamily `k_1=k_2=k_3=k`. With equal rates the denominator is constant and the weight law becomes the ordinary asymmetric Dirichlet distribution

`Dirichlet(k_1,k_2,k_3)`.

Now fix an interior first moment

`x=m_1=sum_i q_i w_i`

and use the same affine residual coordinate `0<u<1` as `VIS-389`--`VIS-394`, so

`w(u)=(1-u)w^L(x)+u w^U(x)`.

Because the slice Jacobian is constant, the exact conditional residual density is

`p_(k,lambda)(u | x,q)`
` proportional_to prod_i w_i(u)^(k_i-1)`
`                / [sum_i lambda_i w_i(u)]^K`.

Its one-dimensional normalization and CDF therefore give an exact probability-integral-transform uniformizer whenever the replica-count vector and sector rates are fixed independently of the candidate residual.

For equal rates, the conditional density reduces to

`p_k(u|x,q) proportional_to prod_i w_i(u)^(k_i-1)`.

On every generic nondegenerate qutrit slice, this is constant only for the one-replica vector `(1,1,1)`. Consequently unequal source-free replica architecture can produce skewed or otherwise structured nonuniform residual laws even when all sector scales are identical.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE MECHANISTIC CONTROL + CLASSICAL NORMALIZED-GAMMA/DIRICHLET PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY FAMILY`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Sectorwise packet multiplicity gives arbitrary integer Gamma shapes

`VIS-394` assumed the same packet-replica count in every root sector. That is natural for a fully replicated architecture but is not forced by source-free packet construction in general. If sector `i` aggregates `k_i` independent circular-Gaussian replicas, each squared amplitude is exponential with rate `lambda_i`, hence

`Y_i ~ Gamma(k_i, rate=lambda_i)`.

The only new mechanism here is unequal multiplicity. The vector `(k_1,k_2,k_3)` must therefore come from an independently specified architecture, admissibility rule, or control construction. Treating the three counts as post-hoc shape parameters would turn the null into residual fitting rather than calibration.

## 2. Exact normalized-Gamma density

Write `Y_i=T w_i` with `sum_i w_i=1`. The simplex change of variables has Jacobian `T^2`. Multiplying the independent Gamma densities yields

`[prod_i lambda_i^(k_i)/Gamma(k_i)]`
` * T^(K-1) prod_i w_i^(k_i-1)`
` * exp[-T A(w)]`,

where

`A(w)=sum_i lambda_i w_i`.

Integrating out `T` gives

`integral_0^infinity T^(K-1) exp[-A(w)T] dT = Gamma(K)/A(w)^K`,

which proves the stated simplex density.

The common-count family of `VIS-394` follows by setting every `k_i=k`. The one-replica sector-scaled Gaussian family of `VIS-391` is the further specialization `k_i=1` for all `i`. Equal rates remove `A(w)` entirely and recover `Dirichlet(k_1,k_2,k_3)`.

## 3. Conditioning on the qutrit first moment

For fixed source support and an interior value `m_1=x`, the feasible weights form the affine segment already parametrized in `VIS-389` by `u`. Restricting the simplex density to this line changes it only by an `u`-independent geometric factor. Therefore

`p_(k,lambda)(u|x,q)`
` = C_(k,lambda)(x,q)`
`   prod_i w_i(u)^(k_i-1)`
`   / A(w(u))^K`,

where `C_(k,lambda)` is the reciprocal of the integral over the admissible `u` interval.

Every `w_i(u)` and `A(w(u))` is affine. For integer `k_i`, the numerator is polynomial and the denominator is an affine function raised to the integer power `K`; the defining one-dimensional integral is therefore explicit and deterministic even when a compact closed form is not useful.

The conditional CDF

`F_(k,lambda)(u|x,q)`

is consequently an exact null uniformizer for a pre-specified unequal-replica architecture.

## 4. Equal sector scale still permits structured residual shape

Set `lambda_1=lambda_2=lambda_3=lambda`. Then `A(w)=lambda`, so

`p_k(u|x,q) proportional_to prod_i w_i(u)^(k_i-1)`.

For a generic interior slice, the three barycentric coordinates are affine functions of `u`, the segment meets two distinct simplex edges, and the coordinate that does not vanish at an endpoint still varies along the segment. If any exponent `k_i-1` is positive, the displayed product is therefore nonconstant; equivalently, a constant conditional density requires `k_1=k_2=k_3=1`.

This matters because residual skew, endpoint suppression, or interior concentration can now arise under a completely source-free equal-rate mechanism. Unequal packet multiplicity alone is sufficient. Such shape cannot be interpreted as arithmetic orientation unless the actual architecture rules out the corresponding count vector before the residual is inspected.

## 5. Consequence for the Wang localization clue

The exact mechanistic nuisance ladder is now broader:

- `VIS-390`: one isotropic Gaussian block per sector;
- `VIS-391`: one independently scaled Gaussian block per sector;
- `VIS-394`: a common replicated-Gaussian count `k` with independently fixed sector rates;
- this finding: an independently specified sectorwise count vector `(k_1,k_2,k_3)` with independently fixed rates.

The progression is not a license to fit ever more flexible distributions. Each enlargement is admissible only when a source-free mechanism fixes its extra degrees of freedom independently of the candidate residual. Once that condition is met, the exact conditional CDF removes the corresponding nuisance shape before any source-specific interpretation.

The next informative extension must therefore add a genuinely different mechanism: cross-sector dependence, non-Gaussian replica amplitudes, an admissibility-induced coupling, or another independently constrained source-free structure. Unequal replica architecture is no longer an uncovered escape.

## Prior-art and novelty audit

The probability family is classical. Independent Gamma variables normalized by their sum produce the Dirichlet family at common scale and the scaled-Dirichlet/normalized-Gamma family at unequal scales. Monti, Mateu-Figueras, and Pawlowsky-Glahn, **Notes on the Scaled Dirichlet Distribution**, in *Compositional Data Analysis: Theory and Applications* (Wiley, 2011), pp. 128--138, DOI `10.1002/9781119976462.ch10`, is the existing Mathia prior-art anchor used already by `VIS-391` and `VIS-394`.

No novelty is claimed for Gamma summation, arbitrary positive Dirichlet shape vectors, normalized independent Gamma variables, scaled-Dirichlet densities, affine conditioning, or probability-integral transforms.

The Mathia-specific result is the exact placement of **sectorwise integer Gamma shapes forced by unequal Gaussian packet multiplicities** inside the qutrit Wang nuisance hierarchy, together with the negative conclusion that equal sector scale does not make a fixed-`m_1` residual uniform once any sector contains more than one independent packet replica.

## Boundaries

- Every `k_i` is a mechanism parameter tied to a replica count, not a free fitted concentration parameter.
- The derivation assumes independent replicas and independent sectors, with scalar Gaussian rate within each sector. Cross-sector dependence and non-Gaussian amplitudes are not covered.
- The integer-shape restriction reflects literal Gaussian replica counting. General positive Gamma shapes are mathematically classical but require a different mechanism if used as a Wang control.
- Source support `{q_1,q_2,q_3}` and conditioning value `m_1` are fixed; source-spectrum variation is not calibrated here.
- The nonuniformity statement concerns generic nondegenerate qutrit slices. Symmetry-enhanced or collapsed boundary cases remain governed by the earlier qutrit classification.
- Rejecting this null does not identify arithmetic structure; it only removes one additional source-free packet architecture.
- No retained visualization is needed because the result is an exact representation-independent probability calculation once the qutrit reduction is fixed.
