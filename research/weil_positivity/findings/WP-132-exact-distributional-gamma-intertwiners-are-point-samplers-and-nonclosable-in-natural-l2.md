# WP-132 — Exact distributional Gamma intertwiners are point samplers and are nonclosable in the natural L² bridge

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + DISTRIBUTIONAL-CLASSIFICATION + NONCLOSABILITY-OBSTRUCTION + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-131` proves that the canonical Prime-Circle solenoid Gamma semigroup and the radial/Mellin Gamma semigroup admit no nonzero **bounded** exact Hilbert-space intertwiner, but deliberately leaves unbounded and distributional generalized-eigenfunction transforms open. On the canonical Schwartz core that escape can be classified exactly.

Fix `tau>0`. In radial Fourier variable `xi`, write

\[
(T_{\mathbb R}(\tau)f)(\xi)=m_\tau(\xi)f(\xi),
\qquad
m_\tau(\xi)=e^{-\tau H_\infty(\xi)},
\]

where `WP-129` proves that `H_infty(xi)=F(xi^2)` with `F` a nonconstant complete Bernstein function, and on the solenoid character side write

\[
(T_\Sigma(\tau)c)_q=m_\tau(2\pi q)c_q,
\qquad q\in\mathbb Q.
\]

If a continuous linear map

\[
Y:\mathcal S(\mathbb R)\longrightarrow \ell^2(\mathbb Q)
\]

satisfies the exact semigroup intertwining relation

\[
YT_{\mathbb R}(\tau)=T_\Sigma(\tau)Y,
\]

then every output coordinate is forced to be a point-supported distribution on the corresponding Gamma level set. More precisely, for `q != 0`,

\[
\boxed{
(Yf)_q=a_q f(2\pi |q|)+b_q f(-2\pi |q|),
}
\]

while the zero coordinate is at most a first jet,

\[
\boxed{
(Yf)_0=a_0 f(0)+b_0 f'(0).
}
\]

Thus the generalized-eigenfunction escape left by `WP-131` does exist distributionally, but it contains no hidden integral transform: exact Gamma covariance collapses it to rational point sampling (plus the double-root jet at zero).

The Hilbert obstruction then strengthens sharply:

\[
\boxed{
Y\neq0
\quad\Longrightarrow\quad
Y:\mathcal S(\mathbb R)\subset L^2(\mathbb R)\to\ell^2(\mathbb Q)
\text{ is not closable}.
}
\]

Consequently every closable exact intertwiner on the natural radial `L^2` core is zero. In the reverse direction, every closable exact intertwiner whose domain contains the canonical finite-character core is likewise zero. The unbounded escape from `WP-131` therefore survives only by changing the domain/Hilbert geometry, abandoning exact intertwining, or excluding the canonical character core.

There is an additional arithmetic matched control. If one tries to put the exact critical Prime-Lattice/Weil amplitudes of `WP-032` on the reciprocal prime-power character frequencies,

\[
q=p^{-k},
\qquad
c_{p^{-k}}(\sigma)=(\log p)p^{-k\sigma},
\]

then at the Weil value `sigma=1/2` the point sampler is not even `ell^2`-valued on a Schwartz function equal to one near the accumulation point `q=0`:

\[
\sum_{p,k\ge1}|c_{p^{-k}}(1/2)|^2
=
\sum_{p,k\ge1}\frac{(\log p)^2}{p^k}
=\infty.
\]

This independently reproduces the exact `sigma=1/2` threshold of `WP-032` inside the distributional radial–solenoid bridge. Stronger damping `sigma>1/2` restores square summability but **not** `L^2` closability, because nonzero point evaluation remains singular in `L^2`.

No global Weil positivity theorem follows. The durable conclusion is narrower: matching the Gamma symbol on rational frequencies cannot be upgraded from the bounded bridge of `WP-131` to a nonzero closable exact bridge by appealing to generalized eigenfunctions. A viable positive mechanism must change the category or the coupling before positivity is inherited.

## 1. Coordinate distributions are supported on Gamma level sets

Let `pi_q:ell^2(Q)->C` be the `q`th coordinate map and define

\[
L_q=\pi_qY\in\mathcal S'(\mathbb R).
\]

The intertwining identity gives, for every Schwartz function `f`,

\[
L_q(m_\tau f)=m_\tau(2\pi q)L_q(f),
\]

or equivalently

\[
\boxed{
\bigl(m_\tau(\xi)-m_\tau(2\pi q)\bigr)L_q=0
}
\]

as a tempered-distribution identity.

`WP-129` proves `H_infty(xi)=F(xi^2)` with `F` a nonconstant complete Bernstein function. Hence `F'(s)>0` for `s>0`, so `H_infty` and therefore `m_tau` are strictly monotone in `|xi|` away from zero. For `q!=0`,

\[
\{\xi:m_\tau(\xi)=m_\tau(2\pi q)\}
=
\{-2\pi|q|,+2\pi|q|\},
\]

and both zeros of `m_tau(xi)-m_tau(2 pi q)` are simple.

The classical structure theorem for point-supported distributions says that a distribution supported at one point is a finite linear combination of derivatives of the Dirac delta. Multiplication by a smooth function with a simple zero kills only the zeroth delta term: if `g(x_0)=0` and `g'(x_0)!=0`, then `g delta_{x_0}=0` but `g delta'_{x_0}=-g'(x_0)delta_{x_0}!=0`, and higher derivatives fail similarly by descending induction. Therefore

\[
L_q=a_q\delta_{2\pi|q|}+b_q\delta_{-2\pi|q|}
\qquad(q\ne0).
\]

At `q=0`, analyticity and evenness give

\[
H_\infty(\xi)=c\xi^2+O(\xi^4),
\qquad c>0,
\]

so `m_tau(xi)-1` has a zero of exact order two at the origin. The same distribution calculation leaves precisely

\[
L_0=a_0\delta_0+b_0\delta_0'.
\]

This classification uses no zeta zeros and no RH-equivalent input.

## 2. Translation covariance removes the ± degeneracy

The two-point ambiguity is caused only by the even Gamma symbol. If the bridge is also required to respect the underlying radial/leaf translation action,

\[
(U_{\mathbb R}(s)f)(\xi)=e^{is\xi}f(\xi),
\qquad
(U_\Sigma(s)c)_q=e^{2\pi iqs}c_q,
\]

and

\[
YU_{\mathbb R}(s)=U_\Sigma(s)Y,
\]

then each coordinate distribution obeys

\[
(e^{is\xi}-e^{2\pi iqs})L_q=0
\qquad\text{for all }s.
\]

Differentiating at `s=0` gives

\[
(\xi-2\pi q)L_q=0,
\]

hence

\[
\boxed{
(Yf)_q=c_q f(2\pi q).
}
\]

So an exact bridge respecting the full leaf flow is not merely sampling-like; it is a weighted rational point sampler.

## 3. Every nonzero sampler is nonclosable from natural L²

The density of the rational sample set does not rescue closability. First note that well-definedness of `Y:S(R)->ell^2(Q)` forces local square summability of the sampling coefficients. For any compact interval `K` away from zero, choose a Schwartz cutoff that equals one on `K` and vanishes on the reflected interval when needed. The output lies in `ell^2`, so the squared coefficients attached to sample points in `K` have finite sum.

Suppose some nonzero coefficient occurs at a nonzero sample point `lambda_0`. Choose smooth cutoffs `phi_n` with

\[
0\le |\phi_n|\le1,
\qquad
\phi_n(\lambda_0)=1,
\qquad
\operatorname{supp}\phi_n\downarrow\{\lambda_0\}.
\]

Then

\[
\|\phi_n\|_{L^2}\to0.
\]

Local square summability and continuity from above of the resulting atomic coefficient measure imply that all other sampled coordinates in the shrinking support vanish in `ell^2`, while the coefficient vector attached to `lambda_0` remains. Thus

\[
Y\phi_n\longrightarrow v_{\lambda_0}\ne0.
\]

This violates the defining criterion for a closable densely defined operator: `f_n->0` and `Yf_n->v` must force `v=0`.

If the only nonzero coordinate is the zero jet, the same conclusion is immediate. A shrinking bump with value one at zero isolates `delta_0`; a function of the form `x chi(x/epsilon_n)` has derivative one at zero and `L^2` norm tending to zero, isolating `delta_0'`. Hence every nonzero Gamma-distributional intertwiner classified in Section 1 is nonclosable in the natural radial `L^2` geometry.

## 4. Reverse unbounded intertwiners also vanish when the canonical core is retained

Let

\[
X:D(X)\subset\ell^2(\mathbb Q)\to L^2(\mathbb R)
\]

be densely defined and closable, assume `D(X)` is invariant under `T_Sigma(tau)`, contains the finite-support character core `c_00(Q)`, and satisfies

\[
XT_\Sigma(\tau)=T_{\mathbb R}(\tau)X
\]

on its domain. For every basis vector `e_q`, the same eigenvector argument as `WP-131` gives

\[
Xe_q=0,
\]

because the radial heat operator has no nonzero `L^2` eigenvectors.

Now take any `f in D(X)` and approximate it in `ell^2` by `g_n in c_00(Q)`. Since the domain is linear, `h_n=f-g_n` lies in `D(X)`, with

\[
h_n\to0,
\qquad
Xh_n=Xf.
\]

Closability forces `Xf=0`. Therefore

\[
\boxed{X=0\text{ on }D(X).}
\]

A nonzero reverse unbounded exact bridge must consequently exclude the canonical character core or fail closability, both of which require additional justification before they can carry a geometric positivity theorem.

## 5. Critical prime-power sampling fails before closability

The distributional classification gives a direct matched test against the finite arithmetic normalization. Restrict rational samples to

\[
q_{p,k}=p^{-k}
\]

and attach the `WP-032` amplitudes

\[
c_{p,k}(\sigma)=(\log p)p^{-k\sigma}.
\]

Let `f in C_c^infty(R)` equal one on a neighborhood of zero. For all sufficiently large primes, already the `k=1` points satisfy `2 pi/p in supp(f)` and `f(2 pi/p)=1`. Therefore

\[
\|Y_\sigma f\|_{\ell^2}^2
\ge
\sum_{p>P}\frac{(\log p)^2}{p^{2\sigma}}.
\]

The prime sum converges exactly when `2 sigma>1` and diverges when `2 sigma<=1`. Thus

\[
\boxed{
\sigma=\frac12
\quad\Longrightarrow\quad
Y_{1/2}f\notin\ell^2.
}
\]

Including all prime powers gives

\[
\sum_{p,k\ge1}(\log p)^2p^{-2k\sigma}
=
\sum_p\frac{(\log p)^2p^{-2\sigma}}{1-p^{-2\sigma}},
\]

with the same threshold `sigma>1/2`. This is exactly the corrected critical boundary in `WP-032`, now appearing as failure of a generalized-eigenfunction sampling bridge rather than failure of the rank-one Gram completion.

For `sigma>1/2`, the coefficients become square summable, so the sampler is at least `ell^2`-valued on bounded Schwartz functions. Section 3 still shows that any nonzero such point sampler is nonclosable as an operator from `L^2(R)`.

## 6. A zero-mode subtraction is a real escape, but it changes the operator

The critical divergence has an instructive cancellation. Replacing point values by differences

\[
f(2\pi p^{-k})-f(0)
\]

adds a factor `O(p^{-k})` for smooth `f`, so

\[
\sum_{p,k}\frac{(\log p)^2}{p^k}
|f(2\pi p^{-k})-f(0)|^2
\]

converges near the accumulation point. This is a genuine positive star-graph/anchored-difference energy and shows that the divergence is not an argument against every renormalized boundary geometry.

But the subtraction is **not** an exact intertwiner of the diagonal Gamma semigroups. Since `m_tau(0)=1`,

\[
\begin{aligned}
&m_\tau(2\pi q)\,[f(2\pi q)-f(0)]\\
&\qquad\ne
m_\tau(2\pi q)f(2\pi q)-f(0)
\end{aligned}
\]

for `q!=0`. Exact covariance instead induces a triangular coupling to the zero mode proportional to

\[
\bigl(m_\tau(2\pi q)-1\bigr)f(0).
\]

Thus a successful zero-mode counterterm would be **new coupled geometry**, not a hidden distributional equivalence of the two canonical Gamma carriers. It remains a legitimate route only if Mathia forces the subtraction/coupling and an independent positive/coercive theorem for the resulting global object, while the finite Mangoldt and archimedean/polar terms still match the Weil formula.

## 7. Prior-art and novelty audit

No novelty is claimed for the underlying distribution theory. The point-support structure theorem is classical; for example, Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 2.3.4, identifies distributions supported at one point with finite sums of delta derivatives. Standard rigged-Hilbert-space spectral theory likewise places generalized continuous-spectrum eigenvectors in a dual test-function space rather than in the ambient `L^2`; Hayato Chiba, *A spectral theory of linear operators on rigged Hilbert spaces under analyticity conditions*, Advances in Mathematics 273 (2015), 324–379, DOI `10.1016/j.aim.2015.01.001`, is a modern reference.

The directed novelty audit also checked sampling/frame literature, where stable point evaluation is naturally formulated in reproducing-kernel, bandlimited, Sobolev, or other regularity spaces rather than raw `L^2`. This reinforces the category boundary rather than supplying the Mathia result. The claim here is only the exact specialization: `WP-129`'s strictly radial Gamma multiplier plus `PC-065`'s rational character spectrum force every Schwartz-to-solenoid distributional intertwiner into point samples/jets, and those samples cannot provide a nonzero closable bridge in the canonical `L^2` geometry. The critical Mangoldt matched control then lands on the independent `WP-032` threshold.

A bounded search for combinations of arithmetic/universal solenoids, digamma/Gamma heat semigroups, distributional intertwiners, point-supported generalized eigenvectors, and critical prime-power sampling found no source asserting this exact Mathia comparison. That absence is not evidence of historical novelty.

## 8. Falsification surface and surviving routes

The finding is falsified if the canonical data used from `WP-129`, `WP-130`, or `PC-065` are wrong, if the Gamma heat multiplier has additional/non-simple nonzero level-set roots, if an exact coordinate intertwining equation need not imply distributional support on that level set, or if the shrinking-bump sequence can be closable despite converging to a nonzero sampled output. None of these steps uses zeta-zero data.

The theorem does **not** rule out:

- an intrinsically forced source space stronger than `L^2` together with a correspondingly justified target norm;
- a canonical zero-mode quotient/subtraction or boundary counterterm, which necessarily changes the exact diagonal intertwining law;
- a compression, Schur complement, response operator, or new coupled generator;
- a genuinely nonseparable finite–archimedean/radial–leaf geometry whose positivity is proved directly;
- a rigged/distributional construction used only as an intermediate device, provided the final positive form is independently defined and closable in its actual Hilbert category.

What is closed is the specific escape left by `WP-131`: **generalized eigenfunctions do not turn the two existing Gamma semigroups into a nonzero closable exact Hilbert bridge.**

## Research consequence

The radial–solenoid Gamma route now has a sharper boundary. Bounded exact intertwiners vanish (`WP-131`); distributional exact intertwiners are forced to rational point samplers/jets; every nonzero such sampler is nonclosable from natural radial `L^2`; and the exact critical Mangoldt weights fail even `ell^2` output at the rational accumulation point.

The interesting residual is therefore not “allow distributions.” It is to derive a **specific category-changing counterterm or coupled boundary geometry** — such as the zero-mode subtraction exposed above — and then prove that its positivity is intrinsic rather than a renormalized restatement of the Weil functional.