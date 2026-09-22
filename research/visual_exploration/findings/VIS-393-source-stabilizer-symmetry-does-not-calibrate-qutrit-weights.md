# VIS-393 — source-stabilizer symmetry alone does not calibrate qutrit spectral weights

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-392`. Identify the positive off-diagonal/root space with

`V_+ = H_12 \oplus H_13 \oplus H_23 \cong C^3`,

where the source-stabilizer torus `T_E` acts by

`(z_12,z_13,z_23) -> (e^{i(theta_1-theta_2)}z_12, e^{i(theta_1-theta_3)}z_13, e^{i(theta_2-theta_3)}z_23)`.

For every nonzero `z in V_+`, define normalized root-sector weights

`w_ij(z)=|z_ij|^2/(|z_12|^2+|z_13|^2+|z_23|^2)`.

Then source-stabilizer symmetry by itself imposes **no probability law at all** on the weight vector `w=(w_12,w_13,w_23)`:

> For every Borel probability measure `nu` on the simplex
>
> `Delta_2={w_i>=0, sum_i w_i=1}`,
>
> there exists a `T_E`-invariant probability law on the unit sphere of `V_+` whose pushed-forward weight law is exactly `nu`.

Consequently, if the source spectrum `q_1<q_2<q_3` is fixed and the first spectral moment

`m_1=sum_i q_i w_i=x`

is fixed in the interior, the feasible slice is the segment parameterized by the residual coordinate `u in [0,1]` from `VIS-389`. **Every Borel probability law on `u` can occur under a source-stabilizer-invariant tangent law.**

Thus the uniform conditional null of `VIS-390` and the inverse-cube conditional family of `VIS-391` are consequences of their isotropic/Gaussian probability models, not consequences of the intrinsic qutrit source symmetry. `VIS-392` is maximal only inside the Gaussian class.

**Evidence/status:** `EXACT-DERIVED + SYMMETRY-QUOTIENT CLASSIFICATION + DECISIVE-NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No arithmetic anomaly, Wang gain, zeta-zero statement, or RH consequence is claimed.

## 1. The sector weights are torus invariants

The source torus changes only the three root-sector phases. Therefore each squared radius `|z_ij|^2`, their total norm, and the normalized weights `w_ij` are invariant under `T_E`.

This already means that source symmetry cannot mix different weight vectors. The simplex is part of the orbit quotient rather than a homogeneous orbit on which Haar symmetry would select one preferred distribution.

## 2. Haar orbit averaging realizes an arbitrary weight law

Let `nu` be any Borel probability measure on `Delta_2`. Sample

`w=(w_12,w_13,w_23) ~ nu`

and choose the canonical unit vector

`z_0(w)=(sqrt(w_12),sqrt(w_13),sqrt(w_23)) in C^3`.

Independently sample `t` from normalized Haar probability on the compact torus `T_E`, and set

`z=rho(t) z_0(w)`,

where `rho` is the root-space representation above.

For any fixed `s in T_E`,

`rho(s)z = rho(st)z_0(w)`.

Left invariance of Haar measure makes `st` have the same law as `t`, so the law of `z` is `T_E`-invariant. Because torus action preserves every sector radius,

`w(z)=w(z_0(w))=w`.

Hence the pushforward of this invariant law under `z -> w(z)` is exactly the prescribed `nu`.

The construction works equally on simplex faces and vertices. No density, Gaussianity, independence, or nondegeneracy assumption is needed.

## 3. Conditional residual shape can therefore be arbitrary

Fix a generic support `q_1<q_2<q_3` and an interior value `x` of

`m_1=sum_i q_i w_i`.

The intersection of the simplex with `m_1=x` is the line segment already used in `VIS-389`--`VIS-391`. Its affine coordinate is

`u=[m_2-L(x)]/[U(x)-L(x)]`,

and `u -> w_x(u)` is a bijection from `[0,1]` to that segment.

Given any Borel probability measure `eta` on `[0,1]`, push it forward through `u -> w_x(u)` to obtain a measure `nu_x` on the simplex, then apply the Haar-orbit construction above. The resulting tangent law is source-stabilizer invariant, satisfies `m_1=x` almost surely, and has residual coordinate distributed exactly as `eta`.

Therefore there is no universal source-symmetry conditional CDF that can replace the model-specific `F_lambda` of `VIS-391`. A symmetry-only attempt to enlarge the nuisance family all the way to every invariant law makes the residual-shape test vacuous.

## 4. The orbit quotient contains even more than the weights

The weights are not the complete set of torus invariants. On the open set where all three root coordinates are nonzero, the phase combination

`psi = arg(z_12 z_23 conjugate(z_13))`

is also invariant because the root characters satisfy

`alpha_12 + alpha_23 - alpha_13 = 0`.

Equivalently, the complex cubic quantity

`tau=z_12 z_23 conjugate(z_13)`

is torus invariant. Its modulus is fixed by the three radii, but its phase supplies an additional orbit-quotient coordinate.

This extra invariant is not needed for the weight-law no-go result. It only strengthens the conclusion that full source-stabilizer symmetry is too weak, by itself, to prescribe a unique non-Gaussian tangent null.

## 5. Consequence for the qutrit nuisance hierarchy

`VIS-390` gives an exact null after making a strong isotropic-orientation assumption. `VIS-391` allows independent sector scales. `VIS-392` proves that those sector scales exhaust all covariance freedom compatible with the full generic source stabilizer **within the Gaussian class**.

The present result marks the next boundary: leaving Gaussianity while retaining the same symmetry opens an essentially unrestricted weight law. A residual that rejects every sector-scaled Gaussian null therefore establishes only that the Gaussian nuisance model is insufficient. It does not, by symmetry alone, identify arithmetic/source specificity.

A useful stronger null must consequently obtain structure from something beyond source-stabilizer invariance: an independently motivated non-Gaussian generative mechanism, admissibility constraints, block-resource-matched controls, externally calibrated moments/tails/dependence, or another source-free restriction fixed before the candidate residual is scored.

This is a negative result for the idea of a canonical "maximally symmetry-preserving" residual null. The maximal invariant family is too rich to be discriminating.

## Prior-art and novelty boundary

The ingredients are standard compact-group and invariant-theory facts. Normalized Haar probability on a compact group is translation invariant, so averaging any point or section over a group orbit produces an invariant probability law. For a torus representation, coordinate moduli and zero-weight monomials are standard invariants; in the `A_2` root representation the cubic monomial above follows from the root relation.

Authoritative background includes Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer, 2015, DOI `10.1007/978-3-319-13467-3`, for maximal tori and root-space representations, and David L. Wehlau, **When is a ring of torus invariants a polynomial ring?**, *manuscripta mathematica* 82 (1994), 161--170, DOI `10.1007/BF02567695`, for the classical weight/monomial viewpoint on torus invariants.

No novelty is claimed for Haar orbit averaging, quotienting a compact group action, torus invariant monomials, or the general fact that invariance does not determine a probability measure on the orbit space. The Mathia-specific content is the exact consequence for the qutrit residual-null hierarchy of `VIS-390`--`VIS-392`.

## Boundaries

- The result classifies what **symmetry alone cannot constrain**; it does not say that every invariant weight law is physically, arithmetically, or Wang-admissibly realizable.
- The arbitrary-law realization deliberately ignores any additional source-free structure that a valid matched control may need to preserve. Such restrictions are precisely what must make a stronger null falsifiable.
- The fixed-`m_1` statement is conditional. A global control may couple the distribution of `m_1` and `u`; symmetry alone also leaves that joint law unconstrained.
- The invariant cubic phase `tau` is noted only to expose further quotient freedom. The current residual spectral statistic depends on sector weights, so no phase-based claim is made.
- Generic distinct source eigenvalues are assumed, as in `VIS-392`. Degenerate sources have larger stabilizers and a different quotient geometry.
