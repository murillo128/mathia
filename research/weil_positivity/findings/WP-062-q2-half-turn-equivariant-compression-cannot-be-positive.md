# WP-062 — `q=2` half-turn-equivariant compression cannot make the full-root Hardy channel positive

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-MECHANISM`. The anticommuting-involution argument is standard chiral/off-diagonal linear algebra, and positivity of finite Hilbert matrices is classical Gram geometry. No theorem-level historical novelty is claimed. The Mathia-specific content is that the full-root `q=2` Hardy operator selected in `WP-048` and isolated in `WP-061` has an exact half-turn chiral symmetry, so every nonzero compression that preserves that symmetry is automatically indefinite. Its canonical finite Hardy sections in fact have exactly balanced and unbounded positive/negative inertia.

`WP-061` leaves open a relative/graded/compressed Hardy-space escape: perhaps the full-root channel

\[
\mathcal F_2=\Gamma_1+\Gamma_2=-H+DHD
\]

could become positive after a canonical compression while retaining the full `q=2` archimedean response. There is now a sharp obstruction to the most symmetric version of that escape. Here

\[
H_{jk}=\frac1{j+k+1},
\qquad
De_j=(-1)^j e_j.
\]

The involution `D` implements the Hardy half-turn `f(z)\mapsto f(-z)`. It is **not** the anchored reflection `z\mapsto\bar z` of `WP-048`; rather, once that reflection has intrinsically selected the full root set `mu_2={1,-1}`, the field `V_2(z)=Log(1-z^2)` has the additional exact half-turn symmetry exchanging its two roots. The resulting Hankel/Hardy operator transforms oddly under that half-turn because of the `j+k+1` Hankel index.

## 1. The selected full-root operator anticommutes exactly with the half-turn

From `D^2=I` and

\[
\mathcal F_2=-H+DHD,
\]

one gets

\[
D\mathcal F_2D
=-DHD+H
=-\mathcal F_2.
\tag{1}
\]

Equivalently,

\[
\boxed{\{D,\mathcal F_2\}=0.}
\tag{2}
\]

Thus the full-root `q=2` channel has the standard chiral/off-diagonal symmetry: `D` maps every positive spectral direction to a negative one of the same magnitude.

There is also a direct moment interpretation. For a finitely supported coefficient vector `c=(c_j)` and

\[
p_c(x)=\sum_j c_jx^j,
\]

Hilbert Gram geometry gives

\[
\langle c,Hc\rangle
=\int_0^1|p_c(x)|^2\,dx,
\]

while

\[
\langle c,DHDc\rangle
=\int_{-1}^0|p_c(x)|^2\,dx.
\]

Hence

\[
\boxed{
\langle c,\mathcal F_2c\rangle
=\int_{-1}^0|p_c(x)|^2\,dx
-\int_0^1|p_c(x)|^2\,dx.
}
\tag{3}
\]

Applying `D` sends `p_c(x)` to `p_c(-x)` and exchanges the two half-intervals, so (3) changes sign. This independently recovers (1) and makes clear that the indefiniteness is built into the full two-root channel rather than caused by a basis accident.

## 2. Every half-turn-equivariant semidefinite compression is zero

Let `M` be a closed `D`-invariant subspace of `ell^2`, let `P_M` be its orthogonal projection, and define the compressed self-adjoint operator

\[
A_M=P_M\mathcal F_2P_M\big|_M.
\tag{4}
\]

Because `M` is `D`-invariant and `D` is a self-adjoint unitary involution,

\[
P_MD=DP_M.
\]

Therefore (1) descends exactly to the compression:

\[
D|_M\,A_M\,D|_M=-A_M.
\tag{5}
\]

If `A_M\succeq0`, unitary conjugation by `D|_M` also gives

\[
-A_M\succeq0.
\]

Thus `A_M\preceq0` as well, and consequently

\[
\boxed{A_M=0.}
\tag{6}
\]

The same argument applies if one starts by assuming `A_M\preceq0`. Hence

\[
\boxed{
A_M\neq0
\quad\Longrightarrow\quad
A_M\text{ is indefinite}
}
\tag{7}
\]

for every half-turn-equivariant compression.

This is stronger than the two-vector counterexample in `WP-061`: positivity cannot be recovered by choosing a nontrivial closed subspace while preserving the exact `q=2` half-turn symmetry. Trivial parity compressions such as the purely even or purely odd Hardy subspace indeed give `A_M=0`; they erase the channel rather than produce a positive archimedean form.

## 3. Canonical finite Hardy sections have exactly balanced inertia `(m,m,0)`

The sign pairing is not a delicate infinite-dimensional effect. For `m>=1`, let

\[
E_m^+
=\operatorname{span}\{e_0,e_2,\ldots,e_{2m-2}\},
\qquad
E_m^-
=\operatorname{span}\{e_1,e_3,\ldots,e_{2m-1}\},
\]

and

\[
E_m=E_m^+\oplus E_m^-.
\]

In this parity-ordered basis, `WP-061`'s off-diagonal formula becomes exact finite-dimensional Hilbert geometry. Since

\[
H_{2i,2j+1}
=\frac1{2i+2j+2}
=\frac12\frac1{i+j+1},
\]

we have

\[
\boxed{
\mathcal F_2\big|_{E_m}
=
\begin{pmatrix}
0&-H_m\\
-H_m&0
\end{pmatrix},
}
\tag{8}
\]

where

\[
(H_m)_{ij}=\frac1{i+j+1},
\qquad 0\le i,j<m.
\]

`H_m` is positive definite because it is the Gram matrix of the linearly independent monomials `1,x,...,x^{m-1}` in `L^2(0,1)`. If

\[
H_mv=\lambda v,
\qquad \lambda>0,
\]

then

\[
\begin{pmatrix}v\\v\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}v\\-v\end{pmatrix}
\]

are eigenvectors of (8) with eigenvalues `-lambda` and `+lambda`, respectively. Therefore

\[
\boxed{
\operatorname{Inertia}(\mathcal F_2|_{E_m})=(m,m,0).
}
\tag{9}
\]

In particular the positive and negative indices of the full-root channel are both unbounded. The `m=1` case is exactly the `e_0\pm e_1` witness from `WP-061`; (9) shows that witness is the first member of an arbitrarily large balanced family.

## 4. Finite-codimensional symmetry-preserving restriction still has infinite two-sided index

The obstruction also rules out removing only finitely many bad Hardy directions.

Let `M` be `D`-invariant with finite codimension

\[
\operatorname{codim}M=d<\infty.
\]

Inside the `2m`-dimensional space `E_m`, set

\[
W_m=M\cap E_m.
\]

Then

\[
\operatorname{codim}_{E_m}W_m\le d.
\tag{10}
\]

Let `P_m^+` and `P_m^-` denote the positive and negative spectral subspaces of the finite form (8), each of dimension `m`. The elementary dimension inequality gives

\[
\dim(W_m\cap P_m^+)\ge m-d,
\qquad
\dim(W_m\cap P_m^-)\ge m-d.
\tag{11}
\]

Every nonzero vector in the first intersection has positive quadratic value and every nonzero vector in the second has negative quadratic value. Hence the quadratic form of the compression to `M` has at least `m-d` positive and `m-d` negative independent directions for every `m>d`. Letting `m` grow yields

\[
\boxed{
n_+(A_M)=n_-(A_M)=\infty
}
\tag{12}
\]

for every finite-codimensional `D`-invariant `M`.

So the failure cannot be repaired by a finite list of constraints, counterterms represented as deleted Hardy directions, or a finite-codimensional primitive condition while preserving half-turn symmetry.

## 5. What this does and does not rule out

This finding kills only the **half-turn-equivariant compression** route. It does not claim that every compression of `mathcal F_2` is indefinite.

A non-`D`-invariant subspace can certainly carry a positive restriction. The positive spectral subspace of `mathcal F_2` is the tautological example. But that subspace is selected from the sign decomposition of the very operator whose positivity one is trying to explain; using it without a prior independent Mathia construction would simply insert the answer at the compression stage.

A genuinely surviving compression must therefore satisfy all of the following:

1. break or polarize the `q=2` half-turn pairing by an independently forced geometric structure rather than by spectral sign selection;
2. retain the **full-root** channel, not silently replace it by the positive primitive `Gamma_2` of `WP-061`;
3. preserve the linear Mellin response that yields the Riemann Gamma logarithmic derivative rather than an absolute-value or squared-energy surrogate;
4. couple to the sparse finite-prime `Lambda(n)/sqrt(n)` term and the polar counterterm before the final sign theorem.

The distinction from `WP-049` is exact. `WP-049` studies the anchored-reflection involution on primitive profinite conductor shells and proves parity-isospectral cancellation of the Mangoldt determinant beyond order two. The present result concerns the **different** half-turn involution `D` on the Hardy coefficient space of the already-selected full-root `q=2` field and proves a no-go for positive compressions of that archimedean operator itself.

## 6. Matched controls and novelty audit

The mechanism behind (1)--(12) is classical. For any self-adjoint operator `A` and unitary involution `J` satisfying

\[
JAJ=-A,
\]

the spectrum is paired under `lambda\leftrightarrow-lambda`, and every `J`-invariant semidefinite compression is zero. In finite dimensions this is the familiar off-diagonal/chiral-symmetry normal form. Likewise, the positivity of `H_m` is simply Gram positivity for monomials.

A targeted prior-art audit of chiral-symmetry/off-diagonal operator literature and Hilbert-matrix Gram geometry therefore gives no basis for a novelty claim for the abstract theorem. The project-specific content is the exact identification

\[
\mathcal F_2=-H+DHD,
\qquad
D\mathcal F_2D=-\mathcal F_2,
\]

inside the same Mathia root channel that `WP-048` independently selected and `WP-061` proposed as a possible compressed bridge.

The strongest matched control is correspondingly unfavorable: any symmetric signed-moment form

\[
\int_{-1}^0|p(x)|^2w(|x|)\,dx
-
\int_0^1|p(x)|^2w(x)\,dx,
\qquad w\ge0,
\]

has the same half-turn/chiral obstruction. Thus the sign theorem is not arithmetic. Arithmetic significance could arise only from an additional canonical map that couples this signed archimedean channel to the finite Weil data before compression.

## 7. Consequence for the Weil-positivity frontier

The compressed-Hardy escape left open by `WP-061` is now narrower:

\[
\boxed{
\text{full-root }q=2
+\text{ half-turn-equivariant compression}
\not\Longrightarrow
\text{nontrivial positive form}.
}
\]

Moreover the obstruction has infinite two-sided index, so no finite-codimensional symmetry-preserving primitive condition can remove it.

A successful Mathia-native global positivity mechanism must therefore introduce a **canonical polarization or symmetry-breaking coupling before positivity is taken**. Such a structure would have to explain why one member of each half-turn sign pair is retained or recombined, while simultaneously preserving the exact finite-prime support, the full `q=2` archimedean Mellin channel, and the polar/global counterterms. Without that extra structure, compression of the selected full-root Hardy operator cannot supply the required independent Weil sign theorem.