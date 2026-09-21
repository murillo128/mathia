# MI-069 — One crossing controls sign breadth, not boundary conditioning

**Evidence level:** exact/asymptotic metric synthesis from [AF-479](../../findings/AF-479-prime-gibbs-coordinate-margin-collapses-logarithmically-at-the-prime-zeta-boundary.md), qualifying the anchored one-crossing mechanism in AF-478 and MI-068.

The one-crossing property controls the **sign geometry** of a realizable secant, but it does not by itself control how its mass is distributed in the source and target norms as a normalization boundary is approached. AF-479 makes that distinction exact for the prime Gibbs curve

`mu_sigma(p)=p^(-sigma)/P(sigma)`, `sigma>1`,

under the canonical coordinate embedding `H(mu)=sqrt(2) mu` into `ell^2`.

For the tangent direction, define

`rho(sigma)=sqrt(2) ||mu_sigma'||_2 / ||mu_sigma'||_1`.

If `epsilon=sigma-1` and `L=log(1/epsilon)`, AF-479 proves

`rho(1+epsilon) ~ sqrt(P(2)/2) / L`.

Equivalently, the tangent norm-breadth ratio `||mu_sigma'||_1/||mu_sigma'||_2` grows like `2L/sqrt(P(2))`. The mechanism is explicit: the `ell^1` speed is asymptotic to `2m(sigma)`, while the `ell^2` speed is smaller by the diverging normalization factor `P(sigma)~L`. The sign pattern remains one-crossing throughout; what deteriorates is the metric concentration of the same admissible direction.

This separates two source-complexity coordinates that MI-068 left coupled on anchored half-lines. A bounded Jordan-support side is a sufficient scale-free resource when the parameter range is anchored away from the singular boundary, but one-crossing alone does not provide a uniform open-boundary margin. Indeed the canonical embedding has no positive lower Lipschitz constant on the full family `sigma>1`, even though it remains injective at every fixed interior parameter.

The useful audit is therefore to measure both **combinatorial secant breadth** and **effective norm breadth**. A source class can exclude Hamming-cube switching and still become progressively ill-conditioned because one admissible sign-coherent direction spreads across more coordinates in the norm seen by the destination.

**Boundary.** The logarithmic rate is proved for the rational-prime Gibbs law and this canonical linear Hilbert embedding. It does not rule out a different nonlinear representation, and it is not a prime discriminator: analogous normalization-boundary deterioration can occur for nonprime ordered Gibbs families. The Mertens/prime-zeta asymptotics are load-bearing for the exact `1/log(1/(sigma-1))` rate.