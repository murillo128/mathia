# XF-023 — summable fixed-index variance tapers have unavoidable collision-positive spikes

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/BOUNDARY`. XF-021 showed that compactly supported centered convex entropies have a positive adjacent-collision boundary pole, while XF-022 ruled out finite-range translation-invariant quadratic overlap as a universal mean-removal repair. One apparent escape remained: replace compact support by a fixed noncompact taper whose weights are positive everywhere and summable, so there is no literal support edge.

That escape fails already for the weighted quadratic variance. Let

\[
\alpha_i\ge 0,
\qquad
0<A:=\sum_{i\in\mathbb Z}\alpha_i<\infty,
\]

with at least two positive weights, and define

\[
\mu_\alpha=\frac1A\sum_i\alpha_i g_i,
\qquad
V_\alpha=\frac12\sum_i\alpha_i(g_i-\mu_\alpha)^2.
\]

For every such fixed index-space weight profile there is an index `j` and a positive local gap configuration with one collapsing gap `g_j=\varepsilon\downarrow0` for which the exact gap diffusion has

\[
\boxed{
V_\alpha'
=-\frac{2}{\varepsilon}
\Bigl[
\alpha_{j-1}a+\alpha_{j+1}b
+\mu_\alpha\bigl(2\alpha_j-\alpha_{j-1}-\alpha_{j+1}\bigr)
\Bigr]
+O(1)
\longrightarrow +\infty .
}
\]

The new structural point is that a collapsing gap probes the **discrete Laplacian of the taper itself**. Any nonzero nonnegative summable profile must have a site where

\[
2\alpha_j-\alpha_{j-1}-\alpha_{j+1}<0.
\]

At such a site the two neighboring gaps can be chosen sufficiently small while the weighted mean is kept positive by weight elsewhere, forcing the displayed bracket to be negative. Thus an infinitely supported logarithmic, polynomial, exponential, or otherwise slowly decaying fixed taper does not remove the source-free collision obstruction: it only moves it from a hard support edge to a site of negative taper curvature.

This does not rule out time/configuration-dependent weights, nonlinear/projective global functionals, or a genuinely Xi-specific lower-gap relation coupling the taper scale to the smallest exterior gap. It does close the natural **fixed summable index-taper + weighted variance** route left open after XF-021.

## 1. Exact singular law for a weighted quadratic variance

On a real-simple Xi slice covered by XF-014,

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=c_{ki}>0.
\tag{1}
\]

Write the weighted variance as

\[
V_\alpha
=\frac12\sum_i\alpha_i g_i^2
-\frac1{2A}\left(\sum_i\alpha_i g_i\right)^2.
\tag{2}
\]

Therefore its gradient is

\[
\boxed{
\frac{\partial V_\alpha}{\partial g_i}
=\alpha_i(g_i-\mu_\alpha).
}
\tag{3}
\]

The moving-mean term is already included in (3); equivalently, direct differentiation uses

\[
\sum_i\alpha_i(g_i-\mu_\alpha)=0
\]

to cancel the `\mu_\alpha'` contribution.

Fix an index `j` and set

\[
g_{j-1}=a>0,
\qquad
g_j=\varepsilon>0,
\qquad
g_{j+1}=b>0,
\tag{4}
\]

while all other local gaps remain fixed and positive as `\varepsilon\downarrow0`. The only singular conductances are

\[
c_{j-1,j}=\frac1{a\varepsilon},
\qquad
c_{j,j+1}=\frac1{\varepsilon b}.
\tag{5}
\]

All other pair contributions stay `O(1)` because every corresponding denominator contains a fixed positive intervening span.

The pair `(j-1,j)` contributes

\[
2\frac{\varepsilon-a}{a\varepsilon}
\Bigl[
\alpha_{j-1}(a-\mu_\alpha)
-\alpha_j(\varepsilon-\mu_\alpha)
\Bigr],
\tag{6}
\]

and `(j,j+1)` contributes

\[
2\frac{b-\varepsilon}{\varepsilon b}
\Bigl[
\alpha_j(\varepsilon-\mu_\alpha)
-\alpha_{j+1}(b-\mu_\alpha)
\Bigr].
\tag{7}
\]

Adding them gives the exact leading collision coefficient

\[
\boxed{
V_\alpha'
=-\frac{2}{\varepsilon}
\left[
\alpha_{j-1}a+\alpha_{j+1}b
+\mu_\alpha\,(A_d\alpha)_j
\right]
+O(1),
}
\tag{8}
\]

where

\[
\boxed{
(A_d\alpha)_j
:=2\alpha_j-\alpha_{j-1}-\alpha_{j+1}
}
\tag{9}
\]

is the nearest-neighbor discrete Laplacian with the same sign convention used for `A` in XF-022.

Equation (8) is the main identity. XF-021's compact-support spike is recovered when the collapsing gap lies just outside a support edge: then `\alpha_j=\alpha_{j+1}=0`, so `(A_d\alpha)_j=-\alpha_{j-1}` and the coefficient is positive whenever the supported neighboring gap lies below the weighted mean.

## 2. A nonnegative summable taper must have negative discrete curvature somewhere

Suppose first that `\alpha` has infinite support. Since `\alpha\in\ell^1(\mathbb Z)`,

\[
\alpha_i\to0
\qquad(|i|\to\infty).
\tag{10}
\]

Assume for contradiction that

\[
(A_d\alpha)_j\ge0
\qquad\text{for every }j.
\tag{11}
\]

Define first differences

\[
d_j:=\alpha_j-\alpha_{j-1}.
\tag{12}
\]

Then

\[
(A_d\alpha)_j=d_j-d_{j+1},
\tag{13}
\]

so (11) says that `d_j` is nonincreasing in `j`.

If some `d_j>0`, then `d_m\ge d_j>0` for every `m\le j`; summing those increments backwards forces `\alpha` to become negative or unbounded, contradicting nonnegativity together with the left limit in (10). If some `d_j<0`, monotonicity gives `d_m\le d_j<0` for every `m\ge j`; summing forward contradicts nonnegativity and the right limit in (10). Hence every `d_j=0`, so `\alpha` is constant, and (10) forces `\alpha\equiv0`, contradicting `A>0`.

Therefore every nonzero nonnegative summable infinite-support taper satisfies

\[
\boxed{
\exists j:\quad (A_d\alpha)_j<0.
}
\tag{14}
\]

This is the elementary one-dimensional discrete Liouville/maximum-principle obstruction behind the result. No external theorem is needed for it.

If `\alpha` has finite support and at least two positive entries, let `r` be its rightmost positive index and take `j=r+1`. Then

\[
(A_d\alpha)_j=-\alpha_r<0,
\tag{15}
\]

and at least one other positive weight lies outside the triple `{j-1,j,j+1}`. Thus the same construction below also contains the compact case, consistently with XF-021.

## 3. Negative taper curvature forces a positive `1/epsilon` spike

Choose `j` as in (14), or as in (15) in the finite-support case, so that

\[
\kappa:=-(A_d\alpha)_j>0.
\tag{16}
\]

Let

\[
W:=A-(\alpha_{j-1}+\alpha_j+\alpha_{j+1}).
\tag{17}
\]

For infinite support, `W>0` automatically. In the finite-support construction above, the assumption of at least two positive weights also gives `W>0`.

Fix a background spacing `h>0`, set every gap outside the triple in (4) equal to `h`, and choose

\[
a=b=\delta h
\tag{18}
\]

with `\delta>0` independent of `\varepsilon`. As `\varepsilon\downarrow0`,

\[
\mu_\alpha
\longrightarrow
\mu_0(\delta)
=
\frac{Wh+\delta h(\alpha_{j-1}+\alpha_{j+1})}{A}
\ge \frac{Wh}{A}>0.
\tag{19}
\]

The bracket in (8) tends to

\[
B(\delta)
=
\delta h(\alpha_{j-1}+\alpha_{j+1})
-\kappa\mu_0(\delta).
\tag{20}
\]

At `\delta=0`,

\[
B(0)=-\kappa\frac{Wh}{A}<0.
\tag{21}
\]

Hence by continuity one may choose a fixed sufficiently small `\delta>0` for which `B(\delta)<0`. Equation (8) then gives

\[
\boxed{
V_\alpha'
=\frac{2|B(\delta)|}{\varepsilon}+O(1)
\longrightarrow+\infty.
}
\tag{22}
\]

Thus making the taper arbitrarily gentle does not give a source-free uniform upper bound. If a scale-dependent taper `\alpha^{(N)}` has a very small negative curvature `-\kappa_N`, one can choose the collapsing gap still smaller than that curvature scale. Without an independent lower-gap relation tying `\varepsilon` to `\kappa_N`, the singularity always wins.

This is exactly analogous to the last-positive-weight observation in XF-021, but it no longer relies on a literal support edge. The obstruction is intrinsic to the curvature required for any nonnegative summable profile to rise from and return to zero.

## 4. Why noncompact capacity does not solve the adjacent-collision problem

XF-017 shows that a logarithmic capacitary taper can make the **fractional Cauchy cutoff cost** vanish like `O(1/log R)` when the inner/outer scale ratio diverges. That is a statement about the aggregate long-range kernel

\[
\sum_{i<k}\frac{(\psi_i-\psi_k)^2}{(i-k)^2}.
\]

Equation (22) is a different obstruction. A single collapsing gap sees the local second difference of the fixed index weights and contributes `1/\varepsilon`. Even when the taper curvature tends to zero with scale, source-free positivity allows `\varepsilon` to tend to zero faster.

Therefore a noncompact or very long capacitary taper can solve the critical **far-leakage** problem and still fail the **adjacent collision** problem. These mechanisms should not be conflated.

In particular, replacing the final zero weight of a compact taper by a tiny positive tail does not remove the issue. The hard boundary disappears, but a nonnegative summable tail necessarily introduces negative discrete curvature somewhere, and that site becomes the new collision witness.

## 5. Matched-control and convergence boundary

The obstruction is local in the singular parameter. Once `g_j=\varepsilon` and its two neighboring gaps are fixed, only the conductances in (5) are `O(1/\varepsilon)`; all interactions with more distant gaps are `O(1)` as `\varepsilon\downarrow0`.

For an infinite summable taper, the background construction above is an asymptotically uniform ordered synthetic gap configuration with only finitely many gaps changed from `h`. The weighted variance is finite, and the far weighted derivative is harmless: the perturbation-induced gap velocities decay with distance while `\alpha\in\ell^1`. More conservatively, the same leading coefficient can be realized in arbitrarily large finite real-rooted polynomial controls of the type used in XF-006. The two adjacent singular root interactions reproduce (8), while finite endpoints and all other roots contribute only `O(1)`.

Thus the spike does not rely on an impossible ordering or on exchanging a delicate infinite sum. It is a local matched-control obstruction to obtaining a universal Lyapunov inequality from fixed summable weights and the gap ODE alone.

The result still does **not** say that the actual Xi configuration realizes this adversarial local geometry. An Xi-specific theorem that prevents a gap from becoming smaller than the taper-curvature scale could defeat the witness. No such relation is supplied by the universal diffusion identity itself.

## 6. Prior art and novelty boundary

The fact used in Section 2 is an elementary one-dimensional discrete maximum-principle/Liouville statement: a nonnegative superharmonic sequence on the recurrent line cannot form a nontrivial summable bump. General versions belong to classical discrete potential theory and random-walk recurrence. The proof needed here is only the two-line monotonicity argument for first differences, so no external theorem is load-bearing and `SOURCES.md` does not need a new anchor.

Likewise, no novelty is claimed for weighted variance differentiation or for the observation that a smooth localization profile must possess curvature. The durable contribution is the exact interaction with the Xi/log-repulsion collision singularity: the leading pole is governed by `(A_d\alpha)_j`, which turns the qualitative compact-boundary obstruction of XF-021 into a no-go for **every fixed nonnegative summable index taper**, including infinitely supported ones.

XF-022 is complementary rather than redundant. There the collision operator `AL` acts on the **gap field** for finite-range translation-invariant quadratic mean removal. Here the nearest-neighbor Laplacian acts on the **localization weights** themselves. The two results close different quadratic escape routes.

## 7. Consequence for `xi_flow`

The centered weighted-variance route should no longer spend effort replacing compact cutoffs by fixed positive summable tails. The fractional capacity gain of XF-017 cannot by itself regularize the adjacent collision pole, because any such taper has a negative-curvature site and the smallest gap is not source-controlled relative to that curvature.

Combined with XF-021 and XF-022, the remaining mean-removal mechanisms are now genuinely outside ordinary fixed-index quadratic localization: configuration-dependent weights whose evolution supplies a compensating term; nonlinear/global/projective functionals built from physical spans or cross-ratios; or Xi-specific gap information strong enough to rule out the local collision witnesses. Among these, the uncentered cross-ratio carrier of XF-018--XF-020 remains the cleanest collision-safe starting point because its dangerous conductances are absorbed before any mean subtraction is imposed.