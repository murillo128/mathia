# PL-407 — Cubic source replacement has an explicit prime-variance power-saving threshold

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + QUANTITATIVE-TARGET`.

**Parent findings:** `PL-404`, `PL-405`, `PL-406`.

## Claim

`PL-406` moves the remaining `PL-404` source-replacement problem into the signed prime short-interval variance sector through the exact triangular identity

\[
Q_{K,H}(f)
=\frac1H\int_0^\infty K''(t)T_f(Ht)\,dt.
\]

That identity gives a sharp quantitative calibration of what a power-saving prime-variance theorem would have to deliver in order to preserve the `H^{-7/4}` zero-sensitive layer.

Let `Delta C_X(h)` be the **source-subtracted even off-diagonal correlation remainder** at lag `h`, with `Delta C_X(0)=0`, and put

\[
\Delta T_X(L)
:=\sum_{h\in\mathbb Z}(L-|h|)_+\Delta C_X(h).
\tag{1}
\]

For the even cubic kernel from `PL-406`,

\[
K_\eta(x)
=|x|e^{-\eta|x|^3}\sin(\pi|x|^3/6),
\tag{2}
\]

linearity of the triangular representation gives the exact normalized source error

\[
\boxed{
\mathcal E_\eta(X,H)
:=\frac1{XH}\sum_{h\ge1}K_\eta(h/H)\Delta C_X(h)
=\frac1{2XH^2}\int_0^\infty K_\eta''(t)\Delta T_X(Ht)\,dt.
}
\tag{3}
\]

Assume, in the effective support of `K_eta''` and with harmless tails treated separately, an LPZ-shaped power-saving remainder

\[
|\Delta T_X(L)|
\ll
XL\left(\frac{L}{X}\right)^\mu(\log X)^B,
\qquad \mu\ge0,
\tag{4}
\]

uniformly for the relevant `L`. Since `K_eta(t)=(pi/6)t^4+O_eta(t^7)` at the origin and decays exponentially at infinity,

\[
\int_0^\infty |K_\eta''(t)|t^{1+\mu}\,dt<\infty.
\tag{5}
\]

Substitution of (4) into (3) therefore yields

\[
\boxed{
|\mathcal E_\eta(X,H)|
\ll_{\eta,\mu}
H^{-1}\left(\frac HX\right)^\mu(\log X)^B.
}
\tag{6}
\]

The `PL-404` layer survives if this is `o(H^{-7/4})`. For a polynomial scale

\[
H=X^\theta,
\qquad 0<\theta<1,
\tag{7}
\]

a robust sufficient condition is

\[
\boxed{
\mu>\frac{3\theta}{4(1-\theta)}.
}
\tag{8}
\]

Equivalently, for a given power saving `mu`, the cubic bridge is certified throughout

\[
\boxed{
\theta<\frac{4\mu}{3+4\mu}.
}
\tag{9}
\]

In particular, a square-root relative power saving `mu=1/2` has the calibration boundary

\[
\boxed{\theta=\frac25.}
\tag{10}
\]

Thus an LPZ-shaped square-root variance remainder would be enough for every fixed polynomial regime `H=X^theta` with `theta<2/5`. At the exact endpoint `theta=2/5`, the polynomial powers tie; a genuine logarithmic saving such as `(log X)^{-nu}`, `nu>0`, would still give the required little-`o`, whereas a bare `O` estimate would not. Above `2/5`, the bound (4) with `mu=1/2` cannot by itself certify the `H^{-7/4}` layer.

This `2/5` is **not a universal barrier** for the cubic statistic and is not claimed as a theorem about the true prime-variance error. It is the boundary of the route that first bounds the variance remainder in absolute value by (4) and then inserts that estimate into the exact signed kernel (3). Cancellation against the oscillating `K_eta''`, or a more structured zero-pair calculation of the one tested functional, can in principle do better.

## 1. Exact normalization

The one-sided source-replacement error in `PL-405`--`PL-406` has normalization `1/(XH)`. Because `Delta C_X` is extended evenly and the cubic kernel has `K_eta(0)=0`,

\[
\sum_{h\ge1}K_\eta(h/H)\Delta C_X(h)
=
\frac12
\sum_{h\in\mathbb Z}K_\eta(h/H)\Delta C_X(h).
\tag{11}
\]

Applying `PL-406`, equation (17), to the difference of the actual and model correlation kernels gives

\[
\sum_{h\in\mathbb Z}K_\eta(h/H)\Delta C_X(h)
=
\frac1H\int_0^\infty K_\eta''(t)\Delta T_X(Ht)\,dt,
\tag{12}
\]

which proves (3). The factor `1/2` is therefore the symmetrization factor from positive lags; the extra `1/H` comes from the triangular representation itself.

The definition (1) is deliberately source-relative. For a prime short-interval second moment, `Delta T_X` is the remainder after subtracting the diagonal and the singular-series/main-term contribution consistent with the correlation model. This avoids pretending that a raw Selberg integral and the `PL-404` source are literally identical before the standard main terms and interval-boundary conventions have been aligned.

## 2. The exponent curve

Insert (4) with `L=Ht` into (3):

\[
\begin{aligned}
|\mathcal E_\eta(X,H)|
&\le
\frac1{2XH^2}
\int_0^\infty
|K_\eta''(t)|
\,XHt
\left(\frac{Ht}{X}\right)^\mu
(\log X)^B\,dt\\
&\ll
H^{-1}
\left(\frac HX\right)^\mu
(\log X)^B
\int_0^\infty|K_\eta''(t)|t^{1+\mu}\,dt.
\end{aligned}
\tag{13}
\]

The moment in the last line is finite. Near zero,

\[
K_\eta''(t)=2\pi t^2+O_\eta(t^5),
\tag{14}
\]

and at infinity it is a polynomial times `e^{-eta t^3}`.

Dividing (6) by the target scale `H^{-7/4}` gives

\[
H^{3/4}\left(\frac HX\right)^\mu(\log X)^B.
\tag{15}
\]

For `H=X^theta`, the polynomial exponent is

\[
\frac{3\theta}{4}-\mu(1-\theta).
\tag{16}
\]

Strict negativity is exactly (8). If equality holds, the conclusion depends on the logarithmic factor; this is why the endpoint in (10) is a calibration boundary rather than an automatically admissible point.

Two useful values are

\[
\theta=\frac13
\quad\Longrightarrow\quad
\mu>\frac38,
\tag{17}
\]

and

\[
\theta=\frac8{33}
\quad\Longrightarrow\quad
\mu>\frac6{25}.
\tag{18}
\]

These are precisely in the polynomial shift ranges already highlighted in `PL-406`: `1/3` is the lower exponent in the 2026 almost-all correlation theorem of Matomaki--Radziwill--Shao--Tao--Teravainen, while `8/33` is the lower exponent in the earlier Matomaki--Radziwill--Tao long-shift theorem. Those unconditional results provide logarithmic rather than power precision, so (17)--(18) are **targets**, not consequences of the published theorems.

## 3. Relation to quantitative prime-variance / zero-pair theory

Languasco--Perelli--Zaccagnini give quantitative versions of the Goldston--Montgomery transfer under RH. In their notation, prime short-interval mean-square remainders are studied with hypothetical errors of the schematic form

\[
R_J(X,\vartheta)
\ll
X^2\vartheta^{1+\alpha}
\times \text{logarithmic factor},
\tag{19}
\]

which, at additive length `L=theta X`, has the same power shape

\[
XL(L/X)^\alpha
\tag{20}
\]

as (4). Their result is a conditional quantitative **transfer framework** between such variance errors and zero pair-correlation errors; it does not supply (4) unconditionally with a chosen positive `mu`.

The present finding uses that literature only as calibration. It asks: *if* the source-subtracted variance relevant to (3) could be controlled with an LPZ-shaped exponent `mu`, what exponent is actually needed by the already-fixed cubic zero layer? Equations (8)--(10) answer that question exactly.

This distinction matters. Calling `mu=1/2` a “square-root saving” describes the relative factor `(L/X)^{1/2}` in the hypothetical variance error. It is not an attribution that LPZ prove that saving in the required arithmetic range.

## 4. Compatibility checks

### The modified Mangoldt observable is harmless in the whole square-root window

`PL-406` proves that replacing

\[
\Lambda_1(n)=\frac{\phi(n)}n\Lambda(n)
\]

by the ordinary von Mangoldt function costs `o(H^{-7/4})` whenever, up to the displayed logarithmic factors there,

\[
H=o(X^{4/7}).
\tag{21}
\]

Since `2/5<4/7`, every fixed polynomial regime below the square-root calibration boundary (10) lies safely inside that replacement window. Thus the `Lambda_1` normalization does not become a new bottleneck for (8).

### The diagonal remains projected out

The source-relative remainder was defined with `Delta C_X(0)=0`, consistently with `K_eta(0)=0`. The logarithmically divergent Ramanujan energy isolated in `PL-405` therefore never enters (3). Equation (8) calibrates the **off-diagonal** remainder left after the exact projection already proved in `PL-406`.

### Sharp interval boundaries are not hidden

The exact identity (3) is algebraic for a finitely supported correlation sequence. Connecting a classical short-interval variance theorem to `Delta T_X` still requires matching its sharp/smooth `n`-cutoff and additive/multiplicative interval convention. Such bookkeeping can contribute lower-order boundary terms and must be verified in any future theorem application. The exponent calculation above is conditional on those terms lying below the same right side as (4); it does not silently identify different Selberg-integral conventions.

## 5. Prior-art / novelty audit

The triangular kernel identity is already recorded as classical structure in `PL-406`. The Goldston--Montgomery prime-variance / pair-correlation correspondence and its quantitative refinements are also prior art.

The main literature anchor is:

- **Alessandro Languasco, Alberto Perelli, Alessandro Zaccagnini**, “Explicit relations between pair correlation of zeros and primes in short intervals,” *Journal of Mathematical Analysis and Applications* **394** (2012), 761--771, DOI `10.1016/j.jmaa.2012.04.058`. The paper studies quantitative transfer between remainders of pair correlation and prime short-interval mean squares, under RH, with power/logarithmic error parameters.

Targeted literature searches for the specific `H^{-7/4}` cubic source scale, its induced exponent curve `mu>3 theta/(4(1-theta))`, and the resulting `theta=2/5` square-root boundary found no exact prior occurrence. A repository audit likewise found no earlier `PL-*` statement of this threshold. The safe novelty claim is therefore only a **line-specific derived calibration** of the already-established `PL-404`--`PL-406` observable, not a new theorem about prime variance or pair correlation.

## 6. Adversarial audit

1. **`2/5` is method-relative.** The derivation takes an absolute value before integrating against `K_eta''`. It discards the signed cubic cancellation that `PL-406` explicitly identifies as the live opportunity. Failure above `2/5` for `mu=1/2` is failure of this bound, not failure of the statistic.

2. **The hypothesis is stronger than current unconditional input.** Existing almost-all-shift results in the relevant polynomial ranges provide fixed logarithmic savings or qualitative `o(1)`, not a fixed positive power `(L/X)^mu` at the source-subtracted variance level required by (4).

3. **LPZ is calibration, not proof of (4).** Their quantitative equivalence theorems are conditional on RH and on assumed error shapes. No statement here upgrades those hypothetical remainders to an unconditional estimate.

4. **Endpoint logic is logarithm-sensitive.** At `theta=2/5`, `mu=1/2`, a power count alone gives only the same `H^{-7/4}` scale. A negative logarithmic exponent can make it little-`o`; a logarithmic loss cannot. Therefore the correct statement is a boundary, not `theta<=2/5` without qualification.

5. **Source/model alignment is a real gate.** A theorem for a standard Selberg integral must be converted to the exact source-subtracted `Delta T_X` in (1), including diagonal, mean, and cutoff terms. Equation (3) is exact after that alignment; the alignment itself is not proved here for every published convention.

6. **No RH implication is claimed.** Even a proof of (4) strong enough for (8) would only complete the arithmetic source replacement at the precision demanded by the parent cubic mechanism. Any final RH consequence would still have to pass all remaining hypotheses and continuation steps in `PL-404`.

## Consequence for the line

`PL-406` says that generic logarithmic averaged Hardy--Littlewood estimates are too coarse and points toward the signed prime-variance / zero-pair sector. The present calibration turns that qualitative statement into a concrete exponent target.

For a power-saving variance route, the arithmetic task is now:

\[
|\Delta T_X(L)|
\ll XL(L/X)^\mu\times\text{logs}
\quad\text{with}\quad
\mu>\frac{3\theta}{{4(1-\theta)}}
\]

on the `L\asymp H=X^theta` range sampled by the cubic kernel. A square-root relative saving reaches every `theta<2/5`; at the modern lower shift exponents, the required powers are only `3/8` at `theta=1/3` and `6/25` at `theta=8/33`.

This creates a clean fork for the next research pass. Either seek a genuinely power-saving, source-subtracted short-interval variance estimate in an intersecting polynomial window, plausibly through quantitative zero-pair machinery, or exploit the **sign of `K_eta''` directly** and beat the absolute-value calibration. The latter is the only route here that could cross the `2/5` boundary without strengthening the variance remainder itself.