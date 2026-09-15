# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the actual completed-Weil corner decomposition with source-specific moving-tail control

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`, `MI-019-moving-green-atoms-require-tail-anti-concentration-beyond-weighted-l1`, `MI-020-half-derivative-is-the-generic-moving-diagonal-sobolev-threshold`.

PL-297--PL-312 close the fixed-order state-side and limiting outer gates. PL-313 identifies the compressed-corner communication channel: for compact physical mismatch the finite-`s` Green transfer reaches the unique obstructed regular outer direction through the scalar endpoint moment `M_±`.

PL-314 sharpens the hypothesis needed to extend that transfer to a genuine endpoint tail. Weighted `L^1(dQ)` control alone is insufficient. The stretched Green measure has a moving diagonal atom at `q=r`, which samples physical logarithmic distance `Q=r/s`; one fixed smooth `L^1` mismatch can place sparse bumps there with arbitrarily small total mass yet produce order-one normalized transfer along a sequence `s_n->0`.

PL-315 rules out broad regularity shortcuts: the counterexample can be `C^infty`, lie in every `W^{k,1}(dQ)`, have arbitrarily small physical `W^{1,1}` norm, belong to every subcritical Sobolev space `H^alpha`, `alpha<1/2`, and satisfy every all-log Fourier moment condition used by the current bootstrap. It can even obey `m(Q)=O(1/Q)` while `limsup Qm(Q)>0`.

PL-316 closes the critical endpoint shortcut. The same moving-diagonal obstruction can have zero extension in `H^{1/2}(R)` with arbitrarily small norm while the normalized Green transfer remains order one along selected scales. Critical half-derivative regularity therefore does not force `Qm(Q)->0`.

PL-317 identifies the exact generic Sobolev success side. If the zero extension lies in any `H^{1/2+eta}(R)`, `eta>0`, fractional Morrey regularity gives a zero boundary trace and hence

`|m(Q)| <= C_beta exp(-beta Q)`

for every `0<beta<min(eta,1/2)`. Thus `Qm(Q)->0`, the moving sample `m(r/s)/s->0`, and the PL-314 rank-one limit follows. Within the zero-extension Sobolev strategy, `1/2` is therefore the sharp boundary between generic failure and automatic success.

The remaining theorem is now source-specific and concrete: derive **any positive supercritical zero-extension gain** from the actual completed-Weil eigen-equation, or prove a weaker structured substitute such as `m(Q)=o(1/Q)`, monotone/one-sided tail behavior, an asymptotic expansion, or a direct estimate of `m(r/s)/s`. Broad unnamed regularity below or at the half derivative has been exhausted.

Only after that moving-scale stability gate is crossed should the scalar `M_±` balance be used as the arithmetic endpoint.

## Prove a rational-prime-specific sign or first-crossing law only after stable matching

The Green-kernel transfer, universal stretched profile and exact regular inverse are geometric. The scalar endpoint moment can have either sign. Rational-prime specificity must enter through the actual mismatch/source relation or selected singular amplitude after the finite-`s` matching theorem **and its source-specific moving-tail control** are proved.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep outer geometry, global regularity, moving sampling, boundary trace and arithmetic sign separate

PL-313 closes the geometric rank-one channel for compact mismatch. PL-314 shows why a weak integrated tail norm cannot automatically pass through a singular moving observation. PL-315--PL-316 show that smoothness and every zero-extension Sobolev level up to the critical half derivative still permit sparse saturation. PL-317 shows that an arbitrarily small positive gain beyond the half derivative changes the mechanism qualitatively by forcing a zero boundary trace and exponential decay in logarithmic endpoint coordinates.

Future work must therefore state which **source equation property** crosses this boundary or supplies a different anti-concentration law at `Q~1/s`. Generic critical regularity is not a substitute for moving-scale control, while supercritical regularity is already enough. Only after this stability gate is crossed does the scalar source balance become the relevant arithmetic object.