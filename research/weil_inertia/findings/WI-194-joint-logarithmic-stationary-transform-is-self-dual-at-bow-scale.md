# WI-194 — joint logarithmic stationary transform is self-dual at bow scale

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-193 shows that even ideal square-root cancellation in every fixed shifted-prime fiber is insufficient below the quarter-scale bow threshold if the shifts are assembled through absolute values. It therefore redirects the source problem toward an estimate that keeps the shift family coupled. The most immediate phase-only implementation of that advice is to replace the fixed-`h` treatment by a joint two-variable Poisson/stationary transform of the source phase.

At the count-saturating bow scale that direct route has an exact obstruction. After writing `n=m+h` and

\[
A:=\frac{U}{2\pi},
\qquad
\phi(m,n):=A\log\frac{n}{m},
\tag{1}
\]

the two-dimensional stationary map sends the phase to **the same logarithmic-ratio phase** on the dual lattice. Moreover, when `m,n\asymp X`, `A\asymp X^2`, and `0<n-m\lesssim K`, the source diagonal strip of width `K` maps to a dual diagonal strip of width `\asymp K`, the central dual scale remains `\asymp X`, and the stationary-phase Jacobian/amplitude is order one. Thus the direct joint transform preserves the `\asymp XK` number of active phase cells rather than compressing them.

Consequently a bare two-dimensional B/Poisson transform does **not** supply the cross-shift saving required by WI-193. It merely reparametrizes the same logarithmic oscillation. This does not rule out two-variable arithmetic methods: a dispersion estimate, bilinear decomposition, large sieve, spectral decomposition, or another argument that uses the von-Mangoldt coefficients jointly may still obtain cancellation. The obstruction is specifically to expecting the nondegenerate two-dimensional phase geometry by itself to create the missing dimensional gain.

No zeta-zero proportion changes here, and no estimate for the actual prime-weighted covariance is claimed.

## 1. Exact joint source phase

On the central dyadic source block of WI-188 and WI-193, the off-diagonal object has the schematic form

\[
\mathcal S(U;X,H)
=
\sum_{1\le h\lesssim K}
\sum_{m\asymp X}
\Lambda(m)\Lambda(m+h)w(m,h)
 e\!\left(A\log\left(1+\frac hm\right)\right),
\qquad
K=\frac XH.
\tag{2}
\]

Set `n=m+h`. Then the phase is exactly

\[
A\log\left(1+\frac hm\right)
=A\log\frac nm
=\phi(m,n).
\tag{3}
\]

Ignoring the arithmetic coefficients only for the purpose of testing the **phase transform**, a two-dimensional Poisson/stationary term with dual frequencies `(r,s)\in\mathbb Z^2` has oscillatory phase

\[
\phi(m,n)-rm-sn.
\tag{4}
\]

Its stationary equations are

\[
-\frac A m=r,
\qquad
\frac A n=s.
\tag{5}
\]

Thus the relevant frequency quadrant has `r<0<s`. Put

\[
p:=-r>0,
\qquad
q:=s>0.
\tag{6}
\]

Then the critical point is exactly

\[
\boxed{
 m=\frac A p,
 \qquad
 n=\frac A q.
}
\tag{7}
\]

Since the source has `n>m`, equation (7) gives `p>q`.

## 2. The Legendre phase is the same logarithmic ratio

Evaluate (4) at the critical point. Using `r=-p`, `s=q`,

\[
\begin{aligned}
\phi(m,n)-rm-sn
&=A\log\frac nm+pm-qn\\
&=A\log\frac{A/q}{A/p}+A-A\\
&=\boxed{A\log\frac pq}.
\end{aligned}
\tag{8}
\]

Thus the joint stationary transform closes on the same phase family:

\[
\boxed{
A\log\frac nm
\longleftrightarrow
A\log\frac pq.
}
\tag{9}
\]

This is the two-variable form of the logarithmic Legendre self-duality already implicit in the one-dimensional B-process machinery used around WI-191--WI-193. Applying the same critical-point calculation to the dual phase returns the reciprocal-coordinate map, up to the corresponding sign/orientation convention. Hence there is no new phase family after one joint transform that could by itself be expected to have a more favorable oscillation scale.

## 3. The diagonal strip is preserved at the count-saturating scale

The stationary map also preserves the geometry that matters for the bow count. From (7),

\[
p-q
=A\left(\frac1m-\frac1n\right)
=\boxed{\frac{A(n-m)}{mn}}.
\tag{10}
\]

Suppose the smooth dyadic localization keeps

\[
c_1X\le m,n\le c_2X,
\qquad
0<n-m\le C_0K,
\tag{11}
\]

with fixed positive constants, while the count-saturating regime has

\[
A\asymp X^2.
\tag{12}
\]

Then (7) gives

\[
p,q\asymp \frac AX\asymp X,
\tag{13}
\]

and (10) gives, uniformly on the localized block,

\[
\boxed{p-q\asymp n-m.}
\tag{14}
\]

In particular the source strip `0<n-m\lesssim K` maps to a dual strip `0<p-q\lesssim K` up to fixed localization constants. A dyadic diagonal strip at central scale `X` and width `K\ll X` contains `\asymp XK` lattice cells; the dual stationary region has the same scale and the same order of lattice cells.

This is the relevant conservation law for WI-193. The desired joint gain cannot come merely from replacing `K` fixed-shift fibers by a nominally two-dimensional stationary transform, because the transform still leaves `\asymp XK` active dual cells in a strip of comparable width.

## 4. Hessian and local amplitude do not create a hidden gain

The Hessian of (1) is diagonal:

\[
\nabla^2\phi(m,n)
=
\begin{pmatrix}
 A/m^2 & 0\\
 0 & -A/n^2
\end{pmatrix},
\tag{15}
\]

so

\[
\det\nabla^2\phi
=-\frac{A^2}{m^2n^2}.
\tag{16}
\]

At `m,n\asymp X` and `A\asymp X^2`,

\[
\left|\det\nabla^2\phi\right|\asymp1,
\qquad
\left|\det\nabla^2\phi\right|^{-1/2}
=\frac{mn}{A}\asymp1.
\tag{17}
\]

Equivalently, the Jacobian of the stationary-coordinate map `(m,n)\mapsto(p,q)=(A/m,A/n)` has absolute determinant

\[
\left|\frac{\partial(p,q)}{\partial(m,n)}\right|
=\frac{A^2}{m^2n^2}
\asymp1.
\tag{18}
\]

Thus neither local density nor the leading stationary amplitude supplies a power saving at the count-saturating scale. The transform is nondegenerate, but nondegeneracy here means a stable change of phase coordinates, not compression.

## 5. What the barrier does and does not rule out

The von-Mangoldt weights in (2) are not smooth amplitudes, so equations (5)--(18) are deliberately **not** asserted as a black-box asymptotic transformation formula for the arithmetic sum. To turn Poisson/stationary phase into a theorem for (2), the arithmetic coefficients would first have to be decomposed or handled by a method compatible with them. That is precisely where additional information can enter.

The exact negative conclusion is narrower and robust:

\[
\boxed{
\text{raw joint logarithmic phase transform}
\;\not\Rightarrow\;
\text{automatic cross-shift power saving at }X\asymp\sqrt U.
}
\tag{19}
\]

A successful joint argument must exploit something not present in the phase geometry alone. Examples include cancellation among arithmetic coefficients after a bilinear/dispersion decomposition, an arithmetic large sieve that keeps the physical shift labels coupled, a spectral/Kloosterman transform with a genuinely favorable coefficient norm, or another source-specific invariant. Such methods may still use Poisson or stationary phase internally; WI-194 only prevents counting the self-dual transform itself as the missing `K^\theta` gain from WI-193.

The same distinction prevents overreading the lattice count. `\asymp XK` dual stationary cells do not prove that the true dual arithmetic sum is large. They prove only that the first transform has not reduced the number or scale of degrees of freedom. Any saving must be established through cancellation between those cells rather than through phase-space compression.

## 6. Prior-art and novelty audit

Multidimensional Poisson summation, stationary phase, and Legendre-coordinate transformations are classical. For the exact logarithmic zeta phase, WI-193 already records Olivier Robert, *On van der Corput's k-th derivative test for exponential sums*, Indagationes Mathematicae 27:2 (2016), 559--589, especially its review of the logarithmic A/B-process, together with the Graham--Kolesnik exponent-pair framework. WI-191--WI-192 establish the closely related one-dimensional Atkinson duality and the failure of a second pure B-process to create a new phase resource.

A bounded external audit for the present question located generic multidimensional stationary-phase/Legendre machinery but no source asserting this exact specialization: the simultaneous map `(m,n)=(A/p,A/q)`, the identity (8), and the preservation (14)--(18) of the count-saturating bow strip. That absence is **not** evidence of priority. The durable content claimed here is the exact derivation and its consequence for the live Mathia route, not novelty of Poisson summation, stationary phase, or logarithmic Legendre duality.

This result is not a restatement of WI-192. WI-192 closes the attempt to iterate the **one-dimensional fixed-shift** B-process through the Atkinson phase. WI-194 instead tests the escape explicitly left open by WI-193—keeping the shift and prime variables jointly coupled—and shows that the most direct **phase-only two-dimensional transform** is still self-dual and strip-preserving. Arithmetic joint cancellation remains open.

## Research consequence

WI-193 correctly redirects the small-bow problem away from fixed-shift modulus bounds, but “go two-dimensional” is not yet enough. The next useful theorem must keep the shift family coupled **and use arithmetic structure while doing so**. A proposal that consists only of applying joint Poisson/stationary phase to `A log(n/m)` and then estimating the resulting dual family has not escaped the source geometry: it has recreated it at comparable scale.

The falsification rule is therefore sharper. Any proposed joint bow escape should identify, before substantial work, the extra arithmetic or spectral resource that breaks the self-duality (9) and the strip conservation (14). If no such resource is present, the route is a reparametrization rather than a source of the cross-shift gain required by WI-193.
