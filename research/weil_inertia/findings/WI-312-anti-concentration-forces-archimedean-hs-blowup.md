# WI-312 — Anti-concentration forces archimedean Hilbert--Schmidt blow-up under capped-tail flattening

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-307, WI-308, WI-310, WI-311.

WI-311 shows that smooth frequency multiplexing can make the capped retained tail arbitrarily close to its maximal scalar floor `1/2 I` while preserving the exact source decomposition. Its remaining caveat was qualitative: the carrier scale diverges, the aggregate autocorrelation oscillates faster, and no uniform control of the finite compact sector was obtained.

There is an exact quantitative obstruction behind that caveat. Let `g_1,...,g_J` be a finite family of real smooth unit-window localizers with

\[
\sum_{\nu=1}^J\|g_\nu\|_2^2=1,
\]

and define the normalized frequency-energy probability measure

\[
\mu(ds)
:=\frac1{2\pi}
\sum_{\nu=1}^J|\widehat g_\nu(s)|^2\,ds.
\]

Its aggregate autocorrelation is

\[
R(a)=\sum_\nu\rho_{g_\nu}(a)
=\int_{\mathbb R}\cos(as)\,\mu(ds).
\tag{1}
\]

For `h>0`, write the concentration function

\[
\mathcal Q_\mu(h)
:=\sup_{x\in\mathbb R}\mu([x-h,x+h]).
\tag{2}
\]

Fix an outer aperture `L>0`, and let

\[
\kappa(a)
=
\frac{2e^{-a/2}}{1-e^{-2a}}
-4\cosh(a/2)
\tag{3}
\]

be the archimedean coefficient in the exact localization defect of WI-307. Since

\[
\lim_{a\downarrow0}a\kappa(a)=1,
\tag{4}
\]

choose any fixed `delta in (0,2L)` small enough that

\[
\kappa(a)\ge\frac1{2a}
\qquad(0<a\le\delta).
\tag{5}
\]

Let `C_R` denote only the continuous archimedean part of the localization-defect operator,

\[
C_R
=
\int_0^{2L}(1-R(a))\kappa(a)J_a\,da,
\tag{6}
\]

with the compressed shifts `J_a` from WI-307. If

\[
\mathcal Q_\mu(h)\le\eta,
\qquad 0<\eta\le\frac18,
\tag{7}
\]

then

\[
\boxed{
\|C_R\|_{\mathrm{HS}}^2
\ge
\frac{2L-\delta}{2}
\left(
\frac{\pi h}{128\eta}-\frac1\delta
\right).
}
\tag{8}
\]

In particular, for fixed `L,h,delta`, any smooth multiwindow family whose frequency concentration tends to zero has

\[
\|C_R\|_{\mathrm{HS}}\longrightarrow\infty.
\tag{9}
\]

Applied to the WI-311 construction, where `h=T_{B_L}` is fixed after the reserve is chosen and

\[
\mathcal Q_{\mu_N}(T_{B_L})
<\frac1{2N}+\epsilon,
\tag{10}
\]

this proves that driving the capped tail to `1/2 I` by `N -> infinity` and `epsilon -> 0` necessarily makes the continuous archimedean compact correction diverge in Hilbert--Schmidt norm. The tradeoff is therefore structural, not an artifact of estimating derivatives of the explicit cosine--sine windows.

This is a no-go result only for **componentwise Hilbert--Schmidt complexity control**. It does not prove divergence of the operator norm, negative index, or the full source correction after combining the continuous and discrete pieces. Exact cancellation or a different invariant can still control the finite negative sector. What (8) closes is the route that tries simultaneously to flatten the capped tail to its maximal scalar floor and keep each compact localization component uniformly bounded in `S_2` before recombination. The same obstruction automatically applies to any `S_p` budget with `p<=2` whenever that norm is finite, since `||A||_{S_p}>=||A||_{S_2}`.

## 1. The frequency law turns the autocorrelation into a characteristic function

Because every `g_nu` is real, `|gHat_nu(s)|^2` is even. Plancherel and the normalization give `mu(R)=1`, and Wiener--Khinchin gives (1). The smooth compact support of the windows makes the density rapidly decaying, so all first moments used below are finite.

Let `X,Y` be independent with law `mu`. Define

\[
I_\mu
:=
\int_0^\infty
\frac{(1-R(a))^2}{a^2}\,da.
\tag{11}
\]

Since `mu` is symmetric, `R(a)^2` is the characteristic function of `X-Y`. Expanding

\[
(1-R)^2=2(1-R)-(1-R^2)
\]

and using the classical identity

\[
\int_0^\infty\frac{1-\cos(at)}{a^2}\,da
=\frac\pi2|t|
\tag{12}
\]

gives the exact formula

\[
\boxed{
I_\mu
=
\pi\,\mathbb E|X|
-\frac\pi2\,\mathbb E|X-Y|
=
\frac\pi2\,\mathsf{ED}_0^2(\mu),
}
\tag{13}
\]

where

\[
\mathsf{ED}_0^2(\mu)
:=2\mathbb E|X|-\mathbb E|X-Y|
\tag{14}
\]

is the squared one-dimensional energy distance from `mu` to the point mass at zero. Equation (13) is a specialization of the classical characteristic-function representation of energy distance; the use made of it below is specific to the Weil localization defect.

For a symmetric continuous law, if

\[
q(x):=\mu((x,\infty)),\qquad x\ge0,
\]

then the standard one-dimensional tail representation gives

\[
\boxed{
\mathsf{ED}_0^2(\mu)
=4\int_0^\infty q(x)^2\,dx.
}
\tag{15}
\]

This identity can also be checked directly from

\[
\mathbb E|X|=2\int_0^\infty q(x)dx
\]

and

\[
\mathbb E|X-Y|
=4\int_0^\infty q(x)(1-q(x))dx.
\]

## 2. Small interval concentration forces large energy distance

Assume (7). Partition the positive half-line into intervals

\[
[2kh,2(k+1)h],
\qquad k=0,1,2,\ldots.
\]

Each has `mu`-mass at most `eta`. Put

\[
K=\left\lfloor\frac1{4\eta}\right\rfloor.
\]

For `eta<=1/8`,

\[
K\ge\frac1{8\eta}.
\tag{16}
\]

For every `0<=x<=2Kh`, at most `K eta<=1/4` of the positive half-mass can lie in `(0,x]`. Symmetry and absolute continuity therefore imply

\[
q(x)\ge\frac14
\qquad(0\le x\le2Kh).
\tag{17}
\]

Substituting (17) into (15) yields

\[
\mathsf{ED}_0^2(\mu)
\ge
4(2Kh)\left(\frac14\right)^2
=
\frac{Kh}{2}
\ge
\frac{h}{16\eta}.
\tag{18}
\]

Hence (13) gives the quantitative anti-concentration estimate

\[
\boxed{
I_\mu
\ge\frac{\pi h}{32\eta}.
}
\tag{19}
\]

The constant is deliberately coarse. The important feature is the unavoidable `1/eta` growth. No detailed information about the separated-carrier construction is used.

## 3. The `1/a` archimedean singularity converts energy distance into Hilbert--Schmidt complexity

Since `|R(a)|<=1`,

\[
\int_\delta^\infty
\frac{(1-R(a))^2}{a^2}\,da
\le
\frac4\delta.
\tag{20}
\]

Combining (19) and (20),

\[
\int_0^\delta
\frac{(1-R(a))^2}{a^2}\,da
\ge
\frac{\pi h}{32\eta}-\frac4\delta.
\tag{21}
\]

Write

\[
b_R(a):=(1-R(a))\kappa(a).
\]

By (5),

\[
\int_0^\delta|b_R(a)|^2da
\ge
\frac14
\int_0^\delta
\frac{(1-R(a))^2}{a^2}da
\ge
\frac{\pi h}{128\eta}-\frac1\delta.
\tag{22}
\]

The operator (6) has difference kernel

\[
K_R(s,t)=\frac12b_R(|s-t|)
\qquad(s,t\in(-L,L)).
\tag{23}
\]

Therefore its Hilbert--Schmidt norm is exactly

\[
\|C_R\|_{\mathrm{HS}}^2
=
\frac12\int_0^{2L}(2L-a)|b_R(a)|^2da.
\tag{24}
\]

Restricting (24) to `(0,delta)` and using (22) proves (8).

This also identifies the mechanism precisely. Near zero the explicit-formula coefficient behaves as `1/a`. A localizer has to satisfy `R(a) -> 1` quickly enough to cancel that singularity. Frequency anti-concentration makes the weighted `L^2` cost of that cancellation grow, and the Hilbert--Schmidt norm records that cost exactly.

## 4. A near-maximal capped floor itself forces frequency anti-concentration

The implication is not limited to the explicit WI-311 frequency comb. Let `qHat` be any bounded retained source profile with

\[
0\le\widehat q(t)\le\frac12
\]

and suppose that for some `h>0`

\[
\widehat q(t)=0
\qquad(|t|\le h).
\tag{25}
\]

Let

\[
\widehat r(\xi)
=
\int\widehat q(t)\,\mu(d(t-\xi)).
\tag{26}
\]

If

\[
\widehat r(\xi)
\ge
\frac12(1-\eta)
\qquad\text{for every }\xi,
\tag{27}
\]

then

\[
\frac\eta2
\ge
\frac12-\widehat r(\xi)
=
\int\left(\frac12-\widehat q(t)\right)\mu(d(t-\xi))
\ge
\frac12\mu([\xi-h,\xi+h]).
\tag{28}
\]

Thus

\[
\boxed{
\mathcal Q_\mu(h)\le\eta.
}
\tag{29}
\]

Equations (8) and (29) show a general incompatibility: whenever a capped source profile has a genuine zero core, pushing its retained convolution uniformly to the maximal `1/2` floor forces the continuous archimedean localization defect to become unbounded in Hilbert--Schmidt complexity.

WI-311 already supplies the stronger explicit anti-concentration (10) at the saturated exterior scale `T_{B_L}`, so its application does not depend on identifying the largest zero core of the particular clipped source profile.

## 5. What this closes, and what it does not

WI-311 left open whether smooth multiplexing might simultaneously produce an almost-scalar retained tail and a uniformly manageable compact correction. Equation (8) gives a decisive negative answer for one natural meaning of manageable: **uniform Hilbert--Schmidt control of the continuous archimedean correction is impossible.** The deterioration is forced by frequency anti-concentration itself and survives every choice of smooth real windows.

This matters for the finite-negative-sector program because Hilbert--Schmidt and related componentwise Schatten bounds are the most direct way to turn compactness into quantitative eigenvalue-count or eigenvalue-depth control. That route cannot stay uniform in the same limit that saturates the capped tail.

The result deliberately stops short of a stronger claim. It does not imply

\[
\|C_R\|\to\infty,
\qquad
n_-(C_R)\to\infty,
\]

and it does not exclude cancellation when the continuous defect is recombined with the finite prime-translation part, the averaged compact source part, or another source-exact correction. A successful continuation must therefore exploit correlated cancellation in the exact source decomposition, use an invariant not dominated by componentwise `S_2` size, or avoid the near-maximal tail-flattening limit.

This sharpens the WI-311 frontier: endpoint singularity and large carrier scale are not merely two awkward constructions. At least for smooth frequency multiplexing, approaching the maximal scalar tail floor necessarily transfers complexity into the archimedean compact sector.

## 6. Prior-art and novelty audit

The characteristic-function representation of energy distance is classical. Relevant anchors are:

- G. J. Szekely and M. L. Rizzo, **Energy statistics: A class of statistics based on distances**, *Journal of Statistical Planning and Inference* 143 (2013), 1249--1272, DOI `10.1016/j.jspi.2013.03.018`.
- M. L. Rizzo and G. J. Szekely, **Energy distance**, *WIREs Computational Statistics* 8 (2016), 27--38, DOI `10.1002/wics.1375`.

Wiener--Khinchin/Plancherel and Hilbert--Schmidt difference-kernel calculations are also standard harmonic-analysis facts. The recent WI-307--WI-311 chain already records the source-exact Weil localization and the smooth frequency-comb construction.

A targeted audit found general energy-distance, concentration-function/characteristic-function, and time-frequency localization literature, but no prior source in the line corpus or the targeted external search that combines (i) capped-tail frequency anti-concentration, (ii) the exact energy-distance identity, and (iii) the `kappa(a)~1/a` Weil archimedean singularity to force the explicit Hilbert--Schmidt lower bound (8). That application-specific implication is therefore recorded as `EXACT-DERIVED`, without any claim of historical priority.

## Research consequence

The next finite-negative-sector step should not try to make the WI-311 tail flatter while separately estimating the continuous compact correction in Hilbert--Schmidt norm. That tradeoff is now quantitatively closed. The surviving routes are source-correlated: prove cancellation between the archimedean and arithmetic/source pieces, find a finite-negative-sector invariant insensitive to the growing `S_2` mass, or work away from the saturated `1/2 I` tail limit where a weaker tail floor may permit a uniform complexity budget.
