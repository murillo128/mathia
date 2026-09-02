# WP-102 — Exact critical prime-torus completions have infinite cylindrical Fisher energy, regardless of correlations

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATION-ROBUST + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-096`--`WP-101` leave a narrow escape. Exact cover covariance turns a finite positive scalar completion into a positive measure on the infinite prime torus. `WP-097` pays for the exact one-prime Weil rays with mixed-prime moments, and `WP-101` shows that correlations can even restore equivalence to product Haar at the sharp total mass. Thus neither product singularity nor absolute continuity is a correlation-robust obstruction.

The standard first-order translation geometry of such a state has a stronger obstruction. Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T
\]

and let `mu_sigma` be any finite positive measure of mass `C>0` satisfying the exact one-prime moments

\[
\boxed{
\widehat\mu_\sigma(e_p)
=-\frac{\log p}{p^\sigma}
\quad\text{for every prime }p.
}
\tag{1}
\]

No condition is imposed on mixed-prime Fourier coefficients. For a finite prime set `P`, let `eta_P` be the normalized marginal

\[
eta_P:=\frac1C(\pi_P)_*\mu_\sigma.
\tag{2}
\]

If `eta_P=h_P m_P` and `u_P:=sqrt(h_P)` has weak first derivatives, define

\[
\mathcal I_P(eta_P)
:=4\sum_{p\in P}\|\partial_p u_P\|_2^2;
\tag{3}
\]

otherwise set `I_P=+infinity`. Define the cylindrical Fisher energy

\[
\mathcal I_{\rm cyl}(\mu_\sigma)
:=\sup_{P\Subset\mathcal P}\mathcal I_P(eta_P).
\tag{4}
\]

Then every finite cylinder obeys

\[
\boxed{
\mathcal I_P(eta_P)
\ge\frac1{C^2}\sum_{p\in P}
\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{5}
\]

Consequently

\[
\boxed{
\mathcal I_{\rm cyl}(\mu_\sigma)=+\infty
\qquad(\sigma\le1/2).
}
\tag{6}
\]

In particular, **every** exact critical completion has infinite cylindrical Fisher energy, whether its mixed moments are independent, correlated, Haar-equivalent, Haar-singular, or chosen by another positive extension. Correlations can repair the measure-class obstruction of `WP-100`; they cannot repair finite product-coordinate Fisher geometry.

The threshold is sharp for this architecture. For `sigma>1/2`, the mixed-prime product completion underlying `WP-097`/`WP-100` has finite cylindrical spatial Fisher energy.

This is a no-go, not a proof of Weil positivity. It closes only

```text
exact cover covariance
    -> positive prime-torus completion
    -> arbitrary mixed-prime correlations
    -> finite spatial Fisher / square-root Dirichlet geometry
    -> use that independent positivity as the Weil sign source
```

at the critical exponent.

## 1. One coordinate moment already costs Fisher energy

Fix finite `P`. If `I_P=+infinity`, (5) is automatic. Otherwise `eta_P=h_Pm_P`, `int h_P dm_P=1`, and `u_P=sqrt(h_P)` lies in the square-root Sobolev domain.

For `p in P`, write `z_p(theta)=exp(i theta_p)`. From (1)--(2),

\[
a_p
:=\int_{\mathbb T^P}\overline{z_p}\,h_P\,dm_P
=-\frac{\log p}{C p^\sigma}.
\tag{7}
\]

Since `h_P=u_P^2`, weak differentiation gives

\[
\partial_p h_P=2u_P\,\partial_pu_P\in L^1.
\tag{8}
\]

Periodic integration by parts against the smooth character yields

\[
\int (\partial_p h_P)\overline{z_p}\,dm_P
=i\int h_P\overline{z_p}\,dm_P
=i a_p.
\tag{9}
\]

Therefore Cauchy--Schwarz gives

\[
|a_p|
=2\left|\int u_P\,\partial_pu_P\,\overline{z_p}\,dm_P\right|
\le2\|u_P\|_2\|\partial_pu_P\|_2
=2\|\partial_pu_P\|_2,
\tag{10}
\]

because `||u_P||_2=1`. Hence

\[
\boxed{|a_p|^2\le4\|\partial_pu_P\|_2^2.}
\tag{11}
\]

Summing (11) over `p in P` and substituting (7) proves (5).

For a positive smooth density, (3) is ordinary Fisher information for independent torus translations:

\[
4\|\partial_p\sqrt h\|_2^2
=\int |\partial_p\log h|^2h\,dm.
\tag{12}
\]

The square-root formulation also handles zeros of the density by Sobolev closure. Equation (11) is just the compact-circle score/Cramér--Rao mechanism.

## 2. The critical rays force divergence

At `sigma=1/2`, (5) becomes

\[
\mathcal I_P(eta_P)
\ge\frac1{C^2}\sum_{p\in P}\frac{(\log p)^2}{p}.
\tag{13}
\]

Euler's divergence of `sum_p 1/p` implies

\[
\sum_p\frac{(\log p)^2}{p}=+\infty,
\tag{14}
\]

since `(log p)^2` is bounded below away from zero for all sufficiently large primes. Exhausting the primes in (13) proves the critical case of (6).

More generally,

\[
\sum_p(\log p)^2p^{-2\sigma}
\begin{cases}
<\infty,&\sigma>1/2,\\
=\infty,&\sigma\le1/2.
\end{cases}
\tag{15}
\]

The convergent half follows by comparison with `sum_{n>=2}(log n)^2 n^{-2 sigma}`; smaller `sigma` only increases the critical tail.

Only the first coordinate moments enter. Mixed-prime coefficients never appear, so correlations cannot cancel this lower bound.

## 3. Global singularity is not an escape

A globally singular measure on an infinite product may have smooth finite-dimensional marginals; `WP-100` already warns against identifying global singularity with bad finite cylinders. Definition (4) therefore tests the marginals directly.

For each finite `P`, either the marginal has no square-root `H^1` density, in which case its extended Fisher energy is already infinite, or inequality (5) applies. In the second case the lower bounds accumulate to (14). Thus a globally singular completion with regular finite marginals still has infinite cylindrical Fisher energy.

This differs materially from `WP-101`. That finding proves that every **globally absolutely continuous** critical completion lies outside `L(log L)^{1/2}`. `WP-102` says that **all** positive completions, including globally singular ones, fail the finite cylindrical Fisher test. No global density is assumed.

## 4. The boundary is sharp above one half

The product completion of `WP-097`/`WP-100` provides a matched supercritical control. Put

\[
r_p=p^{-\sigma},
\qquad
P_{r_p}(\theta)=\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2},
\tag{16}
\]

and

\[
\rho_{p,C,\sigma}(\theta)
=1+\frac{\log p}{C}\bigl(1-P_{r_p}(\theta)\bigr).
\tag{17}
\]

For `C=C_*` from `WP-097`, the factors are nonnegative at `sigma=1/2`; for `sigma>1/2` they are strictly positive because reducing `r_p` weakens the local positivity constraint. Their product has the exact one-prime moments and the mixed moments required for positivity.

The local spatial Fisher contribution is

\[
J_{p,\sigma}
=\int_{\mathbb T}\frac{|\rho'_{p,C,\sigma}|^2}{\rho_{p,C,\sigma}}\,dm.
\tag{18}
\]

For all sufficiently large `p`, the factors are uniformly bounded below and

\[
\rho'_{p,C,\sigma}
=-\frac{\log p}{C}P'_{r_p}.
\tag{19}
\]

The Poisson Fourier series gives

\[
\|P_r'\|_2^2
=2\sum_{k\ge1}k^2r^{2k}
=\frac{2r^2(1+r^2)}{(1-r^2)^3}.
\tag{20}
\]

Hence

\[
J_{p,\sigma}=O_C\!\left((\log p)^2p^{-2\sigma}\right).
\tag{21}
\]

By (15), `sum_p J_{p,sigma}` is finite for `sigma>1/2`; the finitely many small-prime factors contribute finitely. So the supercritical product completion has finite cylindrical Fisher energy.

At `sigma=1/2`, an individual saturated factor may still have finite Fisher energy; the divergence is the accumulated all-prime tail. Thus the transition is genuinely global in the prime coordinates.

## 5. Uniformly coercive first-order metrics inherit the obstruction

For coordinate weights `lambda_p>0`, define

\[
\mathcal E_{P,\lambda}(h)
=4\sum_{p\in P}\lambda_p\|\partial_p\sqrt h\|_2^2.
\tag{22}
\]

The same proof yields

\[
\boxed{
\mathcal E_{P,\lambda}(h_P)
\ge\frac1{C^2}\sum_{p\in P}\lambda_p
\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{23}
\]

At the critical exponent, any choice with `inf_p lambda_p>0` still diverges. More generally, finite critical energy requires at least

\[
\sum_p\lambda_p\frac{(\log p)^2}{p}<\infty.
\tag{24}
\]

Likewise, a first-order score metric whose finite-cylinder metric matrices are uniformly bounded below by a fixed positive multiple of the product metric dominates the unweighted Fisher trace and is blocked by (14).

Therefore a first-order escape must become asymptotically cheap/degenerate in prime directions or cease to be uniformly coercive in the product-coordinate geometry. Such degeneration could be legitimate if another Mathia construction forces it; choosing weights solely to make (24) converge would be an inserted regularization.

This does **not** rule out the one-dimensional Kronecker flow `theta_p=t log p`, a nonlocal/sub-Riemannian geometry, an infinite-codimension quotient, or a finite--archimedean coupling that changes the state before scalar completion.

## 6. Distinction from WP-022 and WP-084

`WP-022` studies the **parameter score** `partial_sigma log nu_sigma` of one specific product-Poisson family. `WP-084` studies the **shift-parameter score** of the positive fixed-shift cover family `P_{n,c}`.

Here no path of measures is chosen and no derivative is taken with respect to `sigma`, `c`, or another external parameter. Equations (3)--(12) use **spatial translation derivatives on the prime torus at fixed sigma**. The result therefore applies to arbitrary positive completions, including the correlated Haar-equivalent critical state of `WP-101`.

## 7. Prior-art audit

No theorem-level novelty is claimed for (11). Fisher-information bounds on Fourier/characteristic-function data are classical score/Cramér--Rao technology. A close explicit anchor is Zhengmin Zhang, *Inequalities for characteristic functions involving Fisher information*, **Comptes Rendus Mathématique** 344 (2007), no. 5, 327--330, DOI `10.1016/j.crma.2007.01.008`. Zhang derives characteristic-function bounds from Fisher information on the real line using Cramér--Rao with trigonometric observables. The compact-circle estimate (11) is simpler and follows directly from periodic integration by parts.

The retained Mathia content is the simultaneous arithmetic specialization

\[
\widehat\mu(e_p)=-\frac{\log p}{C\sqrt p}
\quad\text{for every prime }p,
\tag{25}
\]

followed by the growing-cylinder trace. That converts a classical local inequality into the correlation-independent critical divergence. No zero data, RH assumption, or RH-equivalent positivity functional enters, but the conclusion remains a no-go rather than a global sign theorem.

## 8. Matched free-generator control

For a free commutative monoid with generator energies `E_j>0`, character torus `prod_j T`, and moments

\[
\widehat\mu_\sigma(e_j)=-E_je^{-\sigma E_j},
\tag{26}
\]

the same argument gives

\[
\mathcal I_{\rm cyl}(\mu_\sigma)
\ge\frac1{C^2}\sum_jE_j^2e^{-2\sigma E_j}.
\tag{27}
\]

Thus the boundary is controlled by square-summability of the generator amplitudes in any free-generator system. Rational primes are the specialization `E_j=log p_j`, where the threshold is `sigma=1/2`.

This matched control prevents overinterpretation: the divergence is structural to the exact one-generator amplitudes plus product-coordinate first-order geometry; by itself it contains no Riemann-specific global information.

## Consequence for the research line

`WP-101` showed that correlations can restore Haar equivalence at the exact critical rays. `WP-102` narrows that escape:

\[
\boxed{
\text{correlations can restore measure class}
\quad\text{but cannot restore finite cylindrical Fisher energy.}
\]

A future positive completion therefore cannot obtain the Weil sign merely by placing the standard finite translation Fisher/Dirichlet geometry on the correlated prime-torus state. At the exact critical moments that geometry already has infinite total energy before any Gamma or polar sector is addressed.

The remaining live target must introduce a genuinely global coupling, quotient, degenerate/nonlocal metric, or finite--archimedean geometry whose sign theorem is meaningful **before** the exact Weil consequence is read out. It must explain why that altered geometry is canonical rather than a regularization tailored to (14), survive the generalized-generator control, and generate the archimedean/polar terms intrinsically.