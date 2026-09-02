---
id: CLUE-weil-inertia-full-packing-orbit-quotient-characters
type: research-clue
status: resolved
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-102-full-recurrent-packing-is-an-exact-collapsed-circle-rotation.md
  - research/weil_inertia/formalization/WI102CollapsedRotation.lean
  - research/weil_inertia/findings/WI-096-residual-prime-rank-defect-is-exact-free-cycle-count.md
  - research/weil_inertia/findings/WI-099-residual-prime-rank-defect-is-single-rotation-resonance.md
  - research/visual_exploration/visualizations/shared-source-full-packing-constraints.md
---

# Do full-packing defect modes form quotient characters that constrain shared-source intersections?

## Observation

WI-102 identifies the full-packed residual map, after collapsing its common deleted interval, with a rotation on `Z/tZ`, and its Lean formalization makes the quotient by the generated rotation subgroup explicit. WI-096 independently identifies the true row kernel with functions constant on free cycles subject to one zero-mean relation. This suggested that the `g-1` defect dimensions should be organized canonically by the nontrivial characters of the cyclic quotient rather than by an arbitrary cycle basis.

The same structure suggested a source-labelled question not visible in scalar pairwise rank: if two distinct positive-defect full-packed target interactions share one source prime `p` at the same observation length `N`, can one nonzero source row-kernel vector lie in both pairwise defect spaces? Exact finite exploration found no such example and motivated an intersection theorem.

## Research question

First, identify the single-pair full-packed row kernel constructively as the augmentation hyperplane on

\[
Q=(\mathbf Z/t\mathbf Z)/\langle R\rangle\simeq\mathbf Z/g\mathbf Z,
\qquad g=\gcd(R,t),
\]

with nontrivial quotient characters pulling back to an explicit source-coordinate basis.

Then determine whether two distinct simultaneous positive-defect full-packed targets `q_1,q_2` sharing one source prime can have

\[
K_1\cap K_2\ne\{0\}.
\]

The original exploratory formulation distinguished equal and opposite centers in the canonical nearest-boundary charts. Research resolving the clue showed that this distinction is not the correct one in the actual shared source coordinates: a complement boundary contributes a source-side diagonal phase, which translates the residue-kernel chart. After restoring that phase, all simultaneous actual holes have one common center.

## Why it may matter

A trivial intersection is information unavailable from the individual scalar defects `tau_{p,q}`. It means two large pairwise rank losses cannot be charged to the same hidden source direction and therefore supplies exactly the kind of simultaneous/source-labelled consistency that WI-096 and WI-102 identified as the next route beyond pairwise rank optimization.

## Decisive test

Construct the quotient-character normal form from WI-096/WI-102 without numerical rank tolerance, restore the source phase for both orientations of the nearest pairwise boundary, and compare two target kernels in one common source coordinate system. A proof that the resulting equality systems force every source coordinate to zero resolves the clue positively; one exact nonzero common vector refutes it.

## Evidence boundary

The clue itself is not evidence. The earlier visualization supplied exact finite computational motivation but expressed mixed-sign configurations in unsigned canonical short-boundary charts; mixed-sign shared-kernel conclusions require the source phase correction established in WI-104. No zeta-zero or Yang-covariance improvement follows from the clue alone.

## Research disposition

Outcome: supported

Resolved by:
- [[research/weil_inertia/findings/WI-104-simultaneous-full-packed-prime-defects-have-trivial-shared-source-intersection]]

WI-104 proves the quotient normal form exactly and proves the stronger simultaneous statement

\[
K_1\cap K_2=\{0\}
\]

for any two distinct positive-defect full-packed close-prime targets sharing one source prime at one observation length. Equivalently, their horizontally concatenated cross Gram has full source row rank. The proof also corrects the coordinate picture: once the complement-boundary diagonal phase is restored, the actual deleted intervals are always concentric, and the common exterior reduces to a finite word with two periods. Fine--Wilf periodicity plus one forced-zero collar kills every common-period class.