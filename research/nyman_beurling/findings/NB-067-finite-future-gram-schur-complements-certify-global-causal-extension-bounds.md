# NB-067 — finite future Gram Schur complements certify global causal extension bounds

**Status:** `EXACT-DERIVED + FUTURE-KERNEL-IDENTIFICATION + FINITE-SCHUR-CERTIFICATE + MONOTONE-SOURCE-UPPER-BOUNDS + STABLE-TAIL-SUFFICIENT-CRITERION + FLAT-CONTROL + METHOD-ADVANCE`.

`NB-066` reduces the current collective-tail frontier to one source-only quantity. If

\[
\mathcal A=\overline{\operatorname{span}}\{D_j:j\ge1\}
\]

is the natural Blaschke-deflated Nyman space, `J_R` is Paley--Wiener truncation to `[0,\log R]`, and

\[
\mathcal G_R=J_R\mathcal A
=\operatorname{span}\{J_RD_j:1\le j<R\},
\]

then `NB-066` defines the worst exact future-extension cost

\[
\Lambda_R
:=
\sup_{0\ne g\in\mathcal G_R}
\frac{1}{\|g\|}
\inf\left\{
\|(I-J_R)a\|:
 a\in\mathcal A,\ J_Ra=g
\right\}.
\tag{1}
\]

A bounded `Lambda_R` on any unbounded sequence of windows forces the stable tail `T_infinity` to vanish. The remaining difficulty was that (1) is phrased as an infinite-dimensional extension problem. The present finding removes that oracle: **`Lambda_R` is the monotone limit of explicit finite generalized eigenvalues obtained from Schur complements of the causal innovation Gram matrix.** Every finite future horizon gives a rigorous source-only *upper* bound.

For `N>=R`, let

\[
\mathcal F_{R,N}
:=\operatorname{span}\{D_R,\ldots,D_N\},
\qquad
\mathcal A_{\ge R}
:=\overline{\operatorname{span}}\{D_j:j\ge R\}.
\tag{2}
\]

Then first,

\[
\boxed{
\ker(J_R|_{\mathcal A})=\mathcal A_{\ge R}.
}
\tag{3}
\]

Thus every global natural extension of a visible trace differs from its unique causal prefix by a vector from the closed future span; there are no hidden zero-trace directions outside the later innovations.

Let `P={1,...,R-1}` and, for `c in C^(R-1)`, put

\[
s_c:=\sum_{j<R}c_jD_j,
\qquad
g_c:=J_Rs_c.
\tag{4}
\]

The visible Gram matrix

\[
A_R:=\bigl(\langle J_RD_i,J_RD_j\rangle\bigr)_{i,j<R}
\tag{5}
\]

is positive definite by `NB-062`, and

\[
\|g_c\|^2=c^*A_Rc.
\tag{6}
\]

Let `H^(N)` be the global Gram matrix of `D_1,...,D_N`, partitioned into the prefix block `P` and the future block `F={R,...,N}`. Define the Schur complement

\[
S_{R,N}
:=
H^{(N)}_{PP}
-
H^{(N)}_{PF}
\bigl(H^{(N)}_{FF}\bigr)^{-1}
H^{(N)}_{FP}.
\tag{7}
\]

Finite linear independence of the `D_j` makes `H^(N)_{FF}` positive definite. Standard least squares gives the exact identity

\[
\boxed{
c^*S_{R,N}c
=
\inf_{v\in\mathcal F_{R,N}}
\|s_c+v\|^2.
}
\tag{8}
\]

As `N` increases, the future spaces increase to `A_(>=R)`. Therefore

\[
S_{R,N}\downarrow S_R
\quad\text{in Loewner order},
\tag{9}
\]

where

\[
c^*S_Rc
=
\inf_{v\in\mathcal A_{\ge R}}
\|s_c+v\|^2.
\tag{10}
\]

Because the prefix dimension is finite, the monotone quadratic-form convergence is ordinary matrix-norm convergence.

The early and future time pieces are orthogonal. Every `s_c+v` in (10) has the same early trace `g_c`, hence

\[
\inf_{v\in\mathcal A_{\ge R}}
\|(I-J_R)(s_c+v)\|^2
=
c^*S_Rc-c^*A_Rc.
\tag{11}
\]

Consequently

\[
\boxed{
1+\Lambda_R^2
=
\lambda_{\max}\!\left(
A_R^{-1/2}S_RA_R^{-1/2}
\right).
}
\tag{12}
\]

Combining (9) and (12) gives the finite-horizon certificate

\[
\boxed{
\Xi_{R,N}
:=
\lambda_{\max}\!\left(
A_R^{-1/2}S_{R,N}A_R^{-1/2}
\right)
\downarrow
1+\Lambda_R^2.
}
\tag{13}
\]

In particular, every finite `N>=R` gives

\[
\boxed{
\Lambda_R^2\le \Xi_{R,N}-1.
}
\tag{14}
\]

This is the useful direction: no infinite future projection and no canonical target residual are needed to certify an upper bound for the exact global continuation cost.

## 1. The zero-trace natural space is exactly the future innovation span

The inclusion `A_(>=R) subseteq ker(J_R|A)` is immediate from `NB-062`: every `D_j` with `j>=R` starts at time `log j>=log R`.

For the converse, let `a in A` satisfy `J_Ra=0`. Choose finite causal sums

\[
a_n=\sum_{j=1}^{M_n}c_{n,j}D_j\longrightarrow a.
\tag{15}
\]

Then `J_Ra_n -> 0`. Since all terms with `j>=R` vanish under `J_R`,

\[
J_Ra_n
=
\sum_{j<R}c_{n,j}J_RD_j.
\tag{16}
\]

`NB-062` proves that `{J_RD_j}_{j<R}` is a basis of the finite-dimensional space `G_R`. Hence convergence of (16) to zero forces each prefix coefficient `c_(n,j)->0` for `j<R`. The finite prefix

\[
p_n:=\sum_{j<R}c_{n,j}D_j
\tag{17}
\]

therefore converges to zero in the ambient Hardy norm. The remainder

\[
f_n:=a_n-p_n\in\operatorname{span}\{D_j:j\ge R\}
\tag{18}
\]

converges to `a`, proving `a in A_(>=R)` and hence (3).

This step matters. Without (3), a finite Schur complement against later innovations would only bound an artificial restricted extension problem. Equation (3) shows that the later causal innovations exhaust **all** exact natural corrections that leave the first `R` window unchanged.

## 2. Schur complements are exact finite continuation costs

Fix `c`. Any extension of the visible trace `g_c` has the form

\[
a=s_c+v,
\qquad v\in\mathcal A_{\ge R},
\tag{19}
\]

by (3). At finite horizon, write `v=sum_(j=R)^N d_jD_j`. Expanding the squared norm using the block Gram matrix gives

\[
\|s_c+v\|^2
=
c^*H_{PP}^{(N)}c
+2\Re\,c^*H_{PF}^{(N)}d
+d^*H_{FF}^{(N)}d.
\tag{20}
\]

The unique minimizer is

\[
d_*=-(H_{FF}^{(N)})^{-1}H_{FP}^{(N)}c,
\tag{21}
\]

and substitution gives (8). Equivalently, `S_(R,N)` is the Gram matrix of the prefix innovations after orthogonal projection away from the finite future span.

The spaces `F_(R,N)` increase with `N`; distances to them therefore decrease. This proves Loewner monotonicity in (9). Their union is dense in `A_(>=R)`, so the limiting distance is exactly (10). Since `C^(R-1)` is finite-dimensional, pointwise monotone convergence of these positive quadratic forms gives norm convergence of the matrices.

Finally, `J_R(s_c+v)=g_c` for every admissible `v`. The Paley--Wiener split is orthogonal, hence

\[
\|s_c+v\|^2
=
\|g_c\|^2
+
\|(I-J_R)(s_c+v)\|^2.
\tag{22}
\]

Taking the infimum and using (6), (10) yields (11). Maximizing the resulting Rayleigh quotient proves (12)--(13).

## 3. A finite matrix inequality now kills the entire stable tail

`NB-066` proves that any nonzero `t in T_infinity` forces

\[
\Lambda_R\longrightarrow\infty.
\tag{23}
\]

Equations (13)--(14) turn its contrapositive into a finite certificate. Suppose there are an unbounded sequence `R_k`, finite horizons `N_k>=R_k`, and a constant `C<infinity` such that

\[
\boxed{
S_{R_k,N_k}\preceq C^2A_{R_k}.
}
\tag{24}
\]

Then `Xi_(R_k,N_k)<=C^2`, hence

\[
\Lambda_{R_k}\le\sqrt{C^2-1},
\tag{25}
\]

and `NB-066` forces

\[
\boxed{
\mathcal T_\infty=\{0\}.
}
\tag{26}
\]

Consequently the collective late quotient tends strongly to zero on every arithmetic defect vector, in particular on the canonical residual `h_*=Qe`.

The falsification direction is equally sharp. If a nonzero stable-tail mode exists, then for **every** choice of finite future horizons `N(R)>=R`,

\[
\boxed{
\Xi_{R,N(R)}\longrightarrow\infty.
}
\tag{27}
\]

because `Xi_(R,N)>=1+Lambda_R^2`. Thus a bounded finite-horizon certificate cannot be a truncation artefact: finding one on an unbounded sequence is already enough to rule out the stable tail globally.

This materially changes the practical status of the `NB-066` criterion. The live source theorem is no longer forced to estimate an infinite-dimensional right inverse directly. It is enough to prove, or rigorously certify, the finite generalized-eigenvalue inequality (24) for some horizon schedule `N_k`. The horizon may grow arbitrarily with `R_k`; no uniform finite bandwidth assumption is required.

## 4. Source visibility and controls

All matrices in (13) are source-only. The global entries of `H^(N)` are inner products of the explicit causal innovations

\[
D_j=(j+1)F_{j+1}-jF_j,
\tag{28}
\]

while `A_R` is the Gram matrix of their explicit Paley--Wiener truncations. No target pairing, best Nyman residual, unknown quotient projector, or off-line zero oracle appears. Numerical use would require certified matrix bounds rather than floating-point eigenvalues alone, but the mathematical certificate itself is exact.

The normalization by `A_R` is essential. A small or well-conditioned **global** Gram matrix does not control continuation cost: the denominator in (1) is the energy visible before `log R`, not the total prefix energy. The generalized eigenvalue in (13) measures exactly how much globally unavoidable norm remains after optimal future cancellation relative to that visible trace.

The unit-outer control gives the required calibration. There

\[
D_j^{(0)}\longleftrightarrow e^{t/2}\mathbf1_{[\log j,\log(j+1)]}(t),
\tag{29}
\]

so the innovations occupy disjoint cells. Therefore `A_R=I`, the prefix/future Gram cross-block vanishes, `S_(R,N)=I`, and

\[
\Xi_{R,N}=1,
\qquad
\Lambda_R=0
\tag{30}
\]

for every `R,N`. The certificate correctly recovers the absence of a flat stable tail.

At the opposite extreme, an ill-conditioned causal family can make `S_(R,N)` much larger than `A_R`; (13) then reports a large extension cost rather than converting finite rank or small off-diagonal entries into a false conclusion. Increasing the future horizon can only improve the certificate, because `S_(R,N)` is monotone decreasing.

## 5. Prior-art boundary and next target

Schur complements, least-squares elimination, generalized Rayleigh quotients, and monotone convergence of distances to increasing closed subspaces are standard Hilbert-space and numerical-linear-algebra tools. No novelty is claimed for those ingredients. Recent Nyman--Beurling Gram work by Werner Ehm (`arXiv:2405.06349`) studies explicit Gram formulae and quadratic-form decompositions, while Hugh Carvill (`arXiv:2510.18132`) studies smoothed Gram decay and block compressibility. A bounded targeted search did not locate the line-specific combination used here: the `NB-062` causal innovation flag identifies the **entire zero-trace kernel** with the future natural span, and its finite future Schur complements decrease to the exact `NB-066` continuation constant, so any bounded finite generalized-eigenvalue subsequence eliminates the stable late quotient. No priority claim is made.

No specialized external theorem is load-bearing for (3)--(30), so `SOURCES.md` remains unchanged.

The next useful estimate is now concrete. One may seek a source-derived horizon `N=N(R)` and a uniform constant `C` for which

\[
S_{R,N(R)}\preceq C^2A_R
\tag{31}
\]

on an unbounded sequence. Analytically, this is a finite block-Gram domination problem. Computationally, it is a certified generalized-eigenvalue problem with monotone improvement as future innovations are added. Failure is also informative: if the smallest achievable finite-horizon certificates grow rapidly with `R`, the growth identifies the exact causal directions that must be controlled before the `NB-066` stable-tail obstruction can be removed.
