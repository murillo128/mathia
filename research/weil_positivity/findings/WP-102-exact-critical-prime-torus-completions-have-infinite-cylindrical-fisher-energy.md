# WP-102 — Exact critical prime-torus completions have infinite cylindrical Fisher energy, regardless of correlations

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATION-ROBUST + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-096`--`WP-101` leave a narrow but important question open. Exact cover covariance turns every finite positive scalar completion into a positive measure on the infinite prime torus. At the critical attenuation, `WP-097` gives such a completion by paying with mixed-prime moments, and `WP-101` shows that arbitrary correlations can even restore equivalence to product Haar at the sharp total mass. Thus neither product singularity nor absolute continuity is itself a correlation-robust obstruction.

There is, however, a stronger obstruction for the most canonical first-order positive geometry of a torus density: **spatial Fisher/Dirichlet energy**. It is independent of the mixed-prime correlations.

Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T,
\qquad
m=\bigotimes_p m_p,
\]

and let `mu_sigma` be any finite positive measure of mass `C>0` whose one-prime moments are the exact cover/Weil rays

\[
\boxed{
\widehat\mu_\sigma(e_p)
=-\frac{\log p}{p^\sigma}
\qquad\text{for every prime }p.
}
\tag{1}
\]

No assumption is made on any mixed-prime Fourier coefficient. For a finite prime set `P`, normalize the marginal

\[
\nu_P:=\frac1C(\pi_P)_*\mu_\sigma
\tag{2}
\]

and define its extended spatial Fisher energy by

\[
\mathcal I_P(\nu_P)
:=
4\sum_{p\in P}
\left\|\partial_p\sqrt{h_P}\right\|_{L^2(m_P)}^2
\tag{3}
\]

when `nu_P=h_P m_P` and `sqrt(h_P)` has the indicated weak derivatives, and set `I_P=+infinity` otherwise. Define the cylindrical energy

\[
\mathcal I_{\rm cyl}(\mu_\sigma)
:=\sup_{P\Subset\mathcal P}\mathcal I_P(\nu_P).
\tag{4}
\]

Then every finite cylinder obeys the exact lower bound

\[
\boxed{
\mathcal I_P(\nu_P)
\ge
\frac1{C^2}
\sum_{p\in P}
\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{5}
\]

Consequently

\[
\boxed{
\mathcal I_{\rm cyl}(\mu_\sigma)=+\infty
\qquad\text{for every }\sigma\le\frac12.
}
\tag{6}
\]

In particular, at the Weil exponent

\[
\boxed{
\mathcal I_{\rm cyl}(\mu_{1/2})=+\infty
}
\tag{7}
\]

for **every** positive prime-torus completion carrying the exact one-prime rays, whether its mixed moments are independent, correlated, Haar-equivalent, Haar-singular, or chosen by some other positive extension. Correlations can repair the measure-class obstruction of `WP-100`, as `WP-101` demonstrates, but they cannot repair finite product-coordinate Fisher geometry.

The threshold is sharp for this architecture. For `sigma>1/2`, the mixed-prime product completion used in `WP-097`/`WP-100` has finite cylindrical spatial Fisher energy. Thus (6) is not a generic pathology of infinite products: it occurs exactly at the same square-summability boundary forced by the critical Weil first moments.

This does **not** prove Weil positivity. It is a negative result about a natural positive geometry on the exact-cover completion space. It closes the route

```text
exact cover covariance
    -> positive prime-torus completion
    -> allow arbitrary mixed-prime correlations
    -> canonical finite spatial Fisher / square-root Dirichlet geometry
    -> use its independent positivity as the Weil sign source
```

at the critical exponent. Any rescue within a first-order torus geometry must make the prime-coordinate metric asymptotically degenerate, use a genuinely nonlocal/non-product direction, quotient away infinitely much coordinate energy, or couple the finite and archimedean sectors before the scalar prime-torus state is formed. None of those structures is supplied by the present completion itself.

## 1. One coordinate moment already costs Fisher energy

Fix a finite prime set `P`. If `I_P=+infinity`, (5) is automatic, so assume

\[
\nu_P=h_Pm_P,
\qquad
u_P(\mathbb T^P)=1,
\qquad
u:=\sqrt{h_P}\in H^1(\mathbb T^P).
\tag{8}
\]

For `p in P`, write

\[
z_p(\theta)=e^{i\theta_p}.
\]

The normalized first moment inherited from (1) is

\[
a_p
:=
\int_{\mathbb T^P}\overline{z_p}\,h_P\,dm_P
=-\frac{\log p}{C p^\sigma}.
\tag{9}
\]

Because `h_P=u^2` with `u in H^1`, its weak derivative is

\[
\partial_p h_P=2u\,\partial_pu\in L^1.
\tag{10}
\]

Periodic integration by parts against the smooth character gives

\[
\int (\partial_p h_P)\overline{z_p}\,dm_P
=i\int h_P\overline{z_p}\,dm_P
=i a_p.
\tag{11}
\]

Therefore

\[
|a_p|
=
2\left|\int u\,\partial_pu\,\overline{z_p}\,dm_P\right|
\le
2\|u\|_2\|\partial_pu\|_2
=
2\|\partial_pu\|_2,
\tag{12}
\]

since `||u||_2^2=int h_P dm_P=1`. Squaring,

\[
\boxed{
|a_p|^2
\le
4\|\partial_p\sqrt{h_P}\|_2^2.
}
\tag{13}
\]

Summing (13) over `p in P` proves

\[
\sum_{p\in P}|a_p|^2
\le
\mathcal I_P(\nu_P),
\tag{14}
\]

and substituting (9) gives (5).

For a strictly positive smooth density, (3) is the ordinary Fisher information for the independent translation parameters of the torus:

\[
4\|\partial_p\sqrt h\|_2^2
=
\int |\partial_p\log h|^2 h\,dm.
\tag{15}
\]

The square-root formulation is preferable here because it remains meaningful at zeros of the density and extends directly by Sobolev closure. Equation (13) is simply the score/Cauchy--Schwarz or Cramér--Rao mechanism written in compact-group coordinates.

## 2. The critical prime rays force infinite cylindrical energy

At `sigma=1/2`, (5) becomes

\[
\mathcal I_P(\nu_P)
\ge
\frac1{C^2}
\sum_{p\in P}\frac{(\log p)^2}{p}.
\tag{16}
\]

Euler's divergence of `sum_p 1/p` already implies

\[
\sum_p\frac{(\log p)^2}{p}=+\infty,
\tag{17}
\]

since `(log p)^2` is bounded below away from zero for all sufficiently large primes. Taking an increasing exhaustion by finite prime sets in (16) therefore proves (7).

More generally,

\[
\sum_p(\log p)^2p^{-2\sigma}
\begin{cases}
<\infty,&\sigma>1/2,\\
=\infty,&\sigma\le1/2.
\end{cases}
\tag{18}
\]

The convergent half follows by comparison with

\[
\sum_{n\ge2}(\log n)^2n^{-2\sigma},
\]

and the boundary divergence follows from (17); smaller `sigma` only enlarges the tail. This proves the exact threshold in (6).

The argument uses only the **first** prime-coordinate moment. It does not inspect, factor, or constrain any coefficient supported on two or more distinct primes. Consequently mixed-prime correlations cannot cancel the lower bound.

## 3. Global singularity is not an escape

A possible response to `WP-101` is to abandon absolute continuity and use a Haar-singular positive completion. Definition (4) deliberately tests that escape at the level relevant to local first-order geometry.

A globally singular measure on an infinite product can still have smooth finite-dimensional marginals; `WP-100` supplies exactly this kind of warning through Kakutani product singularity. The present obstruction does not infer infinite Fisher information merely from global singularity. Instead it examines every finite marginal separately.

For each finite `P`, either:

1. the normalized marginal fails to have a square-root `H^1` density, in which case `I_P=+infinity` by definition; or
2. it has such a density, in which case (5) applies.

As `P` exhausts the primes, the second alternative accumulates the divergent lower bound (17). Therefore even a globally singular completion with perfectly regular finite cylinders has

\[
\mathcal I_{\rm cyl}=+\infty.
\tag{19}
\]

This is stronger in a different direction from `WP-101`. That finding proves that every **absolutely continuous global** critical completion lies below the `L(log L)^{1/2}` endpoint. The present finding says that **all positive completions**, including singular ones, fail the finite cylindrical Fisher test. It does not require a global density at all.

## 4. The boundary is sharp: the supercritical product completion has finite Fisher trace

The lower bound would be less informative if every infinite prime-torus completion had infinite spatial Fisher trace. The explicit mixed-prime product state from `WP-097`/`WP-100` gives a matched supercritical control.

For

\[
r_p=p^{-\sigma},
\qquad
P_{r_p}(\theta)=\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2},
\tag{20}
\]

consider the one-prime factor

\[
\rho_{p,C,\sigma}(\theta)
=
1+\frac{\log p}{C}\bigl(1-P_{r_p}(\theta)\bigr).
\tag{21}
\]

For `C=C_*` from `WP-097`, all these factors are nonnegative at `sigma=1/2`; for every `sigma>1/2` they are strictly positive, because decreasing `r_p` weakens the local positivity constraint. Their product has the required first moments and the mixed coefficients that pay for positivity.

The local spatial Fisher contribution is

\[
J_{p,\sigma}
=
\int_{\mathbb T}
\frac{|\rho'_{p,C,\sigma}|^2}
{\rho_{p,C,\sigma}}\,dm.
\tag{22}
\]

For all sufficiently large `p`, `rho_{p,C,sigma}` is uniformly bounded below, while

\[
\rho'_{p,C,\sigma}
=-\frac{\log p}{C}P'_{r_p}.
\tag{23}
\]

The Poisson Fourier series gives exactly

\[
\|P_r'\|_2^2
=2\sum_{k\ge1}k^2r^{2k}
=
\frac{2r^2(1+r^2)}{(1-r^2)^3}.
\tag{24}
\]

Hence

\[
J_{p,\sigma}
=O_C\!\left((\log p)^2p^{-2\sigma}\right)
\qquad(p\to\infty).
\tag{25}
\]

For `sigma>1/2`, (18) makes `sum_p J_{p,sigma}` finite; the finitely many small-prime factors are smooth and strictly positive and contribute only a finite amount. Thus the product completion has

\[
\mathcal I_{\rm cyl}<\infty
\qquad(\sigma>1/2).
\tag{26}
\]

At `sigma=1/2`, individual local factors can still have finite Fisher energy — even the saturated dyadic factor has only a quadratic zero, so its square root has finite one-dimensional Dirichlet energy. The divergence is genuinely the accumulated all-prime tail, not a single bad coordinate.

Therefore the Fisher transition is exactly the same critical square-summability boundary as the first moments themselves:

```text
sigma > 1/2:
    exact mixed-prime positive completion
    + finite cylindrical spatial Fisher geometry is possible

sigma = 1/2:
    exact positive completion is still possible
    but every such completion has infinite cylindrical Fisher geometry
```

## 5. Uniformly coercive first-order metrics do not repair the divergence

Equation (5) is not tied to one numerical normalization of the product metric. Let a weighted coordinate energy on a finite cylinder be

\[
\mathcal E_{P,\lambda}(h)
=
4\sum_{p\in P}\lambda_p
\|\partial_p\sqrt h\|_2^2,
\qquad \lambda_p>0.
\tag{27}
\]

Then the same proof gives

\[
\boxed{
\mathcal E_{P,\lambda}(h_P)
\ge
\frac1{C^2}
\sum_{p\in P}\lambda_p
\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{28}
\]

At the critical exponent, any weighting with `inf_p lambda_p>0` therefore still diverges. More generally, finite energy requires at least

\[
\sum_p\lambda_p\frac{(\log p)^2}{p}<\infty.
\tag{29}
\]

Likewise, a positive quadratic form in the score vector whose metric matrices are uniformly coercive on every finite prime cylinder dominates a fixed multiple of the unweighted Fisher trace and is ruled out by (17).

Thus a first-order metric can escape only by becoming asymptotically cheap or degenerate in the prime directions, or by ceasing to be a uniformly coercive product-coordinate geometry. Such a degeneration may be mathematically meaningful if another Mathia construction forces it, but inserting weights solely to make (29) converge would be a hand-picked regularization and would not satisfy the research mandate.

This statement does **not** rule out the one-dimensional Kronecker flow `theta_p=t log p`, a nonlocal sub-Riemannian geometry, an infinite-codimension quotient, or a finite--archimedean coupling that changes the relevant state before the scalar prime-torus completion. Those are genuinely different constructions and require their own sign theorem.

## 6. This is spatial Fisher geometry, not the parameter Fisher divergences of WP-022 or WP-084

The word `Fisher` appears earlier in this research line, but the objects are different.

`WP-022` studies the **parameter score**

\[
\partial_\sigma\log\nu_\sigma
\]

of the specific canonical product-Poisson family. Its Fisher norm diverges at `sigma=1/2`. That result depends on the chosen radial family and its `sigma` derivative.

`WP-084` studies the **shift-parameter score** of the positive fixed-shift cover family `P_{n,c}` and finds a singular Fisher boundary at `c=0`.

Here there is no chosen path of measures and no derivative with respect to `sigma`, `c`, or another external parameter. The derivatives in (3) are **spatial translation derivatives on the prime torus itself**. The result quantifies the first-order geometry of an arbitrary positive completion at a fixed `sigma`, and (5) survives arbitrary correlations. In particular, it applies to the correlated Haar-equivalent critical completion constructed in `WP-101`, which is not the product-Poisson family of `WP-022`.

## 7. Prior-art audit: the Fourier/Fisher inequality is classical; the Mathia application is the new boundary

No theorem-level novelty is claimed for (13). Bounding Fourier/characteristic-function data by Fisher information through a score identity and Cauchy--Schwarz is classical Cramér--Rao technology. A close explicit prior-art anchor is:

- Zhengmin Zhang, *Inequalities for characteristic functions involving Fisher information*, **Comptes Rendus Mathématique** 344 (2007), no. 5, 327--330, DOI `10.1016/j.crma.2007.01.008`.

Zhang proves upper bounds on characteristic functions in terms of Fisher information on the real line by applying Cramér--Rao to trigonometric observables. The compact-torus one-character estimate (13) is simpler and follows directly from periodic integration by parts.

The project-specific content is the simultaneous arithmetic specialization forced by `WP-096`--`WP-101`:

\[
\widehat\mu(e_p)
=-\frac{\log p}{C\sqrt p}
\quad\text{for every prime }p,
\tag{30}
\]

combined with the growing-cylinder trace of the translation Fisher metric. That specialization converts the classical local inequality into the correlation-independent divergence (7), and it is this exact boundary — not the Fisher inequality itself — that is retained here.

The finding also stays outside classical Weil positivity in the important sense: no zero data or RH-equivalent positivity functional enters the proof. But it is a **no-go**, not an independent proof of the required global sign.

## 8. Matched free-generator control

The obstruction is not specific to rational primes. Let a free commutative monoid have generator energies `E_j>0`, let its character torus be `prod_j T`, and require first moments

\[
\widehat\mu_\sigma(e_j)
=-E_j e^{-\sigma E_j}.
\tag{31}
\]

For a mass-`C` positive completion, the same argument gives

\[
\mathcal I_{\rm cyl}(\mu_\sigma)
\ge
\frac1{C^2}
\sum_j E_j^2e^{-2\sigma E_j}.
\tag{32}
\]

Thus the Fisher boundary is controlled by the square-summability of the generator amplitudes in any free-generator system. The rational primes are the specialization `E_j=log p_j`, where that square-summability threshold is exactly `sigma=1/2`.

This matched control is decisive for interpretation. Infinite critical Fisher energy is a structural consequence of the exact one-generator amplitudes and the product-coordinate first-order geometry; by itself it contains no Riemann-specific global information.

## Consequence for the research line

`WP-101` showed that allowing correlations is much more powerful than the independent-product model suggested: it can restore Haar equivalence at the exact critical rays. `WP-102` narrows that escape substantially:

\[
\boxed{
\text{correlations can restore measure class}
\quad\text{but cannot restore finite cylindrical Fisher energy.}
}
\]

Therefore a future positive completion cannot obtain the Weil sign merely by declaring the correlated prime-torus state to carry the standard finite translation Fisher/Dirichlet geometry. At the exact critical arithmetic moments that geometry has infinite total energy before any Gamma or polar sector is addressed.

The remaining live target is correspondingly more specific: a successful Mathia-native structure must introduce a nontrivial global coupling, quotient, degenerate/nonlocal metric, or finite--archimedean geometry whose sign theorem is meaningful **before** the exact Weil consequence is read out. It must also explain why that altered geometry is canonical rather than a regularization designed around the divergent series (17), survive the generalized-generator control, and generate the archimedean/polar terms intrinsically.