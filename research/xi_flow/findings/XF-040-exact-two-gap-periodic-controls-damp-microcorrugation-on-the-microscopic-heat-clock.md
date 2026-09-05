# XF-040 — exact two-gap-periodic controls damp microcorrugation on the microscopic heat clock

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `STRUCTURAL/DYNAMIC` + `MATCHED-CONTROL`. XF-039 isolates an alternating microscopic corrugation that passes the translated Xi counting tests, has vanishing total logarithmic gap variation, and already lies in the XF-038 Cauchy-network regime while still violating the inverse-buffer requirement `M V_M=O(1)`. That obstruction is genuinely static. If the same alternating gap pattern is promoted to an exact even two-gap-periodic real-entire backward-heat control, its nonlinear amplitude is explicitly solvable and is driven into the `M V_M=O(1)` regime on a vanishing heat-time scale.

More precisely, let `L>0`, put
\[
\omega=\frac{2\pi}{L},
\]
and choose `delta in (pi/2,pi)`. The even real-entire family
\[
\boxed{
G_t(z)=\cos\delta-e^{\omega^2 t}\cos(\omega z)
}
\tag{1}
\]
solves the same backward heat equation
\[
\partial_tG_t=-\partial_z^2G_t.
\tag{2}
\]
Its zero set is entirely real exactly for
\[
\boxed{
t\ge\Lambda_G,
\qquad
\Lambda_G=\omega^{-2}\log|\cos\delta|<0.
}
\tag{3}
\]
For `t>Lambda_G`, the zeros form a spatially `L`-periodic lattice with two alternating positive gaps `a(t),b(t)`, `a+b=L`. Writing
\[
\tau(t):=\frac{a(t)-b(t)}{L}\in(0,1),
\tag{4}
\]
one obtains the exact nonlinear damping law
\[
\boxed{
\sin\!\left(\frac{\pi\tau(t)}2\right)
=e^{-\omega^2(t-t_0)}
\sin\!\left(\frac{\pi\tau(t_0)}2\right)
}
\tag{5}
\]
for any `t>=t_0>Lambda_G`, and equivalently
\[
\boxed{
\sin\!\left(\frac{\pi\tau(t)}2\right)
=e^{-\omega^2(t-\Lambda_G)}.
}
\tag{6}
\]
Thus the exact XF-039 alternating mode is not dynamically persistent in this matched control. Its small-amplitude decay rate is `omega^2`, which at mean Xi spacing `h_T~4pi/log T` is `~(log T)^2/16`.

This does **not** derive `V_M=O(1/M)` for a finite Xi zero block. A finite block is not globally two-periodic, its exterior roots can force the microscopic pattern, and `ell^1` flux variation can be repopulated by modulation and boundary transport. The durable conclusion is narrower but useful: XF-039 cannot be upgraded into a time-persistent matched-control obstruction by making its alternating corrugation globally periodic. Any negative continuation must exploit finite-window/exterior coupling or a slower mode, while a positive continuation can target a localized version of the exact high-frequency damping exhibited here.

## 1. The two-gap pattern is an exact backward-heat family

For real `t`, equation (1) has zeros determined by
\[
\cos(\omega z)=A_t,
\qquad
A_t:=e^{-\omega^2t}\cos\delta.
\tag{7}
\]
If `|A_t|<=1`, every solution is real: if `z=x+iy` and `cos(omega z)` is real with `y!=0`, then `sin(omega x)=0`, so its real value has absolute value `cosh(omega y)>1`. Conversely, if `|A_t|>1`, equation (7) has nonreal conjugate solutions. Hence all zeros are real iff `|A_t|<=1`, which is exactly (3). At `t=Lambda_G` the zeros are double; above it they are simple.

For `t>Lambda_G`, let `delta_t in (pi/2,pi)` be defined by
\[
\cos\delta_t=e^{-\omega^2t}\cos\delta.
\tag{8}
\]
Then the zeros are
\[
\boxed{
 z_{n,\pm}(t)=nL\pm\frac{\delta_t}{\omega},
 \qquad n\in\mathbb Z.
}
\tag{9}
\]
The two alternating gaps are therefore
\[
a(t)=\frac{2\delta_t}{\omega}=\frac{L\delta_t}{\pi},
\qquad
b(t)=L-a(t),
\tag{10}
\]
with mean spacing `s=L/2`. Equation (4) becomes
\[
\tau(t)=\frac{2\delta_t}{\pi}-1.
\tag{11}
\]
Since
\[
\cos\delta_t
=-\sin\!\left(\frac{\pi\tau(t)}2\right),
\tag{12}
\]
equations (8) and (12) give (5). At the transition, `A_{Lambda_G}=-1`, hence `tau=1` and the smaller gap has just collapsed. Expressing (5) relative to that collision time gives (6).

Differentiating (5) yields an exact autonomous amplitude equation,
\[
\boxed{
\tau'
=-\frac{2\omega^2}{\pi}
\tan\!\left(\frac{\pi\tau}{2}\right).
}
\tag{13}
\]
It has the correct sign at every finite amplitude: forward heat time strictly flattens the alternating gap disparity. The singularity as `tau->1` is the opening of the double collision at the transition, not a failure of the formula on the real-simple side.

The same law follows from the XF-014 zero ODE. On the two-sublattice zero set (9), same-sublattice principal values cancel and the cross-sublattice sum is the classical cotangent partial fraction. This gives
\[
a'=\frac{4\pi}{L}\cot\delta_t,
\tag{14}
\]
which is equivalent to (13). The direct backward-heat derivation above is stronger for the matched-control purpose because it also determines the exact real-zero transition time.

## 2. XF-039's flux-BV defect has an exact scalar amplitude here

At a fixed real-simple time write
\[
a=s(1+\tau),
\qquad
b=s(1-\tau),
\qquad
\epsilon:=\operatorname{artanh}\tau.
\tag{15}
\]
Then
\[
\frac ba=e^{-2\epsilon},
\tag{16}
\]
and the logarithmic contrasts alternate exactly between `-2epsilon` and `+2epsilon`. This is precisely the XF-039 microcorrugation, now extended through the whole real line rather than embedded only as a finite static block.

Let `phi=F'` be the normalized-triple contrast flux of XF-030. Substituting
\[
r=\frac{1-\tau}{1+\tau}
\]
into the exact formula
\[
\phi(r)
=-\frac{(r-1)(r+2)(2r+1)}{(r+1)(r^2+r+1)}
\]
gives the exact magnitude
\[
\boxed{
p(\tau):=|\phi|
=\frac{\tau(9-\tau^2)}{3+\tau^2}.
}
\tag{17}
\]
For `0<tau<1`,
\[
2\tau<p(\tau)<3\tau.
\tag{18}
\]
A consecutive sample of `2M` gaps therefore has exactly the XF-039 interior flux variation
\[
\boxed{
V_M(t)=4(M-1)p(\tau(t)).
}
\tag{19}
\]
Consequently, in this family,
\[
\boxed{
M V_M=O(1)
\quad\Longleftrightarrow\quad
\tau=O(M^{-2}).
}
\tag{20}
\]
The inverse-buffer threshold is not hidden in a norm comparison here: it is a scalar amplitude threshold.

## 3. The XF-039 counterexample amplitude reaches the BV threshold in vanishing time

Take the XF-039 scale
\[
\epsilon_M=M^{-1-\alpha},
\qquad 0<\alpha<1,
\tag{21}
\]
at some reference time `t_0`, so
\[
\tau_M(t_0)=\tanh\epsilon_M
=M^{-1-\alpha}(1+o(1)).
\tag{22}
\]
From the exact sine law (5), uniformly while the amplitude decreases from this already-small value,
\[
\tau_M(t_0+\Delta t)
=	au_M(t_0)e^{-\omega^2\Delta t}(1+o(1)).
\tag{23}
\]
Hence choosing
\[
\boxed{
\Delta t_M
=\frac{(1-\alpha)\log M+O(1)}{\omega^2}
}
\tag{24}
\]
forces `tau_M=O(M^-2)` and therefore `M V_M=O(1)` by (18)--(20).

Now place the control at the source mean spacing used in XF-039,
\[
s=h_T\sim\frac{4\pi}{\log T},
\qquad
L=2s.
\tag{25}
\]
Then
\[
\boxed{
\omega^2=\frac{4\pi^2}{L^2}
=\frac{\pi^2}{s^2}
\sim\frac{(\log T)^2}{16}.
}
\tag{26}
\]
For the super-mesoscopic source buffer
\[
M=R(T)\log^2T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T),
\tag{27}
\]
one has `log M=O(log T)`. Thus
\[
\boxed{
\Delta t_M
=\frac{16(1-\alpha)\log M+O(1)}{(\log T)^2}
=O(1/\log T)
\longrightarrow0.
}
\tag{28}
\]
The static family that makes `M V_M` diverge in XF-039 therefore crosses into the required inverse-buffer regime after a heat-time interval that vanishes at high source height when its exterior is the exact periodic continuation.

This is stronger than merely observing that `V_M` decreases. XF-039 needs an additional factor `M` beyond `V_M->0`; equation (28) quantifies the extra damping needed to win exactly that factor.

## 4. The obstruction lives at vanishing depth from its own transition

The exact matched-control transition gives an independent way to see why the XF-039 corrugation can exist at the static source scale. At `t_0=0`, equations (3), (12), and (22) give
\[
\begin{aligned}
-\Lambda_G
&=\omega^{-2}
\log\frac1{|\cos\delta|}\\
&=\omega^{-2}
\log\frac1{\sin(\pi\tau_M(0)/2)}\\
&=\boxed{
\omega^{-2}\bigl((1+\alpha)\log M+O(1)\bigr).
}
\end{aligned}
\tag{29}
\]
At the Xi spacing (26),
\[
\boxed{
-\Lambda_G
=O\!\left(\frac{\log M}{\log^2T}\right)
=O(1/\log T)
\to0.
}
\tag{30}
\]
Thus the exact periodic control realizes the XF-039 microcorrugation at time zero only by sitting a **vanishing heat-time depth above its own real-zero transition**.

Conversely, if one observes this control a fixed depth
\[
\sigma:=t-\Lambda_G>0
\tag{31}
\]
inside its real-rooted regime, then (6) gives the universal formula
\[
\boxed{
\tau(t)
=\frac2\pi\arcsin\!\left(e^{-\omega^2\sigma}\right).
}
\tag{32}
\]
At the source spacing, any fixed `sigma>0` makes `tau` of order
\[
\exp\!\left(-\frac{\sigma}{16}(\log T)^2\right),
\tag{33}
\]
up to a bounded prefactor. This is far below `M^-2` for the source buffers (27). Therefore this entire matched-control family has much more than the inverse-buffer BV margin once a fixed amount of real-rooted heat time is available.

Equation (32) does **not** transfer automatically to Xi. Its role is to identify the missing resource more sharply: the XF-039 static obstruction is compatible with source-scale counting because it can be arbitrarily close, in heat time, to a collision boundary. A positive Xi theorem must use actual time-depth/dissipation information to prevent such microscopic oscillation from being continually regenerated inside a finite window.

## 5. Exact agreement with the XF-007 high-frequency lattice mode

The small-amplitude expansion of (13) is
\[
\boxed{
\tau'=-\omega^2\tau+O(\omega^2\tau^3).
}
\tag{34}
\]
With mean gap `s=L/2`, equation (26) is
\[
\omega^2=\frac{\pi^2}{s^2}.
\tag{35}
\]
XF-007 gives the exact lattice linearization eigenvalue
\[
\lambda_s(\theta)
=-\frac{\theta(2\pi-\theta)}{s^2}.
\tag{36}
\]
The alternating gap mode is `theta=pi`, so
\[
\lambda_s(\pi)=-\frac{\pi^2}{s^2}=-\omega^2.
\tag{37}
\]
Thus the present nonlinear matched control is the exact finite-amplitude completion of the fastest two-gap mode already identified perturbatively in XF-007. There is no hidden factor-of-two or normalization mismatch between the periodic entire-function calculation, the zero ODE, and the lattice Fourier symbol.

This consistency is an important stress test. It also clarifies what is genuinely new relative to XF-007: not the existence of high-frequency damping, but the exact nonlinear continuation all the way from a double-collision transition through the small-corrugation regime, together with the explicit entry time into the `M V_M=O(1)` threshold isolated much later by XF-035--XF-039.

## 6. Falsification boundary

The family (1) is intentionally a matched control, not Xi evidence. It is even, real entire, solves the same backward heat equation, has an exact de Bruijn--Newman-type transition, and on the real-simple side obeys the same logarithmic zero-motion law. Therefore any proposed local argument that claims the alternating mode is Xi-specific fails this control immediately.

On the other hand, the control also kills the strongest direct negative extrapolation from XF-039. The alternating static block cannot simply be declared dynamically persistent: when its exterior is continued in the most coherent possible way, the full nonlinear heat flow damps it at the microscopic `s^2` clock and wins the extra inverse-buffer factor in vanishing time.

What remains open is precisely the finite-window mechanism. A real Xi block can contain low-frequency modulation, the exterior can feed signed flux through the taper region, and the quantity
\[
V_M=\|L_\lambda h\|_{\ell^1}
\]
need not inherit a scalar maximum principle from the gap diffusion. The next positive theorem should therefore be a localized or time-integrated estimate that separates the rapidly damped microscopic component from the source-constrained low-frequency component and controls replenishment through the super-mesoscopic buffer. A decisive negative continuation would need a source-compatible configuration whose excessive `V_M` survives the **actual** nonlinear evolution for a source-relevant interval, not merely one static time slice.

## 7. Prior-art and novelty boundary

Periodic and trigonometric backward heat flow is classical territory. Kabluchko's work on unitary Hermite polynomials and periodic backward heat flow is already anchored in `SOURCES.md`, while the cotangent partial-fraction identity and two-sublattice logarithmic-repulsion calculation are elementary classical identities. No new general theorem about periodic log gases, trigonometric real-rootedness, or backward heat flow is claimed here, and no new source anchor is load-bearing.

The durable Mathia-local content is the exact placement of the XF-039 obstruction inside that classical matched-control family: equations (17)--(20) identify its triple-flux BV defect exactly, (24)--(28) show that the missing inverse-buffer factor is recovered in vanishing source-scale heat time, and (29)--(32) show that the static obstruction corresponds to vanishing depth from the control's own real-zero transition. This is the dynamical calibration that XF-039 itself left open.

## 8. Consequence for `xi_flow`

The frontier is now more specific than "derive `V_M=O(1/M)` dynamically." The worst static microscopic counterexample currently known is an **exactly solvable high-frequency mode**, and on its natural matched-control continuation a fixed real-rooted time depth annihilates it far beyond the required BV scale. The missing theorem is therefore not evidence that microscopic damping exists; it is a localization/assembly theorem showing that the Xi exterior and low-frequency modes cannot continually repopulate microscopic flux variation quickly enough to defeat that damping.

A promising decomposition is now forced by the evidence. Use translated Xi counting to control the low-frequency/geometric component as in XF-034--XF-039, and seek a time-integrated coercive estimate for the high-frequency component of `L_lambda h`, with taper/exterior errors charged to the super-mesoscopic buffer. The periodic control proves that the target rate is compatible with the exact nonlinear dynamics and that the `1/M` BV threshold itself is not too strong for the most adversarial static microcorrugation. It does not yet supply the finite-window estimate needed to conclude a fixed-time Lyapunov inequality or an upper bound for `Lambda`.