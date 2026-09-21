---
finding_id: NB-272
prefix: NB
title: Target cross terms cannot supply the missing K-scale Gram repair
status: proposed
verdict: pending
reviewed: false
created: 2026-09-21
updated: 2026-09-21
authors:
  - OpenAI
origin:
  kind: research-watch
  ref: nyman_beurling
depends_on:
  - NB-001
  - NB-269
  - NB-271
supersedes: []
superseded_by: []
related_findings:
  - NB-268
  - NB-270
---

# Target cross terms cannot supply the missing K-scale Gram repair

## Claim

In the resolved anchored multi-shell setting left open by `NB-271`, adding a fixed target to the exact Hilbert residual does **not** create a hidden positive off-diagonal Gram correction. The target enters only through a linear pairing and a section-defect scalar. For any finite resolved synthesis map

\[
S_K:\mathbb C^K\to\mathcal H,
\qquad
R_K=S_K^*S_K>0,
\qquad
b_K=S_K^*g,
\]

and Euler anchor

\[
e_K^*c=1,
\qquad e_K=(1,\ldots,1)^T,
\]

the exact constrained target residual is

\[
\boxed{
\inf_{e_K^*c=1}\|g-S_Kc\|_{\mathcal H}^2
=
\delta_K^2
+
\frac{|1-e_K^*R_K^{-1}b_K|^2}
{e_K^*R_K^{-1}e_K},
}
\tag{1}
\]

where

\[
\boxed{
\delta_K^2
=
\|g\|_{\mathcal H}^2-b_K^*R_K^{-1}b_K
=
\operatorname{dist}(g,\operatorname{ran}S_K)^2.
}
\tag{2}
\]

Thus the target pairings `b_K` do not change the coefficient-space Hessian `R_K`. In particular, they cannot by themselves supply the `Omega(K)` positive operator growth that `NB-271` proved necessary to repair the resolved Ford-channel leak. Any such new positive Gram term must come from an additional **source-source** component of the exact Nyman norm, not from the target cross term.

When `R_K` is uniformly equivalent to the resolved `NB-269` Hardy metric, so that

\[
r_-I\preceq R_K\preceq r_+I
\]

with fixed positive `r_-`,`r_+`, the anchor denominator satisfies

\[
\frac{K}{r_+}
\le
e_K^*R_K^{-1}e_K
\le
\frac{K}{r_-}.
\tag{3}
\]

Consequently the only two possible order-one target-side obstructions inside this finite resolved class are:

1. a nonvanishing section defect `delta_K^2`; or
2. an anchor mismatch

\[
\mu_K:=1-e_K^*R_K^{-1}b_K
\]

of size `Omega(sqrt(K))`.

If `delta_K=o(1)` and `mu_K=o(sqrt(K))`, then the full anchored residual tends to zero. In particular, a bounded mismatch `mu_K=O(1)` costs only `O(1/K)`.

This is an exact finite-dimensional reduction, not a proof that either condition holds for the full Nyman-Beurling problem.

## Derivation

Let

\[
c_{0,K}:=R_K^{-1}b_K.
\]

Since `R_K=S_K^*S_K` is positive definite in the resolved shell regime, direct expansion gives

\[
\|g-S_Kc\|^2
=
\|g\|^2
-2\Re(c^*b_K)
+c^*R_Kc.
\tag{4}
\]

Completing the square at the unconstrained projection coefficient vector `c_{0,K}` yields

\[
\|g-S_Kc\|^2
=
\delta_K^2
+(c-c_{0,K})^*R_K(c-c_{0,K}),
\tag{5}
\]

with `delta_K^2` given by (2). This is the target-aware finite-section identity of `NB-001` written in the resolved shell coordinates relevant to `NB-269`--`NB-271`.

The Euler constraint becomes

\[
e_K^*(c-c_{0,K})
=
1-e_K^*c_{0,K}
=
\mu_K.
\tag{6}
\]

Set `d=c-c_{0,K}`. The remaining minimization is therefore

\[
\inf_{e_K^*d=\mu_K}d^*R_Kd.
\tag{7}
\]

By Cauchy-Schwarz in the `R_K` metric,

\[
|e_K^*d|^2
=
|(R_K^{-1/2}e_K)^*(R_K^{1/2}d)|^2
\le
(e_K^*R_K^{-1}e_K)(d^*R_Kd).
\tag{8}
\]

Hence

\[
d^*R_Kd
\ge
\frac{|\mu_K|^2}{e_K^*R_K^{-1}e_K}.
\tag{9}
\]

Equality is attained by

\[
d_*
=
\frac{\mu_KR_K^{-1}e_K}
{e_K^*R_K^{-1}e_K},
\tag{10}
\]

which proves (1) exactly.

The important structural point is visible already in (4): `b_K` is a linear coefficient vector. The Hessian of the target residual with respect to `c` is exactly `R_K`; there is no additional `b_Kb_K^*`, no target-induced Toeplitz correction, and no hidden rank-one positive form. Introducing a term such as

\[
|b_K^*c|^2
=
c^*(b_Kb_K^*)c
\]

would define a different observable. It is not present in the squared Hilbert residual.

This matters because `NB-271` showed that an extra positive coefficient-space form `A_K` can produce a rank-uniform Euler-anchor floor only if its strength relative to the resolved Hardy metric grows at least like `K` and is aligned with the anchor. Equation (4) shows that the **target cross term is not such an `A_K` at all**. A genuine new Hessian can arise only if the exact Nyman residual contains an additional source map `T_Kc` whose norm contributes

\[
\|T_Kc\|^2=c^*T_K^*T_Kc,
\]

or an equivalent source-source positive component. That matrix `T_K^*T_K`, not the target pairing, is what must pass the `NB-271` operator-growth and inverse-Gram tests.

Under the `NB-269` resolved normalization, (3) follows immediately from

\[
\frac1{r_+}I
\preceq
R_K^{-1}
\preceq
\frac1{r_-}I
\]

and `\|e_K\|_2^2=K`. Therefore (1) becomes the two-scale equivalence

\[
\inf_{e_K^*c=1}\|g-S_Kc\|^2
=
\delta_K^2
+
\Theta\!\left(\frac{|\mu_K|^2}{K}\right).
\tag{11}
\]

This gives a sharper destination-side diagnostic than the generic phrase "target cross terms may restore coercivity". In this resolved class, the target can restore an order-one floor only through an actual projection defect or through `sqrt(K)`-scale incompatibility between the unconstrained target projection and the Euler anchor.

There are three useful controls.

First, take `b_K=0`. Then `c_{0,K}=0`, `mu_K=1`, and the anchor penalty is only `Theta(1/K)`, but `delta_K^2=\|g\|^2`. A target orthogonal to the source span gives a full order-one floor entirely through the section defect. This prevents interpreting (11) as a general leakage theorem.

Second, take `R_K=I` and suppose `g` lies in the source span with unconstrained coefficients

\[
c_{0,K}=K^{-1/2}e_K.
\]

Then `delta_K=0` but

\[
\mu_K=1-\sqrt K,
\]

so the anchor penalty tends to one. Thus even exact unconstrained target representability does not imply that the anchored problem leaks. The `sqrt(K)` mismatch branch is real and cannot be omitted.

Third, take `R_K=I` and

\[
c_{0,K}=K^{-1}e_K.
\]

Then `delta_K=0` and `mu_K=0`, so the anchored residual is exactly zero. This is the opposite control: neither the target nor the anchor supplies a hidden positive floor once their compatibility is exact.

The block Gram matrix makes the same separation transparent. The Gram matrix of the target and source vectors is

\[
\mathcal G_K
=
\begin{pmatrix}
\|g\|^2 & b_K^*\\
b_K & R_K
\end{pmatrix}.
\tag{12}
\]

Its Schur complement in `R_K` is precisely `delta_K^2`. The target-source block `b_K` changes that Schur complement and the location of the unconstrained minimizer, but it does not change the source-source block `R_K`. The additional affine Euler constraint then adds exactly the second scalar Schur-type penalty in (1). No third positive term is hidden in the algebra.

A fresh prior-art audit found only the generic linear-algebraic framework expected here: constrained least squares and Schur-complement identities give formulas of this form, while the Nyman-Beurling literature continues to formulate finite approximation through target projection against a Gram system. The generic algebra is therefore not claimed as novel. The new line-specific content is the combination with the `NB-269` resolved Hardy normalization and the `NB-271` `Omega(K)` repair threshold: it eliminates **target cross terms themselves** as the missing rank-global positive Gram mechanism and replaces that vague loophole by the two explicit scalars `delta_K` and `mu_K`. No new external theorem is load-bearing, so `SOURCES.md` does not require an update.

## What is established

For every finite resolved shell section with positive-definite source Gram `R_K`, equation (1) is exact. It fully separates the target-aware anchored residual into an unconstrained section defect and an Euler-anchor mismatch penalty.

Within the `NB-269` regime `R_K\asymp I`, the mismatch penalty is exactly of scale `|mu_K|^2/K`. Therefore bounded or even `o(sqrt(K))` mismatch cannot provide an order-one obstruction. Conversely, `Theta(sqrt(K))` mismatch is sufficient in scale to do so.

The target pairing vector `b_K` does not modify the coefficient-space Hessian. Hence it cannot be reinterpreted as the `Omega(K)` positive off-diagonal Gram repair sought after `NB-271`. Any new positive matrix capable of passing that threshold must be generated by additional source-source geometry in the exact destination norm.

This also refines the role of `NB-001`: target data remain essential, but after imposing the Euler anchor their effect is captured by two target-aware quantities rather than by an unspecified extra Gram structure.

## What is not established

No estimate is proved here for the actual asymptotic size of `delta_K` or `mu_K` in the full Nyman-Beurling problem. In particular, the finding does not show that the canonical target lies asymptotically in the resolved Ford source span, nor that its unconstrained projection approximately satisfies the Euler anchor.

The result does not rule out an additional exact source component `T_K` whose Gram `T_K^*T_K` has `Theta(K)` or larger relative operator strength and the anchor-aligned inverse-Gram behavior required by `NB-271`. Such a component would be genuinely new destination geometry rather than a target cross term.

The `sqrt(K)` mismatch control also blocks a tempting overclaim. Uniform boundedness of `\|g\|` and `R_K\asymp I` gives only `\|c_{0,K}\|_2=O(1)`, which permits `|e_K^*c_{0,K}|=O(sqrt(K))` by Cauchy-Schwarz. Without additional structure, one cannot improve the mismatch penalty to `o(1)`.

No assertion is made about the actual zeta zero set, no new Nyman approximation rate is obtained, and no implication toward RH follows from the finite identity alone.

## Open seam

The next discriminating calculation should no longer search for a mysterious positive form generated by the target pairing. There are now two precise branches.

The first is to estimate the actual target quantities

\[
\delta_K^2
=
\operatorname{dist}(g,\operatorname{ran}S_K)^2,
\qquad
\mu_K
=
1-e_K^*R_K^{-1}b_K
\tag{13}
\]

for the canonical Nyman target in the same rank-coupled resolved regime. A useful source-side theorem would have to prove either `delta_K=o(1)` together with `mu_K=o(sqrt(K))`, or expose a quantitative obstruction in one of these two terms without importing the desired closure statement.

The second branch is to identify the smallest exact residual component outside the `NB-269` channel that depends quadratically on the shell coefficients. If it has synthesis map `T_K`, its relative Gram

\[
R_K^{-1/2}T_K^*T_KR_K^{-1/2}
\]

must have operator norm `Omega(K)` before it can even be a candidate for rank-uniform anchor coercivity, and it must also pass the inverse-Gram anchor test of `NB-271`. Any `o(K)` component can be rejected immediately.

This narrows the destination frontier from "find off-diagonal or target-sensitive structure" to a concrete fork: **control the section defect and anchor mismatch, or exhibit a genuinely new K-scale source-source Gram component.**