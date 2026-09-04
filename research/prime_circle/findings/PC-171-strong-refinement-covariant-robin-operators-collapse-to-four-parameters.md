# PC-171 — strong refinement-covariant Robin operators collapse to four parameters

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the strong unbounded Robin/DtN escape left open by PC-170. If one fixed self-adjoint boundary operator is required to intertwine the full Prime-Circle power-refinement semigroup at first-order scale, then on the natural trigonometric core it cannot carry arbitrary primitive Fourier-pair data: every absolute-frequency pair is a copy of one fixed Hermitian `2 x 2` block. Equivalently, the entire operator is a four-real-parameter combination of `|D|`, `D`, reflection, and their first-order reflected partner. Exact strong refinement therefore leaves no mode- or level-dependent slot in which intrinsic prime-shell arithmetic can live.

PC-170 proved that bounded generalized Robin corrections are impossible under exact second-order form covariance and observed two distinct unbounded boundaries. Rotation-invariant operators collapse to the classical Dirichlet-to-Neumann scale `|D|`, while the weaker form relation `C_n^* A C_n = n A` allows large primitive-lattice freedom in the Fourier matrix. The remaining natural question is whether the **strong boundary-condition covariance**

\[
A C_n=n C_n A
\tag{1}
\]

can support a genuinely noncommutative unbounded angular operator whose off-diagonal primitive Fourier data encode the old/new Prime-Circle geometry. The answer is no under the standard common-core hypothesis.

## 1. Exact theorem on the boundary circle

Let

\[
e_k(\theta)=e^{ik\theta},\qquad k\in\mathbb Z,
\]

be the Fourier basis of `L^2(S^1)`, and let

\[
(C_n f)(\theta)=f(n\theta),\qquad n\ge2,
\]

so that

\[
C_n e_k=e_{nk}.
\tag{2}
\]

Let `A` be self-adjoint with the trigonometric polynomials as a core, assume every `C_n` preserves that core, and suppose (1) holds there for **every** integer `n>=2`. The coefficient argument below in fact needs only symmetry on this core; the core assumption is what makes the resulting Fourier action determine the self-adjoint realization. Write

\[
a_{jk}=\langle e_j,Ae_k\rangle.
\]

Taking the `e_j` coefficient in (1) gives the exact recursion

\[
\boxed{
 a_{j,nk}=
 \begin{cases}
 n\,a_{j/n,k},&n\mid j,\\
 0,&n\nmid j.
 \end{cases}}
\tag{3}
\]

Fix a nonzero column `q`. Put `n=|q|` and `k=sgn(q)` in (3). Then

\[
\boxed{a_{j,q}=0\quad\text{unless}\quad |q|\mid j.}
\tag{4}
\]

Symmetry gives `a_{q,j}=overline{a_{j,q}}`. Applying (4) to column `j` shows that a nonzero coefficient also requires `|j|\mid q`. Therefore

\[
\boxed{a_{j,q}\ne0\Longrightarrow |j|=|q|.}
\tag{5}
\]

So there is no coupling between different absolute Fourier frequencies. Every two-dimensional orientation space

\[
E_r=\operatorname{span}\{e_r,e_{-r}\},\qquad r\ge1,
\]

is reducing for `A` on the core.

Now apply (3) with `n=r` and base columns `k=+1,-1`. All four matrix entries on `E_r` scale from the `r=1` block. Hence there is one fixed Hermitian matrix `M` such that

\[
\boxed{A|_{E_r}=rM\qquad(r\ge1).}
\tag{6}
\]

The constant mode also vanishes. Since `C_n e_0=e_0`, equation (1) gives

\[
Ae_0=nC_nAe_0.
\]

Because `C_n` is an isometry,

\[
\|Ae_0\|=n\|Ae_0\|,
\]

and therefore

\[
\boxed{Ae_0=0.}
\tag{7}
\]

Equations (6)--(7) are the complete Fourier classification on the trigonometric core. Since that core determines `A`, the self-adjoint realization is the direct-sum block multiplier with blocks `rM` and maximal graph domain

\[
\mathcal D(A)=\left\{v=(v_r)_{r\ge1}:\sum_{r\ge1}r^2\|Mv_r\|^2<\infty\right\}
\]

plus the free zero mode. Conversely, every fixed Hermitian `M` gives this self-adjoint block multiplier and satisfies (1) on the trigonometric core.

## 2. The four-parameter normal form

Let

\[
D=-i\partial_\theta,
\qquad
R e_k=e_{-k}.
\]

Then `R` is unitary and self-adjoint, `R D=-D R`, and `R` commutes with `|D|`. On trigonometric polynomials the four operators

\[
|D|,\qquad D,\qquad |D|R,\qquad iDR
\]

are symmetric and each obeys (1), because

\[
D C_n=nC_nD,
\qquad
|D|C_n=nC_n|D|,
\qquad
RC_n=C_nR.
\tag{8}
\]

A general Hermitian block

\[
M=
\begin{pmatrix}
a&c\\
\overline c&d
\end{pmatrix}
\]

has four real parameters. Writing them as `alpha,beta,gamma,delta` gives, on the common core, the equivalent normal form

\[
\boxed{
A=\alpha|D|+\beta D+\gamma|D|R+\delta\,iDR,
\qquad
\alpha,\beta,\gamma,\delta\in\mathbb R.
}
\tag{9}
\]

Its self-adjoint closure is exactly the block multiplier described above; when the block is singular, its maximal graph domain can be larger than the common `H^1` domain because the zero-eigenvalue channel carries no first-order growth. On `E_r`, the block is

\[
r
\begin{pmatrix}
\alpha+\beta&\gamma+i\delta\\
\gamma-i\delta&\alpha-\beta
\end{pmatrix}.
\tag{10}
\]

If the Robin form is additionally required to be nonnegative, (10) merely restricts this fixed matrix to the positive-semidefinite cone; it does not restore any frequency-dependent arithmetic freedom. Reflection symmetry `RA=AR` forces `beta=delta=0`, leaving `A=alpha|D|+gamma|D|R`. If rotation invariance is imposed as well, `gamma=0`, and one recovers precisely the classical `alpha|D|` branch identified in PC-170.

## 3. Why strong covariance is much more rigid than the form relation

The distinction from PC-170 is load-bearing. The quadratic-form covariance

\[
C_n^*AC_n=nA
\tag{11}
\]

only samples matrix entries whose two indices are simultaneously divisible by `n`, yielding

\[
a_{nj,nk}=n a_{jk}.
\]

That relation indeed leaves arbitrary data on primitive lattice directions `(j,k)/gcd(j,k)`. By contrast, the strong intertwining (1) controls **every row of every dilated column** through (3). Self-adjointness then reflects the column-divisibility condition back across the diagonal, and the two divisibility constraints force `|j|=|k|`.

Thus removing the boundedness hypothesis from PC-170 does not reopen the strong Robin boundary-condition branch. The apparent primitive-lattice freedom belongs to the weaker form-covariant problem, not to a self-adjoint boundary operator whose domain relation itself is transported exactly by every power covering.

A matched non-prime control is immediate: the proof uses only the bare circle, its Fourier basis, self-adjointness, and the covering maps `theta -> n theta`. No primitive roots, cyclotomic polynomials, von Mangoldt weights, or old/new shell incidence enter (3)--(10). The same four-parameter classification exists before any Prime-Circle data are inserted.

## 4. Stress tests and sharp boundaries

The theorem genuinely needs its hypotheses.

First, self-adjointness/symmetry is essential. Without it, (4) only constrains the support of each column and does not reflect the divisibility condition back to force equal absolute frequencies; triangular divisibility intertwiners can survive.

Second, the **full** power semigroup is essential to the stated four-parameter result. If covariance is demanded only for one fixed refinement, such as `n=2`, independent dilation orbits remain and the classification is much larger.

Third, the result assumes the trigonometric polynomials lie in the operator domain, are preserved by the covering maps, and form a core for the self-adjoint realization. This is the natural setting for the standard first-order Fourier/pseudodifferential/DtN operators relevant to the Robin continuation. Self-adjoint realizations for which this Fourier core is not available are outside the statement.

Fourth, `A` is the same boundary operator transported through every refinement. Level-dependent or shell-dependent families `A_n`, singular point-supported boundary relations, nonlinear boundary maps, and weaker unbounded solutions of (11) are not ruled out.

A direct falsification test is therefore simple: any claimed counterexample in this class must exhibit a nonzero coefficient `a_{jk}` with `|j| != |k|`. Equations (3)--(5) then identify the exact violated assumption: full strong covariance, symmetry, or the common Fourier core.

## 5. Prior art and novelty audit

The surrounding ingredients are classical rather than new. Monomial power maps `z -> z^n` and their induced composition/Koopman operators are standard objects in composition-operator and dynamical-systems theory; the Bost--Connes/cyclotomic power semigroup is already the explicit prior-art boundary recorded in PC-010. The first-order survivor `|D|` is the classical Dirichlet-to-Neumann/Steklov operator on the unit disk, with the authoritative source already recorded for PC-170 in `SOURCES.md`. General self-adjoint nonlocal Robin boundary operators are likewise classical and are anchored there by Gesztesy--Mitrea.

Targeted searches across monomial composition operators, composition--differentiation intertwiners, Koopman operators for expanding circle maps, Bost--Connes semigroup isometries, and DtN/Steklov operators did not locate this exact four-parameter classification under simultaneous strong intertwining by all power maps. That absence is **not** treated as a novelty claim. The proof is elementary Fourier/divisibility algebra once (1) is posed. The durable contribution is the Prime-Circle-specific no-go consequence: the strongest natural unbounded Robin continuation left open by PC-170 collapses to universal first-order circle structure and cannot carry mode-resolved arithmetic without relaxing one of the theorem's hypotheses.

## 6. Consequence for the Prime-Circle/RH search

The natural chain

\[
\text{exact power refinement}
\longrightarrow
\text{one fixed self-adjoint unbounded Robin/DtN operator}
\longrightarrow
\text{primitive Fourier-pair arithmetic}
\longrightarrow
\text{new RH mechanism}
\]

is therefore closed under strong boundary-condition covariance. Refinement does permit nonzero unbounded operators, but it leaves only four global real constants multiplying universal first-order circle operators. Any arithmetic encoded by choosing those constants would be externally inserted rather than generated as level- or mode-dependent Prime-Circle geometry.

What remains open is materially narrower: unbounded operators satisfying only the weaker form covariance (11) whose primitive-direction coefficients are *derived* from old/new shell geometry; shell-dependent or cross-level boundary families; singular point-supported self-adjoint relations; and genuinely nonlinear constructions. None of those is classified here. No `s`-parameter, zeta zero set, functional equation, or critical-line mechanism is produced; this finding instead removes the strong fixed-operator Robin branch from the viable search space.
