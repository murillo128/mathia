# XF-044 — the Cauchy slow mode imposes a logarithmic precision clock at memory scale

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `SHARP-LINEARIZED-OBSTRUCTION` + `STRUCTURAL/THRESHOLD`. XF-041 proves a nonlinear upper bound for periodic gap relaxation, XF-042 turns finite-window relaxation into an input-to-state estimate, and XF-043 shows that a super-mesoscopic physical buffer reduces the remote-tail contribution to a relative shape floor `O(1/R(T))` on a memory-scale core. There is a sharp obstruction to closing the remaining precision gap merely by waiting for more universal Cauchy smoothing.

At the arithmetic `q`-periodic gap lattice of mean spacing `s`, the exact periodic nonlinear gap flow has slowest nonconstant linear mode

\[
\boxed{
\rho_{q,s}
=\frac{4\pi^2(q-1)}{q^2s^2}.
}
\tag{1}
\]

Thus the amplitude exponent in XF-041 is locally sharp for **every** period `q`, not only for the two-gap endpoint. If `\Phi_\tau` denotes the exact `q`-periodic gap flow and `g_*=s\mathbf 1`, then for a slow Fourier mode `v`,

\[
\boxed{
D\Phi_\tau(g_*)v
=e^{-\rho_{q,s}\tau}v.
}
\tag{2}
\]

Consequently any contraction estimate that is uniform in a neighborhood of the lattice must have local multiplicative factor at least `e^{-rho_{q,s} tau}`. This is an exact derivative-of-flow obstruction: no alternative Lyapunov norm or nonlinear coercivity estimate based only on the universal periodic gap dynamics can force all sufficiently small perturbations to contract faster than the slow Fourier mode.

At Xi source spacing

\[
s=h_T\sim\frac{4\pi}{\log T},
\tag{3}
\]

and memory period

\[
q\sim c\log^2T,
\qquad c>0,
\tag{4}
\]

one has

\[
\boxed{
\rho_{q,s}
=\frac1{4c}+o(1).
}
\tag{5}
\]

Hence every fixed positive heat-time interval gives only a fixed-factor local contraction at the memory scale. It cannot supply a multiplicative gain tending to zero with `T`.

This becomes decisive when matched to the exact XF-035 triple-flux threshold. On a `q`-periodic slow sinusoidal gap perturbation

\[
g_j=s\left(1+\varepsilon\cos\frac{2\pi j}{q}\right),
\qquad |\varepsilon|\ll1,
\tag{6}
\]

repeat the pattern across a source block of `2M` gaps, with `q` dividing `2M`. Let

\[
d_j=\log\frac{g_{j+1}}{g_j},
\qquad
\phi_j=F'(d_j),
\qquad
V_M=\sum_{j=0}^{2M-3}|\phi_{j+1}-\phi_j|
\tag{7}
\]

as in XF-030/XF-035. Then

\[
\boxed{
\lim_{\varepsilon\to0}
\frac{V_M}{|\varepsilon|}
=
\left(\frac{2M}{q}+O(1)\right)
6\sin^2\!\left(\frac\pi q\right)
\sum_{j=0}^{q-1}\left|\cos\frac{2\pi j}{q}\right|.
}
\tag{8}
\]

Since

\[
\sum_{j=0}^{q-1}\left|\cos\frac{2\pi j}{q}\right|
=\frac{2q}{\pi}+O(1),
\tag{9}
\]

the exact linear-response coefficient

\[
\mathcal L_{M,q}
:=
\lim_{\varepsilon\to0}
\frac{M V_M}{|\varepsilon|}
\tag{10}
\]

satisfies

\[
\boxed{
\mathcal L_{M,q}
=
24\pi\left(\frac{M}{q}\right)^2
\left(1+O\!\left(\frac1q\right)
+O\!\left(\frac qM\right)\right).
}
\tag{11}
\]

For the source scale `M=R(T)\log^2T` and memory wavelength `q\asymp\log^2T`, equation (11) says that the **borderline** inverse-buffer scale `M V_M=O(1)` corresponds in tangent response to

\[
\boxed{
|\varepsilon|=O(R(T)^{-2}),
}
\tag{12}
\]

while the positive XF-035 stability gate `M V_M=o(1)` requires `|epsilon|=o(R(T)^-2)` along this slow family.

By contrast, XF-043 suppresses the **remote** tail only to the natural relative-shape scale `O(R(T)^{-1})` on such a memory core. Thus a proof strategy that reaches an `O(1/R)` unresolved memory-scale mode and then relies on universal Cauchy relaxation still needs an additional multiplicative gain of order `1/R` merely to reach the borderline flux scale, and a slightly stronger gain to enter the `o(1)` stability gate.

The sharp local clock (1) shows that obtaining such a factor uniformly requires at least

\[
\boxed{
\tau_{\rm precision}
\ge
\rho_{q,s}^{-1}\log R(T)+O(1).
}
\tag{13}
\]

At `q\sim c\log^2T`, this becomes

\[
\boxed{
\tau_{\rm precision}
\ge
(4c+o(1))\log R(T),
}
\tag{14}
\]

which diverges because `R(T)\to\infty`. A fixed real-rooted heat-time interval therefore cannot close this precision gap by source-free memory-scale relaxation alone.

This is not a statement that Xi actually realizes the slow sinusoidal perturbation or that the `O(1/R)` upper floor of XF-043 is attained. It is a sharp falsification of one possible bootstrap: **far-tail suppression to `O(1/R)` plus bounded-time universal Cauchy damping is not, by itself, a route even to the borderline inverse-buffer triple-flux scale at memory wavelength.** Closing the argument requires additional Xi-specific information that suppresses the slow modes, a stronger near-buffer cancellation that lands below the `R^-2` scale, or a different flux organization that avoids paying this precision clock.

## 1. Linearizing the exact periodic gap flow

Use the exact `q`-periodic quotient system from XF-041,

\[
g_i'
=2\sum_{\substack{0\le j<q\\j\ne i}}
C_{ij}(g_j-g_i),
\tag{15}
\]

where the period mean `s` is conserved. At the arithmetic lattice

\[
g_*=s\mathbf1,
\tag{16}
\]

the underlying positions are `x_i=is` up to translation, and the periodized conductances are exactly

\[
C_{ij}^{*}
=\frac1{s^2}
\sum_{n\in\mathbb Z}
\frac1{(i-j+nq)^2}
=
\frac{\pi^2}{q^2s^2}
\csc^2\!\left(\frac{\pi(i-j)}q\right).
\tag{17}
\]

When (15) is differentiated at `g_*`, derivatives of the conductances do not contribute: every such derivative is multiplied by `g_j-g_i=0`. Therefore the Jacobian is exactly the fixed periodized Cauchy Laplacian

\[
\boxed{
(D\mathcal V(g_*)u)_i
=2\sum_{j\ne i}C_{ij}^{*}(u_j-u_i).
}
\tag{18}
\]

For the Fourier mode

\[
u_i^{(\ell)}=e^{2\pi i\ell i/q},
\qquad 1\le\ell\le q-1,
\tag{19}
\]

the finite identity already derived in XF-041 gives

\[
\sum_{r=1}^{q-1}
\frac{\pi^2}{q^2}
\csc^2\!\left(\frac{\pi r}{q}\right)
\left(1-\cos\frac{2\pi\ell r}{q}\right)
=\frac{2\pi^2}{q^2}\ell(q-\ell).
\tag{20}
\]

Hence

\[
\boxed{
D\mathcal V(g_*)u^{(\ell)}
=-\rho_{q,s}^{(\ell)}u^{(\ell)},
\qquad
\rho_{q,s}^{(\ell)}
=\frac{4\pi^2}{q^2s^2}\ell(q-\ell).
}
\tag{21}
\]

The smallest positive rate occurs at `ell=1` or `q-1` and is exactly (1). Because the finite quotient ODE is smooth on the positive-gap simplex, differentiating its flow map gives (2).

Thus the nonlinear amplitude estimate in XF-041,

\[
A(\tau)
\lesssim
A(0)e^{-\rho_{q,s}\tau}
\tag{22}
\]

when `b_0/s\to1`, has the correct local exponent for every `q`. The Cauchy gap is not merely a convenient coercive lower bound; it is the actual slow tangent direction of the exact nonlinear flow.

## 2. A local sharpness statement independent of the chosen norm

Let

\[
v_i=\cos\frac{2\pi i}{q}
\tag{23}
\]

and initialize

\[
g_i(0)=s(1+\varepsilon v_i),
\qquad |\varepsilon|<1.
\tag{24}
\]

For every fixed `q,s,tau`, smooth dependence on initial data and (2) imply

\[
\boxed{
\frac{g_i(\tau)-s}{s}
=\varepsilon e^{-\rho_{q,s}\tau}v_i
+o(\varepsilon)
\qquad(\varepsilon\to0),
}
\tag{25}
\]

uniformly in the finite index set. Therefore, in either `ell^2`, `ell^infinity`, or any fixed norm on the zero-mean period space,

\[
\boxed{
\lim_{\varepsilon\to0}
\frac{\|g(\tau)-s\mathbf1\|}
{\|g(0)-s\mathbf1\|}
=e^{-\rho_{q,s}\tau}.
}
\tag{26}
\]

In particular, suppose a proposed universal estimate on the periodic nonlinear gap flow has, in some neighborhood of the lattice,

\[
\|g(\tau)-s\mathbf1\|
\le
\kappa_{q,s}(\tau)
\|g(0)-s\mathbf1\|.
\tag{27}
\]

Then necessarily

\[
\boxed{
\kappa_{q,s}(\tau)
\ge e^{-\rho_{q,s}\tau}.
}
\tag{28}
\]

This is the exact sense in which (1) is a lower bound on **how fast a uniform proof can force contraction**, not only an upper bound obtained from one particular energy.

## 3. The memory-scale rate remains order one

Insert the Xi source spacing (3) into (1):

\[
\rho_{q,s}
=
\frac{\log^2T}{4q}
\left(1-\frac1q\right)
(1+o(1)).
\tag{29}
\]

Hence a period `q=c\log^2T(1+o(1))` has (5). More generally, obtaining a multiplicative improvement by a factor `R(T)` from the universal local flow requires

\[
\rho_{q,s}\tau
\ge\log R(T)+O(1),
\tag{30}
\]

so

\[
\boxed{
\tau
\ge
\left(4+o(1)\right)
\frac{q\log R(T)}{\log^2T}.
}
\tag{31}
\]

This produces a precision-adjusted scale separator. A factor-`R` improvement can occur in vanishing heat time by this mechanism only when

\[
q\log R(T)=o(\log^2T).
\tag{32}
\]

At the full memory wavelength `q\asymp\log^2T`, the required time diverges like `log R`. The distinction is sharper than asking whether a mode merely loses a fixed fraction of its amplitude: fixed-factor memory and inverse-buffer precision live on different clocks.

## 4. The slow mode has an explicit triple-flux linear response

For the sinusoidal profile (6), set

\[
v_j=\cos\frac{2\pi j}{q}.
\tag{33}
\]

The logarithmic contrast satisfies

\[
d_j
=\varepsilon(v_{j+1}-v_j)+O(\varepsilon^2)
\tag{34}
\]

for fixed `q`. XF-030 gives the exact odd flux law with

\[
F'(d)=-\frac32d+O(d^3).
\tag{35}
\]

Therefore

\[
\phi_{j+1}-\phi_j
=-\frac32\varepsilon
(v_{j+2}-2v_{j+1}+v_j)
+O(\varepsilon^2).
\tag{36}
\]

The second difference is explicit:

\[
v_{j+2}-2v_{j+1}+v_j
=-4\sin^2\!\left(\frac\pi q\right)
\cos\!\left(\frac{2\pi(j+1)}q\right).
\tag{37}
\]

Summing absolute values over one full period gives

\[
\boxed{
\lim_{\varepsilon\to0}
\frac1{|\varepsilon|}
\sum_{j=0}^{q-1}|\phi_{j+1}-\phi_j|
=
6\sin^2\!\left(\frac\pi q\right)
C_q,
}
\tag{38}
\]

where

\[
C_q:=\sum_{j=0}^{q-1}
\left|\cos\frac{2\pi j}{q}\right|.
\tag{39}
\]

A Riemann sum gives

\[
C_q=\frac{2q}{\pi}+O(1),
\tag{40}
\]

and hence

\[
\boxed{
6\sin^2\!\left(\frac\pi q\right)C_q
=\frac{12\pi}{q}+O(q^{-2}).
}
\tag{41}
\]

Now repeat the period across `2M` gaps. The omission of at most two endpoint second differences changes the linear coefficient by only `O(q/M)` relatively after multiplication by `M`. Combining (38)--(41) gives the exact tangent coefficient (11).

The relevant point is the scale

\[
\boxed{
\mathcal L_{M,q}
\asymp
\left(\frac{M}{q}\right)^2.
}
\tag{42}
\]

This calculation is important because a long-wave mode is much cheaper in flux variation than the alternating microcorrugation of XF-039: two discrete derivatives appear before `V_M` is formed. Even after crediting that extra smoothness exactly, however, a memory-scale mode repeated across a super-mesoscopic source buffer has borderline flux amplitude `R^-2`, one factor `R` below the natural `R^-1` remote-floor scale of XF-043.

## 5. The XF-043 floor and the XF-035 threshold are separated by one factor of `R`

Take a memory core with

\[
q\asymp N\asymp\log^2T
\tag{43}
\]

and a source-valid physical buffer

\[
D=R(T)\log T.
\tag{44}
\]

With `s\asymp1/\log T`, XF-043 gives the remote-tail relative-shape floor

\[
A_{\rm far}\ll\frac{Ns}{D}
\asymp\frac1{R(T)}.
\tag{45}
\]

The same physical buffer contains

\[
M\asymp R(T)\log^2T
\tag{46}
\]

gaps at source density, so `M/q\asymp R(T)`. Equation (11) becomes

\[
\boxed{
\mathcal L_{M,q}\asymp R(T)^2.
}
\tag{47}
\]

Thus, in linear response, an unresolved slow-mode amplitude parameter of scale `|epsilon|\asymp1/R` lies a factor `R` above the borderline `M V_M=O(1)` scale, while the positive XF-035 gate requires moving slightly below that borderline to `o(R^-2)`.

Equation (45) is only an **upper bound** on what the remote tail can sustain. The finding does not assert that Xi has a residual of size `1/R`, nor does the tangent calculation assert a uniform finite-amplitude expansion for a simultaneous limit `epsilon=1/R(T)` without an additional nonlinear remainder estimate. The conclusion is instead about proof architecture: if a multiscale estimate leaves an unresolved memory-scale component at the natural `1/R` level and then asks for an amplitude-uniform bounded-time contraction theorem, the required extra factor `R` is ruled out by (28)--(31).

## 6. The same slow clock applies directly to the flux functional

The obstruction is not an artifact of measuring gap amplitude first and then converting it to flux. Combining the flow expansion (25) with the linear flux expansion (36) gives, for every fixed `q,s,M,tau`,

\[
\boxed{
\lim_{\varepsilon\to0}
\frac{V_M(\tau;\varepsilon)}
{V_M(0;\varepsilon)}
=e^{-\rho_{q,s}\tau}.
}
\tag{48}
\]

Therefore any near-lattice estimate that tries to contract `V_M` itself uniformly inherits the same lower bound (28). Changing from variance to the exact triple-discriminant flux does not remove the long-wave spectral clock at first order.

This is a useful separation from XF-039. Microscopic alternating flux variation is killed rapidly because its Fourier frequency is high. The present obstruction sits at the opposite end of the spectrum: its adjacent contrasts are tiny and its flux variation is correspondingly cheap, but the mode relaxes only on the memory-scale Cauchy clock.

## 7. Stress tests and hard boundary

The theorem is a **local linearized sharpness result** for the exact nonlinear periodic flow. It does not claim that a finite-amplitude sinusoidal profile remains a pure Fourier mode for times growing like `log R`; nonlinear mode coupling can matter on such intervals. Equation (14) is therefore a necessary clock for a contraction theorem uniform near the lattice, not a standalone nonlinear lower bound for one prescribed finite-amplitude trajectory over a growing time horizon.

That limitation does not affect the bounded-time obstruction. Equations (26), (28), and (48) already show that on every fixed heat interval the best uniform local contraction factor at `q\asymp\log^2T` stays bounded away from zero. A proof requiring a factor `1/R(T)\to0` cannot come from the universal tangent dynamics alone.

The mode is a periodic synthetic control, not a claim about actual Xi zero statistics. It satisfies the same exact universal gap dynamics used in XF-041 but does not encode the arithmetic source, translated zeta-zero correlations, or a de Bruijn--Newman transition. Those are precisely the kinds of extra information that could exclude or weaken the slow mode and therefore evade the obstruction.

The result also does not contradict XF-041. That finding gives a nonlinear **upper** relaxation estimate; the present calculation identifies the tangent direction showing its exponential rate is sharp. Nor does it contradict XF-043: far-tail suppression remains valid and useful, but its `O(1/R)` scale is not automatically the final precision scale required by XF-035.

Finally, the conclusion is specific to proof mechanisms that need the XF-035 inverse-buffer flux gate or an equivalent first-order flux control. A different source-specific identity that bypasses this gate could avoid the `R^-2` tangent target entirely.

## 8. Prior art and consequence for `xi_flow`

Fourier diagonalization of circulant inverse-square kernels, spectral relaxation of long-range random walks, and the general fact that a linearized slow eigenmode lower-bounds uniform local contraction are classical. The broader contraction mechanism for ordered one-dimensional logarithmic repulsion is already bounded in `SOURCES.md` by Guillin--Le Bris--Monmarche, and the nonlocal Cauchy scaling is already calibrated there by the discrete fractional-diffusion literature. No new external theorem is load-bearing, and no bibliographic novelty claim is made for the spectrum or for linearized semigroup sharpness.

The Mathia-local content is the scale matching that was not available before XF-043: the exact slow tangent mode of XF-041, the exact triple-flux linearization of XF-030/XF-035, the memory scale `q\asymp\log^2T`, and the super-mesoscopic far-tail floor `O(1/R)` together force the logarithmic precision clock (13)--(14).

The next positive gate is therefore sharper than “iterate the buffer until the exterior is small.” A successful continuation must do at least one of the following: use Xi-specific source information to rule out or quantitatively suppress wavelengths `q\gtrsim\log^2T/\log R`; prove a near-buffer cancellation whose memory-scale residual is already `o(R^-2)` in the relevant flux coordinate; or find a different source-sensitive carrier that does not require the XF-035 inverse-buffer flux threshold. Merely combining XF-043 with more bounded-time universal Cauchy damping cannot close the remaining precision gap.