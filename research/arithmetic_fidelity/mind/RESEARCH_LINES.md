# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable Arithmetic-Fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Identify the first rational-prime discriminator that survives matched generalized-prime controls

**Linked intuitions:** `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-005-test-family-fidelity-has-scale-and-dimension-gates`, `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-044-finite-sampling-fidelity-is-margin-modulus-relative`, `MI-067-finite-affine-moment-side-information-only-thins-sparse-positive-fibers-at-support-scale`, `MI-069-one-crossing-controls-sign-breadth-not-boundary-conditioning`, `MI-070-exact-sample-cardinality-and-sampling-geometry-are-different-fidelity-resources`.

AF-479--AF-482 identify the canonical Gibbs boundary law. One-crossing secant geometry does not prevent the local and global Hilbert margin from collapsing as `1/log(1/epsilon)` near `sigma=1`; prime-scale counting density already forces that law, and the leading constant is determined by the square mass `P_Q(2)`.

AF-483 removes a stronger provenance escape. There are nonintegral Beurling-prime controls arbitrarily close termwise to the rational primes with `N_Q(x)~x/log x`, exact `P_Q(2)=P(2)`, rationally independent logarithms and therefore free numerical factorization, yet the same sharp Gibbs boundary asymptotic. Density, one-crossing geometry, exact square mass, canonical margin and free multiplicativity are therefore insufficient to identify the rational-prime source.

AF-484 strengthens the finite-data no-go. For any finite real sample set `1<s_1<...<s_m` and arbitrarily small coordinatewise perturbation tolerances, a nonintegral Beurling-prime system can simultaneously preserve prime density, free factorization and every exact value `P_Q(s_j)=P(s_j)`. Asking for more finite prime-zeta moments does not remove the deformation fiber in this source class.

AF-485 locates a qualitatively different exact-fidelity boundary. For general absolutely convergent Dirichlet sources with strictly increasing exponents, equality on any sample sequence with `Re(s_k)->+infinity` determines the complete exponent/coefficient source by successive least-exponent dominance. Hence right-unbounded countable prime-zeta samples are exactly source-faithful even though every finite exact sample family is not.

The live sampling problem is now quantitative rather than merely injective: determine how sampling growth and absolute accuracy must scale to recover a prescribed finite source depth. Exact rightward rigidity is exponentially ill-conditioned for deep atoms, so a useful theorem must state a recovery modulus rather than infer stability from uniqueness.

The remaining provenance question is also sharper. A rational-prime discriminator must use structure not automatically preserved by the AF-483/AF-484 generalized-prime deformation family: integral/additive or congruence incidence, the full analytic Euler/prime-zeta object rather than finitely many values, finer exact Dirichlet data tied across an unbounded family, or quantitative logarithmic relations whose constants survive the destination quotient.

## Keep sign geometry, exact injectivity, quantitative conditioning and arithmetic provenance separate

The current hierarchy contains four independent gates. One-crossing controls the sign breadth of secants; density and square mass control the canonical Gibbs boundary scale; finite exact Dirichlet samples can still leave large source fibers; and an unbounded rightward sample family can be injective while remaining numerically unstable. None of these facts by itself supplies rational-prime provenance.

Future claims must therefore state which layer is being used: exact source identity, finite sampled data, a stable reconstruction estimate, or a genuinely arithmetic restriction. A theorem that only proves uniqueness from exact asymptotic samples must not be promoted to finite-precision fidelity, while a finite matched-control construction must not be extrapolated to the full analytic object without a separate continuation or rigidity argument.
