# AF-298 — Boundary-observation Gram metrics have a sharp dimension fidelity ceiling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `OBSERVATION-GRAM`, `OPTIMAL-DESIGN`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-297 leaves genuinely nonradial or anisotropic geometry as a possible escape from target-radial conformal repair. A particularly natural candidate is to measure coefficient perturbations by the boundary responses they produce: instead of defining a metric from distance to the zero-count discriminant, take an `L^2` norm of the Dirichlet polynomial itself on the target contour. This produces a dense, generally anisotropic Hilbert metric from the observation family alone.

For the eta truncation

\[
\eta_N(s)=\sum_{n=1}^N(-1)^{n-1}n^{-s},
\qquad
b^{(N)}=\bigl((-1)^{n-1}\bigr)_{n=1}^N,
\]

fix a compact rectifiable Jordan curve `Gamma subset {Re(s)>0}` on which `eta` has no zero. For `z in Gamma` write

\[
r_z=(n^{-\overline z})_{n=1}^N,
\qquad
P_c(z)=r_z^*c.
\]

Let `mu` be any probability measure on `Gamma` whose information matrix

\[
G_{\mu,N}:=\int_\Gamma r_zr_z^*\,d\mu(z)
\]

is positive definite, and give coefficient space the observation-Gram norm

\[
\|c\|_{\mu,N}^2
:=c^*G_{\mu,N}c
=\int_\Gamma |P_c(z)|^2\,d\mu(z).
\]

Let `Delta_{Gamma,N}` be AF-290's boundary-zero discriminant and define the normalized zero-count margin

\[
\delta_{\mu,N}
:=
\frac{\operatorname{dist}_{\mu,N}
(b^{(N)},\Delta_{\Gamma,N})}
{\|b^{(N)}\|_{\mu,N}}.
\]

Then, uniformly over **all** such probability measures, including `N`-dependent and finitely supported measures,

\[
\boxed{
\sup_{\mu}\delta_{\mu,N}
\asymp_{\Gamma} N^{-1/2}.
}
\tag{1}
\]

More precisely, for all sufficiently large `N` there are constants `0<c_Gamma<=C_Gamma<infinity`, depending only on the fixed contour, such that

\[
\boxed{
\frac{c_\Gamma}{\sqrt N}
\le
\sup_{\mu}\delta_{\mu,N}
\le
\frac{C_\Gamma}{\sqrt N}.
}
\tag{2}
\]

The lower bound is attained up to the fixed eta boundary-modulus constants by a `D`-optimal design measure on `Gamma`. Equivalently, one can choose the boundary weighting so that its leverage/reproducing-kernel diagonal obeys

\[
\sup_{z\in\Gamma}
K_{\mu,N}(z)=N,
\qquad
K_{\mu,N}(z):=r_z^*G_{\mu,N}^{-1}r_z.
\tag{3}
\]

Thus boundary-observation geometry can genuinely improve the raw AF-291 eta margin by removing the extra evaluation-growth factor `H_N(alpha)`, but it cannot make the margin order one. Even after optimizing the entire anisotropic boundary weighting, a sharp `N^{-1/2}` fidelity bill remains. The obstruction is no longer the left-edge evaluation norm. It is the **dimension identity**

\[
\boxed{
\int_\Gamma K_{\mu,N}(z)\,d\mu(z)=N.
}
\tag{4}
\]

This closes one important nonradial escape left by AF-297: an arbitrarily optimized full-rank `L^2` geometry generated solely by boundary evaluations cannot stabilize the eta zero-count discriminator. To do better, a representation must use structure beyond a positive average of the same scalar boundary observations, reduce the effective target-relevant dimension through a justified quotient, or add new information.

## Exact distance formula in observation-Gram geometry

For fixed `z`, the boundary-zero condition `P_c(z)=0` is the hyperplane `ker L_z`, where

\[
L_z(c)=r_z^*c.
\]

AF-293 gives the exact distance to this hyperplane in any positive-definite Hilbert metric. For `G=G_{mu,N}`, the dual norm of evaluation is

\[
\|L_z\|_{\mu,N,*}^2
=r_z^*G_{\mu,N}^{-1}r_z
=K_{\mu,N}(z).
\]

Since

\[
\Delta_{\Gamma,N}
=\bigcup_{z\in\Gamma}\ker L_z,
\]

we obtain

\[
\operatorname{dist}_{\mu,N}
(b^{(N)},\Delta_{\Gamma,N})
=
\min_{z\in\Gamma}
\frac{|\eta_N(z)|}{\sqrt{K_{\mu,N}(z)}}.
\tag{5}
\]

The source norm is exactly its boundary-response energy,

\[
\|b^{(N)}\|_{\mu,N}^2
=\int_\Gamma |\eta_N(z)|^2\,d\mu(z).
\tag{6}
\]

Hence

\[
\boxed{
\delta_{\mu,N}
=
\min_{z\in\Gamma}
\frac{|\eta_N(z)|}
{\|\eta_N\|_{L^2(\mu)}\sqrt{K_{\mu,N}(z)}}.
}
\tag{7}
\]

This formula isolates the only freedom supplied by boundary reweighting: it may redistribute the evaluation leverage `K_{mu,N}` around the contour. It cannot change the eta function itself or the boundary-zero failure set.

## Leverage conservation forces the universal upper bound

Because `G_{mu,N}` is the average of the rank-one evaluation matrices,

\[
\begin{aligned}
\int_\Gamma K_{\mu,N}(z)\,d\mu(z)
&=
\int_\Gamma
\operatorname{tr}\!\left(
G_{\mu,N}^{-1}r_zr_z^*
\right)d\mu(z)\\
&=
\operatorname{tr}\!\left(
G_{\mu,N}^{-1}
\int_\Gamma r_zr_z^*d\mu(z)
\right)\\
&=
\operatorname{tr}(I_N)\\
&=N.
\end{aligned}
\tag{8}
\]

Therefore

\[
\max_{z\in\Gamma}K_{\mu,N}(z)\ge N.
\tag{9}
\]

The maximum exists because `Gamma` is compact and `K_{mu,N}` is continuous.

Now use the same compact-uniform eta convergence as AF-291. Since `eta` is nonzero on `Gamma`, there are constants

\[
0<m_\Gamma\le M_\Gamma<\infty
\]

such that for every sufficiently large `N`,

\[
m_\Gamma
\le |\eta_N(z)|
\le M_\Gamma
\qquad(z\in\Gamma).
\tag{10}
\]

For every probability measure `mu`, this also gives

\[
m_\Gamma
\le
\|\eta_N\|_{L^2(\mu)}
\le
M_\Gamma.
\tag{11}
\]

Choose `z_mu` with `K_{mu,N}(z_mu)>=N`. From (7),

\[
\delta_{\mu,N}
\le
\frac{M_\Gamma}
{m_\Gamma\sqrt{K_{\mu,N}(z_\mu)}}
\le
\frac{M_\Gamma}{m_\Gamma\sqrt N}.
\tag{12}
\]

This proves the upper half of (2) for **every** full-rank boundary weighting. No spectral condition-number restriction on `G_{mu,N}` is used. The metric may be dense, strongly anisotropic, depend on `N`, and concentrate its measure on a finite set of contour points. The dimension identity alone prevents order-one zero-count margin.

## D-optimal boundary weighting attains the dimension scale

The upper bound is sharp because the leverage can be equalized optimally.

First note that the evaluation vectors span `C^N`. If a coefficient vector `c` were orthogonal to every `r_z`, then the Dirichlet polynomial

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s}
\]

would vanish on all of `Gamma`. Since it is entire, the identity theorem would force `P_c` to vanish identically, and uniqueness of a finite Dirichlet expansion then gives `c=0`. Hence the compact family

\[
\{r_z:z\in\Gamma\}
\]

spans the full coefficient space and admits positive-definite information matrices.

Consider the compact convex set of information matrices

\[
\mathcal G_N
:=
\left\{
\int_\Gamma r_zr_z^*d\mu(z):
\mu\text{ a probability measure on }\Gamma
\right\}.
\]

Choose `G_N^*` maximizing `log det G` over the positive-definite part of this set. Such a maximizer exists and is positive definite: positive-definite feasible matrices exist by spanning, while `log det G` tends to `-infinity` at the singular boundary. Let `mu_N^*` be a design measure realizing `G_N^*`.

For any `z in Gamma`, the segment

\[
G_t=(1-t)G_N^*+t r_zr_z^*,
\qquad 0\le t\le1,
\]

remains feasible. Optimality of `G_N^*` makes the right derivative of `log det G_t` at `t=0` nonpositive. Therefore

\[
0
\ge
\operatorname{tr}\!\left(
(G_N^*)^{-1}(r_zr_z^*-G_N^*)
\right)
=K_{\mu_N^*,N}(z)-N.
\tag{13}
\]

Thus

\[
\boxed{
K_{\mu_N^*,N}(z)\le N
\qquad(z\in\Gamma).
}
\tag{14}
\]

Together with the average identity (8), this is the `D`-optimal/`G`-optimal equality specialized to the complex Dirichlet evaluation family. Substituting (10), (11), and (14) into (7) gives

\[
\delta_{\mu_N^*,N}
\ge
\frac{m_\Gamma}{M_\Gamma\sqrt N}.
\tag{15}
\]

Combining (12) and (15) proves (2).

The measure need not be continuous. Since `G_N^*` lies in the convex hull of the Hermitian rank-one matrices `r_zr_z^*`, finite-dimensional convexity gives a finitely supported realizing measure if desired. The theorem is therefore not relying on an unrealizable continuum weighting.

## Relation to classical optimal design

The optimization above is exactly the classical approximate-design problem behind the Kiefer--Wolfowitz equivalence theorem. In regression language, `G_{mu,N}` is the information matrix, `K_{mu,N}(z)` is the standardized prediction variance or leverage function, maximizing `det G` is `D`-optimality, and minimizing `sup_z K(z)` is `G`-optimality.

Kiefer and Wolfowitz prove that these two extremum problems are equivalent and that the optimal maximum prediction variance equals the number of parameters. Here the parameter dimension is `N`, so their classical constant is precisely the fidelity ceiling appearing in (3)--(4).

The complex Hermitian formulation needed here does not require a separate theorem: the one-line directional derivative argument above proves the required specialization directly. The prior art is important for interpretation and novelty, not for a hidden additional assumption.

This also identifies `K_{mu,N}` as the diagonal of the reproducing kernel for the finite-dimensional Dirichlet-polynomial space equipped with its `L^2(mu)` inner product. Equation (8) is then the finite-dimensional trace identity saying that the integrated diagonal of an orthogonal-projection kernel equals the dimension of its range.

## What the optimized metric gains and what it cannot gain

The raw canonical coefficient geometry of AF-291 has

\[
\delta_{\Gamma,N}^{\mathrm{raw}}
\asymp_\Gamma
\frac{1}{\sqrt N\,H_N(\alpha)},
\qquad
\alpha=\min_{z\in\Gamma}\operatorname{Re}z.
\tag{16}
\]

Optimizing over boundary-observation Gram geometries changes this to

\[
\delta_{\Gamma,N}^{\mathrm{obs,opt}}
\asymp_\Gamma N^{-1/2}.
\tag{17}
\]

So this is not a vacuous no-go theorem. For contours entering the half-plane `alpha<=1/2`, the observation geometry can remove the additional breadth penalty carried by `H_N(alpha)`. It aligns the coefficient metric with what is actually observable on the contour and redistributes evaluation sensitivity optimally.

But the remaining `N^{-1/2}` factor is irreducible inside this whole class. The reason is structural: a full-rank `N`-dimensional observation space has total leverage `N`. No positive probability weighting of the same scalar evaluations can make every evaluation direction have leverage `o(N)`, and a boundary-zero discriminant contains the kernel of every one of those evaluations.

In this sense AF-298 separates two conditioning bills that were conflated in the raw norm:

1. the **coordinate/evaluation bill** `H_N(alpha)`, which a target-aligned observation Gram metric can remove; and
2. the **effective-dimension bill** `sqrt(N)`, which remains even under the optimal boundary weighting.

A future source-natural nonradial geometry therefore has a sharper target. Merely replacing the coefficient norm by a weighted boundary `L^2` norm is insufficient. To beat `N^{-1/2}` it must change the effective target-relevant dimension, retain a richer coupled observable than scalar point evaluation, or exploit arithmetic structure that invalidates the unrestricted `N`-dimensional perturbation model.

## Prior art and novelty assessment

The optimal-design and reproducing-kernel ingredients are classical, and no general novelty is claimed.

- J. Kiefer and J. Wolfowitz, **“The Equivalence of Two Extremum Problems,”** *Canadian Journal of Mathematics* 12, 363--366 (1960). DOI `10.4153/CJM-1960-030-4`. They prove the equivalence of determinant-maximizing and maximum-prediction-variance-minimizing designs, with optimal maximum variance equal to the parameter dimension. This is exactly the classical theorem behind (13)--(14).
- J. Kiefer, **“Optimum Experimental Designs,”** *Journal of the Royal Statistical Society, Series B* 21(2), 272--304 (1959). DOI `10.1111/j.2517-6161.1959.tb00338.x`. This is foundational optimal-design background for information-matrix criteria and design measures.
- The identity `integral K dmu = N` is the standard finite-rank projection/leverage trace identity; in statistical design it is the average prediction-variance identity used in the Kiefer--Wolfowitz theorem. No novelty is claimed for that fact or for the `D`-optimal construction.

A targeted search found classical optimal-design theory and general Dirichlet-polynomial literature, but no basis for claiming that optimal boundary weighting of finite eta zero-count conditioning is itself a known arithmetic theorem. The retained Arithmetic Fidelity result is the channel-specific composition: AF-290's exact distance to the boundary-zero discriminant, AF-291's uniform eta boundary control, and Kiefer--Wolfowitz leverage equalization together give the sharp best possible `N^{-1/2}` margin over the entire boundary-observation Gram class.

## Boundaries and failure modes

- The theorem optimizes only Hilbert metrics generated as positive averages of the scalar boundary evaluation rank-one forms `r_zr_z^*`. An arbitrary source-derived SPD form need not have this representation; AF-293 prices that larger class by condition number instead.
- The weighting measure may depend on `N`, but its support is confined to the fixed target contour. Allowing additional observations away from `Gamma`, derivatives, vector-valued marks, or nonlinear observables changes the information matrix and requires a new audit.
- The metric is target-aligned because `Gamma` is the zero-count contour, but it is not discriminant-distance-defined: `mu_N^*` depends only on the Dirichlet evaluation family on `Gamma`, not on the eta coefficient vector, eta zeros, or the location of `Delta_{Gamma,N}` inside coefficient space.
- Positive definiteness is essential. A singular observation Gram form has already quotiented coefficient directions. Such a quotient can be legitimate only if those directions are independently proved target-null; otherwise it simply hides possible boundary-zero perturbations.
- The `N^{-1/2}` lower construction is asymptotic only through the fixed constants `m_Gamma,M_Gamma` from eta uniform convergence. The leverage equalization itself is exact at every `N` for which the evaluation family spans.
- The result concerns finite zero count on one fixed contour. It does not control individual zero locations, multiplicities, growing-height windows, the global zero divisor, or RH.
- A metric that beats this ceiling by using extra source information would not contradict the theorem. That would be precisely the kind of enriched fidelity mechanism the line is trying to identify.

## Decisive audit test

When a proposed anisotropic repair is built from a positive average of scalar observations `L_z`, form its information matrix

\[
G=\int L_z^*L_z\,d\mu(z)
\]

and its leverage function

\[
K(z)=L_zG^{-1}L_z^*.
\]

If the observation space has dimension `d`, then

\[
\int K\,d\mu=d.
\]

Therefore some retained observation has leverage at least `d`, and a target failure set containing that observation's kernel has normalized Hilbert margin at most order `d^{-1/2}` whenever the nominal response stays uniformly bounded above and below. Reweighting can at best equalize the leverage at `d`; it cannot remove the dimension bill.

For finite eta boundary zero count, `d=N`. A claim that boundary-energy geometry yields breadth-uniform zero-count fidelity must therefore either exhibit a justified reduction of the target-relevant dimension, use observables whose failure kernels no longer sit inside the same discriminant, or add information beyond the scalar boundary evaluation family.

## Consequence for the research frontier

AF-297 left nonradial geometry as a live alternative to target-radial reweighting. AF-298 tests one of the most canonical such geometries and gives a mixed answer.

Boundary-observation Gram geometry is a real improvement: an optimal design removes the extra `H_N(alpha)` deterioration of the raw coefficient metric. But it has a sharp `N^{-1/2}` ceiling enforced by leverage conservation, even with unrestricted `N`-dependent anisotropy inside this observation-generated class.

The useful remaining question is therefore more specific than “find a nonradial metric.” The next candidate should explain why the effective perturbation dimension seen by the zero-sensitive target is smaller than `N`, or why arithmetic coupling supplies observables stronger than independent scalar boundary evaluation. Without such a mechanism, optimal anisotropic reweighting can redistribute sensitivity but cannot make the discriminator uniformly remote.