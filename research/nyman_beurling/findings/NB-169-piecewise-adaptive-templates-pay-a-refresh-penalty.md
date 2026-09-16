# NB-169 — Piecewise-adaptive templates pay a refresh penalty for logarithmic Euler rescue

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + MEAN-SQUARE + CAPPED-TRANSPORT + HEIGHT-ADAPTIVE + NB-168-REFINEMENT`.

`NB-168` rules out persistent `q_T log T` arithmetic rescue when one compact signed offset template is translated unchanged through an entire dyadic height block. Its cleanest remaining escape is height adaptation: choose a new signed template after moving to a different part of the block, so that the coefficients can track the local prime phases.

Finite refresh does not remove the mean-square obstruction for free. If the template is allowed to change on `M_T` height intervals, Montgomery--Vaughan can be applied separately on every interval. The diagonal budget adds only with the total interval length, while the weighted off-diagonal tariff `a_T^{-2}` is paid once per refreshed template. This gives a quantitative adaptation law: logarithmic Euler rescue on positive density requires either logarithmic capped transport or enough template refreshes that the cumulative `a_T^{-2}` tariff reaches the `log^2 T` scale.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, and partition

\[
[T,2T]=I_{T,1}\cup\cdots\cup I_{T,M_T}
\]

into disjoint consecutive intervals, with

\[
H_{T,j}:=|I_{T,j}|,
\qquad
\sum_{j=1}^{M_T}H_{T,j}=T.
\]

For each interval let `nu_{T,j}` be a finite real signed Borel measure supported on `[-B,B]`, with zero total mass. The partition and all templates may depend arbitrarily on `T` and may be selected using the arithmetic data in the block; the only restriction is that `nu_{T,j}` is fixed while the center `t` ranges inside `I_{T,j}`.

Write

\[
\nu_{T,j}=\nu_{T,j}^+-\nu_{T,j}^-,
\qquad
\nu_{T,j}^+(\mathbf R)=\nu_{T,j}^-(\mathbf R),
\]

and define the capped Jordan transport

\[
\mathsf T_{T,j}
:=
\inf_{\pi\in\Pi(\nu_{T,j}^+,\nu_{T,j}^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v).
\]

For a positive reference charge `q_T`, put

\[
\Xi_{T,j}:=\frac{\mathsf T_{T,j}}{q_T}.
\]

On `t in I_{T,j}` define

\[
\mathcal E_T(t)
:=
\int
\frac{\zeta'}{\zeta}(1+a_T+i(t+u))
\,d\nu_{T,j}(u).
\]

Then

\[
\boxed{
\int_T^{2T}|\mathcal E_T(t)|^2\,dt
\ll_B
\sum_{j=1}^{M_T}
\mathsf T_{T,j}^2
\left(H_{T,j}+a_T^{-2}\right).
}
\]

Equivalently, define the transport-energy and refresh tariffs

\[
\mathcal A_T
:=
\frac1T\sum_{j=1}^{M_T}\Xi_{T,j}^2H_{T,j},
\qquad
\mathcal R_T
:=
\frac1{Ta_T^2}\sum_{j=1}^{M_T}\Xi_{T,j}^2.
\]

For every fixed `eta>0`,

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:
|\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|
\ll_B
\frac{\mathcal A_T+\mathcal R_T}
{\eta^2(\log T)^2}.
}
\]

Thus

\[
\boxed{
\mathcal A_T+\mathcal R_T=o((\log T)^2)
}
\]

forces logarithmic arithmetic rescue onto a set of relative Lebesgue measure `o(1)` even though the signed template is height-adaptive.

A convenient uniform corollary is obtained when

\[
\Xi_{T,j}\le X_T
\qquad(1\le j\le M_T).
\]

Then

\[
\boxed{
\frac1T
\left|
\left\{t:\ |\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|
\ll_B
\frac{X_T^2}{\eta^2(\log T)^2}
\left(1+\frac{M_T}{Ta_T^2}\right).
}
\]

In particular,

\[
\boxed{
X_T\sqrt{1+\frac{M_T}{Ta_T^2}}
=o(\log T)
}
\]

still rules out positive-density logarithmic rescue.

Conversely, if the rescue set has relative measure at least a fixed `delta>0`, then the preceding upper bound forces

\[
X_T^2
\left(1+\frac{M_T}{Ta_T^2}\right)
\gg_{B,\eta,\delta}
(\log T)^2.
\]

Hence, whenever `X_T=o(log T)`,

\[
\boxed{
M_T
\gg_{B,\eta,\delta}
\frac{Ta_T^2(\log T)^2}{X_T^2}.
}
\]

For bounded capped transport this means that successful height adaptation must refresh on average at spacing at most

\[
\boxed{
\frac{T}{M_T}
\ll_{B,\eta,\delta}
\frac{1}{a_T^2(\log T)^2}.
}
\]

The stationary result `NB-168` is exactly the case `M_T=1`.

## Derivation

### Each refreshed template has the same coefficient budgets

Fix one interval and abbreviate `nu=nu_{T,j}`, `mathsf T=mathsf T_{T,j}`. As in `NB-168`, for

\[
\widehat\nu(\xi)=\int e^{-iu\xi}\,d\nu(u),
\]

coupling the Jordan parts gives

\[
|\widehat\nu(\xi)|
\le
2\mathsf T(1+a_T|\xi|).
\]

The Euler expansion in `Re s>1` therefore writes

\[
\mathcal E_{T,j}(t)
=
-\sum_{n\ge2}b_{n,T,j}n^{-it},
\qquad
b_{n,T,j}
=
\frac{\Lambda(n)}{n^{1+a_T}}
\widehat\nu_{T,j}(\log n).
\]

Exactly the coefficient estimates from `NB-168` apply uniformly in `j`:

\[
\sum_{n\ge2}|b_{n,T,j}|^2
\ll_B
\mathsf T_{T,j}^2,
\]

and

\[
\sum_{n\ge2}n|b_{n,T,j}|^2
\ll_B
\mathsf T_{T,j}^2a_T^{-2}.
\]

The second estimate again follows from `Lambda(n)^2<=Lambda(n) log n` and the derivatives of `-zeta'/zeta` at `1+2a_T`. No stationarity across different intervals is used here.

### Montgomery--Vaughan charges one weighted tariff per interval

Write `I_{T,j}=[A_j,A_j+H_{T,j})`. Translating `t=A_j+v` only replaces each coefficient by `b_{n,T,j}n^{-iA_j}`, which does not change its magnitude. The standard Montgomery--Vaughan mean-value consequence therefore gives, first for finite Dirichlet polynomials and then by `L^2` passage to the absolutely convergent series,

\[
\int_{I_{T,j}}
|\mathcal E_{T,j}(t)|^2dt
\ll
H_{T,j}\sum_n|b_{n,T,j}|^2
+
\sum_n n|b_{n,T,j}|^2.
\]

Hence

\[
\int_{I_{T,j}}
|\mathcal E_{T,j}(t)|^2dt
\ll_B
\mathsf T_{T,j}^2
\left(H_{T,j}+a_T^{-2}\right).
\]

The intervals are disjoint, so these estimates add with no cross-terms. This proves the global piecewise-adaptive bound. Dividing by `q_T^2` and applying Chebyshev at threshold `eta q_T log T` gives the exceptional-set estimate.

The two normalized terms have different meanings. `mathcal A_T` is the ordinary time-averaged squared capped transport. `mathcal R_T` is the adaptation cost: every time a new Dirichlet coefficient sequence is installed, the weighted Montgomery--Vaughan error is paid again. Very short intervals therefore cannot evade the stationary mean-square estimate merely by resetting the template often.

## Transfer to logarithmic zero-packet debt

The completed explicit-formula transfer from `NB-165`--`NB-168` continues interval by interval. If the target architecture produces, at a center `t in I_{T,j}`, a packet of at least `kappa log T` zeros each carrying charge at least `q_T`, defeating the resulting logarithmic adverse debt through the arithmetic-source escape requires a completed conservation remainder of order `q_T log T`.

The Gamma, pole, and reference pieces across a bounded offset support remain

\[
O_B(\mathsf T_{T,j}/T)
=
O_B(q_T\Xi_{T,j}/T).
\]

Under the uniform hypothesis `Xi_{T,j}<=X_T=o(T log T)` these elementary terms are negligible at the rescue scale, so a positive-density source rescue would force a positive-density set on which `|mathcal E_T(t)|` is itself `Omega(q_T log T)`. The claim then imposes the stated adaptation tariff.

This does not assume that the templates are chosen independently of the prime phases. The partition and every `nu_{T,j}` may be designed adversarially after inspecting the whole block. The estimate is deterministic once a template is held fixed on its interval. What it forbids is changing the coefficient sequence at arbitrarily fine resolution without paying for the number of changes.

## Quantitative frontier

The result converts the vague height-adaptive escape of `NB-168` into a rate condition. If `X_T` is bounded and `Ta_T^2 -> infinity`, a bounded number of refreshes is still essentially stationary. More strongly, positive-density rescue requires

\[
\frac{M_T}{T}
\gg
 a_T^2(\log T)^2
\]

up to constants. Thus the relevant adaptation scale is not merely one refresh per dyadic block; it is the much finer spacing

\[
H_{\rm adapt}
\asymp
\frac{1}{a_T^2(\log T)^2}
\]

when capped transport stays bounded.

For example, at a Vinogradov--Korobov-sized exterior width

\[
a_T\asymp
(\log T)^{-2/3}(\log\log T)^{-1/3},
\]

bounded-transport positive-density rescue would require

\[
\frac{M_T}{T}
\gg
\frac{(\log T)^{2/3}}
{(\log\log T)^{2/3}},
\]

so the average template lifetime must be `o(1)` in height. At `a_T asymp 1/log T`, the threshold becomes order-one refreshes per unit height. These are illustrations of the theorem, not assumptions about where an actual target packet exists.

## Adversarial checks and exact boundary

The result is genuinely piecewise-stationary, not fully pointwise. An arbitrary measurable family `nu_{T,t}` with infinitely many changes is not covered. Nor does the theorem prevent a sparse discrete sequence of centers from lying entirely in the exceptional set; as in `NB-168`, converting Lebesgue-density control into exclusion of a zero-selected discrete sequence requires an independent robustness interval or counting bridge.

The `M_T a_T^{-2}` term is not an artifact of summing a crude common bound. On an interval of length `H`, Montgomery--Vaughan naturally gives `H sum|b_n|^2 + sum n|b_n|^2`; refreshing the coefficients destroys any possibility of sharing the second term with neighboring intervals. A stronger theorem for continuously varying coefficients would therefore need additional regularity or variation control, not just a repetition of the stationary estimate.

The theorem also retains the ultra-thin limitation already visible in `NB-168`. When `a_T` is very small, the per-refresh tariff `a_T^{-2}` is large, but the critical count `T a_T^2 log^2 T/X_T^2` can itself become small. The statement records exactly that tradeoff rather than claiming uniform suppression for every exterior width.

Finally, `q_T` is a reference charge, not a claim that a crowded off-critical packet exists. The zero-packet interpretation is conditional on such a packet and its target response, consistently with `NB-165`--`NB-168`.

## Representation audit

The interval-summing principle is not specific to zeta. Any family of Dirichlet series whose coefficient sequence is held fixed on each interval and obeys analogous unweighted and `n`-weighted `ell^2` budgets satisfies the same `time energy + refresh tariff` law. The zeta-specific part is again the von Mangoldt Euler series together with capped-Poisson transport, which turns the two coefficient budgets into `mathsf T^2` and `mathsf T^2 a_T^{-2}`, and the explicit-formula transfer identifying `q_T log T` as the source scale capable of cancelling a logarithmic zero packet.

Thus the finding does not claim a new Montgomery--Vaughan or adaptive large-sieve theorem. Its line-local contribution is to quantify how much of the height-adaptive arithmetic-resonance escape left by `NB-168` survives when the sampler has finite refresh complexity.

## Prior-art audit

The only load-bearing external input remains the Montgomery--Vaughan generalized Hilbert inequality and its standard Dirichlet-polynomial mean-value corollary, already anchored in `research/nyman_beurling/SOURCES.md`. A fresh search also found Ruilin Long and Zhengquan Liu, *Application to Dirichlet Series of Maximal Large Sieve Inequality*, Bull. London Math. Soc. 25 (1993), 105--113, DOI `10.1112/blms/25.2.105`, which develops maximal large-sieve estimates for Dirichlet series. That is neighboring prior art for maximal/adaptive Dirichlet-series control, but it is not needed here and does not supply the capped-transport coefficient budgets or the explicit-formula zero-debt transfer. No new source anchor is therefore required.

## Research consequence

`NB-168` left `height-adaptive arithmetic resonance` as a qualitative escape. This finding separates two versions of it. Finite or subcritical-rate adaptation is still too rigid: its arithmetic rescue is sparse whenever

\[
\mathcal A_T+\mathcal R_T=o((\log T)^2).
\]

To escape with controlled capped transport, the architecture must now do something quantitatively stronger: refresh the signed shape at the critical rate `M_T \gtrsim T a_T^2 log^2 T/X_T^2`, concentrate on a genuinely sparse exceptional sequence, or use a continuously height-dependent control whose variation is not captured by a finite-refresh model. The next natural question is whether a bounded-variation or entropy-controlled family `t -> nu_{T,t}` can be reduced to the present stepwise theorem without losing the logarithmic threshold.