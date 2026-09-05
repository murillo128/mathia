# XF-041 — bounded periodic gap controls have nonlinear Cauchy spectral-gap damping

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `NONLINEAR-SPECTRAL-GAP` + `STRUCTURAL/DYNAMIC`. XF-040 shows that the exact two-gap periodic continuation of the XF-039 alternating microcorrugation is rapidly damped by the backward-heat zero dynamics. The two-gap solvability is not essential for that conclusion. On every real-simple `q`-periodic gap trajectory of the logarithmic zero-motion law, the exact nonlinear positive-conductance diffusion of XF-014 has a quantitative Cauchy spectral gap. If the gaps initially have bounded dynamic range, their variance around the period mean decays exponentially at rate `asymp 1/(q s^2)`, where `s` is the mean gap.

More precisely, let `q>=2` and let an ordered real-simple zero trajectory satisfy

\[
x_{i+q}(t)=x_i(t)+S,
\qquad
g_i(t):=x_{i+1}(t)-x_i(t)>0,
\tag{1}
\]

through a time interval on which the XF-014 zero-motion equation is valid. Put

\[
s:=\frac{S}{q},
\qquad
b_0:=\max_{0\le i<q}g_i(t_0),
\qquad
E(t):=\frac12\sum_{i=0}^{q-1}(g_i(t)-s)^2.
\tag{2}
\]

Then `s` is constant, the period maximum gap is nonincreasing, the period minimum gap is nondecreasing, and

\[
\boxed{
E(t)
\le
E(t_0)
\exp\!\left[
-\frac{8\pi^2(q-1)}{q^2 b_0^2}(t-t_0)
\right]
}
\qquad(t\ge t_0).
\tag{3}
\]

The coefficient is nonlinear and global: no small-perturbation assumption is used. Its `q`-dependence is the exact spectral gap of the periodized inverse-square/Cauchy kernel. For `q=2` and a small corrugation, the corresponding amplitude decay rate tends to `pi^2/s^2`, exactly the rate computed independently in XF-040.

At the Xi source spacing `s=h_T~4pi/log T`, suppose the periodic control has `b_0<=C s` with fixed `C` and an initial relative amplitude of order `M^{-1-alpha}`, `0<alpha<1`, where `M=R(T)log^2 T` is the active source buffer. The bound (3) drives the whole period to relative amplitude `O(M^-2)` — a sufficient scale for `M V_M=O(1)` — after

\[
\boxed{
\Delta t
\le
\frac{4C^2 q^2}{q-1}
\frac{(1-\alpha)\log M+\frac12\log q+O(1)}{(\log T)^2}.
}
\tag{4}
\]

Since the source regime has `log M=O(log T)`, every bounded-range periodic obstruction with

\[
\boxed{q=o(\log T)}
\tag{5}
\]

is therefore forced through the inverse-buffer amplitude scale in **vanishing heat time**. XF-040 is the `q=2` exactly solvable endpoint of a much broader nonlinear smoothing mechanism.

This still does **not** prove the needed finite-window Xi estimate. Periodicity removes the exterior flux by identification, whereas a finite Xi window can be continually replenished from outside. The durable narrowing is that a source-compatible persistent obstruction cannot be explained by a coherent short-period microscopic pattern: it must exploit exterior forcing, nonperiodic transport, or wavelengths of at least order `log T` gaps, where the Cauchy relaxation clock ceases to vanish on an order-one heat interval.

## 1. The periodic gap system closes to a finite positive-conductance diffusion

XF-014 gives, on every real-simple slice,

\[
g_i'
=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}
=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\tag{6}
\]

For a `q`-periodic gap sequence, `g_{k+nq}=g_k`. Fix residue classes `i,j in {0,...,q-1}` and define the periodized conductance

\[
C_{ij}
:=
\sum_{n\in\mathbb Z}c_{i,j+nq},
\qquad i\ne j.
\tag{7}
\]

The series converges absolutely because `c_{i,j+nq}=O(n^{-2})`. Terms with `k congruent i (mod q)` make no contribution to (6), since their gap difference vanishes. Hence the infinite system closes exactly to

\[
\boxed{
g_i'
=2\sum_{\substack{0\le j<q\\j\ne i}}
C_{ij}(g_j-g_i),
\qquad C_{ij}=C_{ji}>0.
}
\tag{8}
\]

Summing (8) over one period cancels every pair, so

\[
\sum_{i=0}^{q-1}g_i=qs=S
\tag{9}
\]

is constant. At an index realizing the period maximum, every term in (8) is nonpositive; at an index realizing the period minimum, every term is nonnegative. In the upper/lower Dini derivative sense this gives

\[
\boxed{
\max_i g_i(t)\le b_0,
\qquad
\min_i g_i(t)\ge \min_i g_i(t_0)
}
\tag{10}
\]

for all later real-simple times. Thus the bounded dynamic range can only improve.

This is already a useful distinction from the finite-window problem. There is no boundary term in (8): all long-range interactions re-enter through the quotient conductances `C_ij`.

## 2. Ordering gives a universal inverse-square lower bound

Let

\[
b(t):=\max_i g_i(t)\le b_0.
\tag{11}
\]

If two gap indices differ by a nonzero integer `m`, then both distances in the denominator of `c_{ik}` span exactly `|m|` positive gaps. Therefore

\[
|x_i-x_k|\le b(t)|i-k|,
\qquad
|x_{i+1}-x_{k+1}|\le b(t)|i-k|,
\tag{12}
\]

and hence

\[
\boxed{
c_{ik}
\ge\frac1{b(t)^2(i-k)^2}
\ge\frac1{b_0^2(i-k)^2}.
}
\tag{13}
\]

For residues with `r=j-i not congruent 0 (mod q)`, periodization yields

\[
C_{ij}
\ge
\frac1{b_0^2}
\sum_{n\in\mathbb Z}\frac1{(r+nq)^2}.
\tag{14}
\]

The elementary Mittag--Leffler identity gives

\[
\sum_{n\in\mathbb Z}\frac1{(r+nq)^2}
=rac{\pi^2}{q^2}
\csc^2\!\left(\frac{\pi r}{q}\right).
\tag{15}
\]

Thus the exact nonlinear conductance network dominates a fixed circulant Cauchy kernel:

\[
\boxed{
C_{ij}
\ge
\frac{\pi^2}{q^2b_0^2}
\csc^2\!\left(\frac{\pi(i-j)}q\right).
}
\tag{16}
\]

No lower bound on the gaps is required for (16). Small gaps only increase the relevant conductances. The sole parameter in this coercive lower bound is the initial period maximum `b_0`.

## 3. The periodized Cauchy kernel has an exact spectral gap

Write

\[
u_i:=g_i-s,
\qquad
\sum_{i=0}^{q-1}u_i=0.
\tag{17}
\]

For the circulant kernel

\[
K_r:=\frac{\pi^2}{q^2}
\csc^2\!\left(\frac{\pi r}{q}\right),
\qquad 1\le r\le q-1,
\tag{18}
\]

the Fourier mode `exp(2pi i ell i/q)` has Laplacian eigenvalue

\[
\lambda_\ell
=
\sum_{r=1}^{q-1}K_r
\left(1-\cos\frac{2\pi\ell r}{q}\right).
\tag{19}
\]

Using

\[
1-\cos(2\theta)=2\sin^2\theta
\tag{20}
\]

and the finite identity

\[
\sum_{r=1}^{q-1}
\frac{\sin^2(\pi\ell r/q)}
{\sin^2(\pi r/q)}
=\ell(q-\ell),
\tag{21}
\]

one gets

\[
\boxed{
\lambda_\ell
=\frac{2\pi^2}{q^2}\ell(q-\ell),
\qquad 1\le\ell\le q-1.
}
\tag{22}
\]

Identity (21) follows directly by expanding the squared geometric sum

\[
\left|1+z+\cdots+z^{\ell-1}\right|^2
\tag{23}
\]

at the nontrivial `q`th roots of unity and summing the Fourier coefficients; no external spectral theorem is needed. In particular,

\[
\boxed{
\lambda_*:=\min_{1\le\ell<q}\lambda_\ell
=\frac{2\pi^2(q-1)}{q^2}.
}
\tag{24}
\]

Therefore every zero-mean vector satisfies the periodized Cauchy Poincare inequality

\[
\boxed{
\sum_{0\le i<j<q}K_{i-j}(u_i-u_j)^2
\ge
\lambda_*\sum_{i=0}^{q-1}u_i^2.
}
\tag{25}
\]

The `lambda_*~2pi^2/q` behavior is the finite-period form of the `|theta|` Cauchy symbol from XF-007--XF-008. A nearest-neighbor estimate would give only a `q^-2` spectral gap and would miss the correct nonlocal clock by an entire factor of `q`.

## 4. Exact nonlinear variance contraction

Differentiate the period variance (2). Since the mean is constant, equation (8) and pairwise symmetry give

\[
\begin{aligned}
E'
&=\sum_i u_i g_i'\\
&=-2\sum_{0\le i<j<q}C_{ij}(u_i-u_j)^2.
\end{aligned}
\tag{26}
\]

Combining (16) and (25),

\[
E'
\le
-\frac{2}{b_0^2}\lambda_*
\sum_i u_i^2
=
-\frac{4\lambda_*}{b_0^2}E.
\tag{27}
\]

Substitution of (24) gives

\[
\boxed{
E'
\le
-\frac{8\pi^2(q-1)}{q^2b_0^2}E,
}
\tag{28}
\]

and Gronwall yields (3).

Several potential loopholes are absent. The estimate is valid at arbitrary finite contrast; the conductances may vary nonlinearly with time; no linearization is used; and approaching a small gap strengthens rather than weakens the lower conductance bound. The only boundary is the same as in XF-014: the argument is confined to the real-simple regime and is not continued through a collision.

The variance estimate also controls every gap pointwise:

\[
\boxed{
\max_i\left|\frac{g_i(t)}s-1\right|
\le
\frac{\sqrt{2E(t_0)}}s
\exp\!\left[
-\frac{4\pi^2(q-1)}{q^2b_0^2}(t-t_0)
\right].
}
\tag{29}
\]

If the initial relative amplitude is `A_0=max_i|g_i(t_0)/s-1|`, then `2E(t_0)<=q s^2 A_0^2`, so

\[
\boxed{
A(t)
\le
\sqrt q\,A_0
\exp\!\left[
-\frac{4\pi^2(q-1)}{q^2b_0^2}(t-t_0)
\right].
}
\tag{30}
\]

## 5. XF-040 is the sharp two-gap small-amplitude endpoint

For `q=2`, equation (30) has amplitude exponent

\[
\frac{4\pi^2(q-1)}{q^2b_0^2}
=\frac{\pi^2}{b_0^2}.
\tag{31}
\]

In the small-corrugation regime of XF-040, `b_0/s->1`, so the bound tends to

\[
\frac{\pi^2}{s^2}.
\tag{32}
\]

XF-040 independently derives the exact nonlinear scalar law and obtains precisely this linearized amplitude rate. Thus the quotient-conductance proof has the correct normalization and is asymptotically sharp at the fastest two-gap mode. The new content is that no trigonometric solvability is needed to retain a quantitative damping theorem for arbitrary period `q` and arbitrary finite gap shape.

For large `q`, the slowest nonconstant period mode has rate `asymp 1/(q s^2)` rather than `1/s^2`. This identifies the expected transition from microscopic to longer-wave behavior without appealing to the lattice linearization: it is already forced by the exact nonlinear conductance lower bound.

## 6. Source-scale consequence: all sub-`log T` periodic microstructure relaxes in vanishing time

Assume a matched periodic control is observed at the source mean gap

\[
s=h_T\sim\frac{4\pi}{\log T}
\tag{33}
\]

and has uniformly bounded dynamic range

\[
b_0\le C s
\tag{34}
\]

for a fixed `C`. Suppose its initial relative amplitude obeys the same static scale as the XF-039 obstruction,

\[
A_0=O(M^{-1-\alpha}),
\qquad 0<\alpha<1.
\tag{35}
\]

Equation (30) implies `A(t_0+Delta t)=O(M^-2)` once

\[
\frac{4\pi^2(q-1)}{q^2b_0^2}\Delta t
\ge
(1-\alpha)\log M+\frac12\log q+O(1).
\tag{36}
\]

Using (33)--(34) gives (4).

Why is `M^-2` the relevant target? Once `A=O(M^-2)`, all adjacent logarithmic contrasts satisfy `d_j=O(M^-2)`. The exact compact flux law of XF-035 has `phi=F'(d)=O(d)` near zero, so over an `O(M)`-gap sample

\[
V_M=O(M\,M^{-2})=O(M^{-1}),
\tag{37}
\]

and therefore

\[
\boxed{M V_M=O(1).}
\tag{38}
\]

An `o(M^-2)` amplitude gives the stronger `M V_M=o(1)` gate.

For the source buffer `M=R(T)log^2T` with `R(T)=o(T/log T)`, one has `log M=O(log T)`. Hence (4) is

\[
\Delta t
=O\!\left(\frac{q\log T+q\log q}{\log^2T}\right)
\tag{39}
\]

for large `q`, and in particular

\[
q=o(\log T)
\quad\Longrightarrow\quad
\Delta t=o(1).
\tag{40}
\]

So a coherent periodic pattern on `o(log T)` gaps cannot sustain the XF-039 inverse-buffer defect over any fixed positive amount of real-rooted heat time. The borderline `q~log T` corresponds to a physical wavelength `q s=Theta(1)`, which is exactly where this simple vanishing-time conclusion stops.

This is a scale separator, not an Xi proof. It says that the missing persistent mode cannot remain purely microscopic and periodic once a fixed heat-time depth is available.

## 7. Falsification and prior-art boundary

The mechanism is deliberately universal. It uses only the exact ordered logarithmic-repulsion gap equation of XF-014, positivity of its conductances, and elementary periodized inverse-square identities. Any periodic synthetic log-particle control in the real-simple regime inherits it. Periodic/trigonometric backward heat flow is classical territory, and Kabluchko's backward-heat work is already anchored in `SOURCES.md`; Guillin--Le Bris--Monmarche is already anchored there as the broader one-dimensional positive-contraction prior-art boundary. No new source is load-bearing, and no claim of novelty is made for contraction of periodic repulsive particle systems or for the trigonometric identity (15).

The Mathia-local content is the quantitative bridge between three previously separate pieces of this line: the exact nonlinear conductance diffusion of XF-014, the Cauchy `|theta|` spectral scaling of XF-007--XF-008, and the inverse-buffer flux threshold isolated by XF-035--XF-040. Equation (3) shows that these are not merely compatible pictures: the exact nonlinear dynamics dominate the periodized Cauchy generator with the correct `1/q` spectral gap.

The line-specific falsification boundary remains finite-window forcing. A finite Xi block does not satisfy (8): its exterior cannot be quotiented away, and it can inject variation through the buffer. Nor does source counting by itself control heat-time depth from the collision boundary. Thus (40) cannot be applied to an arbitrary Xi block by periodically extending it; that would change the exterior dynamics whose control is precisely the missing theorem.

## 8. Consequence for `xi_flow`

XF-039's static microcorrugation and XF-040's exact alternating control no longer leave open the possibility that the two-gap pattern was exceptionally benign. **Every bounded-range periodic microstructure with period `q=o(log T)` is nonlinearly damped through the inverse-buffer amplitude scale in vanishing source heat time.** A persistent negative continuation must therefore use one of two genuinely new resources: exterior replenishment/nonperiodic transport, or a wavelength at least `Theta(log T)` gaps (physical scale `Theta(1)`) where the relaxation time can remain order one.

That gives a sharper target for the next positive step. Instead of trying to control all microscopic flux variation directly, decompose a finite Xi window into sub-`log T` oscillation and longer-wave content. The present finding supplies the exact nonlinear model estimate for why the short-period part should dissipate; translated Xi counting and the XF-036--XF-038 rigidity package are naturally aimed at the longer-wave part. What is still missing is a localized/time-integrated inequality that survives the exterior boundary flux and makes that frequency separation quantitative on the actual Xi flow.