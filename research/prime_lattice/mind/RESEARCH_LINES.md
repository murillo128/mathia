# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the actual completed-Weil corner decomposition with source-specific moving-tail control

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`, `MI-019-moving-green-atoms-require-tail-anti-concentration-beyond-weighted-l1`, `MI-020-half-derivative-is-the-generic-moving-diagonal-sobolev-threshold`.

PL-297--PL-312 close the fixed-order state-side and limiting outer gates. PL-313 identifies the compressed-corner communication channel: for compact physical mismatch the finite-`s` Green transfer reaches the unique obstructed regular outer direction through the scalar endpoint moment `M_±`.

PL-314 isolates the moving-diagonal obstruction. The stretched Green measure has an atom at fixed `q=r`, corresponding to physical logarithmic distance `Q=r/s`, so weighted `L^1` tail control can miss sparse packets exactly where the observer samples. PL-315--PL-316 show that smoothness, all finite logarithmic moments, every subcritical Sobolev gain and even critical zero-extension `H^{1/2}` can coexist with order-one normalized transfer along selected scales.

PL-317 identifies the exact generic Sobolev success side. Any fixed zero-extension gain `H^{1/2+eta}`, `eta>0`, forces a zero boundary trace and exponential logarithmic-tail decay, hence `m(r/s)/s->0` and the PL-314 rank-one limit.

PL-318 now rules out another natural shortcut on the source side. The moving-diagonal counterexample can be realized with **bounded logarithmic zero-order forcing** under the completed endpoint operator, while keeping `m in L^1`, `m(Q)=O(1/Q)` and `limsup Qm(Q)>0`. Bounded forcing, even with arbitrarily small norm after scaling, therefore does not supply the missing anti-concentration law.

The remaining theorem is more source-specific than a generic elliptic/regularity estimate: exploit the actual completed-Weil state--source coupling to derive a positive supercritical trace gain, `m(Q)=o(1/Q)`, monotone/one-sided tail behavior, an asymptotic expansion, a cancellation identity, or a direct bound on `m(r/s)/s`. Merely knowing that the right-hand side is bounded is now exhausted together with the subcritical/critical regularity routes.

Only after that moving-scale stability gate is crossed should the scalar `M_±` balance be used as the arithmetic endpoint.

## Prove a rational-prime-specific sign or first-crossing law only after stable matching

The Green-kernel transfer, universal stretched profile and exact regular inverse are geometric. The scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual mismatch/source relation or selected singular amplitude after the finite-`s` matching theorem **and its source-specific moving-tail control** are proved.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep outer geometry, forcing size, moving sampling, boundary trace and arithmetic sign separate

PL-313 closes the geometric rank-one channel for compact mismatch. PL-314--PL-316 show that weak integrated control and generic critical regularity do not pass through a singular moving observation. PL-317 shows that any fixed supercritical zero-extension gain does. PL-318 adds that bounded zero-order forcing under the natural logarithmic endpoint operator is still on the failure side.

Future work must therefore state which **structural property of the actual source equation**, not merely which norm of its forcing, crosses the moving-sample boundary at `Q~1/s`. Generic bounded forcing and generic critical regularity are not substitutes for source-specific anti-concentration. Only after this stability gate is crossed does the scalar source balance become the relevant arithmetic object.