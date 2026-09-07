# PL-191 — Escaping fixed-width affine phase windows are already prime-density flat below the short-interval-PNT horizon

## Claim

`PL-189` proves that a fixed positive-width affine phase window whose **normalized center stays bounded** cannot flatten unless the underlying signed macroscopic coefficient measure already cancels. `PL-190` then shows that shrinking windows reduce to a pointwise readout, but leaves fixed positive-width windows with centers tending to infinity as a distinct scalar regime.

That remaining regime is not generically rigid. Inside the same theorem-controlled Kronecker-frequency range as `PL-182`, even the completely unweighted matched control `c_q=1` becomes uniformly flat on every fixed positive-width window whose normalized center escapes to infinity, while its zero-frequency mean remains identically one.

Fix constants

\[
0<a<b<\infty,
\qquad \delta>0,
\]

let `h_X>=1` be arbitrary, and define as in `PL-189`

\[
\mathcal P_X=\{q\text{ prime}:aX<q\le bX\},
\qquad M_X=|\mathcal P_X|,
\qquad
\rho_X=\frac{h_X}{X+h_X},
\]

\[
\omega_X(q)=\rho_X^{-1}\log\left(1+\frac{h_X}{q}\right),
\qquad
F_X(u)=\frac1{M_X}\sum_{q\in\mathcal P_X}e^{iu\omega_X(q)}.
\]

Let `u_X` be real with

\[
|u_X|\longrightarrow\infty
\]

and, for some fixed `eta` with `0<eta<13/15`,

\[
|u_X|\le X^{13/15-\eta}.
\]

Put

\[
I_X=[u_X-\delta/2,u_X+\delta/2].
\]

Then

\[
\boxed{
\sup_{u\in I_X}|F_X(u)|\longrightarrow0,
}
\]

uniformly in the growth of `h_X`. Consequently

\[
\boxed{
\int_{I_X}|F_X(u)|^2\,du\longrightarrow0,
\qquad
F_X(0)=1\ \text{for every sufficiently large }X.
}
\]

Thus the bounded-center hypothesis in `PL-189` is essential. A fixed positive-width window does **not** by itself propagate flattening back to zero frequency once its center escapes: within the short-interval-PNT resolution band, ordinary prime density already supplies a matched control with perfect nonzero zero-mode mass and vanishing local high-frequency profile.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for any coefficient-blind route

\[
\text{fixed positive affine phase width}
+\text{ escaping normalized center}
\longrightarrow
\text{zero-frequency arithmetic cancellation}.
\]

The theorem-level input is exactly the Guth--Maynard short-interval prime-counting result already audited and stored through `PL-181`--`PL-182`. The present statement is a line-specific transfer of `PL-182` from prefix averages to the macroscopic band and to a fixed moving phase window. No new number-theory or harmonic-analysis theorem is claimed.

## 1. Prefix averages at the two band endpoints inherit the `PL-182` scale

For `u in R`, put

\[
t_X(u)=\frac{u}{\rho_X}=u\frac{X+h_X}{h_X}.
\]

Then

\[
e^{iu\omega_X(q)}
=\exp\!\left(it_X(u)\log\left(1+\frac{h_X}{q}\right)\right).
\]

For either fixed `c=a` or `c=b`, define the prefix average

\[
A_{c,X}(u)
:=\frac1{\pi(cX)}
\sum_{q\le cX\atop q\ \mathrm{prime}}
\exp\!\left(it_X(u)\log\left(1+\frac{h_X}{q}\right)\right).
\]

When `PL-182` is applied with cutoff `Y=cX`, its exact phase-resolution parameter is

\[
\nu_{c,X}(u)
=|t_X(u)|\frac{h_X}{cX+h_X}
=|u|\frac{X+h_X}{cX+h_X}.
\]

Writing `kappa_X=h_X/X`, the ratio is

\[
\frac{X+h_X}{cX+h_X}
=\frac{1+\kappa_X}{c+\kappa_X}.
\]

For each fixed `c>0` this factor is bounded above and bounded away from zero uniformly for all `kappa_X>0`. Hence

\[
\nu_{c,X}(u)\asymp_c |u|
\]

uniformly in `h_X`.

On `I_X`, therefore,

\[
\inf_{u\in I_X}\nu_{c,X}(u)\longrightarrow\infty.
\]

Also

\[
\sup_{u\in I_X}\nu_{c,X}(u)
\ll_{a,b}|u_X|+1
\le C_{a,b}X^{13/15-\eta}.
\]

Apply `PL-182` with any slightly smaller exponent margin, for example `eta/2`. Since `cX` is comparable with `X`, the fixed constants are absorbed for all sufficiently large `X`, and the full interval `I_X` remains inside the theorem-controlled range. The uniform quadrature in `PL-182` gives

\[
A_{c,X}(u)=I_{h_X/(cX),t_X(u)}+o(1)
\]

uniformly for `u in I_X`, while its elementary nonstationary-phase estimate gives

\[
|I_{h_X/(cX),t_X(u)}|
\le \frac{2}{\nu_{c,X}(u)}.
\]

Therefore

\[
\boxed{
\sup_{u\in I_X}|A_{a,X}(u)|
+\sup_{u\in I_X}|A_{b,X}(u)|
\longrightarrow0.
}
\]

No assumption on the relative size of `h_X` and `X` occurs.

## 2. Taking the difference of prefixes gives uniform band flattening

The macroscopic band sum is exactly the difference of the two prefix sums:

\[
F_X(u)
=\frac{
\pi(bX)A_{b,X}(u)-\pi(aX)A_{a,X}(u)
}{
\pi(bX)-\pi(aX)
}.
\]

The ordinary prime number theorem gives

\[
\pi(bX)-\pi(aX)\asymp_{a,b}\frac{X}{\log X}
\]

and keeps both ratios `pi(aX)/M_X` and `pi(bX)/M_X` bounded. Hence the uniform prefix bounds imply

\[
\sup_{u\in I_X}|F_X(u)|\longrightarrow0.
\]

Since `|I_X|=delta`, this immediately yields

\[
\int_{I_X}|F_X(u)|^2du\le
\delta\sup_{u\in I_X}|F_X(u)|^2\longrightarrow0.
\]

At zero frequency there is no cancellation at all:

\[
F_X(0)
=\frac1{M_X}\sum_{q\in\mathcal P_X}1
=1.
\]

This is a stronger matched control than a programmable coefficient construction. The coefficients are the canonical constant target and the flattening is forced by one-point prime density plus nonstationary phase.

A particularly conservative explicit example is

\[
u_X=\log X.
\]

It lies far below every fixed power `X^{13/15-eta}` and still gives fixed-width local flattening with `F_X(0)=1`.

## 3. Why this does not contradict `PL-189`

The proof of `PL-189` is a compactness/analytic-uniqueness argument for observation intervals whose normalized centers remain in a fixed compact set. After dephasing, the coefficient measures have uniformly compact frequency support. Weak-* compactness then gives convergence of their Fourier transforms uniformly on each **fixed** compact `u`-interval, so vanishing on a nondegenerate limiting interval forces an entire limiting transform to vanish everywhere.

An interval translated to `u_X->infinity` has no nondegenerate compact limiting observation interval. Compact support of the measure does not prevent its Fourier transform from decaying at high frequency while keeping a nonzero value at the origin. The constant-coefficient prime measure above realizes exactly this possibility.

Accordingly, the bounded-center condition in `PL-189` is not a technical artifact that can be removed by the same normal-family argument. Its failure already occurs before any Möbius, Liouville, zero-divisor, or RH-sensitive target is introduced.

The result also complements `PL-190`. Shrinking windows collapse to a pointwise readout at **every** center. Here the width stays fixed and positive, so the window is genuinely an interval, yet moving that interval through a diverging subresolution normalized phase is enough for ordinary prime-density oscillation to flatten the unweighted carrier throughout the whole interval.

## 4. Adversarial boundaries

This result is deliberately a matched-control obstruction, not a theorem about a hard arithmetic target.

- It does **not** prove that `mu(q+h)`, `lambda(q+h)`, or another target-specific coefficient sequence flattens on the same escaping window. Such a theorem could still contain genuine arithmetic information.
- It does prove that local high-frequency flattening on a fixed positive-width escaping window has no coefficient-blind implication back to the zero-frequency mean. Any such implication for a hard target must use additional target-specific structure.
- The `X^(13/15-o(1))` frequency horizon is inherited from the current Guth--Maynard short-interval-PNT input in `PL-182`. It is theorem technology, not a spectral boundary. This finding says nothing about escaping centers at or beyond that horizon unless a stronger prime-distribution estimate is supplied.
- The width is fixed here. A varying positive width bounded above and below by constants is handled identically. Diverging widths are already covered by the universal mean-square erasure in `PL-187`; shrinking widths reduce to pointwise observation by `PL-190`.
- The carrier is the same scalar one-measure affine/Kronecker observable as `PL-189`. Joint, nonlocal, matrix-valued, completed, or genuinely target-relative operators are not reduced by this argument.
- No analytic continuation or RH statement follows. All cancellation in the control lives inside the ordinary prime-density regime and therefore cannot itself select `Re(s)=1/2`.

## Prior art and novelty audit

The only non-elementary input is the almost-all short-interval prime number theorem of Guth--Maynard already registered in `research/prime_lattice/SOURCES.md` and audited in `PL-181`--`PL-182`. The uniform continuum decay is the integration-by-parts estimate already proved in `PL-182`; passing from a prefix to a fixed macroscopic band is an elementary difference-of-prefixes argument plus the ordinary PNT.

A repository novelty audit found no earlier `prime_lattice` finding carrying out this escaping-center matched control. `PL-189` explicitly listed fixed positive-width windows with centers tending to infinity as outside its theorem, and `PL-190` explicitly preserved them as a distinct remaining regime. The present result therefore closes a recorded scalar loophole rather than creating a parallel reformulation. No external novelty is claimed for the underlying analytic ingredients.

## Consequence for the research line

The scalar affine window trichotomy is now sharper. Bounded-center positive-width flattening is rigid by `PL-189`; shrinking windows add no information beyond a point by `PL-190`; and fixed positive-width windows whose centers escape but remain below the current short-interval-PNT phase horizon can already flatten for the constant matched control while retaining maximal zero-frequency mass.

Thus a surviving scalar mechanism cannot rely on the **geometry of an escaping fixed-width window alone**. It must either prove target-specific arithmetic information at that moving phase, operate at frequencies beyond the current one-point prime-density resolution with an independently justified estimate, or change the observable before scalar Fourier reduction through a genuinely joint/nonlocal/completed coupling. For any proposed subresolution escaping-window statistic, the matched-control audit is now immediate: compare it first with `c_q=1`; if the same flattening occurs there, the effect is phase resolution rather than evidence of a zero-sensitive prime-lattice mechanism.