---
id: CLUE-weil-positivity-mixed-prime-positive-completion-selector-quotient
type: research-clue
status: accepted
origin: mind
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-096-exact-cover-positive-forms-are-prime-torus-grams-but-sparse-weil-support-needs-infinite-diagonal.md
  - research/weil_positivity/findings/WP-097-mixed-prime-product-completion-gives-sharp-finite-diagonal-threshold.md
---

# Can a canonical quotient of the mixed-prime positive completion recover the Weil selector without losing positivity?

## Observation

WP-096 classifies finite-valued exact-cover-positive forms as positive prime-torus Gram measures and proves that imposing the critical one-prime Weil Fourier rays while deleting every mixed-prime coefficient forces infinite diagonal self-energy. WP-097 shows that this obstruction is not positivity alone: allowing the mixed-prime coefficients of an explicit product completion restores positivity with a sharp finite diagonal threshold. The mixed terms are therefore the mechanism that pays for positivity.

## Research question

Is there an independently forced quotient, conditional expectation, compression, boundary map, or finite--archimedean coupling that starts from a WP-097-type positive completion, removes or neutralizes the mixed-prime modes at the **final selector level**, and retains the exact one-prime Weil coefficients together with a usable positive sign theorem?

The operation must arise from the cover/global geometry itself. A Fourier projection chosen merely to keep the desired rays does not count.

## Why it may matter

This is the first point in the cover-positive program where ordinary positivity and the critical one-prime coefficients coexist with finite energy. If the compulsory mixed-prime completion admits a canonical sign-preserving quotient, it could supply the missing bridge between the finite arithmetic selector and a global positive form. If every natural quotient either keeps the mixed contamination, loses positivity, or recreates the divergent sparse kernel of WP-096, then a broad class of exact-cover Gram completions can be closed.

## Decisive test

Start on a finite prime set `P`, where the WP-097 product measure is an explicit positive density on `T^P`. Classify natural positive contractions/conditional expectations or cover-equivariant quotient maps that preserve every one-coordinate Fourier moment

`phi(p^k)=-(log p) p^{-|k|/2}`

while annihilating all Fourier modes involving at least two prime coordinates. Determine whether positivity and finite diagonal mass force a WP-096-type lower bound after the quotient.

A decisive negative is a theorem that any positive/unital or geometrically admissible map with those one-prime moments must retain mixed modes or acquire divergent diagonal energy. A decisive positive is an explicit canonical map, preferably one compatible with an independently derived archimedean sector, whose induced form has the exact selector and a sign theorem not imported from RH.

## Evidence boundary

No finite--archimedean coupling with the required properties is established. WP-097 proves only existence of a positive mixed-prime completion, not that its mixed coefficients can be removed canonically or that it matches the global Weil form. This file remains a research lead, not evidence for Weil positivity or for RH.

## Research disposition

Accepted, but now sharply narrowed by [`WP-098`](../findings/WP-098-positive-prime-torus-quotients-preserving-coordinate-observables-cannot-erase-mixed-prime-modes.md), [`WP-099`](../findings/WP-099-passive-positive-auxiliary-elimination-cannot-sparsify-the-mixed-prime-completion.md), [`WP-100`](../findings/WP-100-mixed-prime-product-completion-is-haar-singular-at-the-weil-boundary.md), and [`WP-101`](../findings/WP-101-correlations-restore-haar-equivalence-at-critical-diagonal-but-only-below-zygmund-endpoint.md).

`WP-098` closes the same-algebra positive quotient / conditional-expectation route: a unital positive map that preserves each prime-coordinate unitary lies in the multiplicative-domain regime and therefore preserves all mixed products, while the exact first-order Fourier projector that deletes mixed modes is not positivity preserving. Even a state-specific positive sparse output with finite diagonal mass recreates the divergent `WP-096` bound.

`WP-099` closes the natural passive finite--archimedean repair. If a positive global/auxiliary energy reduces to the `WP-097` completion when the auxiliary variable is zero, then eliminating that variable by a Dirichlet principle, Schur complement, or shorted response produces a positive form `S` with `0 <= S <= R_C`. Exact sparse Weil support would require a diagonal at least `D(P)`, while domination forces the output diagonal to be at most the finite input mass `C`; for sufficiently many primes these inequalities are incompatible. If the diagonal is preserved exactly, positivity is even rigid enough to force `S=R_C`, so no mixed coefficient can change at all.

`WP-100` narrows the option of retaining the explicit `WP-097` mixed sector unchanged through the global construction. The natural radial family of those affine product factors is equivalent to product Haar only for `sigma>1/2` and is Kakutani-singular to product Haar for `0<sigma<=1/2`; in particular the exact critical independent-product carrier at `sigma=1/2` is singular for every fixed finite admissible diagonal `C`. Its finite-cylinder Haar densities also have divergent `L^2` norm at the boundary.

`WP-101` shows that this singularity is **not** robust under mixed-prime correlations. At the exact sharp mass `C_*`, a countable mixture of finite-block positive products gives a measure equivalent to product Haar with every exact critical one-prime ray; for any larger mass a Haar background can even make the density bounded below by a positive constant. The surviving obstruction is regularity rather than measure class: the classical Zygmund/Steinhaus endpoint implies that every absolutely continuous completion with the critical first-coordinate moments has density outside `L(log L)^{1/2}`, hence outside every `L^{1+epsilon}`. The construction is deliberately a matched control rather than an intrinsic Mathia mechanism: its block mixture is engineered from the target moments and supplies no archimedean term or independent sign theorem.

The remaining question is therefore genuinely global rather than a hidden positive quotient or a mere singularity escape. A surviving construction may retain a deliberately endpoint-rough mixed-prime sector, use a singular state, or change the finite observable/domain structure before any passive reduction, but it must make the mixed correlations and the archimedean contribution arise from one independently forced geometry. Non-passive relative/off-diagonal or nonlinear reductions remain logically possible, but they must prove their sign independently and cannot inherit it merely from positivity of a hand-built finite-place carrier.