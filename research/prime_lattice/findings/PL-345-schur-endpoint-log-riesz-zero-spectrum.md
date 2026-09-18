# PL-345 — The Schur endpoint residual is a classical log-Riesz zero spectrum; the critical line is its neutral square-root scale

**Evidence:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`

**Status:** `ENDPOINT-RIESZ-IDENTIFICATION + CRITICAL-LINE-NEUTRAL-EXPONENT + RH-EQUIVALENT-SMOOTHED-BOUND + FULL-COMPLETION-NOT-CAPTURED + NO-INDEPENDENT-RH-RIGIDITY`

## Precise claim

`PL-341` shows that the sharp outer-prime Schur edge is asymptotically saturated by the endpoint exponential pair, and `PL-344` shows that its leading bounded-modulation PNT profile is cancelled by the zeta-pole completion. The next prime-side object obtained by subtracting that PNT profile is not a new spectral observable: it is, up to the line's geometric normalization and an asymptotically negligible lower-shell truncation, the classical first Riesz typical mean for the ordinary Dirichlet frequency `lambda_n=log n`.

Put

\[
B=e^{2a},\qquad q_\tau=1+i\tau,
\]

and define the full logarithmic Riesz residual

\[
\mathcal R_a(\tau)
:=e^{-a}\left[
\sum_{n<B}\Lambda(n)n^{i\tau}\log\frac{B}{n}
-
\int_1^B x^{i\tau}\log\frac{B}{x}\,dx
\right].
\tag{PL345-1}
\]

For every fixed `T>0`, uniformly for `|tau|<=T`,

\[
\boxed{
\mathcal R_a(\tau)
=
-e^{2ia\tau}
\sum_\rho
\frac{e^{(2\rho-1)a}}{(\rho+i\tau)^2}
+O_T(ae^{-a})
}
\tag{PL345-2}
\]

as `a->infinity`. The sum runs over the nontrivial zeros of `zeta`, with multiplicity, and is absolutely convergent for each `a`; the convergence is locally uniform in `tau`.

The actual complex outer-shell response selected by the `PL-341` endpoint pair after subtraction of its PNT continuum profile is

\[
\mathcal E_a(\tau)
:=\frac{e^{-a}}{1-e^{-a}}
\left[
\sum_{e^a\le n<B}\Lambda(n)n^{i\tau}\log\frac{B}{n}
-
\int_{e^a}^{B}x^{i\tau}\log\frac{B}{x}\,dx
\right].
\tag{PL345-3}
\]

The Vinogradov--Korobov PNT remainder already used in `PL-062` gives

\[
\boxed{
\mathcal E_a(\tau)=\mathcal R_a(\tau)+o_T(1).
}
\tag{PL345-4}
\]

Consequently the square-root normalization forced by the Weil/Schur endpoint geometry makes `Re rho=1/2` exactly the neutral growth exponent of this centered prime channel:

\[
|e^{(2\rho-1)a}|=e^{(2\operatorname{Re}\rho-1)a}.
\tag{PL345-5}
\]

Under RH, the zero series in (PL345-2) is an absolutely and uniformly convergent exponential series in `a`, hence a uniformly almost-periodic function. Conversely,

\[
\boxed{
\sup_{a\ge a_0}|\mathcal R_a(0)|<\infty
\quad\Longleftrightarrow\quad
RH.
}
\tag{PL345-6}
\]

This is a useful exact scale identification, but it is **not** an independent RH mechanism. The weight is a classical Riesz typical mean, the zero series follows from the already-continued logarithmic derivative of `zeta`, and the same construction transfers to generalized zeta systems with a corresponding explicit formula. Moreover, at this finer `O(1)` scale the PNT continuum is not interchangeable with the exact completed pole/archimedean sector: for the unmodulated `PL-341` endpoint state the pole-versus-continuum mismatch is `3a+O(1)`. Thus (PL345-2) describes the canonically PNT-centered **prime endpoint residual**, not by itself the full completed Weil quadratic form.

## 1. The Schur endpoint weight is exactly a first Riesz typical mean

The complex matrix element behind `PL-341` is

\[
\frac{e^{-a}}{1-e^{-a}}
\sum_{e^a\le n<e^{2a}}
\Lambda(n)(2a-\log n)n^{i\tau}.
\tag{PL345-7}
\]

If one temporarily restores the omitted lower range `n<e^a`, then

\[
\sum_{\log n<2a}\Lambda(n)n^{i\tau}
\left(1-\frac{\log n}{2a}\right)
=
\frac{1}{2a}
\sum_{n<B}\Lambda(n)n^{i\tau}\log\frac{B}{n}.
\tag{PL345-8}
\]

This is exactly the order-one Riesz typical mean for the general Dirichlet frequency

\[
\lambda_n=\log n.
\]

Typical first means of this form are classical in the Hardy--Riesz theory of general Dirichlet series. Modern treatments include Ingo Schoolmann, *On Bohr's theorem for general Dirichlet series*, Math. Nachr. 293 (2020), 1591--1612, DOI `10.1002/mana.201800542`, and Andreas Defant--Ingo Schoolmann, *Riesz means in Hardy spaces on Dirichlet groups*, Math. Ann. 378 (2020), 57--96, DOI `10.1007/s00208-020-01977-8`. Therefore the weight discovered geometrically in `PL-341` is meaningful -- the geometry selected a classical smoothing without inserting it by hand -- but the smoothing itself is prior art.

## 2. Perron gives an absolutely convergent zero expansion

For `c>1`, the standard first-Riesz Perron formula gives

\[
\sum_{n<B}\Lambda(n)n^{i\tau}\log\frac{B}{n}
=
\frac{1}{2\pi i}
\int_{(c)}
-\frac{\zeta'}{\zeta}(s-i\tau)
\frac{B^s}{s^2}\,ds.
\tag{PL345-9}
\]

This identity is initially justified entirely in the half-plane of absolute convergence of `-zeta'/zeta`. Shifting the contour uses the meromorphic continuation of the logarithmic derivative, not a continued Euler product. The pole of `zeta(s-i tau)` contributes

\[
\frac{B^{1+i\tau}}{(1+i\tau)^2},
\]

each nontrivial zero contributes

\[
-\frac{B^{\rho+i\tau}}{(\rho+i\tau)^2},
\]

and the trivial zeros contribute an exponentially small series after multiplication by `B^{-1/2}=e^{-a}`. The double Perron pole at `s=0` contributes

\[
\left(-\frac{\zeta'}{\zeta}\right)'(-i\tau)
+
\log B\left(-\frac{\zeta'}{\zeta}\right)(-i\tau),
\]

which is `O_T(a)` on every compact real `tau` interval.

The continuum term is elementary:

\[
\int_1^B x^{i\tau}\log\frac{B}{x}\,dx
=
\frac{B^{1+i\tau}-1-q_\tau\log B}{q_\tau^2}.
\tag{PL345-10}
\]

Subtracting (PL345-10), multiplying by `e^{-a}`, and collecting the `s=0` and trivial-zero terms yields (PL345-2).

The zero sum is genuinely absolutely convergent. The Riemann--von Mangoldt count gives `N(U)=O(U log U)`, hence for bounded real `tau`

\[
\sum_\rho\frac1{|\rho+i\tau|^2}<\infty
\]

locally uniformly in `tau`. Since `0<Re rho<1`, the additional factor `e^{(2 Re rho-1)a}` is bounded by `e^a` for each fixed `a`, so the contour residue sum is absolutely convergent without assuming RH.

## 3. Removing the lower half-shell does not change the critical residual

Write `E(x)=psi(x)-x`. The difference between the full residual (PL345-1) and the outer-shell residual (PL345-3) consists of the centered lower range `1<=x<e^a` plus the harmless normalization change

\[
\frac{e^{-a}}{1-e^{-a}}-e^{-a}=O(e^{-2a}).
\]

The normalization change times the outer centered bracket is `o_T(1)` by the PNT. For the lower range, Stieltjes integration by parts gives an integral against `E(x)` with weight

\[
f_{a,\tau}(x)=x^{i\tau}\log(B/x).
\]

Split at `x=e^{a/2}`. Chebyshev's bound controls the first part by `O_T(ae^{a/2})`. On `e^{a/2}<=x<=e^a`, the Vinogradov--Korobov PNT remainder used in `PL-062` gives

\[
E(x)\ll x\exp[-\omega(x)],
\qquad
\omega(e^{a/2})\to\infty
\]

faster than any multiple of `log a`, while

\[
|f'_{a,\tau}(x)|\ll_T a/x.
\]

Therefore

\[
e^{-a}
\left|
\int_{1^-}^{e^a}f_{a,\tau}(x)\,dE(x)
\right|
\ll_T
 ae^{-a/2}
+a\exp[-\omega(e^{a/2})]
=o_T(1).
\tag{PL345-11}
\]

This proves (PL345-4). The outer endpoint geometry therefore selects, to critical `O(1)` accuracy, the same zero spectrum as the full first log-Riesz mean.

## 4. Why `1/2` is the neutral exponent, and why boundedness is already RH

If RH holds, every nontrivial zero is `rho=1/2+i gamma`, and (PL345-2) becomes

\[
\mathcal R_a(\tau)
=
-\sum_\rho
\frac{e^{2ia(\gamma+\tau)}}{(\rho+i\tau)^2}
+O_T(ae^{-a}).
\tag{PL345-12}
\]

The coefficient series is absolutely summable, so the main term is uniformly almost periodic in `a` and uniformly bounded on compact `tau` intervals. Thus the geometry-derived square-root normalization does make the critical line a genuine neutral-growth boundary.

The converse is nevertheless only a repackaged zero-free criterion. At `tau=0`, set

\[
G(B)=
\sum_{n<B}\Lambda(n)\log\frac{B}{n}
-
\int_1^B\log\frac{B}{x}\,dx.
\]

Then `mathcal R_a(0)=B^{-1/2}G(B)`. For `Re s>1`, Fubini gives the exact Mellin identity

\[
\int_1^\infty G(x)x^{-s-1}\,dx
=
\frac1{s^2}
\left(
-\frac{\zeta'}{\zeta}(s)-\frac1{s-1}
\right).
\tag{PL345-13}
\]

If `mathcal R_a(0)` is bounded, then `G(x)=O(x^{1/2})`, so the left side of (PL345-13) is analytic in `Re s>1/2`. Hence the right side has no zeta-zero pole there. The functional equation then forces every nontrivial zero onto `Re s=1/2`, proving RH. The reverse implication follows from the absolutely convergent RH zero series (PL345-12).

Thus the attractive statement

\[
\text{endpoint residual remains bounded at the square-root scale}
\]

is not a new route around RH; it is itself an RH-equivalent smoothed prime-error criterion.

## 5. The PNT residual is not yet the full completed endpoint form

The distinction becomes load-bearing at exactly the scale isolated above. `PL-344` only needed the pole and PNT continuum to agree to relative `o(e^a)` accuracy. That is sufficient for the leading edge but not for the `O(1)` zero residual.

At `tau=0`, use the normalized `PL-341` endpoint state and put `N_a=1-e^{-a}`. The exact pole quadratic form from the factorization in `PL-059`/`PL-344` is

\[
Q_{\rm pole}(u_a^+)
=
\frac1{N_a}
\left[
e^{a/2}N_a+e^{-a/2}a
\right]^2.
\tag{PL345-14}
\]

The matching outer PNT continuum from (PL345-3) is

\[
\frac{e^{-a}}{N_a}
\int_{e^a}^{e^{2a}}(2a-\log x)\,dx
=
\frac{e^a-(1+a)}{N_a}.
\tag{PL345-15}
\]

A direct expansion gives

\[
\boxed{
Q_{\rm pole}(u_a^+)
-
\frac{e^{-a}}{N_a}
\int_{e^a}^{e^{2a}}(2a-\log x)\,dx
=3a-1+o(1).
}
\tag{PL345-16}
\]

So after the leading `e^a` PNT mode cancels, the exact pole differs from the continuum surrogate by a deterministic term much larger than the `O(1)` Riesz zero signal. The scalar and archimedean pieces of the completed Weil form live precisely at logarithmic/moving-frequency scales where such terms can matter. They must be retained before any statement about the **full completed** endpoint quadratic form is made.

This prevents an illicit inference from (PL345-2) to a Hilbert--Polya-type completed spectrum. The result identifies the centered prime channel, not the final completed operator.

## 6. Prior-art and falsification audit

**Riesz smoothing is classical.** Equation (PL345-8) is the standard order-one Riesz typical mean for the ordinary Dirichlet frequency. The modern Schoolmann and Defant--Schoolmann references above explicitly place these means in the Dirichlet-series/Hardy framework. The factor `1/s^2` in (PL345-9) is exactly the classical first-Riesz Perron smoothing.

**The zero divisor is inserted by legitimate analytic continuation, but it is still inserted.** Equation (PL345-2) is an explicit-formula identity obtained from `-zeta'/zeta`; it does not derive zero localization from the exponent lattice. The zero side is therefore evidence for the scale dictionary, not an independent spectral explanation of RH.

**The neutral value `1/2` is geometric but not rational-prime-specific.** The factor `B^{-1/2}=e^{-a}` is not chosen to make (PL345-5) work; it is the square-root normalization already forced by the Weil source and the endpoint Schur optimizer in `PL-341`. That is a genuine structural connection. But any generalized-prime zeta with a simple pole, an analogous explicit formula, and the same square-root normalization produces the same neutral exponent for its own zero divisor. The Beurling matched controls already recorded for `PL-062` therefore prevent this scale selection by itself from being rational-prime RH rigidity.

**No contradiction with `PL-063`/`PL-066`.** Those findings use fixed-depth boundary profiles and natural `e^{-L}` normalization, producing factors `X^{rho-1}`. Here the `PL-341` Schur endpoint state itself concentrates with the aperture and cancels the original `n^{-1/2}` source weight, changing the tested arithmetic sum to a first log-Riesz mean and hence the zero factor to `B^{rho-1/2}`. The different exponent is caused by a different moving state, not by an inconsistency in the explicit formula.

## Consequence for the line

The first centered endpoint continuation after `PL-344` is now classified. The PNT-centered prime residual has an exact and natural critical-scale interpretation, but it collapses to classical Riesz/explicit-formula machinery: critical-line zeros are neutral, off-line zeros are exponentially unstable, and boundedness is already equivalent to RH.

Therefore the line should not pursue

\[
\text{endpoint Schur state}
+\text{PNT subtraction}
+\text{bounded critical residual}
\]

as a new RH mechanism. A genuinely new continuation must instead control the **exact completed same-state form** -- including the `O(a)` pole correction and the archimedean/scalar terms -- or introduce rational-prime-specific structure that is not reproduced by generalized zeta systems. The useful residue of this finding is the scale dictionary (PL345-2)/(PL345-5) and the warning (PL345-16): the critical line appears naturally in the endpoint prime channel, but the first place it appears is already a classical RH-equivalent explicit-formula observable.