# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`, `MI-059-source-point-cubes-block-stable-nonlinear-hilbert-recovery-unless-the-source-geometry-changes`, `MI-060-cube-poorness-does-not-certify-hilbert-fidelity`, `MI-061-square-root-tv-is-the-sharp-hilbert-snowflake-boundary`, `MI-062-scalar-hilbert-repair-has-square-root-and-bernstein-gates`, `MI-063-hard-support-is-a-scale-free-resource-soft-tails-are-not`, `MI-064-soft-sparse-hilbert-fidelity-has-a-sharp-tail-resolution-budget`, `MI-065-compressibility-profiles-turn-tail-decay-into-a-resolution-condition-curve`, `MI-066-realizable-tail-breadth-is-the-minimax-side-of-compressibility`, `MI-067-finite-affine-moment-side-information-only-thins-sparse-positive-fibers-at-support-scale`, `MI-068-one-crossing-secants-turn-bounded-jordan-support-into-scale-free-hilbert-fidelity`, `MI-069-one-crossing-controls-sign-breadth-not-boundary-conditioning`.

AF-451--AF-477 separate ambient mixture complexity from what the admissible source family actually realizes. Large paired-mixture cubes force the sharp Hilbert `k^(-1/2)` loss, scalar radial repair on the unrestricted simplex has the square-root/Bernstein boundary, hard support gives exact `sqrt(s)` distortion, soft tails give only resolution-dependent bounds, and finite affine moments leave positive Hamming cubes unless additional source structure blocks them.

AF-478 supplies the complementary positive mechanism: if every oriented secant has one Jordan side supported on at most `N` atoms, coordinate inclusion has uniform TV-to-Hilbert condition `O(sqrt(N))`. Ordered Gibbs families realize this through one likelihood-ratio crossing on parameter ranges anchored away from a singular normalization boundary.

AF-479 shows that this combinatorial success does not control boundary norm breadth. For the prime Gibbs curve and the canonical coordinate Hilbert embedding,

`rho(1+epsilon) ~ sqrt(P(2)/2) / log(1/epsilon)`.

AF-480 proves that the local tangent loss is the exact first-order global half-line conditioning law for rational primes: if `c(sigma_0)` is the optimal lower Lipschitz constant on `sigma>=sigma_0`, then

`P(sigma_0)c(sigma_0) -> sqrt(P(2)/2)`

as `sigma_0 downarrow 1`.

AF-481 first removes the arithmetic interpretation of the local rate: every discrete source sequence with `N_Q(x)~x/log x` has the same canonical `1/log(1/epsilon)` tangent collapse. AF-482 closes the remaining global caveat. For every such `Q`, the sharp anchored half-line constant satisfies

`P_Q(sigma_0)c_Q(sigma_0) -> sqrt(P_Q(2)/2)`.

Thus first-order prime-scale density, together with the canonical coordinate geometry and one-crossing order, already determines the worst global boundary conditioning. Shifted-composite and smooth pseudo-prime controls reproduce not only the local rate but the exact normalized global asymptotic. The residual constant `P_Q(2)` records square-summable generator locations; it is not evidence that rational-prime multiplicative structure survived.

The live arithmetic-fidelity question is therefore strictly below this entire density-class Gibbs mechanism. A useful prime-derived invariant must distinguish rational primes from matched sources that share the same counting law, one-crossing secant geometry, partition singularity and sharp global canonical margin. Candidate progress must identify genuinely finer relational or multiplicative structure, quantify how it changes the realizable secant/norm geometry, and test it against controls matched at the same lower layers. Better conditioning analysis of the canonical Gibbs curve alone cannot supply that distinction.

## Keep identifiability, provenance, pairwise stability and metric repair separate

Exact injectivity, anchored discrimination, pairwise lower Lipschitz stability, bounded-distortion metric repair and exact radial Hilbertization are different claims. The Gibbs sequence adds another split: local tangent conditioning, sharp global anchored conditioning and arithmetic provenance are also different.

A fidelity theorem must state the source metric, admissible comparison class, anchored versus pairwise quantifiers, target/operator category, upper sensitivity budget, exact versus bounded-distortion requirement, absolute downstream resolution, and whether the favorable source restriction is actually prime-selective. AF-482 shows that even the sharp global margin can be density-generic. The absence of a negative witness is not a positive theorem, one-crossing does not control norm breadth, and a normalization singularity plus first-order density shared by matched controls cannot be credited as rational-prime information.