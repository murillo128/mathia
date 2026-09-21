# PC-391 — multi-deletion Kron interaction is a vanishing-rank contrast correction

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the higher-boundary linear Kron/Laplacian branch left open by PC-390.

PC-390 classified the first Buchstab/primorial boundary step in the window `H<q^2`, where adjoining the next prime `q` deletes exactly one old boundary point. The remaining natural question is whether, once `H>=q^2` and several points are deleted at the same sieve step, their mutual couplings create a genuinely higher-dimensional spectral carrier that is not reducible to the one-vertex star responses.

For weighted graph Laplacians the answer can be made exact. If `k` vertices are eliminated simultaneously, the full Kron response decomposes into the sum of the `k` independent one-vertex star-mesh responses plus a positive semidefinite correction whose rank is bounded by the rank of the Laplacian induced on the deleted vertices. For the positive complete chord kernels used in the prime-circle boundary model this gives rank at most `k-1`. In the first nontrivial case `k=2`, the entire irreducible interaction is exactly one outer product measuring the contrast between the two normalized incident profiles.

On every fixed polynomial primorial window `H=p^u`, `u>1`, the number of deleted points satisfies `k<=H/q` while the surviving boundary already contains `~H/log H` primes. Hence the irreducible multi-deletion correction has relative rank `O(log p/p)->0`. It therefore cannot change the limiting empirical bulk spectrum relative to the superposition of the one-vertex responses. This does **not** rule out outlier, determinant, or exceptional-mode effects, and it does not say that the full Kron response is low rank.

## 1. Exact multi-deletion block decomposition

Let `S` be the surviving boundary vertices and let

\[
T=\{t_1,\ldots,t_k\}
\tag{1}
\]

be the vertices deleted at one sieve/refinement step. Consider any positive weighted graph Laplacian on `S sqcup T`. Write

\[
B_{ai}=b_{ai}>0,
\qquad a\in S,\quad t_i\in T,
\tag{2}
\]

for the boundary-to-deleted conductances, let

\[
d_i:=\sum_{a\in S}b_{ai},
\qquad
D:=\operatorname{diag}(d_1,\ldots,d_k),
\tag{3}
\]

and let `K` be the weighted graph Laplacian of the edges internal to `T`. If `L_S` denotes the Laplacian of the edges internal to `S`, then the full Laplacian has the exact block form

\[
L=
\begin{pmatrix}
L_S+\operatorname{diag}(B\mathbf 1)&-B\\
-B^\top&D+K
\end{pmatrix}.
\tag{4}
\]

Kron reduction of all deleted vertices gives

\[
L_{\rm red}
=
L_S+\operatorname{diag}(B\mathbf1)
-B(D+K)^{-1}B^\top.
\tag{5}
\]

Now remove only the internal couplings among the deleted vertices, i.e. set `K=0` while keeping every boundary incidence vector fixed. The resulting response is

\[
\begin{aligned}
L_{\rm ind}
&=L_S+\operatorname{diag}(B\mathbf1)-BD^{-1}B^\top\\
&=L_S+
\sum_{i=1}^k
\left[
\operatorname{diag}(b_i)
-\frac{b_i b_i^\top}{d_i}
\right],
\end{aligned}
\tag{6}
\]

where `b_i` is the `i`th column of `B`. Thus `L_ind` is exactly the superposition, on the common surviving boundary, of the one-interior-vertex star-mesh responses already exposed in PC-390.

The part that cannot be reconstructed from that independent superposition is therefore

\[
\boxed{
\Delta_T
:=L_{\rm red}-L_{\rm ind}
=B\left[D^{-1}-(D+K)^{-1}\right]B^\top.
}
\tag{7}
\]

This isolates the genuine higher-boundary interaction: it vanishes identically when there is only one deleted vertex or when the deleted vertices have no mutual edges.

## 2. The irreducible interaction lives only on deleted-vertex contrast modes

Set

\[
A:=D^{-1/2}KD^{-1/2}\succeq0.
\tag{8}
\]

Then (7) becomes

\[
\boxed{
\Delta_T
=BD^{-1/2}
\left[I-(I+A)^{-1}\right]
D^{-1/2}B^\top
=BD^{-1/2}A(I+A)^{-1}D^{-1/2}B^\top.
}
\tag{9}
\]

Because `A(I+A)^{-1}` is positive semidefinite and has the same kernel and rank as `A`,

\[
\boxed{
\Delta_T\succeq0,
\qquad
\operatorname{rank}\Delta_T\le\operatorname{rank}K.
}
\tag{10}
\]

If the graph induced on `T` has `c_T` connected components, the standard Laplacian rank formula gives

\[
\operatorname{rank}K=k-c_T,
\tag{11}
\]

and hence

\[
\boxed{
\operatorname{rank}\Delta_T\le k-c_T.
}
\tag{12}
\]

For the regularized inverse-power chord conductances of PC-390 every distinct pair has positive conductance. Thus, for `k>=2`, the deleted graph is complete and connected and

\[
\boxed{
\operatorname{rank}\Delta_T\le k-1.
}
\tag{13}
\]

The missing direction is not accidental. Since `K\mathbf1=0`, the normalized common mode `D^{1/2}\mathbf1` lies in the kernel of `A`; only relative or contrast modes among the deleted vertices can generate interaction beyond the independent stars.

This is deliberately a statement about **the correction (7)**, not about the full response. Each individual star term in (6) can itself have rank `|S|-1`, exactly as PC-390 emphasized. Thus (13) does not repeat the overbroad low-rank inference corrected by PC-047.

## 3. Two deleted vertices give one exact contrast outer product

The first genuinely higher-boundary case is already completely explicit. Let `T={u,v}`. Write `x,y` for the two boundary incidence vectors,

\[
X:=\mathbf1^\top x,
\qquad
Y:=\mathbf1^\top y,
\tag{14}
\]

and let `c>0` be the conductance between `u` and `v`. Then

\[
D+K=
\begin{pmatrix}
X+c&-c\\
-c&Y+c
\end{pmatrix},
\qquad
\delta:=XY+c(X+Y).
\tag{15}
\]

A direct inversion in (7) gives

\[
\boxed{
\Delta_{\{u,v\}}
=
\frac{c}{\delta XY}
(Yx-Xy)(Yx-Xy)^\top
=
\frac{cXY}{\delta}
\left(\frac{x}{X}-\frac{y}{Y}\right)
\left(\frac{x}{X}-\frac{y}{Y}\right)^\top.
}
\tag{16}
\]

So the first multi-deletion correction is not a free two-dimensional matrix datum. It is a single rank-one contrast between the **normalized incident profiles** of the two deleted vertices. It vanishes exactly when

\[
\frac{x}{X}=\frac{y}{Y},
\tag{17}
\]

even if the deleted vertices are strongly coupled internally.

Equation (16) is also a useful falsification control for any proposed two-deletion spectral mechanism: any claimed extra information in a linear Kron response must survive after quotienting out the independent star responses and must then be visible in this one contrast direction.

## 4. Primorial/Buchstab deletion count makes the contrast sector asymptotically thin

Let

\[
P_p:=\prod_{\ell\le p}\ell,
\qquad
R_p(H):=\{1\le m\le H:(m,P_p)=1\},
\tag{18}
\]

and let `q` be the next prime after `p`. Passing from `P_p` to `qP_p` removes exactly the old `p`-rough points divisible by `q`, namely

\[
T=q\,R_p(H/q).
\tag{19}
\]

Therefore

\[
k:=|T|=|R_p(H/q)|\le\frac Hq.
\tag{20}
\]

When `H<q^2`, (19) reduces to `T={q}`, recovering the one-deletion regime of PC-390 and `\Delta_T=0`. Once `H>=q^2`, multiple deletion is possible and (9)--(13) describe the genuinely new interaction.

The surviving set is `S=R_q(H)`. Independently of its composite elements, it contains the anchor `1` and every prime `r` with `q<r<=H`, so

\[
|S|\ge \pi(H)-\pi(q)+1.
\tag{21}
\]

Fix any `u>1` and take the polynomial window

\[
H=p^u.
\tag{22}
\]

Since `q\sim p` and `\pi(H)\sim H/\log H`, equations (13), (20), and (21) imply

\[
\frac{\operatorname{rank}\Delta_T}{|S|}
\le
\frac{H/q}{\pi(H)-\pi(q)+1}
=
O\!\left(\frac{\log p}{p}\right)
\longrightarrow0.
\tag{23}
\]

This remains true in the genuine multi-deletion regime, for example every fixed `u>2`, where `k` itself grows without bound.

For Hermitian matrices of the same dimension, the standard finite-rank interlacing bound controls the difference of their eigenvalue-counting functions by the rank of their difference. Hence, with empirical spectral distribution functions `F_red` and `F_ind`,

\[
\boxed{
\sup_\lambda
|F_{\rm red}(\lambda)-F_{\rm ind}(\lambda)|
\le
\frac{\operatorname{rank}\Delta_T}{|S|}
=
O\!\left(\frac{\log p}{p}\right)
\to0.
}
\tag{24}
\]

Thus the internal connectivity of the simultaneously deleted rough-number layer cannot create a distinct limiting **bulk** spectral distribution, on fixed polynomial windows, beyond the superposition of the one-vertex star responses.

## 5. What this does and does not rule out

The result closes a specific escape left open by PC-390. Allowing many boundary points to disappear at once does create a genuine connected interaction, but in the linear Laplacian/Kron model that interaction is completely controlled by the internal deleted-vertex Laplacian and occupies at most its contrast subspace. For two deleted points it is exactly one contrast vector; for `k` points it has rank at most `k-1`; relative to the primorial boundary size its rank tends to zero on every fixed polynomial window.

This is enough to rule out a new **bulk spectral law** whose only new ingredient is the mutual coupling of the simultaneously deleted vertices. It is not enough to rule out all spectral relevance. A perturbation of vanishing rank fraction can still move outliers, alter a determinant or log-determinant substantially, carry exceptional modes, or matter after a non-bulk normalization. Nor does (23) say that `L_red-L_S` is low rank: the independent-star baseline (6) can be full rank on the mean-zero survivor space.

Accordingly, a surviving higher-boundary route must exploit more than the empirical bulk spectrum of this linear Schur response. Plausible remaining targets include exceptional/outlier observables, nonlinear invariants sensitive to the contrast sector, cross-level evolution of those contrast subspaces, or operators whose state is not exhausted by a graph-Laplacian Schur complement.

No zeta zero, functional-equation symmetry, critical-line selection, or Hilbert--Pólya operator follows from (7)--(24).

## 6. Prior-art / novelty audit

The abstract network machinery is classical. Kron reduction of weighted graph Laplacians is Schur complementation; Dörfler and Bullo give the standard network-theoretic treatment, including the quotient property and electrical interpretation already anchored in `research/prime_circle/SOURCES.md`. The decomposition (7) is an elementary comparison between that Schur complement and the same boundary problem with the internal deleted graph switched off. Positivity and the rank bound then follow from standard Laplacian and matrix-monotonicity facts, while (24) is the usual finite-rank/interlacing control on empirical spectral measures.

No novelty is claimed for those abstract linear-algebra/network statements. The line-specific mathematical delta is their combination with the exact primorial deletion identity (19): the first genuinely multi-deletion part of the prime-circle boundary response is a deleted-vertex **contrast** correction, and its rank fraction is forced to vanish as `O(log p/p)` on every fixed polynomial window. This sharply narrows, but does not eliminate, the higher-boundary branch opened by PC-390.

## 7. Audit boundaries and falsification tests

The derivation assumes an ordinary positive weighted graph Laplacian and Schur/Kron elimination. Signed kernels, nonlinear elimination rules, shell-dependent operators not representable in the block form (4), or state spaces that change by more than vertex deletion are outside the claim.

The asymptotic rank-fraction statement uses only `k<=H/q`, the surviving-prime lower bound (21), `q~p`, and the prime number theorem. It concerns fixed polynomial windows `H=p^u`; no claim is made for exponentially growing windows where the deletion density can be different.

A decisive falsification of the exact part would require a positive Laplacian block of the form (4) for which (7) fails, or an example where `rank Delta_T>rank K`; both are direct matrix identities. A decisive falsification of the primorial asymptotic would require failure of either the exact deletion identity (19) or the elementary counting bounds leading to (23).

## Sources

- F. Dörfler and F. Bullo, *Kron Reduction of Graphs with Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), 150--163. Existing prime-circle source anchor for Schur/Kron reduction, quotient structure, and electrical-network interpretation.
- Prime number theorem and standard Hermitian finite-rank interlacing/eigenvalue-counting inequalities are used only in their classical forms.

## Consequence for the research line

PC-390's first open higher-boundary question is now sharply classified for linear graph-Laplacian/Kron transport. Simultaneous deletions do produce information absent from isolated one-vertex stars, but the genuinely connected part is confined to at most `k-1` deleted-vertex contrast modes and is asymptotically invisible to the normalized bulk spectrum on polynomial primorial windows. Future work on this branch should therefore test observables that can remain sensitive to a vanishing-rank contrast sector, rather than treating the full multi-deletion Schur response as an unconstrained new bulk operator.
