# NB-170 — Bounded-variation height adaptation pays a Poisson-resolution refresh tariff

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + BOUNDED-VARIATION + CAPPED-TRANSPORT + HEIGHT-ADAPTIVE + NB-169-REFINEMENT`.

`NB-169` shows that a signed compact sampler cannot defeat the logarithmic Euler-side obstruction on positive density merely by installing finitely many height-dependent templates: every refreshed Dirichlet coefficient sequence pays another Montgomery--Vaughan `a_T^{-2}` tariff. Its explicit frontier is a continuously varying family `t -> nu_{T,t}`, where counting discontinuous refreshes is no longer the right complexity measure.

The correct replacement is variation in the same capped Poisson metric that already controls source and target in `NB-167`. A bounded-variation path can be quantized at the resolution at which `zeta'/zeta` can distinguish two templates. This turns continuous adaptation into an effective number of `NB-169` refreshes and yields a quantitative variation barrier for logarithmic arithmetic rescue.

## Claim

Fix `B>0`. Let `T -> infinity`, let `0<a_T<=1`, and for every `t in [T,2T]` let `nu_{T,t}` be a finite real signed Borel measure supported on `[-B,B]` with zero total mass. Let `q_T>0` be a reference target charge.

For any finite zero-mass signed measure `sigma`, write

\[
\mathsf D_{a_T}(\sigma)
:=
\inf_{\pi\in\Pi(\sigma^+,\sigma^-)}
\iint
\min\left\{1,\frac{|u-v|}{a_T}\right\}
\,d\pi(u,v).
\]

This is the capped Jordan transport norm from `NB-167`; equivalently, by Kantorovich--Rubinstein duality for the bounded metric `d_a(u,v)=min{1,|u-v|/a}`,

\[
\mathsf D_{a_T}(\sigma)
=
\sup_{|\phi(u)-\phi(v)|\le d_{a_T}(u,v)}
\left|\int\phi\,d\sigma\right|.
\]

Define the instantaneous transport amplitude

\[
X_T
:=
\sup_{t\in[T,2T]}
\frac{\mathsf D_{a_T}(\nu_{T,t})}{q_T},
\]

and the normalized path variation

\[
\mathcal V_T
:=
\frac1{q_T}
\sup_{T=t_0<\cdots<t_m=2T}
\sum_{j=1}^m
\mathsf D_{a_T}
\bigl(\nu_{T,t_j}-\nu_{T,t_{j-1}}\bigr).
\]

Assume `mathcal V_T<infinity`; changing the family on a Lebesgue-null set is immaterial. Put

\[
H_T
:=
\min\left\{
\frac1{a_T},
\frac{\log T}{\log\log T}
\right\},
\]

and define the genuinely height-adaptive Euler response

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
|\mathcal E_T(t)|\ge
\eta q_T\log T
\right\}
\right|
\ll_{B,\eta}
\frac{X_T^2}{(\log T)^2}
\left(
1+
\frac1{Ta_T^2}
+
\frac{\mathcal V_TH_T}
{Ta_T^2\log T}
\right).
}
\]

Consequently,

\[
\boxed{
X_T^2
\left(
1+
\frac1{Ta_T^2}
+
\frac{\mathcal V_TH_T}
{Ta_T^2\log T}
\right)
=o((\log T)^2)
}
\]

forces logarithmic Euler rescue onto a set of relative Lebesgue measure `o(1)`.

Conversely, suppose the rescue set has relative measure at least a fixed `delta>0` and the stationary baseline is subcritical,

\[
X_T^2
\left(1+\frac1{Ta_T^2}\right)
=o((\log T)^2).
\]

Then necessarily

\[
\boxed{
\mathcal V_T
\gg_{B,\eta,\delta}
\frac{Ta_T^2(\log T)^3}
{X_T^2H_T}.
}
\]

Thus continuous or infinitely refreshed height adaptation is not free: positive-density rescue requires enough cumulative template motion in the capped metric to cross the source-resolution scale repeatedly.

## Derivation

### The source sees template differences only through capped transport

For fixed `t`, set

\[
f_{T,t}(u)
:=
\frac{\zeta'}{\zeta}
\bigl(1+a_T+i(t+u)\bigr).
\]

The high-ordinate bounds used in `NB-165`--`NB-167`, uniformly for `t in [T,2T]` and `|u|<=B`, give

\[
\|f_{T,t}\|_\infty
\ll_B H_T,
\qquad
\operatorname{Lip}(f_{T,t})
\ll_B \frac{H_T}{a_T}.
\]

Hence its oscillation and Lipschitz constant place `f_{T,t}/(C_BH_T)` in the dual unit ball of `D_{a_T}`. For any two zero-mass templates,

\[
\boxed{
\left|
\int f_{T,t}\,d(\nu-\widetilde\nu)
\right|
\ll_B
H_T\,
\mathsf D_{a_T}(\nu-\widetilde\nu).
}
\]

This is exactly the bounded-Lipschitz mechanism of `NB-167`, now applied to the difference between two templates at the same center height.

### Bounded variation gives finitely many effective templates at source resolution

A bounded-variation path in any metric space admits step approximation at cost proportional to total variation. Concretely, for every `epsilon>0`, the interval `[T,2T]` can be divided, up to endpoints, into consecutive cells

\[
I_{T,1},\ldots,I_{T,M_T}
\]

and one representative template `widetilde nu_{T,j}` from each cell can be chosen so that

\[
\mathsf D_{a_T}
\bigl(\nu_{T,t}-\widetilde\nu_{T,j}\bigr)
\le
q_T\epsilon,
\qquad t\in I_{T,j},
\]

while

\[
\boxed{
M_T\ll 1+\frac{\mathcal V_T}{\epsilon}.
}
\]

One way to see this is to parameterize the path by cumulative metric variation and start a new cell whenever another `epsilon` of variation has accumulated. Jumps larger than `epsilon` start a new cell immediately and themselves consume at least `epsilon` of the total variation, so they obey the same count. Values at the resulting cell boundaries do not affect a Lebesgue-density statement.

Choose

\[
\epsilon
=
 c_{B,\eta}\frac{\log T}{H_T}
\]

with `c_{B,eta}>0` small enough. If `widetilde mathcal E_T(t)` denotes the Euler response obtained from the step template on the cell containing `t`, then the preceding source estimate gives

\[
|\mathcal E_T(t)-\widetilde{\mathcal E}_T(t)|
\le
\frac{\eta}{2}q_T\log T.
\]

Therefore

\[
|\mathcal E_T(t)|\ge\eta q_T\log T
\quad\Longrightarrow\quad
|\widetilde{\mathcal E}_T(t)|
\ge\frac{\eta}{2}q_T\log T.
\]

At the same time,

\[
M_T
\ll_{B,\eta}
1+
\frac{\mathcal V_TH_T}{\log T}.
\]

The important quantity is therefore not the literal number of infinitesimal changes. It is the number of times the path can move by the source-resolution distance `log T/H_T` in normalized capped transport.

### NB-169 applies to the quantized path

Every representative is an actual member, or one-sided limit, of the original bounded-variation family, so

\[
\frac{\mathsf D_{a_T}(\widetilde\nu_{T,j})}{q_T}
\le X_T
\]

up to an inessential limiting convention. Applying the uniform corollary of `NB-169` at threshold `eta/2` gives

\[
\frac1T
\left|
\left\{t:
|\widetilde{\mathcal E}_T(t)|
\ge\frac{\eta}{2}q_T\log T
\right\}
\right|
\ll_{B,\eta}
\frac{X_T^2}{(\log T)^2}
\left(1+\frac{M_T}{Ta_T^2}\right).
\]

Substituting the effective-refresh count proves

\[
\frac1T
|\{t:|\mathcal E_T(t)|\ge\eta q_T\log T\}|
\ll_{B,\eta}
\frac{X_T^2}{(\log T)^2}
\left(
1+
\frac1{Ta_T^2}
+
\frac{\mathcal V_TH_T}
{Ta_T^2\log T}
\right).
\]

The positive-density lower bound for `mathcal V_T` follows by rearranging this inequality once the two stationary terms are `o(1)` after normalization.

## Quantitative interpretation

The new tariff has a simple effective-refresh form:

\[
\boxed{
M_{\rm eff}(T)
\asymp
1+
\frac{\mathcal V_TH_T}{\log T}.
}
\]

A path may oscillate continuously or contain infinitely many tiny jumps, but changes smaller than `log T/H_T` in normalized capped transport cannot alter the Euler response at the `q_T log T` rescue scale by more than a fixed fraction. Only cumulative motion large enough to cross that resolution creates a genuinely new effective coefficient template.

The theorem is most informative in the intermediate regime left open by `NB-167`. If

\[
X_TH_T=o(\log T),
\]

then `NB-167` already gives the pointwise bound `|mathcal E_T(t)|=o(q_T log T)` and no adaptation theorem is needed. Here one may allow

\[
X_TH_T\gtrsim\log T
\]

while still having `X_T=o(log T)`; stationarity alone no longer gives pointwise exclusion, but bounded total template variation still forces logarithmic rescue to be sparse unless the variation reaches the displayed threshold.

In the common high-ordinate regime

\[
H_T=\frac{\log T}{\log\log T},
\]

positive-density rescue under a subcritical stationary baseline forces

\[
\boxed{
\mathcal V_T
\gg
\frac{Ta_T^2(\log T)^2\log\log T}
{X_T^2}.
}
\]

For a step family whose meaningful jumps are each of source-resolution size `asymp log T/H_T`, this becomes the `NB-169` critical refresh count. Tiny step changes are correctly merged into one effective template instead of being charged a full `a_T^{-2}` tariff apiece.

## Transfer to zero-packet debt

The explicit-formula interpretation from `NB-165`--`NB-169` is unchanged. If at a center `t` a target architecture creates at least `kappa log T` zeros carrying charge at least `q_T`, cancelling the corresponding adverse debt through the arithmetic-source escape requires a completed remainder of order `q_T log T`. The Gamma, pole and reference terms on bounded offset support remain lower-order under the same transport-size hypotheses used previously.

Hence a positive-density family of such target packets cannot be rescued by a bounded-variation signed control unless the displayed variation tariff is paid. The statement does not assert that the target packets themselves exist, and it does not convert a Lebesgue-density conclusion into exclusion of an arbitrarily selected sparse sequence of zero heights.

## Adversarial checks and exact boundary

The theorem does **not** control a merely measurable family with infinite capped-transport variation. Such a family can install a genuinely new shape at every height, and reducing it to finitely many templates would require an entropy, modulus-of-continuity or source-specific argument beyond total variation.

The path variation is measured in the same capped metric as the source resolution, not in total variation of the signed measures or ordinary `W_1`. This is essential. Large changes invisible after one Poisson width should not count as extra detail, while tiny positive/negative rearrangements inside one width should be charged proportionally to their actual effect.

The result also does not improve the ultra-thin limitation inherited from `NB-169`: if `Ta_T^2` is too small, the per-template Montgomery--Vaughan tariff may already dominate and the displayed converse variation scale may become non-informative. The theorem records that regime explicitly through the baseline term `1/(Ta_T^2)`.

Finally, the proof is not a new variational mean-value theorem for Dirichlet polynomials. It first compresses the BV family into finitely many source-distinguishable templates and then invokes the already established piecewise-stationary theorem. This makes the dependence on the regularity hypothesis transparent and avoids claiming control of arbitrary time-dependent Dirichlet coefficients.

## Representation and prior-art audit

The metric part is generic. Kantorovich--Rubinstein duality for the bounded metric `min{1,|u-v|/a}` and the elementary quantization of a bounded-variation metric path together say that a Lipschitz test cannot distinguish more than `O(1+V/epsilon)` templates at resolution `epsilon`. Neither statement is specific to zeta.

The source-specific content is the combination already isolated in `NB-167`--`NB-169`: high-ordinate `zeta'/zeta` has bounded-Lipschitz size `H_T` at Poisson scale `a_T`, capped transport controls the resulting coefficient templates, and Montgomery--Vaughan charges `a_T^{-2}` whenever a distinguishable template is refreshed. A fresh prior-art search found neighboring maximal/variational large-sieve and Dirichlet-series estimates, including the maximal large-sieve direction already noted in `NB-169`, but no result supplying this capped-transport BV reduction or its zero-packet transfer. No new load-bearing external source is required, so `SOURCES.md` remains unchanged.

## Research consequence

`NB-169` left continuously varying controls as the cleanest compact height-adaptive escape. That escape now has a quantitative price. A BV family has only

\[
O\left(1+\frac{\mathcal V_TH_T}{\log T}\right)
\]

source-distinguishable templates at logarithmic rescue resolution, and positive-density rescue with sublogarithmic instantaneous capped transport forces `mathcal V_T` to grow at the displayed critical rate.

The remaining compact source-side escape is therefore narrower: use very large or infinite capped-transport variation, concentrate on a genuinely sparse exceptional sequence, or exploit arithmetic resonance so source-specific that it cannot be reduced to bounded-Lipschitz proximity of nearby templates. The next useful question is no longer whether continuous adaptation helps in principle, but whether the arithmetic mechanism that selects the sampler can supply that much Poisson-resolution variation without simultaneously destroying target gain or reintroducing adverse zero debt.