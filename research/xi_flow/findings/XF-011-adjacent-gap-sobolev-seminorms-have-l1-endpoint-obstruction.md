# XF-011 — adjacent-gap Sobolev seminorms are scale-matched Lyapunovs with an `L^1` endpoint obstruction

**Status:** `EXACT-DERIVED` + `LITERATURE-CALIBRATED` + `NEGATIVE/OBSTRUCTION` at the `p=1` endpoint. XF-010 showed that a smooth translation-averaged fixed-radius observable has only an `h^4 kappa^2` generic phase response, whereas the fixed-time Xi lattice flow is driven at `h^2 |kappa|`. The escape through nonsmooth local observables is real but has a sharp functional-analytic boundary: adjacent-gap `W^{1,p}` seminorms are exact Lyapunov quantities for the linearized lattice semigroup and, for every `1<p<infinity`, their continuum limit controls the Cauchy driver `|D|U` in `L^p`. At `p=1`, the raw observable reaches the desired `h^2` scale, but no uniform bound of `|| |D|U ||_1` by total variation is possible.

This creates a concrete precision/nonlocality tradeoff. A local `p`-moment with `p>1` really can control the nonlocal generator after the correct renormalization, but its raw translation average is only of size `h^{2p}`. The endpoint `p=1` is visible already at `h^2` but loses strong control of the Cauchy field.

## 1. Claim

Use the arithmetic-lattice gap linearization from XF-007. For a periodic relative gap perturbation `u=(u_j)` of period `N`,

\[
 u_j'
 =L_hu_j
 :=\frac{2}{h^2}\sum_{m\ne0}\frac{u_{j+m}-u_j}{m^2}.
\tag{1}
\]

For `1<=p<infinity`, define the adjacent-difference seminorm

\[
\mathcal V_{p,h}(u)
:=\left(\frac1N\sum_{j=0}^{N-1}|u_{j+1}-u_j|^p\right)^{1/p}.
\tag{2}
\]

Then the exact linearized semigroup satisfies

\[
\boxed{
\mathcal V_{p,h}(u(t))\le \mathcal V_{p,h}(u(0))
\qquad (t\ge0).
}
\tag{3}
\]

Thus every adjacent-gap `W^{1,p}` seminorm is a Lyapunov quantity for the linearized real-zero flow around arithmetic equilibrium.

Now take the fixed-time mesoscopic scaling of XF-008,

\[
\delta=h^2=\frac{2\pi}{N},
\qquad
u_j=U(\delta j),
\]

with smooth periodic `U`. Then

\[
\boxed{
\frac{\mathcal V_{p,h}(u)}{h^2}
\longrightarrow
\left(\frac1{2\pi}\int_0^{2\pi}|U'(X)|^p\,dX\right)^{1/p}.
}
\tag{4}
\]

For the limiting Cauchy equation

\[
\partial_tU=-2\pi|D_X|U,
\tag{5}
\]

the periodic Hilbert transform `\mathcal H` gives

\[
|D_X|U=\mathcal H\,U'.
\tag{6}
\]

By the classical M. Riesz theorem, for every fixed `1<p<infinity`,

\[
\boxed{
\| |D_X|U\|_{L^p}
\asymp_p
\|U'\|_{L^p}.
}
\tag{7}
\]

For `p=2` the two norms are equal. Therefore a **fixed-radius local difference statistic can control the norm of the nonlocal Cauchy driver** once it is aggregated nonlinearly and renormalized at the correct scale. The locality obstruction of XF-010 applies to the smooth raw finite-stencil expansion; it does not imply that every nonlinear local seminorm is blind to the fractional first-order scale.

The endpoint is different. There is no finite constant `C` such that

\[
\boxed{
\| |D_X|U\|_{L^1}
\le C\|U'\|_{L^1}
}
\tag{8}
\]

for all smooth periodic `U`. Hence total variation alone does not uniformly control the Cauchy driver even though it has exactly the desired `h^2` scaling.

## 2. Exact discrete contraction

Write

\[
a_m:=\frac{2}{h^2m^2}>0,
\qquad
A:=\sum_{m\ne0}a_m<\infty.
\]

Then

\[
L_h=\sum_{m\ne0}a_m(T_m-I),
\tag{9}
\]

where `T_m` is translation by `m` on the periodic index group. Since the total jump rate is finite,

\[
e^{tL_h}
=e^{-At}\exp\!\left(t\sum_{m\ne0}a_mT_m\right)
\tag{10}
\]

is convolution with a nonnegative probability kernel `K_t`: it is the compound-Poisson Markov semigroup whose jump rates are `a_m`.

Let `D=T_1-I`. Translation invariance gives `DL_h=L_hD`, hence

\[
Du(t)=K_t*Du(0).
\tag{11}
\]

Young's inequality for convolution with a probability kernel yields

\[
\|Du(t)\|_{\ell^p}\le\|Du(0)\|_{\ell^p}
\qquad(1\le p\le\infty),
\tag{12}
\]

which is exactly (3) after the harmless periodic normalization. No continuum approximation is used in this Lyapunov statement.

The same argument survives the `h->0` limit. The Cauchy semigroup from XF-008 is convolution with the positive mass-one kernel

\[
P_t(X)=\frac{2t}{X^2+4\pi^2t^2},
\]

periodized on the torus when needed. Spatial differentiation commutes with convolution, so

\[
\|\partial_XU(t)\|_{L^p}
\le
\|\partial_XU(0)\|_{L^p}.
\tag{13}
\]

Thus the discrete and continuum seminorms have the same contraction mechanism.

## 3. Mesoscopic scale and the cosine test

Equation (4) follows from

\[
U(X+\delta)-U(X)=\delta U'(X)+O(\delta^2),
\qquad \delta=h^2,
\]

followed by the periodic Riemann-sum limit. For normalized gaps

\[
\frac{g_j}{h}=1+\varepsilon u_j,
\]

the corresponding observable simply gains a factor `|epsilon|`.

For a single mesoscopic mode

\[
U_k(X)=a\cos(kX),
\]

one obtains

\[
\frac{\mathcal V_{p,h}(U_k)}{h^2}
\longrightarrow
|a|\,|k|
\left(\frac1{2\pi}\int_0^{2\pi}|\sin X|^p\,dX\right)^{1/p}.
\tag{14}
\]

The frequency homogeneity is `|k|`, exactly the homogeneity of the Cauchy generator. Moreover XF-008 gives the **finite-`h`** eigenvalue

\[
\lambda_h(k)
=-2\pi|k|+h^2k^2,
\tag{15}
\]

for fixed `k` in the principal Brillouin regime, so the pure-mode seminorm evolves exactly as

\[
\mathcal V_{p,h}(u_k(t))
=e^{\lambda_h(k)t}\mathcal V_{p,h}(u_k(0)).
\tag{16}
\]

For `p=1`, the raw translation average is therefore already `Theta(h^2|k|)`. For `p=2`, its **square** is `Theta(h^4k^2)`, precisely the smooth quadratic-gradient scale isolated by XF-010; taking the square root restores the first-order Sobolev scale but does not remove the need to know the raw second moment to `h^4` precision.

More generally, if

\[
M_{p,h}(u):=rac1N\sum_j|u_{j+1}-u_j|^p,
\]

then for a smooth mesoscopic field

\[
\boxed{
M_{p,h}(u)=h^{2p}
\frac1{2\pi}\int|U'|^p+o(h^{2p}).
}
\tag{17}
\]

At Xi height `T`, where `h_T\asymp1/\log T`, this raw local signal is `Theta(log^{-2p}T)`.

## 4. The `L^1` endpoint fails explicitly

The endpoint obstruction can be seen without appealing only to an abstract unboundedness theorem. On the circle let

\[
P_r(X)
=\frac{1-r^2}{1-2r\cos X+r^2}
=1+2\sum_{n\ge1}r^n\cos(nX),
\qquad 0<r<1,
\tag{18}
\]

be the Poisson kernel and let

\[
Q_r(X)
=2\sum_{n\ge1}r^n\sin(nX)
=\frac{2r\sin X}{1-2r\cos X+r^2}
\tag{19}
\]

be its conjugate kernel. Set

\[
U_r'(X):=P_r(X)-1.
\tag{20}
\]

The right-hand side has mean zero, so `U_r` is a smooth periodic function. Since `P_r>=0` and its mean is one,

\[
\frac1{2\pi}\int_0^{2\pi}|U_r'|\,dX
\le2.
\tag{21}
\]

On the other hand, Fourier multipliers give

\[
|D_X|U_r=\mathcal H U_r'=Q_r
\]

up to the immaterial sign convention for `\mathcal H`. Because `Q_r` has one sign on `(0,\pi)` and the opposite sign on `(\pi,2\pi)`, direct integration gives

\[
\boxed{
\frac1{2\pi}\int_0^{2\pi}|Q_r(X)|\,dX
=
\frac{2}{\pi}\log\!\frac{1+r}{1-r}
\longrightarrow\infty
\qquad(r\uparrow1).
}
\tag{22}
\]

Thus the ratio between the `L^1` Cauchy-driver norm and total variation can be arbitrarily large even for smooth periodic profiles. Pure Fourier modes conceal this endpoint failure because for one mode both quantities scale with the same `|k|`; multimode concentration exposes the nonlocal Hilbert-transform amplification.

## 5. What this changes relative to XF-009 and XF-010

XF-009 correctly shows that leading fixed-radius value statistics lose mesoscopic ordering. XF-010 correctly shows that a **smooth raw** translation-averaged finite-stencil functional has an analytic long-wave expansion whose first generic phase term is `h^4k^2`. The present result identifies the precise escape hatch rather than merely noting that nonsmooth observables might behave differently.

A local adjacent difference followed by a nonlinear `L^p` aggregation is not a linear finite-stencil symbol. Its `p`th-root seminorm has first-order spatial homogeneity and is an exact contraction for the linearized lattice semigroup. For `1<p<infinity`, the M. Riesz theorem then converts that local derivative norm into a norm of the genuinely nonlocal generator.

But this does **not** make the observation problem disappear. The analytic object naturally presented to a zero-statistics theorem is usually the raw moment `M_{p,h}`, whose signal is only `h^{2p}`. Hence there is a sharp tradeoff:

- at `p=1`, the raw statistic appears at the desired `h^2=Theta(log^{-2}T)` scale but does not strongly control `|D|U`;
- at any fixed `p>1`, the Cauchy driver is controlled in `L^p`, but the raw local moment lies at the finer `h^{2p}=Theta(log^{-2p}T)` scale;
- `p=2` is the cleanest functional-analytic case, with exact Hilbert-transform isometry, but it demands the `log^{-4}T` precision already diagnosed by XF-010.

The endpoint degeneration therefore explains why “use an absolute adjacent-gap difference” is not by itself a complete escape from the local/nonlocal mismatch.

## 6. Matched-control and nonlinear boundary

Equation (3) is universal for the arithmetic-lattice linearization. It depends only on the positive long-range jump rates of the same zero-motion operator and is shared by matched real-entire or polynomial controls. It is therefore **not an Xi-specific selector and cannot by itself upper-bound `Lambda`**.

The statement is also linearized. Nothing here proves that an analogous `W^{1,p}` gap seminorm is monotone for the full nonlinear zero ODE, especially near a large defect or collision where the perturbative lattice description fails. Attempting to use (3) beyond that regime would require a separate nonlinear estimate.

Finally, the gap statistic itself presupposes an ordered real-zero configuration. Under a hypothetical positive `Lambda`, one cannot simply import an ordered-gap theorem at a time where real-rootedness is what must be proved. Any arithmetic input must be attached at a real-rooted time or rewritten in a configuration-level form that remains meaningful with off-line zeros.

## 7. Prior art and novelty boundary

Rodgers--Tao remain the primary source for the real-simple zero ODE and arithmetic-progression local equilibrium. Ciaurri--Roncal--Stinga--Torrea--Varona provide the neighboring discrete nonlocal-diffusion framework already anchored in `SOURCES.md`. The contraction of `L^p` norms under positive convolution semigroups is classical, as is the M. Riesz boundedness theorem for the periodic Hilbert transform on `1<p<infinity`.

No novelty is claimed for Markov-semigroup contraction, Sobolev seminorms, the Hilbert-transform identity `|D|=\mathcal H\partial_X`, the Poisson/conjugate-Poisson kernels, or the failure of strong `L^1` Hilbert-transform boundedness. The Mathia-specific contribution is the exact scale bridge: the adjacent normalized-gap `W^{1,p}` seminorm is an exact Lyapunov for the **Xi lattice linearization**, converges after division by `h^2` to a first-order Sobolev seminorm on the `X=h^2j` fixed-time coordinate, and exposes a quantitative `p=1` versus `p>1` tradeoff that sits exactly between XF-008's `h^2|D|` driver and XF-010's `h^4` smooth local response.

## 8. Consequence for `xi_flow`

The local-versus-nonlocal obstruction is now narrower. A fixed-radius statistic is not doomed merely because the limiting flow has a fractional symbol: **nonlinear adjacent-difference norms can be scale-matched and can control the Cauchy generator for `p>1`**. What remains hard is obtaining them from unconditional zero information at the required shrinking precision and without assuming the ordered real configuration that the Xi-flow argument is trying to establish.

This suggests a concrete upstream target rather than a generic request for “mesoscopic statistics”: look for a real-rootedness-safe estimate whose effective continuum content is a `W^{1,p}`-type mesoscopic bound, and quantify the tradeoff between the raw signal `h^{2p}` and the Hilbert-transform constant as `p` approaches one. If no such estimate can be made meaningful off the critical line, the statistical route still fails at the information-interface stage rather than at the linearized dynamics.