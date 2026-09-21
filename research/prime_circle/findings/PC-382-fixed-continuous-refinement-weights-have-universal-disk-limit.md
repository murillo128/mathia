# PC-382 — fixed continuous refinement weights have a universal disk spectral limit

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the regular infinite-Fourier-tail branch left open by PC-381. PC-380 gives an exact QMF/isometry collapse for the common-anchor chord, and PC-381 extends that exact collapse to every fixed finite-bandwidth scalar weight once the covering degree exceeds the Fourier bandwidth. The present result removes the finite-bandwidth hypothesis for every fixed nonzero continuous scalar branch weight.

Let

\[
(V_m f)(z)=f(z^m),\qquad z\in\mathbb T,
\]

on `L^2(T,dm)` with normalized Haar measure, and let `q in C(T)` be fixed, nonzero, and independent of the refinement degree `m`. Put

\[
S_{m,q}=M_qV_m,
\qquad
c_q=\int_{\mathbb T}|q|^2\,dm>0,
\qquad
T_{m,q}=c_q^{-1/2}S_{m,q}.
\]

Then the exact fiber-energy identity is

\[
T_{m,q}^*T_{m,q}
=M_{A_m},
\qquad
A_m(z)=\frac1{c_qm}\sum_{w^m=z}|q(w)|^2.
\]

The `m` inverse images form one rotated regular `m`-gon. Uniform continuity alone therefore forces their average to converge **uniformly in the base point** to Haar energy. If `\omega_g` is the circle modulus of continuity of `g=|q|^2`,

\[
\boxed{
\|A_m-1\|_\infty
\le
\frac{\omega_g(2\pi/m)}{c_q}
=: \delta_m
\longrightarrow0.
}
\]

For every sufficiently large `m`, `\delta_m<1`, so `T_{m,q}` is bounded below. More strongly, its adjoint spectrum is squeezed between two concentric disks,

\[
\boxed{
\sqrt{1-\delta_m}\,\overline{\mathbb D}
\subseteq
\sigma(T_{m,q}^*)
\subseteq
\sqrt{1+\delta_m}\,\overline{\mathbb D}.
}
\]

Hence

\[
\boxed{
\sigma(T_{m,q}^*)
\xrightarrow[m\to\infty]{\rm Hausdorff}
\overline{\mathbb D}.
}
\]

The convergence holds along prime degrees, composite degrees, or any sequence `m -> infinity`. Thus a fixed continuous one-point weight may retain arbitrarily long exact Fourier support, but after its intrinsic `L^2` normalization it cannot retain an order-one prime-sensitive spectral shape in the large-refinement limit. The result closes the regular infinite-tail loophole in PC-381; the surviving scalar loopholes must vary on the refinement scale, become singular with `m`, or otherwise leave this fixed-profile setting.

## 1. Exact fiber norm formula

The power-map Koopman operator is an isometry and its adjoint averages over inverse images,

\[
(V_m^*h)(z)=\frac1m\sum_{w^m=z}h(w).
\]

Therefore

\[
\begin{aligned}
S_{m,q}^*S_{m,q}
&=V_m^*M_{|q|^2}V_m\\
&=M_{E_m(|q|^2)},
\end{aligned}
\]

where

\[
(E_m g)(z)=\frac1m\sum_{w^m=z}g(w).
\tag{1}
\]

After normalization by `c_q`, this gives the displayed formula for `A_m`. PC-381 identifies the Fourier selector behind (1): whenever a Fourier representation is legitimate termwise, `E_m` keeps only frequencies divisible by `m`. The argument below does not require absolute Fourier summability or any finite support.

## 2. Rotated root fibers are uniformly equidistributed for every fixed continuous profile

Write `z=e^{it}`, `0<=t<2pi`, and

\[
w_j=e^{i(t+2\pi j)/m},\qquad 0\le j<m.
\]

Let `h(theta)=g(e^{itheta})`. The points

\[
\theta_j=\frac{t+2\pi j}{m}
\]

place exactly one sample in each interval

\[
I_j=[2\pi j/m,2\pi(j+1)/m].
\]

Comparing each sample with the average of `h` over its own interval gives

\[
\begin{aligned}
\left|
\frac1m\sum_{j=0}^{m-1}h(\theta_j)
-
\frac1{2\pi}\int_0^{2\pi}h(\theta)\,d\theta
\right|
&\le
\frac1m\sum_{j=0}^{m-1}
\sup_{u,v\in I_j}|h(u)-h(v)|\\
&\le \omega_g(2\pi/m).
\end{aligned}
\tag{2}
\]

The bound is independent of `t`. Since the integral equals `c_q`, equations (1)--(2) yield

\[
\|T_{m,q}^*T_{m,q}-I\|
=\|A_m-1\|_\infty
\le\delta_m\to0.
\tag{3}
\]

Thus every fixed continuous scalar branch profile is asymptotically QMF in operator norm, even when its exact Fourier series is infinite or poorly summable. For a fixed Holder profile this immediately gives a power rate through its modulus of continuity; smoother periodic profiles have the familiar faster trapezoidal convergence, but no regularity beyond continuity is needed for (3).

## 3. Bounded-below weighted covers force a disk into the adjoint point spectrum

Equation (3) alone controls singular values but not, by itself, the spectrum of a nonnormal operator. The missing step is supplied by the large defect of the `m`-to-one cover.

For `delta_m<1`, define the minimum modulus and norm

\[
\alpha_m:=\inf_{\|f\|=1}\|T_{m,q}f\|,
\qquad
\beta_m:=\|T_{m,q}\|.
\]

Then

\[
\alpha_m\ge\sqrt{1-\delta_m},
\qquad
\beta_m\le\sqrt{1+\delta_m}.
\tag{4}
\]

Because `T_{m,q}` is bounded below, its range is closed and

\[
R_m:=T_{m,q}(T_{m,q}^*T_{m,q})^{-1}
\]

is a bounded right inverse of the adjoint,

\[
T_{m,q}^*R_m=I,
\qquad
\|R_m\|=\alpha_m^{-1},
\qquad
\operatorname{Ran}R_m=\operatorname{Ran}T_{m,q}.
\tag{5}
\]

Moreover `K_m:=ker T_{m,q}^*` is infinite dimensional. Fiberizing over `z=w^m`, the range has at each base point the one-dimensional fiber spanned by

\[
(q(w_0),\ldots,q(w_{m-1}))\in\mathbb C^m,
\]

which is nonzero almost everywhere because `A_m>=1-delta_m>0`. Its orthogonal complement has dimension `m-1` on every fiber, and the direct integral of those complements is infinite dimensional.

Now fix `|lambda|<alpha_m` and any `k in K_m`. Since `|lambda|\|R_m\|<1`, set

\[
y=(I-\lambda R_m)^{-1}\lambda R_mk.
\tag{6}
\]

Every term in the Neumann expansion of `y` lies in `Ran T_{m,q}`, so `y perp K_m`. Equation (6) is equivalent to

\[
y=\lambda R_m(k+y).
\]

Applying `T_{m,q}^*` and using (5) gives

\[
T_{m,q}^*(k+y)=\lambda(k+y).
\tag{7}
\]

The map `k -> k+y` is injective because its orthogonal projection onto `K_m` is `k`. Therefore every `|lambda|<alpha_m` is an eigenvalue of `T_{m,q}^*` of infinite multiplicity. Closedness of the spectrum gives

\[
\alpha_m\overline{\mathbb D}
\subseteq \sigma(T_{m,q}^*).
\tag{8}
\]

The trivial norm bound gives

\[
\sigma(T_{m,q}^*)\subseteq\beta_m\overline{\mathbb D}.
\tag{9}
\]

Combining (4), (8), and (9) proves the spectral sandwich and the Hausdorff convergence to the unit disk.

This is stronger than saying that `T_{m,q}` is close to some isometry: the **actual spectrum of its adjoint** is trapped between disks whose radii both tend to one.

## 4. Geometric controls and the singular boundary

The theorem contains the two preceding refinement results as stronger special cases. For the anchored complex chord `q(z)=1-z`, PC-380 has `A_m=1` exactly after RMS normalization for every `m>=2`. For every fixed Laurent-polynomial weight, PC-381 has the same exact equality once `m` exceeds the Fourier bandwidth of `|q|^2`. PC-382 says that an infinite Fourier tail does not evade the collapse when it comes from one fixed continuous geometric profile: the exact equality becomes a uniform asymptotic equality and the full adjoint spectrum converges to the same disk.

This includes any fixed continuous function of the anchored chord or chord phase, provided the resulting weight is not identically zero. It also classifies every **fixed bounded regularization** of a singular chord amplitude. For example, for fixed `epsilon>0`,

\[
q_{\alpha,\varepsilon}(z)
=\bigl(|1-z|^2+\varepsilon^2\bigr)^{-\alpha/2}
\]

is continuous and therefore has the same normalized disk limit.

The literal inverse chord, inverse powers, and `log|1-z|` are different: as multiplication operators on the canonical Haar `L^2` space they are unbounded, so they do not define bounded `S_{m,q}` in this framework. A singular regularization `epsilon=epsilon_m -> 0` can also defeat the common modulus of continuity at the same time as the root mesh shrinks. Such mesh-scale families are not covered and remain a genuine boundary rather than being silently absorbed into the theorem.

The same warning applies to conductor-dependent weights `q_m`, even if each individual `q_m` is continuous. Equation (2) only yields a useful collapse when the family has a modulus of continuity small on the `2pi/m` mesh; this is precisely where the fixed-profile hypothesis enters.

## 5. Prior-art and novelty audit

The operator setting is classical transfer/QMF theory. Bratteli, Evans and Jorgensen, **Compactly supported wavelets and representations of the Cuntz relations**, *Applied and Computational Harmonic Analysis* 8 (2000), 166--196, DOI `10.1006/acha.2000.0283`, develops the quadrature-mirror-filter/Cuntz-isometry framework in which constant preimage energy produces an isometric weighted composition operator. That is the exact mechanism already identified in PC-380 and PC-381.

Xianghong Chen and Hans Volkmer, **On transfer operators on the circle with trigonometric weights**, *Journal of Fractal Geometry* 5 (2018), 351--386, DOI `10.4171/JFG/64`, study the same circle endomorphism transfer form

\[
(Lu)(t)=\frac1d\sum_{i=0}^{d-1} f\!\left(\frac{t+i}{d}\right)\,u\!\left(\frac{t+i}{d}\right)
\]

for trigonometric weights including powers of sine and cosine. Thus weighted root-fiber transfer on the circle is established classical territory, including weights geometrically equivalent to chord profiles.

The additional ingredient in PC-382 is elementary periodic quadrature: the rotated `m`-root fiber is an equally spaced Riemann sum, and continuity gives the uniform estimate (2). Periodic trapezoidal convergence and its stronger smooth/analytic rates are classical numerical/harmonic analysis. The disk inclusion (8) is a direct bounded-operator argument from a right inverse and infinite adjoint defect; no new general operator theorem is claimed.

Accordingly, **no historical novelty is claimed for the abstract theorem**. The durable Prime-Circle content is the boundary classification: after PC-381's finite-bandwidth result, merely replacing a finite Fourier mask by any fixed continuous infinite-tail one-point geometric mask still cannot produce an order-one prime-sensitive spectrum. The mechanism is uniform root-fiber equidistribution plus classical left-invertible weighted-cover geometry.

No zeta factor, completed functional equation, gamma factor, zero divisor, or distinguished real part `1/2` appears. The result is prime-blind and is exactly matched by composite covering degrees.

## 6. Research consequence

The branch

\[
\boxed{
\text{fixed continuous scalar geometry on one power-map branch}
\longrightarrow
\text{infinite Fourier tail}
\longrightarrow
\text{new large-degree spectral shape}
\]

is closed on the canonical Haar `L^2` refinement space. Finite Fourier bandwidth was not the essential reason for the PC-381 collapse; **fixed regularity at the inverse-image mesh scale** is enough.

What remains outside this result is materially sharper: conductor-dependent profiles whose variation stays at scale `1/m`; singular or shrinking regularizations with a justified domain/renormalization; a deliberate magnification of the vanishing defect `A_m-1` with an independently forced scale; matrix-valued or nonlinear branch data; source/shell dependence that couples different fibers before scalarization; genuinely cross-level nonseparable operators; and the global uniformization/accessory sector. A future candidate in this refinement branch should demonstrate one of those escapes rather than only replace a finite Fourier mask by a fixed continuous one.
