# XF-059 — moving-line selector reaches the source-compatible infrared flux threshold

**Status:** `EXACT-DERIVED` + `UNIFORM-INFRARED-EXTENSION` + `SOURCE-SPECIFIC-TRANSPORT` + `MATCHED-CONTROL`. XF-056 proves that the Xi moving-line selector is uniform on the continuous memory cone `theta >= c/q`, and XF-058 shows that the normalized `L^2` aggregate over that cone survives the chirped control that defeats pointwise-frequency coercivity. Both findings deliberately leave `theta=o(1/q)` open.

The lower edge `c/q` is not a limit of the Xi moving-line argument. The same proof reaches to any fixed power above the selector resolution scale `1/M`. More precisely, with

\[
q\asymp\log^2T,\qquad
M=q^2,\qquad
\sigma_T=\frac{4\pi}{\log(T/4\pi)},\qquad
W=M\sigma_T,
\tag{1}
\]

fix `0<delta<1`, `C>0`, and define

\[
\Theta_{T,\delta}
:=
\left[
q^{-2+\delta},
\frac{C\log\log T}{q}
\right].
\tag{2}
\]

For the exact XF-056 probe `f_{T,theta}` and Xi carrier statistic `\mathcal S_{T,\theta}(t)`, every fixed `t_0>0` and every fixed `B>0` satisfy

\[
\boxed{
\sup_{0\le t\le t_0}
\sup_{\theta\in\Theta_{T,\delta}}
|\mathcal S_{T,\theta}(t)|
=
O_{B,\delta,C,t_0}\bigl((\log T)^{-B}\bigr).
}
\tag{3}
\]

Consequently the enlarged normalized square function

\[
\mathfrak E_{T,\delta}^{\Xi}(t)
:=
M\int_{\Theta_{T,\delta}}
|\mathcal S_{T,\theta}(t)|^2\,d\theta
\tag{4}
\]

still obeys

\[
\boxed{
\sup_{0\le t\le t_0}
\mathfrak E_{T,\delta}^{\Xi}(t)=o(1).
}
\tag{5}
\]

This extension reaches below the natural infrared scale of a source-compatible pure mode carrying critical triple-flux variation. If

\[
q^{-4/3}\ll\theta_T\ll q^{-1},
\tag{6}
\]

then there is an ordered sinusoidal matched control whose translated span error is `o(1)` in index units and whose triple-flux variation satisfies

\[
\boxed{
M V_M\longrightarrow\frac{6\kappa}{\pi}>0,
}
\tag{7}
\]

but the selector at its own center has magnitude

\[
\boxed{
\left|
\sum_j f_{T,\theta_T}(z_j)
\right|
=
\frac{\kappa}{2M\theta_T^2}(1+o(1))
\longrightarrow\infty.
}
\tag{8}
\]

Thus the ultraslow **pure-mode** loophole left by XF-056 is not a genuine source-side escape: the Xi selector can be pushed far enough into the infrared to see every such critical mode while remaining prime-free and rapidly small on the actual Xi carrier. The open problem after XF-058 remains an aggregate inverse theorem for arbitrary transition geometry, not a lower-frequency obstruction at wavelength just beyond `q`.

## 1. The moving-line proof only needs `M theta` to be a fixed power of `q`

Keep the XF-056 test function

\[
f_{T,\theta}(x)
=
g\!\left(\frac{x-T}{W}\right)
e^{-i(\omega_{\theta,T}(x-T)+\varphi_{\theta,T})},
\qquad
\omega_{\theta,T}=\frac{\theta}{\sigma_T},
\tag{9}
\]

with `\widehat g\in C_c^\infty((-1,1))`. Its positive-frequency band has physical half-width `W^{-1}`. The exact scale product is

\[
W\omega_{\theta,T}=M\theta.
\tag{10}
\]

At the new lower edge (2),

\[
M\theta\ge q^\delta\longrightarrow\infty.
\tag{11}
\]

Hence the band remains strictly separated from frequency zero by many support widths. The upper edge is unchanged from XF-056, so the whole band also remains below the first Guinand--Weil prime-power frequency `\log 2/2`. The endpoint support argument is therefore still exactly prime-free.

The moving high line is also unchanged:

\[
a_T=A\log T.
\tag{12}
\]

The factor `e^{a_T\omega_{\theta,T}}` is largest at the upper edge of the cone, so lowering the lower edge cannot worsen the polylogarithmic height cost in XF-056. The reflected Euler-product contribution is still a fixed negative power of `T` times a fixed polylogarithm and therefore beats every prescribed negative power of `\log T`.

For the deterministic archimedean background, the XF-056 `N`-fold integration-by-parts estimate has worst term

\[
O_N\!\left(
(\log T)^K
W(M\theta)^{-N}
\right).
\tag{13}
\]

Using (11), `q\asymp\log^2T`, and `W\asymp\log^3T` gives

\[
O_N\!\left(
(\log T)^{K+3-2\delta N}
\right).
\tag{14}
\]

Given any fixed `B`, choose one fixed `N` with `2\delta N>K+3+B`. Terms with derivatives on the deterministic background gain powers of `W/T`, and the physical tails are handled by the same fixed Schwartz powers as in XF-056. This proves (3). Since for `0<delta<1`

\[
M|\Theta_{T,\delta}|
=
O(q\log\log T),
\tag{15}
\]

equation (5) follows from (3) by taking `B` sufficiently large.

No new Xi input is used. The only change from XF-056/XF-058 is retaining the actual parameter `M theta` in the oscillatory estimate rather than replacing it immediately by the memory-cone lower bound `cq`.

## 2. Critical triple flux determines a natural infrared displacement threshold

Consider a pure sinusoidal gap perturbation at a frequency `theta=theta_T->0`. Put

\[
\varepsilon_T
:=
\frac{\kappa}{M^2\theta^2},
\qquad
A_T
:=
\frac{\varepsilon_T}{2\sin(\theta/2)},
\tag{16}
\]

and define

\[
\boxed{
z_j
=
T+\sigma_T\bigl(j+A_T\sin(\theta j+\phi)\bigr).
}
\tag{17}
\]

Then exactly

\[
\frac{z_{j+1}-z_j}{\sigma_T}
=
1+\varepsilon_T
\cos\!\left(\theta(j+\tfrac12)+\phi\right).
\tag{18}
\]

The critical-flux normalization in (16) is forced by two discrete derivatives: for a slowly varying gap wave, the XF-030 triple flux varies at scale `epsilon theta^2`, while `V_M` sums over `Theta(M)` triples and the stability quantity is `M V_M`. Thus `M^2 epsilon theta^2` is the invariant critical combination.

The root-displacement amplitude in index units is

\[
A_T
=
\frac{\kappa}{M^2\theta^3}(1+o(1)).
\tag{19}
\]

Therefore

\[
A_T=o(1)
\quad\Longleftrightarrow\quad
M^2\theta^3\longrightarrow\infty,
\tag{20}
\]

which at `M=q^2` is exactly

\[
\theta\gg q^{-4/3}.
\tag{21}
\]

This is the natural infrared threshold for a **pure critical-flux mode whose root positions remain an `o(1)` perturbation of the local source lattice**. It is not a threshold in the Xi equation itself; it is the scale at which the critical `M V_M` normalization and small source displacement meet.

The interval

\[
q^{-4/3}\ll\theta\ll q^{-1}
\tag{22}
\]

is nonempty. These modes are slower than the XF-056 memory cone but still oscillate many times across the `M`-site source window because

\[
M\theta\gg q^{2/3}\longrightarrow\infty.
\tag{23}
\]

For any translated span,

\[
\left|
(z_b-z_a)-\sigma_T(b-a)
\right|
\le 2\sigma_T A_T=o(\sigma_T).
\tag{24}
\]

Thus the control passes by a wide margin the local translated-span/counting precision consumed in XF-047: its normalized endpoint displacement is `o(1)`, the `M`-gap physical window still has width `W\asymp\log^3T=o(T)`, and the curvature of the smooth Riemann--von Mangoldt main term across that window remains `o(1)`. As with XF-047 and XF-057, this is finite-window source compatibility, not a claim that the infinite sinusoidal continuation is the Xi zero set.

## 3. The exact triple flux stays at the borderline scale

Let

\[
d_j
:=
\log\frac{z_{j+2}-z_{j+1}}{z_{j+1}-z_j},
\qquad
\phi_j:=F'(d_j),
\tag{25}
\]

where `F` is the exact XF-030 triple-discriminant shape function. XF-030 gives

\[
F'(d)=-\frac32d+O(d^3)
\qquad(d\to0).
\tag{26}
\]

From (18),

\[
d_j
=
-2\varepsilon_T\sin(\theta/2)
\sin(\theta(j+1)+\phi)
+
O(\varepsilon_T^2\theta)
\tag{27}
\]

uniformly in `j`. Since

\[
\frac{\varepsilon_T}{\theta}
=
\frac{\kappa}{M^2\theta^3}
=o(1)
\tag{28}
\]

by (20), equations (26)--(27) give

\[
\phi_{j+1}-\phi_j
=
6\varepsilon_T\sin^2(\theta/2)
\cos(\theta(j+\tfrac32)+\phi)
+
O(\varepsilon_T^2\theta).
\tag{29}
\]

Over `2M+O(1)` consecutive indices, (23) implies the elementary averaging law

\[
\sum
\left|
\cos(\theta(j+\tfrac32)+\phi)
\right|
=
\frac{4M}{\pi}
+
O(\theta^{-1}+1)
=
\frac{4M}{\pi}+o(M).
\tag{30}
\]

For the XF-035/XF-057 variation

\[
V_M
:=
\sum_{j=-M}^{M-3}
|\phi_{j+1}-\phi_j|,
\tag{31}
\]

equations (29)--(30) yield

\[
M V_M
=
\frac{24}{\pi}
M^2\varepsilon_T\sin^2(\theta/2)
+o(1).
\tag{32}
\]

The averaging error is `O((M\theta)^{-1})` after the critical normalization, while the nonlinear error contributes

\[
O(M^2\varepsilon_T^2\theta)
=
O\!\left(\frac{\kappa\varepsilon_T}{\theta}\right)
=o(1).
\tag{33}
\]

Finally,

\[
M^2\varepsilon_T\sin^2(\theta/2)
=
\kappa\frac{\sin^2(\theta/2)}{\theta^2}
\longrightarrow\frac{\kappa}{4},
\tag{34}
\]

which proves (7).

Thus an ultraslow pure wave can indeed carry the same borderline triple-flux budget as the memory-scale controls. What prevents it from being an obstruction is not the transition observable; it is the fact that the Xi source selector itself extends far enough downward to see it.

## 4. The matched infrared selector response is larger than order one

Take the same XF-056 probe (9) with center equal to the control frequency `theta` and choose its harmless phase to match (17). Because `M theta->infinity`, Poisson summation gives the exact lattice cancellations used in XF-056:

\[
\sum_j g(j/M)e^{-i\theta j}=0,
\qquad
\sum_j g(j/M)e^{-2i\theta j}=0,
\tag{35}
\]

and likewise for `g'`, for all sufficiently large `T`.

Repeating the XF-056 Taylor calculation with the general relative gap amplitude `epsilon_T` gives

\[
\left|
\sum_j f_{T,\theta}(z_j)
\right|
=
\frac{\varepsilon_T M}{2}
\frac{\theta}{2\sin(\theta/2)}
+
O(M\varepsilon_T^2).
\tag{36}
\]

Here the quadratic remainder has exactly the same scale as in XF-056; relative to the leading term it is `O(epsilon_T)=o(1)`. Hence

\[
\boxed{
\left|
\sum_j f_{T,\theta}(z_j)
\right|
=
\frac{\kappa}{2M\theta^2}(1+o(1)).
}
\tag{37}
\]

For the genuinely ultraslow regime `theta=o(1/q)`,

\[
M\theta^2=q^2\theta^2=o(1),
\tag{38}
\]

so (37) diverges. The critical mode is therefore not marginally visible: once the selector family is extended to its center, its response is parametrically larger than the order-one response of the `theta\asymp1/q` XF-056 control.

Choose now any fixed `0<delta<2/3`. The lower edge of (2) satisfies

\[
q^{-2+\delta}
=o(q^{-4/3}).
\tag{39}
\]

Therefore every frequency satisfying (6) eventually belongs to `\Theta_{T,\delta}`. Equations (3) and (37) then separate the actual Xi carrier from every source-compatible pure critical-flux wave in the entire sub-memory window (6).

## 5. The resolution floor, not the memory scale, is the source-side limit

The proof of (3) exposes the real lower-frequency parameter:

\[
M\theta.
\tag{40}
\]

The compact selector has index-frequency half-width `1/M`. The Xi moving-line method remains rapidly effective whenever the center is a fixed power of `q` support widths away from zero. For every fixed `delta>0`, the lower edge `q^{-2+delta}` is exactly `q^delta` support widths from the origin.

The scale `1/q` in XF-056 is therefore a **dynamical memory scale**, not a source-side Fourier barrier. The pure critical-flux source-compatibility threshold `q^{-4/3}` lies comfortably above the near-resolution range reachable by (3). In particular, widening the normalized square function below `1/q` does not require a new explicit formula, a new prime-free gap, or a new half-plane transport theorem.

This does not prove that the selector can be pushed uniformly all the way to `theta\asymp1/M`. At bounded `M theta`, the positive-frequency band touches the zero-frequency background and the integration-by-parts gain disappears. The finding only needs the fixed-power separation in (2), which already passes below the scale (21).

## 6. Stress tests and evidence boundary

The result is deliberately narrower than the missing source-to-transition inverse theorem. The control (17) is a matched sinusoidal zero configuration, not an asserted Xi zero block and not a positive-time Xi trajectory. Equation (3) is a source-side Xi statement about the exact carrier statistic; equation (7) is a transition-observable calculation on the matched control. Their comparison rules out a simple infrared pure-mode escape but does not identify arbitrary positive-time transition geometry with an endpoint zero sum.

The finding also does not prove a lower-frame inequality of the form `M V_M <= C E_{T,delta}` for an arbitrary gap field. Frequency spreading, sparse defects, cancellation among multiple low bands, moving physical localization, and nonlinear mixing remain possible. XF-057 already shows why pointwise control alone is insufficient, and XF-058 shows only that one canonical chirp survives `L^2` aggregation.

Conversely, the old square function restricted to `theta>=c/q` is not by itself coercive against a pure mode placed below `c/q`; the point here is that this is a removable choice of cone, not a limitation of the Xi estimate. The natural next aggregate should use the enlarged infrared family rather than freeze the XF-058 lower edge.

No upper bound on the de Bruijn--Newman constant follows from (3)--(8), and no claim is made that extending the cone is sufficient for RH.

## 7. Prior-art and novelty boundary

The load-bearing external inputs are unchanged from XF-050--XF-058: Guinand--Weil prime-frequency support, the Xi functional equation and Euler product on the reflected high line, Stirling-type deterministic background control, and the half-plane Fourier--Laplace carrier formalism. The new step is a scale audit of the existing moving-line proof plus the exact XF-030 triple-flux expansion.

A targeted audit of nonuniform/jittered sampling, Kadec-type perturbed-lattice stability, spectral effects of sampling jitter, de Bruijn--Newman heat-flow work, and Xi explicit-formula literature did not locate this line-specific scale match. No novelty is claimed for Poisson summation, perturbed-lattice sampling, or sinusoidal sidebands. The durable delta is the conjunction

\[
\theta_{\rm source}\ge q^{-2+\delta},
\qquad
\theta_{\rm critical}\gg q^{-4/3},
\qquad
M V_M\asymp1,
\tag{41}
\]

showing that the existing Xi transport reaches strictly below the infrared threshold of every small-displacement pure critical-flux control. No new external theorem is load-bearing, so `SOURCES.md` does not require modification.

## 8. Consequence for `xi_flow`

The `theta=o(1/q)` caveat in XF-056/XF-058 can now be sharpened. **Ultraslow pure modes are not the missing escape mechanism.** At the critical triple-flux scale, a pure mode remains source-compatible only above `theta>>q^{-4/3}`, while the exact Xi selector already extends uniformly to `theta=q^{-2+delta}` for every fixed `delta>0`.

The next constructive theorem should therefore enlarge the XF-058 square-function cone into this infrared range and attack aggregate coercivity there. A decisive positive result would control the transition-side `M V_M` by an infrared-extended selector/frame norm. A decisive negative would need a configuration whose critical flux survives while its **aggregate** energy vanishes even after frequencies down to `q^{-2+delta}` are included; merely moving a coherent wave to wavelength longer than `q` no longer suffices.
