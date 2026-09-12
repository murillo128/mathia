# AF-300 — Affine source restriction buys intrinsic dimension, not linear null directions

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `SOURCE-RESTRICTION`, `OPTIMAL-DESIGN`, `LINEAR-QUOTIENT`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-299 leaves one precise escape from the full-space no-quotient theorem: perhaps the admissible coefficient sources really live in a lower-dimensional family, so directions that reach boundary failure in the ambient coefficient space are not valid perturbations. For **complex-affine source models**, that escape can be classified exactly.

Let

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s},
\qquad c\in\mathbb C^N,
\]

let `Gamma` be a compact rectifiable Jordan curve, and let

\[
\Delta_{\Gamma,N}
=\{c:\exists z\in\Gamma\text{ with }P_c(z)=0\}
\]

be AF-290's boundary-zero discriminant. Fix a complex-affine admissible source family

\[
\mathcal A=a+U,
\qquad U\le\mathbb C^N,
\qquad \dim_\mathbb C U=r\ge1,
\]

and assume `A` contains at least one boundary-safe point. For `z\in\Gamma`, write

\[
L_z(c)=P_c(z),
\qquad
\phi_z:=L_z|_U.
\]

Then the source restriction has two sharply different effects.

### 1. The true perturbation dimension drops from `N` to `r`

For every boundary-safe `b\in\mathcal A`, the exact Euclidean distance to boundary failure **within the admissible source family** is

\[
\boxed{
\operatorname{dist}_{2,\mathcal A}
(b,\Delta_{\Gamma,N}\cap\mathcal A)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{\|\phi_z\|_{U^*}},
}
\tag{1}
\]

with the ratio interpreted as `+infinity` when `\phi_z=0`.

If a boundary-observation Gram metric is built only on admissible directions, set

\[
r_z=(n^{-\overline z})_{n=1}^N,
\qquad
u_z:=\Pi_U r_z,
\qquad
G_{\mu,U}
=
\int_\Gamma u_z u_z^*\,d\mu(z).
\]

Then every positive-definite such metric obeys the **source-relative leverage identity**

\[
\boxed{
\int_\Gamma K_{\mu,U}(z)\,d\mu(z)=r,
\qquad
K_{\mu,U}(z)
:=u_z^*G_{\mu,U}^{-1}u_z.
}
\tag{2}
\]

Moreover a `D`-optimal design on the restricted evaluation family satisfies

\[
\boxed{
\sup_{z\in\Gamma}K_{\mu,U}(z)=r.
}
\tag{3}
\]

Thus AF-298's sharp dimension bill is genuinely **source-relative**: once the admissible perturbation family has independently been proved to be `r` complex dimensions, the best scalar boundary-observation geometry pays `sqrt(r)`, not `sqrt(N)`.

More explicitly, set

\[
m_b:=\min_{z\in\Gamma}|P_b(z)|>0,
\qquad
M_b:=\max_{z\in\Gamma}|P_b(z)|,
\]

and normalize the restricted Gram distance by the nominal boundary-response energy

\[
E_\mu(b)
:=
\left(\int_\Gamma|P_b(z)|^2d\mu(z)\right)^{1/2}.
\]

Then

\[
\boxed{
\frac{m_b}{M_b\sqrt r}
\le
\sup_\mu
\frac{\operatorname{dist}_{\mu,U}
(b,\Delta_{\Gamma,N}\cap\mathcal A)}{E_\mu(b)}
\le
\frac{M_b}{m_b\sqrt r}.
}
\tag{4}
\]

The supremum ranges over probability measures whose restricted information matrix is positive definite. Hence a source class with uniformly controlled boundary-modulus ratio `M_b/m_b` has optimal normalized observation-Gram margin of order `r^{-1/2}`.

### 2. Complex-affine restriction creates no further target-null linear directions

Despite this legitimate reduction from ambient dimension `N` to intrinsic source dimension `r`, the restricted boundary-zero family is still essential on `U`:

\[
\boxed{
\bigcap_{z\in\Gamma}\ker\phi_z=\{0\}.
}
\tag{5}
\]

Consequently, if

\[
q:U\to W
\]

is any complex-linear compression with nonzero kernel, then

\[
\boxed{
q\bigl((\Delta_{\Gamma,N}\cap\mathcal A)-a\bigr)=q(U).
}
\tag{6}
\]

Every compressed source state is compatible with a boundary-failure source. Since `A` also contains a safe point, the Boolean boundary-failure discriminator cannot factor through any noninjective complex-linear compression of the admissible coordinates.

Equivalently, among complex-linear representations of a safe-containing complex-affine source family, the smallest exact representation of boundary-failure membership has complex dimension **exactly `r`**. Source restriction may lower the dimension bill from `N` to `r`, but linear quotienting cannot lower it further.

The same statement has a metric form. If `G\ge0` is any Hermitian seminorm on `U` with

\[
\operatorname{rank}G<r,
\]

then for every `b\in\mathcal A`,

\[
\boxed{
\operatorname{dist}_{G,\mathcal A}
(b,\Delta_{\Gamma,N}\cap\mathcal A)=0.
}
\tag{7}
\]

So the legitimate effective-dimension mechanism is now exact: an ambient rank-`r` representation can be faithful when its restriction to the actual `r`-dimensional source tangent space is full rank; a rank deficit **inside the admissible source space** still collapses the zero-count margin completely.

## Abstract affine-hyperplane mechanism

The quotient statement is not special to Dirichlet polynomials. Let `V` be a finite-dimensional complex vector space, let `{ell_j}_{j\in J}` be linear functionals, and let

\[
\Delta=\bigcup_{j\in J}\ker\ell_j.
\]

Restrict to an affine source family `A=a+U`. The induced failure surfaces in source coordinates are

\[
H_j^A
=
\{u\in U:\ell_j(a+u)=0\}.
\]

Write

\[
C_U
:=
\bigcap_{j\in J}\ker(\ell_j|_U).
\]

For a linear compression `q:U\to W` with kernel `K`, the same dichotomy as AF-299 survives affine restriction:

- if `K\subseteq C_U`, failure membership is constant along quotient fibers;
- if `K\not\subseteq C_U`, then every quotient state has a failure representative.

Indeed, choose `h\in K\setminus C_U`. Then some `j_0` has `ell_{j_0}(h)\ne0`. For arbitrary `u\in U`, put

\[
t
=-\frac{\ell_{j_0}(a+u)}{\ell_{j_0}(h)}
\]

and

\[
u'=u+th.
\]

Because `U` is a **complex** linear space, `th\in U`. Also

\[
\ell_{j_0}(a+u')=0,
\]

while

\[
q(u')=q(u).
\]

Thus

\[
q\left(\bigcup_jH_j^A\right)=q(U).
\]

This is the exact reason complex-affine source restriction cannot create a hidden linear quotient direction unless the entire restricted failure family is already blind to that direction.

## Dirichlet restriction remains essential on every nonzero complex source subspace

AF-299 proved

\[
\bigcap_{z\in\Gamma}\ker L_z=\{0\}
\qquad\text{in }\mathbb C^N.
\]

Intersecting with any complex subspace `U` immediately gives

\[
\bigcap_{z\in\Gamma}\ker(L_z|_U)
=
U\cap
\bigcap_{z\in\Gamma}\ker L_z
=\{0\},
\]

which is (5).

Take any nonzero admissible direction `h\in U`. The Dirichlet polynomial `P_h` cannot vanish identically. Therefore there is some boundary point `z\in\Gamma` with

\[
P_h(z)\ne0.
\]

Starting from **any** admissible source `b\in a+U`, the complex line

\[
b+\mathbb C h
\]

contains the exact boundary-failure point

\[
\boxed{
b'
=b-
\frac{P_b(z)}{P_h(z)}h.}
\tag{8}
\]

Any compression that deletes `h` therefore identifies `b` with a source on the zero-count discontinuity set.

This closes the most direct interpretation of AF-299's source-restricted escape. It is not enough to say that the admissible coefficients occupy a lower-dimensional complex-linear model. Such a model lowers the **ambient parameter dimension**, but every one of its remaining complex directions is still target-relevant to the boundary-zero discriminator.

## Exact restricted distance formula

Fix a boundary-safe `b\in\mathcal A`. A perturbation inside the source family has the form `b+h` with `h\in U`.

For a fixed `z\in\Gamma`, reaching the failure hyperplane at `z` means solving

\[
\phi_z(h)=-P_b(z).
\tag{9}
\]

If `\phi_z\ne0`, the minimum-norm solution in the Hilbert space `U` has norm

\[
\frac{|P_b(z)|}{\|\phi_z\|_{U^*}}.
\tag{10}
\]

If `\phi_z=0`, equation (9) has no solution because `b` is boundary-safe, so that boundary point contributes `+infinity`. Taking the minimum over the union of all reachable source-relative failure hyperplanes proves (1).

In the standard Euclidean geometry,

\[
\|\phi_z\|_{U^*}
=\|\Pi_Ur_z\|_2.
\tag{11}
\]

Therefore

\[
\boxed{
\operatorname{dist}_{2,\mathcal A}
(b,\Delta_{\Gamma,N}\cap\mathcal A)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{\|\Pi_Ur_z\|_2}.
}
\tag{12}
\]

Because `|P_b|` has a positive minimum on the compact contour, points where `Pi_U r_z` tends to zero cannot create a hidden smaller infimum. The extended ratio is coercive there, so the minimum is attained.

Equation (12) shows a real gain unavailable to AF-299's unrestricted quotient. Projection of the evaluation normals onto the **actually admissible perturbation directions** can enlarge the distance to boundary failure. Source restriction may therefore improve conditioning even though it does not create a target-null direction inside `U`.

## Source-relative observation design and the `r`-dimensional leverage law

The family `{u_z:z\in\Gamma}` spans `U`. If `h\in U` were orthogonal to every `u_z`, then

\[
P_h(z)=0
\qquad(z\in\Gamma),
\]

so AF-299's identity-theorem argument would force `h=0`.

Hence there exist probability measures `mu` on `Gamma` for which

\[
G_{\mu,U}
=
\int_\Gamma u_zu_z^*d\mu(z)
\]

is positive definite on `U`. Give admissible perturbations the norm

\[
\|h\|_{\mu,U}^2
=h^*G_{\mu,U}h
=
\int_\Gamma|P_h(z)|^2d\mu(z).
\tag{13}
\]

For fixed `z`, the dual norm of the restricted evaluation is

\[
\|\phi_z\|_{\mu,U,*}^2
=u_z^*G_{\mu,U}^{-1}u_z
=:K_{\mu,U}(z).
\tag{14}
\]

Therefore

\[
\boxed{
\operatorname{dist}_{\mu,U}
(b,\Delta_{\Gamma,N}\cap\mathcal A)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{\sqrt{K_{\mu,U}(z)}}.
}
\tag{15}
\]

The leverage trace calculation from AF-298 now runs on `U`, not on the ambient coefficient space:

\[
\begin{aligned}
\int_\Gamma K_{\mu,U}(z)d\mu(z)
&=
\operatorname{tr}_U\left(
G_{\mu,U}^{-1}
\int_\Gamma u_zu_z^*d\mu(z)
\right)\\
&=
\operatorname{tr}_U(I_U)\\
&=r.
\end{aligned}
\tag{16}
\]

Thus every full-rank source-relative boundary metric has

\[
\sup_zK_{\mu,U}(z)\ge r.
\tag{17}
\]

Conversely, maximizing `log det G_{mu,U}` over the compact convex design set and taking the usual directional derivative gives a `D`-optimal measure `mu_*` satisfying

\[
K_{\mu_*,U}(z)\le r
\qquad(z\in\Gamma).
\tag{18}
\]

Together with (16), its maximum is exactly `r`. This proves (2)--(3).

Since

\[
m_b\le E_\mu(b)\le M_b,
\]

equations (15), (17), and (18) immediately give (4). The Kiefer--Wolfowitz parameter-count constant has simply changed from ambient dimension `N` to the number `r` of admissible complex source degrees of freedom.

## Exact control: coordinate-sparse source models

Let `S\subset\{1,\ldots,N\}` have cardinality `r`, and suppose admissible perturbations change only coefficients indexed by `S`:

\[
U_S
=\operatorname{span}_\mathbb C\{e_n:n\in S\}.
\]

Then

\[
\|\phi_z\|_{U_S^*}^2
=\sum_{n\in S}n^{-2\operatorname{Re}z},
\tag{19}
\]

so (12) becomes the exact support-restricted analogue of AF-290:

\[
\operatorname{dist}_{2,a+U_S}
(b,\Delta_{\Gamma,N}\cap(a+U_S))
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}
{\left(\sum_{n\in S}n^{-2\operatorname{Re}z}\right)^{1/2}}.
\tag{20}
\]

Optimized scalar boundary-observation geometry now pays `sqrt(r)`. This is a legitimate reduction of the AF-298 bill because the other `N-r` coefficient directions were removed from the **source model before observation**, not projected away after being admitted as possible perturbations.

But every nonzero direction in `U_S` remains visible to some boundary evaluation. Hence no subsequent rank-`<r` complex-linear feature map can preserve exact boundary-failure membership on a safe-containing complex-affine source class.

The example separates two statements that looked similar after AF-298:

- “only `r` source degrees of freedom are admissible” is a genuine model restriction and changes the conditioning dimension to `r`;
- “keep only `r` of `N` dimensions from an unrestricted source” is a quotient and, by AF-299, gives zero exact failure margin.

They are not interchangeable.

## Prior art and novelty assessment

The ingredients are classical, and no general novelty is claimed.

- Peter Orlik and Hiroaki Terao, *Arrangements of Hyperplanes*, Springer (1992), is the standard reference for hyperplane arrangements, restriction, rank, essentiality, and common intersections. Restricting a linear-functional family to a subspace and inspecting its common kernel is standard arrangement geometry.
- J. Kiefer and J. Wolfowitz, “The Equivalence of Two Extremum Problems,” *Canadian Journal of Mathematics* 12 (1960), 363--366, proves the classical `D`-optimal/`G`-optimal equivalence. Its parameter-count constant is the dimension of the regression space, so the appearance of `r` rather than `N` after a genuine source restriction is classical optimal-design mathematics.
- James W. Demmel, “On condition numbers and the distance to the nearest ill-posed problem,” *Numerische Mathematik* 51 (1987), 251--289, supplies the general distance-to-ill-posedness viewpoint already used in AF-290.
- Finite Dirichlet polynomials are exponential sums with distinct exponents `-log n`; their linear independence and the identity theorem used here are classical.

A targeted literature check found the expected arrangement-restriction and optimal-design frameworks, not a basis for claiming the abstract affine statements as new. The durable Arithmetic Fidelity result is their combination at the current zero-count frontier: **source restriction changes the correct dimension in the observation-leverage bill, but every remaining complex-linear source direction is still capable of reaching boundary failure and therefore cannot be quotiented out.**

## Boundaries and failure modes

- The source model is **complex-affine**. This is load-bearing. For a merely real-linear family, the correction coefficient in (8) is constrained to be real, so one real direction cannot in general solve one complex boundary equation. Positivity, integrality, order constraints, discrete source sets, and nonlinear varieties can therefore evade the saturation proof and require separate geometry.
- The theorem does not prove that any particular arithmetic source class has dimension `r=o(N)`. Choosing a convenient low-dimensional `U` by hand is not an arithmetic mechanism. A useful application must derive the source restriction independently of the zero-count target.
- The `r^{-1/2}` law concerns positive averages of the same scalar boundary evaluations, exactly as in AF-298 but restricted to admissible directions. Richer vector, derivative, nonlocal, or coupled observations can change the information geometry.
- Equation (4) is controlled by the boundary-modulus ratio `M_b/m_b`. It gives a clean dimension law only when that ratio is independently bounded; source restriction does not manufacture such a bound.
- A full-rank metric on `U` may have rank only `r<N` when represented in the ambient space. That is harmless precisely because its ambient nullspace contains only **inadmissible** perturbation directions. Rank deficiency inside `U` is fatal by (7).
- The result concerns finite Dirichlet polynomials and zero count relative to a fixed contour. It does not supply analytic continuation, a global zero matching, a zeta reconstruction, or an RH implication.

## Decisive audit test

Whenever a proposed effective-dimension reduction for a zero-sensitive Dirichlet representation invokes a constrained source family, identify its actual admissible difference geometry before quotienting.

If the source is locally or globally modeled by a complex-affine space `a+U`, compute

\[
r=\dim_\mathbb C U
\]

and test the proposed representation on `U` itself. Scalar boundary-observation leverage pays `sqrt(r)`, while any feature map whose kernel intersects `U` nontrivially identifies every output with a boundary-failure source. A claimed linear representation of dimension below `r` is therefore impossible for exact boundary-failure membership.

Only a source geometry that is not closed under the complex correction move (8)—for example a real, positive, integral, discrete, nonlinear, or genuine symmetry-constrained family—escapes this theorem. Such a proposal must state that geometry explicitly rather than describe it only as “lower dimensional.”

## Consequence for the research line

AF-299's source-restricted escape is now substantially narrower and more quantitative.

A genuine lower-dimensional source model **can** beat the ambient `N^{-1/2}` observation-Gram bill: the correct parameter is its intrinsic complex dimension `r`, and the optimal leverage ceiling becomes `r^{-1/2}`. But complex-affine source restriction does not create any further linear target-null directions. Once the source model is fixed, every remaining complex degree of freedom is still needed by the boundary-zero discriminator.

The next effective-dimension question is therefore not whether an arbitrary low-dimensional coefficient subspace helps—it does exactly by replacing `N` with its dimension, and no more. The live question is whether arithmetic supplies a **non-complex-linear** admissible geometry (real, positive, discrete, multiplicative, nonlinear, or genuine symmetry-derived) whose fibers avoid the boundary-zero discriminant while still retaining enough source breadth to matter for an RH-relevant analytic carrier.