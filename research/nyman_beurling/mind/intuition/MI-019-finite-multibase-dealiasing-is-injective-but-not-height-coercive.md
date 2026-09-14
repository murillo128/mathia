# MI-019 — Finite multibase de-aliasing is injective but not height-coercive

**Evidence level:** exact representation-level obstruction from [NB-127](../../findings/NB-127-finite-multibase-dealiasing-remains-globally-unstable-under-simultaneous-near-aliases.md), strengthening the one-base exact-alias obstruction of NB-126. The translated packets are formal zero-power controls, not asserted actual zeta-zero packets.

A finite family of geometric bases can remove exact aliasing without providing stable absolute-height information. For bases `q_1,...,q_m`, simultaneous Diophantine recurrence gives unbounded shifts `T_k` with

`max_q |exp(i T_k log q)-1| -> 0`.

Under a common vertical translation of a finite zero-power packet, each labelled characteristic root at base `q` is multiplied by that phase. The annihilator coefficient magnitudes are exactly invariant, normalized missing-root margins return continuously to their original values, and every finite sample window returns uniformly when its depth grows slowly enough relative to the phase error.

At the same time the elementary Burnol defect of every translated packet point is `O(T_k^-2)`, so the packet target mass tends to zero. Therefore no continuous positive functional of fixed finite-base recurrence data can uniformly coerce the absolute-height Burnol mass on the formal representation class.

For multiplicatively independent bases such as `2` and `3`, exact phase equality determines the ordinate, but continued-fraction recurrence gives near-returns with error `O(1/T)` along an unbounded sequence. This is the key distinction: **injectivity is not a stability modulus**.

The remaining bridge must make resolution scale explicit. It can use quantitative anti-recurrence for actual zeros, phase accuracy that tightens with cutoff/height, a growing family of independent scales, or richer natural-grid data. Simply combining finitely many non-aliased margins through a stable continuous rule cannot supply the missing absolute-height budget.

**Boundary.** NB-127 does not prove that actual zeta zeros admit the translated controls. An actual-zero theorem may add precisely the missing rigidity. The obstruction applies to representation-level arguments that use only finitely many geometric recurrence descriptors with fixed topology.
