# NB-171 — Finite p-variation height adaptation pays a power refresh tariff

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + P-VARIATION + ORDERED-ENTROPY + CAPPED-TRANSPORT + HEIGHT-ADAPTIVE + NB-170-REFINEMENT`.

`NB-170` shows that bounded total variation in the capped Poisson metric is enough to compress a continuously varying signed sampler into finitely many source-distinguishable templates. Its explicit remaining escape is very large or infinite total variation. Total variation, however, is only the first member of a larger regularity hierarchy. A path may have infinite `1`-variation while still having finite `p`-variation for some `p>1`, and such a path still cannot install a genuinely new arithmetic template at every height for free.

The useful invariant is the number of **ordered source-resolution templates** needed along the height axis. Finite `p`-variation bounds that number by a power law. Combining this elementary path-complexity fact with the piecewise-stationary Montgomery--Vaughan tariff from `NB-169` extends the arithmetic-rescue obstruction strictly beyond bounded variation. In particular, Hölder paths of exponent below one may have infinite total variation and are nevertheless covered quantitatively.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, and for every `t in [T,2T]` let `nu_{T,t}` be a finite real signed Borel measure supported on `[-B,B]` with zero total mass. Let `q_T>0` be a reference target charge. For zero-mass signed measures define, as in `NB-167`--`NB-170`,

\[
\mathsf D_{a_T}(\sigma)
:=
\inf_{\pi\in\Pi(\sigma^+,\sigma^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v),
\]

and the normalized capped metric

\[
\rho_T(\nu,\widetilde\nu)
:=
\frac{\mathsf D_{a_T}(\nu-\widetilde\nu)}{q_T}.
\]

The Kantorovich--Rubinstein representation from `NB-167` makes `rho_T` a norm metric on zero-mass signed measures. Put

\[
X_T
:=
\sup_{t\in[T,2T]}
\rho_T(\nu_{T,t},0),
\qquad
H_T
:=
\min\left\{
\frac1{a_T},
\frac{\log T}{\log\log T}
\right\},
\]

and define the genuinely adaptive Euler response

\[
\mathcal E_T(t)
:=
\int
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr)
\,d\nu_{T,t}(u).
\]

For `epsilon>0`, let `M_T(epsilon)` be the least integer `M`, if finite, for which `[T,2T]` admits a partition into `M` consecutive half-open intervals `I_1,...,I_M` and representatives `mu_j` chosen from the actual family on `I_j` such that

\[
\sup_{t\in I_j}
\rho_T(\nu_{T,t},\mu_j)
\le \epsilon
\qquad(1\le j\le M).
\]

Call this the ordered template number at resolution `epsilon`. Then for every fixed `eta>0` there is a constant `c_{B,eta}>0` such that, with

\[
\epsilon_T
:=
c_{B,\eta}\frac{\log T}{H_T},
\]

one has

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:
|\mathcal E_T(t)|\ge
\eta q_T\log T
\right\}
\right|
\ll_{B,\eta}
\frac{X_T^2}{(\log T)^2}
\left(
1+
\frac{M_T(\epsilon_T)}{Ta_T^2}
\right).
}
\]

This statement itself assumes no bounded variation. It only asks how many consecutive source-resolution pieces the adaptive family really has.

Now fix `p>=1` and define its normalized capped `p`-variation by

\[
\mathcal V_{p,T}
:=
\left(
\sup_{T=t_0<\cdots<t_m=2T}
\sum_{j=1}^{m}
\rho_T
\bigl(\nu_{T,t_j},\nu_{T,t_{j-1}}\bigr)^p
\right)^{1/p}.
\]

If `mathcal V_{p,T}<infinity`, then, up to an absolute change in the resolution constant,

\[
\boxed{
M_T(\epsilon)
\ll
1+
\left(
\frac{\mathcal V_{p,T}}{\epsilon}
\right)^p.
}
\]

Consequently

\[
\boxed{
\frac1T
\left|
\left\{t:
|\mathcal E_T(t)|\ge
\eta q_T\log T
\right\}
\right|
\ll_{B,\eta,p}
\frac{X_T^2}{(\log T)^2}
\left[
1+
\frac1{Ta_T^2}
+
\frac1{Ta_T^2}
\left(
\frac{\mathcal V_{p,T}H_T}{\log T}
\right)^p
\right].
}
\]

Thus finite `p`-variation is enough to make logarithmic arithmetic rescue sparse whenever

\[
\boxed{
X_T^2
\left[
1+
\frac1{Ta_T^2}
+
\frac1{Ta_T^2}
\left(
\frac{\mathcal V_{p,T}H_T}{\log T}
\right)^p
\right]
=o((\log T)^2).
}
\]

Conversely, suppose the rescue set has relative measure at least a fixed `delta>0` and the stationary baseline is subcritical,

\[
X_T^2
\left(1+\frac1{Ta_T^2}\right)
=o((\log T)^2).
\]

Then every finite-`p`-variation realization must satisfy

\[
\boxed{
\mathcal V_{p,T}
\gg_{B,\eta,\delta,p}
\frac{\log T}{H_T}
\left(
\frac{Ta_T^2(\log T)^2}{X_T^2}
\right)^{1/p}.
}
\]

The case `p=1` recovers the `NB-170` bounded-variation tariff, while every `p>1` genuinely allows paths with infinite total variation.

## Ordered source resolution is the real refresh count

For fixed center height `t`, put

\[
f_{T,t}(u)
:=
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr).
\]

The high-ordinate bounds already used in `NB-165`--`NB-170` give, uniformly for `t in [T,2T]` and `|u|<=B`,

\[
\|f_{T,t}\|_\infty\ll_B H_T,
\qquad
\operatorname{Lip}(f_{T,t})
\ll_B \frac{H_T}{a_T}.
\]

Hence the capped Kantorovich--Rubinstein duality gives

\[
\left|
\int f_{T,t}\,d(\nu-\widetilde\nu)
\right|
\ll_B
q_TH_T\rho_T(\nu,\widetilde\nu).
\]

Choose the constant in `epsilon_T` small enough that this is at most `(eta/2)q_T log T` whenever `rho_T(nu,widetilde nu)<=epsilon_T`.

Take an ordered `epsilon_T` approximation with `M=M_T(epsilon_T)` cells and representatives `mu_j`. Define the step response

\[
\widetilde{\mathcal E}_T(t)
:=
\int
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr)
\,d\mu_j(u),
\qquad t\in I_j.
\]

Then

\[
|\mathcal E_T(t)-\widetilde{\mathcal E}_T(t)|
\le
\frac\eta2 q_T\log T,
\]

so logarithmic rescue by the true adaptive path implies rescue at threshold `eta/2` by the step family. Because every representative is an actual member of the family,

\[
\frac{\mathsf D_{a_T}(\mu_j)}{q_T}
\le X_T.
\]

The uniform corollary of `NB-169` therefore applies directly and gives

\[
\frac1T
|\{t:|\widetilde{\mathcal E}_T(t)|\ge(\eta/2)q_T\log T\}|
\ll_{B,\eta}
\frac{X_T^2}{(\log T)^2}
\left(1+\frac{M}{Ta_T^2}\right),
\]

which proves the ordered-template estimate.

The important point is that literal continuity, the number of pointwise changes, and total variation are not themselves the complexity seen by the source. What matters is how often the path moves far enough in capped transport to become distinguishable at the `q_T log T` rescue scale.

## Finite p-variation gives a power law for source-distinguishable refreshes

Let a path have finite `p`-variation `mathcal V_{p,T}`. At a fixed resolution `epsilon`, start from the current template and keep it as the representative until the path first exits its `rho_T`-ball of radius `epsilon`; then refresh the representative and continue. Finite `p`-variation implies the usual regulated representative after changing endpoint values if necessary, and endpoints do not affect the density statement.

Every genuine refresh contributes an increment of size at least `epsilon` between two successive selected path values. If there are `M-1` refreshes, those selected times form an admissible partition, hence

\[
(M-1)\epsilon^p
\le
\mathcal V_{p,T}^p.
\]

Allowing an inessential factor in the covering radius to handle a jump exactly at a cell boundary gives

\[
M_T(2\epsilon)
\le
1+
\left(\frac{\mathcal V_{p,T}}{\epsilon}\right)^p.
\]

Replacing `epsilon` by a constant multiple of the source resolution proves the `p`-variation estimate in the claim.

For `p=1`, this is exactly the counting mechanism hidden inside `NB-170`: total path length divided by source resolution bounds the number of effective refreshes. For `p>1`, the same argument charges only the `p`th power of each refresh. A path may therefore accumulate infinite ordinary variation through ever smaller oscillations and still have finite `p`-variation; those sub-resolution oscillations do not create unlimited arithmetic freedom.

## Hölder controls are a concrete infinite-variation corollary

Suppose, for some `0<alpha<=1`, the family is Hölder in normalized block height:

\[
\rho_T(\nu_{T,t},\nu_{T,s})
\le
L_T
\left(\frac{|t-s|}{T}\right)^\alpha.
\]

With `p=1/alpha`, every partition satisfies

\[
\sum_j
\rho_T
\bigl(\nu_{T,t_j},\nu_{T,t_{j-1}}\bigr)^p
\le
L_T^p
\sum_j\frac{t_j-t_{j-1}}T
=L_T^p,
\]

so

\[
\mathcal V_{1/\alpha,T}\le L_T.
\]

Therefore

\[
\boxed{
\frac1T
|\{t:|\mathcal E_T(t)|\ge\eta q_T\log T\}|
\ll_{B,\eta,\alpha}
\frac{X_T^2}{(\log T)^2}
\left[
1+
\frac1{Ta_T^2}
+
\frac1{Ta_T^2}
\left(
\frac{L_TH_T}{\log T}
\right)^{1/\alpha}
\right].
}
\]

Under the same subcritical stationary baseline, positive-density rescue forces

\[
\boxed{
L_T
\gg
\frac{\log T}{H_T}
\left(
\frac{Ta_T^2(\log T)^2}{X_T^2}
\right)^\alpha.
}
\]

This is a genuine extension beyond bounded variation. For every `alpha<1`, an `alpha`-Hölder path may have infinite total variation, but that fact alone does not provide enough adaptation: its Hölder constant must still grow at the displayed source-resolution rate.

In the common high-ordinate regime

\[
H_T=\frac{\log T}{\log\log T},
\]

the `p`-variation lower bound becomes

\[
\boxed{
\mathcal V_{p,T}
\gg
\log\log T
\left(
\frac{Ta_T^2(\log T)^2}{X_T^2}
\right)^{1/p}.
}
\]

Thus the escape left by `NB-170` is not merely `infinite total variation`. Successful adaptation must be rough enough at the specific Poisson/source resolution relevant to the logarithmic Euler defect.

## Transfer to zero-packet debt

The completed explicit-formula interpretation from `NB-165`--`NB-170` is unchanged. If, at a center `t`, a target architecture produces at least `kappa log T` zeros carrying charge at least `q_T`, cancelling the corresponding adverse debt through the arithmetic-source escape requires a completed remainder of order `q_T log T`.

On bounded offset support, the Gamma, pole and reference terms for a representative template remain `O_B(q_TX_T/T)` under the same hypotheses as in `NB-168`--`NB-170`, and replacing the true template by a source-resolution representative changes the Euler term by at most a fixed fraction of `q_T log T`. Therefore the ordered-template and `p`-variation bounds transfer to the same positive-density zero-packet rescue question.

As before, this is conditional on the target packet and does not turn a Lebesgue-density statement into exclusion of an arbitrarily selected sparse sequence of zero heights.

## Adversarial checks and exact boundary

The theorem does not claim a new variational Montgomery--Vaughan inequality. The only arithmetic mean-square input is still the stationary/template-wise estimate of `NB-168` as assembled interval by interval in `NB-169`. The new step is a deterministic source-resolution compression of a rough path before that theorem is applied.

Finite `p`-variation for one fixed `p` is a real restriction. The result remains silent for a path whose capped transport has infinite `p`-variation for every finite `p`, or whose `p`-variation grows at or above the displayed critical rate. Such a family can refresh on ever finer height scales and is the natural next regularity boundary.

The ultra-thin limitation also remains. When `Ta_T^2` is too small, the per-template Montgomery--Vaughan error dominates and the converse lower bound may cease to be informative. At the logarithmic and Vinogradov--Korobov exterior widths motivating `NB-165`--`NB-170`, `Ta_T^2` is instead very large.

If `X_TH_T=o(log T)`, the pointwise bounded-Lipschitz estimate of `NB-167` is already stronger and no adaptation theorem is needed. The present result matters in the intermediate regime where an individual template can have enough instantaneous source amplitude to reach logarithmic scale, but doing so persistently requires genuine height-dependent roughness.

## Representation and prior-art audit

The `p`-variation notion itself is classical and generic; no novelty is claimed for it or for the elementary fact that an `epsilon`-refresh sequence has length at most `O((V_p/epsilon)^p)`. Variation-norm methods also occur broadly in harmonic analysis and rough-path theory. A fresh prior-art search did not locate a theorem coupling finite `p`-variation of **time-dependent Dirichlet coefficient templates** to the Montgomery--Vaughan weighted error in this capped-transport setting.

The closest Dirichlet-series literature remains the maximal large-sieve direction noted in `NB-169`; searches for `p`-variation/Dirichlet-polynomial results instead returned classical variation theory or unrelated Fourier variation-norm estimates. No such result is load-bearing here. The load-bearing arithmetic source is still the Montgomery--Vaughan Hilbert/mean-value inequality already anchored in `research/nyman_beurling/SOURCES.md`, together with the high-ordinate `zeta'/zeta` bound already anchored for `NB-165`. No new source anchor is required.

The line-specific content is the three-step transfer

\[
\text{capped }p\text{-variation}
\Longrightarrow
\text{ordered source-resolution refresh count}
\Longrightarrow
\text{adaptive Euler mean-square tariff},
\]

and the resulting quantitative obstruction to positive-density cancellation of logarithmic zero-packet debt.

## Research consequence

`NB-168` treats one stationary template, `NB-169` finitely many literal refreshes, and `NB-170` arbitrary bounded-total-variation motion. The present result extends that chain to every finite `p`-variation class. In particular, **infinite total variation is no longer by itself an escape**: Hölder and other rough paths can have infinite `1`-variation while remaining quantitatively compressible at the source resolution.

The compact source-side frontier is therefore narrower. With sublogarithmic instantaneous capped transport, persistent arithmetic rescue now requires one of the following genuinely stronger mechanisms: `p`-variation at least at the displayed critical scale for every regularity exponent available to the family; a path rough enough to have infinite finite-`p` variation; concentration on a genuinely sparse exceptional sequence; or a source-specific selection law whose effective templates evade interval compression at the Poisson resolution. A natural next step is to replace ordered regularity by range metric entropy, which could still control highly discontinuous or temporally scrambled selectors whose set of available shapes is small.