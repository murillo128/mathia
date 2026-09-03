# MI-003 — Ordered local consistency is an information layer that pair scalarization can erase

**Evidence level:** supported; the minimal-order statement is proved only for the ANF-006/ANF-007 bridge and kernel

## Core intuition

Pairwise marginals and scalar pair profiles can preserve every two-point feature while discarding the compatibility relations among overlapping pairs. Ordered local configurations therefore form a genuinely different information layer: the arithmetic content can live in how adjacent relations fit together before any global averaging or moment compression.

## Strongest justified principle

ANF-006 constructs a local ordered-gap certificate that beats the Montgomery--Taylor baseline only because the gap constraint is applied before global pair compression. ANF-007 makes the boundary exact for that bridge: two points cannot improve the baseline, while three consecutive points can. The extra datum is not a third independent pair moment; it is the additive consistency of two adjacent gaps and their sum inside one ordered triple.

This does not prove that order three is universally sufficient, or that the resulting certificate yields RH. It proves a narrower and durable information statement: within the audited kernel, the first successful arithmetic gain appears only after retaining a configuration relation that no single two-point scalarization carries.

## Evidence synthesis and boundaries

The finding complements the finite-pair scalarization obstruction: proliferating finitely many pair channels can still dualize to one signed profile, whereas preserving one ordered local block changes the quotient before that scalarization occurs. The distinction is between **more pair observables** and **higher relational consistency**.

Matched controls remain essential. A configuration-level gain is useful only if it survives the same normalization, source constraints, and global assembly required by the final analytic inequality. Nothing here licenses arbitrary higher-point statistics or claims novelty for classical gap identities.

## Status / novelty

The underlying local inequalities and pair-correlation machinery are literature-backed or exact persisted derivations. The Mathia-specific synthesis is the information boundary: pairwise completeness need not imply ordered-configuration completeness, and ANF-007 supplies an exact minimal-depth witness for one canonical bridge.

## Falsification criterion

Within the ANF-006/007 bridge, exhibit a two-point certificate that strictly improves the Montgomery--Taylor baseline under the same normalization, or show that the three-point gain factors through a single admissible pair profile without retaining the ordered overlap relation.

## Lean-formalizable core

- Two-point no-gain inequality for the audited bridge.
- Three-point certificate and its strict gain.
- Algebraic distinction between independent pair data and the adjacent-gap consistency relation.
