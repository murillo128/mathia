# XF-049 — finite heat-zero Fourier flow is Volterra-triangular

**Status:** `EXACT-DERIVED` + `LITERATURE-CALIBRATED` + `FINITE-MODEL/STRUCTURAL` + `TRANSPORT-BOUNDARY`. XF-048 supplies a source-specific endpoint selector: in the `H_0` zero coordinate, the critical XF-047 memory frequency is `Theta(1/log T)`, while the first nonzero prime-power Fourier line stays at `log 2/2`. What remained unclear was whether the nonlinear logarithmic-particle dynamics itself could transfer high-frequency structure down into that prime-free memory band and thereby manufacture the compensating signal that XF-048 requires.

For every finite real-simple polynomial heat-flow control, there is an exact answer: **the positive-frequency zero spectrum is a closed Volterra system.** If

\[
Z_N(\xi,t):=\sum_{j=1}^N e^{-i\xi x_j(t)},
\]

then for `\xi>0`

\[
\boxed{
\partial_t Z_N(\xi,t)
=
\xi^2 Z_N(\xi,t)
-
\xi\int_0^\xi
Z_N(\eta,t)Z_N(\xi-\eta,t)\,d\eta.
}
\tag{1}
\]

Thus the instantaneous evolution at frequency `\xi` uses only frequencies in `[0,\xi]`; there is no direct high-positive/high-negative down-conversion channel. The same one-sided structure is the Fourier form of the complex Burgers equation for the logarithmic derivative of the heat-evolved polynomial. Linearizing that Burgers field about a flat zero density `\rho=1/\sigma` gives the exact positive-frequency multiplier

\[
\lambda_\rho(\xi)=\xi^2-2\pi\rho\xi.
\tag{2}
\]

At the XF-047 memory frequency `\xi=(2\pi/q)/\sigma`, its damping rate is

\[
-\lambda_\rho(\xi)
=
\frac{4\pi^2(q-1)}{q^2\sigma^2},
\tag{3}
\]

**exactly the periodic slow-mode rate `\rho_q` of XF-047.** This identifies the memory obstruction as the low-frequency branch of the same analytic Burgers/Calogero transport, rather than an artifact of periodization.

The result does not yet propagate the XF-048 Gaussian statistic through the actual infinite Xi flow. The raw infinite zero sum in (1) is not defined without renormalization, and spatial tapering introduces commutators/buffer terms. The new boundary is precise: to turn the endpoint selector into a dynamic contradiction, it is enough to prove that this one-sided Volterra structure survives the Xi renormalization and the `W=Theta(log^3 T)` localization with an `o(1)` error in the matched memory statistic over fixed heat time.

## 1. Exact finite zero system

Let `P_t(z)` be a monic polynomial of degree `N` satisfying the backward heat equation

\[
\partial_t P_t=-\partial_z^2P_t
\tag{4}
\]

on a time interval on which all roots are distinct and real. Write

\[
P_t(z)=\prod_{j=1}^N(z-x_j(t)).
\tag{5}
\]

Differentiating `P_t(x_j(t))=0` and using the standard logarithmic derivative identity at a simple root gives

\[
\boxed{
x_j'
=2\sum_{k\ne j}\frac1{x_j-x_k}.
}
\tag{6}
\]

This is the finite version of the real-simple zero-motion law used throughout `xi_flow`.

For real `\xi`, define the finite zero characteristic sum

\[
Z_N(\xi,t)
:=
\sum_{j=1}^N e^{-i\xi x_j(t)}.
\tag{7}
\]

Differentiate and symmetrize unordered pairs:

\[
\begin{aligned}
\partial_t Z_N(\xi,t)
&=-i\xi\sum_j x_j'e^{-i\xi x_j}\\
&=-2i\xi\sum_{j<k}
\frac{e^{-i\xi x_j}-e^{-i\xi x_k}}
{x_j-x_k}.
\end{aligned}
\tag{8}
\]

For every pair and every real `\xi`, with the integral oriented in the usual way when `\xi<0`,

\[
\frac{e^{-i\xi x}-e^{-i\xi y}}{x-y}
=
-i\int_0^\xi
 e^{-i\eta x}e^{-i(\xi-\eta)y}\,d\eta.
\tag{9}
\]

On the other hand,

\[
\begin{aligned}
Z_N(\eta)Z_N(\xi-\eta)
={}&Z_N(\xi)\\
&+\sum_{j\ne k}
 e^{-i\eta x_j}e^{-i(\xi-\eta)x_k}.
\end{aligned}
\tag{10}
\]

The two ordered terms associated with each unordered pair have equal `\eta`-integrals after the substitution `\eta\mapsto\xi-\eta`. Hence

\[
\int_0^\xi Z_N(\eta)Z_N(\xi-\eta)\,d\eta
=
\xi Z_N(\xi)
+2\sum_{j<k}\int_0^\xi
 e^{-i\eta x_j}e^{-i(\xi-\eta)x_k}\,d\eta.
\tag{11}
\]

Combining (8), (9), and (11) proves (1):

\[
\boxed{
\partial_t Z_N(\xi)
=
\xi^2 Z_N(\xi)
-
\xi\int_0^\xi
Z_N(\eta)Z_N(\xi-\eta)\,d\eta.
}
\tag{12}
\]

No asymptotic approximation, lattice hypothesis, or small-amplitude expansion is used.

## 2. The spectral evolution is genuinely one-sided

For `\xi>0`, the right-hand side of (12) depends only on

\[
\{Z_N(\eta):0\le\eta\le\xi\}.
\tag{13}
\]

Consequently every interval `[0,\Omega]` is algebraically closed under the finite zero-motion vector field. In particular, the quadratic term at a small positive frequency cannot be formed by combining a much larger positive frequency with a negative one. This differs from the unconstrained Fourier convolution of a generic real Burgers field; it is the analytic/Hardy half-space structure inherited from a logarithmic derivative whose poles lie on the real axis.

This statement needs one qualification. Since `Z_N(\xi)` is an entire function of `\xi`, its values in disjoint frequency ranges are not freely specifiable. Volterra triangularity is therefore a statement about the **form of the vector field**, not a claim that one can arbitrarily alter high-frequency data while keeping an exact finite point configuration unchanged at low frequency. What it rules out is a direct nonlinear high-to-low convolution channel in any finite heat-zero truncation.

The formula is translation covariant. Replacing every `x_j` by `x_j+b` multiplies both sides by `e^{-i\xi b}` because the convolution factors acquire phases `e^{-i\eta b}` and `e^{-i(\xi-\eta)b}`. It is also consistent at `\xi=0`, where `Z_N(0)=N` is conserved.

Two elementary controls fix the coefficient and sign. For `N=1`, the convolution is exactly `\xi Z_1(\xi)`, so the two terms in (12) cancel and the single root is stationary. For `N=2`, if `d=x_2-x_1`, direct differentiation gives

\[
\partial_t Z_2
=
\frac{2i\xi}{d}
\left(e^{-i\xi x_1}-e^{-i\xi x_2}\right),
\tag{14}
\]

which is exactly what (12) gives after the diagonal convolution cancels the `\xi^2 Z_2` term.

## 3. Complex Burgers is the analytic origin of the Volterra law

Set

\[
m(z,t):=\frac{\partial_zP_t(z)}{P_t(z)}
=\sum_{j=1}^N\frac1{z-x_j(t)}.
\tag{15}
\]

From `P_t=-P_{zz}` one obtains directly

\[
\boxed{
m_t=-m_{zz}-2m\,m_z.
}
\tag{16}
\]

Thus the finite heat-zero system is the pole dynamics of a backward-viscous complex Burgers equation. In the upper half-plane each Cauchy pole `1/(z-x_j)` has one-sided positive boundary frequency for the Fourier convention used in (7). Multiplication preserves that half-space support, so the quadratic Burgers term at frequency `\xi>0` becomes a convolution only over `0<\eta<\xi`. Equation (12) is the pole-measure version of that analytic fact.

The Burgers/Cole--Hopf connection and Calogero-type pole dynamics are classical. Senouf's 1997 analysis of Burgers singularities explicitly places pole motion in an infinite-dimensional Calogero system; Poláčik--Šverák (2008) relate zeros of complex caloric functions to singularities of complex viscous Burgers solutions. Recent polynomial heat-flow work by Höfert, Jalowy and Kabluchko, published in *International Mathematics Research Notices* in August 2026, likewise identifies a Burgers equation for the limiting Stieltjes transform of heat-evolved polynomial zero distributions. Those works delimit the prior-art class. Equation (12) is derived here independently and is used only for its Mathia-specific frequency consequence below; no claim of general novelty for the Burgers correspondence is made.

## 4. Flat-density linearization reproduces the XF-047 memory clock exactly

The exact match with the previously derived Cauchy slow mode is visible already at the Burgers level. A flat real zero density `\rho>0` has upper-half-plane Cauchy field

\[
m_\rho=-i\pi\rho.
\tag{17}
\]

Write

\[
m=m_\rho+v.
\tag{18}
\]

Since `m_\rho` is constant, (16) gives

\[
\boxed{
v_t=-v_{zz}+2i\pi\rho\,v_z-2v\,v_z.
}
\tag{19}
\]

For a positive boundary frequency `\xi`, the linear part has multiplier

\[
\boxed{
\lambda_\rho(\xi)
=\xi^2-2\pi\rho\xi.
}
\tag{20}
\]

Hence the low band `0<\xi<2\pi\rho` is damped, despite the anti-diffusive `+\xi^2` contribution from backward heat, because the background Cauchy field contributes the larger `-2\pi\rho\xi` term.

Now take the Xi local spacing `\sigma` and set `\rho=1/\sigma`. An index Fourier angle `\theta` corresponds to physical frequency

\[
\xi=\frac\theta\sigma.
\tag{21}
\]

For the first mode of a `q`-periodic pattern, `\theta=2\pi/q`. Substitution into (20) gives

\[
\begin{aligned}
-\lambda_{1/\sigma}(\xi)
&=\frac{2\pi\theta-\theta^2}{\sigma^2}\\
&=\boxed{
\frac{4\pi^2(q-1)}{q^2\sigma^2}
}.
\end{aligned}
\tag{22}
\]

This is exactly the `\rho_q` appearing in XF-047, including the finite-`q` correction `(q-1)/q^2`, not merely its `q\to\infty` scaling. The periodic Cauchy calculation and the analytic Burgers linearization are therefore two representations of the same slow spectral branch.

The flat density in (17) is a local infinite-background model, not an additional theorem about the Xi zero set. Its role here is a stringent consistency check and a structural identification of the clock already proved by the exact periodic control in XF-047.

## 5. Consequence for the endpoint prime-free selector

XF-048 shows that the endpoint Xi source has no prime-power Fourier line below

\[
\omega_2=\frac{\log2}{2},
\tag{23}
\]

while the critical memory frequency is

\[
\xi_T=\Theta\!\left(\frac1{\log T}\right)\to0.
\tag{24}
\]

The finite heat-zero dynamics now excludes one possible explanation for the compensating structure required by XF-048: **ordinary nonlinear mode mixing in a finite logarithmic-particle truncation cannot take frequencies above the prime gap and directly fold them down to `\xi_T`.** At a positive frequency `\xi_T`, the exact quadratic term sees only frequencies at or below `\xi_T`.

This does not yet say that an actual Xi block has no compensating endpoint signal. Such a signal can still come from low-frequency content already present, from the slowly varying archimedean density, from localization/buffer commutators, or from terms created by the renormalized infinite-system limit. What XF-049 removes is the generic "high-frequency cascade back into the memory band" escape inside the finite heat-zero dynamics itself.

There is also no conflict with the fixed-time persistence of XF-047. At `q\asymp\log^2T`, (22) gives `\rho_q=1/4+o(1)` with the corrected Xi spacing, so a fixed heat-time interval only changes the critical memory coefficient by an order-one factor. The endpoint selector can therefore become dynamically useful only if the remaining low-frequency and localization terms are controlled to `o(1)`; universal smoothing alone still does not supply that control.

## 6. Infinite-volume and localization boundary

Equation (12) is deliberately finite. For the actual Xi zero set,

\[
\sum_j e^{-i\xi x_j}
\tag{25}
\]

is not an ordinary convergent function, and a hard finite truncation introduces edge terms that are not present in the complete zero-motion law. Passing (12) naively to `N\to\infty` would therefore be unjustified.

The source-facing observable of XF-048 is instead a Gaussian carrier of width

\[
W\asymp\log^3T
\tag{26}
\]

centered at the memory frequency. Multiplication by that spatial taper becomes a narrow frequency convolution, while differentiating it along the zero flow creates explicit localization commutators. Those terms are precisely where near-buffer forcing can enter. XF-046 already makes the genuinely remote centered forcing little-`o` at the critical scale, but it does not estimate the full Fourier commutator of the XF-048 probe.

The next theorem-level gate is therefore concrete. Construct either a renormalized upper-half-plane Cauchy field for the real-simple Xi zeros, or an equivalent Gaussian-tapered finite-window identity, and prove over every fixed legitimate heat-time interval that its memory-band evolution equals the one-sided Burgers/Volterra evolution plus an error whose contribution to the XF-048 matched statistic is `o(1)`. The estimate must retain the corrected local density `\sigma_T`, separate near-buffer from remote input, and remain valid without extending the zero-motion law through collisions.

If such an estimate holds, the endpoint prime-free condition cannot be repaired by hidden high-frequency Xi structure; only the genuinely low-frequency source/buffer sector remains. If it fails, the leading commutator term identifies the exact mechanism by which the infinite Xi source defeats the finite Volterra closure.

## 7. Stress tests and evidence boundary

The derivation of (12) uses only finite sums and is exact on every real-simple interval. It does not cross a collision time. This is important because the root labels required in (6) cease to be a legitimate analytic coordinate at a collision, as already emphasized by XF-001.

The sign in (20) also matters. Backward heat by itself contributes `+\xi^2`, so the Burgers linearization is not globally dissipative: frequencies above `2\pi\rho` have positive linear growth. The memory regime is far below that threshold, where the Cauchy background gives the known damping. XF-049 therefore does not assert a new global contraction theorem.

Finally, the finite Volterra closure is not yet a source-specific Xi invariant. It is universal for finite real-rooted polynomial heat flows and is best viewed as a structural transport boundary. The Xi-specific input remains XF-048's endpoint explicit formula. What is new for the local program is the exact alignment of three previously separate pieces: the finite zero-motion spectrum is one-sided, its flat-density symbol reproduces the XF-047 slow rate exactly, and the only endpoint frequencies capable of cancelling the memory probe must therefore be sought in the low-frequency/localization sector rather than in generic high-frequency nonlinear mixing.

A targeted prior-art search across Burgers pole dynamics, caloric zero evolution, and current polynomial heat-flow/Stieltjes-transform work found the classical Burgers/Calogero correspondence and continuum limits described above, but no source that closes the specific Xi `W\asymp\log^3T` localized transport problem or couples this Volterra half-space structure to the prime-free endpoint selector of XF-048. Absence of such a match is not used as evidence of broad novelty. No external theorem is load-bearing in (12), (16), or (22), so `SOURCES.md` is unchanged.

## 8. Consequence for `xi_flow`

XF-047 showed that the critical memory wave is an exact nonlinear slow mode compatible with the source-counting information then in use. XF-048 showed that the actual endpoint zeta source forbids that coherent wave unless additional low-frequency structure cancels its matched statistic. XF-049 now shows that, in the finite heat-zero dynamics, **that cancellation cannot be generated by a high-to-low spectral cascade**: positive frequencies evolve by a Volterra-triangular law, and the same Burgers symbol gives exactly the observed memory decay clock.

The remaining dynamic problem is therefore narrower than "transport an arbitrary statistic to the endpoint." It is to prove or falsify an **infinite-volume localized Volterra closure** at the memory scale. A positive result would reduce the endpoint contradiction to controlling only pre-existing low-frequency/near-buffer content; a negative result would expose the precise Xi-specific commutator that must be estimated instead.