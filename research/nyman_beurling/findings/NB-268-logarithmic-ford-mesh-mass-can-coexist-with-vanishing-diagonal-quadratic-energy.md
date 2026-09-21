# NB-268 — Logarithmic Ford mesh mass can coexist with vanishing diagonal quadratic energy

## Status

Source-side route correction / bridge diagnostic. This does **not** assert that the exact Hardy/Nyman quadratic form is small, and it does not assert that zeta zeros realize a matched packet.

## Setup

Keep the resolved-carrier normalization of NB-267,

\[
J=mK,\qquad m\to\infty,\quad K\to\infty,
\]

\[
C_J(w)=\sum_{j=0}^{K-1}c_j e^{ijw/J},\qquad \sum_jc_j=1,
\]

and the live Ford depth

\[
u=\log m+d,\qquad d=O(1).
\]

On the carrier-locked mesh write

\[
D_n=C_J\!\left(\frac{2\pi qn}{Y}+i\frac uY\right),
\qquad
\Delta_m=\frac{2\pi q}{Ym}.
\]

NB-267 proves, for bounded resolved Hilbert cost, that the Euler anchor forces aggregate response

\[
\sum_{|n\Delta_m|\le C\log K}|D_n|\gg m.
\]

The question here is whether that linear aggregate coercivity already yields an order-one quadratic target-side quantity after the live damping \(e^{-u}\asymp m^{-1}\).

## Generic obstruction to an \(\ell^1\)-only bridge

For an arbitrary vector \(a\in\mathbf C^N\),

\[
\|a\|_2^2\ge \frac{\|a\|_1^2}{N},
\]

and this is sharp for equally spread mass. In the NB-267 window,

\[
N\asymp m\log K,
\qquad
\|D\|_1\gtrsim m.
\]

Thus aggregate information alone gives only

\[
e^{-2u}\|D\|_2^2
\gtrsim
\frac1{m\log K},
\]

which tends to zero. An order-one quadratic bridge therefore cannot follow from the NB-267 \(\ell^1\) statement by a generic norm conversion.

The point below is stronger: a completely legal carrier family actually exhibits vanishing diagonal quadratic scale.

## Explicit legal family

Take the uniform positive carrier

\[
c_j=\frac1K,\qquad 0\le j<K.
\]

Then \(\sum c_j=1\) and

\[
\|c\|_2=K^{-1/2},
\]

so the resolved source Hilbert cost is not merely bounded; it decreases.

Put

\[
s_n=n\Delta_m,
\qquad
\beta_m=\frac{u}{Ym}=\frac{\log m+O(1)}{Ym}\to0.
\]

The mesh response is

\[
D_n
=
\frac1K\sum_{j=0}^{K-1}
\exp\!\left((is_n-\beta_m)\frac jK\right).
\]

For \(|s|\le C\log K\), this is a Riemann sum for

\[
G_{\beta_m}(s)
=
\int_0^1 e^{(is-\beta_m)t}\,dt
=
\frac{e^{is-\beta_m}-1}{is-\beta_m}.
\]

Uniformly on that window,

\[
D_n=G_{\beta_m}(s_n)+O\!\left(\frac{1+|s_n|}{K}\right).
\]

Since \(\beta_m\to0\), the limiting profile is

\[
G_0(s)=e^{is/2}\frac{2\sin(s/2)}s.
\]

Its squared modulus is integrable. In fact, by Plancherel for the indicator of \([0,1]\),

\[
\int_{\mathbf R}|G_0(s)|^2\,ds=2\pi.
\]

Because the mesh spacing is \(\Delta_m\asymp m^{-1}\), while \(C\log K\to\infty\), the corresponding lattice sum satisfies

\[
\sum_{|n\Delta_m|\le C\log K}|D_n|^2\asymp m.
\]

The finite-\(K\) Riemann-sum error is harmless: over \(O(m\log K)\) sites its squared contribution is

\[
O\!\left(
 m\log K\,\frac{(\log K)^2}{K^2}
\right)=o(m),
\]

and the cross term is also \(o(m)\) by Cauchy-Schwarz.

At the live depth,

\[
e^{-u}\asymp \frac1m.
\]

Therefore the diagonal damped quadratic diagnostic obeys

\[
\boxed{
 e^{-2u}
 \sum_{|n\Delta_m|\le C\log K}|D_n|^2
 \asymp \frac1m\to0.
}
\]

This same family is fully compatible with the aggregate mesh coercivity of NB-267. Indeed the sinc-type profile has substantial linear mass; NB-267 already guarantees the required \(\Omega(m)\) aggregate response for every legal bounded-cost carrier.

## What this changes

NB-267 remains a genuine source-side linear obstruction: after selecting a favorable angular cone, a matched compatibility packet can turn \(\Omega(m)\) aggregate amplitude into an order-one linear residue after the \(1/m\) damping.

But that mechanism is **not** the same as a quadratic target-side coercivity statement. The uniform carrier shows that the logarithmic Ford mesh may carry the required linear mass while its diagonal quadratic energy, after live damping, still vanishes.

Hence a bridge from NB-267 to the exact Hardy/Nyman distance cannot rely only on

1. the aggregate \(\ell^1\) mesh lower bound, or
2. the diagonal sample energy \(\sum |D_n|^2\).

Any successful target-side argument must use additional structure: for example a nontrivial Gram kernel, off-diagonal terms, concentration forced by the exact projection, or arithmetic information about the actual zero set.

## Adversarial audit and nonclaims

This finding does **not** prove that the exact Hardy/Nyman quadratic form of the uniform carrier is \(o(1)\). The true projected norm may contain positive or coherent off-diagonal contributions that are invisible to the diagonal diagnostic above. If those terms restore an \(\Omega(1)\) lower bound, then they are precisely the missing bridge that should be isolated next.

It also does not invalidate the positive-carrier boundary-layer obstruction of NB-261, and it does not say that actual zeta zeros occupy the favorable mesh sites used in the matched source-side control. The distinction is instead between two coercivity mechanisms: phase-selective linear residue versus unconditional quadratic projected energy.

No new external theorem is load-bearing here. The only generic inputs are the sharp \(\ell^1\)-to-\(\ell^2\) inequality, the Riemann-sum limit, and Plancherel for \(1_{[0,1]}\), so `SOURCES.md` does not need an update.

## Next target

The next non-circular calculation should evaluate, or sharply bound, the **actual Hardy/Nyman Gram form** on this explicit uniform-carrier family. There are two informative outcomes:

- if the exact projected quadratic form is also \(o(1)\), the family becomes a serious candidate escape from the source-side obstruction;
- if it is \(\Omega(1)\), the responsible off-diagonal/Gram structure identifies the missing target-side coercivity mechanism.

Either outcome is more informative than further refinement of the mesh cutoff, because NB-267 has already reached logarithmic radius and the present example shows that diagonal energy alone cannot complete the bridge.
