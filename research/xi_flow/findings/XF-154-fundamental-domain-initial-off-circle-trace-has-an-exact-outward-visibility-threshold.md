---
type: partial-positive
research_line: xi_flow
finding_id: XF-154
status: canonical
---

# XF-154 — fundamental-domain initial off-circle trace has an exact outward visibility threshold

## Statement

For the maximal-contact matched pair used in XF-145--XF-151, the initial complexified physical trace has an exact one-sided visibility threshold once the physical antipodal-distance domain is stated explicitly.

Write

\[
\Delta R(z,0)=R_1(z,0)-R_{\lambda_\rho}(z,0),
\]

so that, up to a unit phase/sign,

\[
\Delta R(z,0)
=
2(1-\lambda_\rho)e^{-iN\pi z/L}
\sin^{N-2}\!\left(\frac{\pi z}{L}\right).
\]

Observe at the outward complex point

\[
z=\frac L2-d+ih,
\qquad
0\le d\le\frac L2,
\qquad h\ge0,
\]

and set

\[
D=\frac{\pi d}{L}\in\left[0,\frac\pi2\right],
\qquad
H=\frac{\pi h}{L}\ge0.
\]

Then the normalized initial separation is exactly

\[
\boxed{
\mathcal A_N(H,D)
:=
\frac{|\Delta R(L/2-d+ih,0)|}{2(1-\lambda_\rho)}
=
e^{NH}
\left(\cos^2D+\sinh^2H\right)^{(N-2)/2}.
}
\tag{1}
\]

Its large-`N` exponential rate is

\[
\boxed{
F_+(H,D)
=
H+\frac12\log\!\left(\cos^2D+\sinh^2H\right).
}
\tag{2}
\]

For every physical distance

\[
0<D\le\frac\pi2,
\]

`F_+(H,D)` is strictly increasing for `H>0`, starts below zero (with the extended value `-infinity` at `D=pi/2`), tends to `+infinity`, and therefore has a unique positive zero

\[
\boxed{
H_*(D)
=
\frac12\log\!\left(
\sqrt{3+\cos^2(2D)}-\cos(2D)
\right).
}
\tag{3}
\]

At the antipodal endpoint `D=0`, the same formula gives

\[
\boxed{H_*(0)=0.}
\tag{4}
\]

Consequently, for every fixed `D` in `(0,pi/2]`, the matched pair is exponentially hidden at the initial slice when `0<=H<H_*(D)` and is exponentially amplified when `H>H_*(D)`. At the real-center endpoint `D=pi/2`,

\[
H_*\!\left(\frac\pi2\right)=\frac12\log3,
\qquad
h_* = \frac{L}{2\pi}\log3.
\tag{5}
\]

Near the antipodal point,

\[
H_*(D)
=
\frac{D^2}{2}-\frac{D^4}{24}+O(D^6),
\]

so in physical coordinates

\[
\boxed{
h_*(d)
=
\frac{\pi}{2}\frac{d^2}{L}
-
\frac{\pi^3}{24}\frac{d^4}{L^3}
+
O\!\left(\frac{d^6}{L^5}\right).
}
\tag{6}
\]

Thus the parabolic complex-reach scale found in XF-151 is sharp for the initial outward trace, with leading physical constant `pi/2`, on the entire fundamental real-distance domain.

## Derivation

The initial-slice identity underlying XF-145 gives

\[
|\Delta R(x,0)|
=
2(1-\lambda_\rho)
\left|\sin\frac{\pi x}{L}\right|^{N-2}.
\]

Its entire continuation has carrier `e^{-iN pi z/L}`. For `z=L/2-d+ih`,

\[
|e^{-iN\pi z/L}|=e^{NH}
\]

and

\[
\left|\sin\!\left(\frac{\pi z}{L}\right)\right|^2
=
\cos^2D+\sinh^2H,
\]

which proves `(1)` and `(2)`.

For `0<D<pi/2`,

\[
F_+(0,D)=\log(\cos D)<0.
\]

At `D=pi/2`, `F_+(0,D)=-infinity` in the extended sense. For every `H>0`,

\[
\partial_HF_+(H,D)
=
1+
\frac{\sinh H\cosh H}
{\cos^2D+\sinh^2H}>0,
\tag{7}
\]

and `F_+(H,D)->+infinity` as `H->infinity`. Hence there is exactly one positive zero for each `0<D<=pi/2`. When `D=0`, `F_+(0,0)=0`, so the threshold is the endpoint `H_*=0` rather than a positive root.

To solve the threshold equation for `D>0`, exponentiate `F_+=0`, square, and write `y=e^{2H}`. This gives

\[
y^2+2\cos(2D)y-3=0.
\]

The positive solution is

\[
y_*(D)=\sqrt{3+\cos^2(2D)}-\cos(2D),
\]

which proves `(3)` and also extends continuously to `(4)`.

Finally, if `D->0` and `H=alpha D^2`, then

\[
F_+(H,D)
=
\left(\alpha-\frac12\right)D^2+O(D^4).
\tag{8}
\]

Therefore, whenever `ND^2->infinity`, the normalized initial separation is exponentially small on the `ND^2` scale for fixed `alpha<1/2` and exponentially large for fixed `alpha>1/2`.

## One-sidedness on the same physical domain

For completeness, the inward continuation `z=L/2-d-ih` has rate

\[
F_-(H,D)
=
-H+\frac12\log\!\left(\cos^2D+\sinh^2H\right).
\tag{9}
\]

The corresponding threshold equation is

\[
3y^2-2\cos(2D)y-1=0,
\qquad y=e^{2H},
\]

with positive root

\[
y=
\frac{\cos(2D)+\sqrt{\cos^2(2D)+3}}{3}
\le1
\]

for `0<=D<=pi/2`, equality occurring only at `D=0`. Hence there is no inward solution with `H>0` anywhere on the physical fundamental domain. At `D=0`,

\[
F_-(H,0)=-H+\log\cosh H<0
\]

for every finite `H>0`.

The orientation therefore matters: outward continuation can cross an exact visibility threshold, whereas inward continuation cannot do so at positive finite depth for this initial matched pair.

## Consequences for the frontier

XF-151 established from an analytic-jet bound that shallow off-circle access cannot beat the real antipodal obstruction before parabolic depth `h` of order `d^2/L`. The exact initial law above shows that this scale is intrinsic to the maximal-contact packet rather than an artifact of that upper bound, and fixes the leading outward constant to `pi/2` near the antipode.

The statement is deliberately restricted to the physical distance parametrization `0<=d<=L/2`, equivalently `0<=D<=pi/2`. Extending the coordinate `D` beyond that interval repeats physical points and invalidates the simple claim that the rate starts below zero for every positive `D`; that over-broad formulation is not part of this finding.

XF-153 independently proves that in the smaller near-antipodal sector `0<=D<=pi/4`, optimizing over all positive heat times changes the signal by at most a factor two. Together, XF-153 and this corrected initial-slice theorem show that positive heat cannot lower the `pi/2` parabolic reach constant in the regime relevant to the antipodal barrier.

## Falsification boundary

This finding concerns only the canonical maximal-contact matched pair. It does not prove stable recovery of `Lambda_per` at or above `H_*(D)`, and it does not establish that the actual Xi source can realize the matched packet. Above threshold this particular initial witness merely stops certifying exponential blindness.

The exact threshold claim is for the fundamental physical domain `0<=D<=pi/2`. At `D=0` the threshold is zero; uniqueness of a **positive** root is asserted only for `0<D<=pi/2`.

## Prior-art audit

A directed audit checked current work on complex-rooted polynomial powers under holomorphic heat flow and the broader de Bruijn--Newman heat-flow setting. Recent work studies the evolving zero distribution of high polynomial powers, including complex zeros, but does not supply the matched-transition initial-trace identity `(1)` or the elementary threshold equation `(3)`. The present derivation is self-contained and uses no external theorem beyond the exact packet identities already established in this research line, so no source entry is required.

## Next gate

The near-antipodal all-future threshold is already controlled by XF-153. The higher-value target-side question is whether an exact all-future threshold can be obtained on the remaining sector `pi/4<D<=pi/2`, where the one-Lipschitz argument used in XF-153 fails. The higher-value source-side alternative remains to derive a source-faithful obstruction showing that Xi cannot realize the maximal-contact matched direction, or to exhibit Xi-specific information that necessarily reaches beyond it.