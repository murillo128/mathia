# WI-224 — Adaptive spline detectors localize dyadic screens to physical O(M) radius

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

WI-223 proves that a **fixed** compact detector can localize any exact dyadic zeta-zero screen only to physical radius

\[
M\,D(\log T),
\]

with `D` an arbitrarily slowly diverging Denjoy--Carleman loss, and it identifies Ingham's fixed-function uncertainty theorem as the obstruction to genuine exponential Fourier decay. That obstruction is real but it is not stable under the `T`-dependent detector family explicitly left open there.

In the same inherited screen model, one can choose a compactly supported smooth detector `phi_T` depending on `T`, with **uniformly bounded `L^2` norm and uniformly nonzero target overlap**, whose Fourier--Laplace transform is exponentially small once the natural frequency is `O(log T)`. Combining this with exactly the same Jutila radial-mass budget as WI-221--WI-223 gives

\[
\boxed{
\sum_{|\gamma_\rho-\gamma_0|\le C M}
\mu_\rho\cosh(k a_\rho)
\gg M
}
\tag{1}
\]

for a constant `C` depending only on the fixed screen parameters and on the exponent in `M=T^{\vartheta+o(1)}`. Thus the iterated-log loss of WI-223 is not intrinsic: **adaptive compact detectors improve the forced physical localization to `O(M)` without any stronger zeta arithmetic.**

There is also a complementary exact barrier. Under the inherited `L^2(J)` screen residual with no quantitative convergence rate, a robust adaptive detector family must keep its `L^2` norm uniformly bounded. For any such fixed-support family with fixed nonzero integral, the Fourier cutoff radius cannot remain bounded while the exterior Fourier supremum tends to zero. Consequently this same adaptive-detector + total-mass-tail architecture cannot reach the original physical bow radius `O(M/log T)`: it necessarily has natural-frequency cutoff `R_T -> infinity`, hence physical radius

\[
\omega(M/\log T).
\tag{2}
\]

The exact frontier between the achieved `O(M)` and the necessary `omega(M/log T)` remains open.

## 1. Inherited screen model and the only source budget used

Use the WI-218--WI-223 normalization. At one fixed interior reciprocal harmonic `0<k<d`, let

\[
M=T^{\vartheta+o(1)},
\qquad \vartheta>0,
\qquad
\eta_M=\frac{\log T}{2dM}=o(1),
\tag{3}
\]

and

\[
F_M:=K_{\eta_M}f_{M,k},
\qquad
F:=K_0(C_k\operatorname{sinc}).
\tag{4}
\]

WI-218 gives compact convergence `F_M -> F`, with `F` real continuous and not identically zero. Assume the same dyadic-zero-screen hypothesis as WI-221--WI-223 on one fixed compact interval `J`:

\[
\|F_M+K_{\eta_M}g_M\|_{L^2(J)}=o(1).
\tag{5}
\]

A mirror pair contributes two exponential channels with

\[
z_\pm=\alpha_\pm+2\pi i\xi_\pm,
\qquad
|\alpha_\pm|=a/M=o(1),
\qquad
|\xi_\pm|=|\nu|/M,
\tag{6}
\]

and coefficient magnitudes

\[
|c_+|=\frac{\mu e^{ak}}M,
\qquad
|c_-|=\frac{\mu e^{-ak}}M.
\tag{7}
\]

As in WI-223, all relevant real tilts eventually satisfy `|alpha|<=1`, the multiplier of `K_{eta_M}` is uniformly bounded on that strip, and Jutila's audited near-line zero-density input gives

\[
\boxed{
\sum_{T<\gamma\le2T}
\mu_\rho\cosh(k a_\rho)
\ll_{k,d}N_T,
}
\qquad
N_T\asymp T\log T.
\tag{8}
\]

No pair correlation, higher moment, support enlargement, or stronger zero-density theorem is used below.

## 2. A `T`-dependent compact detector with uniform conditioning

Choose a fixed interval `J_0 compactly contained in J` on which `F` has constant sign and

\[
|F(u)|\ge c_0>0.
\tag{9}
\]

Choose a fixed nonnegative `C_c^infty` probability density `chi_0` supported on an interval `I`, and a fixed `delta>0`, so that

\[
I+[-\delta/2,\delta/2]\subset J_0.
\tag{10}
\]

For an integer `n>=1` put

\[
b_n:=\delta/n,
\qquad
h_{b_n}(u):=b_n^{-1}{\bf 1}_{[-b_n/2,b_n/2]}(u),
\tag{11}
\]

and define

\[
\psi_n:=h_{b_n}^{*n},
\qquad
\phi_n:=\chi_0*\psi_n.
\tag{12}
\]

These are elementary cardinal-spline windows smoothed by one fixed `C_c^infty` core. They satisfy

\[
\phi_n\ge0,
\qquad
\int\phi_n=1,
\qquad
\operatorname{supp}\phi_n\subset J_0,
\qquad
\phi_n\in C_c^\infty.
\tag{13}
\]

The fixed smooth core is important. A raw order-`n` spline can concentrate as `n` grows, which would make its `L^2` norm an unsafe multiplier of the unspecified `o(1)` residual in (5). Here Young's inequality gives the uniform bound

\[
\boxed{
\|\phi_n\|_2
\le
\|\chi_0\|_2\|\psi_n\|_1
=
\|\chi_0\|_2.
}
\tag{14}
\]

The target overlap is also uniform. From (9), positivity, and unit mass,

\[
\left|\int\phi_n(u)F(u)\,du\right|\ge c_0,
\tag{15}
\]

and compact convergence `F_M->F` gives, for all sufficiently large `M` and **uniformly in `n`**,

\[
\left|\int\phi_n(u)F_M(u)\,du\right|\ge c_0/2.
\tag{16}
\]

Finally (14) makes the screen residual uniformly harmless:

\[
|\langle\phi_n,F_M+K_{\eta_M}g_M\rangle|
\le
\|\chi_0\|_2\,
\|F_M+K_{\eta_M}g_M\|_{L^2(J)}
=o(1).
\tag{17}
\]

Thus `n=n(T)` may grow without consuming an unproved rate in (5).

## 3. Exact Fourier--Laplace tail of the spline factor

For

\[
\Phi_n(z):=\int\phi_n(u)e^{zu}\,du,
\qquad
X_0(z):=\int\chi_0(u)e^{zu}\,du,
\tag{18}
\]

repeated convolution gives the exact factorization

\[
\boxed{
\Phi_n(z)
=
X_0(z)
\left(
\frac{\sinh(z\delta/(2n))}{z\delta/(2n)}
\right)^n.
}
\tag{19}
\]

This is the standard sinc-power Fourier behavior of a cardinal B-spline, here written on the complex strip needed by the off-line channels. Since `chi_0` has fixed compact support,

\[
C_\chi:=\sup_{|\Re z|\le1}|X_0(z)|<\infty.
\tag{20}
\]

Write `z=alpha+2 pi i xi` and

\[
x:=\frac{\alpha\delta}{2n},
\qquad
y:=\frac{\pi\xi\delta}{n}.
\tag{21}
\]

The elementary identity

\[
\left|
\frac{\sinh(x+iy)}{x+iy}
\right|^2
=
\frac{\sinh^2x+\sin^2y}{x^2+y^2}
\tag{22}
\]

controls the full Fourier--Laplace strip. For `|y|>=1`,

\[
\frac{|\sin y|}{|y|}
\le \sin 1=:q_0<1.
\tag{23}
\]

Indeed `sin y/y` decreases on `[1,pi]`, while every later lobe is bounded by `1/pi<sin 1`. Also

\[
|\sinh x|
\le |x|\cosh(\delta/2)
\tag{24}
\]

because `|x|<=delta/(2n)<=delta/2`. Hence

\[
\left|
\frac{\sinh(x+iy)}{x+iy}
\right|^2
\le
q_0^2+
\bigl(\cosh^2(\delta/2)-q_0^2\bigr)
\frac{x^2}{x^2+y^2}
\le
q_0^2+\frac{C_\delta}{n^2}.
\tag{25}
\]

Choose any fixed `q` with `q_0<q<1`. Then for all `n>=n_0(delta,q)`, all `|alpha|<=1`, and all

\[
|\xi|\ge R_n:=\frac{n}{\pi\delta},
\tag{26}
\]

we have the uniform exponential tail

\[
\boxed{
|\Phi_n(\alpha+2\pi i\xi)|
\le C_\chi q^n.
}
\tag{27}
\]

No asymptotic approximation is used in (19)--(27).

## 4. Choosing `n` on the logarithmic scale forces source mass into `O(M)`

The nontrivial screening regime is fixed `0<vartheta<1`; if `vartheta>=1`, the global source-budget factor `N_T/M` is no larger and the same construction is not harder. Take

\[
n_T=\lceil C\log T\rceil
\tag{28}
\]

with `C>0` chosen so that

\[
C|\log q|>1-\vartheta.
\tag{29}
\]

The `T^{o(1)}` factor in `M` and the extra `log T` in `N_T` are absorbed by taking (29) with any fixed positive margin. From (7), (8), the bounded `K_{eta_M}` multiplier, and (27), the total contribution to the detector pairing from channels with `|xi|>=R_{n_T}` is

\[
\ll
\frac{N_T}{M}q^{n_T}
=
o(1).
\tag{30}
\]

But (16)--(17) force the complete screen pairing to have fixed nonzero size. Therefore the complementary channels `|xi|<R_{n_T}` must contribute fixed order. Every such individual channel has detector and `K_{eta_M}` factors bounded by constants independent of `T`, so their radial coefficient ledger must obey

\[
\boxed{
\sum_{|\xi_\rho|<R_{n_T}}
\mu_\rho\cosh(k a_\rho)
\gg M.
}
\tag{31}
\]

In the inherited normalization

\[
\nu_\rho
=
\frac{(\gamma_\rho-\gamma_0)\log T}{2\pi d},
\qquad
\xi_\rho=\nu_\rho/M.
\tag{32}
\]

Since `R_{n_T}=O(log T)`, (32) converts (31) into

\[
|\gamma_\rho-\gamma_0|
\le
\frac{2\pi d M}{\log T}R_{n_T}
=O(M),
\tag{33}
\]

which proves (1).

The constants deteriorate as `vartheta` decreases or as the fixed support margin `delta` shrinks, but remain independent of `T` for every fixed admissible set of parameters.

## 5. A compactness barrier at the original bow scale

The adaptive construction removes WI-223's fixed-detector obstruction at physical scale `O(M)`, but it does not license arbitrary adaptation. The residual in (5) is only `o(1)` with no rate, so the dual pairing is uniformly valid for a varying detector only when its `L^2` norm stays bounded.

This yields an exact no-go statement. Let `(varphi_j)` be any family supported in one fixed compact interval `I`, satisfying

\[
\int_I\varphi_j=1,
\qquad
\sup_j\|\varphi_j\|_{L^2(I)}<\infty.
\tag{34}
\]

There is **no fixed finite `R`** for which

\[
\sup_{|\xi|\ge R}
|\widehat\varphi_j(\xi)|
\longrightarrow0.
\tag{35}
\]

To prove this, take a weakly convergent subsequence in the bounded set of `L^2(I)`, say `varphi_j weakto varphi`. The integral is a continuous linear functional on `L^2(I)`, so `int varphi=1`. For each fixed real `xi`, Fourier evaluation is also a continuous linear functional, hence

\[
\widehat\varphi_j(\xi)
\to
\widehat\varphi(\xi).
\tag{36}
\]

If (35) held, then `widehat varphi(xi)=0` for every `|xi|>=R`. Because `varphi` is compactly supported and belongs to `L^1`, its Fourier transform extends to an entire function. Vanishing on an open real ray forces that entire function to vanish identically, contradicting `widehat varphi(0)=int varphi=1`.

For `0<vartheta<1`, any total-mass tail estimate based only on (8) needs its detector tail factor to tend to zero, in fact to beat `T^{-(1-vartheta)+o(1)}`. Therefore its admissible natural-frequency cutoff cannot stay `O(1)` under the robust uniform-`L^2` condition. Since physical radius equals

\[
\frac{M}{\log T}\,O(R_T),
\tag{37}
\]

this proves the lower-order restriction (2). It does **not** prove that `R_T` must be of order `log T`; an intermediate adaptive construction with `R_T=o(log T)` is not excluded.

## 6. Prior-art and novelty audit

The spline ingredients are classical. Michael Unser's 1999 spline survey records the repeated-convolution/cardinal B-spline calculus and the associated sinc-power Fourier structure used in (19). The neighboring optimal time--frequency concentration problem is classical Slepian--Pollak/Landau--Pollak theory: fixed time support and frequency concentration are governed by prolate spheroidal functions. These sources establish the general harmonic-analysis landscape; they do **not** provide the zeta-screen consequence (1).

Sources checked:

- Michael Unser, **Splines: A Perfect Fit for Signal and Image Processing**, *IEEE Signal Processing Magazine* 16:6 (1999), 22--38, DOI `10.1109/79.799930`.
- D. Slepian and H. O. Pollak, **Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — I**, *Bell System Technical Journal* 40:1 (1961), 43--63, DOI `10.1002/j.1538-7305.1961.tb03976.x`.
- H. J. Landau and H. O. Pollak, **Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty — II**, *Bell System Technical Journal* 40:1 (1961), 65--84, DOI `10.1002/j.1538-7305.1961.tb03977.x`.
- A direct search around adaptive/time-dependent compact test functions, B-spline/sinc-power detectors, and zeta zero-density/screening arguments did not surface this application. Absence from that search is **not** a priority claim.

The new content here is the exact specialization of a `T`-dependent uniformly conditioned spline family to the WI-223 screen normalization, together with the weak-compactness barrier showing that bounded-`L^2` adaptation still cannot reach a fixed natural-frequency cutoff. The construction and barrier are derived here; no novelty claim beyond that audited mathematical delta is asserted.

## 7. Boundaries and consequences for the line

This finding is a theorem **inside the inherited WI-218--WI-223 dyadic-screen model**, not yet a new theorem about the proportion of zeta zeros. In particular:

- (31) is radial-weighted source mass, not raw zero count. Deep off-line zeros can carry weight larger than one, so `Omega(M)` weighted mass does not imply `Omega(M)` distinct zeros.
- A physical interval of radius `O(M)` has ordinary Riemann--von Mangoldt capacity of order `M log T`, so even replacing radial mass by raw count would still leave a logarithmic capacity gap at this scale.
- The construction does not distinguish multiple critical-line zeros from off-line mirror pairs and does not by itself convert the uncertified complement into a positive-density off-line population.
- The compactness argument closes only robust detector families with fixed support, fixed nonzero normalization, and uniformly bounded `L^2` norm under the same total-source-mass tail estimate. A quantitatively stronger screen residual could permit controlled `L^2` growth, and coupled observables or source covariance need not reduce to a scalar Fourier tail.
- The achieved `R_T=O(log T)` may not be optimal. The live gap is whether one can force `R_T=o(log T)` while preserving the same conditioning and polynomially small tail, or prove an uncertainty lower bound of order `R_T=Omega(log T)` for this minimax problem.

The immediate research priority changes accordingly. Repeating fixed Denjoy--Carleman optimization is no longer useful: its `D(log T)` loss is an artifact of fixing the detector before `T`. The live choices are now (i) convert the `Omega(M)` radial mass already forced inside physical `O(M)` into a sharper local zero/source contradiction, (ii) solve the adaptive minimax cutoff problem between `omega(1)` and `O(log T)`, or (iii) leave scalar total-mass tails and exploit coupled/full signed source covariance.