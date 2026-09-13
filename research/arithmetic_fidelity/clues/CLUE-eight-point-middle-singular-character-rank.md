---
id: CLUE-arithmetic-fidelity-eight-point-middle-singular-character-rank
type: research-clue
status: resolved
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-310-prime-phase-relation-lattice-is-cyclic-and-pentagon-is-first-compatible-zero-geometry.md
  - research/arithmetic_fidelity/findings/AF-316-parity-controls-minimal-harmonic-lift.md
  - research/arithmetic_fidelity/findings/AF-317-antipodal-extension-recursion-breaks-six-point-singular-rigidity.md
---

# Does the eight-point middle-singular zero fiber force a second character relation?

## Observation

AF-316 leaves the even-support recovery theorem singular at `e_m=0`. AF-315 removes that singularity for six rational-prime phases because `e_3=0` forces a globally antipodal root set and hence more than one independent integer-character relation, contradicting AF-310's cyclic prime-phase relation lattice.

AF-317 proves that this geometric implication breaks immediately at eight points: centered unit-circle configurations with `e_4=0` can be nontorsion and need not be globally antipodally invariant. The remaining arithmetic question is therefore not torsion versus nontorsion, but the exact **rank** of the integer-character lattice on the singular zero fiber.

## Research question

Let

`M_8^sing = { Z in (S^1)^8 : s_1(Z)=0, e_4(Z)=0 }`

and normalize by one phase to obtain a subset of `(S^1)^7`. Does `M_8^sing` contain a configuration whose integer-character relation lattice has rank at most one, or does every point of the singular centered fiber still satisfy at least two independent character relations?

The first outcome makes the singular geometry compatible with the strongest elementary rational-prime restriction in AF-310. The second would produce a new source-independent exclusion theorem strong enough to remove the `e_4=0` recovery singularity for any multiplicatively independent prime-log orbit.

## Why it may matter

This is the exact gate between AF-310 and AF-316 at the first unresolved even support. AF-317 has already killed the weaker arguments based on torsion points and global antipodal symmetry. A rank-one witness would show that character-lattice arithmetic alone cannot repair the even recovery theorem at eight points; a rank-two theorem would close the singular stratum without needing a deeper transcendence or incidence result.

## Decisive test

Work on the ordered regular part of `M_8^sing` and audit the character map directly.

1. Determine the real dimension and regular locus of the simultaneous constraints `s_1=0` and `e_4=0`, taking the self-inversive phase constraint on `e_4` into account rather than counting it as two generic real equations.
2. For two independent integer characters `chi_a, chi_b`, determine whether `M_8^sing` can be locally contained in the codimension-two torsion coset `chi_a=xi`, `chi_b=eta`.
3. Either prove by a Baire/analytic-rigidity argument that rank-`0/1` points form a nonempty residual subset of some regular component, or prove that the defining equations force a second character relation everywhere.
4. Stress-test any genericity claim against AF-317's antipodal-extension family, which visibly carries at least one torsion relation and therefore sits on a nongeneric comparison stratum.

A single exact rank-`0/1` witness is enough to kill the universal rank-two hypothesis. Conversely, a universal rank-two conclusion must identify the two relations intrinsically rather than infer them from the AF-317 example's deliberately inserted antipodal pair.

## Evidence boundary

AF-317 supplies only a nontorsion, non-globally-antipodal point in `M_8^sing`; it does not bound that point's full relation-lattice rank. AF-310 bounds rational-prime common-time phase points by rank one but does not imply such a point exists in the singular fiber. No eight-prime exact zero, singular-fiber incidence, or RH consequence is established by this clue.

## Research disposition

Outcome: supported

Resolved by:
- [[research/arithmetic_fidelity/findings/AF-318-antipodal-extension-has-residual-rank-one-character-lattice.md]]

AF-318 proves a stronger version of the first alternative: inside AF-317's exact middle-singular antipodal-extension family, the normalized integer-character relation lattice has rank exactly one on a dense residual subset. Hence the universal rank-at-least-two alternative is false. This resolves only the source-independent character-rank gate; rational-prime incidence in the singular fiber remains open.