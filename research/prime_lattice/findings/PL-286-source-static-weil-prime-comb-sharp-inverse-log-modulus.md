# PL-286 — The source-static Weil prime comb retains the sharp inverse-logarithmic form modulus

**Evidence:** `EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + PRIME-LATTICE/KRONECKER`

**Status:** `FULL-COMB-SHARPNESS + GENERIC-CHANNEL-CANCELLATION-EXHAUSTED`

## Claim

Inside the source-static aperture interval

\[
J=\left(\frac{\log 4}{2},\frac{\log 5}{2}\right),
\]

the active prime powers in Suzuki's fixed-domain localized Weil form are exactly `2,3,4`. Let

\[
h_n(a)=\frac{\log n}{a},
\qquad
c_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
A_n(a)=2-h_n(a),
\]

and, on `I=(-1,1)`, write

\[
q_h(w)=\int_{-1}^{1-h}w(x+h)\overline{w(x)}\,dx
\]

for `0<h<2`. The arithmetic moving part of the fixed-domain form is

\[
P_a(w)=-2\sum_{n\in\{2,3,4\}}c_n\,\Re q_{h_n(a)}(w).
\]

With the logarithmic energy from `PL-285`,

\[
E_{\log}(w)=\int_{\mathbb R}\log(2+|\xi|)|\widehat w(\xi)|^2\,d\xi,
\]

the full three-channel prime comb has the same worst-case order as an individual channel:

\[
\boxed{
\sup_{w\ne0}
\frac{|P_b(w)-P_a(w)|}{E_{\log}(w)}
=\Theta\!\left(\frac1{\log(1/|a-b|)}\right)
\qquad (b\to a),
}
\]

for every fixed `a in J`.

More explicitly,

\[
\boxed{
\liminf_{b\to a}
\log\frac1{|a-b|}
\sup_{w\ne0}
\frac{|P_b(w)-P_a(w)|}{E_{\log}(w)}
\ge
2\bigl(c_2A_2(a)+c_3A_3(a)\bigr)>0.
}
\]

At `a=0.8`, the displayed lower constant is approximately

\[
1.90624296.
\]

The scalar and archimedean continuous-kernel terms in Suzuki's fixed-domain formula vary locally Lipschitzly in `a`, while its logarithmic principal form is independent of `a`. Consequently the **complete source-static fixed-domain Weil form**, not just its separate arithmetic channels, also has sharp worst-case `H^log` quadratic-form modulus of inverse-logarithmic order.

Thus the caveat left open in `PL-285` is closed at the generic form-domain level: **simultaneous motion of the active `2,3,4` von-Mangoldt channels does not produce a better worst-case modulus through coefficient cancellation.** Any useful cancellation theorem for transport of the `a=0.8` ground-state margin must use information about the actual low spectral branch, not merely the finite arithmetic sum acting on an arbitrary logarithmic-energy vector.

## 1. Upper bound from the sharp single-channel modulus

`PL-285` proves, for every fixed interior shift,

\[
|q_{h+\delta}(w)-q_h(w)|
\le
\frac{2+o(1)}{\log(1/|\delta|)}E_{\log}(w).
\]

For a fixed `a in J` and `b->a`,

\[
\delta_n(a,b)=h_n(b)-h_n(a)
=(\log n)\left(\frac1b-\frac1a\right),
\]

so for each `n in {2,3,4}`,

\[
\log\frac1{|\delta_n(a,b)|}
=
\log\frac1{|a-b|}+O(1).
\]

There are only three active channels. Summing their estimates with the fixed positive weights `c_n` gives

\[
\sup_{w\ne0}
\frac{|P_b(w)-P_a(w)|}{E_{\log}(w)}
=
O\!\left(\frac1{\log(1/|a-b|)}\right).
\]

The unresolved point after `PL-285` was whether the zeta-specific combination might cancel strongly enough that this finite-sum upper bound was not sharp. The following construction rules that out.

## 2. Exact high-frequency witness

For `xi in R`, take the fixed-domain plane wave

\[
w_\xi(x)=e^{i\xi x},\qquad x\in I,
\]

and extend it by zero outside `I`. Its autocorrelation is exact:

\[
q_h(w_\xi)=(2-h)e^{i\xi h}.
\]

Therefore

\[
P_a(w_\xi)
=-2\sum_{n\in\{2,3,4\}}c_nA_n(a)
\cos\bigl(\xi h_n(a)\bigr).
\]

With the unitary Fourier convention used in `PL-285`, modulation of `1_I` gives

\[
E_{\log}(w_\xi)
=(2+o(1))\log|\xi|
\qquad(|\xi|\to\infty).
\]

The indicator endpoints do not invalidate membership in the logarithmic form domain: `widehat{1_I}` has square decay `O(|eta|^{-2})`, which is integrable against `log(2+|eta|)`.

## 3. Kronecker phase locking makes the `2` and `3` channels add coherently

Put

\[
d=\frac1b-\frac1a.
\]

Then the phase increment of the `n`-th channel between `a` and `b` is

\[
\xi\bigl(h_n(b)-h_n(a)\bigr)=\xi d\log n.
\]

The key prime-lattice input is the rational independence

\[
\frac{\log2}{\log3}\notin\mathbb Q,
\]

which follows from unique factorization. Hence the continuous Kronecker flow

\[
y\longmapsto(y\log2,y\log3)\pmod{2\pi}
\]

is dense in the two-torus.

Fix an arbitrarily small phase tolerance `epsilon>0`. Choose once and for all a number `y=y_epsilon` such that

\[
y\log2=\pi+O(\epsilon)\pmod{2\pi},
\qquad
y\log3=\pi+O(\epsilon)\pmod{2\pi}.
\]

For every sufficiently small nonzero `d`, choose

\[
\xi_d=\frac{y}{d}+t_d.
\]

A second use of the same irrational flow, now with velocity `(log2/a,log3/a)`, allows `t_d` to be chosen so that

\[
\xi_d\frac{\log2}{a}=O(\epsilon)\pmod{2\pi},
\qquad
\xi_d\frac{\log3}{a}=O(\epsilon)\pmod{2\pi}.
\]

For fixed `epsilon`, the correction `t_d` may be kept uniformly bounded as `d->0`: a sufficiently long finite segment of a minimal irrational torus flow is an `epsilon`-net of the compact torus. Therefore

\[
|\xi_d|=\frac{|y|}{|d|}+O(1),
\qquad
\log|\xi_d|=\log\frac1{|d|}+O_\epsilon(1).
\]

For the `2` and `3` channels the old phases are consequently near `0`, while the new phases are near `pi`. Their cosines change coherently from `+1` to `-1`.

The third channel does not spoil the construction because the exponent-lattice relation

\[
4=2^2,
\qquad
\log4=2\log2,
\]

doubles both phases. Thus its old phase is near `0` and its increment is near `2pi`; its cosine remains near `+1`. In exponent-vector language, the witness flips the basis directions associated with `2` and `3` while the `2e_2` channel closes one full phase turn.

## 4. Lower bound

For the phase-locked sequence above and fixed `epsilon`, continuity of `A_n(b)` gives

\[
P_b(w_{\xi_d})-P_a(w_{\xi_d})
=
4\bigl(c_2A_2(a)+c_3A_3(a)\bigr)
+O(\epsilon)+o_{d\to0}(1).
\]

The `n=4` contribution is `O(epsilon)+O(|d|)` because its cosine is nearly unchanged and `A_4(b)-A_4(a)=O(d)`.

Meanwhile

\[
E_{\log}(w_{\xi_d})
=(2+o(1))\log\frac1{|d|}.
\]

Since

\[
\log\frac1{|d|}
=
\log\frac1{|a-b|}+O(1)
\]

for fixed `a`, division yields

\[
\liminf_{b\to a}
\log\frac1{|a-b|}
\sup_{w\ne0}
\frac{|P_b(w)-P_a(w)|}{E_{\log}(w)}
\ge
2\bigl(c_2A_2(a)+c_3A_3(a)\bigr)-O(\epsilon).
\]

Letting `epsilon->0` proves the stated positive lower bound. Together with the finite-sum upper estimate, this gives the sharp `Theta(1/log)` order for the complete active prime comb.

At `a=0.8`,

\[
A_2=2-\frac{\log2}{0.8}\approx1.13356602,
\qquad
A_3=2-\frac{\log3}{0.8}\approx0.62673464,
\]

so

\[
2\left(
\frac{\log2}{\sqrt2}A_2
+
\frac{\log3}{\sqrt3}A_3
\right)
\approx1.90624296.
\]

This is many orders of magnitude larger than the endpoint eigenvalue margin from `PL-284` before the inverse logarithm is paid; it is a route obstruction, not a positivity estimate.

## 5. Passing from the prime comb to the complete fixed-domain form

Source 56 in `research/prime_lattice/SOURCES.md` gives Suzuki's fixed-domain formula. On a compact subinterval of `J`, its `a`-dependence separates into:

1. the finite moving prime-power translations above;
2. elementary scalar terms such as `-log a`;
3. an archimedean continuous-kernel term depending smoothly on `a`;
4. an `a`-independent logarithmic principal form.

The scalar and continuous-kernel differences are locally `O(|a-b|)||w||_2^2`. Since

\[
E_{\log}(w)\ge(\log2)\|w\|_2^2,
\]

their normalized modulus is `O(|a-b|)`, hence

\[
O(|a-b|)
=o\!\left(\frac1{\log(1/|a-b|)}\right).
\]

They cannot cancel the phase-locked prime witness at inverse-logarithmic scale. Therefore the whole source-static fixed-domain Weil quadratic form has the same sharp worst-case `Theta(1/log)` modulus on the canonical logarithmic form domain.

## 6. Prior-art and novelty audit

The external load-bearing source is already source 56:

- **Masatoshi Suzuki**, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2` (2026). Its fixed-interval formula supplies the finite von-Mangoldt translation comb with lags `log(n)/a`, the `a`-independent logarithmic principal form, and the smoother remaining aperture dependence.

The torus-density input is the classical Kronecker theorem, applied only to the rationally independent frequencies `log2` and `log3`. No novelty is claimed for Kronecker recurrence, for logarithmic regularity, or for the exponent identity `log4=2log2`.

A targeted search by the combined structures -- Suzuki's localized Weil form, compressed prime-power translations, logarithmic form moduli, and Kronecker phase alignment -- did not locate a published theorem giving this full-comb lower bound. The durable Mathia contribution claimed here is correspondingly narrow: an exact line-local consequence showing that the possible finite-channel cancellation explicitly left open by `PL-285` does **not** improve the generic canonical form modulus on the first `2,3,4` source-static interval.

No `SOURCES.md` update is needed: the zeta-specific formula is already anchored by source 56, while the new lower bound is derived here from that formula and classical Kronecker recurrence.

## 7. Adversarial checks and boundaries

- **Full comb, not a single channel.** The witness is built simultaneously for `2,3,4`; it closes the exact cancellation caveat in `PL-285` for the generic form-domain norm.
- **The square channel is controlled structurally.** It is not discarded. The relation `log4=2log2` makes its phase increment approximately `2pi` whenever the `2` channel increment is approximately `pi`.
- **Both old and new phases are controlled.** The first Kronecker choice fixes the desired increments; the bounded second correction `t_d` aligns the base phases without changing those increments asymptotically.
- **The witness lies in the domain.** `1_I e^{i xi x}` has finite logarithmic Fourier energy for every finite `xi`; its energy grows as `2 log|xi|+o(log|xi|)`.
- **The result is worst-case, not ground-state-specific.** It does not show that Suzuki's actual lowest eigenfunction realizes this phase locking, nor that its spectral tail has the generic worst-case size.
- **No claim across a source event.** The argument stays inside `J`; activation at `a=log5/2` is a different perturbation regime.
- **No positivity radius.** The theorem does not transport the positive `a=0.8` certificate by itself.
- **No broad novelty claim.** The mechanism is classical Kronecker recurrence specialized to an exact finite arithmetic comb; the value is elimination of a live line-local escape route.
- **Matched non-zeta controls remain possible.** Any finite translation family with two rationally independent frequencies and a harmonically related third can exhibit the same worst-case phase locking. This is a no-go result for generic cancellation, not rational-prime rigidity.

## Consequence for the line

The generic fixed-domain transport problem is now exhausted more sharply than in `PL-285`. Neither termwise estimates nor cancellation among the entire active `2,3,4` von-Mangoldt comb improves the canonical inverse-logarithmic rate on an arbitrary `H^log` energy ball.

The surviving route must therefore be **state-specific**. A useful bridge from the simple positive ground state at `a=0.8` must prove information unavailable to the phase-locked witnesses above: stronger uniform regularity of the actual low branch, a quantitative high-frequency-tail bound for that branch, cancellation forced by its eigen-equation or variational structure, or another source-specific identity. Generic arithmetic-channel cancellation is no longer an admissible explanation for a better transport modulus.