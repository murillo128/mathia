# PL-285 — Fixed-domain Weil translations are norm-discontinuous but logarithmically continuous on the canonical form domain

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION + POSITIVE-TOPOLOGY-IDENTIFICATION`

**Status:** `ENDPOINT-GAP-TRANSPORT-BARRIER + HLOG-MODULUS + SOURCE-STATIC-INTERVAL`

## Claim

The finite-window spectral gap recorded in `PL-284` cannot be propagated to a neighboring aperture by a naive bounded-operator perturbation argument after scaling the localized Weil problem to a fixed interval. The obstruction is not a new prime-power activation. It is already present inside every source-static interval: the active prime terms move through **compressed translations**, and compressed translations are strongly but not operator-norm continuous on `L^2`.

More precisely, scale Suzuki's localized form from `(-a,a)` to `I=(-1,1)`. Every active prime-power channel `n<=e^(2a)` contains a compressed translation with shift

\[
h_n(a)=\frac{\log n}{a}\in(0,2].
\]

Let

\[
(T_h f)(x)=\mathbf 1_I(x)\mathbf 1_I(x+h)f(x+h),
\qquad 0<h<2.
\]

Then for every interior shift `h_0 in (0,2)`,

\[
\boxed{
\lim_{h\to h_0,\ h\ne h_0}\|T_h-T_{h_0}\|_{L^2(I)\to L^2(I)}=2.
}
\]

Thus an arbitrarily small aperture change produces an order-one change in each moving translation channel in the ambient `L^2` operator norm. In particular, the fact that the source set remains exactly `{2,3,4}` on

\[
0.8<a<\frac{\log5}{2}
\]

does **not** make the fixed-domain arithmetic perturbation small in the topology needed for an ordinary Weyl/Kato bounded-operator estimate.

The canonical form topology behaves differently. If the zero extension of `f` has logarithmic Fourier energy

\[
E_{\log}(f)
:=\int_{\mathbb R}\log(2+|\xi|)|\widehat f(\xi)|^2\,d\xi<\infty,
\]

then, for `|delta|<1` and every `R>=1`,

\[
\boxed{
\|(T_{h+\delta}-T_h)f\|_2^2
\le
\delta^2R^2\|f\|_2^2
+
\frac{4E_{\log}(f)}{\log(2+R)}.
}
\]

Choosing `R=|delta|^(-1/2)` gives the explicit logarithmic modulus

\[
\boxed{
\|(T_{h+\delta}-T_h)f\|_2^2
\le
|\delta|\,\|f\|_2^2
+
\frac{4E_{\log}(f)}{
\log(2+|\delta|^{-1/2})}.
}
\]

Hence compressed translations are uniformly continuous from bounded subsets of the canonical logarithmic form domain into `L^2`, with generic operator modulus of order

\[
\|T_{h+\delta}-T_h\|_{H^{\log}\to L^2}
=O\!\left(\frac1{\sqrt{\log(1/|\delta|)}}\right).
\]

This identifies the correct generic topology behind Suzuki's continuity theorem: **not** `L^2` operator norm, but logarithmic form regularity plus compactness. It also shows why the tiny `a=0.8` certificate does not automatically extend meaningfully toward the next prime threshold. A quantitative transport based only on this ambient `H^log` modulus would require control at a logarithmically tiny aperture scale unless one proves substantially stronger regularity or source-specific cancellation.

The result does not prove that the full finite arithmetic sum is itself norm-discontinuous: cancellations among several simultaneously moving channels are logically possible. What it proves is the sharper route restriction needed here: there is no source-independent **termwise** operator-norm continuity estimate from small movement of the prime shifts, so any useful transport of the `PL-284` spectral gap must use the common quadratic form, stronger regularity of low-energy states, or arithmetic interaction among channels.

## 1. Where the moving translations occur in Suzuki's fixed-domain formula

Masatoshi Suzuki's current construction of the localized Weil operator uses the scaling

\[
w(x)=v(ax),\qquad x\in(-1,1),
\]

to place the varying support problem on one fixed interval. In the resulting Rayleigh quotient, the dominant `a`-independent part is the logarithmic form `L(w)`, while the bounded `a`-dependent part is a finite sum of translation quadratic forms indexed by

\[
n\le e^{2a}
\]
plus an explicit continuous-kernel term. The arithmetic translation displacement is exactly

\[
\frac{\log n}{a}.
\]

Suzuki uses this representation in the proof that the lowest eigenvalue `lambda_a` is continuous. The lower-semicontinuity argument does not invoke operator-norm continuity of those translations. Instead it first obtains a uniform bound on the logarithmic form energy of a minimizing sequence, uses the compact embedding of the logarithmic form domain into `L^2(-1,1)`, and then uses joint continuity of the bounded translation/integral terms along simultaneous convergence `a_j->a` and `w_j->w` in `L^2`.

That distinction matters immediately after `PL-283`--`PL-284`. At `a=0.8`, the active prime powers are exactly

\[
2,3,4,
\]
while the next event is

\[
a_5=\frac{\log5}{2}\approx0.8047189562.
\]

It is tempting to regard the entire open interval `(0.8,a_5)` as a small bounded perturbation of the endpoint operator because no new source enters. The fixed-domain formula shows why this is not automatic: the same three atoms remain active, but their translation locations `log(n)/a` move with `a`.

## 2. Compressed translations have an `L^2` norm jump of two

Fix `h_0 in (0,2)`. For `h` sufficiently close to `h_0`, choose a nonzero smooth bump `chi` supported in a compact interval `K subset I` such that both translated supports needed below remain strictly inside `I`. Put

\[
delta=h-h_0\ne0,
\qquad
\xi_\delta=\frac{\pi}{\delta},
\qquad
f_\delta(y)=\chi(y)e^{i\xi_\delta y}.
\]

On the common interior region where truncation does not act,

\[
T_hf_\delta(x)
=
\chi(x+h)e^{i\xi_\delta(x+h)},
\]

whereas

\[
T_{h_0}f_\delta(x)
=
\chi(x+h_0)e^{i\xi_\delta(x+h_0)}.
\]

Since

\[
e^{i\xi_\delta(h-h_0)}=e^{i\pi}=-1,
\]

the two rapidly oscillating translated packets acquire opposite phases. After factoring out the harmless unimodular phase,

\[
(T_h-T_{h_0})f_\delta
\]

has amplitude asymptotic in `L^2` to the sum of two copies of the same bump. Translation continuity of the fixed bump gives

\[
\frac{\|(T_h-T_{h_0})f_\delta\|_2}
{\|f_\delta\|_2}
\longrightarrow2
\qquad(h\to h_0).
\]

Each `T_h` is a contraction, so

\[
\|T_h-T_{h_0}\|\le2.
\]

The lower and upper bounds therefore meet and prove

\[
\lim_{h\to h_0,\ h\ne h_0}
\|T_h-T_{h_0}\|=2.
\]

This is the finite-interval compressed version of the classical fact that the translation group on `L^2` is strongly continuous but not uniformly/operator-norm continuous. The proof is included because the truncation at the interval endpoints could otherwise look like a possible regularization. It is not: arbitrarily high-frequency packets supported away from the boundary still witness the full norm jump.

For a fixed active integer `n`,

\[
h_n(b)-h_n(a)
=
(\log n)\left(\frac1b-\frac1a\right).
\]

Thus `b->a` makes the geometric displacement tend to zero, but it does not make the corresponding compressed translation tend to its old value in `L^2` operator norm.

## 3. The canonical logarithmic form domain restores continuity

The same high-frequency packets that destroy `L^2` operator-norm continuity have growing logarithmic energy. This is exactly why the topology used by Suzuki is stronger than bare `L^2`.

Extend `f` by zero to the real line. Since compression by `I` is contractive,

\[
\|(T_{h+\delta}-T_h)f\|_{L^2(I)}
\le
\|(\tau_\delta-I)\widetilde f\|_{L^2(\mathbb R)},
\]

up to an irrelevant common translation. Plancherel gives

\[
\|(\tau_\delta-I)\widetilde f\|_2^2
=
\int_{\mathbb R}
|e^{i\xi\delta}-1|^2
|\widehat f(\xi)|^2\,d\xi.
\]

Split the integral at frequency `R>=1`. On `|xi|<=R`,

\[
|e^{i\xi\delta}-1|^2
\le \delta^2\xi^2
\le \delta^2R^2.
\]

On `|xi|>R`, use the crude bound `|e^{i\xi\delta}-1|^2<=4` together with

\[
\int_{|\xi|>R}|\widehat f(\xi)|^2d\xi
\le
\frac{E_{\log}(f)}{\log(2+R)}.
\]

Combining the two pieces proves

\[
\|(T_{h+\delta}-T_h)f\|_2^2
\le
\delta^2R^2\|f\|_2^2
+
\frac{4E_{\log}(f)}{\log(2+R)}.
\]

The convenient choice `R=|delta|^(-1/2)` yields

\[
\|(T_{h+\delta}-T_h)f\|_2^2
\le
|\delta|\|f\|_2^2
+
\frac{4E_{\log}(f)}{
\log(2+|\delta|^{-1/2})}.
\]

No arithmetic input appears in this estimate. It is simply the Fourier tail consequence of the logarithmic regularity already built into the localized Weil form domain.

For normalized vectors in an `H^log` energy ball,

\[
\|f\|_2\le1,
\qquad
E_{\log}(f)\le M,
\]

the right-hand side tends to zero uniformly. Therefore the prime translation terms are uniformly continuous on precisely the kind of compact low-energy sets used in Suzuki's continuity argument, even though they are maximally discontinuous on the full `L^2` unit ball.

## 4. Consequence for quadratic forms and endpoint-gap transport

For one channel,

\[
\left|
\langle(T_{h+\delta}-T_h)f,f\rangle
\right|
\le
\|(T_{h+\delta}-T_h)f\|_2\,\|f\|_2.
\]

Hence the preceding estimate gives a logarithmic modulus for the corresponding quadratic-form coefficient on bounded `H^log` sets. A finite source-static sum inherits the same qualitative modulus, with constants depending only on the finitely many active von-Mangoldt weights and on a compact aperture interval. The smooth continuous-kernel and elementary aperture terms in Suzuki's decomposition can be controlled separately by ordinary uniform continuity on such a compact interval.

This gives a principled perturbative route in the correct topology. If one supplies an explicit bound

\[
E_{\log}(f)\le M
\]
for every normalized state relevant to the bottom of the spectrum throughout a chosen aperture neighborhood, and tracks the bounded part of the form quantitatively, then a positive lower bound at one aperture propagates to a nonzero neighborhood by standard variational comparison.

What is missing is not qualitative continuity; Suzuki already proves that. What is missing is a **useful quantitative modulus with constants strong enough to compete with the certified ground margin**.

For the source-58 certificate transferred in `PL-283`, the reported margin is only

\[
m_{0.8}=8.9\times10^{-18}.
\]

The generic logarithmic modulus above behaves like

\[
O\!\left(\frac1{\sqrt{\log(1/|a-b|)}}\right)
\]

after substituting `delta=(log n)(1/b-1/a)`. If all hidden constants are merely order one, making this generic error smaller than a margin of size `m` requires a scale with

\[
\log(1/|a-b|)
\gtrsim m^{-2}.
\]

For `m=8.9e-18`, this is astronomically smaller than the actual gap

\[
\frac{\log5}{2}-0.8\approx4.72\times10^{-3}.
\]

This last comparison is only an **order-of-magnitude diagnosis**, not a certified radius: the constants in the full form comparison and a uniform explicit `H^log` bound on the relevant ground states have not been extracted here. Its role is to show that ambient logarithmic regularity alone has the wrong quantitative strength to make the endpoint certificate plausibly bridge the whole source-static interval.

## 5. Relation to the existing Prime-Lattice ledger

This result does not duplicate the earlier compressed-shift findings.

`PL-049` concerns the **large-window size** of the complete non-archimedean shift sum and proves `||K_L||=Theta(exp L)` using endpoint states. It does not vary an active lag and does not address continuity in the aperture parameter.

`PL-055` concerns fixed Sobolev smoothing of the large-window boundary family. It proves that compact smoothing removes escaping high-frequency recurrence and produces norm/Schatten convergence to a universal PNT model. The present issue is local in `a`, before any large-window limit, and the relevant regularity is the canonical logarithmic form domain appearing in Suzuki's exact finite-aperture operator.

`PL-268` proves strict monotonicity of the ground level by support inclusion and translation symmetry, but supplies no quantitative slope. `PL-279` shows that a **newly activated** prime-power atom is quadratically soft in the original moving domain; it says nothing about the continuing motion of already active translation lags after fixed-domain rescaling. `PL-283`--`PL-284` give a certified/literature-level positive endpoint and a simple isolated ground state, but explicitly leave neighboring-aperture transport open.

The present finding closes only the simplest attempted bridge:

\[
\text{no new prime atom}
\quad\Longrightarrow\quad
\text{small bounded-operator perturbation in }L^2
\quad\Longrightarrow\quad
\text{transport the }a=0.8\text{ gap}.
\]

The first implication is false at the termwise translation level.

## 6. Prior-art and novelty audit

The load-bearing literature source is already registered as source 56 in `research/prime_lattice/SOURCES.md`:

- **Masatoshi Suzuki**, *Weil's quadratic form via the screw function*, arXiv:`2606.09096v2` (2026). The fixed-interval scaling in Section 4 writes the `a`-dependent bounded part using translation operators with displacement `log n/a` plus continuous-kernel terms. The proof of continuity of the ground eigenvalue uses a uniform logarithmic-form bound, compactness into `L^2`, and joint continuity of those bounded terms; it does not claim operator-norm continuity of the translation family or provide a quantitative radius transporting a tiny spectral gap.

The two functional-analytic ingredients used here are classical rather than novelty claims. Translation groups on `L^2` are the standard example of strongly continuous unitary groups that are not uniformly continuous when their generator is unbounded; the interior wave-packet argument above proves the exact compressed-interval norm jump needed here without appealing to an external theorem. The logarithmic Fourier-tail estimate is a direct one-line frequency split in the logarithmic Sobolev scale. Classical logarithmic Sobolev/Bessel-potential literature contains much broader function-space theory; no originality is claimed for this modulus.

A targeted literature audit around Suzuki's 2026 fixed-domain formula, translation-semigroup continuity, logarithmic Sobolev regularity, and localized Weil spectral perturbation found Suzuki's qualitative continuity theorem but no published quantitative aperture radius transferring the recent `a=0.8` computer-assisted lower bound. Search absence is not treated as evidence of novelty. The durable contribution is the exact route diagnosis in the current Prime-Lattice frontier: the `L^2` bounded-operator topology is maximally wrong for the moving source channels, while the canonical `H^log` topology restores continuity only with a generic logarithmic modulus.

## 7. Adversarial checks and boundaries

- **No claim that the full finite sum has norm jump two.** The proof is channelwise. Several moving translations could in principle cancel in a specially structured linear combination. Any theorem about the norm discontinuity of the full arithmetic sum would require an additional separation or phase argument and is not asserted.
- **Compression does not regularize the shift.** The norm-jump witnesses are high-frequency packets supported strictly inside the common overlap, so endpoint truncation is inactive on them.
- **Source thresholds are not the cause.** The argument applies on an interval with a fixed active source set. At `0.8<a<log5/2`, no new von-Mangoldt atom is needed.
- **The `H^log` modulus is sufficient, not claimed sharp.** Optimizing the frequency split can change secondary logarithmic factors and constants but not the basic fact that the ambient logarithmic regularity is far weaker than a positive Sobolev order.
- **The tiny-radius diagnosis is not a certificate.** It does not prove positivity at any explicit `a>0.8`; doing so requires fully tracked constants in Suzuki's complete fixed-domain form and an explicit energy bound for all competing low states.
- **No RH inference.** Even a useful finite neighborhood beyond `0.8` would remain a finite-window theorem. RH needs positivity for every aperture.
- **The `1/2` critical line is not generated here.** The `H^log` modulus is generic Fourier regularity. The arithmetic normalization and RH content are already in the completed Weil form.
- **Matched controls survive.** Any finite family of compressed translations with the same form-domain regularity exhibits the same topology split. Rational-prime specificity can enter only through the coefficients, simultaneous channel relations, or stronger source-specific information.

## Consequence for the line

The immediate post-`PL-284` frontier is now sharper. The interval before the next source event cannot be treated as an ordinary norm-small perturbation merely because the active prime powers remain `2,3,4`. The ambient `L^2` topology sees an order-two jump as each lag moves. The canonical logarithmic form topology restores continuity, but generically only at a logarithmic rate.

A useful next theorem must therefore exploit information stronger than bare continuity of the form domain. Viable targets include a uniform positive-Sobolev or analyticity estimate for the isolated ground branch, a source-specific differential/Schur-complement inequality whose constants remain controlled between prime activations, or a direct variational estimate for the full completed form that couples the three active channels with the archimedean term. Any such theorem would turn the spectral isolation at `a=0.8` into genuine quantitative aperture control; the generic translation topology by itself does not.