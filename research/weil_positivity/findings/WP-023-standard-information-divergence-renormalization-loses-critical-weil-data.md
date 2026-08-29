# WP-023 — Standard information-divergence renormalization loses the critical Weil data

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the most canonical information-geometric escapes left by `WP-022`: replace the divergent Fisher norm by Kullback--Leibler or another smooth `f`-divergence, or normalize the critical score to unit Fisher speed and use its ideal-boundary direction. The positive divergences do exist for `sigma,tau>1/2`, and the KL divergence even has an exact zeta formula. But their infinitesimal positive geometry is necessarily Fisher, so the critical point is at infinite information distance. Under the unique obvious unit-speed normalization, every fixed prime-power Weil coefficient vanishes and the norm escapes to the tail of the prime coordinates. A simultaneous KL approach to the boundary has a finite limit only after collapsing to a universal function of the ratio of the two boundary distances, determined solely by the simple pole of zeta at `1`. Thus the standard information-divergence completion retains positivity only by losing the place-by-place Weil data that made the `WP-022` score interesting.

## 1. Setup: the positive Poisson family from WP-022

For `sigma>1/2`, let

\[
\nu_\sigma
=\bigotimes_p P_{p^{-\sigma}}(\theta_p)\,dm(\theta_p),
\qquad
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\tag{1}
\]

`WP-022` proves that the radial score

\[
S_\sigma=\partial_\sigma\log\frac{d\nu_\sigma}{dm_\infty}
\tag{2}
\]

has local Fourier coefficients

\[
-2(\log p)p^{-k\sigma}\cos(k\theta_p),
\tag{3}
\]

so at `sigma=1/2` its nonconstant part is exactly the finite-prime Weil cosine comb. The same finding also proves that its Fisher norm

\[
I_\sigma=\|S_\sigma\|^2_{L^2(\nu_\sigma)}
=2\sum_p\frac{(\log p)^2p^{-2\sigma}}
{(1-p^{-2\sigma})^2}
\tag{4}
\]

is finite exactly for `sigma>1/2` and diverges at the critical boundary.

The natural next question is therefore whether a **finite positive divergence between measures**, rather than the infinitesimal Fisher norm, can cross or compactify that boundary without losing the arithmetic information in (3).

For the standard smooth information divergences, the answer is no in the direct route.

## 2. The KL divergence has an exact zeta formula

For two one-circle Poisson laws `P_r dm` and `P_s dm`, `0<=r,s<1`, the logarithmic Fourier expansion

\[
\log P_r(\theta)
=\log(1-r^2)+2\sum_{k\ge1}\frac{r^k}{k}\cos(k\theta)
\tag{5}
\]

and the Poisson moments

\[
\mathbb E_r[\cos(k\theta)]=r^k
\tag{6}
\]

give directly

\[
\begin{aligned}
D_{\rm KL}(P_r\|P_s)
&=\int P_r\log\frac{P_r}{P_s}\,dm\\
&=2\log(1-rs)-\log(1-r^2)-\log(1-s^2)\\
&=\boxed{
\log\frac{(1-rs)^2}{(1-r^2)(1-s^2)} }.
\end{aligned}
\tag{7}
\]

For this one-parameter radial family the expression happens to be symmetric in `r,s`, although KL divergence is not symmetric in general.

Taking

\[
r_p=p^{-\sigma},\qquad s_p=p^{-\tau}
\]

and summing the independent prime factors gives, for `sigma,tau>1/2`,

\[
\begin{aligned}
D_{\rm KL}(\nu_\sigma\|\nu_\tau)
&=\sum_p
\left[
2\log(1-p^{-\sigma-\tau})
-\log(1-p^{-2\sigma})
-\log(1-p^{-2\tau})
\right]\\
&=\boxed{
\log\zeta(2\sigma)+\log\zeta(2\tau)
-2\log\zeta(\sigma+\tau)}.
\end{aligned}
\tag{8}
\]

There is no analytic continuation in (8): all three Euler products converge absolutely. Positivity of KL is therefore exactly the familiar log-convexity inequality

\[
\zeta(\sigma+\tau)^2
\le \zeta(2\sigma)\zeta(2\tau),
\qquad \sigma,\tau>\frac12.
\tag{9}
\]

This is already a warning. The new positive scalar does not produce a test-function Weil form; in the ordinary region it is a classical convexity property of the Euler product.

A useful endpoint control is relative entropy to product Haar. Setting `s_p=0` in (7),

\[
\boxed{
D_{\rm KL}(\nu_\sigma\|m_\infty)
=\sum_p-\log(1-p^{-2\sigma})
=\log\zeta(2\sigma)}.
\tag{10}
\]

Thus the positive entropy itself diverges when `sigma downarrow 1/2`. It sees the zeta pole already identified by the score normalization in `WP-022`, not a finite completed Weil energy.

## 3. The critical KL boundary limit is universal pole geometry

Write

\[
\sigma=\frac12+a,
\qquad
\tau=\frac12+b,
\qquad a,b>0.
\]

Equation (8) becomes

\[
D_{\rm KL}(\nu_{1/2+a}\|\nu_{1/2+b})
=
\log\zeta(1+2a)+\log\zeta(1+2b)
-2\log\zeta(1+a+b).
\tag{11}
\]

The classical Laurent expansion at the simple pole,

\[
\zeta(1+x)=\frac1x+O(1),
\qquad
\log\zeta(1+x)=-\log x+O(x),
\tag{12}
\]

gives the exact matched-boundary asymptotic

\[
\boxed{
D_{\rm KL}(\nu_{1/2+a}\|\nu_{1/2+b})
=
\log\frac{(a+b)^2}{4ab}+o(1)}.
\tag{13}
\]

If `b/a -> lambda in (0,infinity)`, then

\[
\boxed{
D_{\rm KL}
\longrightarrow
\log\frac{(1+\lambda)^2}{4\lambda}.}
\tag{14}
\]

All prime-by-prime structure has disappeared from this boundary limit. It depends only on the ratio of the two distances to the critical parameter and on the fact that the Euler product has a simple pole at `1`. The pole residue cancels as well.

Thus KL does admit a nontrivial **projective boundary geometry**, but it is the wrong one for the present target: its leading critical limit is universal pole geometry, not the Mangoldt comb, the Gamma term, a zero-sensitive functional, or a place-matched Weil pairing.

This also gives a matched-control statement. For a weighted free commutative monoid with partition function

\[
Z(s)=\prod_j(1-e^{-s a_j})^{-1},
\tag{15}
\]

the identical product-Poisson calculation yields

\[
D_{\rm KL}(\nu_\sigma^a\|\nu_\tau^a)
=
\log Z(2\sigma)+\log Z(2\tau)-2\log Z(\sigma+\tau).
\tag{16}
\]

Whenever `Z(1+x)~C/x`, equation (14) follows verbatim and the constant `C` cancels. Hence the critical KL geometry cannot distinguish the rational primes from generalized-prime/free-monoid controls having the same first-order pole law.

## 4. Every smooth f-divergence returns to Fisher at second order

The KL calculation is not an accident of that particular divergence. Let

\[
D_f(P\|Q)=\int f\!\left(\frac{dP}{dQ}\right)dQ
\tag{17}
\]

be a smooth Csiszar `f`-divergence with the harmless normalization

\[
f(1)=f'(1)=0,
\qquad f''(1)>0.
\]

For any regular statistical path `P_{\sigma+h}` through `P_\sigma`, write

\[
\frac{dP_{\sigma+h}}{dP_\sigma}
=1+hS_\sigma+O(h^2).
\]

Taylor expansion of `f` and the score identity `E[S_sigma]=0` give

\[
\boxed{
D_f(P_{\sigma+h}\|P_\sigma)
=\frac{f''(1)}2 h^2 I_\sigma+o(h^2).}
\tag{18}
\]

This is the standard information-geometric fact that smooth `f`-divergences induce the Fisher metric, up to scale. It applies in particular to KL, Hellinger, chi-square, and Jensen--Shannon-type smooth local geometries.

Equation (18) has two consequences for the Weil route.

First, **positivity has no linear term**. The arithmetic object of `WP-022` is the first derivative/score, whose coefficients are linear in

\[
(\log p)p^{-k\sigma}.
\]

Every smooth divergence is stationary on the diagonal; its first nontrivial positive term is quadratic in that score. Therefore divergence positivity does not prove the sign of the linear Weil comb any more than Fisher positivity did.

Second, because (4) diverges at `sigma=1/2`, every such smooth divergence has the same singular local metric in the arithmetic radial direction. Replacing Fisher by another smooth standard information divergence cannot create a finite critical quadratic tangent.

## 5. The critical boundary is at infinite Fisher distance

The divergence rate can be made exact from (8). Put

\[
F(s)=\log\zeta(s).
\]

Expanding (8) at `tau=sigma+h` gives

\[
D_{\rm KL}(\nu_\sigma\|\nu_{\sigma+h})
=h^2F''(2\sigma)+O(h^3),
\tag{19}
\]

and hence

\[
\boxed{I_\sigma=2F''(2\sigma).}
\tag{20}
\]

Using (12), with `a=sigma-1/2`,

\[
F''(1+2a)=\frac1{4a^2}+O(1),
\]

so

\[
\boxed{
I_{1/2+a}=\frac1{2a^2}+O(1).}
\tag{21}
\]

The Fisher line element therefore satisfies

\[
\sqrt{I_\sigma}\,d\sigma
\sim \frac{da}{\sqrt2\,a}.
\tag{22}
\]

Consequently

\[
\int_{1/2}^{1/2+\varepsilon}\sqrt{I_\sigma}\,d\sigma=\infty.
\tag{23}
\]

The critical parameter is not a finite boundary point of the regular information manifold. It lies at infinite Fisher distance.

This is stronger than saying that a particular coordinate has a divergent metric coefficient. A regular change of parameter does not make the endpoint finite in the intrinsic metric.

## 6. Unit-speed renormalization kills every fixed prime-power coefficient

There is an obvious canonical response to (21): renormalize the score to unit Fisher norm,

\[
\widehat S_\sigma
=\frac{S_\sigma}{\sqrt{I_\sigma}},
\qquad
\|\widehat S_\sigma\|_{L^2(\nu_\sigma)}=1.
\tag{24}
\]

This is the information-geometric analogue of approaching the ideal boundary at unit speed. It fails arithmetically in an exact way.

For any fixed prime power `p^k`, its nonconstant Fourier coefficient in `S_sigma` is

\[
c_{p,k}(\sigma)=-2(\log p)p^{-k\sigma}.
\tag{25}
\]

By (21),

\[
\frac1{\sqrt{I_{1/2+a}}}
=\sqrt2\,a+o(a),
\]

so

\[
\boxed{
\frac{c_{p,k}(1/2+a)}{\sqrt{I_{1/2+a}}}
\longrightarrow0
\qquad(a\downarrow0)}.
\tag{26}
\]

Thus the canonical normalized boundary tangent has **zero coefficient at every fixed Weil atom**, despite having total norm one.

The same phenomenon holds at the level of complete finite-prime subsystems. For a fixed finite set of primes `F`, let `S_{\sigma,F}` be the conditional/local score from `WP-022` and let

\[
I_{\sigma,F}=\|S_{\sigma,F}\|^2.
\]

Since `F` is finite,

\[
I_{\sigma,F}\longrightarrow I_{1/2,F}<\infty,
\]

whereas `I_sigma -> infinity`. Therefore

\[
\boxed{
\left\|
\mathbb E_{\nu_\sigma}
[\widehat S_\sigma\mid(\theta_p)_{p\in F}]
\right\|^2
=
\frac{I_{\sigma,F}}{I_\sigma}
\longrightarrow0.}
\tag{27}
\]

So the normalized unit tangent does not merely attenuate individual Fourier coefficients. **Every fixed finite-prime cylinder captures asymptotically zero fraction of its norm.** The unit mass escapes to larger and larger prime coordinates.

This is fatal for the direct Weil interpretation. The finite explicit formula is a place-by-place sum with a stable coefficient at every fixed `p^k`. The canonical information-geometric renormalization that makes the critical tangent finite destroys exactly that local stability.

## 7. Why bounded divergences do not evade the obstruction automatically

Some `f`-divergences remain bounded or admit finite values even for singular pairs of measures. That does not contradict the result above.

The no-go concerns using their **standard smooth positive geometry** as the missing Weil quadratic form. On every interior point `sigma>1/2`, equation (18) forces the same Fisher metric; the arithmetic critical direction is infinitely long, and its unit-speed tangent loses all fixed-prime components by (27).

A nonsmooth endpoint functional could still be defined directly on the singular measure `nu_{1/2}`. But then its sign and normalization no longer follow from the ordinary interior `f`-divergence/Fisher theorem. Such a construction is a genuinely new singular or relative boundary mechanism and must be audited on its own terms.

Likewise one may subtract the universal pole part of (11) and rescale subleading terms. That is outside this result only if the subtraction and rescaling are forced by a larger Mathia geometry and carry an independent sign theorem. Choosing them merely to recover desired coefficients would be the hand-picked renormalization excluded by this branch.

## 8. Prior art and novelty audit

No information-geometric novelty is claimed.

- Csiszar `f`-divergences and KL divergence are classical.
- Shun-ichi Amari and Andrzej Cichocki, **“Information geometry of divergence functions,”** *Bulletin of the Polish Academy of Sciences: Technical Sciences* **58**(1) (2010), 183--195, DOI `10.2478/v10175-010-0019-1`, explicitly records that `f`-divergences induce the Fisher information metric, up to the standard scaling, together with the associated dual connections.
- Log-convexity of `zeta(s)` on `s>1` and the Laurent expansion at its pole are classical. Equation (8) is a direct product-Poisson packaging of those facts, not a new zeta inequality.
- The Poisson/wrapped-Cauchy family, its Fisher information, and the measure-class transition are already prior art dependencies of `PL-030` and `WP-022`.

Targeted searches around wrapped-Cauchy/Poisson KL divergence and information-divergence geometry did not identify a reliable source making the specific Prime-Lattice critical-boundary comparison (13), (21), and (27). No novelty claim is inferred from that absence. The durable contribution is the **Mathia-specific closure of a live escape from WP-022**: standard positive information divergences cannot regularize its critical score while preserving the finite Weil data.

## 9. Matched-control and falsification tests

This finding should be withdrawn or narrowed if any of the following exact checks fails:

1. the one-factor Poisson KL divergence is (7);
2. independence and Euler products give the global identity (8) for `sigma,tau>1/2`;
3. the simple-pole expansion gives the universal matched-boundary limit (13)--(14);
4. a smooth `f`-divergence has local quadratic term `(f''(1)/2) I_sigma h^2`;
5. the Fisher information satisfies (20) and the asymptotic (21);
6. the Fisher distance to `sigma=1/2` is infinite;
7. after unit-speed normalization every fixed coefficient (25) vanishes as in (26);
8. the conditional norm on every fixed finite prime set vanishes as in (27);
9. the same KL boundary law holds for a weighted free-monoid partition function with a simple pole, showing that the limit is not RH-specific.

Items 1--8 are exact consequences of the Poisson family and the classical zeta pole, independent of RH and of the zero divisor. Item 9 is a matched-control statement under the explicitly stated simple-pole hypothesis.

## 10. Consequence for the research line

`WP-022` left open a canonical singular/relative renormalization of the critical Poisson geometry. This result closes the **standard information-theoretic version** of that escape:

```text
PL-030 positive product-Poisson geometry
    -> exact critical Weil score
    -> Fisher metric diverges
    -> replace Fisher by KL / smooth f-divergence
    -> same Fisher local geometry
    -> critical point at infinite distance
    -> normalize to unit information speed
    -> every fixed prime-place coefficient vanishes
    -> matched KL boundary limit is universal pole geometry.
```

The remaining Poisson route must therefore be substantially more singular and more global. A viable construction could still use `nu_{1/2}` as finite boundary data, but it must couple or quotient it with an archimedean/global structure **before** the final positivity theorem, or supply a genuinely new singular boundary order/compression/intersection principle. Ordinary divergence positivity no longer supplies that theorem.

## Internal dependencies

- `research/prime_lattice/findings/PL-030-gcd-poisson-measure-class-transition.md`
- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-022-prime-torus-poisson-score-fisher-positivity-breaks-at-critical-boundary.md`
