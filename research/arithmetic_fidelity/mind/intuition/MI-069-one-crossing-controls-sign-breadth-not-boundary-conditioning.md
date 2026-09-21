# MI-069 — One crossing controls sign breadth, not boundary conditioning or provenance

**Evidence level:** exact/asymptotic metric and matched-control synthesis from [AF-479](../../findings/AF-479-prime-gibbs-coordinate-margin-collapses-logarithmically-at-the-prime-zeta-boundary.md), [AF-480](../../findings/AF-480-prime-gibbs-global-half-line-margin-has-the-local-boundary-asymptotic.md), [AF-481](../../findings/AF-481-prime-density-alone-forces-logarithmic-gibbs-boundary-collapse.md), [AF-482](../../findings/AF-482-prime-density-controls-sharp-global-gibbs-margin.md), and [AF-483](../../findings/AF-483-prime-density-square-mass-free-multiplicativity-admit-nonprime-control.md), qualifying the anchored one-crossing mechanism in AF-478 and MI-068.

The one-crossing property controls the **sign geometry** of a realizable secant, but it does not by itself control how its mass is distributed in the source and target norms as a normalization boundary is approached. For the prime Gibbs curve

`mu_sigma(p)=p^(-sigma)/P(sigma)`, `sigma>1`,

under the canonical coordinate embedding `H(mu)=sqrt(2) mu`, AF-479 proves the tangent law

`rho(1+epsilon) ~ sqrt(P(2)/2) / log(1/epsilon)`.

Equivalently, the tangent norm-breadth ratio `||mu_sigma'||_1/||mu_sigma'||_2` grows logarithmically while the sign pattern remains one-crossing.

AF-480 shows that this is not merely a local obstruction. If `c(sigma_0)` is the best lower Lipschitz constant over the whole anchored half-line `sigma>=sigma_0`, then

`P(sigma_0)c(sigma_0) -> sqrt(P(2)/2)`

as `sigma_0 downarrow1`. Boundary-local norm spreading gives the exact first-order global fidelity scale: finite secants introduce no additional asymptotic loss.

AF-481 and AF-482 separate conditioning from arithmetic provenance at the density level. For every discrete sequence `Q` with `N_Q(x)~x/log x`, the same canonical Gibbs construction satisfies both the local tangent law and the sharp global anchored law

`P_Q(sigma_0)c_Q(sigma_0) -> sqrt(P_Q(2)/2)`.

AF-483 then removes a stronger provenance escape. There are nonintegral Beurling-prime sequences `Q={q_n}` arbitrarily close termwise to the rational primes for which `N_Q(x)~x/log x`, `sum q_n^(-2)=P(2)`, and the logarithms `log q_n` are linearly independent over `Q`. Their generated numerical monoid therefore has unique factorization in the chosen generators, yet the canonical Gibbs family has exactly the same leading global margin

`c_Q(1+epsilon) ~ sqrt(P(2)/2)/log(1/epsilon)`.

Thus neither one-crossing geometry, prime-scale density, the exact square mass `P(2)`, nor free multiplicativity identifies the rational-prime source at this interface. A useful discriminator must survive controls matched in all of those quantities and exploit structure that the perturbative generalized-prime model cannot preserve automatically—for example integral/additive or congruence incidence, finer Dirichlet data, or quantitative rather than merely exact logarithmic relations.

The reusable audit has three independent coordinates: **combinatorial secant breadth**, **effective norm breadth**, and **source provenance**. Thin sign geometry can coexist with deteriorating conditioning, and even an exact leading constant plus free numerical factorization can be provenance-generic. Arithmetic credit begins only with a discriminator that survives controls matched at the lower layers actually consumed by the destination.

**Boundary.** AF-481--AF-483 concern the canonical coordinate Hilbert embedding and generalized positive generator sequences; AF-483's control is a Beurling-prime system, not a second subset of ordinary integers. It does not match additive/congruence structure, the full prime-zeta function, higher Dirichlet data, or quantitative Diophantine separation of logarithms. None of these conditioning results yields an RH-facing consequence.
