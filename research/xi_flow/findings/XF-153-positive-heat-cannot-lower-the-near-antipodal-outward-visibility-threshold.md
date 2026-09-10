---
type: partial-positive
research_line: xi_flow
finding_id: XF-153
status: canonical
---

# XF-153 — positive heat cannot lower the near-antipodal outward visibility threshold

## Statement

For the maximal-contact matched pair of XF-141--XF-152, positive heat time cannot improve the outward complex visibility exponent in the physical near-antipodal sector. Let

\[
N=2M,\qquad n=N-2,\qquad u=as,
\]

and observe the complexified physical trace at

\[
z=\frac L2-d+ih,
\qquad
D=\frac{\pi d}{L},
\qquad
H=\frac{\pi h}{L},
\]

with

\[
0\le D\le\frac\pi4,
\qquad H\ge0.
\]

For the fixed transition offset `rho>0`, write

\[
\Delta R(z,s)=R_1(z,s)-R_{\lambda_\rho}(z,s)
\]

and normalize away the common transition-retuning factor by

\[
\mathcal A_N(u;H,D)
:=
\frac{|\Delta R(z,s)|}{2(1-\lambda_\rho)}.
\]

Then the maximal-contact packet has the exact Gaussian representation

\[
\boxed{
\mathcal A_N(u;H,D)
=
e^{NH-N^2u/4}
\left|
\mathbb E\,
\cosh^n\!\left(
H+iD+\sqrt{\frac u2}\,Z
\right)
\right|,
}
\tag{1}
\]

where `Z` is standard Gaussian. At the initial slice,

\[
\boxed{
\mathcal A_N(0;H,D)
=
e^{NH}
\left(\sinh^2H+\cos^2D\right)^{n/2}.
}
\tag{2}
\]

For every future heat time `u>=0`,

\[
\boxed{
\mathcal A_N(u;H,D)
\le
2e^{-(N-1)u}\,
\mathcal A_N(0;H,D).
}
\tag{3}
\]

Consequently

\[
\boxed{
\mathcal A_N(0;H,D)
\le
\sup_{u\ge0}\mathcal A_N(u;H,D)
\le
2\mathcal A_N(0;H,D).
}
\tag{4}
\]

Thus, throughout the quarter-period near-antipodal sector, optimizing over the **entire future heat history changes the maximal-contact signal by at most a factor two** relative to the initial slice. In particular

\[
0\le
\log\sup_{u\ge0}\mathcal A_N(u;H,D)
-
\log\mathcal A_N(0;H,D)
\le\log2.
\tag{5}
\]

The all-future exponential rate is therefore exactly the initial-slice rate

\[
\boxed{
F_+(H,D)
=
H+\frac12\log\!\left(
\cos^2D+\sinh^2H
\right).
}
\tag{6}
\]

For every `0<D<=pi/4`, its unique positive zero is

\[
\boxed{
H_*(D)
=
\frac12\log\!\left(
\sqrt{3+\cos^2(2D)}-\cos(2D)
\right),
}
\tag{7}
\]

while at `D=0` the threshold collapses to `H_*(0)=0`. Hence positive heat time does **not** lower the outward visibility threshold near the antipode.

As `D->0`,

\[
H_*(D)
=
\frac{D^2}{2}-\frac{D^4}{24}+O(D^6),
\]

so the sharp all-future physical reach remains

\[
\boxed{
h_*(d)
=
\frac\pi2\frac{d^2}{L}
-
\frac{\pi^3}{24}\frac{d^4}{L^3}
+
O\!\left(\frac{d^6}{L^5}\right).
}
\tag{8}
\]

More uniformly, if `D_N->0`, `N D_N^2->infinity`, and `H_N=alpha D_N^2` for fixed `alpha`, then

\[
\log\sup_{u\ge0}\mathcal A_N(u;H_N,D_N)
=
\left(\alpha-\frac12+o(1)\right)ND_N^2.
\tag{9}
\]

Thus every fixed `alpha<1/2` leaves the full future exponentially blind on the `ND_N^2` scale, while `alpha>1/2` makes this particular matched-control obstruction disappear at exponential scale. This is a necessity/obstruction statement, not a stable-recovery theorem.

## Derivation

XF-150 gives the exact Fourier expansion of the maximal-contact packet,

\[
t_*\Delta Q(y,s)
=-2\sigma\,2^{-n}
\sum_{k=0}^{n}
(-1)^k\binom nk
 e^{(N-1-k)y}
 e^{-(N-1-k)(k+1)u},
\tag{10}
\]

with `|sigma|=1`. At the outward near-antipodal point,

\[
y=-\frac{2\pi iz}{L}
=2(H+iD)-i\pi.
\tag{11}
\]

Put

\[
m=N-1-k,
\qquad
\delta=m-\frac N2=\frac n2-k.
\]

Because `N` is even,

\[
(-1)^k e^{-i\pi m}=(-1)^{N-1}=-1,
\]

and

\[
m(N-m)=\frac{N^2}{4}-\delta^2.
\]

Therefore `(10)` becomes

\[
t_*\Delta Q
=2\sigma e^{N(H+iD)-N^2u/4}
2^{-n}
\sum_{k=0}^{n}
\binom nk
 e^{2\delta(H+iD)+u\delta^2}.
\tag{12}
\]

Use the Gaussian identity

\[
e^{u\delta^2}
=
\mathbb E e^{\sqrt{2u}\,\delta Z}.
\]

The centered binomial moment then closes exactly:

\[
2^{-n}\sum_{k=0}^{n}
\binom nk
 e^{\delta(2w+\sqrt{2u}Z)}
=
\cosh^n\!\left(w+\sqrt{\frac u2}Z\right),
\qquad
w=H+iD.
\tag{13}
\]

Combining `(12)` and `(13)`, and using

\[
\Delta R=(1-\lambda_\rho)t_*\Delta Q,
\]

gives `(1)`. Setting `u=0` and using

\[
|\cosh(H+iD)|^2
=
\sinh^2H+\cos^2D
\]

gives `(2)`.

The all-future estimate is controlled by a one-dimensional logarithmic geometry. Define for real `t`

\[
\phi_D(t)
:=
\log|\cosh(t+iD)|
=
\frac12\log\!\left(\sinh^2t+\cos^2D\right).
\tag{14}
\]

For `0<=D<=pi/4`,

\[
\phi_D'(t)
=
\frac{\sinh(2t)}{\cosh(2t)+\cos(2D)},
\]

so

\[
\boxed{|\phi_D'(t)|\le1\quad\text{for all real }t.}
\tag{15}
\]

Indeed `cos(2D)>=0`, and `|sinh(2t)|<=cosh(2t)`. Hence `phi_D` is globally one-Lipschitz and

\[
\phi_D\!\left(H+\sqrt{\frac u2}Z\right)
\le
\phi_D(H)+\sqrt{\frac u2}|Z|.
\tag{16}
\]

Taking absolute values only after the exact Gaussian reduction,

\[
\begin{aligned}
\mathcal A_N(u;H,D)
&\le
e^{NH-N^2u/4}
\mathbb E
\exp\!\left[n\phi_D\!\left(H+\sqrt{\frac u2}Z\right)\right]\\
&\le
e^{NH+n\phi_D(H)-N^2u/4}
\mathbb E e^{n\sqrt{u/2}|Z|}.
\end{aligned}
\tag{17}
\]

For a standard Gaussian and `t>=0`,

\[
\mathbb E e^{t|Z|}\le2e^{t^2/2}.
\tag{18}
\]

With `t=n sqrt(u/2)`, `(17)` gives

\[
\mathcal A_N(u;H,D)
\le
2e^{NH+n\phi_D(H)}
\exp\!\left[-\frac{N^2-n^2}{4}u\right].
\]

Since `n=N-2` and therefore `(N^2-n^2)/4=N-1`, this is exactly `(3)`. The lower bound in `(4)` is simply the admissible choice `u=0`.

Equation `(5)` now shows that heat-time optimization contributes only `O(1)` to the logarithm, uniformly in `N`, `H`, and `D` inside the stated sector. Equations `(6)`--`(9)` follow from the initial formula and the elementary threshold algebra already encoded by the maximal-contact packet.

## Consequences for the frontier

XF-151 showed that shallow complex continuation leaves a parabolic reach obstruction, and XF-152 identified the initial outward threshold. The present estimate closes the remaining **positive-time optimization loophole in the near-antipodal regime**: waiting for the packet to unfold cannot reduce the leading reach constant. The initial slice already controls the full-future visibility exponent, with an exact multiplicative loss of at most two in `(4)`.

This makes the target-side boundary substantially more rigid. Near the antipode the maximal-contact family cannot be defeated by combining a subcritical outward displacement with arbitrarily long future heat observation. To escape this matched control one must reach the same parabolic depth `h~(pi/2)d^2/L` at exponential scale, use an observation geometry outside the present single-point outward sector, or invoke source-faithful information that excludes the maximal-contact direction.

The result is deliberately restricted to `0<=D<=pi/4`. That range is where the exact logarithmic modulus `phi_D` is globally one-Lipschitz; beyond it the derivative can exceed one and the factor-two argument no longer applies. No claim is made here about the optimal all-future threshold farther from the antipode.

## Falsification boundary

This is a theorem for the canonical maximal-contact matched pair, not for arbitrary unit-circle divisors or the actual Xi source. It controls the sup norm of one outward complex spatial point over all `s>=0`; it does not prove sufficiency above the threshold, does not cover inward continuation or general nonlocal complex sensors, and does not establish that Xi can realize the matched packet.

The fixed transition separation `rho` remains independent of `N`, so whenever the right-hand side of `(9)` tends to `-infinity`, any Lipschitz decoder for `Lambda_per` on a class containing this pair inherits the reciprocal exponential conditioning lower bound. Conversely, a large matched-pair signal above threshold only removes this particular obstruction and is not a reconstruction theorem.

## Prior-art audit

A directed audit checked the de Bruijn--Newman complex heat-flow literature, effective complex estimates for `H_t`, and recent work on zeros of high polynomial powers under holomorphic heat flow. Those works supply the surrounding heat-flow setting but do not provide the matched-transition Gaussian/binomial identity `(1)` or the factor-two all-future visibility comparison `(4)`. No external theorem is used in the derivation: the proof consists of the exact XF-150 finite-frequency expansion, a Gaussian square identity, the elementary one-Lipschitz estimate `(15)`, and the standard Gaussian exponential-moment bound. No source entry is therefore required.

## Next gate

For this maximal-contact family, the near-antipodal target-side question is now settled at exponential scale: positive heat time cannot lower the outward `pi/2` parabolic reach constant. The higher-value next step is source-side: derive from the actual Xi source a transition-sharp direction with sufficient antipodal/complex reach, or prove that Xi cannot realize the maximal-contact direction. A secondary target-side question is whether the factor-two argument, or a different exact estimate, extends the all-future threshold beyond the quarter-period sector without weakening the transition modulus.