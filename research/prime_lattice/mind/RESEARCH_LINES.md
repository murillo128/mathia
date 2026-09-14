# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Match the `r=O(s)` compressed bulk to the outer stretched profile and derive the amplitude solvability condition

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`, `MI-018-stretched-volterra-amplitude-selection-is-an-endpoint-matching-problem`.

PL-297--PL-308 remove the fixed-order state-side gates: generic spectral stability does not preserve the needed boundary geometry, but for every fixed `s>0` the actual completed-Weil equation admits a finite transmission bootstrap and an exact weak Pohozaev/virial stress identity.

PL-309 shows why ordinary bulk compactness cannot reach the singular small-order trace. The stretched coordinate `r=-s log((1-x)/2)` places the renormalized boundary layer at physical distances `exp(-Theta(1/s))`, so a source vanishing in ordinary bulk norm can still leave an order-one normalized trace.

PL-310 determines the principal outer stretched geometry. The Green measures converge at fixed `r>0` to the Volterra-plus-diagonal operator

`(TF)(r)=e^(-2r)F(r)+e^(-r) integral_0^r e^(-q)F(q)dq`,

whose nonzero fixed cone is exactly

`F(r)=C/sqrt(e^(2r)-1)`.

The shape is universal under bounded matched lower-order perturbations, so the only principal outer degree of freedom is the amplitude `C`.

PL-311 shows that this amplitude cannot generally be selected by a naive regular perturbation on the same fixed-`r` scale. If `f` is endpoint-integrable, `(I-T)f=h`, and `h` is continuous at `0`, then necessarily `h(0)=0`; in particular `e^(-r)` is outside the endpoint-integrable range of `I-T`. A lower-order source with nonzero boundary limit produces precisely such an `e^(-r)` forcing after application of `T`, unless another finite-`s` term cancels it.

The missing information is geometrically localized. Under `x_s(r)=1-2e^(-r/s)`, every fixed physical bulk point `x in (-1,1)` corresponds to `r=s[-log((1-x)/2)]=O(s)`. Thus the entire macroscopic bulk that the fixed-`r` outer limit forgets is compressed into an `r=O(s)` corner. The live theorem is now a **uniform finite-`s` overlap/matching result** between this corner and the fixed-`r` outer profile, strong enough to identify the endpoint solvability condition that selects `C` or cancels the forbidden endpoint forcing.

This is sharper than generic compactness. One needs either a quantitative expansion of `T_s-T` across the overlap or an equivalent weak/virial matching law that preserves the source-sensitive boundary functional. The outer profile alone cannot determine the amplitude, and a bounded boundary value of the source is not enough without the corner compensation.

## Prove a rational-prime-specific sign or first-crossing law for the matched amplitude/stress

The Pohozaev identity, universal stretched profile and endpoint range obstruction do not themselves provide the missing arithmetic sign. The matching theorem must first show how the actual completed-Weil source selects `C` through the compressed bulk/corner interface. Only then can one ask whether rational-prime structure forces the sign or first crossing required by the RH route.

A useful sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation or maximum principle, an absolute-value defect identity, a source-sensitive matching condition, or another order structure unavailable to matched locally finite shift systems.

## Keep fixed-order admissibility, outer shape, endpoint range, corner matching, amplitude and arithmetic sign separate

PL-308 closes fixed-`s` admissibility. PL-309 identifies the exponentially thin layer. PL-310 classifies the universal outer fixed profile. PL-311 adds a new interface: the endpoint-integrable range of the outer defect excludes nonzero endpoint forcing, while all fixed physical bulk information lives in the shrinking `r=O(s)` corner.

The remaining analytic job is therefore not to rederive the universal profile or improve ordinary bulk convergence. It is to prove the **corner-to-outer matching/solvability law** that transfers source information into the scalar amplitude. The later rational-prime sign theorem is a separate arithmetic gate.