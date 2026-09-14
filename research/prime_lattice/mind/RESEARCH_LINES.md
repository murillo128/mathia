# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the actual completed-Weil corner decomposition and scalar matching law

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`.

PL-297--PL-308 remove the fixed-order state-side gates. PL-309 localizes the renormalized trace to an exponentially thin boundary layer. PL-310 identifies the universal outer Volterra profile `C/sqrt(e^(2r)-1)`, and PL-311--PL-312 prove that the regular outer defect has exactly one scalar solvability condition `h(0)=0` and no hidden smooth Fredholm family.

PL-313 now supplies the missing geometric transfer from the compressed physical corner to that cokernel. For compact physical mismatch `m`, the exact Green kernel gives

`(1/sqrt(s)) T_s[s^(-1/2)m(x_s(.))](r) -> e^(-r) M_+(m)`,

with

`M_+(m)=integral m(y)/(1-y) dy`

(and the reflected `M_-` at the other endpoint). Thus the `r=O(s)` physical corner reaches the first regular outer correction through **one rank-one endpoint functional**, precisely the forbidden `e^(-r)` direction. There is no codimension mismatch between the compressed physical problem and the limiting outer range.

The remaining theorem is now sharply finite-`s` and branch-specific: prove an overlap decomposition for the actual completed-Weil eigenbranch, match the singular amplitude `C` strongly enough that the residual corner mismatch is integrable in logarithmic distance, control all other `O(sqrt(s))` terms, and derive the resulting scalar `M_±` balance against the completed source. PL-313 identifies the channel; it does not establish the actual branch identity.

## Prove a rational-prime-specific sign or first-crossing law only after matching

The Green-kernel transfer, universal stretched profile and exact regular inverse are geometric. The scalar `M_±(m)` can have either sign. Rational-prime specificity must enter through the actual mismatch/source relation or the selected singular amplitude after the finite-`s` matching theorem is proved.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep outer geometry, rank-one corner transfer, actual matching and arithmetic sign separate

PL-310--PL-312 close the limiting outer shape and regular range. PL-313 closes the **geometric communication channel** from a resolved compact physical corner to the outer cokernel. What remains is not another outer inversion: it is to show that the actual eigenbranch admits the required weighted corner decomposition and to compute its scalar balance. The later arithmetic sign is a separate gate.
