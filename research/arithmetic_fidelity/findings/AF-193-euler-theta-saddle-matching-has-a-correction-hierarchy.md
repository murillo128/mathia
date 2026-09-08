# AF-193 — Euler theta-to-saddle matching has a correction hierarchy

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `BOUNDARY-CLASSIFICATION`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-190 gives a finite-overlap Jacobi-theta profile when `m/q^2 -> tau in (0,infinity)`, while AF-192 gives the actual Euler-band discrepancy throughout the growing-overlap regime `m -> infinity`, `m/q^2 -> 0`. AF-192 notes that its large-`kappa=m/q` endpoint has the same leading small-`tau` saddle as the AF-190 profile. That agreement is real, but it has two distinct strengths: logarithmic matching holds throughout the overlap `q << m << q^2`, whereas **multiplicative** matching to the leading modular theta profile requires the sharper scale `m >> q^{4/3}`.

Fix

\[
a=\sigma x>0,
\qquad
q\to\infty,
\qquad
m\to\infty,
\qquad
\kappa=\frac mq\to\infty,
\qquad
\tau=\frac{m}{q^2}\to0,
\tag{1}
\]

and retain the AF-192 damping/alignment condition

\[
m q\delta\to0.
\tag{2}
\]

Let `D_delta` be the reciprocal-band Euler discrepancy from AF-192, with

\[
T_\delta=\frac{\pi}{q\delta}.
\tag{3}
\]

Define the leading small-`tau` theta expression

\[
L_{q,m}(a)
=
2\sqrt{\frac{8}{\pi m}}
\exp\!\left[
-aq+\frac{2a^2q^2}{\pi^2m}
\right].
\tag{4}
\]

Then AF-192 implies the sharper comparison

\[
\boxed{
\log\frac{D_\delta}{L_{q,m}(a)}
=
-\frac{4a^4}{3\pi^4}\frac{q^4}{m^3}
+O\!\left(\frac{q^6}{m^5}+\frac qm\right)
+o(1).
}
\tag{5}
\]

Consequently, if

\[
\lambda_\delta=\frac{q^4}{m^3},
\tag{6}
\]

then:

- if `lambda_delta -> 0`, equivalently `m/q^{4/3} -> infinity`,

\[
\boxed{\frac{D_\delta}{L_{q,m}(a)}\to1;}
\tag{7}
\]

- if `lambda_delta -> lambda in (0,infinity)`,

\[
\boxed{
\frac{D_\delta}{L_{q,m}(a)}
\longrightarrow
\exp\!\left[-\frac{4a^4}{3\pi^4}\lambda\right];
}
\tag{8}
\]

- if `lambda_delta -> infinity`, while `(1)` still holds,

\[
\boxed{\frac{D_\delta}{L_{q,m}(a)}\to0.}
\tag{9}
\]

Thus the first ratio-level matched-asymptotic overlap between the moving-saddle law and the **leading** modular theta profile is

\[
\boxed{
q^{4/3}\ll m\ll q^2.
}
\tag{10}
\]

At the critical transition `m ~ c q^{4/3}` the leading theta expression misses a finite factor

\[
\boxed{
\exp\!\left[-\frac{4a^4}{3\pi^4c^3}\right].
}
\tag{11}
\]

For `q << m << q^{4/3}`, the two descriptions still agree at the leading exponential-correction scale, but the omitted saddle corrections accumulate to a nonvanishing, eventually exponentially large, relative effect. Therefore “the theta and saddle regimes meet as `tau -> 0`” is correct only after specifying the asymptotic accuracy being claimed.

## Small-`tau` modular form of the AF-190 profile

AF-190 defines

\[
\Phi_{a,\tau}(u)
=
\sum_{n\in\mathbb Z}
\exp\!\left[
-an-\frac{\pi^2\tau}{8}(n-u)^2
\right],
\qquad
M(a,\tau)=\sup_{0\le u\le1}\Phi_{a,\tau}(u).
\tag{12}
\]

Completing the square gives

\[
\Phi_{a,\tau}(u)
=
\exp\!\left[
-au+\frac{2a^2}{\pi^2\tau}
\right]
\sum_{n\in\mathbb Z}
\exp\!\left[
-\frac{\pi^2\tau}{8}
\left(n-u+\frac{4a}{\pi^2\tau}\right)^2
\right].
\tag{13}
\]

Poisson summation for the shifted Gaussian is exact:

\[
\sum_{n\in\mathbb Z}e^{-(\pi^2\tau/8)(n-b)^2}
=
\sqrt{\frac{8}{\pi\tau}}
\left[
1+2\sum_{\ell\ge1}
 e^{-8\ell^2/\tau}
\cos(2\pi\ell b)
\right].
\tag{14}
\]

Substituting

\[
b=u-\frac{4a}{\pi^2\tau}
\tag{15}
\]

into `(13)` shows uniformly for `u in [0,1]` that

\[
\Phi_{a,\tau}(u)
=
\sqrt{\frac{8}{\pi\tau}}
\exp\!\left[
\frac{2a^2}{\pi^2\tau}-au
\right]
\left(1+O(e^{-8/\tau})\right).
\tag{16}
\]

The derivative of the bracket in `(14)` is also `O(e^{-8/\tau})` uniformly in `u`. Since the explicit factor contributes logarithmic derivative `-a`, for sufficiently small `tau` the whole profile is strictly decreasing on `[0,1]`. Hence its maximum is at `u=0`, and

\[
\boxed{
M(a,\tau)
=
\sqrt{\frac{8}{\pi\tau}}
\exp\!\left[
\frac{2a^2}{\pi^2\tau}
\right]
\left(1+O(e^{-8/\tau})\right).
}
\tag{17}
\]

If one substitutes `tau=m/q^2` into the **profile expression** `2e^{-aq}M(a,tau)/q`, equation `(17)` becomes exactly

\[
\frac{2e^{-aq}}q M\!\left(a,\frac{m}{q^2}\right)
=
L_{q,m}(a)
\left(1+O(e^{-8q^2/m})\right).
\tag{18}
\]

This is a classical modular/Poisson asymptotic for the AF-190 theta function. It is important not to overread `(18)`: AF-190 proves its discrepancy theorem for `tau` tending to a fixed positive value. Equation `(18)` by itself does **not** extend that theorem uniformly to a triangular array with `tau -> 0`. The actual discrepancy in the regime `(1)` is supplied by AF-192, and `(5)` measures precisely how it compares with the small-`tau` theta-profile extrapolation.

## Exact large-`kappa` saddle expansion

AF-192 uses

\[
\Psi(a,\kappa)
=
-\frac{2a}{\pi}
\arctan\frac{\pi\kappa}{2a}
+
\kappa\log
\frac{\pi\kappa}{\sqrt{4a^2+\pi^2\kappa^2}}.
\tag{19}
\]

Set

\[
y=\frac{2a}{\pi\kappa}.
\tag{20}
\]

For large `kappa`, using `arctan(1/y)=pi/2-arctan(y)`, equation `(19)` becomes

\[
\Psi(a,\kappa)+a
=
\frac{2a}{\pi}
\left[
\arctan y-
\frac{\log(1+y^2)}{2y}
\right].
\tag{21}
\]

The convergent power series for `|y|<1` is

\[
\boxed{
\Psi(a,\kappa)+a
=
\sum_{j\ge0}
\frac{(-1)^j(2a/\pi)^{2j+2}}
{(2j+1)(2j+2)}
\kappa^{-(2j+1)}.
}
\tag{22}
\]

Therefore

\[
q\Psi(a,\kappa)
=
-aq
+
\frac{2a^2}{\pi^2}\frac{q^2}{m}
-
\frac{4a^4}{3\pi^4}\frac{q^4}{m^3}
+
O\!\left(\frac{q^6}{m^5}\right).
\tag{23}
\]

The AF-192 prefactor has

\[
\alpha_*(a,\kappa)
=1-\frac{4a}{\pi^2\kappa}+O(\kappa^{-3}),
\tag{24}
\]

\[
H(a,\kappa)
=\frac{\pi^2\kappa}{4}
\left(1+O(\kappa^{-2})\right),
\tag{25}
\]

and hence

\[
C(a,\kappa)q^{-1/2}
=
2\sqrt{\frac{8}{\pi m}}
\left(1+O(\kappa^{-1})\right).
\tag{26}
\]

Substituting `(23)` and `(26)` into AF-192's exact asymptotic law gives `(5)`.

## The full correction hierarchy

Equation `(22)` shows that `q^{4/3}` is not an isolated magic exponent. It is the first member of a nested asymptotic hierarchy. After retaining saddle-exponent terms through index `J`, the first omitted term has scale

\[
\frac{q^{2J+4}}{m^{2J+3}}.
\tag{27}
\]

Thus a truncation through `J` is ratio-accurate once

\[
\boxed{
m\gg q^{(2J+4)/(2J+3)}.}
\tag{28}
\]

For `J=0`, equation `(28)` gives `m >> q^{4/3}`, exactly `(10)`. As more saddle corrections are retained, these thresholds decrease monotonically toward the lower growing-overlap boundary `m >> q`.

Equivalently, if `m=q^\beta` with `1<\beta<2`, only finitely many correction terms are needed for ratio accuracy at every fixed `beta>1`, but the required number grows as `beta downarrow1`. This is the precise sense in which the moving-saddle description remains uniform while any fixed low-order small-`tau` expansion becomes nonuniform near the `m~q` end.

## Stress tests and boundaries

### No extension of AF-190 is being smuggled in

The modular identity `(14)` is an exact statement about the theta profile `M(a,tau)`. AF-190's theorem connects that profile to the Euler discrepancy only when `m/q^2` tends to a fixed positive `tau`. The triangular-array discrepancy for `tau -> 0` is obtained independently from AF-192. This separation is essential: profile matching is not automatically theorem uniformity.

### The correction is not a different fidelity phase

Nothing singular happens to the underlying Euler response at `m~q^{4/3}`. The scale marks only when a one-term asymptotic representation becomes multiplicatively accurate. AF-192 remains the governing actual-discrepancy theorem on both sides. The correction hierarchy is therefore an **accuracy boundary**, not a new mechanism boundary.

### The critical factor has the correct sign

The first omitted coefficient in `(22)` is negative. Hence the leading theta expression overestimates the AF-192 saddle amplitude at the critical `q^{4/3}` scale, producing the factor in `(11)` strictly below one. This sign is fixed by the alternating Taylor series in `(21)` and is not a normalization artifact.

### The endpoint assumptions are necessary

The comparison requires `kappa=m/q -> infinity` so that the large-`kappa` expansion is valid, and `tau=m/q^2 ->0` so that AF-192 rather than AF-190 governs the actual discrepancy. At `m/q^2` of order one the discrete theta comb is the correct mechanism, not a perturbative large-`kappa` expansion of the moving saddle.

### No rational-prime specificity follows

As in AF-187--AF-192, the control family and Euler local logarithm are generalized-prime compatible. The theorem calibrates how accurately one compression asymptotic passes between two source-complexity regimes. It does not distinguish ordinary rational primes from matched Beurling systems and has no direct RH consequence.

## Prior art and novelty assessment

The mathematical ingredients are classical. NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.2 for Jacobi theta Fourier series and §20.7(viii) for lattice-parameter/modular transformations, provides authoritative theta-function background. The classical Poisson summation formula applied to a shifted Gaussian gives `(14)` directly; standard references include Titchmarsh and Zygmund, as summarized by the *Encyclopedia of Mathematics* entry **“Poisson summation formula.”**

Richard B. Paris, **“The discrete analogue of Laplace's method,”** *Computers & Mathematics with Applications* 61(10) (2011), 3024--3034, DOI `10.1016/j.camwa.2011.03.092`, is prior art for systematic asymptotic expansions of positive discrete sums around a dominant term/saddle and already underlies the AF-192 audit.

A targeted search over Jacobi-theta modular limits, Poisson-summed Gaussian lattice profiles, discrete Laplace asymptotics, moving saddles, and transition matching did not identify an authoritative source stating the Euler-specific ratio threshold `(5)`--`(11)` for the AF parity controls. This is not evidence of priority, and no novelty claim is made. The durable result is the exact internal consistency boundary between two already-established Arithmetic Fidelity asymptotic descriptions.

## Consequences for Arithmetic Fidelity

AF-190 and AF-192 do not merely touch qualitatively. Their relationship has a measurable fidelity hierarchy. In the common endpoint `q << m << q^2`, the leading modular theta profile and the moving-saddle law share the same first exponential correction, but preserving the **actual readout to relative error `o(1)`** needs the additional condition `m >> q^{4/3}` unless the next saddle correction is retained.

This is a concrete instance of the line's central distinction between coarse survival and stable quantitative recovery: two compressed descriptions can agree at leading scale while still differ by an order-one multiplicative factor. For downstream RH-facing mechanisms, agreement of rate functions or dominant exponents should therefore not be treated as fidelity of the observable itself; the required asymptotic order must be fixed before declaring two compression regimes equivalent.