# PL-323 — A coercive tail comparison closes the remaining pointwise endpoint-flux gate

**Evidence:** `EXACT-DERIVED + POSITIVE-GATE-CLOSURE + STANDARD-NONLOCAL-MAXIMUM-PRINCIPLE`

**Status:** `POINTWISE-QM-GATE-CLOSED + PL321-ENDPOINT-TRANSFER-AVAILABLE + ARITHMETIC-FIRST-CROSSING-STILL-OPEN`

## Precise claim

`PL-322` reduces the completed-Weil endpoint problem to the pointwise relation

\[
2Qm(Q)+H_{Q_0}m(Q)\longrightarrow0,
\tag{PL323-1}
\]

where

\[
H_{Q_0}m(Q)
=
\int_{Q_0}^{\infty}
\bigl(m(Q)-m(P)\bigr)
\frac{dP}{e^{|Q-P|}-1},
\tag{PL323-2}
\]

in the same pointwise singular-integral sense as `PL-319`--`PL-322`, and where the actual residual is continuous and satisfies `m(Q)->0`. `PL-322` left open whether (PL323-1) forces the desired moving-tail law `Qm(Q)->0`.

It does.

Let `Q_0>0`. Suppose

\[
m\in C([Q_0,\infty);\mathbb C),
\qquad
m(Q)\to0,
\tag{PL323-3}
\]

and suppose `H_{Q_0}m(Q)` exists finitely for every sufficiently large `Q`. If

\[
f(Q):=H_{Q_0}m(Q)+2Qm(Q)\longrightarrow0,
\tag{PL323-4}
\]

then

\[
\boxed{Qm(Q)\longrightarrow0.}
\tag{PL323-5}
\]

Thus the final pointwise gate in `PL-322` is not independent. In the actual completed-Weil endpoint setting, `PL-322` already proves (PL323-4), while `PL-319` records continuity of the state up to the zero boundary trace. Therefore the residual selected in `PL-322` automatically satisfies (PL323-5). Combined with the conditional residual moment already proved there, `PL-321` applies and the moving Green transfer is closed.

No sign assumption is required. The argument works for complex-valued `m` by rotating the phase at a hypothetical maximum.

## 1. The transformed singular remainder is a positive jump operator

Put

\[
k(h)=\frac1{e^h-1},
\qquad
(\mathcal L v)(Q):=H_{Q_0}v(Q)+2Qv(Q).
\tag{PL323-6}
\]

The kernel `k` is positive and symmetric. At a point `Q_*` where a real-valued function `v` attains its global maximum on `[Q_0,\infty)`, every truncated singular integral satisfies

\[
\int_{\substack{P\ge Q_0\\|P-Q_*|>\varepsilon}}
(v(Q_*)-v(P))k(|Q_*-P|)\,dP\ge0.
\tag{PL323-7}
\]

Whenever `H_{Q_0}v(Q_*)` exists finitely, passage to the singular limit therefore gives

\[
H_{Q_0}v(Q_*)\ge0.
\tag{PL323-8}
\]

This is the elementary pointwise maximum principle behind the proof. It is standard nonlocal jump-kernel geometry; source 96 contains the corresponding logarithmic-Laplacian maximum-principle framework. The line-specific ingredient is the growing positive potential `2Q` produced by the exact endpoint source identity.

## 2. An explicit `1/Q` supersolution

Let

\[
p(Q)=\frac1Q.
\tag{PL323-9}
\]

The right-hand part of `H_{Q_0}p(Q)` is nonnegative because `p` is decreasing. The negative left-hand part is

\[
-\int_0^{Q-Q_0}
\frac{h}{Q(Q-h)}\,k(h)\,dh.
\tag{PL323-10}
\]

For `Q>=2Q_0`, split at `h=Q/2`. On `0<h<=Q/2`,

\[
\frac{h}{Q(Q-h)}\le\frac{2h}{Q^2},
\tag{PL323-11}
\]

and

\[
\int_0^\infty h k(h)\,dh
=\frac{\pi^2}{6}.
\tag{PL323-12}
\]

On `Q/2<h<Q-Q_0`, the exponential tail `k(h)\ll e^{-h}` gives a bound `O_{Q_0}(Qe^{-Q/2})`. Hence

\[
H_{Q_0}p(Q)
\ge
-\frac{\pi^2}{3Q^2}
-O_{Q_0}(Qe^{-Q/2}),
\tag{PL323-13}
\]

so

\[
\boxed{
\mathcal Lp(Q)
=H_{Q_0}p(Q)+2
\ge1
}
\tag{PL323-14}
\]

for all sufficiently large `Q`.

This barrier has exactly the scale required by the target conclusion: a source of size `epsilon` can be dominated by `epsilon/Q` after the coercive `2Q` term is included.

## 3. An exponential barrier carries the compact past

Fix any

\[
0<a<1
\tag{PL323-15}
\]

and, for a reference point `R`, set

\[
\phi_R(Q)=e^{-a(Q-R)}.
\tag{PL323-16}
\]

A direct split to the left and right of `Q` gives

\[
\frac{H_{Q_0}\phi_R(Q)}{\phi_R(Q)}
=
\int_0^{Q-Q_0}(1-e^{ah})k(h)\,dh
+
\int_0^\infty(1-e^{-ah})k(h)\,dh.
\tag{PL323-17}
\]

Because `a<1`, both full-line comparison integrals converge. Since the omitted tail from the first integral is negative,

\[
H_{Q_0}\phi_R(Q)
\ge
\lambda_a\phi_R(Q),
\tag{PL323-18}
\]

where

\[
\lambda_a
:=
\int_0^\infty
\bigl(2-e^{ah}-e^{-ah}\bigr)k(h)\,dh
\in(-\infty,0).
\tag{PL323-19}
\]

Consequently

\[
\boxed{
\mathcal L\phi_R(Q)
\ge(2Q+\lambda_a)\phi_R(Q)\ge0
}
\tag{PL323-20}
\]

once `R` is chosen sufficiently large and `Q>=R`.

The role of `\phi_R` is only to dominate arbitrary data on the compact interval `[Q_0,R]`. Its contribution is exponentially invisible after multiplication by `Q` at infinity.

## 4. Tail comparison forces `Qm(Q)->0`

Fix `epsilon>0`. By (PL323-4), choose `R` so large that, for every `Q>=R`,

\[
|f(Q)|\le\epsilon,
\tag{PL323-21}
\]

and so that both (PL323-14) and (PL323-20) hold. Let

\[
B:=\max_{Q_0\le Q\le R}|m(Q)|
\tag{PL323-22}
\]

and define the positive barrier

\[
w(Q)=\frac{\epsilon}{Q}+B\phi_R(Q).
\tag{PL323-23}
\]

For `Q<=R`, `\phi_R(Q)>=1`, hence

\[
w(Q)\ge|m(Q)|.
\tag{PL323-24}
\]

For `Q>=R`,

\[
\mathcal Lw(Q)\ge\epsilon.
\tag{PL323-25}
\]

Suppose, for contradiction, that `|m|-w` is positive somewhere. Since both `m(Q)` and `w(Q)` tend to zero, the positive supremum is attained at some `Q_*>R`. Choose `theta` so that

\[
e^{-i\theta}m(Q_*)=|m(Q_*)|,
\]

and put

\[
v(Q)=\operatorname{Re}(e^{-i\theta}m(Q))-w(Q).
\tag{PL323-26}
\]

For every `Q`,

\[
v(Q)
\le |m(Q)|-w(Q)
\le |m(Q_*)|-w(Q_*)
=v(Q_*),
\tag{PL323-27}
\]

so `v` has a positive global maximum at `Q_*`. By (PL323-8),

\[
H_{Q_0}v(Q_*)\ge0,
\]

and therefore

\[
\mathcal Lv(Q_*)>0.
\tag{PL323-28}
\]

On the other hand, linearity and (PL323-21), (PL323-25) give

\[
\mathcal Lv(Q_*)
=
\operatorname{Re}(e^{-i\theta}f(Q_*))
-\mathcal Lw(Q_*)
\le |f(Q_*)|-\epsilon
\le0,
\tag{PL323-29}
\]

a contradiction. Thus

\[
|m(Q)|
\le
\frac{\epsilon}{Q}
+B e^{-a(Q-R)}
\qquad(Q\ge Q_0).
\tag{PL323-30}
\]

Multiplying by `Q` and taking the upper limit gives

\[
\limsup_{Q\to\infty}Q|m(Q)|\le\epsilon.
\tag{PL323-31}
\]

Because `epsilon>0` was arbitrary, (PL323-5) follows.

The singularity at `P=Q_*` creates no hidden sign problem in this maximum argument. Apply (PL323-7) first to the truncated kernels. The finite pointwise value assumed for `H_{Q_0}m(Q_*)`, together with the explicit smooth barriers, supplies the finite singular limit used in (PL323-28).

## 5. Application to the completed-Weil endpoint branch

`PL-322` starts from the actual source-coupled endpoint profile `g` with

\[
g(Q)=O(Q^{-1/2}),
\qquad
F(Q)\to F_\infty.
\tag{PL323-32}
\]

Its conservative integrated-flux argument produces a unique primitive coefficient `C` and

\[
m(Q)=g(Q)-CQ^{-1/2}
\tag{PL323-33}
\]

with a convergent improper moment. More importantly for the present theorem, `PL-322` derives exactly

\[
2Qm(Q)+H_{Q_0}m(Q)\to0.
\tag{PL323-34}
\]

The state has a continuous zero boundary trace and interior continuity by the logarithmic-Laplacian boundary theory already used in `PL-319`; hence `m` is continuous and tends to zero. In the exact `PL-319`/`PL-322` setting the singular remainder is realized pointwise. Therefore the hypotheses of the comparison theorem above are met, and

\[
\boxed{Qm(Q)\to0.}
\tag{PL323-35}
\]

Together with the conditional moment from `PL-322`, this is precisely the hypothesis set of `PL-321`. Thus for every fixed outer `r>0`,

\[
\boxed{
\mathcal A_s[m](r)
\longrightarrow
 e^{-r}\!\int_0^\infty m(Q)\,dQ
\qquad(s\downarrow0),
}
\tag{PL323-36}
\]

with the integral understood in the conditional improper sense established in `PL-321`--`PL-322` after the harmless compact/tail split.

Accordingly, the endpoint anti-concentration/moving-diagonal problem opened in `PL-314` is closed for the actual source-coupled branch: generic critical-scale profiles can still fail the transfer (`PL-315`--`PL-318`), but the convergent source trace of the completed-Weil eigenstate supplies a coercive equation that rules out those sparse saturating profiles.

## 6. Adversarial and novelty audit

**The maximum principle itself is not new.** Positive-kernel comparison principles are classical, and source 96 already develops weak/strong maximum principles for the logarithmic Laplacian. The durable delta is the line-specific observation that the exact endpoint equation isolated in `PL-322` contains the growing potential `2Q`; the explicit `1/Q` supersolution converts that coercivity into exactly the missing `o(1/Q)` residual law.

**This does not contradict `PL-318`.** Its sparse bump construction has bounded logarithmic-Laplacian forcing but does not satisfy the convergent source-coupled residual equation (PL323-4). The present theorem uses `f(Q)->0` after subtraction of the forced `Q^{-1/2}` profile, not merely `f in L^infty`.

**No sign or positivity of the eigenstate is used.** The phase rotation in (PL323-26) proves the comparison for complex-valued residuals. Thus the closure is not restricted to a ground-state or positive branch.

**Continuity and pointwise realizability are load-bearing.** The proof uses attainment of a positive maximum and the pointwise jump-kernel sign at that maximum. It does not claim the same theorem for an arbitrary distributional solution without a pointwise representative. Those hypotheses are already available in the completed-Weil endpoint setting used by `PL-319`--`PL-322`; weakening them further is unnecessary for the present application.

**The growing coefficient is essential.** Replacing `2Q` by a bounded potential would not give the supersolution (PL323-14) at the `1/Q` scale and would return to the flexibility exposed by `PL-318`. The endpoint geometry is therefore doing real work rather than merely repackaging a generic regularity estimate.

**No RH conclusion follows from this analytic closure alone.** The mechanism is universal endpoint PDE/comparison geometry. It closes the small-order moving-Green transfer needed by the localized Weil construction, but it does not supply the rational-prime-specific scalar compatibility, sign, or first-crossing theorem required downstream to exclude off-critical zeros.

A targeted prior-art audit around nonlocal maximum principles, logarithmic-Laplacian comparison, and Schrödinger-type positive-kernel operators found the comparison principle itself as standard structure, not the particular completed-Weil endpoint consequence. No novelty is claimed for the general maximum principle.

## Consequence for the research line

The endpoint chain `PL-319`--`PL-323` now yields, without an independent residual Sobolev or absolute-integrability hypothesis,

\[
\text{convergent completed-Weil source trace}
+O(Q^{-1/2})\text{ boundary scale}
\Longrightarrow
\text{forced primitive coefficient}
\Longrightarrow
2Qm+Hm\to0
\Longrightarrow
Qm\to0
\Longrightarrow
\text{moving Green transfer}.
\tag{PL323-37}
\]

The analytic moving-diagonal obstruction is therefore no longer the active frontier for the actual branch. Subsequent work should return to the non-universal arithmetic step: whether the transferred rank-one endpoint datum couples to the rational-prime Weil form with a sign/first-crossing constraint strong enough to bear on RH, rather than seeking further ambient endpoint regularity.

## Sources

- `PL-318`: bounded logarithmic forcing permits sparse `1/Q` saturation and is the matched negative control.
- `PL-319`: exact logarithmic-coordinate source identity and continuity/source-trace input for the completed-Weil state.
- `PL-321`: conditional endpoint moments suffice for the moving Green transfer once `Qm(Q)->0`.
- `PL-322`: conservative integrated flux, forced primitive coefficient, conditional residual moment, and the residual equation `2Qm+H_{Q_0}m->0`.
- Source 96 in `research/prime_lattice/SOURCES.md`: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian* (2019), for the singular-integral realization and classical maximum-principle context.
- Source 97 in `research/prime_lattice/SOURCES.md`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian* (2025), for the continuous sharp boundary scale used by the actual endpoint state.