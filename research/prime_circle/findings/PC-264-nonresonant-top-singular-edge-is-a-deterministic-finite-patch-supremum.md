# PC-264 — nonresonant top singular edge is a deterministic finite-patch supremum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the leading spectral-edge/outlier channel left open by PC-262/PC-263.

Let

\[
2<p_n<r_n<q_n
\]

be distinct primes with `q_n -> infinity`, and assume

\[
\alpha_n=\frac{p_n}{q_n}\to\alpha,
\qquad
\beta_n=\frac{r_n}{q_n}\to\beta,
\qquad
0<\alpha<\beta<1,
\]

with `1,alpha,beta` linearly independent over `Q`, exactly as in PC-262. For the natively normalized PC-251 shared-upper defect

\[
\Delta_n=\frac{D_{p_n,r_n;q_n}}{q_n\sqrt{p_nr_n}},
\]

there is a deterministic number `Lambda(alpha,beta)` such that

\[
\boxed{
\|\Delta_n\|=\sigma_{\max}(\Delta_n)
\longrightarrow
\Lambda(\alpha,\beta).
}
\tag{1}
\]

Moreover `Lambda(alpha,beta)` is not a genuinely long-cocycle quantity. It is the increasing supremum of operator norms of finite local patches in the induced torus-return hull of PC-258. In particular, for every `L` the finite matrix already satisfies a source-uniform localization estimate

\[
\boxed{
0\le
\|\Delta_n\|-e_{n,L}
\le \frac1L,
}
\tag{2}
\]

where `e_{n,L}` is the largest norm of a compression of the symmetric dilation of `Delta_n` to `L` consecutive collision-coordinate blocks. For fixed `L`, the admissible local patches converge to a compact family determined only by `(alpha,beta)` and the PC-258 Green-weighted return rule. Hence

\[
e_{n,L}\longrightarrow e_L(\alpha,\beta),
\qquad
\Lambda(\alpha,\beta)=\sup_{L\ge1}e_L(\alpha,\beta).
\tag{3}
\]

Thus the **leading `O(1)` top singular edge and any detached top outlier at that scale are sequence-independent in the nonresonant regime**. The same limit is reproduced by admissible pairwise-coprime rational-partition controls with the same limiting ratios. What remains open is strictly finer: subleading edge fluctuations, fine spacing, shifted/discriminant observables, projective/rotation data, and genuinely subadditive long-transfer quantities such as top Lyapunov behavior.

## 1. PC-257 gives an exact uniformly banded self-adjoint realization

Use the normalized collision factorization from PC-251/PC-258,

\[
\Delta_n=-U_nR_nV_n^T,
\qquad
R_n=\operatorname{diag}(\rho_{n,1},\ldots,\rho_{n,k_n}),
\tag{4}
\]

where the collisions are ordered monotonically and

\[
0<\rho_{n,a}\le\frac{\sqrt{\alpha_n\beta_n}}4.
\tag{5}
\]

Introduce the symmetric dilation

\[
\mathscr H_n=
\begin{pmatrix}
0&\Delta_n\\
\Delta_n^T&0
\end{pmatrix}.
\tag{6}
\]

Its nonzero eigenvalues are `+-sigma_j(Delta_n)`, so

\[
\|\mathscr H_n\|=\|\Delta_n\|.
\tag{7}
\]

PC-257 proves that each collision is one weighted `K_{2,2}` tile and that nonconsecutive collision tiles share no vertex. Assign every active row/column vertex the index of the **first** collision tile containing it. A vertex can belong to one tile or to two consecutive tiles only. Consequently, every matrix edge created by tile `a` joins vertices whose assigned indices differ by at most one.

After deleting isolated zero vertices and grouping equal assigned indices, `mathscr H_n` is therefore exactly block tridiagonal,

\[
\mathscr H_n=H_{0,n}+H_{1,n},
\tag{8}
\]

where `H_0,n` contains equal-block entries and `H_1,n` contains the two adjacent-block diagonals. The block dimension is uniformly bounded: one collision tile contains only four graph vertices, so no block can introduce more than four new coordinates. This is a concrete band realization of PC-257's invariant pathwidth-two statement, not a new model imposed on the carrier.

There is also a uniform coefficient bound. Every active vertex belongs to at most two collision tiles, and one tile contributes two incident entries of magnitude `rho_n,a`. Therefore the absolute row sum of `mathscr H_n` is at most

\[
2(\rho_{n,a-1}+\rho_{n,a})
\le \sqrt{\alpha_n\beta_n}<1.
\tag{9}
\]

The same bound holds for the adjacent-block part, so

\[
\boxed{\|H_{1,n}\|\le1.}
\tag{10}
\]

This uses only the native PC-258 normalization and the exact tile incidence geometry.

## 2. A sliding-window identity localizes the operator norm with `1/L` error

Let `P_s^{(L)}` project onto block indices

\[
s,s+1,\ldots,s+L-1,
\]

with the finite chain extended by zero blocks outside its endpoints, and put

\[
e_{n,L}
=\max_s\|P_s^{(L)}\mathscr H_nP_s^{(L)}\|.
\tag{11}
\]

For every vector `x`, each equal-block quadratic-form term is present in exactly `L` sliding windows, while each adjacent-block term is present in exactly `L-1`. Hence the exact counting identity

\[
\sum_s
\langle P_s^{(L)}x,
\mathscr H_nP_s^{(L)}x\rangle
=
L\langle x,\mathscr H_nx\rangle
-
\langle x,H_{1,n}x\rangle
\tag{12}
\]

holds, together with

\[
\sum_s\|P_s^{(L)}x\|^2=L\|x\|^2.
\tag{13}
\]

Choose a unit eigenvector of `mathscr H_n` at the spectral edge and, if necessary, replace `mathscr H_n` by `-mathscr H_n`. Equations (10)--(13) imply that at least one window has Rayleigh quotient at least

\[
\|\mathscr H_n\|-\frac1L.
\]

Since every window compression has norm at most the global norm,

\[
\boxed{
e_{n,L}
\le\|\mathscr H_n\|
\le e_{n,L}+\frac1L.
}
\tag{14}
\]

This is stronger than an appeal to weak spectral convergence. It says directly that the leading spectral edge of every finite Prime-Circle defect can be approximated, with an error independent of `p_n,r_n,q_n`, by a bounded collision window. A leading `O(1)` top outlier therefore cannot require observation depth proportional to the collision rank.

Endpoint windows cause no new spectral carrier. They are compressions of the same finite-return coefficient patterns with one missing exterior coupling, so their norms are bounded by the corresponding two-sided local-hull patches. PC-260's reflection symmetry gives the same conclusion from the opposite endpoint, but reflection is not needed for (14).

## 3. Fixed collision windows converge to a deterministic torus patch family

PC-262 supplies the second ingredient: in the irrational nonresonant limit, successive collisions have a uniform finite raw-return bound. Therefore a window of `L+O(1)` consecutive collision symbols is determined by at most `C_L(alpha,beta)` consecutive raw torus iterates, uniformly for all sufficiently large `n`.

The coefficients of the corresponding block compression are functions of precisely the PC-258 data:

\[
T_{\alpha_n,\beta_n}(x,y)
=(x+\alpha_n,y+\beta_n)\pmod1,
\]

return to

\[
W_{\alpha_n,\beta_n}
=[1-\alpha_n,1)\times[1-\beta_n,1),
\]

and the Green weight

\[
\rho_n(x,y)=
\sqrt{\alpha_n\beta_n}\,
G\!\left(
\frac{1-x}{\alpha_n},
\frac{1-y}{\beta_n}
\right).
\tag{15}
\]

For fixed `L`, only finitely many membership tests in translated rectangle boundaries occur. Away from those finitely many boundary segments, the local matrix entries vary continuously with the starting torus point and with `(alpha_n,beta_n)`; at the boundaries one takes the compact closure of the one-sided realizable patches.

Let `P_L(alpha,beta)` denote this compact closure of two-sided `L`-block compression matrices, padded by zero coordinates when a combinatorial branch uses fewer active vertices. Define

\[
\boxed{
e_L(\alpha,\beta)
=\max_{A\in\mathcal P_L(\alpha,\beta)}\|A\|.
}
\tag{16}
\]

PC-262 proves weak convergence of the complete rational orbit measures to Haar measure on `T^2`. Because Haar measure has full support, this also forces the finite orbit supports to become Hausdorff-dense: otherwise a fixed-radius open ball missed by a subsequence would contradict weak convergence. Restricting to the interior of the collision rectangle gives the same density for collision starting points.

This yields both directions needed for local-patch convergence. Every continuity patch in `P_L(alpha,beta)` is realized arbitrarily closely by sufficiently large finite rational orbits, while every convergent sequence of finite `L`-patches has, by compactness and the uniform raw-window bound, a limit in `P_L(alpha,beta)`. Boundary branches are already included by closure. Consequently

\[
\boxed{
e_{n,L}\longrightarrow e_L(\alpha,\beta)
}
\tag{17}
\]

for every fixed `L`, up to endpoint compressions, which cannot exceed the corresponding two-sided hull norm as noted above.

The families extend consistently when `L` grows. Any `L`-block patch is a principal compression of an `(L+1)`-block patch in the two-sided hull, so

\[
e_L(\alpha,\beta)\le e_{L+1}(\alpha,\beta)\le1.
\tag{18}
\]

Thus

\[
\Lambda(\alpha,\beta)
:=\lim_{L\to\infty}e_L(\alpha,\beta)
=\sup_Le_L(\alpha,\beta)
\tag{19}
\]

exists.

## 4. The finite Prime-Circle edge converges to the local-hull supremum

For every fixed `L`, (14) and (17) give

\[
\liminf_{n\to\infty}\|\Delta_n\|
\ge e_L(\alpha,\beta).
\tag{20}
\]

Taking the supremum over `L` yields

\[
\liminf_n\|\Delta_n\|
\ge\Lambda(\alpha,\beta).
\tag{21}
\]

Conversely, using (14) and then (17),

\[
\limsup_{n\to\infty}\|\Delta_n\|
\le e_L(\alpha,\beta)+\frac1L
\tag{22}
\]

for every fixed `L`. Letting `L->infinity` and using (19) gives

\[
\limsup_n\|\Delta_n\|
\le\Lambda(\alpha,\beta).
\tag{23}
\]

Equations (21)--(23) prove (1).

The conceptual point is stronger than mere existence of a numerical limit. PC-257 left the complete finite spectrum as a growing transfer product; PC-262 then classicalized its bulk distribution but explicitly left extreme singular values open. The top singular edge is now seen to sit on the **local** side of that boundary: its leading value is exhausted by bounded patches of the same induced torus hull. No matrix product of length `Theta(k_n)` is needed to determine the `O(1)` limit.

## 5. Matched controls and RH-facing consequence

Nothing in Sections 1--4 uses primality after the PC-251 rational-partition carrier has been formed. The proof uses pairwise coprimality, monotone collision tiles, the Green weight, the limiting ratios, and nonresonant torus equidistribution. The admissible pairwise-coprime nonprime controls already used in PC-251/PC-262 therefore have the same compact local patch family `P_L(alpha,beta)` and the same limit `Lambda(alpha,beta)`.

Hence a proposed Prime-Circle/RH mechanism based only on

- the largest normalized singular value;
- the leading spectral radius of the symmetric dilation;
- existence or location of a detached top eigenvalue at `O(1)` scale; or
- any criterion depending only on the limiting top edge,

cannot distinguish the prime source from its matched rational-partition control in this nonresonant regime.

This does **not** prove that all edge information is classical. Quantities such as

\[
q_n^\gamma\bigl(\sigma_{\max}(\Delta_n)-\Lambda(\alpha,\beta)\bigr)
\]

may depend on Diophantine approach rates or rare near-resonances; (1) supplies no universal fluctuation scale. Nor does the local-norm argument determine fine spacing near the edge, shifted characteristic determinants, transfer rotation/winding, or the top Lyapunov exponent of a source-forced projective cocycle. Rationally dependent limiting ratios remain excluded exactly as in PC-262/PC-263, and PC-261 shows that such resonant limits can carry `O(1)` sequence dependence.

The surviving nonresonant long-cocycle question is therefore narrower: a successful invariant must be genuinely global/subadditive or live in subleading fluctuation data. **The leading operator norm is no longer such an invariant.**

## 6. Prior-art and novelty audit

Localization of spectra and operator quantities for finite-range/band operators from finite subwords or local patches is classical operator theory, not a new Prime-Circle mechanism. Particularly close anchors are:

- Raffael Hagger, Marko Lindner and Markus Seidel, **Essential pseudospectra and essential norms of band-dominated operators**, *Journal of Mathematical Analysis and Applications* 437 (2016), 255--291, DOI `10.1016/j.jmaa.2015.11.060`. This contains general norm/limit-operator localization machinery for band-dominated operators.
- Fabian Gabel, Dennis Gallaun, Julian Grossmann, Marko Lindner and Riko Ukena, **Spectral Approximation of Generalized Schrödinger Operators via Approximation of Subwords**, *Complex Analysis and Operator Theory* 18 (2024), article 7, DOI `10.1007/s11785-023-01448-3`. Their framework makes finite subwords/localized norms determine spectral and pseudospectral approximation for band operators and explicitly points to operator-norm localization as established prior art.
- Paul Hege, Massimo Moscolari and Stefan Teufel, **Computing the spectrum and pseudospectrum of infinite-volume operators from local patches**, *Mathematics of Computation*, DOI `10.1090/mcom/4075` (published online 2025; arXiv:`2403.19055`). This gives two-sided spectral approximation for normal short-range operators from finite local patches.

No novelty is claimed for band-operator norm localization, local-patch spectral approximation, compact hulls, or recurrence of irrational torus translations. The project-local result is the exact verification that the PC-251/PC-257 **source-forced normalized collision operator satisfies those hypotheses with a uniform `1/L` localization bound**, and that PC-262's nonresonant rational approximants converge to one deterministic induced-torus patch hull. That combination closes one explicit Prime-Circle frontier left open by the preceding findings.

The novelty audit also rules out interpreting `Lambda(alpha,beta)` as a new zeta spectral quantity merely because it originates from roots-of-unity overlap packets. At this stage it is a norm of a classical finite-range hull generated by rational mechanical words and the Green kernel. No complex `s`, zeta functional equation, critical-line involution, explicit-formula term, or zero detector is produced.

## 7. Falsification and boundary audit

The claim has several direct failure tests.

1. **Band failure:** exhibit a PC-251 collision matrix in which, under the first-tile coordinate assignment, a nonzero entry couples blocks at distance greater than one. This would contradict the monotone-tile incidence argument from PC-257.
2. **Localization failure:** find `n,L` for which `||Delta_n||>e_n,L+1/L`. Equations (12)--(14) reduce this to an exact finite quadratic-form count and the row-sum bound (10).
3. **Patch noncompactness:** for fixed `L`, construct local collision windows requiring unbounded raw return depth along a sequence satisfying the PC-262 rational-independence limit. This would contradict the robust syndetic-return theorem already used in PC-262.
4. **Sequence dependence:** produce two prime sequences with the same rationally independent limiting `(alpha,beta)` for which `||Delta_n||` has different limits. By (14), this would force a difference in some fixed finite-patch supremum and hence falsify the torus patch-convergence step.
5. **Matched-control separation:** construct an admissible pairwise-coprime rational-partition control with the same limiting ratios and local Green-return rule but a different limiting top norm.

The theorem makes no assertion at rationally dependent limiting ratios, under resonance approach without the PC-262 hypothesis, or about a universal convergence rate. It also does not identify the complete Hausdorff limit of the finite spectra; ordinary finite-section spectral pollution and boundary states make that a stronger question than the operator-norm edge treated here.