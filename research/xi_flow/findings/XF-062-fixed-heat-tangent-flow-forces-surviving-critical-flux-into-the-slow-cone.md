# XF-062 — fixed heat tangent flow forces surviving critical flux into the slow cone

**Status:** `EXACT-DERIVED` + `SHARP-LINEARIZED-BAND-REDUCTION` + `MATCHED-CONTROL` + `STRUCTURAL/REPAIR`. XF-061 shows that the derivative-weighted XF-060 selector is not a static inverse norm on arbitrary source-compatible finite-gap geometry: a single `O(M^{-1})` root displacement carries order-one normalized triple-flux variation while placing vanishing energy in the whole shrinking slow cone. That obstruction is real, but it is also spectrally high-frequency. In the exact arithmetic-lattice tangent flow, a fixed positive amount of heat time removes precisely this escape.

Let

\[
q=q_T\asymp\log^2T,
\qquad
M=q^2,
\qquad
N=2M,
\qquad
s=s_T=\frac{4\pi}{\log(T/4\pi)},
\tag{1}
\]

and consider the exact `N`-periodic linearization of the real-zero gap flow at the arithmetic lattice of spacing `s`. Write a tangent root-displacement field in index units as `a_j(t)`, modulo its translation mode, and assume only the source-compatible bound

\[
\|a(0)\|_{\ell^\infty(\mathbb Z/N\mathbb Z)}\le A_0
\tag{2}
\]

for a fixed `A_0`. Put `\Delta a_j=a_{j+1}-a_j`. The linearized triple-flux variation is

\[
\boxed{
\mathcal F_M^{\rm lin}(t;a)
:=\frac32 M\|\Delta^3a(t)\|_{\ell^1}.
}
\tag{3}
\]

This is exactly the first variation of `M V_M`: if

\[
x_j(0)=s\bigl(j+\varepsilon a_j(0)\bigr),
\tag{4}
\]

then, for each fixed `T`,

\[
M V_M(t)
=\varepsilon\mathcal F_M^{\rm lin}(t;a)+O_T(\varepsilon^2)
\qquad(\varepsilon\to0).
\tag{5}
\]

For the unitary discrete Fourier transform of `a`, let

\[
\theta_\ell=\frac{2\pi\ell}{N},
\qquad
m(\theta)=e^{i\theta}-1,
\tag{6}
\]

and define the tangent flux energy on a frequency set `B` by

\[
\boxed{
\mathcal Q_M(B,t)
:=M^3
\sum_{\theta_\ell\in B}
|m(\theta_\ell)|^6
|\widehat a_\ell(t)|^2.
}
\tag{7}
\]

Fix any heat time `\tau>0`. Take the XF-059 selector cone with the concrete infrared exponent `\delta=1/2`,

\[
\boxed{
\Theta_T(C)
=\left\{
\theta:\
q^{-3/2}\le |\theta|\le
\frac{C\log\log T}{q}
\right\}.
}
\tag{8}
\]

Then there exists a fixed `C_*(\tau)>0`, depending only on `\tau` and the asymptotic constants in `q\asymp\log^2T`, such that every fixed `C>C_*(\tau)` satisfies

\[
\boxed{
\mathcal Q_M\bigl(\Theta_T(C)^c,\tau\bigr)=o(1)
}
\tag{9}
\]

uniformly over every family satisfying (2). Moreover

\[
\boxed{
\bigl(\mathcal F_M^{\rm lin}(\tau;a)\bigr)^2
\le \frac92\,
\mathcal Q_M\bigl(( -\pi,\pi],\tau\bigr).
}
\tag{10}
\]

Consequently, if a bounded source-compatible tangent family retains genuinely critical triple flux after a fixed positive heat time,

\[
\liminf_{T\to\infty}
\mathcal F_M^{\rm lin}(\tau;a)>0,
\tag{11}
\]

then the same family must retain order-one `H^3` Fourier energy **inside the exact XF-059 slow cone**:

\[
\boxed{
\liminf_{T\to\infty}
\mathcal Q_M\bigl(\Theta_T(C),\tau\bigr)>0.
}
\tag{12}
\]

The two edges have different mechanisms. Below `q^{-3/2}`, three discrete derivatives make the normalized flux energy `o(1)` for any bounded root-displacement field. Above `C\log\log T/q`, the exact Cauchy-lattice multiplier damps every mode by a sufficiently large negative power of `\log T` during any fixed `\tau>0`. Thus the same band that the Xi moving-line selector controls in XF-059 is also the only band in which bounded tangent geometry can retain critical triple flux after fixed heat time.

This does **not** yet give an upper bound for `Lambda`. The result is a tangent periodic theorem. It does not prove a nonlinear lower frame from the actual XF-059/XF-060 selectors to (7), and it does not cross a collision or a complex-root interval. Its value is that the sparse spectral-support obstruction of XF-061 is no longer an all-time obstruction: at positive tangent heat time, surviving critical flux is forced back into the already source-controlled frequency window.

## 1. Exact periodic tangent multiplier

XF-044 computes the exact Jacobian of the `N`-periodic positive-gap flow at the arithmetic lattice. For the Fourier mode `e^{2\pi i\ell j/N}`,

\[
D\mathcal V(s\mathbf 1)e^{2\pi i\ell j/N}
=-\rho_{N,s}^{(\ell)}e^{2\pi i\ell j/N},
\tag{13}
\]

with

\[
\rho_{N,s}^{(\ell)}
=\frac{4\pi^2}{N^2s^2}\ell(N-\ell).
\tag{14}
\]

Writing the corresponding principal frequency as

\[
\theta=\frac{2\pi\ell}{N}\in[0,\pi],
\tag{15}
\]

this is exactly

\[
\boxed{
\rho_s(\theta)
=\frac{\theta(2\pi-\theta)}{s^2}.
}
\tag{16}
\]

The same multiplier acts on nonconstant root-displacement modes. Indeed the relative gap tangent is `u=\Delta a`; the lattice Jacobian commutes with `\Delta`, and division by the nonzero multiplier `m(\theta)` transfers the same semigroup to `a` modulo translation. Hence

\[
\boxed{
\widehat a_\ell(t)
=e^{-\rho_s(|\theta_\ell|)t}
\widehat a_\ell(0)
\qquad(\ell\ne0).
}
\tag{17}
\]

Equation (17) is the finite-period version of the XF-008 Cauchy/half-Laplacian limit. No continuum approximation is needed below.

## 2. Triple flux is exactly third order in root displacement at the lattice

For (4), the relative gap tangent is

\[
u_j=\Delta a_j.
\tag{18}
\]

The XF-030 logarithmic gap contrast is

\[
d_j
=\log\frac{g_{j+1}}{g_j}
=\varepsilon\Delta u_j+O_T(\varepsilon^2),
\tag{19}
\]

and its exact shape flux obeys

\[
\phi_j=F'(d_j)
=-\frac32d_j+O(d_j^3).
\tag{20}
\]

Therefore

\[
\boxed{
\phi_{j+1}-\phi_j
=-\frac32\varepsilon\Delta^2u_j
+O_T(\varepsilon^2)
=-\frac32\varepsilon\Delta^3a_j
+O_T(\varepsilon^2).
}
\tag{21}
\]

Taking the one-sided derivative at `\varepsilon=0` gives (3)--(5). The third difference is important: it is one derivative from root displacement to gaps and two more from the XF-030 triple-flux variation. This is exactly why both the infrared and ultraviolet edges can be separated cleanly.

For the full Fourier energy, Parseval gives

\[
\mathcal Q_M(( -\pi,\pi],t)
=M^3\|\Delta^3a(t)\|_2^2.
\tag{22}
\]

Since the period has `N=2M` sites,

\[
\|\Delta^3a\|_1
\le\sqrt{2M}\,\|\Delta^3a\|_2.
\tag{23}
\]

Substituting (23) into (3) yields exactly (10):

\[
\bigl(\mathcal F_M^{\rm lin}\bigr)^2
\le
\frac94 M^2(2M)\|\Delta^3a\|_2^2
=\frac92\mathcal Q_M.
\tag{24}
\]

Thus order-one normalized tangent flux requires order-one `M^3 H^3` energy somewhere in frequency space. The rest of the argument identifies where that energy can still live after fixed heat time.

## 3. The ultra-low tail is too flat to carry critical flux

Set

\[
\theta_-:=q^{-3/2}.
\tag{25}
\]

For `|\theta|\le\pi`,

\[
|m(\theta)|=2\sin(|\theta|/2)\le|\theta|.
\tag{26}
\]

The tangent semigroup is contractive in `\ell^2`, so from (2)

\[
\|a(\tau)\|_2^2
\le\|a(0)\|_2^2
\le2MA_0^2.
\tag{27}
\]

Therefore

\[
\begin{aligned}
\mathcal Q_M(|\theta|<\theta_-,\tau)
&\le
M^3\theta_-^6\|a(\tau)\|_2^2\\
&\le2A_0^2M^4q^{-9}.
\end{aligned}
\tag{28}
\]

Because `M=q^2`,

\[
\boxed{
\mathcal Q_M(|\theta|<q^{-3/2},\tau)
=O_{A_0}(q^{-1})=o(1).
}
\tag{29}
\]

No heat damping is used here. This is a pure source-geometry statement: a bounded root displacement cannot place critical third-difference energy at wavelengths longer than `q^{3/2}` gaps. The exponent `3/2` is not claimed sharp; it is chosen because it lies safely inside the XF-059 admissible infrared range and makes the normalization transparent.

More generally, using the XF-059 lower edge `q^{-2+\delta}` gives

\[
\mathcal Q_M\bigl(|\theta|<q^{-2+\delta},\tau\bigr)
=O_{A_0}(q^{-4+6\delta}).
\tag{30}
\]

Hence every fixed `0<\delta<2/3` works. The concrete choice `\delta=1/2` in (8) leaves a full power of `q` of slack.

## 4. Fixed heat time removes the high-frequency tail

Set

\[
\theta_+
:=\frac{C\log\log T}{q}.
\tag{31}
\]

Since `s^{-2}\asymp q`, there is a fixed `\beta>0` such that for all sufficiently large `T`,

\[
s^{-2}\ge\beta q.
\tag{32}
\]

For `0\le\theta\le\pi`, equation (16) gives

\[
\rho_s(\theta)
\ge\pi\beta q\theta.
\tag{33}
\]

Thus every mode with `|\theta|\ge\theta_+` satisfies

\[
\rho_s(|\theta|)
\ge\pi\beta C\log\log T.
\tag{34}
\]

Using `|m|\le2`, (17), and (27) at time zero,

\[
\begin{aligned}
\mathcal Q_M(|\theta|>\theta_+,\tau)
&\le64M^3
 e^{-2\pi\beta C\tau\log\log T}
\|a(0)\|_2^2\\
&\le128A_0^2M^4
 e^{-2\pi\beta C\tau\log\log T}.
\end{aligned}
\tag{35}
\]

Now `M^4=q^8=\exp((16+o(1))\log\log T)`. Therefore any fixed `C` satisfying

\[
2\pi\beta C\tau>16
\tag{36}
\]

makes (35) tend to zero. This proves the high-frequency half of (9). The explicit numerical threshold in (36) is only a convenient sufficient value; no sharpness is claimed.

The important scale is the logarithm. A frequency `\theta\asymp1/q` has only order-one damping over fixed heat time, exactly as XF-044 found. Moving the cutoff up by the factor `\log\log T` changes the damping into an arbitrarily large fixed negative power of `\log T`, enough to beat the polynomial `M^4` cost of an arbitrary bounded tangent field. That is why the XF-059 upper edge is also the natural ultraviolet edge for post-heat tangent flux.

Combining (29) and (35) proves (9).

## 5. Surviving critical flux must occupy the selector band

By (10), if

\[
\mathcal F_M^{\rm lin}(\tau;a)\ge c_0>0
\tag{37}
\]

along a sequence of heights, then

\[
\mathcal Q_M(( -\pi,\pi],\tau)
\ge\frac{2c_0^2}{9}.
\tag{38}
\]

The complement of `\Theta_T(C)` contributes `o(1)` by (9), so

\[
\boxed{
\liminf_{T\to\infty}
\mathcal Q_M(\Theta_T(C),\tau)
\ge\frac{2c_0^2}{9}>0.
}
\tag{39}
\]

This is the promised band reduction. It is stronger than saying that high frequencies damp: it matches both ends of the surviving tangent flux to a band already proved source-small by the actual Xi moving-line construction.

The normalization also matches XF-060. On slow frequencies, `|m(\theta)|\asymp|\theta|`, so (7) is

\[
\mathcal Q_M(\Theta,t)
\asymp
M^3\sum_{\theta\in\Theta}
\theta^6|\widehat a(\theta,t)|^2.
\tag{40}
\]

A root displacement contributes one Fourier derivative to the first-order moving-line selector, while the XF-060 weight contributes two additional discrete derivatives. After accounting for the selector resolution cell of width `1/M`, its quadratic normalization has the same `M^3\theta^6` tangent symbol. This is the structural reason XF-060 detected distributed critical modes and why XF-061's only remaining escape was spectral support outside the band.

Equation (40) is a symbol-level bridge, not yet a lower-frame theorem for the actual localized probes. Establishing that lower frame after heat regularization is a remaining step.

## 6. The XF-061 single-root obstruction is erased at fixed tangent heat time

Take the exact sparse geometry behind XF-061 at tangent scale,

\[
a_j(0)=\frac{\kappa}{M}\,\mathbf 1_{j=0}.
\tag{41}
\]

At `t=0`,

\[
\|\Delta^3a(0)\|_1
=\frac{8\kappa}{M},
\tag{42}
\]

so (3) gives

\[
\boxed{
\mathcal F_M^{\rm lin}(0;a)=12\kappa,
}
\tag{43}
\]

exactly reproducing the leading XF-061 critical flux.

For every fixed `\tau>0`, however, (17) gives much more than band concentration. Since the unitary Fourier coefficients of the point defect all have magnitude `\kappa/(M\sqrt N)`, the bound

\[
\rho_s(\theta)\gg q|\theta|
\qquad(0\le|\theta|\le\pi)
\tag{44}
\]

and an elementary sum-integral comparison yield

\[
\frac1N\sum_{\ell=0}^{N-1}
|m(\theta_\ell)|^6
 e^{-2\rho_s(|\theta_\ell|)\tau}
=O_\tau(q^{-7}).
\tag{45}
\]

Therefore

\[
\boxed{
\mathcal Q_M(( -\pi,\pi],\tau)
=O_\tau(\kappa^2q^{-5}),
}
\tag{46}
\]

and (10) gives

\[
\boxed{
\mathcal F_M^{\rm lin}(\tau;a)
=O_\tau(\kappa q^{-5/2})
\longrightarrow0.
}
\tag{47}
\]

Thus the canonical sparse counterexample is genuinely **static** at the critical normalization. It rules out an arbitrary-block inverse theorem at a fixed instant, exactly as XF-061 claims, but it does not persist for a fixed positive time even in the universal tangent dynamics.

This distinction matters for the next mechanism search. A successful transition argument may use heat regularization before applying a slow-frequency inverse theorem, provided it can justify that the transition-side quantity of interest remains critical during that delay. The present finding proves the spectral part of such a strategy only in the arithmetic tangent model; it does not supply that persistence.

## 7. Stress tests and evidence boundary

The first boundary is **linearization**. Equations (13)--(17) are the exact derivative of the periodic nonlinear flow at the lattice, but (9) is not a finite-amplitude nonlinear Littlewood--Paley theorem. Nonlinear mode coupling can in principle move energy between frequency bands. Upgrading (9) requires controlling that coupling at the source-compatible amplitudes relevant to a transition argument.

The second boundary is **real-simple periodic geometry**. The theorem does not transport through a collision, and it does not describe an interval on which Xi has complex zeros. In a hypothetical `Lambda>0` scenario one cannot simply start at `t=0` with an ordered real zero lattice and evolve to the transition. The useful application would have to occur on a real-simple side of the transition, or through a collision-safe observable already transported by XF-050--XF-054.

The third boundary is **flux persistence**. A localized defect can carry order-one `M V_M` at one instant and then lose it rapidly, as (47) demonstrates. Therefore it is not enough to show that a collision creates a local critical defect. One needs either a quantity with enough persistence to reach a fixed positive delay, or a direct selector/frame estimate arbitrarily close to the transition where the ultraviolet tail has not yet been eliminated.

The fourth boundary is the **selector frame**. XF-059 proves rapid Xi smallness for every moving-line coefficient in `\Theta_T(C)` and XF-060 gives the correct derivative weighting. The present theorem shows that post-heat tangent flux has no asymptotically relevant energy outside that same band. It does not yet prove that the localized continuous selector family controls the band energy (7) uniformly for every admissible tangent field. That is now a precise, narrower analytic gate rather than an arbitrary spectral-support problem.

These boundaries prevent an RH upgrade. The result neither proves `Lambda\le0` nor excludes a positive transition time.

## 8. Prior-art and novelty boundary

The exact periodic multiplier (14), its Cauchy/half-Laplacian scaling, and the de Bruijn--Newman zero ODE are already anchored in `SOURCES.md` through Rodgers--Tao and the nonlocal-diffusion literature used by XF-008/XF-044. Frequency splitting into a low observable sector and a high sector suppressed by a parabolic semigroup is a classical PDE/control principle; no novelty is claimed for that abstract idea, Parseval, or the `\ell^1`--`\ell^2` estimate.

A targeted audit of de Bruijn--Newman zero dynamics, fractional-heat observability, Littlewood--Paley/Sobolev square functions, and heat-semigroup frequency splitting did not locate the line-specific scale conjunction proved here: the XF-030 third-difference tangent flux at `M=q^2`, the Xi spacing `s^{-2}\asymp q`, and the exact XF-059 band `[q^{-3/2},C\log\log T/q]`. No external theorem beyond the line's existing classical anchors is load-bearing, so `SOURCES.md` requires no change.

The durable Mathia-local content is the scale-matched reduction (9)--(12) and its consequence (47): once a bounded lattice tangent is allowed any fixed positive heat time, critical triple-flux geometry can survive only in the same slow band for which the actual Xi endpoint selector is already rapidly small.

## 9. Consequence for `xi_flow`

XF-061 changes the problem from frequency calibration to spectral support. XF-062 shows that this new obstruction is itself time-sensitive. At the arithmetic tangent level, fixed heat time automatically removes both pieces of the complement of the XF-059 band: ultra-low modes are too flat to carry the third-difference critical normalization, while high modes are crushed by the Cauchy semigroup. The single-root defect that killed the static inverse theorem is smoothed from `12\kappa` critical flux to `o(1)`.

The next gate is therefore not another static reweighting of the shrinking cone. It is to determine whether **heat-regularized selector coercivity** survives beyond the lattice tangent model: combine a nonlinear or collision-safe version of the band reduction with a localized lower-frame estimate for the XF-059/XF-060 moving-line family. A negative result would require a source-compatible finite-amplitude control whose nonlinear dynamics preserves order-one transition flux for fixed time while keeping the entire heat-regularized selector band small. A positive result would remove the specific sparse-support escape exposed by XF-061 and reconnect the endpoint selector to a transition-side stability quantity.