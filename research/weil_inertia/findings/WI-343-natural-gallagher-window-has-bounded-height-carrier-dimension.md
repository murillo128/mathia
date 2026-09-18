# WI-343 — natural Gallagher window has bounded height-carrier dimension

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + NON-RH`.

## Claim

The exact multiplicative Gallagher window from WI-195 has an intrinsic unit time--bandwidth product at the bow scale. This makes the many zero ordinates inside one Maynard--Pratt bow highly redundant as **linear carrier tests on one fixed source window**, independently of any arithmetic theorem about `Lambda-Lambda^sharp`.

Let `H>0`, let

\[
I_y(H):=\{n\in\mathbf N:e^y<n\le e^{y+1/H}\},
\]

and give this finite set arbitrary nonnegative weights `w_n`, not all zero. For a height `U` write

\[
c_U(n):=n^{iU},
\qquad
\widehat c_U:=\frac{c_U}{\|c_U\|_w},
\qquad
\|f\|_w^2:=\sum_{n\in I_y(H)}w_n|f(n)|^2.
\]

If `U,V` lie in any interval of length at most `H`, then

\[
\boxed{
|\langle \widehat c_U,\widehat c_V\rangle_w|
\ge \cos\frac12
=0.87758256\ldots .
}
\tag{1}
\]

More strongly, if `\mathcal U` is any such height interval and `U_0=\inf\mathcal U`, then for every integer `d\ge0` the entire normalized carrier family lies within relative Hilbert distance

\[
\boxed{
\frac1{(d+1)!}
}
\tag{2}
\]

of a fixed `(d+1)`-dimensional subspace. In particular, with `d=6`, every carrier is within

\[
\frac1{5040}<2\times10^{-4}
\]

of one fixed seven-dimensional subspace. If `G` is the Gram matrix of any `m` normalized bow-height carriers from the same height interval and its eigenvalues are ordered decreasingly, then

\[
\boxed{
\sum_{j>7}\lambda_j(G)
\le \frac{m}{5040^2}
<3.94\times10^{-8}m.
}
\tag{3}
\]

Thus the count `m=T^vartheta` of bow ordinates does not produce `m` independent linear twists on a natural Gallagher window. The obstruction is geometric and precedes the arithmetic exceptional-set issue in WI-327 and WI-329: at exact bow resolution, the whole height portfolio has bounded approximate dimension independent of `m` and `T`.

This closes the route in which one tries to de-exceptionalize a fixed source window merely by sampling more zero ordinates from the same bow and treating those twists as independent linear probes. It does **not** close source-specific nonlinear observables, cross-window/source-start coupling, a wider logarithmic source aperture, or a theorem that uses the arithmetic coefficients jointly with the height parameter rather than only through the carrier vectors.

## 1. Exact pairwise coherence on a Gallagher window

For `n\in I_y(H)` put

\[
x_n:=\log n-y.
\]

Then exactly

\[
0<x_n\le\frac1H.
\tag{4}
\]

Multiplication by the scalar phase `e^{iUy}` does not affect normalized inner products, so the carrier can be replaced by

\[
\widetilde c_U(n):=e^{iUx_n}.
\tag{5}
\]

Take two heights `U,V` with `|U-V|\le H` and set `Delta=U-V`. Since every phase `Delta x_n` lies in an interval of length at most

\[
\frac{|\Delta|}{H}\le1,
\tag{6}
\]

rotate the weighted average by the midpoint phase `e^{-i\Delta/(2H)}`. Every rotated summand then has argument in `[-1/2,1/2]`, hence real part at least `cos(1/2)`. With `W=\sum_n w_n`,

\[
\begin{aligned}
|\langle \widehat c_U,\widehat c_V\rangle_w|
&=
\frac1W\left|\sum_n w_ne^{i\Delta x_n}\right|\\
&\ge
\frac1W\Re\left(
e^{-i\Delta/(2H)}
\sum_n w_ne^{i\Delta x_n}
\right)\\
&\ge \cos\frac12.
\end{aligned}
\tag{7}
\]

This proves (1) for **every** choice of positive source weights. No prime distribution, zero-spacing theorem, or asymptotic approximation is involved.

There is also a useful aggregate formulation. For `m` normalized carriers, `G_{jk}=\langle\widehat c_{U_j},\widehat c_{U_k}\rangle_w`, so

\[
\operatorname{tr}G=m
\]

and (1) gives

\[
\operatorname{tr}(G^2)
=\sum_{j,k}|G_{jk}|^2
\ge
m+m(m-1)\cos^2\frac12.
\tag{8}
\]

Thus the participation-ratio effective rank

\[
r_{\rm eff}(G):=
\frac{(\operatorname{tr}G)^2}{\operatorname{tr}(G^2)}
\]

satisfies

\[
\boxed{
r_{\rm eff}(G)
\le
\frac{m}{1+(m-1)\cos^2(1/2)}
\longrightarrow
\sec^2\frac12
=1.2984464\ldots .
}
\tag{9}
\]

This does not say that the exact algebraic rank is bounded; (2)--(3) give the stronger approximation statement needed for that distinction.

## 2. Factorial bounded-dimensional approximation

Fix the left endpoint `U_0` of the height interval and write

\[
\delta:=U-U_0,
\qquad 0\le\delta\le H.
\]

After factoring out the fixed carrier `e^{iU_0x_n}`, the variable part is `e^{i\delta x_n}`. Taylor's formula with integral remainder on the real axis gives, for every `d\ge0`,

\[
e^{i\delta x}
=
\sum_{r=0}^{d}
\frac{(i\delta x)^r}{r!}
+R_{d+1}(\delta x),
\qquad
|R_{d+1}(z)|\le\frac{|z|^{d+1}}{(d+1)!}.
\tag{10}
\]

By (4), `|\delta x_n|\le1`. Therefore, pointwise on the entire Gallagher window,

\[
\left|
e^{i\delta x_n}
-
\sum_{r=0}^{d}\frac{(i\delta)^r x_n^r}{r!}
\right|
\le\frac1{(d+1)!}.
\tag{11}
\]

Let

\[
V_d:=
\operatorname{span}
\left\{
(e^{iU_0x_n}x_n^r)_{n\in I_y(H)}:
0\le r\le d
\right\}.
\tag{12}
\]

Its dimension is at most `d+1`. Equation (11), summed against arbitrary nonnegative weights, gives

\[
\operatorname{dist}_w(c_U,V_d)
\le
\frac{\|c_U\|_w}{(d+1)!}.
\tag{13}
\]

After normalization this is exactly (2).

Now take `m` normalized carriers and let `P_d` be orthogonal projection onto `V_d`. Equation (13) yields

\[
\sum_{k=1}^{m}
\|(I-P_d)\widehat c_{U_k}\|_w^2
\le
\frac{m}{((d+1)!)^2}.
\tag{14}
\]

The nonzero eigenvalues of their Gram matrix equal those of the corresponding covariance operator. By the variational characterization of the best rank-`d+1` approximation (or directly by the min--max principle), (14) implies

\[
\boxed{
\sum_{j>d+1}\lambda_j(G)
\le
\frac{m}{((d+1)!)^2}.
}
\tag{15}
\]

Setting `d=6` proves (3). The factorial tail is useful because the effective dimension remains bounded even if the bow itself contains a power-growing number of zeros.

## 3. Application to the WI-195 bow/Gallagher geometry

WI-195 fixes precisely the multiplicative short-window identity

\[
\int_{\mathbf R}
\left|
\sum_{e^y<n\le e^{y+\delta}}b_n
\right|^2dy
=
\sum_{m,n}
b_n\overline{b_m}
(\delta-|\log(n/m)|)_+,
\tag{16}
\]

and at bow height scale chooses

\[
\delta=\frac1{H_{\rm bow}}.
\tag{17}
\]

The selected bow ordinates themselves occupy a vertical interval of length `H_bow`. Hence every individual source window in the exact identity satisfies the hypotheses of Sections 1--2 with

\[
H=H_{\rm bow},
\qquad
H\delta=1.
\tag{18}
\]

The consequence is independent of the surviving exponent `vartheta`, of the number `m=T^vartheta` of selected bow zeros, and of whether those ordinates are critical or off critical. On each fixed source window, the exact carrier portfolio has pairwise normalized coherence at least `cos(1/2)` and admits the rank-seven approximation (3).

This sharpens the interpretation of WI-328--WI-330. WI-328 shows that on the shorter cubic block the bow is asymptotically twist-frozen. WI-329 then moves to the natural source length, where order-one dephasing first becomes possible, and shows that the published almost-all nilsequence theorem already has one common phase-uniform exceptional set. The present finding shows that the order-one dephasing should **not** be confused with a power-growing supply of independent phase directions: the natural window has only unit time--bandwidth product.

In particular, even if one replaced the phase-uniform theorem used in WI-329 by separate estimates at each bow ordinate, a proof could not legitimately amplify their strength by pretending that the `m` carriers are orthogonal or statistically independent linear tests. Any such amplification would need additional arithmetic decorrelation not contained in the carrier geometry.

## 4. What this closes and what remains live

The exact no-go is narrow. It rules out the implication

\[
\text{many bow ordinates}
+\text{one natural Gallagher window}
\Longrightarrow
\text{many independent linear carrier probes}.
\tag{19}
\]

That implication fails before one asks anything about primes: equations (1)--(3) hold for arbitrary positive Hilbert weights and for every placement of the heights inside a span `H`.

Several routes remain outside the obstruction:

- integrating over many **different source starts/windows** in (16), where the arithmetic coefficient vector itself changes;
- using a wider logarithmic source aperture, so that the product `H\delta` grows rather than staying equal to one;
- exploiting cross-window covariance or a source-specific nonlinear statistic rather than a portfolio of the linear carriers `n^{iU}`;
- using off-critical information, the zero equation, or other zeta-specific data that couples the selected ordinate to the coefficients;
- proving the signed off-diagonal cancellation requested by the accepted distinguished-twist clue directly.

Accordingly this finding does not prove the WI-195 `L^2` target, does not control the exceptional starts left by WI-327/WI-329, does not improve the certified simple-critical-zero proportion, and does not prove RH. It is a route-closing geometric constraint on how height multiplicity can be used.

## 5. Prior art and novelty boundary

The general phenomenon is classical time--bandwidth concentration, not new harmonic analysis. Slepian--Pollak and Landau--Pollak developed the prolate-spheroidal theory showing that the effective number of independent signals localized simultaneously in time and frequency is governed by the time--bandwidth product:

- D. Slepian and H. O. Pollak, **Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — I**, *Bell System Technical Journal* 40 (1961), 43--63, DOI `10.1002/j.1538-7305.1961.tb03976.x`.
- H. J. Landau and H. O. Pollak, **Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — III: The Dimension of the Space of Essentially Time- and Band-Limited Signals**, *Bell System Technical Journal* 41 (1962), 1295--1336, DOI `10.1002/j.1538-7305.1962.tb03279.x`.

The second paper explicitly formulates the classical engineering principle that the number of essentially independent signals is controlled by the `WT` product. Those results provide the correct prior-art interpretation of (18), but they are not needed to prove (1)--(3): the coherence and factorial approximation here follow directly from the exact Gallagher aperture and elementary Taylor remainder.

A bounded line-local audit found no earlier `weil_inertia` finding expressing the natural bow/Gallagher window as a unit time--bandwidth carrier family, no stored `Slepian`/`prolate` anchor, and no previous quantitative bound corresponding to (1)--(3). WI-187 concerns the different Montgomery--Vaughan arithmetic resolution ratio `x/H_bow`; WI-328 concerns asymptotic twist-freezing on a shorter cubic block; WI-329 concerns the common exceptional set of a phase-uniform arithmetic theorem. This finding should therefore be read as an exact synthesis/application of a classical mechanism, with no external priority claim.

## Research consequence

Do not try to beat the distinguished-start obstruction by counting bow ordinates as independent linear samples on the same natural Gallagher source window. The exact localizer fixes `H_bow delta=1`, so those carriers remain strongly coherent and uniformly bounded-dimensional regardless of how many zeros the bow contains. Height diversity can become genuinely informative only after importing structure absent from this one-window carrier family: different source windows, larger time--bandwidth product, nonlinear/source-dependent couplings, or direct signed covariance information.