# NB-240 — Short-interval pair correlation still erases Ford carrier packets

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + FRESH-PRIOR-ART-AUDIT + NEGATIVE/METHOD-BOUNDARY + SHORT-INTERVAL-PAIR-CORRELATION + MESOSCOPIC-CARRIER-SCALE + NB-232/NB-239-REFINEMENT + SOURCE-ONLY`.

`NB-232` showed that a global Montgomery-type pair statistic can be asymptotically unchanged by arbitrarily sparse insertion of the carrier-critical packets from `NB-231`. That left a natural possibility: perhaps a genuinely **short-interval** pair-correlation theorem removes the global dilution and sees the dangerous packet at the selected height.

A fresh result of Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals* (arXiv:2609.07918, September 2026), proves an unconditional Montgomery pair-correlation formula in every power-length interval

\[
I=(T,T+T^\theta],\qquad 0<\theta<1
\]

for fixed smooth test functions. Auditing that theorem against the Ford carrier gives a stronger negative conclusion than the global argument in `NB-232`.

There are **two independent scale mismatches**. First, the theorem's stated error is stable under insertion of `O(log log T)` arbitrary critical-strip zeros in the interval, even after functional-equation reflections are included. The complete `NB-231` packet therefore fits strictly below the resolution of the published asymptotic. Second, for the same-depth near-one part of the packet, the fixed Montgomery test kernel itself annihilates every off-diagonal carrier interaction: the packet spacing is `Theta(1/R)`, while the pair kernel is normalized at the much finer mean-zero spacing `Theta(1/log T)`.

Thus replacing **global** pair correlation by the currently available **short-interval** pair correlation does not close the Ford transition. A useful two-point theorem would have to be simultaneously short-height, Ford-depth-conditioned, and **mesoscopically retuned to the carrier mode**; fixed-test mean-spacing pair correlation is not enough.

## 1. The fresh short-interval theorem and the Ford scales

Write

\[
Q:=\log T,\qquad
\ell:=\log Q,\qquad
R:=Q^{2/3}\ell^{1/3},\qquad
X\asymp R.
\tag{1}
\]

Retain the conservative critical-packet regime of `NB-231`,

\[
1\ll J\le \ell,
\tag{2}
\]

with `M asymp J` near-one zeros in the Ford transition layer and carrier-locked ordinates

\[
\gamma_j=t+\frac{2\pi qj+\vartheta}{X},
\qquad
1\le j\le M,
\qquad q\in\mathbb N\text{ fixed}.
\tag{3}
\]

The line's Ford smoothing scale satisfies `J=R/H_F`, so the full dangerous packet lies in a vertical window of width

\[
W_F\asymp \frac{J}{R}=\frac1{H_F}=o(1).
\tag{4}
\]

Wang's Theorem 2.2 instead fixes `0<lambda<theta<1`, takes a fixed real even

\[
g\in C_c^\infty(\mathbb R),
\qquad
\operatorname{supp}g\subset[-\lambda,\lambda],
\]

and studies, for `I=(T,T+T^theta]`, the complex-zero pair statistic

\[
\mathcal P_I(g)
:=
\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(
\frac{i(\rho-\rho')Q}{2\pi}
\right)
 w(\rho-\rho'),
\qquad
w(z)=\frac4{4-z^2}.
\tag{5}
\]

The theorem gives

\[
\mathcal P_I(g)
=
\frac{T^\theta Q}{2\pi}
\left(
 g(0)+\int_{\mathbb R}|\alpha|g(\alpha)\,d\alpha
\right)
+
O_g\!\left(T^\theta+T^\lambda Q^2\right).
\tag{6}
\]

This is a real strengthening of the available pair-correlation literature in the height variable: the zero sum is restricted to a power-length interval instead of a global range. The question here is narrower: does (6), as stated, resolve an `NB-231` packet inside the Ford transition?

## 2. A stability lemma for the short-interval complex pair statistic

The answer is no already at the level of the theorem's error term.

Let `Z` be a zero multiset in `I` satisfying the standard unit-interval bound

\[
\#\{\rho\in Z:u<\Im\rho\le u+1\}\ll Q
\tag{7}
\]

throughout the height range `u asymp T`. Let `E` be any additional multiset of `A` points

\[
\rho=\beta+i\gamma,
\qquad
0<\beta<1,
\qquad
\gamma\in I.
\tag{8}
\]

No spacing or phase assumption on `E` is needed for the following estimate.

Because `g` is supported in `[-lambda,lambda]`, its entire Fourier transform obeys the elementary Paley-Wiener bound

\[
\left|
\widehat g(a+ib)
\right|
\le
\|g\|_1 e^{2\pi\lambda|b|}.
\tag{9}
\]

For

\[
u=
\frac{i(\rho-\rho')Q}{2\pi},
\]

we have

\[
|\Im u|
=
\frac{|\beta-\beta'|Q}{2\pi}
<
\frac Q{2\pi},
\]

and therefore

\[
\left|
\widehat g\!\left(
\frac{i(\rho-\rho')Q}{2\pi}
\right)
\right|
\ll_g T^\lambda.
\tag{10}
\]

At the same time, if `z=(beta-beta')+i(gamma-gamma')`, then `|beta-beta'|<1` and

\[
\Re(4-z^2)
=
4-(\beta-\beta')^2+(\gamma-\gamma')^2
\ge
3+(\gamma-\gamma')^2.
\]

Hence

\[
|w(\rho-\rho')|
\le
\frac4{3+(\gamma-\gamma')^2}.
\tag{11}
\]

For one inserted point, split the original ordinates into unit shells. From (7) and (11),

\[
\sum_{\rho'\in Z}
|w(\rho-\rho')|
\ll Q.
\tag{12}
\]

Equations (10)--(12) imply that all old--new pairs contribute at most

\[
O_g(A T^\lambda Q).
\tag{13}
\]

The new--new pairs contribute at most

\[
O_g(A^2T^\lambda).
\tag{14}
\]

Thus the complete statistic satisfies the stability estimate

\[
\boxed{
\left|
\mathcal P_{I,Z\cup E}(g)
-
\mathcal P_{I,Z}(g)
\right|
\ll_g
T^\lambda(AQ+A^2).
}
\tag{15}
\]

The same estimate survives closure under the zeta symmetries `rho -> 1-rho`, conjugation and multiplicity, because these operations change `A` by only a fixed factor. In particular, the potentially large horizontal amplification of a near-one zero paired with its reflected near-zero partner has already been paid for by the factor `T^lambda` in (15).

Now take the `NB-231` packet. Including all symmetry partners still gives

\[
A=O(J)=O(\ell)=o(Q).
\tag{16}
\]

Therefore

\[
T^\lambda(AQ+A^2)
=
o(T^\lambda Q^2).
\tag{17}
\]

Since `lambda<theta`, it is also `o(T^theta)`. Consequently, adding a full transition-saturating Ford packet changes the left side of Wang's pair-correlation formula by **strictly less than the resolution already allowed by its published error term**.

This is a statement about the information content of the theorem (6), not about modifying the actual zero set of zeta. The matched insertion is an adversarial control: two zero multisets can differ by the dangerous Ford packet while remaining indistinguishable at the precision of (6). Any argument importing only that asymptotic therefore cannot exclude the packet.

## 3. Fixed mean-spacing kernels erase the carrier coherence itself

The error-budget argument above is enough to rule out a direct use of the published short-interval theorem. The same-depth core of the `NB-231` packet reveals a more structural mismatch.

Take

\[
\rho_j=\beta_*+i\gamma_j
\]

with a common Ford depth and ordinates (3). For `j neq k`,

\[
\frac{i(\rho_j-\rho_k)Q}{2\pi}
=
-q(j-k)\frac QX
\in\mathbb R.
\tag{18}
\]

Because `g in C_c^infty`, its Fourier transform is Schwartz on the real axis. Hence for every fixed `B>1`,

\[
|\widehat g(u)|
\ll_{B,g}(1+|u|)^{-B}.
\tag{19}
\]

Using `|w|<=4/3` and summing by the difference `m=|j-k|`,

\[
\begin{aligned}
\sum_{j\ne k}
\left|
\widehat g\!\left(
\frac{i(\rho_j-\rho_k)Q}{2\pi}
\right)
 w(\rho_j-\rho_k)
\right|
&\ll_{B,g}
M\sum_{m\ge1}
\left(1+mq\frac QX\right)^{-B} \\
&\ll_{B,g,q}
M\left(\frac XQ\right)^B.
\end{aligned}
\tag{20}
\]

But

\[
\frac XQ
\asymp
Q^{-1/3}\ell^{1/3}	o0,
\qquad
M\ll\ell.
\tag{21}
\]

Taking, for example, `B=2` gives

\[
\boxed{
\sum_{j\ne k}
\widehat g\!\left(
\frac{i(\rho_j-\rho_k)Q}{2\pi}
\right)
 w(\rho_j-\rho_k)
=o(1).
}
\tag{22}
\]

Thus the packet's own contribution to the fixed-test pair statistic is

\[
\boxed{
M\widehat g(0)+o(1).
}
\tag{23}
\]

The leading term is purely diagonal. It remembers how many packet points there are, but it has forgotten the fact that their phases satisfy

\[
e^{iX(\gamma_j-t)}=e^{i\vartheta}
\]

for every `j`.

This makes the scale mismatch exact. Standard pair correlation normalizes ordinate differences by `Q=log T`, so a fixed test is sensitive to gaps of order `1/Q`. The Ford packet uses gaps of order `1/X asymp 1/R`, and

\[
\frac{1/R}{1/Q}
\asymp
\frac QR
\to\infty.
\tag{24}
\]

The carrier packet is not a close-spacing anomaly. It is a sparse **mesoscopic lattice**, and the fixed Montgomery kernel suppresses its off-diagonal lattice correlations before any averaging over the height interval is considered.

## 4. Shorter height intervals alone cannot repair the mismatch

Wang's theorem localizes the height variable to

\[
|I|=T^\theta,
\tag{25}
\]

whereas the exact Ford coefficient selects a window of width

\[
W_F\asymp\frac JR=o(1).
\tag{26}
\]

The ratio

\[
\frac{T^\theta}{W_F}
\asymp
T^\theta\frac RJ
\to\infty
\tag{27}
\]

shows that the published theorem is still enormously coarser in absolute height than the required deterministic window. However, (22) says something stronger than this obvious comparison: **even a hypothetical improvement that localized the same fixed test all the way down to the Ford window would still erase the packet's off-diagonal carrier coherence.**

To keep the packet separation visible in a Montgomery framework, the test must itself move with `T`. In the usual Fourier parameter `alpha`, carrier phase corresponds to

\[
T^{i\alpha(\gamma-\gamma')}
=
e^{iX(\gamma-\gamma')}
\quad\Longleftrightarrow\quad
\alpha\asymp\frac XQ
\asymp\frac RQ\to0.
\tag{28}
\]

Equivalently, an integrated test `g=g_T` would need to narrow on the `alpha` scale `X/Q` so that its transform does not decay at the large normalized gap `Q/X`. Wang's theorem is stated for **fixed** `g`, with constants depending on `g`; it supplies no uniform estimate for such a shrinking test family.

And retuning the vertical pair scale is still not sufficient by itself. The Ford obstruction uses only zeros in the shallow transition layer

\[
X(1-\beta)-\log J=O(1),
\tag{29}
\]

whereas the standard pair statistic sums over the entire critical strip. `NB-232` already showed why population averaged over all zeros can miss an exceptional near-one packet. The viable two-point target therefore needs all three coordinates at once:

\[
\boxed{
\text{selected height window}
\;+
\text{Ford depth}
\;+
\text{carrier-scale phase}.
}
\tag{30}
\]

This is precisely the information retained by the `R^{-1} zeta'/zeta` edge current isolated in `NB-237`.

## 5. Prior-art audit and novelty boundary

The closest fresh theorem is Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*, arXiv:2609.07918 (submitted 7 September 2026). Its Theorem 2.2 proves (6) for fixed `0<lambda<theta<1` and fixed smooth `g`, extending the unconditional Montgomery framework of Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh to intervals of length `T^theta`. This is exactly the natural candidate to test after the global obstruction in `NB-232`.

No novelty is claimed for the elementary facts used in the audit: Riemann--von Mangoldt gives (7), compact Fourier support gives the exponential-type bound (9), and `C_c^infty` gives Schwartz decay on the real axis. The line-local contribution is the scale coupling: applying those standard facts to the exact `NB-231` Ford packet yields both the theorem-level stability bound (15)--(17) and the carrier-kernel annihilation (22).

A targeted search also found classical and modern work on mesoscopic zero statistics, including Brad Rodgers' mesoscopic central-limit results, but those concern different observables and do not supply a deterministic, near-one-depth-conditioned pair estimate at the carrier mode. The recent Najnudel--Nikeghbali Stieltjes-transform result already noted in `NB-237` is likewise random-height/critical-line in nature rather than a uniform Ford-depth estimate. No external theorem beyond Wang's displayed statistic is load-bearing for the exact bounds above, so this audit does not require a new durable `SOURCES.md` dependency.

## 6. Adversarial review and falsification boundary

Several limits are essential.

First, (15) is a stability statement for the **conclusion** of the short-interval pair theorem. An artificially inserted packet need not satisfy the exact zeta explicit formula from which Wang derives that theorem. The point is narrower: the theorem at its stated precision cannot be the input that rules the packet out.

Second, the sharp kernel annihilation (22) uses the same-depth matched packet of `NB-231`, so the Fourier argument is real. If depths vary, the pair-kernel argument acquires a complex displacement and the Paley-Wiener growth in (10) becomes relevant instead; the general stability bound (15) is the statement that survives arbitrary horizontal positions in the critical strip.

Third, this finding does not rule out a `T`-dependent Montgomery test with quantitative constants uniform under shrinking support, nor a pointwise mesoscopic form-factor theorem at `alpha asymp X/Q`. Such a result would be genuinely different from the fixed-test theorem audited here. It would still have to preserve the Ford-depth mark and deterministic height localization to address the current source coefficient.

Fourth, as throughout `NB-231`--`NB-239`, the matched packet is an adversarial spectral control, not a claim that the actual zeros of zeta realize this geometry. The result only identifies which currently available information is logically insufficient to exclude it.

A decisive falsification of the method boundary would therefore be a theorem that controls, uniformly in the selected height `t`, a depth-conditioned pair/current statistic with vertical test scale `X/Q` (or directly the carrier phase `X(gamma-t)`) in the Ford window. The first-order formulation of `NB-237` remains the more direct equivalent target.

## Conclusion

The newest short-interval Montgomery theorem improves the **height averaging**, but it does not improve the two scales that matter to the Ford packet. A complete `O(log log T)` transition-saturating packet lies below the theorem's stated error budget, including its reflected off-line partners. More structurally, a fixed mean-spacing pair kernel sees the same-depth packet only through its diagonal term and suppresses all carrier-locked off-diagonal pairs by `o(1)`.

So the surviving frontier is sharper than “local pair correlation.” The needed input must be **local in height, conditioned in Ford depth, and retuned from the mean-zero scale `1/log T` to the carrier scale `1/R`**. Without all three, the `NB-231` coherent packet remains invisible.