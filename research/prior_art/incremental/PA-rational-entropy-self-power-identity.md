---
id: PA-rational-entropy-self-power-identity
type: prior-art
canonical_name: Rational entropy and integer self-power identity
aliases:
  - Common-denominator equal-entropy identity
kind: finite entropy identity
topics:
  - rational probability distributions
  - logarithmic moments
---

# Rational entropy and integer self-power identity

## What it is

For positive integers with `sum a_i=sum b_j=T`, Shannon entropy satisfies
`H(a/T)=log T-(1/T)sum a_i log a_i`. Hence equal entropies are equivalent to
`product a_i^(a_i)=product b_j^(b_j)`.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-593-integer-first-jet-rigidity-does-not-give-a-rational-precision-gap|AF-593]] uses this classical conversion for exact reciprocal-mass and logarithmic-moment matching. Its distinctness, nonintegrality and generator-cutoff constraints remain additional requirements.

## Known scope and limits

Leinster's Theorem 7.2 uses the identity to show that equal real entropies give equal entropy residues when denominators are prime to the modulus. It does not identify the distributions or supply an admissible rational replacement set. No RH implication follows.

## Related prior art

Shannon entropy is the underlying functional; the common-denominator identity is the object registered here, not a new entropy theorem.

## Evidence and provenance

- Tom Leinster, [*Entropy modulo a prime*, arXiv:1903.06961v3](https://arxiv.org/abs/1903.06961v3), §7, proof of Theorem 7.2, equations (101)–(105).
- Trigger: `research/arithmetic_fidelity/findings/AF-593-integer-first-jet-rigidity-does-not-give-a-rational-precision-gap.md`, exact rational certificate and prior-art comparison, inspected at `67319d8a8695f0955a4fcfd31e91e199ad74c78b`.
