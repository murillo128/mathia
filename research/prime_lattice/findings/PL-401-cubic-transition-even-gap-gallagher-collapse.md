# PL-401 — Cubic transition reopens even gaps, but Gallagher averaging collapses the first mesoscopic signal

## Claim

The parity obstruction in `PL-400` is a genuinely **subcubic** phenomenon. Let

\[
q=r+d,\qquad T=2\pi rq,
\]

with integers `r,d`, and reuse the continuation-faithful pair coefficient

\[
P_{r,d}
 =\exp\!\big(i\{2\theta(T)-T\log(rq)\}\big)Q_q(T)Q_r(T)
\]

from `PL-400`. If

\[
d\to\infty,\qquad d=o(r^{1/2}),
\]

then the next phase term retained in the incomplete-gamma transition gives

\[
P_{r,d}
 =\frac{1+o(1)}{\sqrt2\,\pi d}
   \exp\!\left(
      -\frac{i\pi}{2}(d^2+1)
      -\frac{i\pi d^3}{6r}
   \right).
\tag{1}
\]

Consequently

\[
\Re P_{r,d}
 =-\frac{1+o(1)}{\sqrt2\,\pi d}
 \begin{cases}
 \sin\!\left(\dfrac{\pi d^3}{6r}\right),&d\ \text{even},\\[1.2ex]
 \cos\!\left(\dfrac{\pi d^3}{6r}\right),&d\ \text{odd}.
 \end{cases}
\tag{2}
\]

Thus `PL-400` is recovered when `d=o(r^{1/3})`, but at the cubic scale

\[
\frac{d}{r^{1/3}}\to c>0
\]

the even-gap real channel is generically restored at its full `1/d` scale:

\[
d\,\Re P_{r,d}
 \longrightarrow
 -\frac{1}{\sqrt2\,\pi}
   \sin\!\left(\frac{\pi c^3}{6}\right).
\tag{3}
\]

This is the first continuation-faithful gap regime after `PL-400` in which the same-sign real channel and the parity class carrying the Hardy--Littlewood von Mangoldt bulk are no longer asymptotically disjoint.

However, the most immediate mesoscopic aggregation still fails to produce arithmetic rigidity. Let `S_2(d)` be the standard weighted Hardy--Littlewood pair singular series, normalized so that `S_2(d)=0` for odd `d`. Gallagher's classical singular-series averaging gives

\[
\sum_{d\le H} S_2(d)=H+o(H).
\tag{4}
\]

For fixed `C>0`, and any `D=D(r)` satisfying

\[
D\to\infty,\qquad D=o(r^{1/3}),
\]

(1)--(4) imply

\[
\sum_{D<d\le C r^{1/3}}
 S_2(d)\,\Re P_{r,d}
 \longrightarrow
 -\frac{1}{\sqrt2\,\pi}
 \int_0^C
 \frac{\sin(\pi u^3/6)}{u}\,du.
\tag{5}
\]

Taking `C -> infinity` after the `r -> infinity` limit gives the explicit universal mass

\[
-\frac{1}{\sqrt2\,\pi}
 \int_0^\infty\frac{\sin(\pi u^3/6)}{u}\,du
 =-\frac{1}{6\sqrt2}.
\tag{6}
\]

The arithmetic input in this first aggregate has therefore collapsed to the **mean** of the singular series. Replacing `S_2(d)` by the trivial parity control `2 1_{2\mid d}` produces the same limit. The cubic transition genuinely reopens the even-gap channel, but its leading Gallagher-averaged signal is universal rather than a new RH-sensitive invariant.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTEXT + ROUTE-REOPENING/UNIVERSALITY-CONTROL`.

The asymptotic is derived from the exact incomplete-gamma continuation representation already audited in `PL-395`--`PL-400`. Equation (4) is classical singular-series averaging. No Euler product is analytically continued in this argument.

## 1. Retaining the cubic transition phase

`PL-400` derived, at the upper transition coordinate,

\[
y_q^2
 =\frac{i\pi d^2}{2}
  +\frac{i\pi d^3}{6r}
  +O\!\left(\frac dr+\frac{d^4}{r^2}\right).
\tag{7}
\]

That finding imposed `d=o(r^{1/3})`, so the cubic term was `o(1)` and only the quadratic parity phase survived. The stronger but still transition-local regime

\[
d=o(r^{1/2})
\]

instead makes only the remainder in (7) tend to zero. Hence

\[
e^{-y_q^2}
 =\exp\!\left(
   -\frac{i\pi d^2}{2}
   -\frac{i\pi d^3}{6r}
  \right)(1+o(1)).
\tag{8}
\]

The same erfc-sector estimate used in `PL-399` and `PL-400` remains valid because `\arg y_q\to\pi/4`, `|y_q|\asymp d`, and `d\to\infty`. Moreover

\[
y_q=d\sqrt{\frac{\pi i}{2}}\,(1+o(1)),
\]

so

\[
Q_q(T)
 =\frac{1+o(1)}{\sqrt2\,\pi d}
   \exp\!\left(
      -\frac{i\pi}{4}
      -\frac{i\pi d^2}{2}
      -\frac{i\pi d^3}{6r}
   \right),
\tag{9}
\]

while the lower transition factor still satisfies

\[
Q_r(T)=1+O(1/d).
\tag{10}
\]

Finally the Hardy phase from `PL-400` is

\[
2\theta(T)-T\log(rq)
 =-T-\frac\pi4+O(T^{-1}).
\tag{11}
\]

Because `T=2\pi rq` and `rq` is an integer, `e^{-iT}=1`. Multiplying (9)--(11) proves (1).

The parity reduction is exact at the quadratic level. For even `d`,

\[
\exp\!\left(-\frac{i\pi}{2}(d^2+1)\right)=-i,
\]

whereas for odd `d` it equals `-1`. Taking real parts gives (2). In particular, the even channel has three regimes:

- `d=o(r^{1/3})`: the sine tends to zero, recovering the `o(1/d)` suppression of `PL-400`;
- `d\asymp r^{1/3}`: the cubic phase is order one and generically restores a real coefficient of order `1/d`;
- `r^{1/3}\ll d=o(r^{1/2})`: the real coefficient remains of order at most `1/d` but oscillates through cubic-phase nodes.

The cubic scale is therefore an actual phase transition for the parity conclusion, not merely a place where the previous error estimate stopped being convenient.

## 2. Uniform error on a bounded cubic window

For the aggregation below, fix `C` and restrict to

\[
D<d\le C r^{1/3}.
\]

The component estimates used in `PL-399`--`PL-400` give, after retaining the cubic phase, an absolute remainder of the form

\[
P_{r,d}
 =\frac{1}{\sqrt2\,\pi d}
   e^{-i\pi(d^2+1)/2-i\pi d^3/(6r)}
 +O\!\left(
      \frac1{d^2}+\frac1r+\frac{d^3}{r^2}
   \right),
\tag{12}
\]

uniformly on such windows once `D -> infinity`. The three terms come respectively from the `Q_r-1` correction, the incomplete-gamma/prefactor corrections, and exponentiating the remainder in (7). The erfc inverse-power correction is smaller here.

This quantitative form matters because a bare uniform relative `o(1)` would not by itself justify summing against a harmonic `1/d` envelope. Gallagher's mean estimate and partial summation imply

\[
\sum_{D<d\le C r^{1/3}} S_2(d)
\left(
\frac1{d^2}+\frac1r+\frac{d^3}{r^2}
\right)=o(1),
\tag{13}
\]

provided `D -> infinity`. Thus the mesoscopic limit may be taken through the leading term in (12).

## 3. Gallagher averaging turns the reopened channel into a universal integral

Set

\[
H=r^{1/3},\qquad
 g(u)=\frac{\sin(\pi u^3/6)}{u},
\]

with the continuous extension `g(0)=0`. Because the pair singular series vanishes for odd `d`, (2) and (12) reduce the leading weighted sum to

\[
-\frac{1}{\sqrt2\,\pi}
\sum_{D<d\le CH}
 S_2(d)\,\frac1H g(d/H).
\tag{14}
\]

The measure form of Gallagher's average,

\[
\frac1H\sum_{d\le uH}S_2(d)\to u
\]

for fixed `u`, together with partial summation, sends (14) to the integral in (5). The lower cutoff disappears because `D/H -> 0` and `g(u)=O(u^2)` at zero.

The infinite-window value is elementary. With `v=\pi u^3/6`,

\[
\int_0^\infty \frac{\sin(\pi u^3/6)}u\,du
 =\frac13\int_0^\infty\frac{\sin v}{v}\,dv
 =\frac\pi6,
\]

which yields (6).

This is a useful matched control. Gallagher averaging has used only the first moment of `S_2`; therefore the identical limit follows from

\[
S_2(d)\rightsquigarrow 2\,1_{2\mid d}.
\]

The nonzero cubic signal is real, continuation-faithful, and parity-compatible, but at this level it does not remember the arithmetic fluctuations of the singular series.

## 4. Relation to actual von Mangoldt correlations

`PL-075` identified the von Mangoldt version of a pair channel as Hardy--Littlewood correlation data and records modern almost-all-shift results in growing ranges. The cubic window `H\asymp X^{1/3}` lies inside the range where averaged prime-pair information is substantially stronger than fixed-shift knowledge.

That observation is **not** promoted here to an asymptotic for the actual `Lambda(r)Lambda(r+d)`-weighted continuation sum. Such a transfer would require a theorem strong enough for the joint, smoothly `r`-dependent pair-saddle weight in (1), with errors summable over the cubic gap window. Equation (5) is therefore a theorem about the classical singular-series model, not a disguised proof of an averaged Hardy--Littlewood statement.

This boundary is important. The exact continuation geometry has now supplied a nonzero parity-compatible kernel, but the remaining arithmetic step is explicit: show that genuine prime-pair correlations retain a non-universal component after this cubic weighting, rather than merely reproducing the Gallagher mean.

## 5. Prior-art and novelty audit

The ingredients are classical or already canonical in this line: uniform incomplete-gamma transition asymptotics, the Hardy/Riemann--Siegel phase, Hardy--Littlewood pair singular series, and Gallagher averaging. Targeted searches for Riemann--Siegel/incomplete-gamma cubic transition phases combined with prime-pair or singular-series gap aggregation did not locate a direct source for (1)--(6).

The safe novelty claim is therefore only the **derived composition inside the Mathia continuation kernel**: retaining the first previously discarded cubic phase identifies the exact scale where the `PL-400` parity obstruction breaks and shows that the first singular-series aggregate then collapses to a universal sine-integral mass. This is not a claim that cubic turning-point asymptotics or singular-series averaging are new.

## 6. Falsification controls and remaining gap

The decisive local falsification check is numerical or symbolic evaluation of the exact regularized incomplete-gamma factors at

\[
T=2\pi r(r+d),\qquad d\sim c r^{1/3},
\]

for even `d`: the quantity `d Re P_{r,d}` must approach

\[
-(\sqrt2\,\pi)^{-1}\sin(\pi c^3/6).
\]

A sign failure here would invalidate the phase orientation in (1)--(3). A second control is arithmetic: replacing the singular series by `2 1_{2|d}` must leave (5) unchanged; if a proposed consequence also survives this replacement, it has not yet used prime arithmetic beyond parity density.

No RH implication follows from this finding. The leading cubic aggregate is specifically **too universal**. A surviving RH-facing mechanism must retain information erased by Gallagher first-moment averaging: fluctuations of `S_2(d)`, genuine `Lambda`-pair errors/correlations, a different continuation channel, or a coupling across gaps/heights that cannot be matched by the trivial even-gap control.

## Consequence for the line

`PL-400` did not close the continuation-faithful pair route; it located the end of its subcubic regime. The cubic term in the exact transition phase reopens the correct even parity class at `d\asymp r^{1/3}`. But the most obvious mesoscopic average immediately scalarizes to a universal constant. The next useful test is therefore not whether the even channel exists—it does—but whether **arithmetic fluctuations around the Gallagher mean survive the cubic continuation kernel in a form that cannot be reproduced by the parity-only control**.
