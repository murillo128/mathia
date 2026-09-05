---
id: CLUE-arithmetic-fidelity-nyman-target-recovery-profile
type: research-clue
status: proposed
origin: master-researcher
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-129-convex-restricted-witnesses-induce-quotient-recovery-geometry.md
  - research/arithmetic_fidelity/findings/AF-133-restricted-witness-composition-requires-quotient-compatible-recovery.md
  - research/arithmetic_fidelity/findings/AF-134-minimal-compositional-witness-saturation.md
  - research/prime_lattice/findings/PL-020-nyman-gram-blaschke-orthogonality.md
  - research/nyman_beurling/README.md
---

# Which target-sensitive data make Nyman Gram compression quantitatively faithful?

## Observation

AF-133 proves, for its finite witness/Markov setting, that a recovery has finite transport coefficient only if it maps invisible downstream residuals to invisible upstream residuals. Small stagewise errors are otherwise insufficient.

AF-134 further gives the minimal backward witness saturation for declared recovery maps. Its application warning is concrete: a proposed small side mark is not a useful compression repair if its required saturation already recovers the full discarded dual information.

An arithmetic instance is already available. In the Nyman Hardy model, PL-020 writes the generators as `psi_n=B phi_n`, where multiplication by the common inner Blaschke factor is an isometry. Their Gram matrices agree exactly, but for the fixed normalized target `k_1(s)=1/s`,

`dist(k_1,span psi_n)^2 = 1-|B(1)|^2 + |B(1)|^2 dist(k_1,span phi_n)^2`.

Thus the omitted target alignment can carry precisely the off-line-zero obstruction while every generator-Gram statistic remains unchanged.

## Research question

On finite Nyman sections, what source-natural enrichment of Gram data preserves approximation distance with a quantified stability modulus as section size grows? Start with the actual target pairings `b_i=<psi_i,k_1>` and compare full, projected, and spectrally truncated versions of `b`, rather than adding an arbitrary copy of the target or zero divisor.

## Why it may matter

This would instantiate the fidelity theory in an arithmetic compression and distinguish exact finite sufficiency from useful asymptotic stability. It complements the Nyman line's approximation-rate problem: the present question concerns the information and regularity that a proposed compressed certificate must retain.

## Decisive test

Define the finite source class and its admissible coordinate changes. Use the standard reference identity `d^2=||k_1||^2-b^*G^dagger b` with consistent inner-product convention and singular-Gram treatment. Construct same-Gram/different-target-distance controls, then determine which proposed target summaries still identify them. For any surviving enrichment, bound distance error in its declared data norm, including the sensitivity of small Gram eigenvalues and their target weights.

Use AF-133/AF-134 directly only if a legitimate finite statistical-channel model is specified; otherwise prove the deterministic analogue needed here. For the declared reconstruction, compute the backward saturation of the retained target witnesses and test whether it is materially smaller than the full target-pairing data. A useful outcome is an explicit uniform recovery modulus for an arithmetic family or an explicit sequence with vanishing retained-data discrepancy and nonvanishing target-distance error. Merely deriving the standard projection formula or storing all omitted information is not the residual result.

## Evidence boundary

The PL-020 identity and AF-133 quotient criterion are established only in their stated settings. Their quantitative transfer to compressed Nyman certificates is unproved. No norming constant, approximation rate, control of a hypothetical Blaschke factor, or RH consequence is assumed.
