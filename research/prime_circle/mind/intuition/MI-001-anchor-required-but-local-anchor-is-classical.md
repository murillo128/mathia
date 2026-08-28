# MI-001 — Arithmetic information requires an anchor, but not merely a local one

**Evidence level:** supported

## Core intuition

The original prime-circle geometry has two opposite information losses. If a primitive birth shell is treated as an unmarked configuration, absolute arithmetic position is forgotten; if one keeps the common vertex but probes only a finite local jet there, the result collapses to classical cyclotomic/Jordan-totient data. The potentially nonclassical regime is therefore **anchored and nonlocal**.

## Strongest justified principle

A candidate prime-circle invariant capable of distinguishing genuinely arithmetic structure should depend on the common vertex (or equivalent absolute marking) **and** on a finite-distance/global relation among several charges, shells, regions, or uniformizations. Neither an intrinsic invariant of one unmarked shell nor a finite differential jet at the anchor is sufficient.

PC-019 gives the exact obstruction to the first class: for odd `n`, `Phi_{2n}(z)=Phi_n(-z)`, so any unmarked single-shell construction identifies `n` with `2n`. PC-020 gives the obstruction to the second: the complete anchored local expansion of `log Phi_n(e^t)` is determined by `Lambda(n)`, `phi(n)` and the even Jordan totients. PC-001/PC-003 show why the anchor nevertheless matters: `U_n(1)=Lambda(n)` and the full field has an exact interior/exterior reciprocity.

## Boundary cases and failure modes

The statement does not say that every anchored nonlocal observable is new. Resultants, Dedekind/Vasyunin correlations, Farey geometry and cyclotomic refinement already recover classical structures. Nor does it exclude a local construction involving several labeled shells simultaneously; “local” here means a finite jet of a single anchored shell.

## Status / novelty

The component identities are classical or exact-derived. The synthesis is a design constraint, not a claimed theorem in the literature.

## Falsification criterion

Refute this intuition by exhibiting either (i) an unmarked single-shell invariant that distinguishes an odd prime `p` from `2p`, or (ii) a finite anchored single-shell jet invariant not determined by the classical cyclotomic derivative/Jordan-totient data.

## Lean-formalizable core

- `Phi_(2*n)(z)=Phi_n(-z)` for odd `n` and the induced shell isometry.
- Formula for the logarithmic derivatives of `Phi_n(e^t)` at `t=0` in terms of Jordan totients.
- `U_n(z)=phi(n) log|z|+U_n(1/conj z)` away from the charge set.
