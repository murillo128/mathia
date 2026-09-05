# XF-057 — chirped critical flux escapes the pointwise slow-frequency selector

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `NEGATIVE/OBSTRUCTION` + `SOURCE-TO-TRANSITION-NONCOERCIVITY`. XF-056 closes the frequency-detuning loophole for a single coherent slow wave: the actual Xi carrier is `o(1)` against every compact selector whose center moves continuously through the slow Cauchy cone, while a pure critical wave has an order-one matched response at its own center. A stronger inverse conclusion does **not** follow from those pointwise selector estimates alone.

There is an explicit chirped finite-gap control whose local frequency sweeps continuously through the same slow cone, whose translated source-scale gap averages remain much flatter than the counting tolerances used earlier in the line, and whose critical triple-flux variation stays of order one, yet **every individual XF-056 selector has vanishing response uniformly over the whole cone**.

Use

\[
q\asymp \log^2T,\qquad M=q^2,
\qquad
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\qquad
W=M\sigma_T,
\tag{1}
\]

with integer `q`, and fix constants

\[
a_0>b>0,\qquad \kappa>0.
\tag{2}
\]

Put

\[
\Phi_j:=\frac{a_0}{q}j+\frac{b}{2q^3}j^2,
\qquad
\varepsilon:=\frac{\kappa}{M},
\tag{3}
\]

and define an ordered gap configuration by

\[
\boxed{
 z_{j+1}-z_j
 =\sigma_T\bigl(1+\varepsilon\cos\Phi_j\bigr),
 \qquad z_0=T.
}
\tag{4}
\]

For large `T` all gaps are positive. On the active `2M`-gap block `|j|\le M`, the phase increment is

\[
\delta_j:=\Phi_{j+1}-\Phi_j
=\frac{a_0}{q}+\frac{b(j+1/2)}{q^3},
\tag{5}
\]

so

\[
\boxed{
\frac{a_-}{q}\le \delta_j\le\frac{a_+}{q},
\qquad
a_-:=a_0-b>0,
\qquad
a_+:=a_0+b+o(1).
}
\tag{6}
\]

Thus the control is not a hidden high-frequency corrugation. Its instantaneous wavelength is everywhere of memory order `q`, and its frequency sweeps across an interval of width `Theta(1/q)` containing `Theta(q)` distinct XF-056 resolution bands because one selector has index-frequency width `1/M=1/q^2`.

Let

\[
f_{T,\theta}(x)
=
g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega_{\theta,T}(x-T)+\varphi_{\theta,T})},
\qquad
\omega_{\theta,T}=\frac{\theta}{\sigma_T},
\tag{7}
\]

be the exact XF-056 probe, with `\widehat g\in C_c^\infty((-1,1))`, and let

\[
\Theta_T
=
\left[\frac cq,\frac{C\log\log T}{q}\right]
\tag{8}
\]

for fixed `c,C>0`, choosing `c<a_-`. Then

\[
\boxed{
\sup_{\theta\in\Theta_T}
\left|
\sum_{j\in\mathbb Z}f_{T,\theta}(z_j)
\right|
=O\!\left(\frac{\log\log T}{\sqrt q}\right)
=o(1).
}
\tag{9}
\]

The phases `\varphi_{\theta,T}` may be arbitrary. In contrast, if `d_j` and `\phi_j` are the XF-030/XF-035 log-gap contrast and triple flux on the active block,

\[
d_j
:=\log\frac{z_{j+2}-z_{j+1}}{z_{j+1}-z_j},
\qquad
\phi_j:=F'(d_j),
\tag{10}
\]

and

\[
V_M:=\sum_{j=-M}^{M-3}|\phi_{j+1}-\phi_j|,
\tag{11}
\]

then

\[
\boxed{
0<\frac{3\kappa a_-^2}{2}
\le
\liminf_{T\to\infty} M V_M
\le
\limsup_{T\to\infty} M V_M
\le 3\kappa a_+^2<\infty.
}
\tag{12}
\]

Hence the pointwise continuous selector family can vanish uniformly while the configuration remains exactly at the **borderline critical triple-flux scale**. In particular, the implication

\[
\sup_{\theta\in\Theta_T}|\text{selector}(\theta)|=o(1)
\quad\Longrightarrow\quad
M V_M=o(1)
\tag{13}
\]

is false under the local source-envelope/span information already admitted by the line. The missing inverse bridge cannot be a frequency-by-frequency estimate followed only by a supremum over centers. It must aggregate spectral/time-frequency information in a coercive way, or use additional Xi dynamics that forbids this chirped distribution of the critical shape budget.

This is a **matched finite-gap obstruction**, not a claim that Xi realizes (4). It does not refute XF-056: that finding correctly excludes every single coherent pure wave at every center. The new point is that distributing the same critical variation over a slowly changing phase makes each `1/M`-resolution coefficient small while leaving the total transition-side flux budget nonvanishing.

## 1. A quadratic exponential-sum bound spreads the chirp over many selector bands

The only oscillatory estimate needed is the classical van der Corput second-derivative bound. In the present quadratic specialization, for any real `\nu`, any integer interval `I` of length `N`, and either sign,

\[
\boxed{
\left|
\sum_{j\in I}
 e^{i(\pm\Phi_j-\nu j)}
\right|
\ll_b
1+Nq^{-3/2}+q^{3/2}.
}
\tag{14}
\]

Indeed the phase has constant second derivative `\pm b/q^3`; the standard estimate `N\lambda^{1/2}+\lambda^{-1/2}` with `\lambda=b/q^3` gives (14). The bound is uniform in the linear term `\nu`, which is exactly what is needed when the selector center moves.

For every fixed Schwartz function `a`, Abel summation and (14) give

\[
\boxed{
\sup_{\nu\in\mathbb R}
\left|
\sum_{j\in\mathbb Z}
 a(j/M)e^{i(\pm\Phi_j-\nu j)}
\right|
=O_a(q^{3/2}).
}
\tag{15}
\]

The `Nq^{-3/2}` part of (14) is harmless on dyadic tails because `a` is Schwartz; on the `N\asymp M=q^2` core it is only `O(q^{1/2})`. The `q^{3/2}` curvature term dominates.

Define the cumulative chirp by

\[
A_0=0,
\qquad
A_{j+1}-A_j=\cos\Phi_j.
\tag{16}
\]

Applying (14) with `\nu=0` to the interval from `0` to `j` yields

\[
|A_j|
\ll_b q^{3/2}+|j|q^{-3/2}.
\tag{17}
\]

Since (4) gives

\[
z_j=T+j\sigma_T+\sigma_T\varepsilon A_j,
\tag{18}
\]

the chirp displaces the arithmetic lattice by only `O(\sigma_Tq^{-1/2})` throughout the `M`-scale core, despite carrying a nonvanishing total flux budget below.

## 2. The exact XF-056 probe is uniformly blind to the chirp

Write

\[
x_j^0:=T+j\sigma_T,
\qquad
p_j:=z_j-x_j^0=\sigma_T\varepsilon A_j.
\tag{19}
\]

XF-056 already proves the exact Poisson cancellation

\[
\sum_{j\in\mathbb Z}
 f_{T,\theta}(x_j^0)=0
\tag{20}
\]

uniformly for `\theta\in\Theta_T`: the selector center is farther than its `1/M` support width from zero and from every `2\pi` alias.

It remains to estimate the perturbation away from the arithmetic lattice. At a lattice point,

\[
f'_{T,\theta}(x_j^0)
=
\frac{e^{-i(\theta j+\varphi_{\theta,T})}}{\sigma_T}
\left[
\frac1M g'(j/M)-i\theta g(j/M)
\right].
\tag{21}
\]

The cumulative factor `A_j` costs one inverse discrete frequency. More precisely, for a Schwartz `a` put

\[
B_a(\theta):=
\sum_j A_j a(j/M)e^{-i\theta j}.
\tag{22}
\]

Discrete summation by parts, using `A_{j+1}-A_j=\cos\Phi_j`, gives

\[
|e^{i\theta}-1|\,|B_a(\theta)|
\ll
\left|
\sum_j \cos\Phi_j\,a((j+1)/M)e^{-i\theta j}
\right|
+
\sum_j|A_j|\,|a((j+1)/M)-a(j/M)|.
\tag{23}
\]

The first term is `O_a(q^{3/2})` by (15). Equation (17), together with

\[
\sum_j|\Delta a(j/M)|=O_a(1),
\qquad
\sum_j|j|\,|\Delta a(j/M)|=O_a(M),
\tag{24}
\]

makes the second term `O_a(q^{3/2})` as well. Since `\theta\ge c/q`, one obtains

\[
\boxed{
\sup_{\theta\in\Theta_T}|B_a(\theta)|
=O_a(q^{5/2}).
}
\tag{25}
\]

Taylor expanding (7) around `x_j^0` and using (20)--(21), the complete first-order contribution is therefore

\[
\begin{aligned}
\left|
\sum_j p_j f'_{T,\theta}(x_j^0)
\right|
&\ll
\varepsilon
\left(
\theta |B_g(\theta)|+rac1M|B_{g'}(\theta)|
\right)\\
&\ll
\frac{\kappa\log\log T}{\sqrt q}
+O(q^{-3/2}).
\end{aligned}
\tag{26}
\]

The Taylor remainder is smaller. From (17) and Schwartz decay,

\[
\sum_j A_j^2(1+|j|/M)^{-N}=O_N(q^5)
\tag{27}
\]

for fixed sufficiently large `N`. Uniformly along the tiny segment between `x_j^0` and `z_j`,

\[
|f''_{T,\theta}(x)|
\ll_N
\frac{\theta^2+\theta/M+M^{-2}}{\sigma_T^2}
(1+|j|/M)^{-N}.
\tag{28}
\]

Hence

\[
\sum_j |p_j|^2
\sup_{[x_j^0,z_j]}|f''_{T,\theta}|
\ll
\varepsilon^2 q^5
\left(\theta^2+\frac\theta M+\frac1{M^2}\right)
=O\!\left(\frac{\kappa^2(\log\log T)^2}{q}\right)
=o(1).
\tag{29}
\]

Equations (20), (26), and (29) prove (9). The crucial scale is visible directly: the chirp occupies `Theta(q)` selector-resolution cells, and the quadratic-phase cancellation reduces the coherent `Theta(M)` pure-wave sum to `O(q^{3/2})`. Multiplication by the critical gap amplitude `\varepsilon=\kappa/q^2` then leaves only `O(q^{-1/2})` response at any one center.

## 3. The same chirp retains critical triple-flux variation

Put

\[
u_j:=\cos\Phi_j,
\qquad
r_j:=1+\varepsilon u_j.
\tag{30}
\]

On the active block, (6) gives

\[
\Delta u_j=O(q^{-1}).
\tag{31}
\]

Because `\delta_{j+1}-\delta_j=b/q^3`, a symmetric Taylor expansion around `\Phi_{j+1}` gives the more important second-difference formula

\[
\boxed{
\Delta^2u_j
=-\delta_j^2\cos\Phi_{j+1}+O(q^{-3})
}
\tag{32}
\]

uniformly for `-M\le j\le M-2`. The difference between `\delta_j^2` and the exact average of `\delta_j^2,\delta_{j+1}^2` is itself absorbed by `O(q^{-3})`.

To keep cancellation from hiding the absolute variation, apply (14) to the doubled phase `2\Phi_j`. Over `2M+O(1)` sites,

\[
\sum \cos^2\Phi_j
=M+O(q^{3/2}).
\tag{33}
\]

Since `|\cos x|\ge\cos^2x`, equations (6), (32), and (33) imply

\[
\boxed{
 a_-^2+o(1)
\le
\sum_{j=-M}^{M-2}|\Delta^2u_j|
\le
2a_+^2+o(1).
}
\tag{34}
\]

Now

\[
d_j
=\log r_{j+1}-\log r_j
=O(\varepsilon/q),
\tag{35}
\]

and smoothness of `\log(1+\varepsilon u)` on `|u|\le1` gives

\[
d_{j+1}-d_j
=
\varepsilon\Delta^2u_j
+O(\varepsilon^2/q^2).
\tag{36}
\]

XF-030 gives the exact local triple-flux expansion

\[
F'(d)=-\frac32d+O(d^3).
\tag{37}
\]

Summing the resulting flux differences over the `2M`-gap block, the errors in (36)--(37) are `o(\varepsilon)`, and therefore

\[
\boxed{
V_M
=\frac{3\varepsilon}{2}
\sum_{j=-M}^{M-2}|\Delta^2u_j|
+o(\varepsilon).
}
\tag{38}
\]

Since `M\varepsilon=\kappa`, (34) and (38) prove (12).

This is exactly the scale that matters in the existing transition-side chain. XF-044 identifies relative slow-wave amplitude `Theta(q^{-2})` when `M=q^2` as the critical scale at which `M V_M` is order one. The chirp keeps that same amplitude and wavelength scale; it only destroys global phase coherence across the full `M`-site selector envelope.

## 4. The control still passes the local source inputs that counting can see

For every gap in (4),

\[
\left|
\frac{z_{j+1}-z_j}{\sigma_T}-1
\right|
\le\frac\kappa M.
\tag{39}
\]

Consequently every translated block of `L` consecutive gaps satisfies the deterministic span bound

\[
\left|
\frac{z_{j+L}-z_j}{L\sigma_T}-1
\right|
\le\frac\kappa M.
\tag{40}
\]

At `M=q^2` with `q\asymp\log^2T`, this is far below the fixed-fraction translated-counting error consumed in XF-036 and the local gap envelope admitted in XF-047. The full active span is `O(M\sigma_T)=O(\log^3T)=o(T)`, so the density changes negligibly across it.

Thus the failure of (13) is not a mean-density artifact or a hard boundary fold. As in XF-047, this remains only a matched finite-gap/source-tolerance control: (4) is **not** asserted to be an actual Xi zero block, its continuation is not asserted to satisfy the full global explicit formula, and no root-motion equation is imposed on it.

The distinction matters. XF-048--XF-056 supplied precisely the additional Xi-specific information that kills one coherent memory wave. XF-057 shows that the resulting collection of pointwise band exclusions still does not, by itself, convert local source compatibility into the `o(1)` triple-flux conclusion needed by the strongest transition-side gate.

## 5. What inverse bridge is now ruled out

Consider any proposed source-to-transition argument whose genuinely Xi-specific input from XF-056 is only the uniform scalar family

\[
\sup_{\theta\in\Theta_T}
|\mathcal S_{T,\theta}(t)|=o(1),
\tag{41}
\]

and whose other hypotheses on the candidate local block are no stronger than the translated span/gap-envelope data already matched above. If the argument attempts to conclude `M V_M=o(1)` by identifying each selector with one local Fourier coefficient and then taking a pointwise supremum over `\theta`, (4) is a counterexample to that deterministic inverse step: its corresponding matched zero statistics satisfy the same `o(1)` pointwise bound (9), but (12) keeps `M V_M` away from zero.

The obstruction is a basic concentration mismatch. Triple-flux variation is an `ell^1`-type quantity in a second difference of the gap field. The XF-056 tests are narrow linear functionals of width `1/M`. A chirp can distribute an order-one total variation budget over a growing number of those narrow bands while making every one of their coefficients vanish.

This does **not** show that no inverse theorem exists. It shows what extra ingredient such a theorem must expose. Possibilities include a genuinely coercive aggregate over selector centers, a time-frequency/wave-packet norm that follows the changing local phase, or a dynamical Xi identity proving that a source-compatible transition block cannot realize the chirped concentration pattern. Merely densifying the list of pointwise frequencies cannot help: XF-056 already supplies the continuum, and (9) is uniform over that continuum.

## 6. Stress tests and evidence boundary

The construction reduces to the coherent-wave intuition only when the chirp curvature tends to zero much faster than `q^{-3}`. At the chosen curvature `b/q^3`, the phase changes by `Theta(1)` beyond its linear extrapolation across the `M=q^2` envelope and the local frequency sweeps by `Theta(1/q)`. This is exactly large enough to spread the response across `Theta(q)` resolution cells while keeping every local wavelength at the slow Cauchy scale.

Taking `b=0` removes the obstruction: the quadratic exponential-sum gain disappears, the configuration becomes a pure wave, and the selector centered at `a_0/q` recovers the order-one response of XF-056. Thus the vanishing in (9) is genuinely caused by slow phase drift rather than by a normalization mistake or by shrinking the critical amplitude.

The result is static. It does not prove that the chirp survives a fixed interval of the exact nonlinear Xi zero flow, does not control collisions, and does not produce an upper or lower bound for `Lambda`. A future dynamic theorem could still rule out the chirp even though the endpoint pointwise selector family alone cannot. Conversely, any proposed dynamic bridge should be stress-tested on a localized or evolving analogue of (4), because all of its instantaneous frequencies lie in the sector where the Cauchy heat clock is only order one rather than vanishingly fast.

## 7. Prior-art and novelty boundary

Quadratic chirps, stationary-phase spreading, and van der Corput estimates for exponential sums are classical. The load-bearing bound (14) is the standard second-derivative test; a durable bibliographic anchor is S. W. Graham and G. Kolesnik, *Van der Corput's Method of Exponential Sums*, London Mathematical Society Lecture Note Series 126, Cambridge University Press (1991), DOI `10.1017/CBO9780511661976`.

A targeted audit of de Bruijn--Newman zero dynamics, Rodgers--Tao's local-equilibrium argument, the Polymath15 upper-bound framework, and Fourier/explicit-formula formulations did not locate this scale-coupled chirped matched control or an inverse theorem that would invalidate it. No novelty is claimed for the exponential-sum estimate or for the generic fact that chirps spread Fourier mass. The line-specific mathematical delta is the simultaneous scale match

\[
\text{gap amplitude }M^{-1},
\qquad
\text{local frequency }q^{-1},
\qquad
\text{chirp curvature }q^{-3},
\qquad
M=q^2,
\tag{42}
\]

which yields both the uniform XF-056-type blindness (9) and the nonvanishing transition-side flux (12).

## 8. Consequence for `xi_flow`

The source-selector program has now crossed a useful boundary. XF-054--XF-056 show that the Xi source excludes every coherent critical slow mode, even continuously detuned ones, throughout a fixed heat interval. XF-057 shows that **coherent-mode exclusion is not yet coercivity**: a critical shape budget can be spread over a slowly varying phase so that all narrow pointwise coefficients vanish.

The next source-to-transition theorem should therefore not spend effort on denser frequency sampling. The decisive question is whether the exact Xi carrier controls an aggregate/time-frequency quantity strong enough to dominate the triple-flux budget, or whether the heat dynamics themselves forbid the chirped concentration pattern. Until one of those stronger bridges is proved, `sup_\theta o(1)` is insufficient to close the `M V_M=o(1)` gate.