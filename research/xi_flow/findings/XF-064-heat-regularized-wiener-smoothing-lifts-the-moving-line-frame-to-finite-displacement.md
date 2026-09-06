# XF-064 — heat-regularized Wiener smoothing lifts the moving-line frame to finite displacement

**Status:** `EXACT-DERIVED` + `FINITE-DISPLACEMENT-FRAME` + `HEAT-REGULARIZED` + `STRUCTURAL/REPAIR`. XF-063 closes the positive-time selector-frame problem for the **first variation** of the moved lattice, but leaves open whether evaluating the same selector on an `O(1)` root displacement can broaden sidebands or transfer enough frequency mass to destroy the lower frame. In the exact periodic tangent heat model, that measurement nonlinearity does not reopen the gate.

The key quantity is not the pointwise displacement amplitude by itself. Fixed positive heat time reduces the Fourier Wiener norm of every initially bounded tangent from its worst possible `O(q)` size to only `O(sqrt(q))`. The outer selector frequency is `O(log log T/q)`, so the nonlinear phase parameter in the Wiener algebra is

\[
\frac{\log\log T}{q}\,O(\sqrt q)
=O\!\left(\frac{\log\log T}{\sqrt q}\right)
=o(1).
\]

Every quadratic and higher power in the exact moved selector therefore becomes a geometrically small perturbation of the XF-063 tangent frame, uniformly over all bounded initial tangents.

Use the XF-062--XF-063 scales

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
s=\frac{4\pi}{\log(T/4\pi)},
\tag{1}
\]

and the fixed nonzero XF-056 envelope `g` with

\[
\chi:=\widehat g\in C_c^\infty((-1,1)),
\qquad
C_g:=\int_{\mathbb R}|\chi(u)|^2\,du>0.
\tag{2}
\]

Let `a(t)` be the exact `N`-periodic arithmetic-lattice tangent flow of XF-062, with

\[
\|a(0)\|_{\ell^\infty}\le A_0,
\tag{3}
\]

and fix `tau>0`. For the same constant `C>C_*(tau)` used by XF-062--XF-063, write

\[
B_T^{\rm in}
=
\left[
2q^{-3/2},
\frac{C\log\log T}{q}
\right],
\qquad
B_T^{\rm out}
=
\left[
q^{-3/2},
\frac{(C+1)\log\log T}{q}
\right].
\tag{4}
\]

For a real periodic displacement `a`, define the **exact finite-displacement moved selector in index coordinates**

\[
\boxed{
\mathcal N_{M,a}(\theta)
:=
\sum_{j\in\mathbb Z}
 g\!\left(\frac{j+a_j}{M}\right)
 e^{-i\theta(j+a_j)}.
}
\tag{5}
\]

On `B_T^{out}` the undisplaced lattice contribution is exactly zero for all sufficiently large `T`, because `M theta>=q^{1/2}>1` and `supp chi subset (-1,1)`. Thus (5) is already the exact nonlinear response relative to the lattice baseline.

Let `mathcal L_{M,a}` be the XF-063 first variation,

\[
\mathcal L_{M,a}(\theta)
=
\sum_j a_j
\left[
\frac1M g'(j/M)-i\theta g(j/M)
\right]e^{-i\theta j}.
\tag{6}
\]

Equip selector functions with the XF-060/XF-063 weighted norm

\[
\|F\|_{X_T}^2
:=
M\int_{B_T^{\rm out}}
(M\theta^2)^2|F(\theta)|^2\,d\theta.
\tag{7}
\]

Then the exact finite-displacement response at positive tangent heat time satisfies

\[
\boxed{
\|\mathcal N_{M,a(\tau)}-\mathcal L_{M,a(\tau)}\|_{X_T}
\le
\varepsilon_T\,
\mathcal Q_M(( -\pi,\pi],\tau)^{1/2},
}
\tag{8}
\]

where

\[
\boxed{
\varepsilon_T
=O_{A_0,\tau,C,g}\!\left(
\frac{\log\log T}{\sqrt q}
\right)
=o(1).
}
\tag{9}
\]

Here `mathcal Q_M` is the XF-062 tangent `H^3` energy,

\[
\mathcal Q_M(B,t)
=M^3\sum_{\xi_\ell\in B}
|e^{i\xi_\ell}-1|^6
|\widehat a_\ell(t)|^2.
\tag{10}
\]

Consequently the XF-063 lower frame survives **without an infinitesimal displacement parameter**. If

\[
\liminf_{T\to\infty}
\mathcal F_M^{\rm lin}(\tau;a)>c_0>0,
\tag{11}
\]

then

\[
\boxed{
\liminf_{T\to\infty}
M\int_{B_T^{\rm out}}
(M\theta^2)^2
|\mathcal N_{M,a(\tau)}(\theta)|^2\,d\theta
\ge
\frac{C_gc_0^2}{18}>0.
}
\tag{12}
\]

Thus bounded periodic lattice tangents that retain critical triple flux after fixed positive heat time remain visible even when the moving-line statistic is evaluated on the **fully displaced points** `j+a_j(t)`, rather than only through its first variation at the lattice.

This is a genuine finite-amplitude repair of the *measurement* side of XF-063. It is not yet a nonlinear zero-flow theorem: the state `a(t)` still evolves by the exact tangent semigroup, not by the finite-amplitude Xi root dynamics. No comparison of an actual transition block with `a(t)` is proved, no collision or complex-root interval is crossed, and no upper bound on the de Bruijn--Newman constant follows.

## 1. Positive heat time reduces the relevant Wiener norm

For the unitary discrete Fourier transform on `Z/NZ`, define

\[
\mathfrak W(a)
:=
\frac1{\sqrt N}
\sum_\ell |\widehat a_\ell|.
\tag{13}
\]

This normalization makes `mathfrak W` the natural Fourier algebra norm for pointwise products. XF-062 gives, for every nontranslation mode,

\[
\widehat a_\ell(\tau)
=e^{-\rho_s(|\xi_\ell|)\tau}
\widehat a_\ell(0),
\qquad
\rho_s(\xi)
=\frac{\xi(2\pi-\xi)}{s^2}.
\tag{14}
\]

Since `s^{-2}asymp q`, there is a fixed `c_tau>0` such that, for principal frequencies `xi_ell=pi ell/M` with `1<=ell<=M`,

\[
2\rho_s(\xi_\ell)\tau
\ge c_\tau\frac{\ell}{q}.
\tag{15}
\]

Hence

\[
\sum_{\ell\ne0}
 e^{-2\rho_s(|\xi_\ell|)\tau}
=O_\tau(q).
\tag{16}
\]

By Cauchy--Schwarz, Parseval, and (3),

\[
\begin{aligned}
\mathfrak W(a(\tau))
&\le
\frac{|\widehat a_0|}{\sqrt N}
+
\frac1{\sqrt N}
\left(\sum_{\ell\ne0}e^{-2\rho_s\tau}\right)^{1/2}
\|a(0)\|_2\\
&\le
A_0+C_{\tau}A_0\sqrt q.
\end{aligned}
\tag{17}
\]

Therefore

\[
\boxed{
\mathfrak W(a(\tau))=O_{A_0,\tau}(\sqrt q).
}
\tag{18}
\]

The same calculation with one discrete derivative gives

\[
\|\Delta a(\tau)\|_\infty
=O_{A_0,\tau}(q^{-1/2}).
\tag{19}
\]

Thus for sufficiently large `T` the fully displaced points `j+a_j(tau)` remain strictly ordered, even though `a_j(tau)` itself need not tend to zero. The finite-displacement configuration in (5) is therefore geometrically legitimate in the periodic model, not merely a formal evaluation of the selector.

The important contrast is time zero. From only `||a(0)||_infinity<=A_0`, the worst possible Wiener norm is `O(A_0 q)`, for which `theta_max mathfrak W(a)` need not vanish. Positive heat time improves precisely the norm that controls nonlinear frequency multiplication.

## 2. The discrete Wiener algebra preserves the third-difference scale

Let

\[
m(\xi):=e^{i\xi}-1
\tag{20}
\]

and define

\[
\|b\|_{\dot H_m^3}^2
:=
\sum_\ell |m(\xi_\ell)|^6|\widehat b_\ell|^2.
\tag{21}
\]

For products, the unitary DFT gives a normalized convolution. Moreover the exact telescoping identity on the unit circle implies

\[
|m(\xi_1+\cdots+\xi_r)|
\le
\sum_{h=1}^r|m(\xi_h)|.
\tag{22}
\]

Using `(sum x_h)^3<=r^2 sum x_h^3`, Young's convolution inequality, and the normalization (13), one obtains the elementary tame product estimate

\[
\boxed{
\|a^r\|_{\dot H_m^3}
\le
r^3\,\mathfrak W(a)^{r-1}
\|a\|_{\dot H_m^3},
\qquad r\ge1.
}
\tag{23}
\]

The exact polynomial `r^3` is not important; factorials from the analytic expansion below dominate it. What matters is that nonlinear multiplication costs powers of the **Wiener norm**, while retaining exactly one copy of the third-difference energy.

By (10),

\[
M^{3/2}\|a(\tau)\|_{\dot H_m^3}
=
\mathcal Q_M(( -\pi,\pi],\tau)^{1/2}.
\tag{24}
\]

Thus every nonlinear power of the heat-regularized displacement can still be measured against the same `H^3` quantity used by XF-062--XF-063.

## 3. Exact analytic expansion of the fully moved selector

Because `chi` is smooth and compactly supported, `g` is entire of exponential type. For bounded `a_j`, both the envelope shift and phase shift in (5) may therefore be expanded absolutely:

\[
\mathcal N_{M,a}(\theta)
=
\sum_{n,k\ge0}
\frac{(-i\theta)^k}{n!k!M^n}
\sum_j
 a_j^{n+k}g^{(n)}(j/M)e^{-i\theta j}.
\tag{25}
\]

The `(n,k)=(0,0)` term is the undisplaced lattice and vanishes identically on `B_T^{out}`. The two terms with `n+k=1` are exactly

\[
\frac1M\sum_j a_jg'(j/M)e^{-i\theta j}
-i\theta\sum_j a_jg(j/M)e^{-i\theta j},
\tag{26}
\]

which sum to `mathcal L_{M,a}`. Hence the nonlinear remainder is precisely the sum of all terms with

\[
n+k\ge2.
\tag{27}
\]

This expansion keeps the full displacement amplitude. No `epsilon->0` limit is taken.

## 4. Compact Fourier support diagonalizes every nonlinear power separately

Let `b` be any real `N`-periodic sequence. Expanding it in discrete Fourier modes and applying Poisson summation gives

\[
\sum_j b_jg^{(n)}(j/M)e^{-i\theta j}
=
\frac{M}{\sqrt N}
\sum_\ell
\widehat b_\ell
\bigl(iM(\theta-\xi_\ell)\bigr)^n
\chi\!\left(M(\theta-\xi_\ell)\right),
\tag{28}
\]

with the understood principal alias. As in XF-063, distinct sidebands are disjoint because their spacing is `pi/M` while each has half-width `1/M`.

For

\[
T_{n,k}[b](\theta)
:=
\frac{(-i\theta)^k}{n!k!M^n}
\sum_j b_jg^{(n)}(j/M)e^{-i\theta j},
\tag{29}
\]

change variables `u=M(theta-xi_ell)` on each active sideband. Since `|u|<1`, `N=2M`, and all sidebands meeting `B_T^{out}` have centers within `1/M` of that band, disjointness yields

\[
\|T_{n,k}[b]\|_{X_T}
\le
\frac{C_g'}{n!k!}
M^{3/2-n}
\left(
\sum_{\xi_\ell\in B_T^{\rm out,+}}
|\xi_\ell|^{2k+4}
|\widehat b_\ell|^2
\right)^{1/2},
\tag{30}
\]

where `B_T^{out,+}` denotes a harmless `1/M` enlargement and `C_g'` depends only on the fixed window. The same estimate holds if `|xi|` is replaced by `|m(xi)|` up to an absolute constant, since the entire band tends to zero and lies a distance much larger than `1/M` from the origin.

Set

\[
\theta_-:=q^{-3/2},
\qquad
\theta_+:=\frac{(C+1)\log\log T}{q},
\qquad
W_\tau:=\mathfrak W(a(\tau)).
\tag{31}
\]

For `k>=1`, every active center satisfies

\[
|\xi|^{k+2}
\ll
\theta_+^{k-1}|m(\xi)|^3.
\tag{32}
\]

Applying (23) to `b=a^{n+k}` therefore gives, for every nonlinear term with `k>=1`,

\[
\frac{\|T_{n,k}[a^{n+k}]\|_{X_T}}
{\mathcal Q_M^{1/2}}
\ll_g
\frac{(n+k)^3}{n!k!}
\left(\frac{W_\tau}{M}\right)^n
(\theta_+W_\tau)^{k-1}.
\tag{33}
\]

The pure-envelope nonlinear terms have `k=0` and necessarily `n>=2`. On the outer band,

\[
|\xi|^2
\ll
\theta_-^{-1}|m(\xi)|^3,
\tag{34}
\]

so

\[
\frac{\|T_{n,0}[a^n]\|_{X_T}}
{\mathcal Q_M^{1/2}}
\ll_g
\frac{n^3}{n!}
\theta_-^{-1}M^{-1}
\left(\frac{W_\tau}{M}\right)^{n-1}.
\tag{35}
\]

Equations (33)--(35) are the finite-amplitude analogue of the single-mode cancellation used in XF-063. They show exactly where nonlinear mode coupling can enter and which two dimensionless parameters control it.

## 5. Both nonlinear parameters vanish after fixed heat time

From (18), (31), and `M=q^2`,

\[
\alpha_T
:=
\frac{W_\tau}{M}
=O(q^{-3/2}),
\tag{36}
\]

while

\[
\boxed{
\beta_T
:=
\theta_+W_\tau
=O\!\left(
\frac{\log\log T}{\sqrt q}
\right)
=o(1).
}
\tag{37}
\]

For the envelope-only series,

\[
\theta_-^{-1}M^{-1}\alpha_T
=O(q^{-2}).
\tag{38}
\]

The factorials in (33)--(35) make the complete double series absolutely summable, and for sufficiently large `T` its nonlinear part is bounded by

\[
O_{A_0,\tau,C,g}(\beta_T+\alpha_T+q^{-2}).
\tag{39}
\]

Combining (27), (33), (35), and (39) proves (8)--(9).

There is a useful conceptual distinction here. Compact support of `chi` still diagonalizes **each power** `a^r`, but different powers can place energy on the same sideband and need not be mutually orthogonal. The proof does not assume otherwise. Instead it sums their norms by the triangle inequality, and positive-time Wiener smoothing makes that potentially adverse sum a vanishing fraction of the tangent `H^3` energy.

## 6. The nonlinear lower frame inherits the XF-063 constant

XF-063 proves

\[
\|\mathcal L_{M,a(\tau)}\|_{X_T}^2
\ge
\left(\frac{C_g}{4}+o(1)\right)
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in}),\tau\bigr).
\tag{40}
\]

XF-062 and the infrared refinement used in XF-063 give

\[
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in}),\tau\bigr)
=
\mathcal Q_M(( -\pi,\pi],\tau)+o(1)
\tag{41}
\]

uniformly over the bounded initial family. Under the critical-flux hypothesis (11), XF-062 also gives

\[
\liminf_{T\to\infty}
\mathcal Q_M(( -\pi,\pi],\tau)
\ge
\frac{2c_0^2}{9}.
\tag{42}
\]

By the reverse triangle inequality and (8),

\[
\|\mathcal N_{M,a(\tau)}\|_{X_T}
\ge
\|\mathcal L_{M,a(\tau)}\|_{X_T}
-arepsilon_T\mathcal Q_M^{1/2}.
\tag{43}
\]

Since `epsilon_T=o(1)` and the complement in (41) is `o(1)`, the asymptotic lower-frame coefficient is unchanged. Equations (40)--(43) prove (12).

In particular, the exact finite-displacement selector cannot be made small by phase cancellation among its quadratic and higher terms while the positive-time tangent triple flux remains critical. Any such cancellation would have to compete with an order-one linear frame using nonlinear terms whose total norm is only an `o(1)` fraction of the same `H^3` energy.

## 7. Stress tests and evidence boundary

A uniform translation `a_j=c` has `mathcal Q_M=0`. The exact selector (5) also vanishes on `B_T^{out}` by shifted Poisson summation, so (8) is consistent with the translation null mode rather than charging it through the absolute amplitude `|c|`.

A single coherent slow wave already has a small Wiener norm, so its finite-amplitude selector is perturbatively close to the tangent response even before invoking the full `O(sqrt q)` heat estimate. The positive-time argument is needed for arbitrary broadband bounded tangents, whose time-zero Wiener norm can be as large as `O(q)` and for which `theta_+ mathfrak W(a)` is not forced to vanish.

The XF-061 sparse defect presents the opposite extreme: it is spectrally broad at time zero, but XF-062 removes its critical `H^3` flux after fixed positive time. XF-064 shows that evaluating the selector nonlinearly on the resulting smoothed displacement does not recreate a hidden order-one cancellation channel.

The result does **not** show that the true finite-amplitude zero flow is close to the tangent semigroup for a fixed positive time. In particular, it does not control the Duhamel error generated by nonlinear gap conductances, prove that transition flux survives until `tau`, or define ordered real roots through a collision/complex interval. Those are now the live nonlinear/dynamical gates. What is closed here is narrower: once a bounded transition state has legitimately entered the XF-062 positive-time tangent regime, the exact moved-point measurement itself no longer requires an infinitesimal-amplitude assumption.

## 8. Prior-art and novelty boundary

Perturbed exponential bases, nonuniform sampling, Gabor/STFT frames, and tame Sobolev/Wiener product estimates are classical. A targeted audit found the Kadec `1/4` stability tradition, Daubechies--Grossmann--Meyer painless nonorthogonal expansions, and modern perturbed trigonometric interpolation results to cover neighboring frame and sampling phenomena. None supplies the Mathia-specific conjunction used above: the exact XF-062 Cauchy-lattice heat multiplier, the `q^2` selector width, the shrinking `log log T/q` source cone, the compact-support sideband geometry of XF-056/XF-063, and the resulting positive-time Wiener parameter `theta_+ mathfrak W(a(tau))=o(1)`.

No novelty is claimed for Fourier algebra product estimates, Poisson summation, or stability of frames under perturbation. The proof above is self-contained from the exact tangent multiplier and compact-band selector already canonical in `xi_flow`; no external theorem is load-bearing, so `SOURCES.md` requires no new anchor.

## 9. Consequence for `xi_flow`

XF-062 removes the static high-frequency escape after fixed tangent heat time, XF-063 proves that the surviving tangent `H^3` energy is framed by the source-controlled moving-line selector, and XF-064 shows that **finite evaluation of that selector on the displaced lattice has the same lower frame asymptotically**. The remaining obstruction is therefore not a hidden nonlinear defect of the measurement map.

The next decisive gate is dynamical. One must either compare a source-compatible finite-amplitude transition block to the positive-time tangent regime with an error small in the same `H^3`/Wiener scale while proving that critical transition flux survives the comparison delay, or construct a genuine nonlinear/collision-time trajectory that loses the framed flux before tangentization. Further perturbations of the selector formula itself are no longer the main missing step.