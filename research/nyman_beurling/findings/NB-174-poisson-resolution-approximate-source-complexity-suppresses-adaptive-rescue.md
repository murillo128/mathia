# NB-174 — Poisson-resolution approximate source complexity suppresses adaptive rescue

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + APPROXIMATE-LINEAR-COMPLEXITY + CAPPED-TRANSPORT + ARBITRARY-ADAPTATION + NB-172/NB-173-UNIFICATION`.

`NB-172` controls an arbitrarily rough adaptive sampler by covering its whole range with finitely many stationary templates. `NB-173` gives a stronger vector bound when the range lies **exactly** in a low-complexity stationary linear span. Exact span membership is too brittle for the scale actually seen by the source: `NB-167` already shows that `zeta'/zeta` cannot distinguish two compact signed templates whose capped Poisson transport separation is much smaller than `log T/H_T`, where

\[
H_T:=\min\left\{\frac1{a_T},\frac{\log T}{\log\log T}\right\}.
\]

The correct linear currency is therefore approximate rather than exact. A template family only needs to lie within one source-resolution neighborhood of a low-complexity stationary span. The residual is then pointwise invisible at the logarithmic rescue scale, while the low-dimensional core is controlled by the stationary mean-square theorem of `NB-168`.

This produces one quantity that contains both previous unordered compressions. At tolerance zero it is the exact linear source complexity of `NB-173`; at positive tolerance it is bounded above by the `NB-172` covering tariff. Consequently, small metric entropy cannot coexist with large **approximate** linear complexity at the same capped-Poisson resolution, although low approximate linear complexity can still coexist with very large metric entropy.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, let `q_T>0`, and for every `t in [T,2T]` let `nu_{T,t}` be a finite real signed Borel measure supported on `[-B,B]` with zero total mass. For any zero-mass finite signed measure `sigma`, write

\[
\mathsf D_{a_T}(\sigma)
:=
\inf_{\pi\in\Pi(\sigma^+,\sigma^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v),
\]

and define

\[
H_T
:=
\min\left\{\frac1{a_T},\frac{\log T}{\log\log T}\right\},
\qquad
X_T
:=
\sup_{t\in[T,2T]}
\frac{\mathsf D_{a_T}(\nu_{T,t})}{q_T}.
\]

The genuinely adaptive arithmetic response is

\[
\mathcal E_T(t)
:=
\int
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr)
\,d\nu_{T,t}(u).
\]

For `epsilon>=0`, define the **epsilon-approximate linear source complexity** `mathfrak L_T(epsilon)` as the infimum of `mY^2` over all finite stationary dictionaries

\[
\tau_{1,T},\ldots,\tau_{m,T}
\]

of zero-mass signed measures supported on `[-B,B]`, coefficient functions `beta_{j,T}(t)`, and residuals `r_{T,t}` such that

\[
\mathsf D_{a_T}(\tau_{j,T})\le q_T,
\tag{1}
\]

\[
\nu_{T,t}
=
\sum_{j=1}^{m}\beta_{j,T}(t)\tau_{j,T}
+r_{T,t},
\tag{2}
\]

\[
\sup_{t\in[T,2T]}
\sum_{j=1}^{m}|\beta_{j,T}(t)|^2
\le Y^2,
\tag{3}
\]

and

\[
\sup_{t\in[T,2T]}
\frac{\mathsf D_{a_T}(r_{T,t})}{q_T}
\le\epsilon.
\tag{4}
\]

No regularity or measurability of the coefficient or residual selections is required. If no finite representation exists, set `mathfrak L_T(epsilon)=infinity`.

There is a constant `C_B>0` such that for every fixed `eta>0` and every `epsilon>=0` satisfying

\[
\Lambda_T(\epsilon)
:=
\eta\log T-C_B\epsilon H_T
>0,
\tag{5}
\]

one has

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:
|\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|^*
\ll_B
\frac{\mathfrak L_T(\epsilon)}{\Lambda_T(\epsilon)^2}
\left(1+\frac1{Ta_T^2}\right).
}
\tag{6}
\]

Here `|.|^*` is Lebesgue outer measure. In particular, if

\[
\epsilon_T
\le
\frac{\eta}{2C_B}\frac{\log T}{H_T},
\tag{7}
\]

then

\[
\boxed{
\frac1T
\left|
\left\{t:
|\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|^*
\ll_{B,\eta}
\frac{\mathfrak L_T(\epsilon_T)}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
}
\tag{8}
\]

Thus positive-density logarithmic rescue forces large linear source complexity **after quotienting out all template motion below the source's own capped-Poisson resolution**. In the natural regime `Ta_T^2 -> infinity`, any family satisfying

\[
\mathfrak L_T(\epsilon_T)=o((\log T)^2)
\]

at a fixed small multiple of `log T/H_T` has rescue density `o(1)`.

## Derivation

For fixed `t`, put

\[
f_{T,t}(u)
:=
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr).
\]

The high-ordinate bound and analyticity estimate already assembled in `NB-165`--`NB-167` give uniformly for `t in [T,2T]` and `|u|<=B`

\[
\|f_{T,t}\|_\infty\ll_B H_T,
\qquad
\operatorname{Lip}(f_{T,t})
\ll_B\frac{H_T}{a_T}.
\]

The capped Kantorovich--Rubinstein estimate of `NB-167` therefore gives one `C_B` such that every residual obeying (4) satisfies pointwise

\[
\left|
\int f_{T,t}\,dr_{T,t}
\right|
\le
C_B q_T\epsilon H_T.
\tag{9}
\]

For an admissible dictionary define the stationary responses

\[
\mathcal E_{j,T}(t)
:=
\int f_{T,t}(u)\,d\tau_{j,T}(u).
\]

By (2),

\[
\mathcal E_T(t)
=
\sum_{j=1}^{m}\beta_{j,T}(t)\mathcal E_{j,T}(t)
+
\int f_{T,t}\,dr_{T,t}.
\tag{10}
\]

If the left side has magnitude at least `eta q_T log T`, (9) and (5) force

\[
\left|
\sum_{j=1}^{m}\beta_{j,T}(t)\mathcal E_{j,T}(t)
\right|
\ge
q_T\Lambda_T(\epsilon).
\tag{11}
\]

Pointwise Cauchy--Schwarz and (3) give

\[
\left|
\sum_{j=1}^{m}\beta_{j,T}(t)\mathcal E_{j,T}(t)
\right|^2
\le
Y^2\sum_{j=1}^{m}|\mathcal E_{j,T}(t)|^2.
\tag{12}
\]

Every dictionary direction is stationary and normalized by (1), so `NB-168` gives

\[
\int_T^{2T}|\mathcal E_{j,T}(t)|^2\,dt
\ll_B
q_T^2\left(T+a_T^{-2}\right).
\tag{13}
\]

Summing (13) and applying Markov to the measurable quantity on the right of (12), the rescue set is contained in a measurable set of size

\[
\ll_B
\frac{mY^2}{\Lambda_T(\epsilon)^2}
\left(T+a_T^{-2}\right).
\]

This containment remains valid even if `t -> beta_T(t)` and `t -> r_{T,t}` are nonmeasurable. Dividing by `T` and taking the infimum over all admissible approximate representations proves (6). Equation (8) follows from (7).

The argument uses the two previous mechanisms at exactly their natural scales: `NB-167` removes the unresolved residual pointwise, while `NB-168` controls the stationary linear core in mean square. No additional regularity of the adaptive rule is introduced.

## Exact rank and range entropy are two boundary cases

At zero tolerance,

\[
\boxed{
\mathfrak L_T(0)=\mathfrak L_T,
}
\tag{14}
\]

where `mathfrak L_T` is the exact linear source complexity of `NB-173`. Indeed `mathsf D_{a_T}(r)=0` forces the zero signed measure, so (2)--(4) reduce to the exact representation there. Hence `NB-173` is the `epsilon=0` endpoint of (6).

At positive tolerance, let `mathcal N_T(epsilon)` be the internal covering number of `NB-172` for the normalized metric

\[
\rho_T(\nu,\mu)
:=
\frac{\mathsf D_{a_T}(\nu-\mu)}{q_T}.
\]

If `X_T>0`, choose an internal `epsilon`-cover with centers `mu_1,...,mu_K` from the actual range and set

\[
\tau_j:=\frac{\mu_j}{X_T}.
\]

Then `mathsf D_{a_T}(tau_j)<=q_T`. For each family value choose any nearby center and use the one-hot coefficient vector with its active coefficient equal to `X_T`; the uncovered difference is an admissible residual of normalized transport at most `epsilon`. Therefore

\[
\boxed{
\mathfrak L_T(\epsilon)
\le
\mathcal N_T(\epsilon)X_T^2.
}
\tag{15}
\]

The case `X_T=0` is trivial. Taking `epsilon` to be the `NB-172` source resolution in (8), (15) recovers the entropy bound of `NB-172` up to the same fixed constants.

Thus the apparent competition between `NB-172` and `NB-173` has a one-sided resolution at the scale relevant to the source:

- small range entropy always gives small approximate linear complexity at the same tolerance;
- small approximate linear complexity does **not** force small range entropy, because a continuum may fill a long or high-dimensional region inside one well-conditioned low-rank span.

The rank-one amplitude family already used in `NB-173` is the simplest example of the second direction.

## Approximate complexity still dominates unresolved amplitude

The approximate quantity cannot become small merely by hiding a large individual sampler in the residual. For any admissible representation, the triangle inequality and homogeneity of capped transport give

\[
\frac{\mathsf D_{a_T}(\nu_{T,t})}{q_T}
\le
\sum_{j=1}^{m}|\beta_{j,T}(t)|+\epsilon
\le
\sqrt m\,Y+\epsilon.
\]

Taking the supremum over `t` and then the infimum over representations yields

\[
\boxed{
(X_T-\epsilon)_+^2
\le
\mathfrak L_T(\epsilon).
}
\tag{16}
\]

So (6) does not evade the pointwise amplitude currency of `NB-167`; it isolates the additional stable linear repertoire required after an `epsilon`-sized unresolved component is removed.

Equations (15)--(16) place the new quantity between two already established currencies:

\[
(X_T-\epsilon)_+^2
\le
\mathfrak L_T(\epsilon)
\le
\mathcal N_T(\epsilon)X_T^2.
\tag{17}
\]

This relation is exact at the level needed here and does not require a general entropy-width theorem.

## Source-resolution consequence

In the high-ordinate regime

\[
H_T=\frac{\log T}{\log\log T},
\]

the source tolerance in (7) is of order

\[
\epsilon_T\asymp_{B,\eta}\log\log T.
\]

This looks large only because `epsilon` is measured in units of the target charge `q_T`: `NB-167` says that the corresponding residual can still alter the Euler response by only a fixed fraction of `q_T log T`. A nonlinear adaptive architecture may therefore generate a huge exact catalogue of templates and even have infinite exact linear rank while remaining harmless if that catalogue stays within source resolution of a low-complexity stationary span.

Conversely, if logarithmic rescue occurs on a set of relative outer measure at least a fixed `delta>0`, then every approximate representation satisfying (7) must obey

\[
\boxed{
\mathfrak L_T(\epsilon_T)
\gg_{B,\eta,\delta}
\frac{(\log T)^2}
{1+(Ta_T^2)^{-1}}.
}
\tag{18}
\]

So a concise nonlinear arithmetic rule is not an escape merely because its image has large exact rank or large covering number at microscopic scales. It must generate large stable source complexity at the **specific resolution consumed by `zeta'/zeta`**, or concentrate rescue on a sparse exceptional set, or enter the same ultra-thin `a_T\lesssim T^{-1/2}` regime left open by `NB-168`.

## Adversarial checks and exact boundary

The theorem does not assert that `mathfrak L_T(epsilon)` is a canonical Kolmogorov width or dimension. Classical `n`-width and reduced-basis theory studies approximation of compact sets by low-dimensional subspaces, while (1)--(4) additionally price the conditioning of a normalized dictionary through the worst coefficient `ell^2` energy. That coefficient cost is essential to the vector mean-square step.

The tolerance cannot be chosen arbitrarily. Once `C_B epsilon H_T` reaches `eta log T`, the residual alone may carry the entire rescue scale, and (6) correctly becomes vacuous. No conclusion is claimed beyond that source-resolution boundary.

The factor `1+(Ta_T^2)^{-1}` is inherited unchanged from `NB-168`. This result does not improve the ultra-thin exterior regime where the weighted Montgomery--Vaughan term is already expensive for a single stationary direction.

The conclusion remains a density obstruction. It does not exclude a deliberately selected zero-density or discrete sequence of exceptional heights, and it does not by itself bridge source persistence back to global Nyman approximation.

Finally, the bound is one-sided. Large `mathfrak L_T(epsilon)` is necessary for positive-density rescue under the stated regime, not sufficient: stationary source responses may be strongly correlated or arithmetically ineffective even when the template range is geometrically complicated.

## Representation and prior-art audit

Approximation of compact sets by low-dimensional subspaces is classical under Kolmogorov `n`-widths and reduced-basis theory; relations between metric entropy, convex approximation and width-type quantities are also classical. Representative boundaries include Bernd Carl, Ioanna Kyrezi and Alain Pajor, *Metric Entropy of Convex Hulls in Banach Spaces*, J. London Math. Soc. 60 (1999), 871--896, DOI `10.1112/S0024610799008005`, and the modern reduced-basis/width literature. No novelty is claimed for approximate low-rank representation or for entropy-versus-width ideas in functional analysis.

A targeted search did not reveal the source-specific statement used here: approximation of height-adaptive compact signed exterior-zeta samplers in the capped Jordan transport geometry, at the resolution `log T/H_T` selected by the high-ordinate logarithmic derivative, followed by a stationary Montgomery--Vaughan mean-square transfer to logarithmic zero-packet conservation debt. The load-bearing analytic inputs remain exactly those already persisted in `NB-167` and `NB-168`; no new external theorem is used, so `SOURCES.md` need not change.

## Research consequence

`NB-172` and `NB-173` are now two endpoints of one source-resolution compression principle. The relevant question is not whether the adaptive family has many exact shapes or even infinite exact linear rank. It is whether, after ignoring capped-transport differences too small for `zeta'/zeta` to matter at the `q_T log T` scale, the remaining family still requires a large well-conditioned stationary linear repertoire.

This narrows the surviving compact-support escape. A positive-density arithmetic rescue must have large `mathfrak L_T(epsilon_T)` at `epsilon_T` of order `log T/H_T`, or exploit the sparse-height/ultra-thin exceptions already identified. In particular, microscopic entropy and exact-rank explosions are not by themselves source complexity. Any future source-natural nonlinear mechanism should be tested against its **approximate** capped-Poisson linear complexity at the actual source resolution rather than against exact rank or raw catalogue size.