# NB-032 — moving-tail orthogonal complements preserve the full asymptotic Nyman target distance

**Status:** `EXACT-DERIVED + TARGET-INDEPENDENT-GRAM-SKELETON + ASYMPTOTIC-DISTANCE-PRESERVATION + COMPRESSION-BOUNDARY`. `NB-031` proves that the moving high-index adjacent sector is uniformly target-poor in the Hilbert/Gram normalization that matters. The orthogonal complement of that nuisance sector therefore carries essentially all of the finite Nyman target projection. More strongly, that complement has rank at most the lower cutoff minus one, even though its vectors may use the entire section through Gram orthogonalization.

Let

\[
V_N:=\operatorname{span}(g_2,\ldots,g_N),
\qquad
h_n:=g_n-g_{n+1},
\]

and for integers `2<=M<N` set

\[
W_{M,N}^{\rm tail}
:=\operatorname{span}(h_M,\ldots,h_{N-1}),
\tag{1}
\]

\[
K_{M,N}
:=V_N\cap\left(W_{M,N}^{\rm tail}\right)^\perp .
\tag{2}
\]

Write

\[
d_N:=\operatorname{dist}(e,V_N),
\qquad
\kappa_{M,N}:=\operatorname{dist}(e,K_{M,N}).
\tag{3}
\]

Then the following statements are exact.

First,

\[
\boxed{
V_N=W_{M,N}^{\rm tail}\oplus K_{M,N}
}
\tag{4}
\]

and

\[
\boxed{
K_{M,N}
=\operatorname{span}\left\{
(I-P_{W_{M,N}^{\rm tail}})g_j:2\le j\le M
\right\}.
}
\tag{5}
\]

Hence

\[
\boxed{\dim K_{M,N}\le M-1.}
\tag{6}
\]

Second, the best projections satisfy the exact Pythagorean identity

\[
\boxed{
\kappa_{M,N}^2
=d_N^2+
\|P_{W_{M,N}^{\rm tail}}e\|^2.
}
\tag{7}
\]

`NB-031` gives

\[
\|P_{W_{M,N}^{\rm tail}}e\|^2
\le
\varepsilon_M,
\qquad
\varepsilon_M
:=
\frac1M+
\frac{(H_M-1)^2}{M-H_M}
=O\!\left(\frac{(\log M)^2}{M}\right),
\tag{8}
\]

uniformly in `N`. Therefore

\[
\boxed{
d_N^2
\le
\kappa_{M,N}^2
\le
d_N^2+\varepsilon_M
}
\tag{9}
\]

and, at the approximant level,

\[
\boxed{
\|P_{V_N}e-P_{K_{M,N}}e\|
=\|P_{W_{M,N}^{\rm tail}}e\|
\le\sqrt{\varepsilon_M}.
}
\tag{10}
\]

Thus the entire moving tail-adjacent family can be removed orthogonally with an explicit target-distance penalty depending only on the lower cutoff `M`, not on the full section size `N`.

The asymptotic consequence is stronger than a fixed finite-section compression. Let `N_j->infinity` and choose **any** integers `M_j` with

\[
2\le M_j<N_j,
\qquad
M_j\to\infty.
\tag{11}
\]

If

\[
d_\infty:=\lim_{N\to\infty}d_N,
\]

then (9) gives

\[
\boxed{
\kappa_{M_j,N_j}\longrightarrow d_\infty.
}
\tag{12}
\]

In particular one may require `M_j=o(N_j)`, or let `M_j` diverge arbitrarily slowly. The subspaces `K_(M_j,N_j)` then have dimension `o(N_j)` — even `O(log log N_j)` for the choice `M_j=ceil(log log N_j)` once the expression is defined — while retaining the **same limiting target distance as the entire canonical section**.

Combined with the discrete Báez-Duarte criterion already anchored for this line, for every predeclared pair of sequences satisfying (11),

\[
\boxed{
\mathrm{RH}
\iff
\kappa_{M_j,N_j}\to0.
}
\tag{13}
\]

Equation (13) is not presented as an independently new RH criterion. Its role is structural: after removing a rigorously target-poor moving tail sector, the remaining source-defined Gram skeleton may have arbitrarily slowly growing dimension without losing the asymptotic approximation problem.

## 1. The tail quotient has at most `M-1` degrees of freedom

For every `n>M`, telescoping gives

\[
g_n
=g_M-\sum_{k=M}^{n-1}h_k.
\tag{14}
\]

Therefore

\[
V_N
=
W_{M,N}^{\rm tail}
+
\operatorname{span}(g_2,\ldots,g_M).
\tag{15}
\]

Since `W_(M,N)^tail` is a finite-dimensional subspace of `V_N`, it is closed and

\[
V_N
=W_{M,N}^{\rm tail}
\oplus
\left(V_N\cap(W_{M,N}^{\rm tail})^\perp\right),
\]

which is (4). Apply `I-P_W` to (15). Because `I-P_W` maps `V_N` onto `K_(M,N)` and kills `W`,

\[
K_{M,N}
=
(I-P_W)\operatorname{span}(g_2,\ldots,g_M),
\]

proving (5)--(6). No linear-independence assumption on the canonical generators is needed.

This makes the compression geometrically explicit. The skeleton is not simply the low-index span `V_M`: each vector `(I-P_W)g_j` may acquire components involving all tail indices through the orthogonal projection. What is small is the **rank of the target-bearing complement**, not necessarily its support or its condition number.

## 2. Exact target-distance loss is the removed tail projection

Because `W:=W_(M,N)^tail` is contained in `V_N` and `K:=K_(M,N)` is its orthogonal complement inside `V_N`,

\[
P_{V_N}e=P_We+P_Ke
\tag{16}
\]

with orthogonal summands. Since `||e||=1`,

\[
d_N^2
=1-\|P_{V_N}e\|^2
=1-\|P_We\|^2-\|P_Ke\|^2,
\]

whereas

\[
\kappa_{M,N}^2
=1-\|P_Ke\|^2.
\]

Subtracting proves (7). Equation (10) follows directly from (16), and inserting the exact target-angle bound of `NB-031` proves (9).

Notice that no closure assumption, Möbius estimate, zeta estimate, eigenvalue asymptotic, or condition-number bound is used. The only Nyman-specific input beyond Hilbert projection algebra is `NB-031`'s source-derived estimate that the moving tail-adjacent space itself has vanishing target projection.

## 3. Arbitrarily slow dimensional growth preserves the limiting problem

The canonical spaces `V_N` are nested, so `d_N` decreases to `d_infinity`. For any sequences satisfying (11),

\[
d_{N_j}^2
\le
\kappa_{M_j,N_j}^2
\le
d_{N_j}^2+\varepsilon_{M_j}.
\]

Because `M_j->infinity`, `epsilon_(M_j)->0`, and (12) follows by squeezing.

This is stronger than choosing one convenient polynomial or logarithmic cutoff. The lower cutoff can grow as slowly as desired, provided it actually diverges. Consequently the asymptotic target distance is not carried by a linear-dimensional collection of high-index adjacent directions. Those directions can be projected away, and their total lost target mass tends to zero.

The statement is also unconditional with respect to the truth of RH. If RH fails and `d_infinity>0`, the thin skeletons converge to that same positive distance; they do not manufacture closure. If RH holds, they inherit closure. Thus the compression preserves the decision problem rather than biasing it toward either outcome.

## 4. The skeleton is finite-Gram constructible but globally conditioned

Let `A_N` be the canonical synthesis map, let `G_N=A_N^*A_N`, and let `D_(M,N)` be the coefficient matrix whose columns synthesize the adjacent differences `h_M,...,h_(N-1)`. Then

\[
W_{M,N}^{\rm tail}=\operatorname{ran}(A_ND_{M,N})
\]

and its orthogonal projector is

\[
P_W
=
A_ND_{M,N}
\left(D_{M,N}^*G_ND_{M,N}\right)^+
D_{M,N}^*A_N^*.
\tag{17}
\]

Thus (5) gives a completely finite target-independent construction of the skeleton from the canonical Gram data. The target pairings are needed only to evaluate the retained target distance, as required by `NB-001`.

This does **not** yield an algorithm with cost proportional to `M`. Forming the projector in (17) still uses the full tail block and may inherit severe Gram ill-conditioning. The dimension reduction is therefore a structural compression theorem, not a numerical-complexity or conditioning theorem. Any attempt to replace (17) by a local or truncated approximation must separately control the induced projection error.

## 5. Adversarial controls and failure modes

Several boundaries are essential.

First, the result does not say that the low-index canonical space `V_M` already approximates as well as `V_N`. The vectors in `K_(M,N)` are Gram-orthogonalized against the entire moving tail and can depend on all indices up to `N`. Interpreting (6) as support compression would be false.

Second, low dimension does not imply good conditioning. The skeleton basis in (5) may become nearly dependent, and its Gram matrix may be as delicate as the original problem. No uniform inverse bound is claimed.

Third, `M` must tend to infinity. For a fixed lower cutoff, `NB-031` supplies only a fixed error `epsilon_M`; there is no claim that the removed tail becomes asymptotically target-null merely by sending `N` to infinity.

Fourth, the additive error `epsilon_M` is not competitive with the deepest known quantitative Nyman rates unless `M` is chosen correspondingly large. Equation (9) preserves the limiting distance but does not improve an existing rate for `d_N`.

Fifth, the theorem does not yet identify arithmetic structure in the retained skeleton. Möbius locking acts on canonical coefficients before this global Gram orthogonalization; additional work is needed to determine whether a stable signed or multiscale invariant survives inside `K_(M,N)`.

Finally, the compression is target-relevant because `NB-031` proved a source-specific target-angle estimate for the removed subspace. The abstract fact that a subspace has small Rayleigh quotient or large codimension would not imply (7)--(10). This remains consistent with `NB-001` and `NB-030`: Gram-only compression without target control is insufficient.

## 6. Prior-art and novelty boundary

The Hilbert-space identity (7) and the orthogonal-complement construction are elementary and no novelty is claimed for those abstractions. The substantive specialization is their combination with the exact moving-tail target bound of `NB-031`, which yields the arbitrary-slow-dimensional Nyman skeleton (12)--(13).

A targeted literature check covered the classical Báez-Duarte discrete criterion and numerical finite-section work, Nicolas Jousse's work on continuity of projections onto varying Nyman subspaces, recent Gram-compressibility work of Hugh Carvill, and Jongho Yang's 2026 Friedrichs-angle study of Nyman-Beurling subspaces. Accessible statements did not identify the same canonical integer adjacent-tail orthogonal complement, the explicit distance sandwich (9), or the arbitrary-slow-rank consequence (12). Search absence is not a priority claim, and the result remains classified as an exact derived structural consequence rather than a literature novelty claim.

No external theorem is load-bearing beyond literature already anchored in `SOURCES.md`, so no source-list update is required.

## 7. Consequence for the live spectral question

`NB-030` showed that the unrestricted adjacent span can remain maximally target-bearing even in a low-Rayleigh regime. `NB-031` then isolated a genuinely target-poor moving tail. The present result completes that separation at the level of the **actual best approximation problem**: removing the entire moving tail changes the squared distance by at most `epsilon_M`, while the retained orthogonal complement has rank at most `M-1`.

Thus the target-selected spectral problem can be compressed much more aggressively than a linear-dimensional nuisance subtraction suggests. One may choose `M=o(N)` — even arbitrarily slowly divergent — and still retain the full limiting Nyman distance. The next nontrivial question is no longer whether the optimal approximant has substantial Hilbert mass outside the moving tail; (7)--(10) answer that exactly. The live question is whether the globally conditioned skeleton `K_(M,N)` admits a source-faithful multiscale description, stable conditioning, or a Möbius-sensitive invariant strong enough to control its distance to the target without simply reconstructing the full `N x N` Gram problem.