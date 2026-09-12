# PL-285 — Fixed-domain Weil translations are norm-discontinuous with a sharp logarithmic form modulus

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + POSITIVE-TOPOLOGY-IDENTIFICATION`

**Status:** `ENDPOINT-GAP-TRANSPORT-BARRIER + SHARP-HLOG-MODULUS + SOURCE-STATIC-INTERVAL`

## Claim

The finite-window spectral gap recorded in `PL-284` cannot be propagated to a neighboring aperture by a naive bounded-operator perturbation argument after scaling the localized Weil problem to a fixed interval. The obstruction is already present inside every source-static interval: the active prime terms move through compressed translations, and compressed translations are strongly but not operator-norm continuous on `L^2`.

Scale Suzuki's localized form from `(-a,a)` to `I=(-1,1)`. Every active prime-power channel contains a compressed translation with shift

\[
h_n(a)=\frac{\log n}{a}\in(0,2].
\]

For

\[
(T_h f)(x)=\mathbf 1_I(x)\mathbf 1_I(x+h)f(x+h),
\qquad 0<h<2,
\]

one has, for every fixed interior `h in (0,2)`,

\[
\boxed{
\lim_{\delta\to0,\,\delta\ne0}
\|T_{h+\delta}-T_h\|_{L^2(I)\to L^2(I)}=2.
}
\]

Thus the absence of a new prime-power activation does not make the fixed-domain arithmetic perturbation norm-small on `L^2`.

The canonical logarithmic form domain restores continuity, and the generic rate can be sharpened completely. For the zero extension of `f`, set

\[
E_{\log}(f)=
\int_{\mathbb R}\log(2+|\xi|)|\widehat f(\xi)|^2\,d\xi,
\qquad
\|f\|_{H^{\log}}:=E_{\log}(f)^{1/2}.
\]

Then

\[
\boxed{
\|T_{h+\delta}-T_h\|_{H^{\log}\to L^2}
\sim
\frac{2}{\sqrt{\log(1/|\delta|)}}
\qquad(\delta\to0).
}
\]

More importantly for the Rayleigh quotient, the corresponding autocorrelation quadratic form

\[
q_h(f):=\langle T_hf,f\rangle
\]

has the stronger exact estimate

\[
\boxed{
|q_{h+\delta}(f)-q_h(f)|
\le
\omega(\delta)E_{\log}(f),
}
\]

where

\[
\omega(\delta)
:=
\sup_{\xi\in\mathbb R}
\frac{|e^{i\delta\xi}-1|}{\log(2+|\xi|)}
=
\frac{2+o(1)}{\log(1/|\delta|)}.
\]

The inverse-logarithmic order is sharp for every interior shift: for each fixed `h in (0,2)` there are smooth compactly supported wave packets `f_delta` for which

\[
\frac{|q_{h+\delta}(f_\delta)-q_h(f_\delta)|}
{E_{\log}(f_\delta)}
\ge
\frac{c_h+o(1)}{\log(1/|\delta|)}
\]

with `c_h>0`. Hence `PL-285`'s previous Cauchy--Schwarz form estimate was quantitatively nonoptimal by one square root, but its basic route diagnosis was correct: **bare canonical `H^log` regularity gives only logarithmic aperture control, and that logarithmic scale is intrinsic rather than an artifact of the frequency split.**

For a source-static finite prime-power set, this improves the generic arithmetic form comparison from `O(1/sqrt(log))` to `O(1/log)`. It still does not come close to transporting the `8.9e-18` endpoint margin through the macroscopic interval from `a=0.8` to the next activation `a=log(5)/2` without substantially stronger information about the actual low-energy branch or source-specific cancellation.

## 1. Fixed-domain prime translations

Masatoshi Suzuki's fixed-interval scaling writes the varying-support problem on `I=(-1,1)` with an `a`-independent logarithmic principal form and an `a`-dependent bounded part. The arithmetic contribution is a finite sum of translation quadratic forms indexed by the prime powers with

\[
n\le e^{2a},
\]

and the displacement of the `n`-th active channel is exactly

\[
h_n(a)=\frac{\log n}{a}.
\]

The remaining bounded terms are explicit continuous-kernel and elementary aperture terms. Suzuki's proof of continuity of the lowest eigenvalue uses a uniform logarithmic-form bound, compact embedding into `L^2`, and joint continuity of these bounded terms. It does not use operator-norm continuity of the moving translations.

At `a=0.8`, the active prime powers are exactly

\[
2,3,4,
\]

and the next source event is

\[
a_5=\frac{\log5}{2}\approx0.8047189562.
\]

Thus the entire interval

\[
0.8<a<a_5
\]

is source-static. Nevertheless the three lags `log(n)/a` continue to move, so the family is not constant between source events.

## 2. Ambient `L^2` operator norm is maximally discontinuous

Fix `h in (0,2)`. Choose a nonzero smooth bump `chi` whose support and the relevant translates remain strictly inside `I`. For `delta != 0`, put

\[
\xi_\delta=\frac{\pi}{\delta},
\qquad
f_\delta(x)=\chi(x)e^{i\xi_\delta x}.
\]

On the common interior region, changing the lag from `h` to `h+delta` multiplies the carrier by

\[
e^{i\xi_\delta\delta}=-1.
\]

Translation continuity of the fixed envelope then gives

\[
\frac{\|(T_{h+\delta}-T_h)f_\delta\|_2}
{\|f_\delta\|_2}
\longrightarrow2.
\]

Since both compressed translations are contractions,

\[
\|T_{h+\delta}-T_h\|\le2,
\]

so the lower and upper bounds meet. Compression at the endpoints does not regularize the translation family because the witnessing packets can be kept strictly inside the common overlap.

For an active prime power `n`,

\[
h_n(b)-h_n(a)
=(\log n)\left(\frac1b-\frac1a\right).
\]

Thus `b->a` makes the geometric displacement small but not the corresponding `L^2` operator perturbation.

## 3. The `H^log -> L^2` modulus is exactly inverse square-root logarithmic

Zero-extend `f` to the real line. Compression is contractive, so

\[
\|(T_{h+\delta}-T_h)f\|_2
\le
\|(\tau_\delta-I)\widetilde f\|_2.
\]

By Plancherel,

\[
\|(\tau_\delta-I)\widetilde f\|_2^2
=
\int_{ℝ}|e^{i\delta\xi}-1|^2|\widehat f(\xi)|^2\,d\xi.
\]

Hence

\[
\|T_{h+\delta}-T_h\|_{H^{\log}\to L^2}
\le
\sup_{\xi}
\frac{|e^{i\delta\xi}-1|}
{\sqrt{\log(2+|\xi|)}}.
\]

Let `L_delta=log(1/|delta|)`. Evaluating at `xi=pi/delta` gives the lower scale `2/sqrt(L_delta+O(1))`. Conversely, split the multiplier according to `|delta xi|<exp(-sqrt(L_delta))` and its complement. In the first region the numerator is exponentially small in `sqrt(L_delta)`; in the second,

\[
\log(2+|\xi|)
\ge
L_\delta-\sqrt{L_\delta}+o(L_\delta),
\]

while the numerator is at most `2`. Therefore

\[
\sup_{\xi}
\frac{|e^{i\delta\xi}-1|}
{\sqrt{\log(2+|\xi|)}}
=
\frac{2+o(1)}{\sqrt{L_\delta}}.
\]

The interior wave packets from the previous section also satisfy

\[
E_{\log}(f_\delta)
=
\bigl(L_\delta+O(1)\bigr)\|\chi\|_2^2,
\]

because modulation translates the rapidly decaying Fourier transform of `chi`. Their `L^2` translation difference tends to `2||chi||_2`, so the compressed family attains the same asymptotic order and constant. Thus

\[
\boxed{
\sqrt{\log(1/|\delta|)}
\|T_{h+\delta}-T_h\|_{H^{\log}\to L^2}
\longrightarrow2.
}
\]

This sharpens the sufficient frequency-split estimate previously stored in this finding and proves that the inverse-square-root logarithmic operator modulus cannot be improved using only the ambient `H^log` norm.

## 4. Quadratic forms gain one square root

The spectral transport problem does not require the full `H^log -> L^2` operator norm of a channel. It requires control of its quadratic-form value. Here the autocorrelation structure gives an exact improvement.

For the zero extension of `f`,

\[
q_h(f)
=
\int_{ℝ}\widetilde f(x+h)\overline{\widetilde f(x)}\,dx.
\]

With the unitary Fourier convention,

\[
q_h(f)
=
\int_{ℝ}e^{ih\xi}|\widehat f(\xi)|^2\,d\xi.
\]

Therefore

\[
q_{h+\delta}(f)-q_h(f)
=
\int_{ℝ}
e^{ih\xi}(e^{i\delta\xi}-1)|\widehat f(\xi)|^2\,d\xi,
\]

and directly

\[
|q_{h+\delta}(f)-q_h(f)|
\le
E_{\log}(f)
\sup_{\xi}
\frac{|e^{i\delta\xi}-1|}{\log(2+|\xi|)}.
\]

The same two-region argument gives

\[
\omega(\delta)
:=
\sup_{\xi}
\frac{|e^{i\delta\xi}-1|}{\log(2+|\xi|)}
=
\frac{2+o(1)}{L_\delta}.
\]

The order is genuinely sharp on the finite interval. Choose `chi in C_c^infinity(I)` such that

\[
C_h:=\int\chi(x+h)\overline{\chi(x)}\,dx\ne0,
\]

which is possible for every `h in (0,2)`, and again take a carrier frequency `xi_delta=pi/delta`, allowing an `O(1)` adjustment of the carrier if one wants the real part rather than the complex autocorrelation. Then

\[
|q_{h+\delta}(f_\delta)-q_h(f_\delta)|
\longrightarrow2|C_h|,
\]

whereas

\[
E_{\log}(f_\delta)
=
(L_\delta+O(1))\|\chi\|_2^2.
\]

Consequently

\[
\frac{|q_{h+\delta}(f_\delta)-q_h(f_\delta)|}
{E_{\log}(f_\delta)}
\ge
\frac{2|C_h|/\|\chi\|_2^2+o(1)}{L_\delta}.
\]

Thus the quadratic-form modulus is `Theta(1/log(1/|delta|))` in the canonical logarithmic energy scale. The earlier `O(1/sqrt(log))` form estimate obtained by applying Cauchy--Schwarz to the operator bound is valid but loses a square root.

## 5. Consequence for a source-static Weil interval

For a fixed active prime power,

\[
\delta_n(a,b)
=h_n(b)-h_n(a)
=(\log n)\left(\frac1b-\frac1a\right).
\]

On any compact source-static aperture interval and for `b->a`,

\[
\log\frac1{|\delta_n(a,b)|}
=
\log\frac1{|a-b|}+O(1).
\]

Therefore a normalized `H^log` energy ball

\[
\|f\|_2\le1,
\qquad
E_{\log}(f)\le M
\]

obeys, channelwise,

\[
|q_{h_n(b)}(f)-q_{h_n(a)}(f)|
=
O\!\left(
\frac{M}{\log(1/|a-b|)}
\right).
\]

A finite source-static arithmetic sum inherits this upper modulus, with constants depending on its finitely many von-Mangoldt coefficients. Smooth variation of those coefficients and Suzuki's continuous-kernel/elementary terms contributes its own ordinary compact-interval modulus and must be tracked separately in any certificate.

This improves the generic scaling diagnosis after `PL-284`. If a full form comparison had a bound of schematic size

\[
\frac{CM}{\log(1/|a-b|)}
\]

and had to fit below a positive margin `m`, the ambient estimate would require

\[
\log\frac1{|a-b|}
\gtrsim
\frac{CM}{m}.
\]

For the literature-level certificate

\[
m_{0.8}=8.9\times10^{-18},
\]

this is much better than the previous `m^{-2}` diagnosis, but it is still astronomically restrictive for order-one `CM`. By contrast, the actual source-static distance to the next activation is

\[
\frac{\log5}{2}-0.8
\approx4.7189562\times10^{-3}.
\]

No certified radius is claimed here: an explicit transport theorem still needs constants for the complete fixed-domain form and a uniform logarithmic-energy bound for every competing low state. The point is structural. **The generic form-domain modulus has now been optimized, and even the sharp generic rate is only inverse logarithmic.** Any useful bridge across a macroscopic fraction of the source-static interval must exploit information not contained in a bare `H^log` energy bound.

## 6. Prior-art and novelty audit

The load-bearing literature source remains source 56 in `research/prime_lattice/SOURCES.md`:

- **Masatoshi Suzuki**, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2` (2026). Its fixed-interval formula supplies the moving lags `log n/a`, the logarithmic principal form, and the qualitative compactness argument proving continuity of the lowest eigenvalue.

Source 58 supplies the computer-assisted `a=0.8` positivity margin and parity-resolved spectral data used in `PL-283`--`PL-284`. It does not provide a neighboring-aperture transport theorem.

The underlying facts about translation groups and function spaces of logarithmic smoothness are classical. A targeted audit of logarithmic Sobolev/Besov difference characterizations confirms that logarithmic regularity is an established functional-analytic scale; no novelty is claimed for the existence of such moduli. The exact multiplier identities above are elementary Plancherel calculations specialized to Suzuki's compressed autocorrelation channel. The durable Mathia delta is the **sharp route diagnosis**: the operator modulus in the canonical topology is exactly inverse-square-root logarithmic, while the quadratic form relevant to the variational problem improves exactly to inverse logarithmic order.

No new `SOURCES.md` entry is required because the external load-bearing zeta claims are already covered by sources 56 and 58; the sharp modulus itself is proved here directly.

## 7. Adversarial checks and boundaries

- **Same finding, stronger proof.** This revision keeps `PL-285` rather than allocating a new ID because it sharpens the same endpoint-transport/topology claim. The previous sufficient `O(1/sqrt(log))` estimate remains correct at the operator level; only its use as a quadratic-form rate was nonoptimal.
- **No full-sum lower bound is claimed.** The inverse-log upper estimate passes to any finite source-static sum. The sharp lower witness is channelwise. Arithmetic cancellation among several channels could improve the full zeta-specific sum; proving such cancellation would be new source-specific information rather than a contradiction.
- **Compression is handled exactly.** Zero extension turns `q_h` into the ordinary autocorrelation on the line, so the Fourier multiplier identity does not ignore endpoint truncation.
- **Interior-shift condition matters.** The sharp wave-packet argument is stated for fixed `h in (0,2)`. Threshold activation at `h=2` is governed by the separate soft-onset analysis of `PL-279`.
- **No positivity radius is fabricated.** Continuity plus the positive `a=0.8` margin gives some nonzero neighborhood abstractly, but the present result does not certify its size.
- **No RH inference.** Finite-window positivity, even if extended beyond `0.8`, remains far weaker than Weil positivity for all compact supports.
- **Matched controls survive.** The sharp logarithmic modulus depends only on translation and logarithmic Fourier energy. It is reproduced by non-zeta finite translation families, so it is topology, not rational-prime rigidity.

## Consequence for the line

The immediate post-`PL-284` frontier is now narrower. Ordinary `L^2` operator perturbation is impossible, and the canonical logarithmic topology has been optimized: it yields a sharp `1/sqrt(log)` operator modulus and a sharp `1/log` autocorrelation-form modulus. There is no further generic gain available merely by optimizing the frequency split.

A useful next theorem must therefore exploit **source-specific structure of the low-energy branch**. Viable targets are a positive-Sobolev or stronger regularity estimate for the isolated ground state, a quantitative bound on the ground-state logarithmic spectral tail much sharper than the ambient form-domain bound, cancellation among the simultaneously moving `2,3,4` channels tied to their rational-prime coefficients, or a direct variational/Schur identity for the complete localized Weil form. Any of these would go beyond generic translation topology; without such extra structure, the tiny endpoint certificate cannot be transported a meaningful aperture distance.