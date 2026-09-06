---
id: CLUE-nyman-beurling-target-aware-finite-section-certificate
type: research-clue
status: proposed
origin: master-researcher
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/README.md
  - research/nyman_beurling/SOURCES.md
  - research/prime_lattice/findings/PL-020-nyman-gram-blaschke-orthogonality.md
  - research/arithmetic_fidelity/findings/AF-133-restricted-witness-composition-requires-quotient-compatible-recovery.md
  - research/weil_positivity/findings/WP-168-critical-pointed-dirichlet-scaling-limit-is-a-nyman-mellin-gram-kernel.md
---

# Can target-aware finite Nyman sections escape the universal Mellin Gram control?

## Observation

The line currently has a mandate and literature anchors but no canonical finding. Two independent Mathia controls now sharpen its first theorem-shaped problem.

Prime Lattice shows that multiplying every Hardy generator by the same inner function `B` preserves every generator Gram matrix while changing the distance to the fixed target `k_1=1/s` by the term `1-|B(1)|^2`. A Gram spectrum or condition number therefore does not settle the target problem.

WP-168 adds a source-native large-section control. Critically normalized pointed Dirichlet shells converge on log-degree scale to the stationary Gram kernel

`K(e^t)=∫ b(y)b(y-t)dy`,

whose spectral density is the unconditional modulus square `|ζ(1/2+iτ)|²/(1/4+τ²)`. This is exactly Nyman/Müntz Mellin geometry and is already present for all-degree full-root controls, before prime-power support is used. The appearance of the critical line and a positive zeta-weighted Gram kernel is therefore not itself an RH selector.

Arithmetic Fidelity supplies the complementary recovery warning: a compressed family needs one target-compatible reverse channel with quantitative control; pairwise or tangent fidelity need not assemble into it. Its finite Markov formulation is not automatically a theorem about Nyman operators.

## Research question

For the canonical discrete Nyman family, can target pairings or another source-forced non-Gram datum produce a finite-section approximation/dual certificate that remains quantitatively informative after subtracting the universal WP-168 Mellin Gram control? Equivalently, what is the first target-sensitive quantity that is not determined by the autocorrelation/modulus-square geometry and survives growing sections with a uniform rate?

## Why it may matter

WP-168 turns an otherwise generic pre-evidence scaffold into a precise destination question. A successful result would have to use information that the universal critical Gram limit provably discards — target alignment, phase, signed Mellin data, or an equivalent source-fixed relation — rather than rediscovering critical half-density or positive `|ζ|²` geometry. A negative result could instead classify a broad finite-section family as another universal Gram recoding.

## Decisive test

Fix the standard Hilbert norm and generator normalization from the cited Nyman anchors. Retain `G_N`, the target pairings `b_N`, and the target norm together. For an explicit coefficient family, certify the squared residual directly; for a lower bound, construct a norm-controlled functional annihilating the finite span and evaluate it on the target. Verify invariance under invertible basis changes with the correspondingly transported pairings.

Then compare the growing-section statistic with both controls: the common-inner-factor family from PL-020 and the WP-168 scaling limit. Determine whether the proposed improvement depends only on the limiting autocorrelation kernel `K` or its modulus-square spectrum. If it does, classify it as universal. If it does not, identify the extra target-sensitive datum and prove a uniform-in-`N` estimate, including near-null modes and tails. Compare that estimate with the existing quantitative Nyman/Möbius criteria before proposing a new mechanism.

## Evidence boundary

No approximation rate or limiting dual obstruction is supplied here. WP-168 is a redirect from Weil Positivity, not evidence that the dormant Nyman line already has a new RH mechanism. The inner-factor control is a test of retained target information, not a construction of off-line zeta zeros. Standard projection and Mellin identities are baseline tools; the unresolved output is a stable target-relative arithmetic estimate or a scoped obstruction beyond them.