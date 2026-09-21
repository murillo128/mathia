# MI-069 — One crossing controls sign breadth, not boundary conditioning or provenance

**Evidence level:** exact/asymptotic metric synthesis from [AF-479](../../findings/AF-479-prime-gibbs-coordinate-margin-collapses-logarithmically-at-the-prime-zeta-boundary.md), [AF-480](../../findings/AF-480-prime-gibbs-global-half-line-margin-has-the-local-boundary-asymptotic.md), [AF-481](../../findings/AF-481-prime-density-alone-forces-logarithmic-gibbs-boundary-collapse.md), and [AF-482](../../findings/AF-482-prime-density-controls-sharp-global-gibbs-margin.md), qualifying the anchored one-crossing mechanism in AF-478 and MI-068.

The one-crossing property controls the **sign geometry** of a realizable secant, but it does not by itself control how its mass is distributed in the source and target norms as a normalization boundary is approached. For the prime Gibbs curve

`mu_sigma(p)=p^(-sigma)/P(sigma)`, `sigma>1`,

under the canonical coordinate embedding `H(mu)=sqrt(2) mu`, AF-479 proves the tangent law

`rho(1+epsilon) ~ sqrt(P(2)/2) / log(1/epsilon)`.

Equivalently, the tangent norm-breadth ratio `||mu_sigma'||_1/||mu_sigma'||_2` grows logarithmically while the sign pattern remains one-crossing.

AF-480 shows that this is not merely a local obstruction. If `c(sigma_0)` is the best lower Lipschitz constant over the whole anchored half-line `sigma>=sigma_0`, then

`P(sigma_0)c(sigma_0) -> sqrt(P(2)/2)`

as `sigma_0 downarrow1`. Boundary-local norm spreading gives the exact first-order global fidelity scale: finite secants introduce no additional asymptotic loss.

AF-481 and AF-482 then separate conditioning from arithmetic provenance completely at this level. For every discrete sequence `Q` with `N_Q(x)~x/log x`, the same canonical Gibbs construction satisfies both the local tangent law and the sharp global anchored law

`P_Q(sigma_0)c_Q(sigma_0) -> sqrt(P_Q(2)/2)`.

Shifted-composite and smooth pseudo-prime controls reproduce the same normalized global mechanism. The logarithmic collapse and the fact that the worst pair is asymptotically controlled by the singular boundary are therefore consequences of coarse density plus canonical Gibbs geometry, not of rational primality. The residual constant `P_Q(2)` records exact square-summable coordinate locations but does not by itself certify multiplicative prime structure.

The reusable audit has three independent coordinates: **combinatorial secant breadth**, **effective norm breadth**, and **source provenance**. Thin sign geometry can coexist with deteriorating conditioning, and even a sharp global conditioning asymptotic can be explained entirely by a matched coarse source law. Arithmetic credit begins only with a discriminator that survives controls matched at those lower layers.

**Boundary.** AF-481--AF-482 concern the canonical coordinate Hilbert embedding for discrete sources with counting law `N_Q(x)~x/log x`. They do not rule out a different nonlinear representation, a finer multiplicative invariant, or a source class with genuinely different counting asymptotics. None of these conditioning results yields an RH-facing consequence.