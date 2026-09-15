# WI-297 — pole MGF tightness forces an aperture-independent `L^2` core

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-MGF/CONCENTRATION + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened** first-crossing branch of `WI-281`, `WI-284`, and `WI-294`--`WI-296`. The result retains the exponential-moment imbalance in Suzuki's pole factorization that `WI-296` explicitly left unused.
- **Result:** a hypothetical screened null mode cannot merely have a positive global `L^1` budget; after normalizing the measure `v(x)dx`, its spatial variance is bounded by an exact aperture-independent constant. Consequently a fixed interval of universal length captures a fixed positive fraction of the normalized `L^2` mass, independently of the crossing aperture `a`.
- **What it does not claim:** this does not rule out complete screening. Full-span support can still be maintained by arbitrarily weak remote satellites. The result supplies the missing **tight core**, not yet a propagation theorem forcing a fixed amount of mass into those satellites.
- **Novelty boundary:** Suzuki supplies the gamma-plus-pole decomposition; `WI-295` supplies the exact digamma bathtub profile and `WI-296` supplies the self-consistent global `L^1` floor. Moment-generating-function identities, `cosh t\ge1+t^2/2`, Chernoff/Markov tails, and Chebyshev concentration are classical. The line-local deduction is to divide the exact pole upper bound by the same `L^1` mass used in the bathtub and recognize the resulting ratio as a two-sided MGF dispersion functional of the physical-space probability measure. No priority claim is made.

## Claim

Let `a>0` be a Suzuki first crossing and let

\[
0\ne v\ge0,
\qquad
\|v\|_2=1,
\qquad
A_av=0,
\qquad
q_a(v)=0,
\tag{1}
\]

be a real null mode, extended by zero outside `(-a,a)`. Assume complete screening of every active prime-power autocorrelation. Put

\[
M:=\|v\|_1=\int v(x)\,dx,
\qquad
s:=M^2.
\tag{2}
\]

Recall from `WI-295` the exact monotone bathtub profile

\[
\mathcal H(u)
=\frac{u}{2\pi}
\int_{-\pi/u}^{\pi/u}
\left[
\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi
\right]dz,
\qquad u>0,
\tag{3}
\]

and from `WI-296` the exact self-consistency condition

\[
\mathcal H(s)+2s<0,
\qquad
\sigma_*<s\le\log2,
\tag{4}
\]

where

\[
\sigma_*:=\inf\{u>0:\mathcal H(u)+2u<0\}.
\tag{5}
\]

Define the compact candidate-admissible set

\[
\mathcal S
:=
\{u\in(0,\log2]:\mathcal H(u)+2u\le0\}
\tag{6}
\]

and the exact pole-dispersion constant

\[
\boxed{
\kappa_*
:=
\max_{u\in\mathcal S}
\left(-\frac{\mathcal H(u)}{2u}\right).
}
\tag{7}
\]

If a candidate (1) exists, `\mathcal S` is nonempty by (4). It is bounded away from zero because `\mathcal H(u)\to+\infty` as `u\downarrow0`, hence the maximum in (7) is finite.

Normalize the positive `L^1` measure of the null mode to a probability law,

\[
d\nu(x):=\frac{v(x)}M\,dx,
\qquad
X\sim\nu.
\tag{8}
\]

Then

\[
\boxed{
\mathbb E e^{X/2}\,\mathbb E e^{-X/2}<\kappa_*.
}
\tag{9}
\]

Equivalently, for independent `X,Y\sim\nu`,

\[
\boxed{
\mathbb E\cosh\!\left(\frac{X-Y}{2}\right)<\kappa_*.
}
\tag{10}
\]

In particular

\[
\boxed{
\operatorname{Var}_\nu(X)<4(\kappa_*-1).
}
\tag{11}
\]

Thus the mandatory global `L^1` mass of `WI-296` is spatially tight, uniformly in the aperture. Writing

\[
V_*:=4(\kappa_*-1),
\qquad
R_*:=\sqrt{2V_*}=\sqrt{8(\kappa_*-1)},
\tag{12}
\]

there is a center `\bar x=\mathbb E_\nu X` for which

\[
\boxed{
\int_{|x-\bar x|<R_*}v(x)\,dx>\frac M2.
}
\tag{13}
\]

Consequently the same interval captures a universal positive amount of normalized `L^2` mass:

\[
\boxed{
\int_{|x-\bar x|<R_*}v(x)^2\,dx
>
q_*
:=
\frac{\sigma_*}{8R_*}
=
\frac{\sigma_*}{16\sqrt{2(\kappa_*-1)}}
>0.
}
\tag{14}
\]

The intersection with `(-a,a)` is understood in (13)--(14); its length is at most `2R_*`, which only strengthens the Cauchy--Schwarz step below.

There is also an exact exponential `L^1` tail form. If

\[
A_+:=\mathbb E e^{X/2},
\qquad
A_-:=\mathbb E e^{-X/2},
\qquad
c:=\log\frac{A_+}{A_-},
\tag{15}
\]

then for every `R\ge0`,

\[
\boxed{
\nu(X\ge c+R)<\sqrt{\kappa_*}\,e^{-R/2},
\qquad
\nu(X\le c-R)<\sqrt{\kappa_*}\,e^{-R/2}.
}
\tag{16}
\]

So any remote satellites that preserve full essential span must carry exponentially small `L^1` mass relative to the forced core scale.

For orientation only, direct high-precision evaluation of the exact one-dimensional optimization in (7) gives

\[
\kappa_*\approx1.12394355932233367,
\qquad
R_*\approx0.99576527082373654,
\qquad
q_*\approx0.04079578763572088.
\tag{17}
\]

These decimals are not load-bearing; the theorem is (7)--(16).

## 1. The null identity bounds a two-sided physical-space MGF

Under complete screening, `WI-296` gives the exact prime-deleted identity

\[
G(v)+P_a(v)=0
\tag{18}
\]

and the strict candidate-dependent bathtub estimate

\[
G(v)>\mathcal H(s).
\tag{19}
\]

Hence

\[
\boxed{P_a(v)<-\mathcal H(s).}
\tag{20}
\]

Suzuki's positive pole factorization is

\[
P_a(v)=2L_-(v)L_+(v),
\qquad
L_\pm(v)=\int v(x)e^{\pm x/2}\,dx.
\tag{21}
\]

By (8),

\[
L_+(v)=M\,\mathbb E e^{X/2},
\qquad
L_-(v)=M\,\mathbb E e^{-X/2}.
\tag{22}
\]

Divide (20) by `2s=2M^2` and use `s\in\mathcal S` from (4):

\[
\mathbb E e^{X/2}\,\mathbb E e^{-X/2}
=
\frac{P_a(v)}{2s}
<
-\frac{\mathcal H(s)}{2s}
\le\kappa_*.
\tag{23}
\]

This proves (9). The lower Cauchy--Schwarz bound in `WI-296` says the left side of (23) is at least one. Equality would require `X` to be constant `\nu`-almost surely; that is impossible for a nonzero `L^2` function with an absolutely continuous measure `v(x)dx`. Therefore any candidate forces `\kappa_*>1`, so `R_*` and `q_*` in (12)--(14) are well-defined and positive.

The key point is that `WI-296` used only the lower bound `P_a(v)\ge2M^2`. Equation (23) keeps the **amount by which the two exponential moments fail to saturate that lower bound**, which is spatial information rather than another scalar mass floor.

## 2. Pole dispersion is exactly a pairwise `cosh` moment

Let `X,Y` be independent with law `\nu`. Independence gives

\[
\mathbb E e^{(X-Y)/2}
=
\mathbb E e^{X/2}\,\mathbb E e^{-Y/2}.
\tag{24}
\]

The distribution of `X-Y` is symmetric, so its odd `sinh` contribution vanishes. Therefore

\[
\mathbb E e^{(X-Y)/2}
=
\mathbb E\cosh\!\left(\frac{X-Y}{2}\right),
\tag{25}
\]

which proves (10).

Now use the elementary global inequality

\[
\cosh t\ge1+\frac{t^2}{2}.
\tag{26}
\]

Since

\[
\mathbb E(X-Y)^2=2\operatorname{Var}_\nu(X),
\tag{27}
\]

(10), (26), and (27) give

\[
\kappa_*
>
1+\frac18\mathbb E(X-Y)^2
=
1+\frac14\operatorname{Var}_\nu(X),
\tag{28}
\]

which is (11).

This converts the pole bound into a genuine aperture-independent tightness statement. No support topology, selector approximation, or numerical property of the hypothetical null mode is used.

## 3. A fixed interval contains a fixed positive `L^2` mass

Let `\bar x=\mathbb E_\nu X`. From (11),

\[
\operatorname{Var}_\nu(X)<V_*.
\tag{29}
\]

Chebyshev's inequality at radius `R_*=\sqrt{2V_*}` gives

\[
\nu(|X-\bar x|\ge R_*)
\le
\frac{\operatorname{Var}_\nu(X)}{R_*^2}
<\frac12.
\tag{30}
\]

Multiplying by `M` proves (13).

Set

\[
I_*:=(-a,a)\cap(\bar x-R_*,\bar x+R_*).
\tag{31}
\]

Then `|I_*|\le2R_*`, and Cauchy--Schwarz gives

\[
\left(\int_{I_*}v\right)^2
\le
|I_*|\int_{I_*}v^2
\le
2R_*\int_{I_*}v^2.
\tag{32}
\]

By (13) the left side is greater than `M^2/4=s/4`; by `WI-296`, `s>\sigma_*`. Hence

\[
\int_{I_*}v^2
>
\frac{s}{8R_*}
>
\frac{\sigma_*}{8R_*}=q_*.
\tag{33}
\]

This proves (14). In contrast with qualitative full-span information, `q_*` does not go to zero when `a` grows.

## 4. The same MGF gives exponential `L^1` tails

With `A_\pm` and `c` from (15), direct substitution gives

\[
\mathbb E e^{(X-c)/2}
=
\mathbb E e^{-(X-c)/2}
=
\sqrt{A_+A_-}
<\sqrt{\kappa_*}.
\tag{34}
\]

Markov's inequality applied to the two exponentials yields

\[
\begin{aligned}
\nu(X\ge c+R)
&\le e^{-R/2}\mathbb E e^{(X-c)/2},\\
\nu(X\le c-R)
&\le e^{-R/2}\mathbb E e^{-(X-c)/2},
\end{aligned}
\tag{35}
\]

and (16) follows from (34).

Thus `WI-295`'s two-piece separated-mass tariff and `WI-296`'s global `L^1` floor can be strengthened to an actual global tightness law: the `L^1` probability measure itself has uniformly controlled exponential tails after recentering.

## 5. Exact characterization of the constant and stress tests

The exact constant (7) is a one-dimensional special-function optimization. Writing

\[
m(z)=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi,
\tag{36}
\]

`WI-295` proves that `m` is even and strictly increasing on `z>0`. From (3),

\[
-\frac{\mathcal H(u)}{2u}
=-\frac1{2\pi}\int_0^{\pi/u}m(z)\,dz.
\tag{37}
\]

Hence

\[
\frac d{du}
\left(-\frac{\mathcal H(u)}{2u}\right)
=
\frac{m(\pi/u)}{2u^2}.
\tag{38}
\]

Since `m(0)<0` and `m(z)\to+\infty`, `m` has a unique positive zero. Therefore the unconstrained profile in (37) has a unique interior maximum at `u=\pi/z_0`; (7) merely restricts that exact profile to the candidate-admissible set `\mathcal S`. The decimal in (17) comes from this exact characterization and is included only as orientation.

Several failure modes are intentionally excluded:

1. The argument is **one-signed**. For sign-changing `v`, `v(x)dx/M` is not a probability measure and the positive pole factorization no longer defines the MGF dispersion used above.
2. Complete screening is load-bearing through the prime-deleted identity (18). Unscreeened prime terms can alter the upper bound (20).
3. Tightness is not support compactness. Equation (16) permits nonzero satellites at arbitrarily large separation if their `L^1` mass decays exponentially.
4. The fixed `L^2` core in (14) does not by itself contradict full-span firstness. A further source-specific propagation theorem is needed to transfer a positive amount of that core mass toward distant support or to show that the exact null equation cannot sustain exponentially weak relays.

The fourth point is the remaining gate rather than a weakness in (14): `WI-282` showed that qualitative full span admits vanishing satellites, while (14) now proves that the actual null identity simultaneously forces an aperture-independent nonvanishing core.

## 6. Prior-art and novelty audit

The load-bearing operator source remains Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), already source-audited in `WI-238`, `WI-284`, `WI-295`, `WI-296`, and `SOURCES.md`. Suzuki supplies the localized Weil form and the exact gamma/pole decomposition; no new claim about Suzuki's operator is made here.

The probability identities used after (23) are classical: products of moment-generating functions describe the law of an independent difference, `cosh t\ge1+t^2/2` controls its second moment, Chebyshev converts variance into a fixed-mass interval, and Markov/Chernoff converts exponential moments into tails. A targeted external search around Suzuki's localized Weil operator, pole factorization, exponential-moment localization, and `L^1` tightness found Suzuki's paper and generic MGF/concentration literature but no matching zeta/Suzuki statement. Search absence is audit context only and is not evidence of priority.

The line-local novelty check is sharper. `WI-295` used the pole only as a scalar upper tariff on two separated `L^1` pieces. `WI-296` used only the scalar lower bound `L_-L_+\ge M^2` and explicitly identified the **exact exponential-moment imbalance** as information discarded by that compression. Equations (23)--(35) retain precisely that imbalance. Thus `WI-297` does not restate the previous mass floor: it upgrades it to variance, exponential-tail, and positive-`L^2`-core constraints on the same hypothetical null vector.

## Consequence for the research line

The live sparse-satellite escape is now narrower. A one-signed completely screened first null mode must contain an aperture-independent core carrying at least `q_*>0` of its normalized `L^2` mass, while its normalized `L^1` measure has uniformly bounded variance and exponential tails. Full essential span can survive only through progressively weak satellites.

The next decisive bridge should therefore be **local-to-global propagation** rather than another global uncertainty inequality: combine the fixed core (14) with the cutwise firstness/source identities of `WI-270`--`WI-280` and ask whether an exact null mode can propagate from that core to arbitrarily distant support while respecting the exponential pole-tail budget (16). A proof that every full-span screened null mode must transport a fixed positive `L^1` or `L^2` amount across successive cuts would collide directly with (16) and close the one-signed complete-screening branch.
