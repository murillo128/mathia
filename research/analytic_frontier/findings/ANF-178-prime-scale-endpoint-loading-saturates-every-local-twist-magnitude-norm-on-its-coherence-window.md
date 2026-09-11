# ANF-178 — Prime-scale endpoint loading saturates every local twist magnitude norm on its coherence window

**Status:** `DERIVED + MATCHED-CONTROL + LOCAL-TWIST-LARGE-VALUES + FIXED-MAGNITUDE-STATISTIC-BARRIER`. `ANF-177` shows that the prime-scale endpoint-loading packet from `ANF-175` does not merely attain the dangerous charge at the distinguished twist `U`: its value remains `Omega(a_X)` throughout the natural coherence window

\[
a_X:=\sqrt{\delta X\log X},
\qquad
W_X\asymp \frac{X}{a_X}\asymp\sqrt{\frac{X}{\log X}},
\]

and its local `L^2` mass there matches the coefficient-generic Montgomery--Vaughan envelope. A natural next possibility is that `L^2` is simply too weak: perhaps a fourth moment, a higher fixed moment, a large-values inequality, or another convex magnitude statistic could make the carrier-aligned packet exceptional even though its mean square is generic.

That escape is unavailable at the coefficient-generic level. On the same coherence window the packet has **pointwise magnitude comparable to `a_X` everywhere**: the lower bound is the coherence statement of `ANF-177`, while the upper bound is just its `l^1` coefficient mass. Consequently every finite local `L^p` norm, every fixed Orlicz-type magnitude statistic which is nondegenerate at a constant fraction of `a_X`, and the critical large-value distribution all live at their maximal coherence scale. In particular, for every fixed `p>0`,

\[
\boxed{
\int_{U-W_X}^{U+W_X}|P_X(t)|^p\,dt
\asymp_{p,\delta}
W_Xa_X^p
\asymp_{p,\delta}
X a_X^{p-1}.
}
\]

Thus replacing the `L^2` route of `ANF-177` by any fixed higher moment does not cross the endpoint-memory barrier. The obstruction is not a weakness of second-moment technology; it is the existence of a full coherence interval on which the matched control is already uniformly large.

## 1. The ANF-175 packet is uniformly target-sized throughout its dual coherence interval

Retain the notation and construction of `ANF-177`. The packet is

\[
P_X(t)=A_X\sum_{j\in S}(X+j)^{-it},
\qquad
A_X=\log X,
\]

where the active set `S` is selected from `log X`-spaced candidates lying in one angular sector of the distinguished carrier. Its physical span and coefficient masses satisfy

\[
L_X\asymp a_X,
\qquad
M_X:=\sum_{j\in S}A_X\asymp a_X,
\qquad
Q_X:=\sum_{j\in S}A_X^2\asymp a_X\log X.
\tag{1}
\]

The sector selection gives

\[
|P_X(U)|\ge a_X.
\tag{2}
\]

`ANF-177` proves from the elementary logarithmic Lipschitz estimate that, after choosing a sufficiently small fixed `c_delta>0`,

\[
W_X:=c_\delta\frac{X}{a_X}
\tag{3}
\]

satisfies

\[
|P_X(U+\tau)|\ge \frac{a_X}{2}
\qquad (|\tau|\le W_X).
\tag{4}
\]

The opposite inequality needs no harmonic analysis. By (1),

\[
|P_X(t)|
\le \sum_{j\in S}A_X
=M_X
\le C_\delta a_X
\tag{5}
\]

for every real `t`. Combining (4) and (5), on the entire interval

\[
I_X:=[U-W_X,U+W_X]
\]

we have the two-sided pointwise envelope

\[
\boxed{
\frac12 a_X
\le |P_X(t)|
\le C_\delta a_X
\qquad (t\in I_X).
}
\tag{6}
\]

This is stronger than the mean-square statement of `ANF-177`: after normalization by the dangerous endpoint scale `a_X`, the whole magnitude profile stays inside a fixed compact annulus bounded away from zero.

## 2. Every finite local moment has the forced scale `X a_X^(p-1)`

Let `p>0` be fixed. Raising (6) to the `p`th power and integrating over `I_X`, whose length is `2W_X`, gives

\[
2W_X\left(\frac{a_X}{2}\right)^p
\le
\int_{I_X}|P_X(t)|^pdt
\le
2W_X(C_\delta a_X)^p.
\tag{7}
\]

Since `W_Xasymp_delta X/a_X`,

\[
\boxed{
\int_{I_X}|P_X(t)|^pdt
\asymp_{p,\delta}
X a_X^{p-1}.
}
\tag{8}
\]

Equivalently, every normalized local `L^p` mean satisfies

\[
\boxed{
\left(
\frac{1}{|I_X|}
\int_{I_X}|P_X(t)|^pdt
\right)^{1/p}
\asymp_{p,\delta}a_X.
}
\tag{9}
\]

For the even moments most commonly used in Dirichlet-polynomial large-value arguments, (8) reads

\[
\boxed{
\int_{I_X}|P_X(t)|^{2k}dt
\asymp_{k,\delta}
X a_X^{2k-1}
\qquad(k\ge1\text{ fixed}).
}
\tag{10}
\]

There is also a coefficient-generic upper route which makes the relation to `ANF-177` explicit. Its `L^2` estimate gives

\[
\int_{I_X}|P_X(t)|^2dt\ll_\delta Xa_X,
\tag{11}
\]

while (5) gives `||P_X||_infinity=O_delta(a_X)`. Therefore, for every fixed `p>=2`,

\[
\int_{I_X}|P_X(t)|^pdt
\le
\|P_X\|_\infty^{p-2}
\int_{I_X}|P_X(t)|^2dt
\ll_{p,\delta}Xa_X^{p-1},
\tag{12}
\]

matching the deterministic lower bound. So the entire fixed-moment hierarchy generated from generic size and spacing information is already sharp on this matched control.

## 3. Higher moments do not improve the critical large-value tail

The obstruction is even clearer at the level of distribution functions. From (4),

\[
\boxed{
\operatorname{meas}
\left\{t\in I_X:
|P_X(t)|\ge\frac{a_X}{2}
\right\}
=|I_X|
\asymp_\delta\frac{X}{a_X}.
}
\tag{13}
\]

Thus the dangerous level is not attained on a thin exceptional subset of the coherence window: **the whole natural window is exceptional**.

If one applies the `2k`th-moment Markov bound at the same constant-fraction threshold, (10) gives only

\[
\operatorname{meas}
\left\{t\in I_X:
|P_X(t)|\ge c a_X
\right\}
\ll_{k,c,\delta}
\frac{Xa_X^{2k-1}}{a_X^{2k}}
\asymp
\frac{X}{a_X},
\tag{14}
\]

which is the exact order already forced by (13). Increasing a **fixed** moment therefore does not make the critical endpoint alignment rarer. More fundamentally, equation (13) is independent of the moment order: no coefficient-generic large-values statement applying to this packet can make the level `a_X/2` occupy `o(X/a_X)` measure, regardless of how it is proved.

The same point holds for much more general magnitude penalties. If `Psi:[0,infinity)->[0,infinity)` is nondecreasing, finite at `C_delta`, and satisfies `Psi(1/2)>0`, then (6) yields

\[
\boxed{
|I_X|\,\Psi(1/2)
\le
\int_{I_X}
\Psi\!\left(\frac{|P_X(t)|}{a_X}\right)dt
\le
|I_X|\,\Psi(C_\delta).
}
\tag{15}
\]

So changing from powers to any fixed nondegenerate convex/Orlicz-type statistic of the local magnitude cannot distinguish the matched packet either. The problem is geometric coherence before it is a choice of norm.

## 4. Consequence: `L^2` is already the cheapest local-magnitude interface

Suppose one tries to rule out target endpoint loading by proving, for the physical prime-minus-rough residual, a source-specific `p`th-moment estimate on the natural window. Equation (8) shows the relevant contradiction scale:

\[
\int_{U-W_X}^{U+W_X}|P_{\rm phys}(t)|^pdt
=o\!\left(Xa_X^{p-1}\right)
\tag{16}
\]

would exclude an `ANF-175`-type coherent charge of size `a_X` with the same mass/span geometry. But increasing `p` does not weaken the arithmetic burden in any coefficient-generic sense: the matched obstruction rescales by exactly the corresponding factor `a_X^{p-2}`. The `p=2` target

\[
\int_{U-W_X}^{U+W_X}|P_{\rm phys}(t)|^2dt=o(Xa_X)
\tag{17}
\]

is therefore already the simplest member of the entire local-magnitude family. A fourth or sixth moment is useful only if the **actual prime/rough source** gives a strict saving unavailable to the matched packet; the moment order itself supplies no escape.

This separates two ideas which can otherwise be conflated. Higher moments are powerful when large values are sparse and one needs to penalize their concentration. Here the target-sized value is forced to persist by elementary phase continuity across the complete `X/a_X` coherence interval. There is no concentration defect for a higher moment to expose. To beat the packet one must instead prevent the carrier-relative placement which creates the charge, obtain a source-specific cancellation theorem below the generic local-magnitude scale, or control directly the signed dyadic / Fejer scale-slope defect of `ANF-169`--`ANF-172`.

This finding does **not** say that higher moments of the physical residual are useless. A genuinely arithmetic theorem may well prove (16), and a higher-moment expansion could be the vehicle for proving it. What is ruled out is treating higher moment order, convexity, or generic large-values technology as additional information by themselves. Any successful use must derive a strict source-specific saving which the explicit prime-scale matched control does not satisfy.

## 5. Prior-art and novelty audit

No new load-bearing external theorem is needed. The only analytic upper input in (11)--(12) is the local `L^2` Montgomery--Vaughan estimate already recorded and audited in `ANF-177` and `SOURCES.md`; the `L^infinity` bound is the triangle inequality. The moment, distribution-function, and Orlicz conclusions are then elementary consequences of the persisted packet's pointwise coherence.

A targeted audit of higher-moment and large-values work for Dirichlet polynomials found the expected extensive literature on using moments to control exceptional large values, but no external result is required for the present conclusion. The Mathia-specific delta is the opposite-direction stress test: the source-matched endpoint packet has a full interval of critical-size values, so **every** fixed local magnitude statistic is forced to the corresponding coherence-scale order. `ANF-177` established this only for `L^2`; the present result closes the whole fixed local-magnitude hierarchy and identifies the level-set geometry behind that saturation.

## Verdict

The prime-scale endpoint-memory obstruction is not merely mean-square sharp. On its natural twist coherence window of width `X/a_X`, the matched packet has magnitude `Theta(a_X)` at every point. Hence every fixed local `L^p` moment has order `X a_X^(p-1)`, every nondegenerate fixed magnitude penalty has full-window mass, and the critical large-value set itself has measure `Theta(X/a_X)`.

Accordingly, replacing the `L^2` interface by fourth moments, higher fixed moments, or generic large-values/Orlicz penalties does not move the analytic frontier. The next theorem still has to be source-specific: beat the generic `L^2` scale `Xa_X` (or the equivalent `p`th-moment scale), prove that the actual prime/rough placement cannot assemble the coherent charge, or attack the exact signed Fejer scale-slope statistic directly.