# XF-137 — optimized exterior patch hides a full-degree logarithmic heat jet

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/TRANSITION-CONDITIONING` + `FULL-DEGREE-LOG-JET` + `ZERO-DELAY` + `UNIT-CIRCLE-MATCHED-CONTROL` + `LOCAL-PATCH-OBSERVABILITY` + `CROSS-SCALE`. XF-135 proves transition blindness for logarithmic jets whose generic fixed-radius Cauchy cost is subexponential, and XF-136 enlarges the hidden central-packet aperture to the sharp constant `b_*` within the XF-133 envelope. The optimized aperture crosses a qualitative threshold: it is large enough to pay the factorial cost of an **entire degree-order logarithmic jet** if the jet is taken at a macroscopic exterior point inside the blind patch.

Let

\[
b_*
:=
\frac12\sqrt{W_0(2)\bigl(2+W_0(2)\bigr)}
=0.779767136088\ldots
\tag{1}
\]

be the XF-136 aperture constant. For even degree `N=2M`, take the XF-134 transition-sharp control with the XF-136 optimal packet depth `r=floor(alpha_* M)`, and write

\[
Q_s(\beta)
:=
E_{\rm c}(-e^{\beta/N},s),
\qquad
q_0(\beta):=1+e^\beta.
\tag{2}
\]

For every `rho>=0`, the shifted control has trace `Q_(s+rho)` and

\[
\Lambda_{\rm per}(E_{\rm c})=0,
\qquad
\Lambda_{\rm per}(E_{{\rm c},\rho})=-\rho.
\tag{3}
\]

Define the exterior center

\[
\lambda_*:=\frac{b_*}{2},
\qquad
\beta_N:=\lambda_*N.
\tag{4}
\]

For any fixed `0<theta<=1`, put

\[
d_\theta:=\frac{\theta}{e}.
\tag{5}
\]

Because

\[
\boxed{
b_*>\frac2e,}
\tag{6}
\]

one has `d_theta<lambda_*` and `lambda_*+d_theta<b_*`. Then, uniformly in the complete future history and in every finite time shift,

\[
\boxed{
\sup_{\substack{s\ge0,\ \rho\ge0\\1\le j\le\lfloor\theta N\rfloor}}
\left|
\partial_\beta^j\log Q_s(\beta_N)
-
\partial_\beta^j\log Q_{s+\rho}(\beta_N)
\right|
\le
\exp\!\left[-c_\theta N+O(\log N)\right],
}
\tag{7}
\]

where

\[
\boxed{
c_\theta:=b_*-\frac{2\theta}{e}>0.}
\tag{8}
\]

In particular, for the **full degree-order jet** `1<=j<=N`,

\[
\boxed{
c_*:=c_1=b_*-\frac2e
=0.044008253745\ldots>0,}
\tag{9}
\]

so every root-spacing-normalized logarithmic derivative through order `N` remains exponentially transition-blind at the same observation point throughout the entire future heat history.

This is not an exact non-identifiability theorem: exact degree-order derivative data can carry the missing state information. It is a conditioning theorem. On the explicit matched-control pair, recovering an order-one transition-time shift from the full degree-order logarithmic jet requires exponential accuracy at rate at least `exp(c_* N-O(log N))` in the observation norm `(7)`.

## 1. The optimized packet is relatively tiny on a growing exterior Cauchy disk

Write the transition-sharp trace as

\[
Q_s(\beta)=q_0(\beta)+u_s(\beta),
\tag{10}
\]

where `u_s=t_* Delta E(-e^(beta/N),s)` and XF-134 gives `|t_*|<=2`. With the optimized XF-136 depth,

\[
A_N
:=
\frac{(r!)^2}{(M^2-r^2)^r}
=
\exp[-b_*N+O(\log N)].
\tag{11}
\]

The XF-133 complex-patch estimate is simultaneous in every heat time and every complex probe:

\[
|u_s(\gamma)|
\le
2e^{|\gamma|}A_N,
\qquad s\ge0.
\tag{12}
\]

Fix `theta` and consider the growing disk

\[
D_{\theta,N}
:=
\{\gamma:|\gamma-\beta_N|\le d_\theta N\}.
\tag{13}
\]

On this disk,

\[
|\gamma|\le(\lambda_*+d_\theta)N,
\qquad
\operatorname{Re}\gamma\ge(\lambda_*-d_\theta)N>0.
\tag{14}
\]

Hence the stationary endpoint carrier satisfies

\[
|q_0(\gamma)|
=|1+e^\gamma|
\ge e^{\operatorname{Re}\gamma}-1
\ge e^{(\lambda_*-d_\theta)N}-1.
\tag{15}
\]

Combining `(11)`--`(15)` gives, uniformly for `gamma in D_(theta,N)` and `s>=0`,

\[
\begin{aligned}
\left|\frac{u_s(\gamma)}{q_0(\gamma)}\right|
&\le
\frac{2e^{(\lambda_*+d_\theta)N}A_N}
{e^{(\lambda_*-d_\theta)N}-1}\\
&=
\exp\!\left[-(b_*-2d_\theta)N+O(\log N)\right]\\
&=
\exp\!\left[-c_\theta N+O(\log N)\right].
\end{aligned}
\tag{16}
\]

The center `lambda_*` cancels from the exponential rate. Its role is geometric: it places a disk of radius `d_theta N` wholly inside the positive-real-`beta` half-plane and wholly inside the XF-136 blind aperture. The remaining exponential budget is exactly the packet rate `b_*` minus the two radial margins paid when passing from the absolute packet bound to a relative carrier bound.

For large `N`, the right side of `(16)` is below `1/2`. Therefore `Q_s/q_0=1+u_s/q_0` is zero-free on `D_(theta,N)`, uniformly in `s`, and the analytic branch

\[
F_s(\gamma)
:=
\log\!\left(1+\frac{u_s(\gamma)}{q_0(\gamma)}\right)
\tag{17}
\]

obeys

\[
\sup_{\gamma\in D_{\theta,N}}|F_s(\gamma)|
\le
\exp[-c_\theta N+O(\log N)].
\tag{18}
\]

## 2. A radius proportional to `N` pays for a jet proportional to `N`

For `j>=1`, the common carrier cancels:

\[
\partial_\beta^j\log Q_s
-
\partial_\beta^j\log Q_{s+\rho}
=
\partial_\beta^jF_s
-
\partial_\beta^jF_{s+\rho}.
\tag{19}
\]

Apply Cauchy's estimate at the center `beta_N` using the entire radius `d_theta N` from `(13)`. Equations `(18)`--`(19)` give

\[
\left|
\partial_\beta^j\log Q_s(\beta_N)
-
\partial_\beta^j\log Q_{s+\rho}(\beta_N)
\right|
\le
\exp[-c_\theta N+O(\log N)]
\frac{j!}{(d_\theta N)^j}.
\tag{20}
\]

The choice `d_theta=theta/e` is exactly what neutralizes the factorial at the top of a `theta N` jet. A uniform Stirling upper bound gives, for `1<=j<=theta N`,

\[
\frac{j!}{(d_\theta N)^j}
\le
C\sqrt j
\left(\frac{j}{\theta N}\right)^j
\le
C\sqrt N.
\tag{21}
\]

Thus the whole factorial price is only polynomial, and `(7)` follows.

There is also a useful variational interpretation. If a Cauchy radius `dN` is used to control all orders through `theta N`, its exponential factorial cost is

\[
\kappa(\theta,d)
=
\max\left\{0,\theta\left[\log\!\left(\frac{\theta}{d}\right)-1\right]\right\}.
\tag{22}
\]

while the relative packet margin from `(16)` is `b_*-2d`. The net blindness exponent is therefore

\[
b_*-2d-\kappa(\theta,d).
\tag{23}
\]

Within this growing-disk Cauchy argument, `(23)` is maximized at

\[
d=\frac\theta e,
\tag{24}
\]

and the optimum is exactly `c_theta=b_*-2theta/e`. Thus `(8)` is not an arbitrary convenient choice of radius: it is the best exponent produced by this analytic-continuation balance.

## 3. XF-136 crosses the full-degree threshold that the older aperture did not

The qualitative point is the strict inequality `(6)`. For the old XF-133--XF-135 aperture rate `log(2)/2=0.3465...`, a radius large enough to pay for `N!` could not fit inside the hidden region. After the Lambert-W optimization,

\[
\frac{b_*}{2}
=0.3898835680\ldots
>
\frac1e
=0.3678794412\ldots .
\tag{25}
\]

There is therefore enough room for a Cauchy disk of radius `N/e` around the symmetric exterior center `beta_N=(b_*/2)N`, with a positive exponential margin left over. At full order,

\[
\sup_{1\le j\le N}
\frac{j!}{(N/e)^j}
=
\exp[O(\log N)],
\tag{26}
\]

whereas the relative packet signal is `exp[-(b_*-2/e)N+O(log N)]`.

This converts the numerical improvement in XF-136 into a structural one. XF-135 only certified raw logarithmic derivatives satisfying `J_N log J_N=o(N)` when the observation remained only a fixed root-spacing distance into the exterior. The present theorem allows `J_N=N`, but it pays for that by moving the observation center a fixed **macroscopic** distance into the exterior so that a Cauchy disk of radius `Theta(N)` avoids the carrier-zero line.

That distinction is essential. The result does not prove that a full degree-order jet taken only `O(1)` in `beta` away from the unit circle is transition-blind. Near that line the available zero-free Cauchy radius is only `O(1)`, so the factorial growth of high logarithmic derivatives can overwhelm the central-packet suppression. A root-spacing full-degree jet remains a genuinely stronger target observable and is not eliminated here.

## 4. Physical-coordinate form and conditioning consequence

XF-067 uses

\[
\beta=-\frac{2\pi iN}{L}z.
\tag{27}
\]

Thus the center `(4)` is the fixed macroscopic point

\[
\boxed{
z_*
=i\frac{b_*}{4\pi}L
=i\,0.0620518971\ldots L.}
\tag{28}
\]

For the full jet `theta=1`, the Cauchy disk used in the proof has physical radius

\[
\boxed{
R_*
=
\frac{L}{2\pi e}
=0.0585498315\ldots L.}
\tag{29}
\]

Its lower edge remains a positive macroscopic distance from the real divisor line,

\[
\frac{L}{2\pi}
\left(\frac{b_*}{2}-\frac1e\right)
=
\frac{c_*}{4\pi}L
=0.0035020656\ldots L,
\tag{30}
\]

and its upper edge remains inside the XF-136 blind disk. Moreover

\[
\left(\frac{L}{2\pi N}\right)^j
\partial_z^j
=
(-i)^j\partial_\beta^j,
\tag{31}
\]

so `(7)` is exactly the same estimate for the root-spacing-normalized physical logarithmic derivatives.

For any fixed `rho>0`, define the full future `N`-jet observation by collecting `(31)` for `1<=j<=N` and `s>=0` in the sup norm. Equations `(3)`, `(7)`, and `(9)` imply that every Lipschitz decoder of `Lambda_per` on this two-point matched-control family has condition number at least

\[
\boxed{
\exp[c_*N-O(\log N)].
}
\tag{32}
\]

The bound is uniform in `rho`; as in XF-134--XF-136, `rho=rho_N` may be any finite nonnegative sequence. Exact analytic identifiability is therefore compatible with exponentially catastrophic transition conditioning even after the local observation is upgraded from a function value or subexponential jet to a degree-sized logarithmic jet.

## 5. Prior-art boundary and next gate

Cauchy derivative estimates and the ill-conditioning of analytic continuation are classical. A directed audit included Trefethen, *Quantifying the ill-conditioning of analytic continuation*, BIT Numerical Mathematics 60 (2020), 901--915, DOI `10.1007/s10543-020-00802-7`, and the quantitative parabolic analyticity/observability literature represented by Escauriaza--Montaner--Zhang and Apraiz--Escauriaza--Wang--Zhang. Those works delimit the broad analytic-continuation and heat-observability setting; they do not provide the explicit unit-circle transition-sharp packet, the Lambert-W aperture, or the degree-order jet threshold `(8)`.

No external theorem is load-bearing here. The proof uses only the internal XF-133 analytic packet estimate, the XF-134 transition-sharp matched controls, the optimized XF-136 amplitude, the elementary carrier lower bound, and the classical Cauchy/Stirling inequalities. No source anchor is therefore added to `SOURCES.md`, and no novelty claim is made for Cauchy theory itself.

The target-side frontier is now narrower. Merely replacing local values by **all normalized logarithmic derivatives through the polynomial degree** does not restore polynomial transition conditioning if the observation remains at a macroscopic exterior center inside the optimized blind region. The two nearby escape routes that remain are materially different: use a full high-order jet only root-spacing distance from the divisor, where collision poles can amplify the central packet, or prove an Xi-specific source theorem excluding the XF-133 central packet before target inversion. The accepted Gaussian-reference quotient clue remains live precisely on this source-specific side; common reference division alone still cancels from logarithmic-jet differences.

## Conclusion

The Lambert-W aperture of XF-136 is not merely a larger constant. Because `b_*>2/e`, it is wide enough to hide the **entire degree-order logarithmic heat jet** of a transition-sharp matched control at a single macroscopic exterior point. With the optimal Cauchy radius `d_theta=theta/e`, jets through order `theta N` have blindness exponent `c_theta=b_*-2theta/e`; at full order the explicit residual exponent is

\[
\boxed{
c_*=b_*-2/e=0.044008253745\ldots .}
\]

Thus complete future access to `N` root-spacing-normalized logarithmic derivatives can still require exponentially precise data to recover an order-one transition-time change. The remaining local target-side loophole is no longer derivative count by itself, but proximity: a degree-order jet taken only root-spacing distance from the divisor is outside this theorem and is the next natural conditioning test.