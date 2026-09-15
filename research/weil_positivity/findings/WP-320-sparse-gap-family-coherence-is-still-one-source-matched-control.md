---
id: WP-320
title: Sparse Mangoldt gap-family coherence can be reproduced by one non-atomic Herglotz control
branch: weil_positivity
status: supported
kind: sparse-family-one-source-matched-control-obstruction
claim_strength: exact matched-control construction along a sufficiently sparse subsequence of the WP-319 bounded-gap family; one fixed finite non-atomic positive Herglotz measure asymptotically reproduces both the boundary-derivative normalization and the derivative-biased gap laws at the same physical nodes and scales, so merely requiring infinitely many scalar Julia tangents to come from one source is not arithmetic-selective
created: 2026-09-15
related: [WP-304, WP-318, WP-319]
prior_art:
  - Toby O'Neil, A measure with a large set of tangent measures, Proceedings of the American Mathematical Society 123 (1995), no. 7, 2217-2220, DOI 10.2307/2160960, for the classical warning that a single Radon measure can have an extremely non-rigid family of tangent measures
  - Tuomas Sahlsten, Tangent measures of typical measures, Real Analysis Exchange 40 (2015), no. 1, 53-80, DOI 10.14321/realanalexch.40.1.0053, for the stronger generic tangent-flexibility result and a self-contained proof of the O'Neil phenomenon
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for the classical Julia-Nevanlinna reduction underlying WP-318
---

# WP-320 — Sparse Mangoldt gap-family coherence can be reproduced by one non-atomic Herglotz control

## Claim

`WP-319` leaves one scalar loophole deliberately open. Although every individual gap-normalized Mangoldt Julia law has a non-arithmetic matched control, perhaps the **fact that many such laws arise from one and the same source** imposes a family-level arithmetic rigidity that a generic positive Herglotz measure cannot reproduce.

That loophole does not survive if the family is allowed to be thinned to a sufficiently sparse infinite subsequence.

Use the fixed-gap subsequence of `WP-319`. Thus there are primes `p_j -> infinity`, a fixed integer `d>=1`, regular midpoint nodes

\[
t_j=-\frac{\log p_j+\log(p_j+d)}2,
\qquad
g_j=\log\left(1+\frac d{p_j}\right),
\tag{1}
\]

boundary derivatives

\[
D_j=
\sum_{n\ge2}
\frac{\Lambda(n)/(n+1)}{(\log n-\ell_j)^2},
\qquad
\ell_j=-t_j,
\tag{2}
\]

and derivative-biased gap-coordinate probability laws `rho_j`. The estimates already proved in `WP-319` imply

\[
D_j\asymp_d p_j\log p_j,
\qquad
g_j\asymp_d p_j^{-1},
\qquad
D_jg_j^2=O_d\!\left(\frac{\log p_j}{p_j}\right)\to0,
\tag{3}
\]

and the family `{rho_j}` is tight with

\[
\operatorname{supp}\rho_j\cap(-1/2,1/2)=\varnothing.
\tag{4}
\]

Then there is a further infinite subsequence, relabelled by `k`, and a **single finite non-atomic positive Borel measure** `mu_ctrl` on the real line such that, at the same physical nodes `t_k` and the same gap scales `g_k`, all of the following hold.

First, every `t_k` is a regular point of the Herglotz function represented by `mu_ctrl`. Second, with

\[
\widehat D_k
:=
\int_{\mathbb R}\frac{d\mu_{\rm ctrl}(x)}{(x-t_k)^2},
\tag{5}
\]

one has

\[
\boxed{\frac{\widehat D_k}{D_k}\longrightarrow1.}
\tag{6}
\]

Third, let `widehat rho_k` be the derivative-biased probability law of `mu_ctrl` at `t_k`, pushed to the **same** arithmetic gap coordinate

\[
u=\frac{x-t_k}{g_k}.
\tag{7}
\]

Then, in bounded-Lipschitz distance,

\[
\boxed{
d_{\rm BL}(\widehat\rho_k,\rho_k)\longrightarrow0.
}
\tag{8}
\]

Consequently the canonically normalized scalar Julia profiles of `WP-318` satisfy

\[
-K_{\widehat\rho_k}(\zeta)
+
K_{\rho_k}(\zeta)
\longrightarrow0
\tag{9}
\]

locally uniformly for `zeta` in the upper half-plane. If both profiles are instead normalized by the arithmetic factor `D_kg_k`, equation (6) gives the same conclusion.

Thus **one-source coherence across infinitely many gap tangents is not, by itself, a source-selective scalar positivity mechanism**. A surviving family-level route must demand substantially more: for example coherence on a non-sparse/all-gap family, an exact cross-gap invariant stable under the topology relevant to Julia reduction, or a genuinely global finite-archimedean coupling.

This result is intentionally narrower than a no-go for all family-level rigidity. The matched control is engineered from the chosen arithmetic subsequence, and the construction uses aggressive thinning. It therefore does not reproduce the full Mangoldt source, its global counting law, or dense relations among consecutive gaps.

**Classification:** `EXACT-DERIVED + LITERATURE-AUDITED + NEGATIVE/OBSTRUCTION + SPARSE-FAMILY-COHERENCE + ONE-SOURCE-MATCHED-CONTROL + NONATOMIC-HERGLOTZ-CONTROL + GAP-ADAPTED-JULIA + NOT-WEIL-POSITIVITY`.

## 1. Tightness lets each arithmetic law be approximated without copying its atoms

Fix a summable error sequence, say

\[
\varepsilon_k=2^{-k}.
\tag{10}
\]

The tightness estimate of `WP-319` is stronger than mere subsequential compactness: for fixed `d`,

\[
\limsup_{j\to\infty}
\rho_j(\{|u|>R\})
\ll_d R^{-1}.
\tag{11}
\]

Choose `R_k -> infinity` so slowly that the right-hand side of (11) is much smaller than `epsilon_k`. For every sufficiently late `j`, truncate `rho_j` to `[-R_k,R_k]`, renormalize, and smooth each retained atom by an arbitrarily short interval directed **away from zero**. Because of the exact hole (4), this produces a non-atomic probability law `sigma_{k,j}` satisfying

\[
\operatorname{supp}\sigma_{k,j}
\subset
[-2R_k,-1/2]\cup[1/2,2R_k],
\tag{12}
\]

and

\[
d_{\rm BL}(\sigma_{k,j},\rho_j)\le\varepsilon_k
\tag{13}
\]

once `j` is late enough. The smoothing is purely a control construction: it deliberately destroys the prime-power atoms while retaining the topology seen by bounded analytic Herglotz kernels.

The compact support also gives

\[
\int u^2\,d\sigma_{k,j}(u)
\le4R_k^2.
\tag{14}
\]

## 2. Sparse block grafting produces one finite non-atomic source

Choose the arithmetic index `j_k` inductively so far out in the fixed-`d` family that, in addition to (13), all of the following hold:

\[
D_{j_k}\ge k,
\qquad
2R_kg_{j_k}<\frac14,
\qquad
4R_k^2D_{j_k}g_{j_k}^2\le2^{-k},
\tag{15}
\]

and the physical centers are pairwise separated by more than `4`:

\[
|t_{j_k}-t_{j_l}|>4
\qquad(k\ne l).
\tag{16}
\]

All four requirements are compatible. Indeed `D_j -> infinity` by (3), `g_j ->0`, `D_jg_j^2->0`, and `t_j=-\log p_j+o(1)->-infinity`.

Write

\[
t_k:=t_{j_k},\quad
g_k:=g_{j_k},\quad
D_k:=D_{j_k},\quad
\rho_k:=\rho_{j_k},\quad
\sigma_k:=\sigma_{k,j_k}.
\tag{17}
\]

Let

\[
A_k(u):=t_k+g_ku
\tag{18}
\]

and define the positive non-atomic block

\[
\boxed{
\mu_k
:=D_kg_k^2\,(A_k)_\#\bigl(u^2\sigma_k(du)\bigr).
}
\tag{19}
\]

Its total mass obeys

\[
M_k:=\mu_k(\mathbb R)
=D_kg_k^2\int u^2d\sigma_k(u)
\le2^{-k}.
\tag{20}
\]

Therefore

\[
\boxed{
\mu_{\rm ctrl}:=\sum_{k\ge1}\mu_k
}
\tag{21}
\]

is a finite positive non-atomic Borel measure. In particular it satisfies the one-dimensional Herglotz growth condition automatically and defines a scalar Herglotz-Nevanlinna function through the standard integral representation.

Equation (12) says that the `k`th block has no support in

\[
(t_k-g_k/2,t_k+g_k/2).
\tag{22}
\]

By (15)-(16), every other block is more than a fixed positive physical distance from `t_k`. Hence `t_k` is a regular point for the **single assembled control source**, not merely for its own block.

## 3. The own block matches the derivative exactly and remote blocks vanish relatively

The factor `u^2` in (19) is chosen for one exact reason. Since `x-t_k=g_ku` on the `k`th block,

\[
\begin{aligned}
\int\frac{d\mu_k(x)}{(x-t_k)^2}
&=D_kg_k^2
\int\frac{u^2}{g_k^2u^2}\,d\sigma_k(u)\\
&=D_k.
\end{aligned}
\tag{23}
\]

Thus the own block reproduces the arithmetic derivative normalization exactly, while its derivative-biased gap law is exactly `sigma_k`.

Let the other blocks contribute

\[
E_k
:=
\sum_{l\ne k}
\int\frac{d\mu_l(x)}{(x-t_k)^2}.
\tag{24}
\]

The physical separation in (15)-(16) gives a constant `c>0`, independent of `k,l`, such that every point in the `l`th block is at distance at least `c` from `t_k`. Therefore

\[
0\le E_k
\le c^{-2}\sum_lM_l
<\infty.
\tag{25}
\]

The right-hand side is independent of `k`, whereas `D_k->infinity`. Hence

\[
\frac{E_k}{D_k}\to0,
\qquad
\widehat D_k=D_k+E_k,
\tag{26}
\]

which proves (6).

If `eta_k` denotes the derivative-biased gap law contributed by all remote blocks, then the full control law decomposes exactly as

\[
\widehat\rho_k
=
\frac{D_k}{D_k+E_k}\,\sigma_k
+
\frac{E_k}{D_k+E_k}\,\eta_k.
\tag{27}
\]

Consequently

\[
\begin{aligned}
d_{\rm BL}(\widehat\rho_k,\rho_k)
&\le
 d_{\rm BL}(\sigma_k,\rho_k)
 +2\frac{E_k}{D_k+E_k}\\
&\le
\varepsilon_k+o(1)
\longrightarrow0,
\end{aligned}
\tag{28}
\]

which proves (8). Notice that no control on where `eta_k` lives in the normalized coordinate is required. Its entire contribution is suppressed by the vanishing derivative weight `E_k/(D_k+E_k)`.

## 4. The topology is strong enough for the Julia-profile conclusion

The approximate matched control matters only if the observable used by the proposed sign mechanism is stable in the topology being matched. Here it is.

For a probability law `rho`, its Cauchy transform

\[
G_\rho(\zeta)=
\int_{\mathbb R}\frac{d\rho(u)}{\zeta-u}
\tag{29}
\]

has a kernel that is bounded and Lipschitz in `u`, uniformly when `zeta` ranges over a compact subset of the upper half-plane. Thus (8) implies local uniform convergence of the corresponding Cauchy transforms. The arithmetic family is uniformly tight by `WP-319`; equation (28) makes the control family uniformly tight as well. On every compact subset of the upper half-plane this supplies a uniform nonzero lower bound for `|G|`, so reciprocal Cauchy transforms are stable too.

`WP-318` identifies the normalized scalar Julia response exactly with the negative Boolean self-energy `-K_rho`, obtained from this reciprocal-Cauchy-transform operation. Therefore (8) implies (9). The control matches not merely a weak measure-theoretic decoration but the actual normalized scalar Julia field on compact spectral sets.

This addresses the matched-control stability caveat explicitly: the approximation is taken in a topology in which the proposed local sign observable is continuous.

## 5. What this falsifies, and what it leaves open

The result kills a specific strengthening of the one-point route left open in `WP-319`:

> require that infinitely many arithmetic gap tangents belong to one common positive Herglotz source.

That requirement alone is too weak. After sparse thinning, a single **non-atomic** source can reproduce the same derivative normalizations and normalized Julia profiles asymptotically. Scalar Pick positivity therefore still does not know that the source was Mangoldt.

Several stronger statements are deliberately not claimed.

The construction does **not** reproduce every bounded prime-power gap, every consecutive gap, or any positive-density family of nodes. It uses arbitrarily large physical separation between selected charts. A rigidity theorem coupling nearby or overlapping charts can therefore escape this control.

The control is deliberately engineered from the target laws. It is not a natural Euler-product competitor, and it does not share the Mangoldt counting function, multiplicative correlations, or global explicit formula. Accordingly this finding does not show that all arithmetic information is absent; it shows only that the local scalar Julia data in (5)-(9), even when required at infinitely many nodes of one source, do not identify it.

The matching is asymptotic in bounded-Lipschitz/compact-Herglotz topology, not an exact equality of atomic laws. An exact discrete family identity or a discontinuous invariant may contain more information, but such an invariant would need its own canonicality and positivity theorem.

Finally, nothing in the construction creates the Gamma term, the pole/trivial-zero counterterms, or a global Weil quadratic form. Matrix/operator-valued boundary responses, nonseparable finite-archimedean geometry, and genuine cohomological/intersection mechanisms remain untouched.

## 6. Prior-art and novelty audit

The generic warning behind this result is classical rather than new. O'Neil constructed a Radon measure for which, at almost every point, **every** nonzero locally finite Radon measure occurs as a tangent measure; Sahlsten later gave a self-contained proof that this extreme tangent flexibility is typical in the Baire-category sense. Those theorems already show that a rich family of local blow-up profiles need not characterize a source without additional regularity or cross-scale structure.

The present result is not claimed as a new theorem in geometric measure theory. Its Mathia-specific content is the explicit compatibility with the `WP-319` arithmetic coordinates and with the derivative normalization forced by scalar Julia reduction: the blocks are placed at the **same moving gap midpoints**, use the **same gap scales**, match `D_k` relatively, and after derivative bias reproduce the actual normalized Julia fields. The proof is an elementary sparse-grafting construction specialized to that Herglotz observable.

Classical boundary Nevanlinna-Pick theory supplies the Julia positivity itself, as already audited in `WP-318`. Neither that positivity nor tangent-measure flexibility is new. The substantive research delta is the closure of the weak same-source escape left explicitly open by `WP-319`.

## Consequence for the research line

The scalar support-side frontier is narrower again. `WP-319` showed that one arithmetic gap tangent is matched-control universal; this finding shows that even **infinitely many** such tangents can remain matched-control universal when sampled sparsely from one source.

Therefore a scalar Julia route can no longer claim family-level arithmetic specificity merely from common provenance. It must exhibit a cross-gap constraint that survives without thinning and that one positive Herglotz source cannot reproduce by separated local grafting. Even then, it would still have to generate the archimedean and global Weil terms from the same independently positive structure.