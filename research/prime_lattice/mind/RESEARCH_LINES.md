# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the actual completed-Weil corner decomposition with moving-diagonal tail control

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`, `MI-019-moving-green-atoms-require-tail-anti-concentration-beyond-weighted-l1`.

PL-297--PL-312 close the fixed-order state-side and limiting outer gates. PL-313 identifies the compressed-corner communication channel: for compact physical mismatch the finite-`s` Green transfer reaches the unique obstructed regular outer direction through the scalar endpoint moment `M_±`.

PL-314 now sharpens the hypothesis needed to extend that transfer to a genuine endpoint tail. Weighted `L^1(dQ)` control alone is insufficient. The stretched Green measure has a moving diagonal atom at `q=r`, which samples physical logarithmic distance `Q=r/s`; one fixed smooth `L^1` mismatch can place sparse bumps there with arbitrarily small total mass yet produce order-one normalized transfer along a sequence `s_n->0`.

A clean sufficient condition is

`m in L^1(dQ)` and `Q m(Q) -> 0`.

Under this tail law the moving-diagonal contribution vanishes and the rank-one limit from PL-313 survives. The condition is not claimed necessary: BV, monotonicity, a stronger boundary expansion, or another source-structured anti-concentration estimate may give the same control.

The remaining branch-specific theorem is therefore stronger than existence of the weighted endpoint moment. It must derive an overlap decomposition for the actual completed-Weil eigenbranch, match the singular amplitude, and prove enough tail regularity or anti-concentration to suppress `Q~1/s` concentration before invoking the scalar `M_±` balance.

## Prove a rational-prime-specific sign or first-crossing law only after stable matching

The Green-kernel transfer, universal stretched profile and exact regular inverse are geometric. The scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual mismatch/source relation or selected singular amplitude after the finite-`s` matching theorem **and its moving-tail control** are proved.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep outer geometry, weak tail norms, moving sampling and arithmetic sign separate

PL-313 closes the geometric rank-one channel for compact mismatch. PL-314 shows why a weak integrated tail norm cannot automatically pass through a singular moving observation: negligible `L^1` mass can remain order-one at the moving Green diagonal. Future work must state which property of the actual branch rules out that concentration. Only after this stability gate is crossed does the scalar source balance become the relevant arithmetic object.