# PC-390 — primorial boundary Laplacian transport is next-prime-gap degree shedding

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the graph-Laplacian and one-vertex Kron variants left open by PC-389 in the prime-only primorial boundary window.

PC-389 showed that, for a fixed pairwise kernel matrix on a polynomial boundary window `H=x^u`, `1<u<2`, adjoining the next prime deletes exactly one boundary vertex and the new kernel matrix is asymptotically the corresponding principal minor. Graph Laplacians do **not** obey that principal-minor law: deleting the vertex also removes its incident weights from every surviving degree. For the regularized inverse-power chord kernel this discrepancy is exact up to the exponentially small conductor change, and its operator norm is asymptotically a strictly monotone function of the **next consecutive prime gap**.

Thus the Laplacian escape from PC-389 is real but classicalized. It retains more arithmetic than the raw pairwise matrix transport, yet the extra signal is precisely the deleted prime's incident star, already determined by the rough-number support. Kron elimination turns that same one-vector star into a full-rank nonlocal mesh, but does not create an independent carrier.

## 1. Prime-only successive primorial setup

Let `p_n<p_{n+1}<p_{n+2}` be consecutive primes and write

\[
p:=p_n,\qquad q:=p_{n+1},\qquad r:=p_{n+2},\qquad
N:=\prod_{\ell\le p}\ell .
\tag{1}
\]

Fix `1<u<2` and put `H=p^u`. For all sufficiently large `p`,

\[
r<H<q^2.
\tag{2}
\]

The first inequality follows, for example, from Bertrand's postulate and `p^{u-1}->infinity`; the second follows from `q~p`. By PC-388/PC-389 the old and new primitive boundary supports are therefore exactly

\[
R=\{1\}\cup\{s:p<s\le H,\ s\text{ prime}\},
\qquad
R^+=R\setminus\{q\}.
\tag{3}
\]

For fixed `alpha>0` and `tau>=0`, use the normalized regularized inverse-chord kernel

\[
\kappa_M(d)
:=M^{-2\alpha}
\left[2\left(\cosh\frac{\tau}{M}
-\cos\frac{2\pi d}{M}\right)\right]^{-\alpha},
\qquad d\ne0.
\tag{4}
\]

For a finite set `S` of exponent coordinates, let `L_M[S]` be the weighted graph Laplacian with off-diagonal entries

\[
(L_M[S])_{a,b}=-\kappa_M(a-b),\qquad a\ne b,
\tag{5}
\]

and diagonal equal to the sum of the incident weights inside `S`.

Define

\[
A:=L_N[R],
\qquad
A^+:=L_{qN}[R^+],
\tag{6}
\]

and let `C` be the principal submatrix of `A` obtained by deleting the coordinate `q`.

## 2. Vertex deletion produces an exact diagonal degree-shedding term

For `a in R^+` put

\[
w_a:=\kappa_N(a-q),
\qquad
D:=\operatorname{diag}(w_a)_{a\in R^+}.
\tag{7}
\]

The same-conductor induced Laplacian on the surviving set is not the principal minor `C`. The latter still contains, in every surviving diagonal entry, the edge weight that used to connect that vertex to `q`. Hence the exact identity

\[
\boxed{
L_N[R^+]=C-D.
}
\tag{8}
\]

This is the elementary graph-Laplacian vertex-deletion correction, but it matters here because `D` need not be small even though only one support point disappeared.

The change from conductor `N` to `qN` is negligible on the polynomial boundary window. Uniformly for `1<=|d|<=H`,

\[
\kappa_N(d)
=(\tau^2+4\pi^2d^2)^{-\alpha}
\left(1+O\!\left(\frac{1+d^2}{N^2}\right)\right),
\tag{9}
\]

and the same expansion holds with `N` replaced by `qN`. Therefore the absolute row sum of the Laplacian difference satisfies

\[
\|L_{qN}[R^+]-L_N[R^+]\|_{\rm op}
\le
O\!\left(
\frac1{N^2}
\sum_{1\le d\le H}
(1+d^2)(\tau^2+4\pi^2d^2)^{-\alpha}
\right)
=o(1),
\tag{10}
\]

because `H` is polynomial in `p` while `N=\exp((1+o(1))p)` by the prime number theorem. Combining (8)--(10),

\[
\boxed{
A^+=C-D+o_{\rm op}(1).
}
\tag{11}
\]

Thus PC-389's principal-minor transport fails for the graph Laplacian by exactly the incident-degree profile of the deleted prime.

## 3. The operator-norm defect is the next consecutive prime gap

Let

\[
g:=r-q=p_{n+2}-p_{n+1}.
\tag{12}
\]

On the present window, `r` is the nearest surviving prime to the right of `q`; there is no surviving prime to its left, and the only left-hand point is the anchor `1`. Bertrand's postulate gives `g<q`, so the nearest surviving exponent distance is `g` (up to a harmless possible tie with the anchor). Since `kappa_N(d)` is positive and strictly decreasing for `1<=d<N/2`,

\[
\|D\|_{\rm op}=\kappa_N(g).
\tag{13}
\]

Using (9) and the reverse triangle inequality in (11) gives the sharp transport law

\[
\boxed{
\|A^+-C\|_{\rm op}
=
(\tau^2+4\pi^2g^2)^{-\alpha}+o(1).
}
\tag{14}
\]

The error tends to zero uniformly along the primorial sequence. Consequently this cross-level Laplacian defect is, asymptotically, an invertible monotone encoding of the next consecutive prime gap.

This immediately rules out a universal operator-norm principal-minor limit. Maynard proved unconditionally that

\[
\liminf_m(p_{m+1}-p_m)\le600,
\tag{15}
\]

so along an infinite subsequence

\[
\limsup_n\|A^+-C\|_{\rm op}
\ge
(\tau^2+4\pi^2\,600^2)^{-\alpha}>0.
\tag{16}
\]

On the other hand, classical large-gap results, in particular Ford--Green--Konyagin--Tao, give consecutive prime gaps tending to infinity along another subsequence. Hence

\[
\boxed{
\liminf_n\|A^+-C\|_{\rm op}=0,
\qquad
\limsup_n\|A^+-C\|_{\rm op}>0.
}
\tag{17}
\]

The Laplacian transport therefore genuinely oscillates with prime-gap extremes rather than converging to the PC-389 compression law.

## 4. Kron elimination makes the same star nonlocal but adds no new carrier

One might try to preserve the deleted vertex harmonically rather than simply remove it. Order `A` as `R^+ sqcup {q}` and let

\[
w=(w_a)_{a\in R^+},
\qquad
s=\sum_{a\in R^+}w_a.
\tag{18}
\]

Then the exact block form is

\[
A=
\begin{pmatrix}
L_N[R^+]+D&-w\\
-w^*&s
\end{pmatrix}.
\tag{19}
\]

The Kron/Schur elimination of `q` is therefore

\[
\operatorname{Kron}_q(A)
=L_N[R^+]+M_q,
\qquad
\boxed{
M_q:=D-\frac{ww^*}{s}.
}
\tag{20}
\]

Equivalently,

\[
\langle f,M_qf\rangle
=
\frac1{2s}
\sum_{a,b\in R^+}w_aw_b|f_a-f_b|^2.
\tag{21}
\]

Thus `M_q` is exactly the classical star-mesh transform of the incident star at `q`. It is positive semidefinite, has kernel spanned by the constant vector, and because every chord weight is positive it has rank

\[
\boxed{
\operatorname{rank}M_q=|R^+|-1.
}
\tag{22}
\]

So the nonlocal response is **not** low rank: eliminating one vertex produces a complete weighted mesh that is full rank on the mean-zero subspace. But its apparent nonlocal complexity is entirely determined by the single incident-weight vector `w`.

Even a nonlinear spectral invariant makes this explicit. If `m=|R^+|`, the weighted matrix-tree identity for the complete mesh with conductances `w_aw_b/s` gives

\[
\boxed{
\operatorname{pdet}M_q
=
\frac{m}{s}\prod_{a\in R^+}w_a.
}
\tag{23}
\]

The same formula follows directly from the determinant lemma applied to `D-ww^*/s`. Thus the full-rank Kron mesh, its pseudodeterminant, and its spectrum are functions only of the deleted prime's incident chord profile. In the prime-only boundary zone that profile is itself a deterministic transform of the already-selected prime support and its gaps.

Combining (10) and (20),

\[
\operatorname{Kron}_q(A)-A^+
=M_q+o_{\rm op}(1).
\tag{24}
\]

Kron reduction therefore preserves the degree-shedding information rather than erasing it, but does not manufacture a second independent arithmetic structure.

## 5. Prior-art and novelty audit

The graph-theoretic mechanism in (20) is classical. Dörfler and Bullo treat Kron reduction of weighted graph Laplacians as Schur complementation and its electrical-network interpretation; the one-vertex case is precisely the star-mesh transform. That source is already a standing prime-circle literature anchor from PC-039/PC-162.

The two number-theoretic inputs controlling the subsequences in (17) are also classical results: James Maynard, **Small gaps between primes**, *Annals of Mathematics* 181 (2015), 383--413, DOI `10.4007/annals.2015.181.1.7`, proves in particular `liminf (p_{n+1}-p_n)<=600`; Kevin Ford, Ben Green, Sergei Konyagin and Terence Tao, **Large gaps between consecutive prime numbers**, *Annals of Mathematics* 183 (2016), 935--974, DOI `10.4007/annals.2016.183.3.4`, prove consecutive gaps with a lower bound tending to infinity.

I did not locate prior art phrasing the specific prime-circle identity (14), but its content is a transparent composition of the classical primorial-wheel support from PC-388/PC-389, elementary Laplacian vertex deletion, the local Euclidean chord limit, and established prime-gap theorems. It is therefore not a new prime-gap theorem or a new spectral route to zeta. The line-specific contribution is the exact diagnosis of what survives when PC-389's cross-level transport is upgraded from a pairwise kernel matrix to the canonical graph Laplacian/Kron response.

## 6. RH-facing boundary and falsification

Equation (14) is important precisely because it prevents a false negative: graph-Laplacian transport does **not** collapse to the same asymptotic principal-minor interlacing law as the raw kernel matrix. It can retain order-one arithmetic fluctuations. However those fluctuations are already the consecutive prime gaps selected by the primitive support. Any bound on `g` can be translated through the monotone function in (14) into a bound on the transport defect, and conversely. Without an independent geometric estimate on that defect, this is a re-encoding of classical prime-gap information rather than a mechanism that constrains zeta zeros.

The result is deliberately limited to the positive monotone regularized inverse-power chord kernel, primorial cutoffs, and the prime-only window `1<u<2`. It does not classify sign-changing kernels, windows `H>=q^2` where Buchstab deletes many vertices at once, nonlinear multi-step elimination histories, or operators that retain phases beyond the scalar incident weights.

The decisive finite audit is straightforward. For any sufficiently large consecutive triple `p<q<r`, build `R` from (3), form `A`, delete the `q` row/column to obtain `C`, and independently build `L_N[R^+]`. Their difference must be exactly `D` from (7). The largest entry of `D` must occur at `r` and equal `kappa_N(r-q)`. The one-vertex Schur complement must then differ from `L_N[R^+]` by (20), with one zero eigenvalue and pseudodeterminant (23). Any violation falsifies the finding.

## Consequence for the research line

PC-389's one-vertex Buchstab deletion had left graph-Laplacian and Schur/Kron responses open because their degree bookkeeping is not a principal-submatrix operation. PC-390 resolves that boundary sharply. The Laplacian does preserve extra cross-level arithmetic, but exactly as the deleted prime's incident star; its strongest operator-norm signal is the next consecutive prime gap, and its canonical nonlocal Kron completion is the classical star-mesh transform of the same vector.

Future work should therefore not treat Laplacian nonconvergence or Kron fill-in by itself as evidence of a new RH mechanism. A surviving construction would need an interaction among several Buchstab deletions, phases, changing state spaces, or another source-forced structure that cannot be reconstructed from the sequence of incident support-gap vectors alone.