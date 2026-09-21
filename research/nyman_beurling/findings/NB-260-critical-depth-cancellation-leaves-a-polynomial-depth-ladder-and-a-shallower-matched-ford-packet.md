# NB-260 — Critical-depth cancellation leaves a polynomial depth ladder and a shallower matched Ford packet

> **Representation:** _Nyman–Beurling / Hardy-projected vantage._ The line-specific data are the exact Euler normalization, the `H`-resolved signed carrier dictionary, the shell-Hilbert/`ell^2` identification of `NB-257`, and the legal complex zero evaluation of `NB-259`. The generic engine is derivative compactness for short exponential sums after rescaling the imaginary Ford coordinate. This is a destination-side method boundary: a bounded-cost carrier can notch one critical-depth Ford cell cheaply, but at every fixed-power channel scale below the effective depth resolution it cannot suppress a whole proportional ladder of Ford depths; at the `NB-259` crossover the carrier is asymptotically affine in depth and a shallower Bellotti-compatible matched packet restores order-one residue mass.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + HARDY-PROJECTED-ZERO-EVALUATION + H-SEPARATED-SIGNED-CARRIER + DEPTH-LADDER-RIGIDITY + POLYNOMIAL-COMPACTNESS + CRITICAL-NOTCH-AFFINE-LIMIT + SHALLOW-REPLACEMENT-PACKET + MATCHED-CONTROL + NB-259-REFINEMENT + DESTINATION-INTERFACE + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-259` shows that the legal zero mark samples the resolved carrier not on the real Ford axis but at imaginary height

\[
A_J:=\frac{\log J}{Y},
\qquad Y:=\frac XR\asymp1,
\]

and that an exact notch at `iA_J` has bounded shell-Hilbert cost already at

\[
K\asymp\left(\frac{J}{A_J}\right)^{2/3}
\asymp\left(\frac{J}{\log J}\right)^{2/3}.
\]

That cheap notch is genuinely useful locally, but it does not suppress the depth ladder below it. Put

\[
N_J:=\frac{J}{A_J}\asymp\frac{J}{\log J}
\]

and rescale the whole imaginary segment from the Euler anchor to the critical layer by

\[
D_J(s):=C_J(i sA_J),
\qquad 0\le s\le1,
\]

where

\[
C_J(w)=\sum_j c_j e^{ijw/J},
\qquad C_J(0)=1.
\]

If the physical shell-Hilbert cost is bounded and

\[
K\le N_J^{1-\delta}
\qquad(\delta>0\text{ fixed}),
\]

then some fixed derivative of `D_J` tends uniformly to zero. Consequently `D_J` is uniformly `o(1)`-close on `[0,1]` to a polynomial of fixed degree whose value at zero is one. Finite-dimensional coercivity then gives, for every fixed interval `I\subset(0,1]` of positive length,

\[
\boxed{
\liminf_{J\to\infty}\int_I |C_J(isA_J)|^2\,ds>0.
}
\]

Thus suppression of an entire proportional depth ladder at bounded Hilbert cost forces the channel count out of every fixed-power regime:

\[
\boxed{
K\ge N_J^{1-o(1)}
=\left(\frac{J}{\log J}\right)^{1-o(1)}
}
\]

as a necessary scale for this scalar resolved architecture.

At the exact `NB-259` crossover the statement is sharper. Any bounded-cost exact critical-notch family with

\[
K\asymp N_J^{2/3},
\qquad C_J(0)=1,
\qquad C_J(iA_J)=0,
\]

is asymptotically affine in the normalized depth variable:

\[
\boxed{
C_J(isA_J)=1-s+o(1)
}
\]

uniformly for `0\le s\le1`. The critical notch therefore exports, rather than removes, the carrier: every fixed shallower fraction `s=\theta<1` retains order-one amplitude.

Moreover this is not only a one-point observation. For every fixed

\[
0<\theta<\frac16,
\]

the same bounded-cost exact-notch family is uniformly affine on the horizontal range needed by a `\Theta(J^\theta)` carrier-locked packet at depth `X(1-\beta)=\theta\log J`. The packet is compatible with the same zero-free, Bellotti local-count, growing-density, and ordinary zero-count information used in `NB-231`, and its full signed Hardy-projected residue contribution stays bounded away from zero. Hence the cheap critical-depth notch of `NB-259` cannot by itself defeat the existing matched-control obstruction: it pushes an order-one compatible packet to a shallower Ford layer.

## 1. Rescale the legal imaginary zero coordinate

Retain the resolved dictionary and normalization of `NB-257`--`NB-259`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR,
\qquad
J:=\frac RH\to\infty,
\]

with `Y` in a fixed compact subinterval of `(0,\infty)`. Fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\operatorname{diam}(\operatorname{supp}\phi)<1.
\]

For odd `K=2m+1`, use the disjoint `H`-grid

\[
\xi_j=jH,
\qquad -m\le j\le m,
\]

and an Euler-normalized coefficient measure

\[
\lambda=\sum_{j=-m}^m c_j\delta_{\xi_j},
\qquad
\sum_jc_j=1.
\]

As in `NB-257`, the physical coefficients satisfy

\[
d\nu(\xi)=e^{r\xi/X}\,d\lambda(\xi).
\]

Because the translated shells are disjoint,

\[
H\|h_\nu\|_2^2
=\|\phi\|_2^2
\sum_j e^{2r\xi_j/X}|c_j|^2.
\]

Whenever `K=o(J)`, the carrier span is `o(X)` and the Euler tilt in this identity is `1+o(1)`. Hence a uniform physical bound

\[
H^{1/2}\|h_\nu\|_2\le M
\]

implies

\[
\boxed{\|c\|_2\le C_M.}
\]

Define

\[
B_\lambda(z):=\sum_jc_je^{i\xi_jz},
\qquad
C_J(w):=B_\lambda(w/R)
=\sum_jc_je^{ijw/J}.
\]

The Euler normalization gives `C_J(0)=1`. For a zero `\rho=\beta+i\gamma`, `NB-255` and `NB-259` identify the exact extra signed carrier in the Hardy-projected zero mark as

\[
C_J\!\left(R(\gamma-t_0)+iR(1-\beta)\right).
\]

The critical Ford layer `X(1-\beta)=\log J+O(1)` therefore lies at

\[
R(1-\beta)
=\frac{\log J+O(1)}Y
=A_J+O(1),
\qquad
A_J:=\frac{\log J}{Y}.
\]

Introduce the effective depth resolution

\[
\boxed{
N_J:=\frac{J}{A_J}
=\frac{YJ}{\log J}.
}
\]

The imaginary segment `0\le\operatorname{Im}w\le A_J` is the natural ladder joining the Euler anchor to the critical zero layer. Rescale it to unit length:

\[
\boxed{
D_J(s):=C_J(isA_J)
=\sum_jc_j e^{-js/N_J},
\qquad 0\le s\le1.
}
\]

Thus the relevant small parameter is no longer `K/J`, as on the real Ford axis, but

\[
\frac K{N_J}=\frac{KA_J}{J}.
\]

This is exactly the logarithmic gain that made the single `NB-259` notch cheaper.

## 2. Fixed-power depth dictionaries collapse to finite-degree polynomials

For every integer `q\ge1`, differentiation gives

\[
D_J^{(q)}(s)
=\sum_jc_j\left(-\frac j{N_J}\right)^q e^{-js/N_J}.
\]

Assume

\[
K\le N_J^{1-\delta}
\qquad(\delta>0\text{ fixed}).
\]

Then `K/N_J\to0`, so the exponential weights are uniformly bounded by `1+o(1)` for `0\le s\le1`. Cauchy--Schwarz, the coefficient bound, and

\[
\sum_{|j|\le m}|j|^{2q}\ll_q K^{2q+1}
\]

give

\[
\boxed{
\|D_J^{(q)}\|_{L^\infty(0,1)}
\ll_{q,M}
\frac{K^{q+1/2}}{N_J^q}.
}
\]

Using the fixed-power hypothesis,

\[
\frac{K^{q+1/2}}{N_J^q}
\le
N_J^{(1-\delta)/2-\delta q}.
\]

Choose a fixed integer

\[
q>\frac{1-\delta}{2\delta}.
\]

Then

\[
\boxed{
\|D_J^{(q)}\|_\infty=o(1).
}
\]

Let `P_J` be the Taylor polynomial of `D_J` at zero of degree `q-1`. Taylor's theorem yields

\[
\boxed{
\|D_J-P_J\|_{L^\infty(0,1)}=o(1),
\qquad
P_J(0)=D_J(0)=1.
}
\]

Now fix any closed interval `I\subset(0,1]` of positive length. On the finite-dimensional space of polynomials of degree at most `q-1`, evaluation at zero is a continuous functional for the `L^2(I)` norm. Hence there is a constant `\kappa_{I,q}>0` such that

\[
\int_I|P(s)|^2ds\ge\kappa_{I,q}|P(0)|^2
\]

for every such polynomial. Applying this to `P_J` gives

\[
\boxed{
\liminf_{J\to\infty}
\int_I|D_J(s)|^2ds
\ge\kappa_{I,q}>0.
}
\]

In the original zero coordinate this is

\[
\boxed{
\liminf_{J\to\infty}
\int_I
\left|
B_\lambda\!\left(i\frac{s\log J}{X}\right)
\right|^2ds
>0.
}
\]

Therefore a bounded-cost resolved scalar carrier cannot be small throughout any fixed positive fraction of the depth ladder while `K\le N_J^{1-\delta}`.

Equivalently, if a family satisfies

\[
\int_I|D_J(s)|^2ds\to0
\]

for one fixed interval `I` of positive length, then it cannot obey `K\le N_J^{1-\delta}` for any fixed `\delta>0`. A necessary channel-count scale is therefore

\[
\boxed{
K\ge N_J^{1-o(1)}
=\left(\frac{J}{\log J}\right)^{1-o(1)}.
}
\]

This is the depth-ladder analogue of `NB-258`, but it is stated on the legally sampled complex zero geometry rather than on the unprojected real Ford axis.

## 3. At the `NB-259` crossover the entire depth profile is affine

The first nontrivial case is exactly the cheap critical notch found in `NB-259`. Suppose the carrier is at the bounded-cost two-point crossover

\[
K\asymp N_J^{2/3}.
\]

The derivative estimate with `q=2` gives

\[
\|D_J''\|_\infty
\ll
\frac{K^{5/2}}{N_J^2}
=O(N_J^{-1/3})
=o(1).
\]

Assume that the carrier imposes the exact critical-depth notch

\[
D_J(1)=C_J(iA_J)=0.
\]

Since `D_J(0)=1`, Taylor's theorem gives

\[
0=1+D_J'(0)+o(1),
\qquad
D_J'(0)=-1+o(1).
\]

A second Taylor expansion then yields uniformly for `0\le s\le1`,

\[
\boxed{
D_J(s)=1-s+o(1).
}
\]

Thus the logarithmic imaginary displacement that makes the endpoint notch cheap also fixes its leading geometry: **the notch is a ramp through the depth ladder**. It kills `s=1`, but for every fixed `0<\theta<1`,

\[
\boxed{
C_J(i\theta A_J)=1-\theta+o(1).
}
\]

No additional coefficient optimization at the same bounded-cost `K\asymp N_J^{2/3}` scale can turn the `NB-259` endpoint cancellation into uniform suppression of a macroscopic depth fraction. The affine limit follows only from bounded Hilbert cost, the resolved dictionary, and the two endpoint constraints; it is not special to the minimum-norm coefficient vector constructed in `NB-259`.

## 4. The affine ramp supports an explicit shallower matched packet

The affine depth profile is already a destination-side obstruction, but the current Ford route is controlled by sums over zeros rather than by one carrier value. We therefore test whether the ramp can support the same kind of admissible spectral control used in `NB-231`.

Fix

\[
0<\theta<\frac16
\]

and retain the conservative population regime

\[
1\ll J\le L:=\log Q.
\]

Put the packet at the shallower horizontal depth

\[
\boxed{
X(1-\beta)=\theta\log J,
\qquad
R(1-\beta)=\theta A_J.
}
\]

Take

\[
M:=\lfloor\delta J^\theta\rfloor
\]

for a fixed small `\delta>0`, and choose carrier-locked ordinates

\[
\gamma_n
=t_0+\frac{2\pi qn}{X},
\qquad 1\le n\le M,
\]

with the same fixed spacing integer `q` used in the `NB-231` population audit. Then

\[
e^{iX(\gamma_n-t_0)}=1
\]

and the Ford real coordinates are

\[
x_n:=R(\gamma_n-t_0)
=\frac{2\pi qn}{Y}
=O(J^\theta).
\]

To extend the affine approximation from the vertical axis to this packet, differentiate `C_J` twice. On the strip `0\le\operatorname{Im}w\le A_J`, the coefficient bound, `K\asymp N_J^{2/3}`, and `K A_J/J=o(1)` give

\[
\sup_w |C_J''(w)|
\ll
\frac{K^{5/2}}{J^2}
\ll
J^{-1/3}A_J^{-5/3}.
\]

The endpoint condition `C_J(iA_J)=0` therefore implies

\[
C_J'(0)
=\frac{i}{A_J}
+O\!\left(A_J\sup|C_J''|\right).
\]

For

\[
w_n:=x_n+i\theta A_J,
\]

Taylor's theorem gives

\[
C_J(w_n)
=1+\frac{i w_n}{A_J}
+O\!\left(
|w_n|A_J\sup|C_J''|
+|w_n|^2\sup|C_J''|
\right).
\]

Because `x_n=O(J^\theta)`, the error is

\[
O\!\left(
J^{2\theta-1/3}A_J^{-5/3}
+J^{\theta-1/3}A_J^{-2/3}
+J^{-1/3}A_J^{1/3}
\right)
=o(1)
\]

uniformly in `n` for every fixed `\theta<1/6`. Hence

\[
\boxed{
C_J(w_n)
=1-\theta+i\frac{x_n}{A_J}+o(1),
\qquad
\Re C_J(w_n)=1-\theta+o(1)>0.
}
\]

The exact smooth-shell profile is simultaneously flat across the packet. Indeed

\[
H(\gamma_n-t_0)=\frac{x_n}{J}=O(J^{\theta-1})=o(1),
\]

while

\[
H(\sigma_X-\beta)
=O\!\left(\frac{A_J}{J}\right)=o(1).
\]

Therefore

\[
F\!\left(H(\gamma_n-t_0)+iH(\sigma_X-\beta)\right)
=F(0)+o(1)
\]

uniformly. Although `|C_J(w_n)|` may grow like `|x_n|/A_J`, multiplying that growth by the profile error still gives `o(1)` because `\theta<1/6<1/2`. Consequently

\[
\Re\!\left\{
F\!\left(H(\gamma_n-t_0)+iH(\sigma_X-\beta)\right)
C_J(w_n)
\right\}
=F(0)(1-\theta)+o(1).
\]

At this depth the exact Ford damping is

\[
e^{-X(1-\beta)}=J^{-\theta}.
\]

For the Euler-normalized mixture, `NB-255` gives the exact zero transform factorization

\[
L_\nu(v_\rho)
=e^{iXv_\rho}F(Hv_\rho)B_\lambda(z_\rho),
\]

with `B_\lambda(z_\rho)=C_J(w_\rho)` and

\[
e^{iXv_\rho}
=e^{iX(\gamma-t_0)}e^{-r}e^{-X(1-\beta)}.
\]

Using carrier locking, the positive real profile-times-carrier estimate, and `M\sim\delta J^\theta`, the packet contribution satisfies

\[
\boxed{
\liminf_{J\to\infty}
\Re\sum_{n=1}^M L_\nu(v_{\rho_n})
\ge
\delta e^{-r}F(0)(1-\theta)>0.
}
\]

Thus the critical-depth notch does not merely leave a formal carrier value behind. At bounded Hilbert cost it permits an explicit shallower `\Theta(J^\theta)` packet whose reduced population exactly compensates the weaker damping at depth `\theta\log J`.

## 5. The replacement packet obeys the existing zeta-information ledger

The packet above is an abstract matched control, not a claim about the actual zeta zero set. Its purpose is to test whether the currently imported zero-free and population information rules out the geometry left by the carrier.

It does not. First,

\[
R(1-\beta)=\frac{\theta\log J}{Y}\to\infty,
\]

so the packet eventually lies safely to the left of every fixed normalized Vinogradov--Korobov zero-free boundary.

Second, under `J\le L`,

\[
M=O(J^\theta)\le O(L^\theta)=o(L),
\]

which is strictly smaller than the `\Theta(J)` population already audited in `NB-231`. The growing near-one density allowance therefore has ample room for it, while fixed-depth density bounds do not apply because the normalized depth tends to infinity.

Third, the ordinate spacing remains

\[
\gamma_{n+1}-\gamma_n
=\frac{2\pi q}{X}\asymp\frac1R.
\]

Exactly as in `NB-231`, a Bellotti disk of normalized radius `K_0` intersects only `O(K_0)` consecutive packet points once the fixed `q` is chosen large enough for the local-count constant. Ordinary unit-interval zero counting is even looser because `M=o(L)=o(Q)`.

Thus every population input currently used by the Ford route permits the shallower packet. What fails is not a zero-count theorem but the hope that cancelling only the original `X(1-\beta)\sim\log J` layer removes the complete matched-control family.

## 6. Prior art, representation, and surviving frontier

The generic mechanism in Sections 2--3 is classical short-exponential-sum rigidity: bounded coefficient `ell^2` norm and a frequency span that is a fixed power below the reciprocal observation scale force a finite-degree Taylor limit. Minimum-energy superoscillatory interpolation and its cost tradeoffs are well established; Ferreira--Kempf (IEEE Trans. Signal Processing 54 (2006), DOI `10.1109/TSP.2006.877642`) is a representative reference, and a fresh search also found Karmakar--Jordan, *Beyond Superoscillation: General Theory of Approximation with Bandlimited Functions*, arXiv:`2306.03963`, which studies finite-interval superoscillatory/supergrowing approximation and energy tradeoffs. Neither result is load-bearing here: the derivative bound, polynomial coercivity, and matched packet are derived directly.

A fresh targeted search across Nyman--Beurling/Hardy formulations, Mellin interpolation, and near-one zeta zero geometry did not locate the specific effective-depth scale `N_J=J/log J`, the polynomial depth-ladder obstruction, or the transfer from a critical-depth notch to a Bellotti-compatible shallower matched packet. This is a prior-art boundary, not a uniqueness claim. No new external theorem is required, so `SOURCES.md` does not acquire a new durable dependency.

The representation boundary is important. The depth-ladder lower bound is a statement about the scalar signed carrier evaluated on the legal Hardy-projected complex zero line; it is stronger than the real-axis source coercivity of `NB-258`, but it is still not a lower bound for the final Nyman distance. The explicit packet is likewise a compatibility control: it shows that the existing theorem package cannot exclude order-one residue mass after the critical notch, not that actual zeta zeros realize the packet.

The surviving scalar route is now narrower. A single critical cell is cheap because the logarithmic imaginary displacement reduces the interpolation price to `K\asymp N_J^{2/3}`. But suppressing a positive fraction of the whole depth ladder at bounded Hilbert cost requires leaving every fixed-power regime and reaching

\[
K\ge N_J^{1-o(1)}.
\]

Even that would still have to control the hard ordinate range `R(\gamma-t_0)=O(J)` simultaneously. The next non-circular calculation should therefore treat the **two-dimensional destination rectangle**: near-full effective depth rank together with the full `\Theta(J)` Ford ordinate width, rather than adding more isolated depth notches.

## 7. Adversarial audit

The strongest possible overclaim would be to read the necessary scale `K\ge N_J^{1-o(1)}` as a proof that a successful Nyman approximant needs `(J/log J)^{1-o(1)}` global terms. It does not. The conclusion is only for the specific `H`-resolved scalar signed carrier architecture with bounded shell-Hilbert cost and exact Euler normalization. A genuinely vector-valued construction, unresolved overlapping dictionary, or cancellation after a different legal Hardy operation lies outside the statement.

A second concern is that the depth-ladder `L^2` floor might be irrelevant because actual zeros occupy discrete depths. That is why Section 4 gives the separate matched control. At the concrete `NB-259` crossover, the endpoint notch forces an affine profile, and an explicit discrete shallower packet samples a region where the real part of the carrier remains positive. The packet uses fewer zeros as the layer becomes shallower, exactly compensating the stronger residue weight.

A third concern is the numerical exponent `1/6`. It is not claimed to be intrinsic. It comes from the uniform second-derivative control needed to keep the affine approximation valid across a packet whose horizontal Ford diameter is `\Theta(J^\theta)`. Improving the packet reach would require sharper structure of the interpolating coefficients or a higher-order two-dimensional argument. The substantive conclusion needs only one fixed positive `\theta`, so any `\theta<1/6` suffices.

Finally, the proof deliberately keeps the critical-cell cancellation and the final Nyman norm separate. `NB-259` correctly showed that real-axis coercivity can disappear after logarithmic imaginary translation; the present result does not reverse that correction. It shows instead that **one translated notch cannot be extrapolated into a depth-ladder suppression theorem at the same bounded-cost rank**.
