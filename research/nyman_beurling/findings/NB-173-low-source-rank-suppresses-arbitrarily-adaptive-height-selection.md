# NB-173 — Low source rank suppresses arbitrarily adaptive height selection

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + FINITE-RANK + CAPPED-TRANSPORT + ARBITRARY-ADAPTATION + NB-172-REFINEMENT`.

`NB-168` controls one stationary compact signed source template. `NB-169`--`NB-171` price increasingly rough height adaptation through ordered refresh complexity, while `NB-172` removes temporal regularity entirely at the cost of the covering number of the template range. That still leaves an important mismatch: a continuum of templates can have large Poisson-resolution covering number even when every template is chosen from a very low-dimensional *linear* source family.

Linearity of `zeta'/zeta` gives a stronger control in that regime. If every adaptive template is assembled from `m_T` stationary capped-transport-normalized source directions, then an arbitrary height-dependent selector is bounded by the vector energy of those `m_T` stationary responses. Cauchy--Schwarz followed by the scalar `NB-168` mean-square theorem gives a density estimate depending on a rank-times-coefficient-energy complexity, with no continuity, measurability, variation, interval partition, or range-cover assumption on the selector.

This closes a regime not covered sharply by `NB-172`: large or even rapidly growing range entropy can be harmless when it is generated inside a low-rank source dictionary with sublogarithmic coefficient energy.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, and let `q_T>0`. For zero-mass finite real signed Borel measures supported on `[-B,B]`, write

\[
\mathsf D_{a_T}(\sigma)
:=
\inf_{\pi\in\Pi(\sigma^+,\sigma^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v).
\]

Suppose there are stationary zero-mass signed templates

\[
\tau_{1,T},\ldots,\tau_{m_T,T}
\]

supported on `[-B,B]` and normalized by

\[
\mathsf D_{a_T}(\tau_{j,T})\le q_T
\qquad(1\le j\le m_T),
\tag{1}
\]

such that for every `t in [T,2T]` the adaptive template has a representation

\[
\nu_{T,t}
=
\sum_{j=1}^{m_T}\beta_{j,T}(t)\tau_{j,T},
\qquad
\sum_{j=1}^{m_T}|\beta_{j,T}(t)|^2\le Y_T^2.
\tag{2}
\]

The coefficient functions may be chosen arbitrarily as functions of height, including after inspecting the local arithmetic source. No regularity or measurability is assumed.

Define

\[
\mathcal E_T(t)
:=
\int
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr)
\,d\nu_{T,t}(u).
\]

Then for every fixed `eta>0`,

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:
|\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|^*
\ll_{B,\eta}
\frac{m_TY_T^2}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
}
\tag{3}
\]

Here `|.|^*` is Lebesgue outer measure. Thus logarithmic arithmetic rescue is confined to relative outer measure `o(1)` whenever

\[
\boxed{
m_TY_T^2
\left(1+\frac1{Ta_T^2}\right)
=o((\log T)^2).
}
\tag{4}
\]

Conversely, if the rescue set has relative outer measure at least a fixed `delta>0`, every representation satisfying (1)--(2) must obey

\[
\boxed{
m_TY_T^2
\gg_{B,\eta,\delta}
\frac{(\log T)^2}
{1+(Ta_T^2)^{-1}}.
}
\tag{5}
\]

So arbitrary adaptive selection from a low-rank stationary source span is not free. Positive-density rescue requires a large rank, large transport-weighted coefficient energy, or the same ultra-thin exterior degeneration already present for one stationary template.

## Intrinsic linear source complexity

The normalization in (1) removes the meaningless freedom to rescale a dictionary vector and inversely rescale its coefficient. It also leads to a representation-independent envelope.

For the range

\[
\mathcal R_T:=\{\nu_{T,t}:T\le t\le2T\},
\]

define its **linear source complexity** by

\[
\mathfrak L_T
:=
\inf
\left\{
 mY^2:
 \begin{array}{l}
 \nu_{T,t}=\sum_{j=1}^{m}\beta_j(t)\tau_j\ \text{for all }t,\\[2mm]
 \mathsf D_{a_T}(\tau_j)\le q_T,\\[1mm]
 \sup_t\sum_{j=1}^{m}|\beta_j(t)|^2\le Y^2
 \end{array}
\right\},
\tag{6}
\]

with `mathfrak L_T=infinity` if no finite stationary representation exists. Since (3) holds for every admissible representation, it immediately gives

\[
\boxed{
\frac1T
\left|
\left\{t:
|\mathcal E_T(t)|\ge\eta q_T\log T
\right\}
\right|^*
\ll_{B,\eta}
\frac{\mathfrak L_T}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right).
}
\tag{7}
\]

This quantity cannot be made artificially small by duplicating a dictionary direction. More basically, let

\[
X_T
:=
\sup_t\frac{\mathsf D_{a_T}(\nu_{T,t})}{q_T}
\]

be the instantaneous capped-transport amplitude from `NB-172`. For every representation in (6), the triangle inequality and Cauchy--Schwarz give

\[
\frac{\mathsf D_{a_T}(\nu_{T,t})}{q_T}
\le
\sum_{j=1}^{m}|\beta_j(t)|
\le
\sqrt m\,Y,
\]

hence

\[
\boxed{X_T^2\le\mathfrak L_T.}
\tag{8}
\]

Thus `mathfrak L_T` refines rather than evades the pointwise amplitude currency: it records how much *linear source repertoire* is available beyond the largest individual template.

For a pre-existing unnormalized dictionary `sigma_j`, with

\[
\Xi_j:=\frac{\mathsf D_{a_T}(\sigma_j)}{q_T}>0,
\]

one may set `tau_j=sigma_j/Xi_j` and `beta_j=alpha_j Xi_j`. The coefficient budget becomes

\[
Y_T^2
=
\sup_t\sum_j|\alpha_j(t)|^2\Xi_j^2,
\tag{9}
\]

which is invariant under independent rescaling of each original dictionary vector. Zero-transport directions are the zero signed measure and may simply be discarded.

## Derivation

For each stationary normalized source direction define

\[
\mathcal E_{j,T}(t)
:=
\int
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr)
\,d\tau_{j,T}(u).
\]

By linearity,

\[
\mathcal E_T(t)
=
\sum_{j=1}^{m_T}\beta_{j,T}(t)\mathcal E_{j,T}(t).
\tag{10}
\]

Pointwise Cauchy--Schwarz and (2) give

\[
|\mathcal E_T(t)|^2
\le
Y_T^2
\sum_{j=1}^{m_T}|\mathcal E_{j,T}(t)|^2.
\tag{11}
\]

Every `tau_{j,T}` is stationary as `t` ranges through the dyadic block, so `NB-168` applies separately to each one. By (1),

\[
\int_T^{2T}|\mathcal E_{j,T}(t)|^2\,dt
\ll_B
q_T^2\left(T+a_T^{-2}\right).
\tag{12}
\]

Summing (12),

\[
\int_T^{2T}
\sum_{j=1}^{m_T}|\mathcal E_{j,T}(t)|^2\,dt
\ll_B
m_Tq_T^2\left(T+a_T^{-2}\right).
\tag{13}
\]

If `Y_T=0`, the adaptive response vanishes identically. Otherwise (11) implies the pointwise containment

\[
\left\{t:|\mathcal E_T(t)|\ge\eta q_T\log T\right\}
\subseteq
\left\{t:
\sum_{j=1}^{m_T}|\mathcal E_{j,T}(t)|^2
\ge
\frac{\eta^2q_T^2(\log T)^2}{Y_T^2}
\right\}.
\tag{14}
\]

The set on the right is measurable even when the selector `t -> beta_T(t)` is not. Markov's inequality together with (13) proves (3), hence (4), (5), and after optimization (7).

The argument is deliberately vectorial rather than entropic. It does not cover the template range by nearby points; it bounds the entire adaptive linear span at once through the sum of the stationary source energies.

## Strict separation from range entropy

`NB-172` and (3) are genuinely different controls. Consider the rank-one family

\[
\nu_{T,t}=\beta_T(t)\tau_T,
\qquad
\mathsf D_{a_T}(\tau_T)=q_T,
\qquad
|\beta_T(t)|\le Y_T.
\tag{15}
\]

The selector may range through a continuum and oscillate arbitrarily with height. The present theorem gives

\[
\frac{|\{t:|\mathcal E_T(t)|\ge\eta q_T\log T\}|^*}{T}
\ll
\frac{Y_T^2}{(\log T)^2}
\left(1+\frac1{Ta_T^2}\right),
\tag{16}
\]

exactly the stationary scale apart from the allowed coefficient amplitude.

By contrast, if the coefficient range fills an interval of length comparable to `Y_T`, its internal covering number at the `NB-172` source resolution `epsilon_T` is of order at least `Y_T/epsilon_T` when `Y_T>>epsilon_T`. In the high-ordinate regime

\[
H_T=\frac{\log T}{\log\log T},
\qquad
\epsilon_T\asymp\log\log T,
\]

take for example

\[
Y_T=(\log T)^{3/4}.
\]

Then (16) tends to zero like `(log T)^(-1/2)`, whereas the direct `NB-172` union-bound tariff can be as large as

\[
\frac{(Y_T/\log\log T)Y_T^2}{(\log T)^2}
\asymp
\frac{(\log T)^{1/4}}{\log\log T},
\]

which is non-vanishing and therefore inconclusive. Large covering entropy generated by amplitude motion along one source direction is not the same resource as genuinely new stationary source directions.

The separation from `NB-171` is equally direct: `beta_T(t)` in (15) may jump on every rational/irrational alternation or otherwise have infinite `p`-variation for every finite `p`. Equation (16) is unchanged because temporal roughness never enters the proof.

## Transfer to zero-packet conservation debt

The completed explicit-formula transfer used in `NB-168`--`NB-172` applies without change. The elementary Gamma, pole, and reference terms for a true adaptive template are pointwise controlled by its capped-transport amplitude. Equation (8) shows that under the sparse-rescue regime

\[
\mathfrak L_T
\left(1+\frac1{Ta_T^2}\right)
=o((\log T)^2),
\]

one has `X_T=o(log T)` after the same ultra-thin factor is taken into account. Hence those elementary completed terms remain negligible at the `q_T log T` scale on bounded offset support.

Therefore, if an architecture produces a target packet of order `log T` zeros carrying charge `q_T`, cancellation of its logarithmic adverse debt by an adaptive arithmetic-source remainder can occur on positive density only if the linear source complexity reaches the threshold in (5), or one of the previously identified sparse/ultra-thin escapes is used.

As in `NB-168`--`NB-172`, this remains a density obstruction. A deliberately selected discrete sequence of exceptional target heights is not excluded.

## Adversarial checks and exact boundary

The theorem does **not** say that algebraic rank alone controls adaptation. A badly conditioned source basis can require large coefficient energy `Y_T`; this is why the invariant is `m_TY_T^2`, not merely `m_T`. Definition (6) optimizes over normalized stationary representations so that a basis rescaling cannot manufacture a favorable bound.

Nor is `mathfrak L_T` claimed to be a canonical Banach-space dimension. It is the exact complexity exposed by this argument: normalized stationary dictionary size times the worst coefficient `ell^2` energy. Different dictionaries can improve it, and the infimum records that freedom. Establishing a dual characterization or a sharp relation with metric entropy would be additional work.

The factor `1+(Ta_T^2)^{-1}` is inherited from `NB-168` and is unavoidable for this proof. Nothing here improves the ultra-thin `a_T \lesssim T^{-1/2}` regime, where the weighted Montgomery--Vaughan error already becomes expensive for one source direction.

The result also does not control a family whose useful templates genuinely require large linear source complexity, even if they are generated by a concise nonlinear arithmetic rule. Such a rule is now a sharper surviving possibility: it must generate many source-distinguishable directions or large normalized coefficient energy, not merely many metric-cover cells.

Finally, (3) is an upper bound obtained by summing the individual stationary energies. Correlations among the `E_{j,T}` could make the true vector energy much smaller; no lower bound or sharpness claim is made for arbitrary dictionaries.

## Representation and prior-art audit

The new mathematical step is elementary Hilbert-space geometry: an arbitrary pointwise linear selector is dominated by the Euclidean norm of a finite vector of stationary responses, and its integrated vector energy is the sum of the scalar energies. Vector-valued Dirichlet-series and Dirichlet-polynomial theory is classical and much broader than this observation; for example, A. Defant and P. Sevilla-Peris, *Convergence of Dirichlet polynomials in Banach spaces*, Trans. Amer. Math. Soc. 363 (2011), 691--697, and later work on vector-valued Hardy spaces study coefficient-space geometry in a general functional-analytic setting. No novelty is claimed for vector-valued Cauchy--Schwarz or for vector-valued Dirichlet series.

A targeted search did not reveal a prior formulation of the specific source-side statement here: arbitrary height-dependent linear selection among compact signed exterior zeta samplers, normalized by one-Poisson-width capped Jordan transport, with the resulting rank-energy tariff transferred to logarithmic zero-packet conservation debt. The only load-bearing external theorem remains the Montgomery--Vaughan mean-square input already anchored in `SOURCES.md` and already packaged by `NB-168`. No new literature theorem is required, so `SOURCES.md` is unchanged.

## Research consequence

The compact adaptive frontier now has a third independent complexity axis. `NB-171` controls **ordered movement**, `NB-172` controls **unordered range entropy**, and the present result controls **linear source complexity**. A sampler can be expensive in one currency and cheap in another: a wildly oscillating continuum may have infinite ordered variation and large covering number while remaining rank one, in which case (3) still suppresses positive-density logarithmic rescue.

Consequently, a viable compact arithmetic selector cannot rely merely on temporal roughness or a large catalogue of nearby templates. To escape all current persistence bounds it must generate enough genuinely independent capped-transport-normalized source directions (or large coefficient energy), while also evading the ordered/entropy controls where those are stronger; alternatively it must concentrate on a sparse exceptional set or enter the ultra-thin exterior regime. This remains source-side progress rather than an RH proof: no argument here converts the density obstruction into pointwise exclusion of a zero-selected sequence or supplies the missing bridge back to global Nyman target approximation.