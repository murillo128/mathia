# NB-026 — disjoint adjacent cancellations force a macroscopic target-poor low-Rayleigh sector

**Status:** `EXACT-DERIVED + MACROSCOPIC-LOW-RAYLEIGH-SECTOR + TARGET-POOR-RITZ-SECTOR + UNIVERSAL-DICTIONARY-CONTROL + NEGATIVE/METHOD-BOUNDARY`. `NB-025` exhibits one explicit adjacent-index cancellation whose normalized-Gram Rayleigh quotient is `O(log N/N)` and whose canonical target loading vanishes. That phenomenon is not confined to one exceptional bad direction. By packing disjoint adjacent pairs into the upper half of the canonical dictionary and then using only compression, trace, and min-max, one obtains a **linear-dimensional** coefficient subspace on which the normalized Gram form is uniformly `O(log N/N)` while the target functional is uniformly `O(log N/N)` in Euclidean coefficient norm.

Let

\[
\phi_n:=\frac{g_n}{\|g_n\|},\qquad
\widetilde G_N=(\langle\phi_j,\phi_k\rangle)_{2\le j,k\le N},
\qquad
\widetilde b_N=(\langle e,\phi_k\rangle)_{2\le k\le N},
\tag{1}
\]

and for `2<=n<N` let `beta^(n)` be the two-coordinate vector from `NB-025`,

\[
\beta_n^{(n)}=\|g_n\|,\qquad
\beta_{n+1}^{(n)}=-\|g_{n+1}\|,
\qquad
u_n:=\frac{\beta^{(n)}}{\|\beta^{(n)}\|_2}.
\tag{2}
\]

Its Hilbert image is `g_n-g_(n+1)`. Define the disjoint upper-half packing

\[
J_N:=\{a_N,a_N+2,a_N+4,\ldots\}\cap[2,N-1],
\qquad a_N:=\lceil N/2\rceil,
\tag{3}
\]

and put

\[
k_N:=|J_N|,\qquad
m_N:=\lfloor k_N/2\rfloor.
\tag{4}
\]

For `N>=8`,

\[
k_N\ge\frac{N-3}{4},
\qquad
m_N\ge\frac{N-7}{8}.
\tag{5}
\]

Then there exists a subspace

\[
L_N\subset\mathbb R^{N-1},\qquad \dim L_N=m_N,
\tag{6}
\]

such that every `v in L_N` satisfies simultaneously

\[
\boxed{
 v^*\widetilde G_Nv
 \le
 \frac{16(H_N+2)}{N}\,\|v\|_2^2
}
\tag{7}
\]

and

\[
\boxed{
 |\widetilde b_N^*v|
 \le
 \frac{4\log(N+1)}{N}\,\|v\|_2.
}
\tag{8}
\]

In particular, if the eigenvalues of `widetilde G_N` are ordered increasingly, then

\[
\boxed{
\lambda_{m_N}(\widetilde G_N)
\le
\frac{16(H_N+2)}{N}
=O\!\left(\frac{\log N}{N}\right).
}
\tag{9}
\]

Thus a positive proportion of the normalized canonical Gram spectrum is forced below the adjacent-cancellation scale. This is unconditional and independent of the Nyman distance, RH, Möbius locking, or the optimal approximation coefficients.

There is also a useful deflation consequence. If `W_N` is any coefficient subspace of codimension `r_N<m_N`, then

\[
\dim(W_N\cap L_N)\ge m_N-r_N>0.
\tag{10}
\]

Hence `W_N` still contains a nonzero vector obeying both (7) and (8). In particular, **discarding only `o(N)` coefficient directions cannot remove all of this universal low-Rayleigh, target-poor sector.** This statement concerns linear elimination/deflation in the canonical normalized coefficient coordinates; it is not invariant under an arbitrary invertible change of basis.

## 1. Disjoint adjacent pairs give an orthonormal nuisance family

For each `n in J_N`, the support of `u_n` is exactly `{n,n+1}`. Distinct indices in `J_N` differ by at least two, so these supports are disjoint. Therefore

\[
\langle u_n,u_{n'}\rangle_{\ell^2}=0
\qquad(n\ne n'),
\tag{11}
\]

and the family `{u_n:n in J_N}` is orthonormal in coefficient space. Let

\[
U_N:=\operatorname{span}\{u_n:n\in J_N\}.
\tag{12}
\]

Then `dim U_N=k_N`.

The counting bound (5) is elementary. The interval `[ceil(N/2),N-1]` has at least `(N-1)/2` integers, and selecting every second one gives `k_N>=(N-3)/4`. Taking the integer half once more gives `m_N>=(N-7)/8`.

`NB-025` proves for every `n+1<=N`

\[
u_n^*\widetilde G_Nu_n
\le\frac{4(H_n+2)}{n}.
\tag{13}
\]

For `n in J_N`, one has `n>=N/2` and `H_n<=H_N`, hence

\[
\boxed{
q_n:=u_n^*\widetilde G_Nu_n
\le Q_N:=\frac{8(H_N+2)}{N}.
}
\tag{14}
\]

The point of using disjoint pairs is that no estimate of the off-diagonal Gram interactions between different adjacent cancellations is required. Their coefficient supports give an orthonormal basis of `U_N`, so the diagonal Rayleigh estimates already control the trace of the compression.

## 2. Compression trace forces a linear-dimensional low-Rayleigh subspace

Let

\[
C_N:=P_{U_N}\widetilde G_N|_{U_N}
\tag{15}
\]

be the positive compression of the normalized Gram matrix to `U_N`. Since `{u_n:n in J_N}` is an orthonormal basis of `U_N`, (14) gives

\[
\operatorname{tr}C_N
=\sum_{n\in J_N}q_n
\le k_NQ_N.
\tag{16}
\]

Write the compression eigenvalues increasingly as

\[
0<\mu_1\le\cdots\le\mu_{k_N}.
\tag{17}
\]

For `m_N=floor(k_N/2)`, at least `k_N-m_N+1>=k_N/2` eigenvalues are at least `mu_(m_N)`. Consequently

\[
\frac{k_N}{2}\mu_{m_N}
\le\operatorname{tr}C_N
\le k_NQ_N,
\]

so

\[
\boxed{
\mu_{m_N}
\le2Q_N
=\frac{16(H_N+2)}{N}.
}
\tag{18}
\]

Let `L_N` be the span of the first `m_N` compression eigenvectors. For every `v in L_N`, because `v in U_N`,

\[
v^*\widetilde G_Nv
=v^*C_Nv
\le\mu_{m_N}\|v\|_2^2,
\tag{19}
\]

which proves (7). The Courant--Fischer min-max principle applied to the `m_N`-dimensional trial space `L_N` gives (9).

This is strictly stronger than the single-vector conclusion of `NB-025`: the universal adjacent mechanism forces not merely `lambda_min=O(log N/N)`, but at least `m_N>= (N-7)/8` eigenvalues below a constant multiple of that scale.

## 3. The entire Ritz sector is coefficient-target-poor

The second input from `NB-025` is the exact target-pairing estimate

\[
|\widetilde b_N^*u_n|
\le
\frac{2\log(n+1)}{n^{3/2}}.
\tag{20}
\]

Since the `u_n` are orthonormal, Bessel's identity on `U_N` gives

\[
\|P_{U_N}\widetilde b_N\|_2^2
=
\sum_{n\in J_N}|\widetilde b_N^*u_n|^2.
\tag{21}
\]

For `n in J_N`, `n>=N/2`, so each summand is at most

\[
\frac{32\log^2(N+1)}{N^3}.
\tag{22}
\]

Using the crude but sufficient `k_N<=N/2`,

\[
\boxed{
\|P_{U_N}\widetilde b_N\|_2
\le\frac{4\log(N+1)}{N}.
}
\tag{23}
\]

Because `L_N subset U_N`, every `v in L_N` therefore satisfies

\[
|\widetilde b_N^*v|
=|(P_{U_N}\widetilde b_N)^*v|
\le\frac{4\log(N+1)}{N}\|v\|_2,
\]

which is (8).

The norm in (8) is deliberately the **Euclidean coefficient norm**. It does not imply that every vector in `L_N`, after Hilbert normalization of its image, has vanishing target angle: the Gram norm of a vector in `L_N` may be much smaller than the upper bound (7). The correct statement is that the target functional itself has vanishing operator norm on this macroscopic low-Rayleigh coefficient sector.

## 4. Low-rank deflation cannot purge the universal sector

Let `W_N` have codimension `r_N<m_N`. The dimension inequality

\[
\dim(W_N\cap L_N)
\ge\dim W_N+\dim L_N-(N-1)
=m_N-r_N
\tag{24}
\]

proves (10). Any nonzero vector in the intersection retains (7) and (8).

Therefore a spectral strategy that tries to interpret weak canonical Gram modes by first deleting a fixed number, or more generally `o(N)`, of nuisance coefficient directions cannot eliminate the whole adjacent-cancellation mechanism. At the `O(log N/N)` Rayleigh scale, the nuisance space is extensive. A successful separation has to use additional structure—target loading, arithmetic coefficient locking, a multiscale transform, or another source-specific invariant—not merely a finite-rank cleanup of the smallest modes.

This corollary does **not** cover arbitrary invertible preconditioning. Such a change of coordinates can alter the normalized Gram spectrum completely, just as an orthonormal basis of the span has identity Gram matrix. It only rules out low-rank elimination as a way of making the canonical normalized spectrum itself source-specific.

## 5. Prior-art boundary and adversarial controls

The local adjacent-generator regularity underlying `NB-025` sits inside the classical multiplicative autocorrelation literature for the fractional-part function. Báez-Duarte--Balazard--Landreau--Saias (`arXiv:math/0306251`) study that autocorrelation directly, Balazard--Martin (`arXiv:1305.4395`) analyze its local regularity, and Werner Ehm (`arXiv:2405.06349`) derives modern Nyman--Beurling Gram formulae and quadratic-form decompositions. Hugh Carvill (`arXiv:2510.18132`) studies a different multiplicative-ladder parameterization and obtains Gram block-compressibility after Mellin smoothing.

A targeted search of those Gram/autocorrelation directions did not locate the finite-section statement (6)--(9), namely that disjoint adjacent differences in the **canonical integer dictionary after individual norm normalization** force a linear-dimensional low-Rayleigh sector together with the target-functional bound (8). Search absence is not a priority claim. No specialized external theorem is load-bearing here: the proof uses only `NB-025` plus elementary finite-dimensional linear algebra, so `SOURCES.md` does not require a new dependency.

Several controls are load-bearing. First, (9) is only an upper bound on the `m_N`-th eigenvalue; it does not identify an asymptotic spectral distribution. Second, although `L_N` is target-poor in the precise sense (8), the individual global eigenvectors below the threshold in (9) need not lie in `L_N` and do not automatically inherit (8). Third, the result is universal dictionary geometry and gives neither an upper nor a lower bound on `d_N`. Fourth, the construction is coordinate-sensitive and does not contradict the possibility that a substantially different arithmetic basis exposes better conditioning. Finally, `L_N` is obtained from the compression eigenvectors inside the explicit disjoint-pair span; it is an exact existence construction, not an assertion that the original adjacent vectors are mutually Gram-orthogonal.

## 6. Consequence for the target-selected spectral route

`NB-024` shows that good Nyman approximation forces the actual normalized least-squares coefficient vector to carry large Euclidean mass in a low spectral sector. `NB-025` warns that one universal adjacent cancellation already makes raw condition-number growth non-diagnostic. The present result strengthens that warning substantially: **a linear fraction of the coefficient dimensions is already available to universal, target-poor low-Rayleigh geometry at scale `O(log N/N)`.**

Thus the next useful spectral theorem cannot merely count small eigenvalues, prove a growing condition number, or deflate finitely many visibly smooth adjacent modes. It must measure what is source-specific about the target-selected weak directions. One viable formulation would compare the Möbius-locked coefficient vector from `NB-020`/`NB-024` against the entire macroscopic nuisance space `U_N` or a sharper universal closure of adjacent smooth-index differences, and prove that a quantitatively significant part of its weak-mode mass survives outside that control. Another is to construct a target-weighted or source-weighted generalized spectral quantity whose coercive part vanishes on this universal sector but remains linked to the section-enrichment budget of `NB-015`--`NB-017`.

What this finding rules out is narrower but exact: **small canonical Gram eigenvalues are not a sparse nuisance phenomenon.** Any RH-facing spectral mechanism must separate target-loaded arithmetic weakness from a macroscopic background of source-independent finite-difference weakness.