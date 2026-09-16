# NB-172 — Small template entropy suppresses arbitrarily rough height adaptation

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + METRIC-ENTROPY + UNORDERED-ADAPTATION + CAPPED-TRANSPORT + NB-171-REFINEMENT`.

`NB-168` suppresses logarithmic Euler rescue for one block-stationary compact signed template. `NB-169`--`NB-171` allow height adaptation but control it through ordered refreshes, bounded variation, or finite `p`-variation. Their explicit regularity escape is a path so rough that it can have infinite `p`-variation for every finite `p`.

That escape is still too broad. Temporal roughness and geometric repertoire are different resources. A sampler may switch infinitely often, or with infinite `p`-variation for every `p`, while repeatedly choosing from only a small set of Poisson-resolution shapes. Such switching does not create a new arithmetic source direction each time. A finite cover of the *range* of templates is enough to reduce arbitrary height dependence to finitely many stationary exceptional sets, with no continuity, variation, or interval-partition assumption.

The resulting tariff is different from the ordered tariff of `NB-171`: range entropy multiplies the whole stationary mean-square budget, whereas ordered regularity shares the main `T`-term and pays only for refresh boundaries. Neither dominates the other in general. The new result closes the specific escape of arbitrarily violent switching among a small repertoire.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, and for every `t in [T,2T]` let `nu_{T,t}` be a finite real signed Borel measure supported on `[-B,B]` with zero total mass. Let `q_T>0` be a reference target charge. For zero-mass signed measures define the normalized capped Poisson transport metric from `NB-167`--`NB-171`,

\[
\rho_T(\nu,\mu)
:=
\frac{\mathsf D_{a_T}(\nu-\mu)}{q_T},
\]

where

\[
\mathsf D_{a_T}(\sigma)
:=
\inf_{\pi\in\Pi(\sigma^+,\sigma^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v).
\]

Put

\[
X_T
:=
\sup_{t\in[T,2T]}
\rho_T(\nu_{T,t},0),
\qquad
H_T
:=
\min\left\{\frac1{a_T},\frac{\log T}{\log\log T}\right\},
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

Let

\[
\mathcal R_T:=\{\nu_{T,t}:T\le t\le2T\}
\]

be the range of available shapes. For `epsilon>0`, define the internal covering number `mathcal N_T(epsilon)` as the least integer `K` for which there exist actual family values

\[
\mu_1,\ldots,\mu_K\in\mathcal R_T
\]

such that

\[
\mathcal R_T
\subseteq
\bigcup_{j=1}^K
\{\nu:\rho_T(\nu,\mu_j)\le\epsilon\}.
\]

If no finite cover exists, set `mathcal N_T(epsilon)=infinity`.

For every fixed `eta>0`, there is `c_{B,eta}>0` such that with

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
|\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|^*
\ll_{B,\eta}
\frac{\mathcal N_T(\epsilon_T)X_T^2}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
}
\tag{1}
\]

Here `|.|^*` denotes Lebesgue outer measure, so no measurability or path regularity is required. For a measurable family it is ordinary Lebesgue measure.

Consequently, logarithmic arithmetic rescue is confined to relative outer measure `o(1)` whenever

\[
\boxed{
\mathcal N_T(\epsilon_T)X_T^2
\left(1+\frac1{Ta_T^2}\right)
=o((\log T)^2).
}
\tag{2}
\]

Conversely, if the rescue set has relative outer measure at least a fixed `delta>0`, every finite cover at source resolution satisfies

\[
\boxed{
\mathcal N_T(\epsilon_T)
\gg_{B,\eta,\delta}
\frac{(\log T)^2}
{X_T^2\left(1+(Ta_T^2)^{-1}\right)}.
}
\tag{3}
\]

Thus positive-density rescue requires either near-logarithmic instantaneous capped transport or a large number of geometrically distinct source-resolution templates. Infinite temporal roughness by itself is not enough.

## Derivation

For fixed center height `t`, put

\[
f_{T,t}(u)
:=
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr).
\]

The high-ordinate estimates already assembled in `NB-165`--`NB-171` give uniformly on `t in [T,2T]` and `|u|<=B`

\[
\|f_{T,t}\|_\infty\ll_B H_T,
\qquad
\operatorname{Lip}(f_{T,t})
\ll_B\frac{H_T}{a_T}.
\]

The capped Kantorovich--Rubinstein estimate of `NB-167` therefore supplies a constant `C_B` such that for any two zero-mass templates

\[
\left|
\int f_{T,t}\,d(\nu-\mu)
\right|
\le
C_B q_TH_T\rho_T(\nu,\mu).
\tag{4}
\]

Choose

\[
c_{B,\eta}=\frac{\eta}{2C_B}.
\]

Suppose `mathcal N_T(epsilon_T)=K<infinity`, and choose an internal cover `mu_1,...,mu_K`. For every `t` there is at least one `j` with

\[
\rho_T(\nu_{T,t},\mu_j)\le\epsilon_T.
\]

Define the stationary response of that fixed cover center by

\[
\mathcal E_{T,j}^{\rm stat}(t)
:=
\int
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr)
\,d\mu_j(u).
\]

Equation (4) gives

\[
|\mathcal E_T(t)-\mathcal E_{T,j}^{\rm stat}(t)|
\le
\frac\eta2 q_T\log T.
\]

Hence pointwise

\[
\{t:|\mathcal E_T(t)|\ge\eta q_T\log T\}
\subseteq
\bigcup_{j=1}^K
\left\{t:
|\mathcal E_{T,j}^{\rm stat}(t)|
\ge\frac\eta2q_T\log T
\right\}.
\tag{5}
\]

No assignment `t -> j(t)` has to be measurable and no interval decomposition is used. This is exactly why arbitrary switching is admissible.

Because each `mu_j` is an actual family value,

\[
\frac{\mathsf D_{a_T}(\mu_j)}{q_T}
\le X_T.
\]

`NB-168` applies to every fixed `mu_j` on the full dyadic block and yields

\[
\frac1T
\left|
\left\{t:
|\mathcal E_{T,j}^{\rm stat}(t)|
\ge\frac\eta2q_T\log T
\right\}
\right|
\ll_{B,\eta}
\frac{X_T^2}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
\tag{6}
\]

Taking outer measure in (5), using finite subadditivity, and summing (6) proves (1). Statements (2) and (3) are immediate.

The proof uses no regularity of `t -> nu_{T,t}`. It is a finite-range reduction followed by the same stationary Montgomery--Vaughan mean-square estimate already proved in `NB-168`.

## A finite-alphabet corollary

Suppose the adaptive architecture may choose, at every height, from at most `K_T` compact signed shapes, with no restriction at all on how often or how irregularly it switches. More generally, suppose its whole range lies within `epsilon_T` of `K_T` actual shapes. Then

\[
\mathcal N_T(\epsilon_T)\le K_T,
\]

and

\[
\frac1T
|\{t:|\mathcal E_T(t)|\ge\eta q_T\log T\}|^*
\ll
\frac{K_TX_T^2}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
\tag{7}
\]

In particular, in the natural regime `Ta_T^2 -> infinity`, any bounded-size repertoire with

\[
X_T=o(\log T)
\]

has density-zero logarithmic rescue even if the sampler alternates between its shapes on a dense set of heights and has infinite `p`-variation for every finite `p`.

This is a genuine regime not covered by `NB-171`: repeated large jumps between two or three templates can make every ordered variation budget infinite while the unordered range entropy stays constant.

## Relation to ordered adaptation

The ordered template number `M_T(epsilon)` of `NB-171` and the unordered range cover `mathcal N_T(epsilon)` measure different costs. Any ordered approximation with `M` representatives immediately provides a range cover with at most `M` centers, so

\[
\mathcal N_T(\epsilon)\le M_T(\epsilon)
\]

up to the same harmless radius convention. But the resulting arithmetic tariffs are different:

\[
\text{ordered:}\qquad
\frac{X_T^2}{(\log T)^2}
\left(1+\frac{M_T}{Ta_T^2}\right),
\]

whereas (1) gives

\[
\text{unordered:}\qquad
\frac{\mathcal N_TX_T^2}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
\]

The ordered theorem is stronger when the path progresses through many genuinely different templates in a regular way, because the main `T`-energy is shared among consecutive cells and only the Montgomery--Vaughan endpoint error pays for refreshes. The entropy theorem is stronger for violent recurrence: the path may revisit a tiny repertoire infinitely often, so ordered refresh count and all finite `p`-variation budgets can blow up while `mathcal N_T` remains small.

Thus `p`-variation and range entropy are complementary, not successive names for the same complexity.

## Transfer to zero-packet debt

The explicit-formula transfer of `NB-168`--`NB-171` is unchanged. If at a center `t` a target architecture produces at least `kappa log T` zeros carrying charge at least `q_T`, cancelling the corresponding adverse debt through the arithmetic-source escape requires a completed remainder of order `q_T log T`.

The elementary Gamma, pole, and reference terms are controlled pointwise by the true template's capped transport and remain `O_B(q_TX_T/T)` on bounded offset support. Under the sparse-rescue regime (2), since `mathcal N_T>=1` whenever the family is nonempty, one already has `X_T=o(log T)` after the harmless ultra-thin factor is included, so these elementary terms are negligible at `q_T log T` scale.

Therefore (1) also bounds, at the same resolution, the set of centers where arbitrary height adaptation can use the arithmetic source to cancel logarithmic zero-packet debt. As before, this is a density statement. It does not exclude a deliberately selected discrete sequence lying entirely in the exceptional set.

## Adversarial checks and exact boundary

The internal-cover condition is deliberate. Allowing arbitrary external net centers could introduce representatives with capped transport much larger than the family amplitude `X_T`; choosing centers from `mathcal R_T` keeps the `NB-168` budget uniform without an extra projection argument.

The union bound is intentionally crude and no sharp maximal inequality is claimed. Correlations between nearby stationary templates may permit an entropy-integral improvement, but none is needed for the present obstruction. In particular, (2) is sufficient, not necessary.

Small metric entropy also does not defeat the pointwise amplitude barrier. If `X_T` is itself comparable to `log T`, even a one-template family lies outside the density-zero conclusion, consistently with `NB-168`. Conversely, if `X_TH_T=o(log T)`, the pointwise bounded-Lipschitz estimate of `NB-167` is already stronger and no entropy theorem is needed. The useful window is where individual shapes can reach logarithmic scale pointwise but the architecture has too few source-distinguishable shapes to do so on a positive proportion of heights.

The ultra-thin limitation remains exactly the stationary one. When `Ta_T^2` is small, the weighted Montgomery--Vaughan error in every cover center is expensive. The entropy argument cannot remove a limitation already present for one fixed template.

Finally, range entropy says nothing about a family with a huge repertoire concentrated on a sparse exceptional set of heights. That is a genuinely different selective mechanism and remains open.

## Representation and prior-art audit

The covering-number step is classical metric-space technology, and the finite-union reduction in (5) is elementary. No novelty is claimed for epsilon-nets, metric entropy, union bounds, or Montgomery--Vaughan mean-square theory.

A targeted prior-art search found a close methodological neighbor in Michel Weber, *Local Suprema of Dirichlet Polynomials and Zerofree Regions of the Riemann Zeta-Function*, arXiv:1005.3932 (2010), which uses covering arguments together with Montgomery--Vaughan-type estimates to control local extrema of finite families of shifted Dirichlet polynomials. This confirms that the generic covering-plus-Dirichlet-mean-value strategy is classical territory. It does not provide the present capped-Jordan source metric, the source resolution `log T/H_T`, or the transfer from an adaptive signed exterior sampler to logarithmic zero-packet conservation debt.

The only load-bearing external theorem here remains the Montgomery--Vaughan generalized Hilbert inequality already anchored in `SOURCES.md` and used through `NB-168`. The new step is a direct consequence of the line-local capped transport estimate plus the stationary theorem, so no additional source anchor is required.

## Research consequence

After `NB-171`, saying that a successful sampler may have infinite `p`-variation for every finite `p` is no longer a sufficient description of the escape. Even maximally rough switching is harmless if it repeatedly revisits too small a repertoire at the Poisson/source resolution.

For positive-density arithmetic rescue, a compact height-adaptive architecture must now pay through at least one of two independent complexity channels: ordered refresh complexity large enough to evade `NB-171`, or unordered range entropy large enough to evade (3). A path can be expensive in one and cheap in the other, so both must be tracked.

The surviving compact escape is correspondingly sharper: construct a genuinely arithmetic height selector whose available signed shapes have large Poisson-resolution entropy, or concentrate the mechanism on a sparse exceptional set, or enter the ultra-thin exterior layer. Merely making the height dependence discontinuous, oscillatory, or of infinite variation no longer evades the conservation program.