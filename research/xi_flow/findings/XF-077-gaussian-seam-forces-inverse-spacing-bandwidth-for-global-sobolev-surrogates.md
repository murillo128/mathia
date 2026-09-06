# XF-077 — Gaussian seam forces inverse-spacing bandwidth for global Sobolev surrogates

**Status:** `EXACT-DERIVED` + `MATCHED-ZERO-FREE-CONTROL` + `QUANTITATIVE-SEAM-BANDWIDTH` + `GLOBAL-SURROGATE-NO-GO`. XF-074 shows that the Gaussian-reference quotient is generically meromorphic on a full period, XF-075 rules out a source-independent exact seam repair, and XF-076 proves that an exact entire finite-band solution of the quotient equation must be spatially constant. The remaining finite-surrogate escape hatch is approximate: perhaps an `N`-mode entire trigonometric carrier could approximate the quotient closely enough that its transport residual and auxiliary-divisor cost are negligible.

For full-period Sobolev approximation at the existing Vieta bandwidth, that escape hatch already fails on the same zero-free Fourier-mode control used in XF-074. At a frozen time put

\[
d:=\frac{\pi v}{L},
\qquad
a:=\frac{2\pi^2v}{L^2}.
\tag{1}
\]

For the exact zero-free backward-heat mode chosen in XF-074,

\[
u_{\omega_0}(z,s)=e^{\omega_0^2s+i\omega_0z},
\qquad
\omega_0=\frac{\pi h}{L},
\tag{2}
\]

the Gaussian/Appell quotient is, up to a nonzero scalar,

\[
R(z)=\frac{W_L(z-id)}{W_L(z)}.
\tag{3}
\]

Its full periodic Fourier coefficients can be computed exactly. There is a nonzero scalar `B=B(L,v,t)` such that for every `n>=0`,

\[
\boxed{
\widehat R_{n+1}
=
\widehat R_{-n}
=
B\,\frac{(-1)^n}{2\sinh(a(n+\tfrac12))}.
}
\tag{4}
\]

Thus the artificial theta seam does not merely create isolated poles. It creates a spectral layer of width

\[
\boxed{
a^{-1}\asymp \frac{L^2}{v}.
}
\tag{5}
\]

To keep the scale bookkeeping explicit, use the dimensionless periodic Sobolev seminorm

\[
\boxed{
\|f\|_{\dot H^s_{\rm idx}}^2
:=
\sum_{k\in\mathbb Z\setminus\{0\}}
|k|^{2s}|\widehat f_k|^2.
}
\tag{6}
\]

It differs from the standard physical seminorm on the length-`L` torus only by the common factor `(L/(2\pi))^{2s}`. Hence every relative approximation statement below is identical in either normalization.

For every fixed `s>=1` there are constants `c_s,C_s>0` such that, for all sufficiently small `a`,

\[
c_s|B|^2a^{-(2s+1)}
\le
\|R\|_{\dot H^s_{\rm idx}}^2
\le
C_s|B|^2a^{-(2s+1)}.
\tag{7}
\]

Every individual Fourier mode contributes at most `C_s|B|^2a^{-2s}` to this energy. Consequently, if `F` is **any** `L`-periodic trigonometric polynomial supported on at most `D` integer Fourier modes, then

\[
\boxed{
\frac{\|R-F\|_{\dot H^s_{\rm idx}}^2}
     {\|R\|_{\dot H^s_{\rm idx}}^2}
\ge
1-C_s aD.
}
\tag{8}
\]

In particular, capturing any fixed positive fraction of the full-period derivative energy requires

\[
\boxed{
D=\Omega(a^{-1})=\Omega(L^2/v).
}
\tag{9}
\]

At the XF-073 Xi localization scale,

\[
L=(\log T)^3,
\qquad
v=(\log T)^{3/2}+O(1),
\tag{10}
\]

so the seam bandwidth is

\[
a^{-1}=\Theta((\log T)^{9/2}).
\tag{11}
\]

The XF-067 periodic zero carrier on the same physical window has microscopic spacing `s_T=Theta(1/log T)` and therefore

\[
N=L/s_T=\Theta((\log T)^4)
\tag{12}
\]

roots and `N+1` trigonometric modes. Hence

\[
aN=\Theta((\log T)^{-1/2})\to0,
\tag{13}
\]

and every `O(N)`-mode global periodic surrogate satisfies, for each fixed `s>=1`,

\[
\boxed{
\frac{\|R-F\|_{\dot H^s_{\rm idx}}^2}
     {\|R\|_{\dot H^s_{\rm idx}}^2}
\ge
1-O((\log T)^{-1/2}).
}
\tag{14}
\]

So the natural Xi zero-count carrier is short by a factor `Theta(sqrt(log T))` for **global Sobolev approximation of the quotient itself**.

This does not rule out the remaining center-local route. It also does not prove that the actual Xi quotient realizes the matched control's seam spectrum, and it does not identify this carrier Sobolev norm with the XF-070 weighted log-Vieta resource. What it rules out is a universal argument saying that Gaussian reference division plus finite-band approximation at the ordinary Xi zero-count degree automatically gives a globally small derivative-level quotient error for all admissible backward-heat data.

## 1. The Gaussian reference has a complete simple seam divisor

At a frozen heat time suppress the harmless factor `h^{-1/2}` and write

\[
W_L(z)
=
\sum_{m\in\mathbb Z}
\exp\!\left(-\frac{(z+mL)^2}{2v}\right).
\tag{15}
\]

Poisson summation gives

\[
W_L(z)
=
C_{L,v}
\sum_{k\in\mathbb Z}
Q^{k^2}e^{2ikw}
=
C_{L,v}\,\theta_3(w,Q),
\qquad
w=\frac{\pi z}{L},
\quad
Q=e^{-a}.
\tag{16}
\]

The Jacobi triple product is

\[
\theta_3(w,Q)
=
\prod_{m\ge1}(1-Q^{2m})
(1+Q^{2m-1}e^{2iw})
(1+Q^{2m-1}e^{-2iw}).
\tag{17}
\]

Because `0<Q<1`, exactly one linear factor vanishes at each zero. Equation (17) therefore upgrades the exhibited XF-074 seam family to the complete simple divisor

\[
\boxed{
Z(W_L)
=
\left\{
\left(r+\frac12\right)L+i(2n+1)d:
r,n\in\mathbb Z
\right\}.
}
\tag{18}
\]

The same image sum gives the quasi-periodicity already used in XF-074,

\[
W_L(z+2id)=e^{a-2\pi iz/L}W_L(z).
\tag{19}
\]

Applying (19) at `z-id` gives

\[
W_L(z+id)=e^{-2\pi iz/L}W_L(z-id).
\tag{20}
\]

For the quotient (3),

\[
\boxed{R(z+2id)=e^{-a}R(z).}
\tag{21}
\]

In the strip `0<Im z<2d`, equation (18) shows that `R` has exactly one pole modulo `L`, at

\[
z_*=\frac L2+id.
\tag{22}
\]

It is simple, and its residue `rho` is nonzero because the numerator there is `W_L(L/2)>0`.

## 2. Contour translation gives the exact Fourier coefficients

Define

\[
\widehat R_k
=
\frac1L\int_0^L
R(x)e^{-2\pi ikx/L}\,dx,
\qquad k\in\mathbb Z.
\tag{23}
\]

Integrate `R(z)e^{-2\pi ikz/L}` around the rectangle with horizontal sides `Im z=0` and `Im z=2d`. The vertical sides cancel by `L`-periodicity. By (21), the upper horizontal integral in the forward direction is

\[
e^{a(2k-1)}L\widehat R_k.
\tag{24}
\]

The rectangle contains only the pole (22), so the residue theorem gives

\[
\left(1-e^{a(2k-1)}\right)L\widehat R_k
=
2\pi i\,\rho\,e^{-2\pi ikz_*/L}.
\tag{25}
\]

Since

\[
e^{-2\pi ikz_*/L}=(-1)^ke^{ak},
\tag{26}
\]

we obtain

\[
\widehat R_k
=
\frac{2\pi i\rho}{L}
\frac{(-1)^ke^{ak}}{1-e^{a(2k-1)}}.
\tag{27}
\]

Putting

\[
B:=\frac{2\pi i\rho}{L}e^{a/2}\ne0
\tag{28}
\]

and separating `k=n+1` and `k=-n` gives exactly (4).

This derivation uses only the explicit Gaussian theta divisor and the quotient quasi-periodicity. The classical theta-to-Jacobi-elliptic identity gives the same coefficient formula through the standard Fourier series of `cd`; that is a prior-art cross-check rather than a separate line-specific input.

## 3. Sobolev energy is spread across `Theta(1/a)` modes

For `s>=1`, equation (4) gives

\[
\|R\|_{\dot H^s_{\rm idx}}^2
=
\frac{|B|^2}{4}
\sum_{n\ge0}
\frac{(n+1)^{2s}+n^{2s}}
{\sinh^2(a(n+\tfrac12))}.
\tag{29}
\]

Choose the block

\[
1\le a(n+\tfrac12)\le2.
\tag{30}
\]

It contains `Theta(1/a)` indices. On it, `sinh(a(n+1/2))` is bounded above by the fixed number `sinh 2`, while `n=Theta(1/a)`. Thus

\[
\|R\|_{\dot H^s_{\rm idx}}^2
\ge
c_s|B|^2a^{-(2s+1)}.
\tag{31}
\]

Conversely, every single weighted coefficient is `O_s(|B|^2a^{-2s})`. For `a(n+1/2)<=1`, use `sinh x>=x`; for `a(n+1/2)>1`, use exponential growth of `sinh` and boundedness of `x^{2s}e^{-2x}`. Summing the same two ranges also gives the upper half of (7).

Let `S` be any set of at most `D` Fourier indices. The preceding single-mode bound and (31) imply

\[
\sum_{k\in S}|k|^{2s}|\widehat R_k|^2
\le
C_s aD\,\|R\|_{\dot H^s_{\rm idx}}^2.
\tag{32}
\]

Fourier orthogonality makes the best approximation supported on `S` the exact projection onto those coefficients. Minimizing over all such `S` gives (8). The estimate is therefore stronger than a low-pass obstruction: even an adversarial choice of `D` Fourier modes cannot capture a fixed fraction of the derivative energy while `aD=o(1)`.

## 4. The Xi zero-count degree misses the seam scale by `sqrt(log T)`

XF-073 chooses the source-localization scales (10), so

\[
a=2\pi^2(\log T)^{-9/2}(1+o(1)).
\tag{33}
\]

The intended periodic carrier has one root per microscopic Xi spacing across a window of length `L`. In the `H_0` coordinate used by XF-048--XF-071 that spacing is `Theta(1/log T)`, so (12) follows. Equivalently, in the XF-070--XF-071 notation `N=2q^2`, `s^{-2}\asymp q`, and `L=Ns`; matching `L\asymp log^3 T` gives `q\asymp log^2 T` and again `N\asymp log^4 T`.

Therefore the exact seam scale and the exact zero-count scale are distinct:

\[
\frac{a^{-1}}N
=
\Theta(\sqrt{\log T}).
\tag{34}
\]

An `N`-root Vieta carrier has exactly `N+1` trigonometric modes before nonlinear coefficient processing. If a proposed Gaussian-quotient bridge first asks such a carrier to approximate `R` globally in any fixed derivative Sobolev norm, equations (8) and (13) show that this first step already loses asymptotically all of the matched control's derivative energy.

The statement is intentionally about the **carrier function**, not the logarithmic Vieta coefficients. A finite trigonometric polynomial can have an infinite Fourier expansion after taking a logarithm, so (8) must not be reinterpreted as a truncation theorem for the XF-070 log-Vieta state.

## 5. Stress tests and evidence boundary

The matched input (2) is entire, zero-free, and solves the exact backward heat equation. The obstruction is therefore not produced by a complicated source zero set. It comes solely from periodizing and dividing the Gaussian reference, precisely the architectural mechanism isolated by XF-074.

The result is frozen-time. The frequency `omega_0` is chosen from the frozen `h(t_0)` as in XF-074, so no claim is made that one fixed shifted-theta representation persists with the same half-seam alignment over a time interval. A static approximation obstruction is enough to rule out a universal fixed-time Sobolev approximation theorem at degree `O(N)`.

The norm restriction is load-bearing. Equation (8) is proved for the full-period dimensionless Sobolev seminorm (6), equivalently for the standard physical `\dot H^s(\mathbb T_L)` seminorm after multiplying numerator and denominator by the same `(2\pi/L)^{2s}` factor. It does not rule out approximation in a much weaker norm, on the XF-073 interior half-period, or in a seam-excluding weighted norm. In particular it does not say that an approximate finite surrogate with a carefully designed transport residual is impossible.

Nor is the matched Fourier mode an Xi source. The theorem rules out arguments based only on generic backward-heat admissibility plus the Gaussian reference. An Xi-specific cancellation theorem could still make the actual quotient much more compressible than this control.

Finally, the carrier Sobolev norm is not identified with the XF-070 weighted log-Vieta resource. The relevance is architectural: any route that tries to reach the Vieta carrier by first obtaining global derivative-level closeness of `R` to an ordinary `N`-mode trigonometric polynomial faces the bandwidth gap (34) before Vieta extraction begins.

## 6. Prior art and novelty boundary

Gaussian periodization, the Jacobi theta product, the theta-to-Jacobi-elliptic dictionary, and the Fourier series of the Jacobi elliptic functions are classical. No novelty is claimed for those formulas. A targeted prior-art search found the expected theta/Jacobi identities and general trigonometric approximation theory, but no source connecting the Gaussian-reference seam parameter `a=2 pi^2 v/L^2` to the de Bruijn--Newman `L=log^3 T` localization window, the `N=Theta(log^4 T)` Xi zero-count carrier, or the resulting `Omega(log^(9/2) T)` mode requirement for full-period derivative Sobolev approximation.

The line-specific content is the exact contour extraction (25)--(28) from the XF-074 matched control and the scale comparison (33)--(34). Because the proof is self-contained from the explicit periodized Gaussian and classical theta identities, no new external theorem is load-bearing for the Xi-specific conclusion and `SOURCES.md` does not need a new anchor.

## 7. Consequence for `xi_flow`

XF-076 left three broad possibilities after the exact finite-band no-go: stay center-local, allow a quantitative approximate finite surrogate, or use a more elaborate source-dependent seam treatment. XF-077 removes the naive version of the second option. At the existing Vieta degree `N=Theta(log^4 T)`, a universal full-period Sobolev approximation of the Gaussian quotient is not merely imperfect; on a matched zero-free control its relative derivative-energy error tends to one.

A global approximate surrogate can still survive by paying at least the inverse-seam bandwidth

\[
D=\Omega((\log T)^{9/2}),
\tag{35}
\]

and then proving that the enlarged carrier's normalization, auxiliary zeros, transport residual, and connection to the XF-070 resource remain controlled. That is a new scale, larger than the physical Xi zero count by `Theta(sqrt(log T))`.

The cheaper live route is therefore the one already suggested by XF-074--XF-076: **do not approximate through the seam**. Keep the Gaussian quotient on the center-local safe region and derive a destination statistic that can be transported or compared without demanding a full-period derivative-Sobolev reconstruction. The remaining transition-nontriviality gate is unchanged.

No upper bound on `Lambda` follows here, and no RH implication is claimed.
