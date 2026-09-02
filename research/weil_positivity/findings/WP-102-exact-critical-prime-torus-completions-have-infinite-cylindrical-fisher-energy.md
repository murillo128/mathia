# WP-102 — Exact critical prime-torus completions have infinite cylindrical Fisher energy, regardless of correlations

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATION-ROBUST + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-096`--`WP-101` leave a narrow but important escape. Exact cover covariance turns every finite positive scalar completion into a positive measure on the infinite prime torus. `WP-097` pays for the exact one-prime Weil rays with mixed-prime moments, and `WP-101` shows that arbitrary correlations can even restore equivalence to product Haar at the sharp total mass. Thus neither product singularity nor absolute continuity is a correlation-robust obstruction.

The standard first-order positive geometry of such a state has a stronger obstruction. Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T,
\qquad
m=\bigotimes_p m_p,
\]

and let `mu_sigma` be any finite positive measure of mass `C>0` with the exact one-prime moments

\[
\boxed{
\widehat\mu_\sigma(e_p)
=-\frac{\log p}{p^\sigma}
\qquad\text{for every prime }p.
}
\tag{1}
\]

No condition is imposed on mixed-prime Fourier coefficients. For a finite prime set `P`, let

\[
\nu_P:=\frac1C(\pi_P)_*\mu_\sigma
\tag{2}
\]

be the normalized marginal. Define its extended spatial Fisher energy by

\[
\mathcal I_P(\nu_P)
:=4\sum_{p\in P}
\left\|\partial_p\sqrt{h_P}\right\|_{L^2(m_P)}^2
\tag{3}
\]

when `nu_P=h_P m_P` and `sqrt(h_P)` has the indicated weak derivatives; otherwise set `I_P=+infinity`. Define

\[
\mathcal I_{\rm cyl}(\mu_\sigma)
:=\sup_{P\Subset\mathcal P}\mathcal I_P(\nu_P).
\tag{4}
\]

Then every finite cylinder satisfies

\[
\boxed{
\mathcal I_P(\nu_P)
\ge
\frac1{C^2}\sum_{p\in P}
\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{5}
\]

Hence

\[
\boxed{
\mathcal I_{\rm cyl}(\mu_\sigma)=+\infty
\qquad(\sigma\le1/2).
}
\tag{6}
\]

In particular, every exact critical completion has

\[
\boxed{
\mathcal I_{\rm cyl}(\mu_{1/2})=+\infty,
}
\tag{7}
\]

whether its mixed moments are independent, correlated, Haar-equivalent, Haar-singular, or chosen by some other positive extension. Correlations can repair the measure-class obstruction of `WP-100`, as `WP-101` demonstrates, but they cannot repair finite product-coordinate Fisher geometry.

The threshold is sharp for this architecture: for `sigma>1/2`, the mixed-prime product completion underlying `WP-097`/`WP-100` has finite cylindrical spatial Fisher energy.

This does **not** prove Weil positivity. It closes only the route

```text
exact cover covariance
    -> positive prime-torus completion
    -> arbitrary mixed-prime correlations allowed
    -> finite spatial Fisher / square-root Dirichlet geometry
    -> use its independent positivity as the Weil sign source
```

at the critical exponent. A rescue must alter the geometry itself: for example through asymptotically degenerate coordinate weights, a genuinely nonlocal direction, an infinite-dimensional quotient, or finite--archimedean coupling before the scalar prime-torus state is formed.

## 1. One coordinate moment already costs Fisher energy

Fix a finite prime set `P`. If `I_P=+infinity`, (5) is automatic. Otherwise write

\[
\nu_P=h_Pm_P,
\qquad
u_P(\mathbb T^P)=1,
\qquad
u:=\sqrt{h_P}\in H^1(\mathbb T^P).
\tag{8}
\]

To avoid confusing the measure `nu_P` with the square-root amplitude, rename the latter immediately as

\[
u:=\sqrt{h_P}.
\tag{9}
\]

For `p in P`, put `z_p(theta)=e^{i theta_p}`. The normalized first moment inherited from (1) is

\[
a_p
:=\int_{\mathbb T^P}\overline{z_p}\,h_P\,dm_P
=-\frac{\log p}{C p^\sigma}.
\tag{10}
\]

Since `h_P=u^2` with `u in H^1`, its weak derivative satisfies

\[
\partial_p h_P=2u\,\partial_pu\in L^1.
\tag{11}
\]

Periodic integration by parts against the smooth character gives

\[
\int (\partial_p h_P)\overline{z_p}\,dm_P
=i\int h_P\overline{z_p}\,dm_P
=i a_p.
\tag{12}
\]

Therefore

\[
|a_p|
=2\left|\int u\,\partial_pu\,\overline{z_p}\,dm_P\right|
\le2\|u\|_2\|\partial_pu\|_2
=2\|\partial_pu\|_2,
\tag{13}
\]

because `||u||_2^2=int h_P dm_P=1`. Thus

\[
\boxed{
|a_p|^2\le4\|\partial_p\sqrt{h_P}\|_2^2.
}
\tag{14}
\]

Summing (14) over `p in P` and inserting (10) proves (5).

For a strictly positive smooth density, the right-hand side of (3) is the ordinary Fisher information of the independent translation parameters:

\[
4\|\partial_p\sqrt h\|_2^2
=\int |\partial_p\log h|^2h\,dm.
\tag{15}
\]

The square-root formulation is useful because it still makes sense at zeros of the density and extends by Sobolev closure. Equation (14) is the compact-circle score/Cauchy--Schwarz mechanism in its simplest form.

## 2. Critical Weil rays force infinite cylindrical energy

At `sigma=1/2`, (5) is

\[
\mathcal I_P(\nu_P)
\ge\frac1{C^2}\sum_{p\in P}\frac{(\log p)^2}{p}.
\tag{16}
\]

Euler's divergence of `sum_p 1/p` implies

\[
\sum_p\frac{(\log p)^2}{p}=+\infty,
\tag{17}
\]

because `(log p)^2` is bounded below away from zero for all sufficiently large primes. Exhausting the primes in (16) proves (7).

More generally,

\[
\sum_p(\log p)^2p^{-2\sigma}
\begin{cases}
<\infty,&\sigma>1/2,\\
=\infty,&\sigma\le1/2.
\end{cases}
\tag{18}
\]

The convergent half follows by comparison with `sum_{n>=2}(log n)^2 n^{-2 sigma}`; the boundary is (17), and smaller `sigma` only enlarges the tail. This proves (6).

Only the **first** coordinate moment is used. No mixed-prime coefficient enters the estimate, so correlations cannot cancel the lower bound.

## 3. Global singularity is not an escape

A globally singular measure on an infinite product can still have smooth finite-dimensional marginals; `WP-100` is a direct warning not to identify global singularity with bad finite cylinders. Definition (4) therefore tests finite marginals rather than assuming a global density.

For each finite `P`, either the marginal has no square-root `H^1` density, giving `I_P=+infinity` immediately, or (5) applies. In the second case the lower bounds accumulate as `P` grows. Hence even a globally singular completion with regular finite marginals satisfies (7).

This is stronger in a different direction from `WP-101`. `WP-101` proves that every **globally absolutely continuous** critical completion lies outside `L(log L)^{1/2}`. `WP-102` says that **all** positive completions, including globally singular ones, fail the finite cylindrical Fisher test. No global density is assumed.

## 4. The boundary is sharp above one half

The explicit mixed-prime product state from `WP-097`/`WP-100` supplies a matched supercritical control. Let

\[
r_p=p^{-\sigma},
\qquad
P_{r_p}(\theta)=\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2},
\tag{19}
\]

and

\[
\rho_{p,C,\sigma}(\theta)
=1+\frac{\log p}{C}\bigl(1-P_{r_p}(\theta)\bigr).
\tag{20}
\]

For `C=C_*` from `WP-097`, these factors are nonnegative at `sigma=1/2`; for every `sigma>1/2` they are strictly positive because decreasing `r_p` weakens the local positivity constraint. The corresponding product has the exact first moments and the mixed moments that pay for positivity.

Its one-coordinate Fisher contribution is

\[
J_{p,\sigma}
=\int_{\mathbb T}
\frac{|\rho'_{p,C,\sigma}|^2}{\rho_{p,C,\sigma}}\,dm.
\tag{21}
\]

For all sufficiently large `p`, the factors are uniformly bounded below and

\[
\rho'_{p,C,\sigma}
=-\frac{\log p}{C}P'_{r_p}.
\tag{22}
\]

The Poisson Fourier series gives

\[
\|P_r'\|_2^2
=2\sum_{k\ge1}k^2r^{2k}
=\frac{2r^2(1+r^2)}{(1-r^2)^3}.
\tag{23}
\]

Therefore

\[
J_{p,\sigma}
=O_C\!\left((\log p)^2p^{-2\sigma}\right).
\tag{24}
\]

Equation (18) makes `sum_p J_{p,sigma}` finite for `sigma>1/2`; the finitely many small-prime factors contribute finitely. Thus

\[
\mathcal I_{\rm cyl}<\infty
\qquad(\sigma>1/2)
\tag{25}
\]

for this explicit completion.

At `sigma=1/2`, an individual saturated factor can still have finite Fisher energy: the dyadic factor has only a quadratic zero, so its square root has finite one-dimensional Dirichlet energy. The obstruction is the accumulated all-prime tail, not one bad coordinate.

## 5. Uniformly coercive first-order metrics inherit the obstruction

For weights `lambda_p>0`, define

\[
\mathcal E_{P,\lambda}(h)
=4\sum_{p\in P}\lambda_p
\|\partial_p\sqrt h\|_2^2.
\tag{26}
\]

The same argument gives

\[
\boxed{
\mathcal E_{P,\lambda}(h_P)
\ge\frac1{C^2}\sum_{p\in P}\lambda_p
\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{27}
\]

At the critical exponent any weighting with `inf_p lambda_p>0` still diverges. More generally, finite critical energy requires at least

\[
\sum_p\lambda_p\frac{(\log p)^2}{p}<\infty.
\tag{28}
\]

Likewise, any positive first-order metric on the score vector whose finite-cylinder metric matrices are uniformly bounded below by a fixed positive multiple of the product metric dominates the unweighted Fisher trace and is blocked by (17).

So a first-order escape must become asymptotically cheap/degenerate in prime directions or cease to be uniformly coercive in the product-coordinate geometry. Such degeneration could be meaningful if another Mathia construction forces it; choosing weights solely to make (28) converge would be an inserted regularization.

This result does **not** rule out the one-dimensional Kronecker flow `theta_p=t log p`, a nonlocal/sub-Riemannian geometry, an infinite-codimension quotient, or a finite--archimedean coupling that changes the relevant state before scalar completion.

## 6. Distinction from WP-022 and WP-084

The word `Fisher` occurs earlier in this line, but the geometries differ.

`WP-022` studies the **parameter score** `partial_sigma log nu_sigma` of the specific canonical product-Poisson family. Its Fisher norm diverges at `sigma=1/2`; that claim depends on the chosen radial family and its `sigma` derivative.

`WP-084` studies the **shift-parameter score** of the positive fixed-shift cover family `P_{n,c}` and finds a singular Fisher boundary at `c=0`.

Here there is no path of measures and no derivative with respect to `sigma`, `c`, or another external parameter. Equations (3)--(15) use **spatial translation derivatives on the prime torus itself**. The result applies to an arbitrary positive completion at fixed `sigma`, including the correlated Haar-equivalent critical state constructed in `WP-101`.

## 7. Prior-art audit

No theorem-level novelty is claimed for (14). Fisher-information bounds on Fourier/characteristic-function data are classical score/Cramér--Rao technology. A close explicit anchor is:

- Zhengmin Zhang, *Inequalities for characteristic functions involving Fisher information*, **Comptes Rendus Mathématique** 344 (2007), no. 5, 327--330, DOI `10.1016/j.crma.2007.01.008`.

Zhang derives characteristic-function bounds from Fisher information on the real line using Cramér--Rao with trigonometric observables. The compact-circle estimate (14) is simpler and follows directly from periodic integration by parts.

The retained Mathia content is the simultaneous specialization forced by the exact cover moments,

\[
\widehat\mu(e_p)=-\frac{\log p}{C\sqrt p}
\quad\text{for every prime }p,
\tag{29}
\]

followed by the growing-cylinder trace. That turns a classical local inequality into the correlation-independent critical divergence (7). No zero data, RH assumption, or RH-equivalent positivity functional enters the derivation, but the conclusion is a no-go rather than an independent global sign theorem.

## 8. Matched free-generator control

Let a free commutative monoid have generator energies `E_j>0`, character torus `prod_j T`, and target moments

\[
\widehat\mu_\sigma(e_j)=-E_je^{-\sigma E_j}.
\tag{30}
\]

For a mass-`C` positive completion, the same cylinder argument gives

\[
\mathcal I_{\rm cyl}(\mu_\sigma)
\ge\frac1{C^2}\sum_jE_j^2e^{-2\sigma E_j}.
\tag{31}
\]

Thus the boundary is controlled by square-summability of the generator amplitudes in any free-generator system. Rational primes are the specialization `E_j=log p_j`, for which the threshold is exactly `sigma=1/2`.

This control prevents overinterpretation: the Fisher divergence is structural to the exact one-generator amplitudes plus product-coordinate first-order geometry; by itself it contains no Riemann-specific global information.

## Consequence for the research line

`WP-101` showed that correlations can restore Haar equivalence at the exact critical rays. `WP-102` narrows that escape:

\[
\boxed{
\text{correlations can restore measure class}
\quad\text{but cannot restore finite cylindrical Fisher energy.}
}
\]

A future positive completion therefore cannot obtain the Weil sign merely by placing the standard finite translation Fisher/Dirichlet geometry on the correlated prime-torus state. At the exact critical arithmetic moments that geometry has infinite total energy before any Gamma or polar sector is addressed.

The remaining live target is more specific: a successful Mathia-native structure must introduce a genuinely global coupling, quotient, degenerate/nonlocal metric, or finite--archimedean geometry whose sign theorem is meaningful **before** the exact Weil consequence is read out. It must explain why that altered geometry is canonical rather than a regularization tailored to (17), survive the generalized-generator control, and generate the archimedean/polar terms intrinsically.