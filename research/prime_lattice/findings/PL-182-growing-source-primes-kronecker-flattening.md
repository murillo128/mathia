# PL-182 — Growing source primes do not escape Kronecker flattening below the short-interval-PNT resolution scale

## Claim

`PL-181` proves short-interval-PNT flattening for the canonical vertical/Kronecker affine readout when the frozen source prime `r` is fixed, and explicitly leaves a growing source `r=r(X)` open. That escape disappears after using the exact phase derivative instead of Taylor-expanding in `(r-1)/X`.

Let `h_X>=1` be arbitrary; in particular one may take `h_X=r_X-1` for an arbitrarily growing source prime `r_X`. Define

\[
B_{X,h}(t)
:=
\frac1{\pi(X)}
\sum_{q\le X\atop q\ \mathrm{prime}}
\exp\!\left(it\log\left(1+\frac hq\right)\right),
\qquad
\kappa_X:=\frac{h_X}{X},
\]

and the exact phase-resolution parameter

\[
\nu_X
:=
|t_X|\frac{h_X}{X+h_X}
=
|t_X|\frac{\kappa_X}{1+\kappa_X}.
\]

For every fixed `eta` with `0<eta<13/15`, uniformly for arbitrary `h_X>=1` and real `t_X` satisfying

\[
\nu_X\le X^{13/15-\eta},
\]

one has

\[
\boxed{
B_{X,h_X}(t_X)
=
I_{\kappa_X,t_X}+o(1),
}
\]

where

\[
I_{\kappa,t}
:=
\int_0^1
\exp\!\left(it\log\left(1+\frac\kappa u\right)\right)\,du.
\]

Moreover, for `nu=|t|kappa/(1+kappa)>0`,

\[
\boxed{|I_{\kappa,t}|\le \frac{2}{\nu}.}
\]

Consequently, if

\[
\nu_X\longrightarrow\infty,
\qquad
\nu_X\le X^{13/15-\eta},
\]

then

\[
\boxed{B_{X,h_X}(t_X)\longrightarrow0}
\]

uniformly across the growth rate of `h_X`. Thus merely letting the frozen source prime grow does not produce a surviving non-Haar Kronecker readout anywhere inside the same short-interval-PNT resolution band as `PL-181`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. The only deep input is the same Guth--Maynard almost-all short-interval PNT already audited in `PL-181`. The extension to arbitrary `h_X` is an exact derivative estimate plus elementary oscillatory integration. No literature novelty is claimed.

## 1. Exact affine phase and the correct scale for a growing source

For the vertical character

\[
f_t(m)=m^{it}
=\exp\!\bigl(it\langle v(m),(\log p)_p\rangle\bigr),
\]

`PL-179`--`PL-181` reduce the oriented one-source affine plaquette, after removing the known source phase, to

\[
\left(1+\frac hq\right)^{it},
\qquad h=r-1.
\]

When `h` is fixed, `PL-181` uses the scale `|t|h/X`. For arbitrary `h`, keep the phase exact:

\[
\phi_{h,t}(x)
:=
t\log\left(1+\frac hx\right),
\qquad
\phi'_{h,t}(x)
=-\frac{th}{x(x+h)}.
\]

On the bulk interval `x in [delta X,X]`, with fixed `delta in (0,1)`, define

\[
\nu=|t|\frac{h}{X+h}.
\]

Then

\[
|\phi'_{h,t}(x)|
=
|t|\frac{h}{x(x+h)}
\le
C_\delta\frac{\nu}{X},
\]

because

\[
\frac{|t|h/[x(x+h)]}{\nu/X}
=
\frac{X(X+h)}{x(x+h)}
\le C_\delta
\]

uniformly for every `h>=1`. This removes the fixed-source assumption from the local phase-variation step. The natural parameter is therefore `nu`, not `|t|h/X` once `h` can be comparable with or larger than `X`.

The regimes match intuition:

\[
h\ll X:\quad \nu\sim |t|h/X,
\qquad
h\asymp X:\quad \nu\asymp |t|,
\qquad
h\gg X:\quad \nu\sim |t|.
\]

## 2. The same good-offset short-interval argument is uniform in `h`

Use the exact Guth--Maynard input quoted and audited in `PL-181`: for every fixed positive epsilon, the expected prime count holds for all but

\[
O\!\left(Xe^{-c(\log X)^{1/4}}\right)
\]

starts of intervals of length at least `X^(2/15+epsilon)` in the relevant dyadic range. As in `PL-181`, a freely chosen residue offset partitions the already-fixed global prime sum so that only a vanishing total mass lies in exceptional cells.

Fix `eta in (0,13/15)` and choose

\[
H=X^{2/15+\eta/3}
\]

up to the harmless dyadic rescaling used in `PL-181`. If

\[
\nu\le X^{13/15-\eta},
\]

then on every good bulk cell of length `H`,

\[
\sup_{u,v\in I}
|\phi_{h,t}(u)-\phi_{h,t}(v)|
\ll_\delta
\frac{\nu H}{X}
\ll_\delta
X^{-2\eta/3}
=o(1),
\]

uniformly in `h`. Therefore the prime sum on a good cell is its local prime count times the phase at one representative point, up to an error whose globally normalized sum is `o(1)`. Exceptional cells and incomplete edge cells are controlled exactly as in `PL-181`; the estimate does not involve `h` because the weight always has modulus one.

After summing the dyadic blocks and using `pi(delta X)/pi(X)->delta`, this gives, uniformly in the displayed `nu` range,

\[
B_{X,h}(t)
=
\int_0^1
\exp\!\left(it\log\left(1+\frac{h/X}{u}\right)\right)du
+o(1).
\]

No Taylor expansion in `h/X` occurs. Hence the argument remains valid when `h/X` tends to zero, a positive constant, infinity, or oscillates.

## 3. The continuum response decays uniformly once the exact phase scale diverges

Set `kappa=h/X>0` and

\[
\psi(u)=t\log\left(1+\frac\kappa u\right).
\]

Then

\[
\psi'(u)
=-t\frac{\kappa}{u(u+\kappa)}.
\]

For `0<u<=1`,

\[
|\psi'(u)|
\ge
|t|\frac{\kappa}{1+\kappa}
=\nu.
\]

More explicitly,

\[
\frac1{\psi'(u)}
=-\frac{u(u+\kappa)}{t\kappa}.
\]

This tends to zero as `u->0`, while its magnitude at `u=1` is exactly `1/nu`; along `(0,1]` it is monotone in magnitude. Integrating by parts in

\[
I_{\kappa,t}=\int_0^1e^{i\psi(u)}du
\]

therefore yields

\[
|I_{\kappa,t}|
\le
\left|\frac1{\psi'(1)}\right|
+
\int_0^1
\left|\frac{d}{du}\frac1{\psi'(u)}\right|du
\le
\frac2\nu.
\]

This estimate is uniform in `kappa`. Combining it with the prime-to-continuum quadrature proves cancellation whenever `nu_X->infinity` below the `X^(13/15-eta)` resolution horizon.

## 4. What this closes and what it does not

The result closes the explicit growing-source loophole left in `PL-181` for the **same broad one-prime average and the same canonical vertical character**. The source can grow faster than the moving-prime cutoff: if `h_X>>X`, the exact resolution parameter simply saturates at `nu_X~|t_X|`, and the continuum response remains nonstationary and decays like `O(1/|t_X|)`.

Conversely, bounded `nu_X` need not give zero. It gives a deterministic continuum profile `I_{kappa_X,t_X}` controlled by one-point prime density. This is a negative information statement, not evidence of an RH mechanism: inside the theorem-controlled band, neither increasing `r_X` nor increasing `t_X` while keeping the exact local phase resolvable forces the readout to see prime-pair structure, the zeta zero divisor, analytic continuation, or the critical line.

The result does **not** control:

- frequencies with `nu_X` at or beyond the current `X^(13/15-o(1))` short-interval resolution horizon;
- thin or jointly constrained source/moving-prime families for which one-point local prime density is insufficient;
- non-product prime phases or target/completion weights inserted before the affine cancellation;
- shifted-prime Liouville or other parity correlations from `PL-178`, which are a different observable.

The exponent `13/15` remains a theorem-technology horizon inherited from the current almost-all short-interval PNT, not a prime-lattice spectral constant.

## Prior art and novelty audit

The theorem-level input is established prior art:

- **Larry Guth, James Maynard**, “New large value estimates for Dirichlet polynomials,” *Annals of Mathematics* **203**(2) (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`. Corollary 1.4 supplies the almost-all prime number theorem at interval length `X^(2/15+epsilon)` used here; `PL-181` records the exact theorem-to-quadrature audit and the good-offset conversion.

Targeted searches for the exact phases `log((p+h)/p)`, `log(1+h/p)`, and `exp(it log(1+h/p))` did not locate a paper treating this growing-shift average as a separate invariant. This absence is not used as a novelty claim. The displayed extension is an elementary consequence of the cited short-interval theorem once the exact derivative is normalized by `h/(X+h)`.

A matched control is immediate: any point set with the same almost-all local counting law at scale `X^(2/15+epsilon)` obeys the same slowly-varying-weight quadrature. The residual continuum kernel is therefore not intrinsically zeta-zero-sensitive.

## Consequence for the clue

`CLUE-affine-log-spectrum-nonhaar-escape` should no longer list a growing frozen source as a live escape for the canonical Kronecker phase merely because `r_X/X` is unbounded. For this branch the correct decisive parameter is

\[
\nu_X
=
|t_X|\frac{r_X-1}{X+r_X-1}.
\]

Whenever `nu_X<=X^(13/15-eta)`, the broad prime average is forced to the continuum profile above, and whenever additionally `nu_X->infinity` it tends to zero. The remaining live phase edge is beyond this phase-resolution horizon or in a genuinely different source/target coupling that invalidates the one-point prime-density quadrature.