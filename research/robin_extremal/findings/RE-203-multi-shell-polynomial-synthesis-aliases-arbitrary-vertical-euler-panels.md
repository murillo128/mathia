# RE-203 — Multi-shell polynomial synthesis aliases arbitrary vertical Euler panels below the KV phase-resolution scale

**Status:** `EXACT-DERIVED + COMPLEX-EULER-SAMPLING + MULTI-SHELL-POLYNOMIAL-SYNTHESIS + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + KV-FIDELITY + INTEGER-MULTIPLICITIES + ARBITRARY-FINITE-PANEL`.

**Parent findings:** RE-200, RE-201, RE-202.

`RE-202` prices a single translated-shell alias through simultaneous Diophantine recurrence. For a completely irregular panel that argument is universal only below `o(log log Q)` samples, because one common shift must approximately recur at every sampled height. That common-shift requirement is not intrinsic to the source model. Once the repair may use several remote shells, the shell amplitudes themselves can interpolate an arbitrary finite vertical panel.

Put

\[
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\qquad
d_Q:=\frac1{\sqrt Q\log Q}.
\tag{1}
\]

Let

\[
\mathcal T_Q=\{t_1,\ldots,t_M\}\subset\mathbb R,
\qquad
T_Q:=\max_j|t_j|,
\tag{2}
\]

be an arbitrary finite set of vertical sampling heights. No spacing, commensurability, low-rank module or separation hypothesis is imposed. If

\[
\boxed{
M+\log(2+T_Q)=o(V(Q)),
}
\tag{3}
\]

then there is a finite ordinary-prime perturbation with coefficients `c_q\in\{-1,+1\}` such that, for

\[
D_Q(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\tag{4}
\]

one has

\[
\boxed{
|D_Q(1)|+
\max_{1\le j\le M}|D_Q(1+it_j)|
=o(d_Q).
}
\tag{5}
\]

At the same time, before the first remote repair shell arrives, the local packet carries

\[
D_{Q,\mathrm{local}}(1)=\Theta(d_Q),
\tag{6}
\]

and the complete perturbation uses only multiplicities `{0,1,2}` relative to the ordinary-prime baseline and satisfies, for every fixed `b>0`,

\[
|\Delta\vartheta(x)|
=o\!\left(xe^{-bV(x)}\right)
\tag{7}
\]

through and beyond all affected scales.

Thus **the failure of a common almost-period does not make a finite vertical Euler panel source-coercive**. A collection of remote shells acts as a finite impulse-response filter in logarithmic shell index, and exact polynomial interpolation on the unit circle cancels any finite panel in the regime (3). For bounded or polynomial-height samples this extends the universal arbitrary-panel alias range from `o(log log Q)` in `RE-202` to

\[
M=o(V(Q)).
\tag{8}
\]

The cost is exponential in `M`, rather than the single-shell recurrence cost of `RE-202`.

## 1. A real polynomial interpolates every sampled phase

Fix once and for all

\[
h:=\log 8.
\tag{9}
\]

For each sampled height define

\[
z_j:=e^{-it_jh}\in\mathbb T.
\tag{10}
\]

Consider the conjugation-stable multiset

\[
\mathcal Z:=\{1\}\cup
\{z_j,\overline{z_j}:1\le j\le M\}
\tag{11}
\]

and the polynomial

\[
F(z):=\prod_{\zeta\in\mathcal Z}
\left(1-\frac z\zeta\right),
\qquad
P(z):=1-F(z).
\tag{12}
\]

Because every `\zeta` has modulus one and the multiset is invariant under conjugation, `P` has real coefficients. Write

\[
P(z)=\sum_{\ell=1}^{n}a_\ell z^\ell,
\qquad n=2M+1.
\tag{13}
\]

Repeated points in (11) cause no problem. By construction,

\[
P(1)=1,
\qquad
P(z_j)=1\quad(1\le j\le M).
\tag{14}
\]

Moreover each factor in (12) has coefficient `\ell^1` norm two, so

\[
1+\sum_{\ell=1}^{n}|a_\ell|
\le 2^n,
\qquad
\sum_{\ell=1}^{n}|a_\ell|
\le e^{O(M)}.
\tag{15}
\]

This is the entire interpolation mechanism. It is generic finite-dimensional Fourier algebra: no Diophantine recurrence is required.

## 2. Shell amplitudes realize the polynomial with ordinary primes

Take a local center

\[
X_0:=2Q
\tag{16}
\]

and remote centers

\[
X_\ell:=e^{\ell h}X_0,
\qquad 1\le\ell\le n.
\tag{17}
\]

With the choice (9), the first remote center is `16Q`, leaving a fixed multiplicative interval on which the local selector-scale debt is present before any repair.

Use the Korobov--Vinogradov PNT input already anchored for this line. Choose a constant `a>0` for which the corresponding prime-counting error is `O(xe^{-aV(x)})`, and set

\[
\eta_Q:=e^{-aV(Q)/2}.
\tag{18}
\]

Since `n=O(M)=o(V(Q))`, uniformly for `0\le\ell\le n`,

\[
\log X_\ell=\log Q+o(V(Q)),
\qquad
V(X_\ell)=(1+o(1))V(Q).
\tag{19}
\]

Hence every logarithmic bin

\[
I_\ell:=
[X_\ell e^{-\eta_Q},X_\ell e^{\eta_Q}]
\tag{20}
\]

contains

\[
(2+o(1))\frac{\eta_QX_\ell}{\log X_\ell}
\tag{21}
\]

ordinary primes. The bins are mutually disjoint for large `Q`.

Choose

\[
B\asymp\frac{\sqrt Q}{\log Q}
\tag{22}
\]

ordinary primes from `I_0` and assign coefficient `+1` to them. For each `\ell\ge1` with `a_\ell\ne0`, choose

\[
N_\ell:=
\left\lfloor |a_\ell|e^{\ell h}B\right\rceil
\tag{23}
\]

ordinary primes from `I_\ell` and give each coefficient

\[
c_q=-\operatorname{sgn}(a_\ell).
\tag{24}
\]

There are enough distinct primes. Indeed, from (15), (21) and (23), the ratio of the required population in any remote bin to the available population is at most

\[
\exp\{O(M)+aV(Q)/2-\tfrac12\log Q\}
=o(1).
\tag{25}
\]

Thus the construction uses genuine ordinary primes only. Relative to baseline multiplicity one, coefficient `+1` duplicates a prime and coefficient `-1` deletes it, so all multiplicities remain in `{0,1,2}`.

Ignoring bin width and integer rounding for one moment, the first Euler harmonic of the local packet at `s=1+it_j` is

\[
B X_0^{-1-it_j}.
\tag{26}
\]

The `\ell`th remote shell contributes

\[
-a_\ell B X_0^{-1-it_j}e^{-it_j\ell h}
=-a_\ell B X_0^{-1-it_j}z_j^\ell.
\tag{27}
\]

Summing (27) and using (14) gives the exact ideal cancellation

\[
B X_0^{-1-it_j}
\left(1-P(z_j)\right)=0.
\tag{28}
\]

At `t=0` the same identity follows from `P(1)=1`. Thus the shell populations realize a real finite impulse-response interpolant that cancels the local first harmonic at every requested sample simultaneously.

## 3. Prime quantization and exact Euler factors preserve the cancellation

For `q\in I_\ell` and `|t|\le T_Q`, elementary differentiation gives

\[
q^{-1-it}
=X_\ell^{-1-it}
\left(1+O((1+T_Q)\eta_Q)\right).
\tag{29}
\]

The total ideal reciprocal mass, measured absolutely across all shells, is bounded by

\[
\frac B{X_0}
\left(1+\sum_{\ell=1}^{n}|a_\ell|\right)
\le d_Qe^{O(M)}.
\tag{30}
\]

Consequently prime placement contributes at most

\[
d_Qe^{O(M)}(1+T_Q)\eta_Q=o(d_Q)
\tag{31}
\]

by (3) and (18).

Rounding the populations in (23) changes the first harmonic by at most

\[
O\!\left(\sum_{\ell=1}^{n}X_\ell^{-1}\right)
=O(M/Q)
=o(d_Q).
\tag{32}
\]

Finally, uniformly on `\Re s=1`,

\[
\log(1-q^{-s})^{-1}
=q^{-s}+O(q^{-2}).
\tag{33}
\]

The total contribution of all higher prime powers is therefore

\[
O\!\left(
\frac{B}{Q^2}
+\sum_{\ell=1}^{n}
\frac{|a_\ell|e^{\ell h}B}{X_\ell^2}
\right)
\le
\frac{d_Q}{Q}e^{O(M)}
=o(d_Q).
\tag{34}
\]

Equations (28), (31), (32) and (34) prove (5).

The local packet alone has

\[
\sum_{q\in I_0}H_q(1)
=\Theta(B/Q)
=\Theta(d_Q).
\tag{35}
\]

Because the first remote bin is centered at `16Q`, every cutoff after the local bin and before the first remote bin sees this uncancelled selector-scale reciprocal debt. The full remote synthesis hides it from the prescribed finite panel only later.

## 4. Exponential interpolation cost is still KV-cheap below `V(Q)` samples

The local Chebyshev perturbation is

\[
O(B\log Q)=O(\sqrt Q).
\tag{36}
\]

Using (15), (17) and (23), the total absolute Chebyshev mass of all remote edits is

\[
\ll
B\log Q
\sum_{\ell=1}^{n}|a_\ell|e^{\ell h}
\le
\sqrt Q\,e^{O(M)}.
\tag{37}
\]

Under (3), this is

\[
Q^{1/2+o(1)}.
\tag{38}
\]

All affected shell centers satisfy

\[
X_\ell=Qe^{O(M)}=Q^{1+o(1)}.
\tag{39}
\]

Hence for every fixed `b>0`, throughout and beyond the affected scales,

\[
\frac{Q^{1/2+o(1)}}{X_\ell e^{-bV(X_\ell)}}
\le
Q^{-1/2+o(1)}e^{bV(X_\ell)}
=o(1),
\tag{40}
\]

because `V(X_\ell)=o(\log Q)`. The same comparison applies between shells by bounding each partial Chebyshev sum by the total absolute edit mass. This proves (7).

The contrast with `RE-202` is structural. A single repair shell must find one logarithmic displacement `L` for which all phases recur together, so arbitrary panels pay an `M`-dimensional simultaneous-approximation cost. Multiple shells instead provide `O(M)` independent amplitudes. Polynomial interpolation trades the Diophantine denominator for coefficient mass `e^{O(M)}`, and that mass remains invisible to the KV fidelity budget throughout (3).

## Representation audit

The polynomial identity (12)--(15) is classical finite-dimensional interpolation/FIR-filter algebra on the unit circle. No novelty is claimed for the fact that finitely many prescribed phases can be annihilated by a finite polynomial, nor for the exponential coefficient-norm bound obtained by multiplying linear factors.

The source-specific content is the realization of that algebra by **ordinary-prime Euler atoms with integer multiplicities** at selector reciprocal scale. The amplitude factor `e^{-\ell h}` of a remote shell is compensated by `e^{\ell h}` more ordinary primes; the coefficient signs are implemented by deletion or duplication; prime supply remains ample in KV-short logarithmic bins; prime powers remain below selector scale; and the resulting exponentially growing edit mass is still `Q^{1/2+o(1)}` when `M=o(V(Q))`.

This sharpens the architectural lesson from `RE-200`--`RE-202`. Vertical Fourier phase does provide high local rank inside a fixed shell, but neither arithmetic commensurability nor the existence of a cheap common almost-period is the fundamental global obstruction. A source allowed to distribute its repair across several shells can synthesize the sampled vector directly.

## Adversarial self-review

**Do arbitrary irregular heights invalidate the interpolation?** No. The points `z_j=e^{-it_jh}` may be anywhere on the unit circle and may repeat. The product (12) still has real coefficients because conjugates are included, and it enforces `P(z_j)=1` exactly. No spacing or Diophantine condition enters.

**Are complex or continuous shell weights being smuggled into an integer-prime source?** No. The polynomial coefficients are real, but each coefficient is converted into the integer population (23), with only a rounding error of size (32). Its sign determines whether ordinary primes are deleted or duplicated. Every individual edit coefficient is exactly `-1` or `+1`.

**Can exponentially large coefficients exhaust the prime supply?** Not in the stated regime. Equation (25) compares the required population with the actual PNT/KV population in each short bin. The `Q^{1/2}` supply margin dominates both `e^{O(M)}` and the short-bin loss `e^{aV(Q)/2}` because `M=o(V(Q))` and `V(Q)=o(\log Q)`.

**Could large sampled heights resolve the width of the prime bins and destroy phase matching?** Yes in principle; that is why (3) contains `\log(2+T_Q)`. The placement error is multiplied by `1+T_Q` in (29). Condition (3) makes this loss negligible after the exponential coefficient norm is included.

**Do exact prime powers restore source visibility?** No on this scale. Their total error is (34), an additional factor `Q^{-1}` below the first-harmonic mass even after the `e^{O(M)}` coefficient cost.

**Does this prove that every finite vertical panel is useless?** No. The proof is quantitative and stops when the number of samples, sample height or required interpolation norm approaches the phase-resolution/KV budget. In particular it does not cover `M\asymp V(Q)` or larger, a continuum of heights, or panels extending to `T_Q` with `\log T_Q\asymp V(Q)`.

**Does the construction reproduce the full matched controls of `RE-188`--`RE-199` or itself force an order-one Robin excursion?** No. It proves noncoercivity of the proposed finite vertical observation family at selector reciprocal scale. The local packet exhibits a `\Theta(d_Q)` transient, but this finding does not establish that this packet alone produces the full Robin destination displacement or simultaneously satisfies every earlier source constraint.

**Could a global budget on edit count or shell count defeat this construction?** Possibly. The mechanism uses `O(M)` shells and total population inflated by `e^{O(M)}`. Such a budget is not part of the current ordinary-prime/KV source class. A future source-native complexity constraint could therefore change the conclusion.

## Prior-art audit

The generic construction is a finite polynomial with prescribed zeros on the unit circle, equivalently a finite impulse-response filter designed to vanish at finitely many frequencies. That mechanism is classical and is not claimed as a new interpolation theorem.

No new external theorem is load-bearing. The only arithmetic input beyond elementary Euler-factor estimates is the Korobov--Vinogradov PNT control already anchored in `SOURCES.md` for this line. Consequently no durable source addition is required.

## Literature status

The novel line-specific point is not finite polynomial interpolation. It is the quantitative conversion from that interpolation into a **multi-shell ordinary-prime matched control** with selector-scale reciprocal debt, exact `{0,1,2}` multiplicities and every-fixed-`b` KV fidelity. The construction shows that the arbitrary-panel `o(log log Q)` boundary in `RE-202` was a boundary of single-shell recurrence, not of finite vertical Euler sampling itself.

For bounded or polynomial-height samples, the sufficient universal-alias range is now `M=o(V(Q))`. This remains a construction threshold, not a proved rigidity transition.

## Caveats

The coefficient bound `e^{O(M)}` is deliberately crude. Better interpolation polynomials for specially designed height sets may reduce the source cost, while adversarially chosen height sets may force large coefficient norms under additional constraints. No matching lower bound is proved here.

The result concerns finitely many sampled heights, not uniform approximation on a vertical interval. Passing from discrete interpolation to a continuum changes the problem from finite algebra to approximation theory and may restore coercivity.

The fidelity statement uses the current source class, which constrains Chebyshev discrepancy but does not separately penalize the number of edited primes or remote shells. Adding such a source-native complexity bound would need a separate analysis.

The finding does not prove RH, Robin's inequality, a zero-free region or a full source-identification theorem.

## Next experiment

The next positive question should no longer be phrased as “choose more irrational heights.” Instead, quantify the minimum **multi-shell interpolation complexity** needed to hide selector-scale debt from a prescribed vertical observation family.

A useful target is a lower bound connecting the number of samples, their height span and either the coefficient `\ell^1` norm or the number/range of remote shells required by every real interpolant satisfying `P(e^{-it_jh})\approx1`. Compare that lower bound with the `Q^{1/2}` prime-supply margin and the KV phase-resolution scale. If optimally designed panels force interpolation complexity `\exp(\Omega(V(Q)))` before `M` reaches the natural `V(Q)` scale, the vertical channel may finally become source-coercive. If not, the next escape route is likely a continuous vertical window or an observable carrying source-native global complexity rather than finitely many scalar samples.

## Sources

- `RE-200`, *Vertical Euler phase supports linear stable dimension on one prime shell*.
- `RE-201`, *Commensurate vertical Euler frames admit remote-shell aliases at selector debt scale*.
- `RE-202`, *Diophantine rank prices noncommensurate vertical Euler aliases*.
- `RE-015`, for the Korobov--Vinogradov PNT envelope already anchored in `SOURCES.md`.