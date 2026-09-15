# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the actual completed-Weil corner decomposition with source-specific moving-tail control

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`, `MI-019-moving-green-atoms-require-tail-anti-concentration-beyond-weighted-l1`.

PL-297--PL-312 close the fixed-order state-side and limiting outer gates. PL-313 identifies the compressed-corner communication channel: for compact physical mismatch the finite-`s` Green transfer reaches the unique obstructed regular outer direction through the scalar endpoint moment `M_±`.

PL-314 sharpens the hypothesis needed to extend that transfer to a genuine endpoint tail. Weighted `L^1(dQ)` control alone is insufficient. The stretched Green measure has a moving diagonal atom at `q=r`, which samples physical logarithmic distance `Q=r/s`; one fixed smooth `L^1` mismatch can place sparse bumps there with arbitrarily small total mass yet produce order-one normalized transfer along a sequence `s_n->0`.

PL-315 now rules out a much broader regularity shortcut. The counterexample can be chosen `C^infty`, in every `W^{k,1}(dQ)`, with arbitrarily small physical `W^{1,1}` norm, inside every subcritical Sobolev space `H^alpha`, `alpha<1/2`, and inside every all-log Fourier moment space used by the current bootstrap. It can even satisfy the critical envelope `m(Q)=O(1/Q)` while `limsup Qm(Q)>0`, and the moving atom still sees order one.

Thus neither the all-log hierarchy of PL-291--PL-292, generic BV/`W^{1,1}`, arbitrary smoothness, nor every subcritical Sobolev gain justifies the corner reduction. The clean PL-314 condition `Qm(Q)->0` remains sufficient, and PL-315 shows why a mere `O(1/Q)` remainder is not enough. The remaining branch-specific theorem must come from the actual completed-Weil eigen-equation and force a genuinely source-structured tail law: `Qm(Q)->0`, an asymptotic expansion with an `o(1/Q)` remainder, monotone/one-sided tail structure, or a direct estimate of the moving samples `m(r/s)`.

Only after that moving-scale stability gate is crossed should the scalar `M_±` balance be used as the arithmetic endpoint.

## Prove a rational-prime-specific sign or first-crossing law only after stable matching

The Green-kernel transfer, universal stretched profile and exact regular inverse are geometric. The scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual mismatch/source relation or selected singular amplitude after the finite-`s` matching theorem **and its source-specific moving-tail control** are proved.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep outer geometry, global regularity, moving sampling and arithmetic sign separate

PL-313 closes the geometric rank-one channel for compact mismatch. PL-314 shows why a weak integrated tail norm cannot automatically pass through a singular moving observation. PL-315 shows that this failure is not repaired by broad smoothness or by every regularity class currently below the critical half derivative: sparse saturation can survive all of them.

Future work must therefore state which **source equation property** rules out concentration at `Q~1/s`. Global regularity is not a substitute for moving-scale anti-concentration. Only after this stability gate is crossed does the scalar source balance become the relevant arithmetic object.
