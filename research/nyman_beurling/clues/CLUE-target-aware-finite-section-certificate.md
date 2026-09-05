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
---

# Can target-aware finite Nyman sections yield a stable approximation or dual certificate?

## Observation

The line currently has a mandate and literature anchors but no canonical finding. A relevant obstruction from Prime Lattice is exact: multiplying every Hardy generator by the same inner function `B` preserves every generator Gram matrix, while its distance to the fixed target `k_1=1/s` acquires the term `1-|B(1)|^2`. Consequently a Gram spectrum or condition number alone does not settle the target problem.

Arithmetic Fidelity supplies a complementary principle: a recovery between compressed descriptions needs to respect the information quotient and control its transport amplification. Its finite Markov formulation is not automatically a theorem about Nyman operators.

## Research question

For the canonical discrete Nyman family, can retained target pairings produce an explicit approximation family with a controlled error across growing sections, or a dual certificate that pinpoints why such a family cannot attain a proposed rate? The object is the actual target-relative distance, not a basis-dependent coefficient pattern.

## Why it may matter

This gives the line a first theorem-shaped problem while preventing a numerical Gram experiment from overlooking the RH-sensitive target alignment. Even a conditioning obstruction for one well-defined approximation family would be a useful first result.

## Decisive test

Fix the standard Hilbert norm and generator normalization from the cited Nyman anchors. Retain `G_N`, the target pairings `b_N`, and the target norm together. For an explicit coefficient family, certify the squared residual directly; for a lower bound, construct a norm-controlled functional annihilating the finite span and evaluate it on the target. Verify invariance under invertible basis changes with the correspondingly transported pairings.

Test the same procedure on the common-inner-factor control above. Then isolate the precise estimate needed to pass from finite sections to a uniform-in-`N` rate, including near-null modes and tails. Compare that estimate with the existing quantitative approximation literature and Möbius criteria before proposing a new mechanism. Finite calculations should falsify unstable candidates, not count as evidence of limiting closure.

## Evidence boundary

No approximation rate or limiting dual obstruction is supplied. The control `B` is a test of what the data retain, not a construction of actual off-line zeta zeros. Standard projection identities are baseline tools; the unresolved output is a stable arithmetic estimate or a scoped obstruction beyond them.
