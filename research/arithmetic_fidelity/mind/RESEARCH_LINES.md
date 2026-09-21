# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable Arithmetic-Fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Identify the first rational-prime discriminator that survives matched generalized-prime controls

**Linked intuitions:** `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-005-test-family-fidelity-has-scale-and-dimension-gates`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-044-finite-sampling-fidelity-is-margin-modulus-relative`, `MI-067-finite-affine-moment-side-information-only-thins-sparse-positive-fibers-at-support-scale`, `MI-069-one-crossing-controls-sign-breadth-not-boundary-conditioning`, `MI-070-exact-sample-cardinality-and-sampling-geometry-are-different-fidelity-resources`.

AF-479--AF-482 identify the canonical Gibbs boundary law. One-crossing secant geometry does not prevent the local and global Hilbert margin from collapsing as `1/log(1/epsilon)` near `sigma=1`; prime-scale counting density already forces that law, and the leading constant is determined by the square mass `P_Q(2)`.

AF-483 removes a stronger provenance escape. There are nonintegral Beurling-prime controls arbitrarily close termwise to the rational primes with `N_Q(x)~x/log x`, exact `P_Q(2)=P(2)`, rationally independent logarithms and therefore free numerical factorization, yet the same sharp Gibbs boundary asymptotic. Density, one-crossing geometry, exact square mass, canonical margin and free multiplicativity are therefore insufficient to identify the rational-prime source.

AF-484 strengthens the finite-data no-go. For any finite real sample set `1<s_1<...<s_m` and arbitrarily small coordinatewise perturbation tolerances, a nonintegral Beurling-prime system can simultaneously preserve prime density, free factorization and every exact value `P_Q(s_j)=P(s_j)`. Asking for more fixed finite prime-zeta moments does not remove the deformation fiber in this source class.

AF-485 locates a qualitatively different exact-fidelity boundary. For general absolutely convergent Dirichlet sources with strictly increasing exponents, equality on any sample sequence with `Re(s_k)->+infinity` determines the complete exponent/coefficient source by successive least-exponent dominance. AF-486 then supplies the fixed-depth quantitative refinement for positive discrete sources: `2J-1` consecutive samples in a window moving to the right determine the first `J` nodes through Hankel determinants, and node recovery remains valid under absolute errors of sharp exponential order `q_J^(-t)`, up to source-dependent Vandermonde/weight conditioning.

The live sampling question has therefore moved beyond fixed-depth existence. At each fixed `J`, moving Hankel geometry gives a joint reconstruction modulus and shows that exponential signal decay is unavoidable rather than an artifact of recursive peeling. The remaining quantitative frontier is how this behaves as depth grows, under signed or complex coefficients, under different sampling geometries, and under conditioning assumptions strong enough to yield a useful uniform source-depth theorem.

The provenance question remains separate. A rational-prime discriminator must use structure not automatically preserved by the AF-483/AF-484 generalized-prime deformation family: integral/additive or congruence incidence, the full analytic Euler/prime-zeta object rather than finitely many fixed values, finer exact Dirichlet data tied across an unbounded family, or quantitative logarithmic relations whose constants survive the destination quotient.

## Keep sign geometry, exact injectivity, quantitative conditioning and arithmetic provenance separate

The current hierarchy contains four independent gates. One-crossing controls the sign breadth of secants; density and square mass control the canonical Gibbs boundary scale; fixed finite Dirichlet samples can still leave large source fibers; and rightward sampling can be both exactly faithful and finitely reconstructive at fixed depth while demanding exponentially fine absolute precision for deeper atoms. None of these facts by itself supplies rational-prime provenance.

Future claims must therefore state which layer is being used: exact source identity, fixed sampled data, a moving finite-depth recovery theorem with its conditioning constants, or a genuinely arithmetic restriction. AF-486 closes the claim that the AF-485 rightward rigidity has no finite-depth stable formulation, but it does not turn exponential signal loss into a uniform deep-source algorithm or distinguish rational primes from every admitted generalized-prime source.
