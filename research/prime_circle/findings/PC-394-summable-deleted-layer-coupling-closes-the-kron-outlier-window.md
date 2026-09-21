# PC-394 — summable deleted-layer coupling closes the Kron outlier window

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the individual-outlier escape left open by PC-391/PC-393 in the positive inverse-power chord/Kron branch.

PC-391 showed that the genuinely simultaneous part of a multi-deletion Kron response has vanishing rank fraction on fixed polynomial primorial windows, but explicitly left individual outliers open. PC-393 later closed normalized determinant and pseudodeterminant amplification, while still leaving the possibility that one exceptional eigenvalue of the thin contrast sector could remain order one.

For the same positive regularized inverse-power chord kernel, the internal geometry of the deleted layer gives a sharper bound. At the successive primorial step `P_p -> q P_p`, every simultaneously deleted exponent is a multiple of the new prime `q`. Hence distinct deleted vertices are separated by at least `q`, and the internal deleted-vertex conductances inherit the inverse-power decay at that coarse spacing. Combining this with the exact Schur-complement factorization gives

\[
\boxed{
\|\Delta_T\|_{\rm op}
\le \operatorname{tr}K,
}
\tag{1}
\]

where `K` is the Laplacian of the graph induced on the deleted set. On `H=p^u`, `u>2`, Buchstab counting then yields, for every `alpha>1/2`,

\[
\boxed{
\|\Delta_T\|_{\rm op}
=O_{\alpha,\tau,u}\!\left(
\frac{p^{u-1-2\alpha}}{\log p}
\right).
}
\tag{2}
\]

Therefore throughout the genuine multi-deletion window

\[
\boxed{
2<u\le 1+2\alpha,
\qquad \alpha>\frac12,
}
\tag{3}
\]

the irreducible simultaneous-deletion correction tends to zero in operator norm. By Weyl's inequality every eigenvalue of the true Kron response and the independent-star baseline then differs by `o(1)`. Thus **the internal coupling of the deleted layer cannot create a persistent unscaled spectral outlier in this whole summable-decay phase**.

For the inverse-square case `alpha=1`, this closes the complete first higher-boundary range `2<u<=3`, including the critical cubic window where the bound is `O(1/log p)`. The result does not cover `u>1+2 alpha`, `alpha<=1/2`, signed/indefinite kernels, renormalized outliers, or cross-level evolution of the contrast eigenspaces.

## 1. Exact contraction of the simultaneous-deletion correction

Use the notation of PC-391. Let `S` be the surviving boundary and `T={t_1,...,t_k}` the vertices deleted simultaneously. Let

\[
B=(b_{ai})_{a\in S,\,i\le k},
\qquad
d_i:=\sum_{a\in S}b_{ai},
\qquad
D:=\operatorname{diag}(d_1,...,d_k),
\tag{4}
\]

and let `K` be the weighted Laplacian of edges internal to `T`. PC-391 proved

\[
\Delta_T
=B\left[D^{-1}-(D+K)^{-1}\right]B^\top\succeq0.
\tag{5}
\]

Because the chord kernel is strictly positive, every `d_i>0`. Define

\[
P:=BD^{-1}.
\tag{6}
\]

The `i`th column `p_i` of `P` is the normalized incidence profile of deleted vertex `t_i`; it is a probability vector on `S`:

\[
p_i\ge0,
\qquad
\mathbf1^\top p_i=1.
\tag{7}
\]

Writing

\[
Q:=D-D(D+K)^{-1}D,
\tag{8}
\]

gives the exact factorization

\[
\boxed{\Delta_T=PQP^\top.}
\tag{9}
\]

Moreover

\[
Q=D(D+K)^{-1}K=K(D+K)^{-1}D
\tag{10}
\]

and

\[
K-Q=K(D+K)^{-1}K\succeq0.
\tag{11}
\]

Hence

\[
\boxed{0\preceq Q\preceq K,}
\qquad
\boxed{0\preceq\Delta_T\preceq PKP^\top.}
\tag{12}
\]

This is the relevant extra information beyond the rank bound of PC-391: the irreducible response is not merely supported on the deleted contrast space; its size is controlled by the conductance actually connecting those deleted vertices to one another.

If `c_{ij}` is the internal conductance between `t_i` and `t_j`, then

\[
K=\sum_{i<j}c_{ij}(e_i-e_j)(e_i-e_j)^\top
\tag{13}
\]

and therefore

\[
PKP^\top
=\sum_{i<j}c_{ij}(p_i-p_j)(p_i-p_j)^\top.
\tag{14}
\]

Since probability vectors satisfy `||p_i-p_j||_2^2<=2`, positivity gives

\[
\begin{aligned}
\|\Delta_T\|_{\rm op}
&\le \|PKP^\top\|_{\rm op}\\
&\le \operatorname{tr}(PKP^\top)\\
&=\sum_{i<j}c_{ij}\|p_i-p_j\|_2^2\\
&\le2\sum_{i<j}c_{ij}\\
&=\operatorname{tr}K.
\end{aligned}
\tag{15}
\]

Equation (15) is independent of the conditioning of `D` and avoids the small-denominator issue that would arise from bounding `(D+K)^{-1}` directly.

## 2. Primorial deletion forces a coarse `q`-spaced internal graph

At a successive primorial step, PC-391 gives the exact deleted set

\[
T=q\,R_p(H/q),
\tag{16}
\]

where `q` is the next prime after `p` and

\[
R_p(L):=\{1\le r\le L:(r,P_p)=1\}.
\tag{17}
\]

Put

\[
L:=H/q,
\qquad
k:=|T|=|R_p(L)|.
\tag{18}
\]

Thus every pair of distinct deleted exponents has separation

\[
|t_i-t_j|=q|r_i-r_j|.
\tag{19}
\]

For the normalized regularized inverse-power chord kernel of PC-390,

\[
\kappa_M(d)
=M^{-2\alpha}
\left[2\left(\cosh\frac{\tau}{M}-\cos\frac{2\pi d}{M}\right)\right]^{-\alpha},
\tag{20}
\]

with `alpha>0`, `tau>=0`, the local Euclidean expansion already established in PC-390 is uniform on every polynomial window `H=o(M)`. In particular, for all sufficiently large `p`,

\[
\boxed{
\kappa_M(d)\le C_{\alpha,\tau}|d|^{-2\alpha}
\qquad(1\le |d|\le H).
}
\tag{21}
\]

Consequently

\[
\sum_{i<j}c_{ij}
\le
C_{\alpha,\tau}q^{-2\alpha}
\sum_{i<j}|r_i-r_j|^{-2\alpha}.
\tag{22}
\]

For each integer separation `h`, a subset of `k` integer points contains at most `k` unordered pairs at distance `h`. Hence

\[
\boxed{
\operatorname{tr}K
\le
C_{\alpha,\tau}
\,k q^{-2\alpha}
\sum_{1\le h\le L}h^{-2\alpha}.
}
\tag{23}
\]

This estimate uses only the exact `q`-multiple structure of the Buchstab deletion layer; it does not assume random primes, pair correlation, or a conjectural gap law.

## 3. Summable chord tails eliminate unscaled outliers up to `u=1+2 alpha`

Take the fixed polynomial window

\[
H=p^u,
\qquad u>2.
\tag{24}
\]

Then `q~p` and `L=H/q~p^{u-1}`. PC-388's classical Buchstab asymptotic for rough numbers gives

\[
k=|R_p(L)|
=O_u\!\left(\frac{p^{u-1}}{\log p}\right).
\tag{25}
\]

If `alpha>1/2`, the series in (23) is summable:

\[
\sum_{h\le L}h^{-2\alpha}=O_\alpha(1).
\tag{26}
\]

Combining (15), (23), and (25),

\[
\boxed{
\|\Delta_T\|_{\rm op}
=O_{\alpha,\tau,u}\!\left(
\frac{p^{u-1-2\alpha}}{\log p}
\right).
}
\tag{27}
\]

Therefore

\[
2<u\le1+2\alpha
\quad\Longrightarrow\quad
\boxed{\|\Delta_T\|_{\rm op}\to0.}
\tag{28}
\]

The endpoint is included: when `u=1+2 alpha`, (27) is `O(1/log p)`.

Since

\[
L_{\rm red}=L_{\rm ind}+\Delta_T,
\qquad \Delta_T\succeq0,
\tag{29}
\]

Weyl's eigenvalue inequalities imply, for every ordered eigenvalue,

\[
\boxed{
0\le
\lambda_j(L_{\rm red})-\lambda_j(L_{\rm ind})
\le\|\Delta_T\|_{\rm op}=o(1).
}
\tag{30}
\]

Thus there is no persistent order-one eigenvalue displacement attributable to the *irreducible mutual coupling* of the simultaneously deleted layer in this regime. Any order-one outlier already present in `L_ind` comes from the direct survivor graph or the superposed one-vertex star responses classified earlier; it is not generated by the higher-boundary interaction isolated in PC-391.

The important concrete case is `alpha=1`. Then

\[
\boxed{
2<u\le3
\quad\Longrightarrow\quad
\|\Delta_T\|_{\rm op}=O\!\left(
\frac{p^{u-3}}{\log p}
\right)=o(1).
}
\tag{31}
\]

So inverse-square chord geometry does not acquire an exceptional simultaneous-deletion eigenvalue anywhere from the first rough-composite threshold through the cubic boundary window.

## 4. The threshold is a proof boundary, not evidence for a transition

For completeness, (23) also shows why the argument is specific to summable chord tails. At `alpha=1/2`,

\[
\sum_{h\le L}h^{-1}=O(\log L),
\tag{32}
\]

and for `0<alpha<1/2`,

\[
\sum_{h\le L}h^{-2\alpha}=O(L^{1-2\alpha}).
\tag{33}
\]

In the genuine multi-deletion range `u>2`, these universal bounds no longer force `||Delta_T|| ->0`. Likewise, for `alpha>1/2` and `u>1+2 alpha`, (27) becomes inconclusive.

Nothing singular is proved to occur at `u=1+2 alpha`; the line is only where the present source-forced upper bound ceases to vanish. A sharper estimate could move it. In particular, PC-394 does **not** assert existence of outliers beyond the boundary, nor does it rule out an outlier after multiplying the contrast correction by a diverging normalization.

## 5. Prior-art and novelty audit

The abstract ingredients are classical. Kron reduction is Schur complementation of graph Laplacians, with the standard network interpretation given by Dörfler and Bullo, already anchored in `research/prime_circle/SOURCES.md`. The order relation in (12) is the elementary positive-matrix/parallel-sum structure behind Schur reduction; no novelty is claimed for it. Weyl eigenvalue stability and the summability of `h^{-2 alpha}` are standard.

The arithmetic density input is also classical. PC-388 already anchored the rough-number/Buchstab asymptotic, including Kai Fan's modern explicit treatment of `Phi(x,y)`. No new sieve estimate is used here.

The line-specific mathematical delta is their combination with the *exact shape of the simultaneously deleted primorial layer*: `T=q R_p(H/q)`. That forces every internal deleted edge onto the coarse `q`-lattice, and after the normalized-incidence contraction (9)--(15) this produces the explicit outlier bound (27). I did not find prior art making this prime-circle/Kron/Buchstab phase statement; its components are classical, so the result is classified as a project-specific boundary/no-go rather than a new graph-spectral or sieve theorem.

No zeta zero, functional-equation symmetry, critical-line selector, or Hilbert--Pólya operator follows from this estimate.

## 6. Falsification and scope

The finite-dimensional core is directly falsifiable. For any positive weighted Laplacian block of the PC-391 form, construct `P,Q,K` and check (9)--(15). A violation of `Delta_T <= P K P^T` or `||Delta_T|| <= tr K` would invalidate the exact step.

For the prime-circle specialization, enumerate `T=q R_p(H/q)`, build its internal chord Laplacian, and compare `||Delta_T||` against the right side of (23). The asymptotic conclusion additionally depends on the established Buchstab count (25) and the uniform local chord estimate (21).

The finding is restricted to positive regularized inverse-power chord conductances on fixed polynomial primorial windows. It does not cover signed/indefinite kernels, nonlinear elimination, exponentially growing windows, shell-dependent rescalings that amplify `Delta_T`, or observables depending on the orientation/evolution of the vanishing contrast subspace rather than its unscaled operator amplitude.

## Consequence for the research line

PC-391's vanishing-rank result left open the possibility that the thin simultaneous-deletion sector might still matter through a single exceptional eigenvalue. PC-393 removed normalized determinant amplification but did not address that loophole. PC-394 closes it for the natural summable-tail phase: when `alpha>1/2` and `2<u<=1+2 alpha`, the entire irreducible multi-deletion correction vanishes in operator norm, so it cannot generate any persistent unscaled spectral outlier.

For the canonical inverse-square interaction this removes the outlier route through `H<=p^3`. What remains genuinely open in this positive linear-Kron branch is pushed to longer windows `u>1+2 alpha`, renormalized exceptional observables, or cross-level phase/subspace information. Signed/indefinite and nonlinear operators remain outside the argument entirely.