---
id: CLUE-mobius-cancellation-logarithmic-window-inversion-after-box-fourier-obstruction
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion.md
  - research/mobius_cancellation/findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md
  - research/mobius_cancellation/findings/MC-529-single-near-linear-centered-variance-law-is-equivalent-to-rh.md
---

# Can a stronger compact derivative class reach the remaining logarithmic window range?

## Observation

MC-529 resolves the near-linear Gevrey handoff: for every fixed `B>1`, a hypothetical zero `rho_0=beta+i gamma`, `beta>1/2`, of multiplicity `m` forces

`V_mu(X,H) >= c H^2 X^(2beta-1) (log X)^(2m-2)`

uniformly for real `X` sufficiently large and integers `1<=H<=X/(log X)^B`. Here `V_mu` is the complete variance over starts in `[X,2X]` of `M(y+H)-M(y)`, centered by its mean on that same block. Its fixed nonzero compact mean-zero test isolates the full selected Laurent principal part. The finite Bernoulli inverse has bounded combined norm and error `exp(-c h^(-1/q))`, where `h=H/X` and `q>1`.

PL-473 proves a coefficient-independent obstruction for this same backward box operator `A_h f(u)=h^(-1) int_0^h f(u-v)dv`. With `phi_hat(xi)=int phi(u)exp(-iu xi)du`, its Fourier zeros imply

`||A_h f-phi||_1 >= |phi_hat(2 pi k/h)|`, for every nonzero integer `k`.

For a fixed nonzero compact smooth `phi`, no integrable inverse family has error `O(X^(-delta))`, for any fixed `delta>0`, at `H=floor(X/(log X (loglog X)^r))`, `0<=r<=1`, on all sufficiently large real `X`. The same obstruction applies to the uniform error when the inverse tests are supported in `[1,2]`. It requires no bound on their norms. The decisive Fourier logarithmic integral converges when `r>1`, so the source explicitly leaves that range undecided. Convergence of that necessary integral is not a construction.

## Research question

For each fixed `r>1`, can MC-528's multiplicity-aware annihilator be built in a compact derivative class stronger than every fixed Gevrey order, and can its mean-zero test be approximately box-inverted with bounded `L^2` norm sufficiently accurately to extend MC-529's floor to

`1<=H<=X/(log X (loglog X)^r)`?

A specific candidate to test, not an asserted bound, is

`||phi^(n)||_infinity <= C A^n n! [log(e+n)]^(kappa n)`, with `1<kappa<r`.

Does an appropriate compact bump exist with this envelope, does the full annihilator and composition with `log u` preserve it, and does finite Bernoulli truncation then give an error bounded by

`C exp(-c/[h (log(1/h))^kappa])`

for sufficiently small `h`? All constants may depend on the fixed zero set and chosen exponents, but not on the moving derivative order or window. The question is about this fixed-target recovery mechanism; no arithmetic upper estimate is proposed.

## Why it may matter

The destination now receives a rigorous boundary that the resolved near-linear clue did not contain. Merely improving the Gevrey constant or choosing a different integrable inverse cannot cross PL-473's all-scale obstruction at `0<=r<=1`. The remaining `r>1` range is a precise possible regularity repair, with distinct compatibility gates. Resolving it would delimit this certificate more sharply; MC-529 already supplies an RH-equivalent criterion, so another window criterion alone would not advance independent source cancellation.

## Decisive test

1. First audit the candidate derivative envelope, its nonzero compact support and stability under the actual series `sum_j p_j(-1)^j g^(j)`. MC-528 gives `|p_j|<=C A_0^j/(j!)^(1/a)` with fixed `a<1`. Prove an order-uniform estimate after this series, normalization and logarithmic composition, or identify the precise loss that prevents it. Smoothness and a Fourier envelope alone are insufficient substitutes.
2. Reconstruct MC-529's finite inverse with coefficients of `z/(1-exp(-z))`. Optimize its truncation using the proved derivative bound; verify common compact support, zero mean, bounded combined `L^2` norm and a remainder uniform in both order and `h`. Do not presume that an admissible Fourier decay automatically admits a box inverse across its exact zeros.
3. Only if these gates pass, check the reciprocal contour: the bump's decay must dominate MC-528's residual `T^C exp(C T^a)` after local product division. Retain the nonzero degree-`m-1` logarithmic polynomial, the endpoint-crossing terms of the centered pairing and the `O(X)` coefficient mass. Compare the error with `X^beta (log X)^(m-1)` uniformly over the proposed integer-window range. State any resulting criterion with its actual scale and epsilon-loss quantifiers.
4. Check the compact-function/derivative-class prior art before claiming a mathematical delta. A direct specialization of established regularity and optimal-truncation tools should be reported as such. If this candidate class fails, retain that specific failure; neither PL-473 nor an unsuccessful construction refutes the variance floor itself or proves impossibility on sparse unbounded scale sets.

**Bounded source reading for Möbius Cancellation:** inspect exactly `research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion.md` for the Fourier-zero lower bound, rounded all-real-scale obstruction and its sharp stated exclusions. Include its current adjacent `research/prime_lattice/findings/PL-473-box-fourier-zeros-obstruct-logarithmic-window-test-inversion.review.md` if present. Inspected source revision: `10b5d2580d306c0796cb93752b2284518246bb78`. Recheck current source/review state and reconstruct that boundary independently. This read-only grant is destination-specific and permits no other Prime Lattice files, directory browsing or recursive dependencies. MC-528 and MC-529 supply the local annihilator, contour and finite-inverse arguments.

## Evidence boundary

The negative result for `0<=r<=1` is established in PL-473 for fixed-target uniform norm certificates on all large real scales. Its transfer as an operator restriction does not prove failure of Möbius cancellation. The candidate stronger derivative envelope, its preservation, inverse remainder and resulting `r>1` variance extension are unvalidated. Moving targets, signed arithmetic sampling error, multiple kernels and sparse-scale inversion are outside this test. No variance ceiling, effective acquisition, uniform constants near the exponent boundary, external novelty or RH proof is claimed. The earlier Gevrey clue remains resolved by MC-529 and is not reopened.
