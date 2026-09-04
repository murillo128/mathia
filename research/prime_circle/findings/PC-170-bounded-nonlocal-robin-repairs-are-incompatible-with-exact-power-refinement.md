# PC-170 — bounded nonlocal Robin repairs are incompatible with exact power refinement

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for repairing the local-operator/domain obstruction of PC-168/PC-169 by adding a fixed bounded, compact, or finite-rank angular Robin operator at the original root circle. Exact second-order power-refinement covariance forces every bounded boundary operator to vanish already for one nontrivial refinement. The first nonzero covariant boundary operators are necessarily unbounded of first-order scale; in the rotation-invariant reflection-symmetric class the canonical survivor is a multiple of the classical Dirichlet-to-Neumann operator `|D_theta|`, so refinement alone still does not supply prime-shell arithmetic.

PC-168 classifies finite-order local differential coefficients compatible with the full Prime-Circle power semigroup and explicitly leaves nonlocal boundary operators and root-circle-supported data outside its theorem. PC-169 then closes the scalar radial inverse-square self-adjoint-extension anomaly but explicitly leaves angular-mode-coupling and root-incidence boundary conditions open. The most direct continuation is therefore to keep the universal second-order bulk operator and place the arithmetic information in a nonlocal self-adjoint operator acting on the angular boundary trace at the original unit circle. This finding gives an exact obstruction for the entire bounded/order-zero part of that continuation.

## 1. The canonical refinement isometry fixes the scaling mismatch

Work on either open side of the root circle in the logarithmic half-cylinder

\[
X=\mathbb R_+\times S^1,
\qquad
(t,\theta),
\qquad
t=|\log|z||,
\]

with Haar measure `dt dtheta/(2pi)`. For an integer refinement `n>=2`, put

\[
(C_n h)(\theta)=h(n\theta)
\tag{1}
\]

on `L^2(S^1)`. Because `theta -> n theta` preserves normalized Haar measure as an `n`-fold covering,

\[
\boxed{C_n^*C_n=I,\qquad \|C_n\|=1.}
\tag{2}
\]

The normalized pullback on the half-cylinder is

\[
(V_n f)(t,\theta)=n^{1/2}f(nt,n\theta).
\tag{3}
\]

The radial half-density makes `V_n` an isometry. For the constant-coefficient second-order bulk Dirichlet form singled out by the regular PC-166/PC-168 branch,

\[
q_0[f]
=\int_X\left(|\partial_t f|^2+|\partial_\theta f|^2\right)
\frac{dt\,d\theta}{2\pi},
\tag{4}
\]

one has exactly

\[
\boxed{q_0[V_n f]=n^2q_0[f].}
\tag{5}
\]

Let `gamma f=f(0,.)` denote the boundary trace. Equation (3) gives

\[
\boxed{\gamma V_nf=n^{1/2}C_n\gamma f.}
\tag{6}
\]

Now let `A` be any bounded self-adjoint operator on `L^2(S^1)`. It defines the standard generalized/nonlocal Robin form

\[
q_A[f]
=q_0[f]+\langle\gamma f,A\gamma f\rangle.
\tag{7}
\]

This includes bounded multiplication operators, bounded integral kernels, compact operators, and finite-rank angular couplings. The trace theorem makes the added term a legitimate lower-order form perturbation of the bulk energy.

Demand the same exact second-order covariance for the **same** boundary operator at every refinement,

\[
q_A[V_nf]=n^2q_A[f].
\tag{8}
\]

Subtracting (5) and using (6) yields, first on the dense trace space and hence on all of `L^2(S^1)`,

\[
\boxed{C_n^*AC_n=nA.}
\tag{9}
\]

The scaling factor `n` is forced: a boundary trace contributes one half-density factor from each side of the quadratic form, whereas the second-order bulk energy has degree two.

## 2. One refinement kills every bounded boundary operator

Equation (9) is already impossible for a nonzero bounded `A`. Since `C_n` is an isometry,

\[
\|C_n^*AC_n\|\le \|A\|.
\tag{10}
\]

But (9) also gives

\[
\|C_n^*AC_n\|=n\|A\|.
\tag{11}
\]

For any `n>1`, (10)--(11) imply

\[
\boxed{A=0.}
\tag{12}
\]

Thus the full integer refinement semigroup is not even needed: **a single nontrivial power refinement excludes every nonzero bounded generalized Robin operator in an exactly covariant second-order Prime-Circle Hamiltonian.**

The conclusion is robust to using the strong Robin boundary condition rather than the quadratic form. If the domain condition is written schematically as

\[
\partial_t f|_{t=0}=A\,\gamma f,
\tag{13}
\]

then refinement of the normal derivative and trace gives the stronger intertwining law

\[
A C_n=n C_nA.
\tag{14}
\]

Taking norms in (14) gives the same obstruction. Hence the no-go is not an artifact of choosing the form formulation.

There is an immediate perturbative consequence. Suppose an unbounded boundary operator `A_0` already obeys (9) on a common core and try to add a bounded root-sensitive correction `K`,

\[
A=A_0+K.
\tag{15}
\]

If `A` is also refinement covariant, subtraction gives

\[
C_n^*KC_n=nK,
\]

so (12) forces

\[
\boxed{K=0.}
\tag{16}
\]

Therefore even after a scale-correct unbounded boundary operator has been found, **no bounded, compact, or finite-rank arithmetic defect can be superimposed while retaining exact refinement covariance**.

This closes a particularly natural use of the finite Prime-Circle root data. Any construction that turns a fixed finite root-incidence matrix into a bounded operator on the canonical boundary Hilbert space, or any bounded regularization of point-root data, lies in the class killed by (12)/(16). Raw point-evaluation distributions and singular self-adjoint boundary relations are not bounded operators on this boundary `L^2` space and are deliberately outside the theorem.

## 3. The sharp escape is first-order and immediately classical in the symmetric sector

Boundedness is genuinely load-bearing. Let

\[
e_k(\theta)=e^{ik\theta},
\qquad k\in\mathbb Z.
\]

Then

\[
C_ne_k=e_{nk}.
\tag{17}
\]

For the angular derivative `D=-i partial_theta` and its positive modulus

\[
|D|=(-\partial_\theta^2)^{1/2},
\]

one obtains on trigonometric polynomials

\[
D C_n=n C_nD,
\qquad
|D|C_n=nC_n|D|,
\tag{18}
\]

and hence

\[
\boxed{C_n^*|D|C_n=n|D|.}
\tag{19}
\]

So a nonzero covariant boundary operator exists, but it must have the missing first-order growth.

The rotation-invariant class can be classified exactly. If a self-adjoint boundary operator is a Fourier multiplier

\[
Ae_k=a_ke_k
\tag{20}
\]

and satisfies (9) for every integer `n>=2`, then

\[
\boxed{a_{nk}=n a_k.}
\tag{21}
\]

Consequently

\[
a_0=0,
\qquad
a_k=k a_1\ (k>0),
\qquad
a_{-k}=k a_{-1}\ (k>0).
\tag{22}
\]

Thus the whole translation-invariant covariant family has only two real slope parameters, one on each orientation. If reflection `theta -> -theta` is also a symmetry, `a_1=a_{-1}` and

\[
\boxed{A=c|D|.}
\tag{23}
\]

For `c>=0` this is the positive symmetric branch. The operator `|D|` is exactly the classical Dirichlet-to-Neumann/Steklov operator of the Euclidean unit disk: its Fourier eigenvalue on `e_k` is `|k|`. Therefore the sharpest symmetry-preserving unbounded escape is not a new Prime-Circle operator at all; it is standard boundary harmonic analysis.

This stress test also identifies the precise surviving non-symmetric boundary. For a general operator with Fourier matrix elements

\[
a_{jk}=\langle e_j,Ae_k\rangle,
\]

formal covariance gives

\[
\boxed{a_{nj,nk}=n a_{jk}.}
\tag{24}
\]

Equation (24) still leaves arbitrary data on primitive lattice directions `(j,k)/gcd(j,k)`. Refinement covariance by itself therefore does **not** choose a prime-sensitive unbounded operator; it merely forces first-order homogeneity along every integer dilation orbit. A future positive mechanism would have to derive those primitive-direction coefficients canonically from embedded old/new root geometry and survive a matched non-prime control, rather than choosing them freely.

## 4. Prior art and novelty audit

Generalized and genuinely nonlocal Robin boundary operators are classical. Fritz Gesztesy and Marius Mitrea, **Nonlocal Robin Laplacians and some remarks on a paper by Filonov on eigenvalue inequalities**, *Journal of Differential Equations* 247:10 (2009), 2871--2896, DOI `10.1016/j.jde.2009.07.007`, characterize self-adjoint Laplacians with local and nonlocal Robin-type boundary operators on Lipschitz domains. This supplies the standard analytic framework for treating `A` in (7)/(13); no novelty is claimed for nonlocal Robin realizations themselves.

The unbounded survivor is equally classical. Bruno Colbois, Alexandre Girouard, Carolyn Gordon and David Sher, **Some recent developments on the Steklov eigenvalue problem**, *Revista Matemática Complutense* 37 (2024), 1--161, DOI `10.1007/s13163-023-00480-3`, reviews the Dirichlet-to-Neumann operator and records explicitly that on the Euclidean disk

\[
\mathcal D_{\mathbb B^2}=\sqrt{\Delta_{S^1}}=|D|.
\]

Thus neither the boundary-operator formalism nor the first-order scale-correct symmetric operator is historically new. Targeted searches across nonlocal Robin Laplacians, boundary triples, Steklov/Dirichlet-to-Neumann operators, and scale-covariant boundary conditions did not locate this exact Prime-Circle compression statement, but absence of an exact wording match is not treated as novelty. The durable contribution here is the elementary line-specific obstruction (9)--(16): the power-covering isometries are incompatible with every bounded arithmetic boundary correction at second-order scale.

## 5. Consequence for the Prime-Circle/RH search

PC-168 showed that the local coefficients of a fully refinement-covariant second-order operator are universal homogeneous cone data. PC-169 showed that the remaining scalar inverse-square radial domain anomaly either collapses to universal scale-fixed domains or is incompatible with the full semigroup. The natural next repair was to put the missing root arithmetic in an angular or nonlocal boundary operator at `t=0`.

Equations (12) and (16) close the complete bounded/order-zero part of that repair. A bounded multiplication profile, compact kernel, finite-rank root-incidence matrix, or bounded root-sensitive perturbation of the canonical `|D|` boundary operator cannot coexist with exact Prime-Circle power covariance. The only bounded graph-type Robin choice is Neumann `A=0`; Dirichlet is the separate universal infinite-coupling boundary and carries no root arithmetic.

This is **not** a no-go for every boundary mechanism. Unbounded first-order operators satisfying (24), singular point-supported/distributional self-adjoint extensions, level-dependent or shell-dependent boundary families, cross-level boundary relations, and genuinely nonlinear/nonlocal constructions remain outside the theorem. In particular, (24) leaves a mathematically real opening for a geometry-forced unbounded operator whose primitive Fourier-pair coefficients come from exact old/new incidence. What is ruled out is the much easier route of encoding those data as any fixed bounded or finite-rank boundary correction.

No `s`-parameter, Riemann zeros, functional equation, or critical line is produced here. The result is instead a sharp obstruction on where such information **cannot** live: under exact second-order refinement covariance, it cannot reside in bounded boundary data. The first admissible linear boundary scale is the classical order-one Dirichlet-to-Neumann scale, and any arithmetic content beyond that must be derived from additional Prime-Circle structure rather than from refinement covariance alone.