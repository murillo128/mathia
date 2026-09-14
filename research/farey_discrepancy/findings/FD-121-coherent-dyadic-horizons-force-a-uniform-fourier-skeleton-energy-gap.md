# FD-121 — coherent dyadic horizons force a uniform Fourier-skeleton energy gap

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + CROSS-HORIZON-COHERENCE + UNIFORM-DYADIC-ENERGY-GAP + POSITIVE/ROUTE-NARROWING`.

`FD-120` shows that a synthetic source may satisfy the complete squarefree/unit-amplitude increment law and one exact divisor identity at a single horizon while remaining asymptotically on the `FD-118` Möbius equality ray. Its essential freedom is that the signs can be rebuilt separately for every horizon. The first genuinely different source restriction is therefore **coherence of one common staircase across horizons**.

On the minimal Fourier skeleton this restriction already has a critical-scale quantitative cost. Let `Y` be any real source defined on the positive integers up to `2N`. For a horizon `H`, write

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
A_H(k)
:=
\sum_{d\mid k}d\,Y\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\tag{1}
\]

and use the normalized skeleton energy of `FD-119`--`FD-120`,

\[
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}
\frac{|A_H(k)|^2}{k^2}.
\tag{2}
\]

Since `A_H(1)=Y(H)`, define the excess above the unrestricted equality value by

\[
\Delta_H(Y)
:=
\mathcal E_H^{\mathcal Q}(Y)-|Y(H)|^2
\ge0.
\tag{3}
\]

Then for every `N>=6`,

\[
\boxed{
\Delta_N(Y)+\Delta_{2N}(Y)
\ge
c_0\bigl(|Y(N)|^2+|Y(2N)|^2\bigr),
}
\tag{4}
\]

where

\[
\boxed{
c_0
:=
\frac{41-\sqrt{1553}}{64}
=0.0248669\ldots .
}
\tag{5}
\]

Thus two consecutive dyadic horizons cannot both approach their separate same-horizon equality rays. If `Y(N)` and `Y(2N)` are nonzero, at least one of the two horizons satisfies

\[
\boxed{
\frac{\mathcal E_H^{\mathcal Q}(Y)}{|Y(H)|^2}
\ge 1+c_0,
\qquad H\in\{N,2N\}.
}
\tag{6}
\]

In particular, when both terminal amplitudes are of square-root size, the total forced excess in (4) is `Omega(N)`: exactly the critical energy scale that the horizon-dependent witnesses of `FD-120` evade.

The proof uses only three low skeleton modes. No squarefree support, unit-increment law, multiplicativity, divisor identity or Mertens-specific fact is needed. Cross-horizon coherence itself already breaks joint saturation.

## 1. Three shared low modes couple the two horizons

Put

\[
t:=Y(N),
\qquad
T:=Y(2N),
\qquad
s:=Y\!\left(\left\lfloor\frac N2\right\rfloor\right).
\tag{7}
\]

For `N>=6`, one has `2\in\mathcal Q_N` and `2,4\in\mathcal Q_{2N}`. The corresponding divisor sums are

\[
A_N(2)=t+2s,
\tag{8}
\]

\[
A_{2N}(2)=T+2t,
\tag{9}
\]

and

\[
A_{2N}(4)
=T+2t+4s,
\tag{10}
\]

because

\[
\left\lfloor\frac{2N}{4}\right\rfloor
=
\left\lfloor\frac N2\right\rfloor.
\tag{11}
\]

All other non-head energy terms are nonnegative. Therefore

\[
\begin{aligned}
\Delta_N(Y)+\Delta_{2N}(Y)
&\ge
\frac{|t+2s|^2}{4}
+
\frac{|T+2t|^2}{4}
+
\frac{|T+2t+4s|^2}{16}.
\end{aligned}
\tag{12}
\]

This is already the entire mechanism: `s` is the same source value in the `k=2` mode at horizon `N` and the `k=4` mode at horizon `2N`, while `t` is simultaneously the head value at `N` and the `k=2` source value at `2N`.

## 2. Exact minimization gives a uniform constant

For the real source relevant here, the right side of (12) has the exact completion of squares

\[
\begin{aligned}
&\frac{(t+2s)^2}{4}
+
\frac{(T+2t)^2}{4}
+
\frac{(T+2t+4s)^2}{16}
\\
&\qquad=
2\left(s+\frac t2+\frac T8\right)^2
+t^2+tT+\frac{9}{32}T^2.
\end{aligned}
\tag{13}
\]

After minimizing over the shared interior coordinate `s`, the remaining quadratic form in `(t,T)` has matrix

\[
B
=
\begin{pmatrix}
1 & 1/2\\
1/2 & 9/32
\end{pmatrix}.
\tag{14}
\]

Its eigenvalues are

\[
\lambda_\pm
=
\frac{41\pm\sqrt{1553}}{64}.
\tag{15}
\]

Hence `B>=c_0 I` with `c_0=lambda_-`, and (12)--(15) prove (4). The same calculation can be written as a Hermitian quadratic form for complex formal sources, but the real statement already covers cumulative arithmetic sources such as Mertens.

The constant in (5) is the exact best constant for this **three-mode truncation**. No claim is made that it is the optimal constant for the full skeleton; additional modes can only strengthen the left side of (4).

## 3. Why the two equality rays are incompatible

`FD-119` identifies the unrestricted equality ray at horizon `H` as

\[
Y\!\left(\left\lfloor\frac Hk\right\rfloor\right)
=
Y(H)\frac{\mu(k)}k,
\qquad k\in\mathcal Q_H.
\tag{16}
\]

At horizon `N`, its `k=2` condition is

\[
s=-\frac t2.
\tag{17}
\]

At horizon `2N`, its `k=2` and `k=4` conditions are

\[
t=-\frac T2,
\qquad
s=0,
\tag{18}
\]

because `mu(4)=0`. For a nonzero endpoint these requirements cannot hold simultaneously. Equation (4) is the stable quantitative version of that incompatibility: one cannot even make all three residual modes small compared with both terminal amplitudes.

This pinpoints the freedom used by `FD-120`. There the witness `Y_N` is rebuilt for each `N`; the coordinate that plays the role of `s` at one horizon is not required to agree with the corresponding coordinate of a separately constructed witness at `2N`. Once a single common source must serve both horizons, that repair freedom disappears and a fixed relative energy penalty appears without imposing any additional local source law.

The distinction is therefore not merely between a finite and a growing number of constraints. A full horizon of pointwise admissibility can be asymptotically cheap if it is horizon-local, while only three low modes already become expensive when they are tied together by exact cross-horizon reuse of the same source values.

## 4. Dyadic-chain consequence and remaining loophole

Let `H_j=2^jN_0`, `t_j=Y(H_j)` and `Delta_j=Delta_{H_j}(Y)`. Applying (4) at every adjacent pair gives

\[
\Delta_j+\Delta_{j+1}
\ge
c_0\bigl(|t_j|^2+|t_{j+1}|^2\bigr).
\tag{19}
\]

Consequently, whenever the adjacent endpoint values are nonzero, it is impossible to have simultaneously

\[
\Delta_j<c_0|t_j|^2
\quad\text{and}\quad
\Delta_{j+1}<c_0|t_{j+1}|^2.
\tag{20}
\]

So `c_0`-near-saturation cannot occur at two consecutive dyadic horizons. On a long critical-amplitude dyadic chain this forces a block-scale or positive-density obstruction to equality-ray tracking.

That still falls short of a pointwise RH-relevant estimate. A source may in principle alternate between a nearly saturated horizon and a costly neighboring horizon. Equation (4) does not say which member of a dyadic pair pays the penalty, and it does not by itself convert the extra skeleton energy into a better bound for `M(N)` or the Franel discrepancy at a prescribed `N`.

The next frontier is therefore much narrower than after `FD-120`: **cross-horizon coherence is now known to be quantitatively load-bearing**, but a successful endpoint theorem must prevent alternating near-saturation or transfer the pairwise/block energy penalty to the designated horizon. Candidate mechanisms include overlapping multi-scale constraints, genuine Möbius sign correlation/multiplicativity, or an identity that couples the excess energy itself across neighboring horizons.

## 5. Stress test and prior-art boundary

The algebra in (13)--(15) was checked symbolically. As an independent finite regression check, exact integer/rational evaluation of the full skeleton energies was tested on random common source arrays for `45` horizons `6<=N<=50`, with `1000` samples per horizon; no violation of (4) occurred. These computations are checks only—the proof is the three-mode inequality above.

The obvious adversarial boundaries are explicit. The result does not prove that the actual Mertens trajectory is close to either equality ray, does not supply a pointwise coercivity gap at every horizon, and does not show that `c_0` is sharp for the full Fourier skeleton. It also does not use or recover Möbius multiplicativity; the theorem holds for every common real source, so its content is purely the cost of cross-horizon representation coherence.

A targeted prior-art audit covered Farey/Mertens discrepancy formulas, Mertens matrix compression, and the floor-quotient order. Lagarias--Richman and Cardinal provide the established floor-quotient/compression boundary already relevant to `FD-118`, but no matching formulation of the dyadic two-horizon energy inequality (4) was found. No external theorem is load-bearing here: (4) follows directly from the internal skeleton transform and three elementary divisor sums, so `SOURCES.md` requires no new dependency.

The durable conclusion is positive but limited: **the horizon-independence loophole left by `FD-120` is real proof currency on the minimal Fourier skeleton**. A common source cannot jointly saturate even two adjacent dyadic horizons; the remaining problem is to turn that pairwise coercivity into a pointwise endpoint gain rather than to search for yet more same-horizon admissibility constraints.
