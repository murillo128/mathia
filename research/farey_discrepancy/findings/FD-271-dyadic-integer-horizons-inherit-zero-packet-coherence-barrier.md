# FD-271 — Dyadic integer horizons inherit the zero-packet coherence barrier

- **Date:** 2026-09-22
- **Status:** proved discrete mean-square bridge + conditional moment calibration
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** Mertens zero packet / discrete logarithmic sampling / multiplicative large-sieve type bound / phase coherence / exceptional horizons
- **Depends on:** FD-261, FD-267, FD-268, FD-269, FD-270
- **Classification:** `EXACT-DERIVED + DISCRETE-LOG-SAMPLING + LARGE-SIEVE-TYPE + ZERO-CLUSTER-BOUND + EXCEPTIONAL-COHERENCE-RESTRICTION`

## Claim

FD-270 showed that the finite critical-zero repair packet has only essentially linear divisor-depth size in Bohr mean over the continuous phase variable `u=log N`. Its explicit surviving loophole was arithmetic sampling: the physical problem only visits

\[
u=\log N,\qquad N\in\mathbb N,
\]

and a zero-density set in continuous `u` could conceivably contain many of those points.

For the same finite simple critical-line packet, that loophole can be reduced to a genuinely sparse exceptional set. Let

\[
F_T(t)
=
2\Re\sum_{0<\gamma\le T}
\frac{t^\rho}{\rho\zeta'(\rho)},
\qquad
\rho=\frac12+i\gamma,
\]

and let

\[
G_{T,N}(d)
=
\sum_{q\mid d}
\bigl(F_T(Nq)-F_T(N(q-1))\bigr).
\]

Normalize away the common critical amplitude,

\[
\widetilde G_{T,N}(d)
=
N^{-1/2}G_{T,N}(d),
\]

and define the depth-band mass

\[
S_{T,x}(N)
=
\sum_{x<d\le2x}
|\widetilde G_{T,N}(d)|.
\]

Finally retain the FD-270 reciprocal-square ledger

\[
\mathcal L_{-1}(T)
=
\sum_{0<\gamma\le T}
\frac1{(1+\gamma)|\zeta'(\rho)|^2}.
\]

Then for every fixed `epsilon>0`, uniformly for integers

\[
2\le T\le x\le X,
\]

one has the discrete dyadic-horizon estimate

\[
\boxed{
\left(
\frac1X
\sum_{X<N\le2X}
S_{T,x}(N)^2
\right)^{1/2}
\ll_\epsilon
x^{1+\epsilon}
\log(2+T)\,
\mathcal L_{-1}(T)^{1/2}.
}
\tag{1}
\]

The logarithm is harmless at power scale and may be absorbed into `x^epsilon`. Thus the power law obtained in FD-270 from continuous Bohr orthogonality survives on the actual integer horizons.

In particular, if

\[
J_{-1}^{\le}(T)
:=
\sum_{0<\gamma\le T}
|\zeta'(\rho)|^{-2}
\le T^{\sigma+o(1)},
\]

then FD-270's dyadic decomposition gives

\[
\mathcal L_{-1}(T)
\le
T^{\max(\sigma-1,0)+o(1)}.
\]

Putting `T=x<=X` in (1),

\[
\boxed{
\left(
\frac1X
\sum_{X<N\le2X}
S_{x,x}(N)^2
\right)^{1/2}
\le
x^{1+\frac12\max(\sigma-1,0)+o(1)}.
}
\tag{2}
\]

Under the same natural `J_{-1}` scale `sigma=1` used as the calibration in FD-270, the integer-sampled RMS is therefore only

\[
\boxed{x^{1+o(1)}}.
\tag{3}
\]

Against the FD-261 threshold `x^(2-beta)`, where

\[
\beta=\log_2\frac32,
\qquad
2-\beta=1.4150374992\ldots,
\]

Markov's inequality now gives the genuinely arithmetic exceptional-set bound

\[
\boxed{
\frac1X
\#\left\{
X<N\le2X:
S_{x,x}(N)\ge x^{2-\beta}
\right\}
\le
x^{-2(1-\beta)+o(1)}
=
x^{-0.8300749985\ldots+o(1)}.
}
\tag{4}
\]

So integer logarithms cannot make threshold-sized critical-zero coherence typical, or even positive-density, on dyadic horizon blocks. Any surviving discrete resonance must live on a polynomially sparse set of horizons at polynomial depth.

## 1. Integer logarithms have an explicit off-diagonal kernel

Write

\[
K_\rho(d)
=
\sum_{q\mid d}
\left(q^\rho-(q-1)^\rho\right).
\]

Then

\[
\widetilde G_{T,N}(d)
=
2\Re P_{T,d}(N),
\qquad
P_{T,d}(N)
=
\sum_{0<\gamma\le T}
a_{\gamma,d}N^{i\gamma},
\]

with

\[
a_{\gamma,d}
=
\frac{K_\rho(d)}
{\rho\zeta'(\rho)}.
\]

The integer average of two frequencies is governed by

\[
A_X(\Delta)
:=
\frac1X
\sum_{X<N\le2X}
N^{i\Delta}.
\]

For

\[
|\Delta|\le X
\]

there is the uniform bound

\[
\boxed{
|A_X(\Delta)|
\ll
\frac1{1+|\Delta|}.
}
\tag{5}
\]

For `|Delta|<=1` this is trivial. For `1<|Delta|<=X`, put

\[
z_n=n^{i\Delta},
\qquad
\delta_n
=
\Delta\log\left(1+\frac1n\right).
\]

On `X<n<=2X`, the increments `delta_n` are monotone, have one sign, and satisfy

\[
|\delta_n|\asymp\frac{|\Delta|}{X}\le1.
\]

Since

\[
z_{n+1}-z_n
=
z_n(e^{i\delta_n}-1),
\]

summation by parts with

\[
(e^{i\delta_n}-1)^{-1}
\]

gives a boundary term plus the total variation of this reciprocal multiplier. Both are `O(X/|Delta|)`: on the displayed increment range its magnitude is `O(1/|delta_n|)`, while its variation along the monotone sequence is bounded by the same endpoint scale. Hence

\[
\left|
\sum_{X<N\le2X}N^{i\Delta}
\right|
\ll
\frac{X}{|\Delta|},
\]

which proves (5). This is the special `n^(it)` instance of the classical Kusmin--Landau/first-derivative mechanism, derived here directly so that no spacing hypothesis on individual zeta zeros is imported.

The restriction `T<=X` is structural for this simple argument. If frequencies are allowed far above the integer scale, the discrete phase derivative can pass through integer resonances and (5) need not follow from this monotone nonresonance calculation. The regime needed below has `|gamma-gamma'|<=T<=x<=X`, so no such aliasing is present.

## 2. Zero clustering costs only logarithms

Expanding the complex packet gives

\[
\frac1X
\sum_{X<N\le2X}
|P_{T,d}(N)|^2
=
\sum_{\gamma,\gamma'\le T}
a_{\gamma,d}\overline{a_{\gamma',d}}\,
A_X(\gamma-\gamma').
\]

The Riemann--von Mangoldt zero-counting formula implies the standard local bound

\[
\#\{\rho:y<\Im\rho\le y+1\}
\ll \log(2+y).
\tag{6}
\]

Our packet contains only simple critical-line zeros, so its unit-interval count is bounded by the count of all nontrivial zeros. Grouping the ordinates `gamma'` according to the integer part of `|gamma-gamma'|`, equations (5)--(6) give uniformly in `gamma<=T`

\[
\sum_{\gamma'\le T}
\frac1{1+|\gamma-\gamma'|}
\ll
\log^2(2+T).
\tag{7}
\]

Indeed each distance shell contains `O(log(2+T))` ordinates and the shell weights form a harmonic sum.

Applying the Schur bound to the positive matrix with entries

\[
(1+|\gamma-\gamma'|)^{-1}
\]

therefore yields

\[
\boxed{
\frac1X
\sum_{X<N\le2X}
|P_{T,d}(N)|^2
\ll
\log^2(2+T)
\sum_{\gamma\le T}|a_{\gamma,d}|^2.
}
\tag{8}
\]

No pair-correlation conjecture, lower bound on zero spacing, or linear independence of zero ordinates is used. Arbitrarily tight zero clusters are already covered by the unconditional local zero-count estimate.

The two logarithms in (7) are not claimed sharp. Classical multiplicative large-sieve/Hilbert-inequality machinery can exploit more cancellation than the absolute Schur bound. For the present question their optimization is irrelevant because every fixed polylogarithmic loss disappears at the exponent scale of FD-261.

## 3. Divisor replication preserves the FD-270 power law

Since

\[
|\widetilde G_{T,N}(d)|^2
\le4|P_{T,d}(N)|^2,
\]

summing (8) over `x<d<=2x` gives

\[
\frac1X
\sum_{X<N\le2X}
\sum_{x<d\le2x}
|\widetilde G_{T,N}(d)|^2
\ll
\log^2(2+T)
\sum_{\gamma\le T}
\frac{
\sum_{x<d\le2x}|K_\rho(d)|^2
}{
|\rho|^2|\zeta'(\rho)|^2
}.
\tag{9}
\]

FD-270 proved, for every fixed `epsilon>0`,

\[
\sum_{x<d\le2x}|K_\rho(d)|^2
\ll_\epsilon
x^{1+\epsilon}
\bigl(1+\min\{\gamma,x\}\bigr).
\tag{10}
\]

Because `T<=x`, equations (9)--(10) imply

\[
\frac1X
\sum_{X<N\le2X}
\sum_{x<d\le2x}
|\widetilde G_{T,N}(d)|^2
\ll_\epsilon
x^{1+\epsilon}
\log^2(2+T)
\mathcal L_{-1}(T).
\tag{11}
\]

Finally Cauchy--Schwarz in the `O(x)` depth coordinates gives

\[
S_{T,x}(N)^2
\ll
x
\sum_{x<d\le2x}
|\widetilde G_{T,N}(d)|^2.
\]

Averaging and taking square roots proves (1), after renaming `epsilon`.

This is the exact discrete counterpart of the Bohr-mean bridge in FD-270. Continuous orthogonality there killed every off-diagonal zero pair exactly. Integer sampling does not, but the residual Gram matrix has only polylogarithmic operator norm in the range `T<=X`. The polynomial depth exponent is unchanged.

## 4. What the exceptional-set bound does and does not remove

Under the natural reciprocal-square moment scale, equation (3) says that a typical dyadic integer horizon carries only linear-depth critical-zero packet mass. The threshold needed to challenge the FD-260 positive-cushion ceiling is `x^(2-beta)`. Squaring the ratio between these scales gives (4):

\[
x^{2}
/
x^{2(2-\beta)}
=
x^{-2(1-\beta)}.
\]

Thus the precise loophole left by FD-270 narrows substantially. The arithmetic sampling set

\[
\{\log N:N\in\mathbb N\}
\]

cannot by itself convert the generic continuous cancellation into a density-one or positive-density coherent packet. At polynomial depth `x=X^(lambda+o(1))`, the exceptional count in one dyadic horizon block is at most

\[
X^{1-2(1-\beta)\lambda+o(1)}.
\tag{12}
\]

This is a true power saving in horizon count for every fixed `lambda>0`.

It is not an all-horizon theorem. A set of size (12) can still contain infinitely many horizons, and the current source-side obstruction often needs information on special large-value subsequences rather than on generic `N`. Nothing here proves that Mertens-large horizons avoid the exceptional phase set. Establishing such an avoidance, or proving that a suitable source-large family has greater counting abundance than (12), would be a materially stronger source--phase coupling statement.

The result also inherits the truncation boundary of FD-270. It controls the finite zero packet only. It does not show that the explicit-formula remainder is negligible in the replicated one-sided repair norm, and it does not turn a two-sided `L^2` bound into a lower or upper bound for the negative part needed by the positivity argument without further work.

## 5. Prior-art boundary and verdict

The ingredients behind the new discrete step are classical. The estimate (5) is a special first-derivative/Kusmin--Landau exponential-sum bound; the Riemann--von Mangoldt formula gives (6); and Montgomery--Vaughan large-sieve/Hilbert-inequality methods are the standard neighboring framework for discrete mean values of exponential or Dirichlet polynomials. A targeted search also found the broader literature on mean values of Dirichlet polynomials sampled at zeta zeros, but not a result matching the present direction of sampling: integer horizons applied to the consecutive-difference/divisor-replicated zero packet.

No classical ingredient is claimed as new. The new content is the composition of the integer log-sampling kernel with the FD-270 replicated-kernel estimate, producing (1)--(4) and closing the specific possibility that the physical lattice `u=log N` generically defeats the Bohr cancellation. The Montgomery--Vaughan and Titchmarsh literature anchors needed for that boundary are already present in `SOURCES.md`, so no source-file change is required.

**Verdict.** The discrete-horizon escape after FD-270 is not a bulk phenomenon. For zero packets truncated at or below the physical depth and for `x<=X`, integer sampling changes the Bohr mean-square bound only by polylogarithmic factors. Under the natural `J_{-1}` scale, threshold coherence can occur on at most an `x^(-0.830074...+o(1))` fraction of a dyadic horizon block. The surviving spectral route must therefore explain a polynomially sparse arithmetic resonance that is correlated with the source horizons relevant to the positivity obstruction, or obtain its strength from the explicit-formula remainder rather than from generic critical-zero phase coherence.
