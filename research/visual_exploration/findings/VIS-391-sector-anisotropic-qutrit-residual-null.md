# VIS-391 — sector-anisotropic Gaussian tangents give an exact qutrit residual null

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-390`. Let

`0 < q_1 < q_2 < q_3`

be the three positive eigenvalues of the intrinsic source-subspace commutator Laplacian `Delta_S`, with corresponding real root sectors

`V_+ = H_1 direct_sum H_2 direct_sum H_3`,

`dim_R H_i = 2`.

`VIS-390` calibrated the source-free isotropic tangent null by taking a Haar-uniform direction in `V_+`, which makes the sector weights `Dirichlet(1,1,1)` and the residual qutrit coordinate

`u = [m_2-L(m_1)]/[U(m_1)-L(m_1)]`

uniform conditional on the first moment `m_1`.

There is an exact stronger nuisance family that allows nonarithmetic sector anisotropy. Take independent centered Gaussian blocks

`Z_i ~ N(0, sigma_i^2 I_(H_i))`,

with arbitrary fixed `sigma_i>0`, put

`g = (Z_1+Z_2+Z_3)/||Z_1+Z_2+Z_3||_F`,

and define sector weights

`w_i = ||P_i g||_F^2`.

Set

`lambda_i = 1/(2 sigma_i^2)`

and

`A(w)=lambda_1 w_1+lambda_2 w_2+lambda_3 w_3`.

Then on the probability simplex

`f_W(w_1,w_2,w_3) = 2 lambda_1 lambda_2 lambda_3 / A(w)^3`.

Thus unequal sector variances replace the uniform `Dirichlet(1,1,1)` simplex law by the corresponding scaled-Dirichlet density. A common rescaling of all `lambda_i` changes nothing; only their ratios matter.

Let

`m_1 = sum_i w_i q_i`,

`m_2 = sum_i w_i q_i^2`.

As in `VIS-390`, the affine map from the simplex to the moment triangle has constant Jacobian magnitude

`J=(q_2-q_1)(q_3-q_1)(q_3-q_2)`,

so

`f_(m_1,m_2) = 2 lambda_1 lambda_2 lambda_3 / [J A(w(m_1,m_2))^3]`.

For a fixed interior first moment `x=m_1`, let `w^L(x)` and `w^U(x)` be the barycentric weights at the lower and upper endpoints of the feasible `m_2` slice. Explicitly,

for `q_1<x<q_2`,

`w^L=((q_2-x)/(q_2-q_1),(x-q_1)/(q_2-q_1),0)`,

for `q_2<x<q_3`,

`w^L=(0,(q_3-x)/(q_3-q_2),(x-q_2)/(q_3-q_2))`,

and for all `q_1<x<q_3`,

`w^U=((q_3-x)/(q_3-q_1),0,(x-q_1)/(q_3-q_1))`.

Write

`A_L(x)=A(w^L(x))`,

`A_U(x)=A(w^U(x))`.

Since the normalized residual coordinate `u` linearly parametrizes the whole slice,

`w(u)=(1-u)w^L+u w^U`

and therefore

`A(u)=A_L+u(A_U-A_L)`.

The exact conditional density of the residual coordinate is

`p(u | x,q,lambda)`
` = [2 A_L^2 A_U^2/(A_L+A_U)] / [A_L+u(A_U-A_L)]^3`,

for `0<u<1`.

If `A_L != A_U`, its conditional CDF is

`F_lambda(u|x)`
` = [A_L^(-2)-[A_L+u(A_U-A_L)]^(-2)] / [A_L^(-2)-A_U^(-2)]`.

If `A_L=A_U`, then `F_lambda(u|x)=u`.

Consequently

`v = F_lambda(u|x)`

is exactly `Uniform(0,1)` under this sector-anisotropic Gaussian tangent null. Equal sector variances give equal `lambda_i`, hence `A_L=A_U`, and recover the isotropic uniform-`u` result of `VIS-390`.

**Evidence/status:** `EXACT-DERIVED + STRONGER NONARITHMETIC NUISANCE NULL + SCALED-DIRICHLET PRIOR ART + NEGATIVE CONTROL + NO-NOVELTY-CLAIM FOR NORMALIZED-GAMMA/SIMPLEX PROBABILITY`.

No arithmetic anomaly, admissible-Wang model, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Unequal root-sector variances give a scaled-Dirichlet simplex law

Because every positive qutrit root sector has real dimension two,

`Y_i=||Z_i||_F^2`

is exponential with rate `lambda_i=1/(2 sigma_i^2)`. The three `Y_i` are independent. Write

`Y_i=r w_i`,

with `r=Y_1+Y_2+Y_3` and `w_1+w_2+w_3=1`.

The ordinary simplex Jacobian is `r^2`, so the joint density in `(r,w)` is

`lambda_1 lambda_2 lambda_3 r^2 exp[-r A(w)]`.

Integrating over `r>0` gives

`f_W(w)`
` = lambda_1 lambda_2 lambda_3 integral_0^infinity r^2 exp[-r A(w)] dr`
` = 2 lambda_1 lambda_2 lambda_3/A(w)^3`.

For equal rates the factor `A(w)` is constant on the simplex and the density is exactly `2`, recovering `Dirichlet(1,1,1)`.

This matters because an actual Gram tangent need not be isotropic across the three root sectors even when there is no arithmetic coupling. A source-independent construction rule, admissibility constraint, coarse block geometry, or other nonarithmetic resource can produce sector-specific variances before any arithmetic signal is present.

## 2. Moment coordinates preserve the rational-cubic density

`VIS-390` already established that the map

`w -> (m_1,m_2)`

is affine and invertible on the generic qutrit simplex, with constant Jacobian magnitude `J`. Therefore no new geometric factor appears when passing to the moment triangle:

`f_(m_1,m_2)=f_W(w(m_1,m_2))/J`.

At fixed `m_1=x`, the admissible `m_2` values form the same vertical interval

`L(x) <= m_2 <= U(x)`

as in `VIS-389` and `VIS-390`. The lower endpoint lies on the adjacent-support edge containing `x`; the upper endpoint lies on the `q_1`--`q_3` edge. Their barycentric coordinates are exactly the `w^L,w^U` above.

Because inverse barycentric coordinates are affine in `(m_1,m_2)`, moving linearly through the vertical moment slice also moves linearly between `w^L` and `w^U`. Hence `A(w)` is affine in `u`, which reduces the entire anisotropic conditional shape to the two endpoint values `A_L,A_U`.

## 3. Exact conditional density and uniformizer

At fixed `x`, the Jacobian from `m_2` to the normalized residual coordinate `u` is the constant interval width `U(x)-L(x)`. It cancels from conditional normalization, leaving density proportional to

`[A_L+u(A_U-A_L)]^(-3)`.

The elementary integral

`integral_0^1 [A_L+u(A_U-A_L)]^(-3) du`
` = (A_L+A_U)/(2 A_L^2 A_U^2)`

holds also by continuity when `A_L=A_U`. This gives the stated conditional density.

For `A_L != A_U`, integrating once more yields the stated CDF. The probability-integral transform therefore gives

`v=F_lambda(u|x) ~ Uniform(0,1)`.

This is an exact finite-dimensional calibration, not an asymptotic or simulation approximation.

The sign of `A_U-A_L` also shows the nuisance effect directly. If `A_U>A_L`, the conditional density decreases in `u`; if `A_U<A_L`, it increases. Sector variance anisotropy can therefore push residual mass toward either endpoint of the isotropic `u` interval without any arithmetic mechanism.

## 4. Consequence for the Wang localization route

An extreme value of the isotropic coordinate `u` is no longer enough even as evidence of unusual tangent orientation unless isotropy itself is justified. The first stronger exact control should allow pre-specified or independently calibrated sector variance ratios and transform the observed residual through `F_lambda`.

The nuisance parameters must not be fit to the same single observed tangent merely to make it typical. A valid use must obtain the rate ratios from a pre-registered nonarithmetic model, independent matched controls, repeated control realizations, or another source-free resource that is fixed before evaluating the candidate arithmetic family.

Under such a calibrated block-Gaussian null, the exact diagnostic is `v`, not raw `u`. A candidate source-specific effect must remain exceptional after this correction and then survive still stronger controls that preserve admissibility, coarse Gram structure, cross-sector dependence, or other nonarithmetic resources actually present in the Wang construction.

This narrows the accepted `CLUE-wang-fixed-source-packet-localization.md`: the minimal qutrit route has an exact nuisance ladder from isotropic tangent orientation (`VIS-390`) to arbitrary independent sectorwise Gaussian scales (this finding). What remains is structure not reproducible by that block-scale anisotropy and strong enough to pay the destination cost.

## Prior-art and novelty audit

The probability construction is classical. Monti, Mateu-Figueras, and Pawlowsky-Glahn, **Notes on the Scaled Dirichlet Distribution**, in *Compositional Data Analysis: Theory and Applications* (Wiley, 2011), pp. 128--138, DOI `10.1002/9781119976462.ch10`, studies the scaled-Dirichlet family obtained by relaxing the equal-scale requirement in normalized Gamma constructions. Graf's later simplicial generalized-beta work further embeds scale vectors into broader normalized generalized-Gamma simplex families.

No novelty is claimed for normalized independent Gamma variables with unequal scales, scaled-Dirichlet densities, affine simplex coordinates, or the probability-integral transform.

The Mathia-specific contribution is the exact specialization forced by the generic rank-one qutrit commutator geometry: the three positive sectors all have real dimension two, so arbitrary sectorwise Gaussian variances produce the explicit cubic density above, and the one residual spectral-shape coordinate from `VIS-389` admits a closed-form conditional uniformizer after `m_1` and the source spectrum are fixed.

## Boundaries

- The result assumes independent Gaussian tangent blocks whose covariance is scalar inside each two-dimensional root sector. Arbitrary within-sector anisotropy, cross-sector covariance, non-Gaussian tails, and nonlinear admissibility constraints are not covered.
- The source spectrum `{q_1,q_2,q_3}` is held fixed. `VIS-388` identifies it with the source cubic invariant, but this finding does not calibrate variation of that source geometry itself.
- The nuisance rates are legitimate controls only when fixed without tuning to the candidate residual being judged. Post-hoc fitting can absorb the effect by construction and is not evidence.
- A common scale of all `lambda_i` cancels; only two independent rate ratios matter.
- The exact uniformizer tests the specified sector-anisotropic Gaussian null. Rejection does not identify arithmetic structure; it only shows that this stronger nonarithmetic null is insufficient.
- No retained visualization is needed because the result is exact and representation-independent once the qutrit source spectrum and sector covariance model are fixed.
