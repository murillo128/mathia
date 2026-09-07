# AF-191 — Linear-complexity Euler clusters obey a saddle-point fidelity law

**Status:** `EXACT-DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `LITERATURE-CONTEXT`, `NO-NOVELTY-CLAIM`

## Claim

AF-190 leaves open the growing-overlap regime `m/q^2 -> 0` for the positive parity-split controls. The first nontrivial part of that boundary has a different exact mechanism from both AF-189 and AF-190: when the cancellation order grows only linearly with the reciprocal-band index, the dominant Euler harmonic is no longer the first harmonic reached at the band edge. A lower harmonic wins by balancing its larger Euler coefficient against the off-resonance penalty of the finite-difference filter.

Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
a=\sigma x>0,
\qquad
r=e^{-a}\in(0,1).
\tag{1}
\]

Let `\delta\downarrow0`, and let positive integers `q=q_\delta` and `m=m_\delta` satisfy

\[
q_\delta\to\infty,
\qquad
\kappa_\delta:=\frac{m_\delta}{q_\delta}\in[\kappa_-,\kappa_+]
\subset(0,\infty),
\qquad
m_\delta q_\delta\delta\longrightarrow0.
\tag{2}
\]

Use the normalized positive parity-split controls of AF-182--AF-190,

\[
\nu_\delta
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta},
\tag{3}
\]

and the Euler local logarithm

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+it.
\tag{4}
\]

Put

\[
T_\delta=\frac{\pi}{q_\delta\delta},
\qquad
D_\delta=
\sup_{|t|\le T_\delta}
\left|
\int F_{\sigma+it}(u)\,d\nu_\delta(u)
\right|.
\tag{5}
\]

For `\kappa>0` define

\[
f_{a,\kappa}(\alpha)
=-a\alpha
+\kappa\log\sin\frac{\pi\alpha}{2},
\qquad 0<\alpha\le1.
\tag{6}
\]

It is strictly concave and has the unique maximizer

\[
\boxed{
\alpha_*(a,\kappa)
=
\frac{2}{\pi}
\arctan\frac{\pi\kappa}{2a}
\in(0,1).
}
\tag{7}
\]

Write

\[
\Psi(a,\kappa)
=f_{a,\kappa}(\alpha_*)
=
-\frac{2a}{\pi}
\arctan\frac{\pi\kappa}{2a}
+
\kappa\log
\frac{\pi\kappa}
{\sqrt{4a^2+\pi^2\kappa^2}},
\tag{8}
\]

and

\[
H(a,\kappa)
=
- f_{a,\kappa}''(\alpha_*)
=
\frac{a^2}{\kappa}
+
\frac{\pi^2\kappa}{4},
\tag{9}
\]

\[
C(a,\kappa)
=
\frac{2}{\alpha_*(a,\kappa)}
\sqrt{\frac{2\pi}{H(a,\kappa)}}.
\tag{10}
\]

Then, uniformly for `\kappa_\delta` in the fixed compact interval of `(2)`,

\[
\boxed{
D_\delta
=
\bigl(C(a,\kappa_\delta)+o(1)\bigr)
q_\delta^{-1/2}
\exp\!\left[
q_\delta\Psi(a,\kappa_\delta)
\right].
}
\tag{11}
\]

In particular, if `\kappa_\delta\to\kappa\in(0,\infty)`, then

\[
\frac{1}{q_\delta}\log D_\delta
\longrightarrow
\Psi(a,\kappa).
\tag{12}
\]

The dominant harmonic index satisfies

\[
\boxed{
\frac{k_*}{q_\delta}
\longrightarrow
\alpha_*(a,\kappa)<1.
}
\tag{13}
\]

Thus the `k=q` isolated-resonance picture of AF-189 does not merely lose a sharp constant when `m/q^2` becomes small. At linear source complexity the whole maximizing channel moves into the sub-band harmonic range `k<q`. The fidelity exponent is selected by a saddle-point competition between Euler attenuation and finite-difference cancellation.

## Exact response and the zero-damping envelope

Write `q=q_\delta`, `m=m_\delta`, `\theta=t\delta`, and

\[
R_\delta(t)
=
\int F_{\sigma+it}(u)\,d\nu_\delta(u).
\tag{14}
\]

The exact harmonic expansion from AF-187--AF-190 is

\[
R_\delta(t)
=
2^{1-m}
\sum_{k\ge1}
\frac{r^k e^{-iktx}}{k}
\left(e^{-k(\sigma+it)\delta}-1\right)^m.
\tag{15}
\]

Set

\[
b_{k,\delta}(\theta)
=
\frac{|1-e^{-k\sigma\delta}e^{-ik\theta}|}{2}.
\tag{16}
\]

For `1\le k<q` and `|\theta|\le\pi/q`, the triangle inequality and monotonicity of sine on `[0,\pi/2]` give

\[
b_{k,\delta}(\theta)
\le
\sin\frac{\pi k}{2q}
+
\frac{1-e^{-k\sigma\delta}}2.
\tag{17}
\]

Since

\[
\sin\frac{\pi k}{2q}\ge\frac{k}{q}
\tag{18}
\]

and `1-e^{-k\sigma\delta}\le k\sigma\delta`, equation `(17)` yields uniformly for all `1\le k<q`,

\[
\boxed{
b_{k,\delta}(\theta)
\le
\left(1+\frac{\sigma q\delta}{2}\right)
\sin\frac{\pi k}{2q}.}
\tag{19}
\]

The assumptions imply `m q\delta\to0`, so

\[
\left(1+\frac{\sigma q\delta}{2}\right)^m=1+o(1).
\tag{20}
\]

Therefore the entire sub-band contribution is bounded by `1+o(1)` times the positive zero-damping edge sum

\[
S_q
=
2\sum_{k=1}^{q-1}
\frac{e^{-ak}}{k}
\sin^m\frac{\pi k}{2q}.
\tag{21}
\]

For `k\ge q`, no localization is needed:

\[
2\sum_{k\ge q}\frac{r^k}{k}b_{k,\delta}(\theta)^m
\le
\frac{2r^q}{q(1-r)}.
\tag{22}
\]

The theorem therefore reduces first to identifying the sharp asymptotic scale of `(21)` and then to showing that the continuous vertical band can attain that positive envelope asymptotically.

## Saddle point and discrete Laplace asymptotic

Put `\alpha=k/q` and `\kappa=m/q`. Every summand in `(21)` can be written as

\[
\frac1q\,
\frac{2}{\alpha}
\exp\!\left[q f_{a,\kappa}(\alpha)\right].
\tag{23}
\]

The derivatives are

\[
f_{a,\kappa}'(\alpha)
=-a
+\frac{\pi\kappa}{2}
\cot\frac{\pi\alpha}{2},
\tag{24}
\]

and

\[
f_{a,\kappa}''(\alpha)
=-\frac{\pi^2\kappa}{4}
\csc^2\frac{\pi\alpha}{2}<0.
\tag{25}
\]

Thus `(7)` is the unique critical point and the unique global maximum. At the endpoint,

\[
f_{a,\kappa}(1)=-a,
\tag{26}
\]

while strict interior maximality gives

\[
\boxed{\Psi(a,\kappa)>-a.}
\tag{27}
\]

Because `\kappa` is restricted to a compact subset of `(0,\infty)`, the saddle `\alpha_*` stays uniformly away from both endpoints, its curvature `H` stays bounded above and below by positive constants, and `(27)` has a uniform positive gap. Standard discrete Laplace asymptotics for positive sums applied to `(23)` therefore give, uniformly in that compact `\kappa` range,

\[
\boxed{
S_q
=
\bigl(C(a,\kappa)+o(1)\bigr)
q^{-1/2}e^{q\Psi(a,\kappa)}.
}
\tag{28}
\]

The `q^{-1/2}` factor is important. Unlike the finite-overlap regime of AF-190, where only order-one many neighboring harmonics survive, the linear-complexity saddle has width `O(q^{-1/2})` in `\alpha`, hence contains `O(\sqrt q)` harmonics. Their collective contribution supplies the Gaussian Laplace prefactor in `(28)`.

Equation `(27)` also shows that the tail `(22)` is exponentially smaller than `(28)`. Combining `(19)`--`(22)` and `(28)` proves

\[
D_\delta
\le
\bigl(C(a,\kappa_\delta)+o(1)\bigr)
q^{-1/2}e^{q\Psi(a,\kappa_\delta)}.
\tag{29}
\]

## Microscopic phase alignment makes the saddle envelope sharp

The remaining issue is phase: `(21)` is a magnitude envelope, while `(15)` is a complex harmonic sum. The continuous band again contains a much finer phase mesh than the scale on which the saddle profile changes.

Ignoring real damping, for `0<k\theta<2\pi`,

\[
e^{-ik\theta}-1
=-2i e^{-ik\theta/2}
\sin\frac{k\theta}{2}.
\tag{30}
\]

Hence, apart from the common factor `(-i)^m`, the `k`-th term in `(15)` has zero-damping phase

\[
\exp\!\left[
-ik\theta
\left(\frac{x}{\delta}+\frac m2\right)
\right].
\tag{31}
\]

Set

\[
A_\delta=\frac{x}{\delta}+\frac m2.
\tag{32}
\]

Choose the largest phase-alignment mesh point

\[
\theta_*
=
\frac{2\pi\ell_\delta}{A_\delta}
\le
\frac{\pi}{q}.
\tag{33}
\]

Since `m\delta\to0`, the mesh spacing is `O(\delta)`, so

\[
0\le
\frac{\pi}{q}-\theta_*
=O(\delta).
\tag{34}
\]

For every harmonic in a fixed neighborhood of the saddle `k/q=\alpha_*(a,\kappa_\delta)`, the sine factor at `\theta_*` differs relatively from its band-edge value by `1+O(q\delta)`. Raising that ratio to the `m`-th power changes it by

\[
\exp[O(mq\delta)]=1+o(1).
\tag{35}
\]

At the same time, `(33)` makes every zero-damping phase in `(31)` exactly equal. Restoring `e^{-k\sigma\delta}` perturbs each factor by relative size `O(q\delta)` throughout the saddle neighborhood, so after the `m`-th power both magnitude and phase change by `o(1)` because `mq\delta\to0`.

Strict concavity gives an exponential gap outside any fixed saddle neighborhood, and `(27)` makes all `k\ge q` harmonics exponentially negligible on the main scale. Consequently the aligned saddle block adds with common phase and magnitude `(1+o(1))S_q`, while the complete remainder is `o(S_q)`. Thus

\[
|R_\delta(\theta_*/\delta)|
=
(1+o(1))S_q.
\tag{36}
\]

The chosen frequency lies inside the declared band by `(33)`, so `(28)` and `(36)` prove the lower bound matching `(29)`, hence `(11)`.

This alignment is an intrinsic feature of observing a continuous vertical interval. A fixed or sparse sampling grid may miss the `O(\delta)` phase mesh and requires a separate aliasing/Diophantine analysis.

## What the saddle law says about the overlap transition

The dimensionless quantity controlling the maximizing mechanism has changed. AF-190 uses `m/q^2` because neighboring reciprocal resonances separated by `q^{-2}` are individually resolved when the filter width becomes comparable to that spacing. Here `m/q` is order one, so order `\sqrt q` neighboring harmonics overlap and the correct variable is the macroscopic harmonic fraction `\alpha=k/q`.

For large fixed `\kappa`,

\[
\alpha_*(a,\kappa)
=
1-
\frac{4a}{\pi^2\kappa}
+O(\kappa^{-3}),
\tag{37}
\]

and

\[
\Psi(a,\kappa)
=
-a+
\frac{2a^2}{\pi^2\kappa}
+O(\kappa^{-3}).
\tag{38}
\]

Thus increasing linear cancellation order pushes the maximizing harmonic back toward the band edge and drives the exponential rate toward the isolated-resonance rate `-a`. This is consistent with, but is not a uniform consequence of, the AF-190 finite-overlap theorem; the two results use different simultaneous scalings.

For small fixed `\kappa`,

\[
\alpha_*(a,\kappa)
=\frac{\kappa}{a}+O(\kappa^3),
\tag{39}
\]

and

\[
\Psi(a,\kappa)
=
\kappa\left(
\log\frac{\pi\kappa}{2a}-1
\right)
+O(\kappa^3).
\tag{40}
\]

This identifies the direction of the next boundary but does not provide a theorem uniform as `m/q -> 0`. In that regime the saddle itself approaches the small-harmonic endpoint and a different rescaling is required.

## Falsification and boundaries

The conclusion is deliberately specific.

- The source pair is the AF-182 positive parity-split family. A different source class can have a different cancellation profile.
- The destination kernel is the Euler local logarithm with monotone harmonic weights `e^{-ak}/k`. Replacing those weights changes both the saddle equation and possibly the number or location of maximizing channels.
- The observation is a continuous vertical band. Sparse frequency sampling need not realize the phase alignment used for sharpness.
- The compact lower and upper bounds on `m/q` are part of the theorem. Neither `m/q -> 0` nor `m/q -> infinity` is covered uniformly by `(11)`.
- The condition `mq\delta->0` is what makes real damping and phase perturbation negligible across the `O(\sqrt q)` saddle block. A nonzero damping scale changes the exponent/profile.
- The theorem is a sharp forward discrepancy law for one generalized-prime matched-control family. It does not establish a stable inverse theorem for all source systems.
- Nothing here distinguishes rational primes from Beurling or other generalized Euler-product systems. The local prime-power harmonic ladder used in the proof belongs to the wider Euler-product category.

The reusable fidelity lesson is narrower and exact: once source complexity and observation bandwidth vary together, the destination kernel can select a **moving internal channel** rather than merely preserve or erase a fixed discriminator. A recovery audit therefore has to optimize over the kernel's internal harmonic channels before treating a nominal bandwidth edge as the information boundary.

## Prior art and novelty assessment

The asymptotic tool is classical. Richard B. Paris, **“The discrete analogue of Laplace's method,”** *Computers & Mathematics with Applications* 61(10) (2011), 3024--3034, DOI `10.1016/j.camwa.2011.03.092`, gives a justification of discrete Laplace asymptotics for positive-term sums and higher-order expansions. The clustered-observation context is also mature: Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **“Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes,”** *SIAM Journal on Matrix Analysis and Applications* 41(1) (2020), 199--220, DOI `10.1137/18M1212197`, proves sharp partial-Fourier conditioning bounds whose exponents depend on cluster size. Donoho's 1992 superresolution work and the later clustered-source literature already establish that resolution and source complexity interact nontrivially.

A targeted search over weighted trigonometric power sums, discrete Laplace asymptotics, finite differences of logarithmic/Euler kernels, and clustered Fourier recovery did not identify an authoritative source stating the specialized law `(11)` for the Euler logarithm and the AF-182 parity controls. That search is not evidence of priority, and no novelty claim is made. The durable contribution here is the exact closure of the finite-linear-complexity subregime left open by AF-190 and the identification of its moving-harmonic saddle.

## Dependencies and evidence boundary

The proof uses the exact Euler harmonic response and parity controls already established in AF-182 and reused in AF-187--AF-190. The new mathematical step is the uniform reduction to the edge sum `(21)`, its strictly concave saddle `(6)`--`(10)`, and the matching phase-aligned lower bound `(30)`--`(36)`.

No numerical experiment is used as evidence. No RH consequence, rational-prime uniqueness statement, or general inverse theorem follows from this finding. The remaining growing-overlap region includes `m/q -> infinity` with `m/q^2 -> 0`, where the saddle approaches the edge on an intermediate scale, and `m/q -> 0`, where the saddle approaches the small-harmonic endpoint.