# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Match the `r=O(s)` compressed bulk to the outer stretched profile and derive the scalar endpoint cancellation

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`.

PL-297--PL-308 remove the fixed-order state-side gates: generic spectral stability does not preserve the needed boundary geometry, but for every fixed `s>0` the actual completed-Weil equation admits a finite transmission bootstrap and an exact weak Pohozaev/virial stress identity.

PL-309 shows why ordinary bulk compactness cannot reach the singular small-order trace. The stretched coordinate `r=-s log((1-x)/2)` places the renormalized boundary layer at physical distances `exp(-Theta(1/s))`, so a source vanishing in ordinary bulk norm can still leave an order-one normalized trace.

PL-310 determines the principal outer stretched geometry. The Green measures converge at fixed `r>0` to the Volterra-plus-diagonal operator

`(TF)(r)=e^(-2r)F(r)+e^(-r) integral_0^r e^(-q)F(q)dq`,

whose nonzero fixed cone is exactly `F(r)=C/sqrt(e^(2r)-1)`. The shape is universal under bounded matched lower-order perturbations, so the principal outer degree of freedom is the amplitude `C`.

PL-311 identifies a necessary endpoint compatibility for regular outer perturbations: if `(I-T)f=h` with endpoint-integrable `f` and continuous `h`, then `h(0)=0`. PL-312 completes that limiting range problem in the regular gauge. On `C([0,R])`, the range of `I-T` is exactly the continuous functions with `h(0)=0` and finite `lim_(r->0)h(r)/r`; for `C^1` forcing, **the single scalar condition `h(0)=0` is necessary and sufficient**. The preimage is unique and given by the explicit right inverse

`Rh = h/(1-e^(-2r)) + e^(-r)/sqrt(1-e^(-2r)) integral_0^r e^(-q)h(q)/(1-e^(-2q))^(3/2)dq`.

The only homogeneous degree of freedom outside that continuous gauge is exactly the singular profile `C/sqrt(e^(2r)-1)`. Hence no hidden family of smooth Fredholm conditions remains in the limiting outer equation. Once the constant endpoint mismatch is cancelled, every `C^1` remainder has a unique regular outer correction.

The missing information is now localized even more sharply. Under `x_s(r)=1-2e^(-r/s)`, every fixed physical bulk point lies in the shrinking `r=O(s)` corner. A legitimate finite-`s` matching theorem must produce the **one scalar endpoint cancellation** required by the outer range and at the same time select the coefficient of the singular homogeneous profile. The outer Volterra equation itself has no further regular compatibility condition to discover.

The live theorem is therefore a uniform corner-to-outer expansion or equivalent weak/virial matching law that identifies the total first-order endpoint forcing and the amplitude `C`. More regular inversion of `I-T` is no longer a research direction.

## Prove a rational-prime-specific sign or first-crossing law for the matched amplitude/stress

The Pohozaev identity, universal stretched profile and exact regular right inverse do not themselves provide the missing arithmetic sign. The matching theorem must first show how the actual completed-Weil source makes the endpoint cancellation and selects `C` through the compressed bulk/corner interface. Only then can one ask whether rational-prime structure forces the sign or first crossing required by the RH route.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep fixed-order admissibility, outer shape, regular range, corner matching, singular amplitude and arithmetic sign separate

PL-308 closes fixed-`s` admissibility. PL-309 identifies the exponentially thin layer. PL-310 classifies the universal outer fixed profile. PL-311 identifies the endpoint obstruction, and PL-312 proves that for `C^1` forcing this obstruction is the **only** regular outer one. The singular homogeneous profile remains the amplitude mode excluded by the continuous correction gauge.

The remaining analytic job is therefore not to rederive the universal profile or search for another smooth outer solvability condition. It is to prove the finite-`s` corner-to-outer matching law that supplies `h_tot(0)=0` and fixes the singular amplitude. The later rational-prime sign theorem is a separate arithmetic gate.