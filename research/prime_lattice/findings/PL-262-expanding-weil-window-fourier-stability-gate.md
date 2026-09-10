# PL-262 — Expanding Weil windows impose a sharp L2-to-entire stability gate on the spectral-determinant bridge

## Claim

The remaining convergence step in the Connes–Consani–Moscovici (CCM) zeta-spectral-triple program cannot be justified from ordinary `L2` closeness of the actual Weil ground state to the prolate model when the support interval expands with `lambda`. The Fourier–Mellin evaluation functional itself amplifies endpoint error at the exact Paley–Wiener scale.

Let

\[
\mathcal H_\lambda=L^2([\lambda^{-1},\lambda],d^*u),
\qquad A_\lambda=\log\lambda,
\]

and use the CCM Fourier–Mellin convention

\[
\widehat f(z)=\int_{\lambda^{-1}}^\lambda f(u)u^{-iz}\,d^*u.
\]

Writing `t=log u`, so that `t in [-A_lambda,A_lambda]`, gives

\[
\widehat f(z)=\int_{-A_\lambda}^{A_\lambda}F(t)e^{-izt}\,dt,
\qquad F(t)=f(e^t).
\]

For a residual `r_lambda` and `z=x+iy`, Cauchy–Schwarz is not merely a rough estimate: it gives the exact norm of the point-evaluation functional on this finite-support `L2` space,

\[
|\widehat r_\lambda(x+iy)|
\le \|r_\lambda\|_2\,E_y(\lambda),
\]

where

\[
E_y(\lambda)^2=
\begin{cases}
\displaystyle \frac{\sinh(2|y|\log\lambda)}{|y|},&y\ne0,\\[6pt]
2\log\lambda,&y=0.
\end{cases}
\]

Hence for every fixed `0<a<1/2`,

\[
\sup_{|\Im z|\le a}|\widehat r_\lambda(z)|
\le
\left(\frac{\sinh(2a\log\lambda)}{a}\right)^{1/2}
\|r_\lambda\|_2
\sim \frac{\lambda^a}{\sqrt{2a}}\|r_\lambda\|_2.
\]

Therefore a sufficient bare-`L2` condition for locally uniform transform convergence on the full open critical strip `|Im z|<1/2` is

\[
\boxed{
\forall\varepsilon>0:\qquad
\|r_\lambda\|_2=o(\lambda^{-1/2+\varepsilon}).
}
\]

On the real axis alone the corresponding `L2`-only gate is

\[
\|r_\lambda\|_2\sqrt{\log\lambda}\longrightarrow0.
\]

More intrinsically, one can replace the global rate by endpoint-sensitive control such as

\[
\int_{-A_\lambda}^{A_\lambda}|r_\lambda(t)|e^{a|t|}\,dt\longrightarrow0
\qquad(0<a<1/2),
\]

which is sufficient for the same closed-substrip convergence and can be substantially weaker for structured residuals concentrated away from the moving endpoints.

Applied to the CCM program, let `xi_lambda` denote an actual even ground eigenvector of the continuum restricted Weil form (assuming the still-open simple-even statement) and `k_lambda` the prolate-wave model of CCM, and choose the nonzero scalar `c_lambda` in the same normalization used to compare them. Put

\[
r_\lambda=c_\lambda\xi_\lambda-k_\lambda.
\]

CCM already prove that `hat k_lambda` tends locally uniformly to Riemann's `Xi` on every closed substrip of `|Im z|<1/2`, while explicitly leaving as a missing step the requirement that `k_lambda` approximate a scalar multiple of `xi_lambda` “sufficiently accurately.” The estimate above makes one rigorous sufficient meaning of that phrase:

\[
\forall\varepsilon>0:\quad
\|c_\lambda\xi_\lambda-k_\lambda\|_2
=o(\lambda^{-1/2+\varepsilon})
\]

implies

\[
c_\lambda\widehat\xi_\lambda\longrightarrow\Xi
\]

locally uniformly throughout the open critical strip. If the simple-even hypothesis simultaneously gives that every `hat xi_lambda` has only real zeros, Hurwitz's theorem then excludes nonreal zeros of `Xi` in that strip and yields RH.

The scale is sharp as a statement based **only** on unweighted `L2` error. Ordinary `L2` convergence on expanding intervals does not even guarantee pointwise convergence of the transforms on the real axis, and exponentially small `L2` residuals can retain order-one transform values at nonreal points. Thus the route

\[
\|c_\lambda\xi_\lambda-k_\lambda\|_2\to0
\quad\Longrightarrow\quad
\widehat\xi_\lambda\to\Xi
\]

is invalid without a rate or additional endpoint/regularity structure.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + STRUCTURAL-REDUCTION + NEGATIVE/OBSTRUCTION` for using qualitative unweighted `L2` convergence of the prolate model as the missing CCM convergence theorem. The Paley–Wiener evaluation estimate is classical Hilbert-space/Fourier analysis and is not claimed as new. The line-specific contribution is the exact quantitative application to the expanding CCM interval and its open-strip zero-transfer problem. A targeted audit found the CCM papers stating the approximation gap but not a theorem replacing “sufficiently accurate” by this `L2`/endpoint stability scale. This finding does not claim that the displayed `L2` rate is necessary for the actual structured ground states; it is the sharp universal guarantee available from `L2` error alone.

## 1. Exact evaluation norm on the expanding logarithmic interval

Let `A=log lambda` and identify `H_lambda` unitarily with `L2([-A,A],dt)`. For `z=x+iy`, the transform evaluation is the bounded linear functional

\[
\mathcal L_z(F)=\int_{-A}^{A}F(t)e^{-izt}\,dt.
\]

Its Riesz vector is `t -> exp(i conjugate(z) t)`, hence

\[
\|\mathcal L_z\|^2
=\int_{-A}^{A}|e^{-izt}|^2dt
=\int_{-A}^{A}e^{2yt}dt.
\]

For `y != 0`, symmetry gives

\[
\int_{-A}^{A}e^{2yt}dt
=\frac{e^{2|y|A}-e^{-2|y|A}}{2|y|}
=\frac{\sinh(2|y|A)}{|y|},
\]

and at `y=0` the value is `2A`. This proves the stated formula exactly, including its optimal constant for unrestricted `L2` residuals.

For a closed strip `|Im z|<=a`, the norm is maximized at `|y|=a`, so

\[
\sup_{|\Im z|\le a}|\widehat r_\lambda(z)|
\le E_a(\lambda)\|r_\lambda\|_2.
\]

Since

\[
E_a(\lambda)
=\left(\frac{\lambda^{2a}-\lambda^{-2a}}{2a}\right)^{1/2}
\sim\frac{\lambda^a}{\sqrt{2a}},
\]

we obtain the closed-substrip criterion

\[
\lambda^a\|r_\lambda\|_2\to0.
\]

Taking `a=1/2-epsilon` for every positive `epsilon` is exactly the family of conditions

\[
\|r_\lambda\|_2=o(\lambda^{-1/2+\varepsilon})
\qquad\text{for every }\varepsilon>0.
\]

No zeta input enters this estimate. The `1/2` appears here because that is the half-width of the complex strip that contains the transforms of all nontrivial zeta zeros in the `Xi` variable, not because generic Paley–Wiener theory intrinsically prefers `1/2`.

## 2. Why the full open strip, not only the real line, is load-bearing

Use the standard entire function

\[
\Xi(z)=\xi(1/2+iz).
\]

If `rho=beta+i gamma` is a nontrivial zero of zeta, then the associated zero of `Xi` is

\[
z_\rho=\gamma-i(\beta-1/2).
\]

Since every nontrivial zero satisfies `0<beta<1`, every such `z_rho` lies in

\[
|\Im z|<1/2.
\]

RH is precisely the assertion that these zeros are all real.

The CCM finite spectral triples are designed so that, under their simple-even ground-state hypothesis, the Fourier–Mellin transform of the ground vector has only real zeros. Thus a clean limiting argument does not need to follow every zero individually. If a sequence of nonzero scalar normalizations satisfies

\[
c_\lambda\widehat\xi_\lambda\to\Xi
\]

locally uniformly on the upper and lower parts of the open strip, then each approximant is zero-free there. Hurwitz's theorem makes the limit zero-free there as well because `Xi` is not identically zero. That is already RH.

This explains why convergence only on the real axis is insufficient for the proposed proof. A hypothetical off-line zeta zero becomes a nonreal `Xi` zero at some fixed height `|Im z|=a<1/2`; the approximation has to be stable on a neighborhood of that point. The evaluation norm at exactly that height grows like `lambda^a`.

The regularized determinant does not change this zero argument. CCM obtain the determinant as a nonvanishing exponential factor times `hat xi_lambda`; multiplying or dividing by that factor changes normalization but not the zero set. The quantitative statement here is therefore made directly for `hat xi_lambda`, where the comparison with `hat k_lambda` is cleanest.

## 3. Combination with the proven prolate-model limit

CCM's Section 7 constructs the educated guess

\[
k_\lambda=\mathcal E(h_\lambda)
\]

from the `n=0,4` prolate-wave eigenfunctions. Their Lemmas 7.2–7.3 establish the model side of the limit: suitable prolate eigenfunctions approach the corresponding Hermite functions with an `O(lambda^-2)` sup-norm estimate, and the Fourier–Mellin transforms `hat k_lambda` converge to `Xi` uniformly on closed substrips of the open critical strip.

The missing object is not therefore the transform of `k_lambda`; it is the transfer from this model to the actual minimal eigenvector `xi_lambda` of the restricted Weil form. CCM state this explicitly as one of the two essential missing steps, alongside proving that the smallest eigenvalue is simple with even eigenvector.

For any compact `K` contained in `|Im z|<1/2`, let

\[
a_K=\max_{z\in K}|\Im z|<1/2.
\]

Then

\[
\sup_{z\in K}|c_\lambda\widehat\xi_\lambda(z)-\Xi(z)|
\le
E_{a_K}(\lambda)\|c_\lambda\xi_\lambda-k_\lambda\|_2
+
\sup_{z\in K}|\widehat k_\lambda(z)-\Xi(z)|.
\]

The second term tends to zero by CCM. The first tends to zero under either the displayed `L2` rate or an appropriate weighted endpoint estimate. This gives an explicit, falsifiable target for the missing approximation step rather than an unspecified notion of closeness.

A recent independent numerical/convergence literature around the CCM construction studies finite-mode and finite-prime error budgets and confirms striking numerical convergence, but those computations do not supply this continuum `lambda -> infinity` ground-state comparison. They are useful novelty controls only; the theorem above does not depend on them.

## 4. Ordinary L2 convergence is provably too weak

The expanding support is essential. On a fixed interval, `L2` convergence automatically gives uniform convergence of these Fourier transforms on every compact set because the evaluation norms are fixed. Here the interval length is `2 log lambda`, and the evaluation norms diverge.

### Failure already on the real axis

Set `A=log lambda` and take the even real residual

\[
r_A(t)=A^{-1}\mathbf 1_{[-A,A]}(t).
\]

Then

\[
\|r_A\|_2=\sqrt{2/A}\longrightarrow0,
\]

but

\[
\widehat r_A(0)=\int_{-A}^{A}A^{-1}dt=2.
\]

Thus qualitative `L2` convergence does not even guarantee pointwise Fourier convergence at `z=0` on growing support.

### Exponential endpoint amplification off the real axis

Fix `y>0` and take the even real residual

\[
r_A(t)=e^{-yA}
\left(\mathbf 1_{[A-1,A]}(t)+\mathbf 1_{[-A,-A+1]}(t)\right).
\]

Its norm satisfies

\[
\|r_A\|_2=\sqrt2\,e^{-yA}\longrightarrow0.
\]

At the nonreal point `z=iy`, however,

\[
\widehat r_A(iy)
=e^{-yA}\int_{A-1}^{A}e^{yt}dt
+e^{-yA}\int_{-A}^{-A+1}e^{yt}dt.
\]

The first term tends to the positive constant

\[
\frac{1-e^{-y}}{y},
\]

while the second tends to zero. Thus an error whose `L2` norm is already of order `lambda^{-y}` can still leave an order-one transform defect at height `Im z=y`.

These examples can be replaced by normalized Riesz vectors to saturate the evaluation bound exactly. The elementary even examples are recorded because the CCM candidate ground states and prolate model are even: reflection symmetry by itself does not remove the obstruction.

Therefore the factor `lambda^a` in the `L2`-only estimate is not an artifact of a loose inequality. A weaker conclusion may hold for the actual highly structured residuals, but it must use structure beyond their unweighted `L2` norm.

## 5. The useful escape is endpoint-sensitive structure, not merely faster global norm convergence

The exact transform identity also shows how this negative can be escaped. For `|Im z|<=a`,

\[
|e^{-izt}|\le e^{a|t|},
\]

hence

\[
\sup_{|\Im z|\le a}|\widehat r_\lambda(z)|
\le
\int_{-A_\lambda}^{A_\lambda}|r_\lambda(t)|e^{a|t|}dt.
\]

So it is enough to prove weighted `L1` convergence of the residual for every `a<1/2`. In multiplicative coordinates the weight is

\[
\max(u^a,u^{-a}).
\]

This makes the real research target more precise. The prolate/Weil comparison could succeed through any of the following kinds of information, provided it is proved rather than inferred numerically: sufficiently fast global `L2` convergence; uniform suppression near `u=lambda^{\pm1}` strong enough to beat the Mellin weight; a differential/integral equation forcing cancellation in the residual; or quantitative Sobolev/bandlimited estimates that control the endpoint layers. The finding does not prefer one of these mechanisms.

Conversely, a proof that only establishes

\[
\|c_\lambda\xi_\lambda-k_\lambda\|_2\to0
\]

with no rate or endpoint information leaves a genuine logical gap before zero convergence. The gap is analytic, not numerical.

## Prior-art and novelty audit

The main literature anchor is:

- **Alain Connes, Caterina Consani, Henri Moscovici**, “Zeta spectral triples,” arXiv:`2511.22755` (2025), published in *EMS Series of Lectures in Mathematics* (2026), DOI `10.4171/ELM/37/3`. Their Section 7 proves the locally uniform closed-substrip convergence `hat k_lambda -> Xi`; Section 8 explicitly identifies as a missing step the need to show that `k_lambda` is a sufficiently accurate approximation to a scalar multiple of the actual Weil ground eigenvector `xi_lambda`.

The preceding conceptual/numerical source is Connes–Consani, “Spectral triples and zeta-cycles,” *L'Enseignement Mathématique* **69** (2023), 93–148, DOI `10.4171/LEM/1049`, where the prolate approximation and restricted Weil-form spectral geometry are developed.

The functional-analytic estimate used here is elementary classical Paley–Wiener/RKHS material: the Fourier transform of an `L2` function supported in `[-A,A]` is entire of exponential type `A`, and point evaluation is a bounded functional with the Riesz norm computed above. No novelty is claimed for that fact, Cauchy–Schwarz, or Hurwitz's theorem.

A targeted current audit around the CCM convergence problem, Paley–Wiener point evaluation, prolate ground-state approximation, and recent numerical convergence analyses did not find a peer-reviewed theorem that closes the actual `xi_lambda-k_lambda` step or states this expanding-window `L2` stability rate as its solution. Accordingly the durable claim is classified as an **exact derived reduction/boundary**, not as a new theorem of general Fourier analysis and not as evidence that the required rate actually holds.

## Adversarial boundaries and falsification

1. **The `o(lambda^{-1/2+epsilon})` family is sufficient and sharp for universal `L2`-only control, not logically necessary for the specific CCM residual.** A structured residual may have large `L2` norm yet a tiny transform on the relevant strip because of endpoint suppression or cancellation.

2. **Normalization matters.** The residual must be formed after choosing the scalar `c_lambda` in the same gauge in which `c_lambda hat xi_lambda` is intended to converge to `Xi`. An arbitrarily diverging or vanishing rescaling can make an `L2` statement meaningless while leaving zero sets unchanged.

3. **The simple-even problem remains independent.** Transform convergence does not prove that each finite/semilocal ground-state transform has only real zeros. CCM's first missing step must still be supplied, or replaced by another mechanism ensuring zero-freeness off the real axis for the approximants.

4. **This does not control the finite Fourier cutoff `N`.** It addresses the continuum expanding-support comparison in `lambda`. Galerkin convergence `N -> infinity` at fixed `lambda`, including persistence of the ground-state gap and transfer of coefficient tails, is a separate approximation problem.

5. **The endpoint examples are controls, not models of the actual eigenvector error.** They prove that topology alone is insufficient; they do not predict where the genuine residual is concentrated.

6. **No Euler product is continued into the strip.** The only zeta-side input in the transfer is the entire completed `Xi` function and CCM's proved transform convergence for `k_lambda`. The finite-prime Weil forms themselves arise from the completed explicit-formula framework.

7. **The critical `1/2` is not derived from the abstract exponent lattice.** It enters because all nontrivial zeta zeros map to the open strip `|Im z|<1/2`. Generic compact-support Fourier transforms would give the same evaluation law with whatever strip width the target problem required.

A direct falsification of the universal `L2` boundary would require a uniform point-evaluation estimate on `L2([-A,A])` asymptotically smaller than the norm of its explicit Riesz vector, which is impossible. What remains open is whether the special arithmetic/prolate residual obeys much stronger structural estimates than an arbitrary `L2` vector.

## Consequence for `prime_lattice`

This finding does not displace the current main frontier isolated by `PL-259`–`PL-261`: finite Weil forms already give complete detectability of RH failure, and the load-bearing missing theorem there is **source-forced sign coercivity/positivity**, not another observability result.

It does, however, close a loose end in the parallel spectral-determinant route first audited in `PL-013`. “The prolate model converges to the Weil ground state in `L2`” would still be too weak if meant only qualitatively. A viable convergence theorem must control the residual in a topology that survives the growing logarithmic support and the complex Mellin weights. The exact bare-`L2` target is `lambda^a ||r_lambda||_2 -> 0` at every height `a<1/2`; endpoint-weighted control is an equally legitimate and potentially more natural substitute.

This sharpens the division of labor in the line:

\[
\text{finite Weil detectability}
\quad\text{is already complete (`PL-261`),}
\]

while the spectral approximation route still needs both

\[
\text{simple-even ground-state rigidity}
\]

and

\[
\text{expanding-window transform stability of the actual ground state.}
\]

Neither follows from the abstract prime-exponent lattice, from the existence of very small Rayleigh values, or from qualitative prolate resemblance. Any future result on this branch should therefore be tested against the explicit evaluation scale above before being interpreted as progress toward determinant/zero convergence.