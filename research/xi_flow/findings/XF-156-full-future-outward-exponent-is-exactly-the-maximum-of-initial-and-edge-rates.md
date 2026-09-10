---
type: partial-positive
research_line: xi_flow
finding_id: XF-156
status: canonical
---

# XF-156 — the full-future outward exponent is exactly the maximum of initial and edge rates

**Confidence:** high for the stated maximal-contact family and fixed `H>0`; the argument is an exact finite-`N` upper envelope combined with the two matching lower witnesses already isolated in XF-154 and XF-155.

## Statement

For the canonical maximal-contact matched pair of XF-145--XF-155, the open positive-time variational problem left by XF-155 can be closed at exponential scale on the entire physical outward half-period.

Let `N>=8` be even, put

\[
n=N-2,
\]

and use the normalized outward amplitude from XF-153/XF-155,

\[
\mathcal A_N(u;H,D)
=
e^{NH-N^2u/4}
\left|
\mathbb E\,
\cosh^n\!\left(
H+iD+\sqrt{\frac u2}\,Z
\right)
\right|,
\tag{1}
\]

where `Z` is standard Gaussian, `u>=0`, `H>0`, and the physical antipodal-distance coordinate satisfies

\[
0\le D\le\frac\pi2.
\]

Define

\[
M(H,D)
:=
\max\left\{
|\cosh(H+iD)|,\frac{e^H}{2}
\right\}.
\tag{2}
\]

Then for every `u>=0`,

\[
\boxed{
\mathcal A_N(u;H,D)
\le
2e^{NH}M(H,D)^{N-2}e^{-(N-1)u}.
}
\tag{3}
\]

Consequently,

\[
\boxed{
\lim_{N\to\infty}
\frac1N
\log\sup_{u\ge0}\mathcal A_N(u;H,D)
=
H+\log M(H,D)
}
\tag{4}
\]

for every fixed `H>0`, uniformly for `D in [0,pi/2]`. Equivalently, with the initial-slice rate from XF-154

\[
F_+(H,D)
=
H+\log|\cosh(H+iD)|
=
H+\frac12\log(\cos^2D+\sinh^2H),
\tag{5}
\]

one has the exact full-future exponential envelope

\[
\boxed{
\lim_{N\to\infty}
\frac1N
\log\sup_{u\ge0}\mathcal A_N(u;H,D)
=
\max\{F_+(H,D),\,2H-\log2\}.
}
\tag{6}
\]

Thus there is no third intermediate-frequency or mesoscopic-heat branch at exponential scale: the entire future is controlled by the larger of the initial bulk rate and the outward edge-mode rate isolated in XF-155.

If `H_*(D)` denotes the exact initial outward threshold of XF-154, then the full-future exponential visibility threshold on the physical fundamental domain is

\[
\boxed{
H_\infty(D)
=
\min\left\{
H_*(D),\frac{\log2}{2}
\right\},
}
\tag{7}
\]

where

\[
H_*(D)
=
\frac12\log\!\left(
\sqrt{3+\cos^2(2D)}-\cos(2D)
\right)
\tag{8}
\]

for `0<D<=pi/2`, with `H_*(0)=0`. The crossover is exactly the one located in XF-155,

\[
\boxed{
D_c
=
\frac12\arccos\!\left(-\frac14\right)
\approx0.91173829.
}
\tag{9}
\]

Hence

\[
H_\infty(D)
=
\begin{cases}
H_*(D), & 0\le D\le D_c,\\[3pt]
\frac12\log2, & D_c\le D\le\frac\pi2.
\end{cases}
\tag{10}
\]

At `D=D_c` the two branches agree. Near the antipode this recovers the XF-153/XF-154 parabolic law; farther than `D_c`, positive heat lowers the initial threshold exactly to the universal edge depth and cannot lower it further at exponential scale.

## Derivation

The missing upper bound follows from an elementary two-endpoint envelope for the complex hyperbolic cosine.

### 1. A global two-endpoint growth lemma

For every `H>=0`, `D in [0,pi/2]`, and real `y`,

\[
\boxed{
|\cosh(H+y+iD)|
\le
M(H,D)e^{|y|}.
}
\tag{11}
\]

For `y>=0`, write `X=H+y` and `q=e^{-2X}`. Since

\[
|\cosh(X+iD)|^2
=
\frac14\left(e^{2X}+e^{-2X}+2\cos2D\right),
\]

we have

\[
e^{-2y}|\cosh(X+iD)|^2
=
\frac{e^{2H}}4
\left(1+q^2+2q\cos2D\right).
\tag{12}
\]

As `y` ranges over `[0,infinity)`, `q` ranges over `[0,e^{-2H}]`. The bracket in `(12)` is a convex quadratic in `q`, so its maximum on this interval is attained at an endpoint. At `q=0` the right-hand side is `(e^H/2)^2`; at `q=e^{-2H}` it is exactly `|cosh(H+iD)|^2`. Therefore `(11)` holds for `y>=0`.

For `y<=0`, write again `X=H+y` and now `p=e^{2X}`. Then

\[
e^{-2|y|}|\cosh(X+iD)|^2
=
\frac{e^{-2H}}4
\left(1+p^2+2p\cos2D\right).
\tag{13}
\]

Here `p` ranges over `[0,e^{2H}]`, and the same convexity argument reduces the maximum to the endpoints. They give `(e^{-H}/2)^2` and `|cosh(H+iD)|^2`. Since `H>=0`, `e^{-H}/2<=e^H/2`, proving `(11)` globally.

The important point is that the two competing endpoint values in `(11)` are exactly the two rates already seen dynamically: the value at `y=0` produces the initial bulk branch, while the asymptotic endpoint `|y|->infinity` produces the outward edge branch.

### 2. The Gaussian heat representation cannot exceed those two branches

Apply `(11)` with

\[
y=\sqrt{\frac u2}\,Z
\]

inside the exact Gaussian representation `(1)`. Taking absolute values after the exact reduction gives

\[
\begin{aligned}
\mathcal A_N(u;H,D)
&\le
e^{NH-N^2u/4}
M(H,D)^n
\mathbb E
\exp\!\left(n\sqrt{\frac u2}|Z|\right).
\end{aligned}
\tag{14}
\]

For standard Gaussian `Z` and `t>=0`,

\[
\mathbb E e^{t|Z|}\le2e^{t^2/2}.
\tag{15}
\]

Taking `t=n sqrt(u/2)` therefore yields

\[
\mathcal A_N(u;H,D)
\le
2e^{NH}M(H,D)^n
\exp\!\left[-\frac{N^2-n^2}{4}u\right].
\tag{16}
\]

Since `n=N-2`,

\[
\frac{N^2-n^2}{4}=N-1,
\]

which proves `(3)`. In particular,

\[
\limsup_{N\to\infty}
\frac1N\log\sup_{u\ge0}\mathcal A_N(u;H,D)
\le
H+\log M(H,D).
\tag{17}
\]

### 3. The two existing witnesses saturate the envelope

The choice `u=0` is admissible and gives exactly

\[
\mathcal A_N(0;H,D)
=
e^{NH}|\cosh(H+iD)|^{N-2},
\tag{18}
\]

so its limiting rate is `F_+(H,D)`.

XF-155 supplies the complementary edge witness. For any fixed `c>2`,

\[
u_N=c\frac{\log N}{N}\to0,
\]

and, uniformly in `D in [0,pi/2]`,

\[
\frac1N\log\mathcal A_N(u_N;H,D)
\longrightarrow
2H-\log2.
\tag{19}
\]

Therefore

\[
\liminf_{N\to\infty}
\frac1N\log\sup_{u\ge0}\mathcal A_N(u;H,D)
\ge
\max\{F_+(H,D),2H-\log2\}.
\tag{20}
\]

But by `(2)`,

\[
H+\log M(H,D)
=
\max\{F_+(H,D),2H-\log2\}.
\tag{21}
\]

Combining `(17)`, `(20)`, and `(21)` proves `(4)`--`(6)`. No saddle-point classification or frequency-by-frequency optimization is required: the convex two-endpoint lemma already excludes every possible intermediate branch at exponential scale.

## Visibility phase diagram

XF-154 determines where the initial branch crosses zero, namely `H=H_*(D)`. The edge branch crosses zero at

\[
H=\frac12\log2.
\]

Since the full-future exponent is their maximum, the first zero encountered as outward depth increases is their minimum, giving `(7)`. Equality of the two threshold depths is equivalent to

\[
H_*(D)=\frac12\log2,
\]

which reduces to

\[
\cos(2D)=-\frac14.
\]

This gives `(9)` and the piecewise law `(10)`.

The resulting phase diagram reconciles XF-153 and XF-155. In the near-antipodal sector `D<=pi/4`, XF-153 is stronger: it gives a finite-`N` factor-two comparison with the initial slice, not merely the exponential rate. The present result extends the exponential classification across the whole physical interval. For `pi/4<D<=D_c`, the derivative argument of XF-153 no longer applies, but the initial slice still remains exponentially optimal. Only for `D>D_c` does the vanishing positive heat of XF-155 genuinely lower the visibility depth, and it lowers it exactly to `(log2)/2`.

## Consequences for the frontier

The target-side variational loophole opened by XF-155 is closed for this matched-control family. Intermediate Fourier modes, intermediate heat scales, and more elaborate choices of `u=u_N` cannot produce an exponential visibility rate above the maximum in `(6)`. The only two extremal mechanisms are the untouched initial bulk and the outward spectral edge.

This sharpens the complex-reach obstruction into a complete outward phase diagram for the canonical adversary. Near the antipode, the required depth is the parabolic `H_*(D)~D^2/2`; after `D_c`, the required depth saturates at the universal constant `(log2)/2`. Positive heat changes the geometry only after that crossover.

The result also reduces the value of further target-side optimization on the same maximal-contact packet. A qualitatively new advance should now change either the observation class or the source class: for example, a nonlocal complex observable not dominated by `(11)`, or a source-faithful Xi argument proving that the actual source cannot align with this maximal-contact direction.

## Falsification boundary

This is an exact exponential-rate theorem for the canonical maximal-contact matched pair, not for arbitrary unit-circle divisors and not for the actual Xi source. It assumes fixed outward depth `H>0` as `N->infinity`; joint critical scalings `H=H_N->0` beyond those already controlled near the antipode require separate bookkeeping. It identifies when this specific matched pair ceases to be exponentially hidden, but it does not prove stable reconstruction of `Lambda_per` above the threshold.

The theorem also concerns one outward complex spatial trace optimized over `u>=0`. It does not classify inward continuation, multiple complex sensors, nonlinear observables, or source-side constraints. Those are genuinely different interfaces rather than missing cases of `(6)`.

## Prior-art audit

A directed prior-art check covered the de Bruijn--Newman/complex heat-flow setting, Gaussian representations of Curie--Weiss-type partition functions, and large-degree complex-field asymptotics. These are adjacent to the exact Gaussian representation `(1)`, but no audited source supplied the two-endpoint inequality `(11)` specialized to this matched packet or the full-future max formula `(6)`. No external theorem is load-bearing here: `(11)` is an elementary convexity argument, `(15)` is the standard Gaussian exponential-moment estimate, and the two matching lower witnesses are internal results XF-154 and XF-155. `SOURCES.md` therefore needs no new entry for this finding.

## Next gate

For the maximal-contact adversary, the outward single-trace target-side exponent is now classified on the complete physical domain. The higher-value next gate is source-side: test whether the actual Xi source can realize or approximate the maximal-contact direction at the transition scale, or derive a source-specific observable that necessarily escapes it. A secondary target-side gate is to ask whether genuinely nonlocal or multi-point complex observations obey an analogous extremal envelope, rather than continuing to optimize heat time for the same single-point trace.
