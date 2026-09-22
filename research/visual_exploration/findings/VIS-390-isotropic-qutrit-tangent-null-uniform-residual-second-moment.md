# VIS-390 — isotropic qutrit tangent null makes the residual second moment uniform

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388` and `VIS-389`. Let

`0 < q_1 < q_2 < q_3`

be the three positive eigenvalues of the intrinsic source-subspace commutator Laplacian `Delta_S`, and let the corresponding real root sectors be

`V_+ = H_1 direct_sum H_2 direct_sum H_3`,

with `dim_R H_i=2`.

Choose a source-free tangent orientation `g` Haar-uniformly from the unit sphere of the six-dimensional positive spectral subspace `V_+`, and define

`w_i = ||P_i g||_F^2`,

so `w_i>=0` and `w_1+w_2+w_3=1`. Then

`(w_1,w_2,w_3) ~ Dirichlet(1,1,1)`,

hence the weight vector is exactly uniform on the probability simplex.

Let

`m_1 = sum_i w_i q_i`,

`m_2 = sum_i w_i q_i^2`.

The affine map from `(w_1,w_2,w_3)` to `(m_1,m_2)` is invertible, with constant Jacobian magnitude

`J = (q_2-q_1)(q_3-q_1)(q_3-q_2)`.

Therefore `(m_1,m_2)` is exactly uniform on the moment triangle

`T = conv{(q_1,q_1^2),(q_2,q_2^2),(q_3,q_3^2)}`

with constant density `2/J`.

Consequently, after conditioning on the observed first moment `m_1`, the only residual qutrit shape scalar from `VIS-389` has an exact source-free null: `m_2` is uniform on its feasible interval. Define

`L(m_1) = (q_1+q_2)m_1-q_1 q_2` for `q_1<=m_1<=q_2`,

`L(m_1) = (q_2+q_3)m_1-q_2 q_3` for `q_2<=m_1<=q_3`,

and

`U(m_1) = (q_1+q_3)m_1-q_1 q_3`.

For interior `m_1`,

`u = [m_2-L(m_1)]/[U(m_1)-L(m_1)]`

satisfies

`u | (m_1,q_1,q_2,q_3) ~ Uniform(0,1)`.

Since `VIS-388` shows that the support `{q_1,q_2,q_3}` is fixed by the intrinsic source cubic invariant `t^2=tr(E^3)^2`, this may equivalently be written as

`u | (t^2,m_1) ~ Uniform(0,1)`

under the isotropic tangent-orientation null.

Thus a generic qutrit rank-one source has algebraic room for one residual shape scalar, but that scalar now has an exact source-free conditional calibration. An observed residual variance or second moment is not source-specific evidence merely because it is extreme relative to an arbitrary visual profile; it must be extreme relative to this exact conditional null and still survive stronger Wang-resource-matched controls.

**Evidence/status:** `EXACT-DERIVED + SOURCE-FREE CONDITIONAL NULL + CLASSICAL DIRICHLET/SPHERE INGREDIENT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM FOR DIRICHLET OR FINITE-MOMENT GEOMETRY`.

No arithmetic anomaly, Wang destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Haar sphere blocks give a uniform simplex

Choose independent standard Gaussian vectors

`Z_i in H_i ~= R^2`,

and put

`Z=Z_1+Z_2+Z_3`,

`g=Z/||Z||_F`.

Gaussian rotational invariance makes `g` Haar-uniform on the unit sphere of `V_+`. The block energies

`Y_i=||Z_i||_F^2`

are independent `chi^2_2` variables, equivalently independent Gamma variables with common shape `1` and common scale `2`. Hence

`w_i = Y_i/(Y_1+Y_2+Y_3)`

has the Dirichlet law with parameters `(1,1,1)`.

Its density with respect to `dw_1 dw_2` on

`w_1>0`, `w_2>0`, `w_1+w_2<1`

is the constant `2`. The qutrit multiplicity two of every positive root sector is exactly what makes the tangent-weight simplex uniform; for unequal block dimensions the corresponding Dirichlet parameters would be the half-dimensions of the blocks.

## 2. Moment coordinates have a constant Jacobian

Eliminate `w_3=1-w_1-w_2`. Then

`m_1 = q_3 + (q_1-q_3)w_1 + (q_2-q_3)w_2`,

`m_2 = q_3^2 + (q_1^2-q_3^2)w_1 + (q_2^2-q_3^2)w_2`.

The absolute determinant of this affine map is

`|(q_1-q_3)(q_2^2-q_3^2) - (q_2-q_3)(q_1^2-q_3^2)|`

` = (q_2-q_1)(q_3-q_1)(q_3-q_2)`

` = J`.

The three simplex vertices map to `(q_i,q_i^2)`, so the image is exactly the moment triangle `T`. Because the source density is constant and the Jacobian is constant, the joint density of `(m_1,m_2)` is the constant `2/J` on `T`.

This also recovers two source-free unconditional moment checks. Using the qutrit root identities from `VIS-388`,

`E[m_1] = (q_1+q_2+q_3)/3 = 1`,

and

`E[m_2] = (q_1^2+q_2^2+q_3^2)/3 = 3/2`.

Moreover `Var(m_1)=1/8`, again independent of the source cubic parameter. These are implementation/calibration checks, not the main discriminating statistic.

## 3. Conditioning on defect energy leaves a uniform scalar

`VIS-389` gives the exact feasible interval for `m_2` at fixed first moment. For

`q_1<=m_1<=q_2`,

`L(m_1)=(q_1+q_2)m_1-q_1q_2`,

`U(m_1)=(q_1+q_3)m_1-q_1q_3`,

while for

`q_2<=m_1<=q_3`,

`L(m_1)=(q_2+q_3)m_1-q_2q_3`

and the same `U(m_1)` applies.

Since the joint density on `T` is constant, every vertical slice at fixed interior `m_1` has constant conditional density in `m_2`. Therefore

`m_2 | m_1 ~ Uniform(L(m_1),U(m_1))`.

Equivalently,

`E[m_2|m_1]=(L+U)/2`,

`Var(m_2|m_1)=(U-L)^2/12`,

and the affine rank coordinate

`u=(m_2-L)/(U-L)`

is exactly uniform on `(0,1)`.

The interval width is also explicit:

`U-L=(q_3-q_2)(m_1-q_1)` for `q_1<=m_1<=q_2`,

and

`U-L=(q_2-q_1)(q_3-m_1)` for `q_2<=m_1<=q_3`.

It collapses only at the extreme support means `m_1=q_1` and `m_1=q_3`, where the tangent measure is already forced to a single atom.

## 4. The first-moment null is triangular

Integrating the constant joint density over the vertical slice gives the exact marginal null for the scale-invariant defect rate:

`f_(m_1)(x) = 2(x-q_1)/[(q_3-q_1)(q_2-q_1)]`

for `q_1<x<q_2`, and

`f_(m_1)(x) = 2(q_3-x)/[(q_3-q_1)(q_3-q_2)]`

for `q_2<x<q_3`.

The two pieces agree at `q_2`. This separates two diagnostics that should not be conflated: whether the observed scalar defect rate `m_1` is unusual under an isotropic tangent orientation, and whether the residual shape coordinate `u` is unusual **after conditioning on that observed rate**.

This null is complementary to `VIS-385`. `VIS-385` randomizes the source subspace `S` while holding the Gram tangent fixed. The present null holds the qutrit source spectrum fixed and randomizes tangent orientation inside its positive commutator spectrum. They test different possible sources of apparent exceptional alignment.

## 5. Consequence for the Wang localization clue

The accepted clue `research/visual_exploration/clues/CLUE-wang-fixed-source-packet-localization.md` no longer needs an arbitrary family of qutrit spectral-shape coordinates or an empirical isotropic tangent simulation to calibrate its minimal rank-one test bed.

At fixed source cubic invariant `t^2` and observed defect rate `m_1`, every scale-invariant positive spectral statistic is already a function of the single scalar `m_2` by `VIS-389`, and the isotropic tangent null for that scalar is exactly uniform after the normalization above.

A clean minimal test can therefore report two separate quantities: the source-free position of `m_1` under the triangular first-moment null, and the conditional residual coordinate `u`. An extreme `u` identifies non-isotropic alignment of the Gram tangent with the qutrit commutator sectors relative to this null. It does **not** by itself identify arithmetic/source information: admissibility constraints, coarse Gram geometry, block structure, or other nonarithmetic Wang resources may create the same non-isotropy and must be preserved by stronger matched controls.

The qutrit branch is therefore narrowed from “search the spectral profile” to “explain and validate an exact one-dimensional conditional residual.”

## Prior-art and novelty audit

The probabilistic ingredients are classical. Normalizing independent Gamma variables gives a Dirichlet vector; equivalently, normalized squared Gaussian block norms give Dirichlet block weights for a uniform spherical direction. Olkin and Rubin, **Multivariate Beta Distributions and Independence Properties of the Wishart Distribution**, *Annals of Mathematical Statistics* 35:1 (1964), 261–269, DOI `10.1214/aoms/1177703748`, is classical multivariate beta/Dirichlet-Wishart prior art. Jose H. Guardiola, **The spherical-Dirichlet distribution**, *Journal of Statistical Distributions and Applications* 7 (2020), article 6, DOI `10.1186/s40488-020-00106-9`, explicitly develops the Dirichlet-to-hypersphere transformation and its uniform spherical specialization.

No novelty is claimed for Gaussian generation of Haar sphere measure, chi-square/Gamma block energies, the Dirichlet distribution, affine change of variables, or conditional uniformity of a constant-density triangle.

The Mathia-specific contribution is the exact specialization to the intrinsic qutrit Wang/source commutator geometry established in `VIS-388` and `VIS-389`: the three positive sectors have equal real dimension two, which turns the residual tangent-shape degree of freedom into an exactly calibrated scalar after source shape and defect energy are conditioned out.

## Boundaries

- The null is for a Haar-isotropic tangent orientation in the positive spectral subspace with the source spectrum held fixed. An actual Wang Gram tangent need not be isotropic.
- The exact `Dirichlet(1,1,1)` law uses the generic qutrit rank-one multiplicities `2,2,2`. Higher matrix dimension, higher source rank, or merged spectral sectors produce different block dimensions and generally different Dirichlet parameters or support geometry.
- Conditioning on `m_1` removes the scalar defect-energy coordinate but does not preserve every Wang resource correlated with tangent orientation.
- An extreme `u` proves deviation from this source-free isotropic tangent null only. It does not prove arithmetic specificity, novelty, stability across truncation/scale, or destination-level usefulness.
- The nongeneric qutrit source boundaries already collapse the residual shape channel as classified in `VIS-389`; this conditional null is intended for the generic three-support regime.
- No retained visualization is needed because the null and its calibration are exact and representation-independent after the intrinsic source spectrum is fixed.
