# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove source-structured small-order convergence on the stretched boundary scale

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-297--PL-304 isolate the state-side obstruction: renormalized boundary stress does not control the half-Sobolev moment, generic spectral stability does not preserve BV, and the exact logarithmic resolvent is not an ordinary `L^p`- or measure-to-BV smoother. PL-305 proves that once a fixed state is in `C_0 cap BV_0`, the lower-order prime-shift and completion terms are already `C^1` through aperture activations.

PL-306--PL-308 remove fixed-order shape calculus and regularity as independent gates. For every fixed `s>0`, the actual completed-Weil right-hand side admits a finite Grubb `mu`-transmission bootstrap, and the low-regularity Pohozaev identity yields the exact weak stress law

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w)+a^(2s)[b_a(w)+V_a(w)]`.

PL-309 now shows why ordinary bulk compactness cannot close the singular limit. The explicit one-dimensional fractional Green trace has stretched coordinate

`r=-s log((1-x)/2)`,

so fixed `r=O(1)` samples physical distances `exp(-Theta(1/s))` from the boundary. Smooth forcings with `||f_s||_infty=O(sqrt(s))->0` can nevertheless produce any prescribed finite limit of `tau_(s,+)/sqrt(s)`. Thus `C_0`, `L^infty`, norm-resolvent or generic bulk forcing convergence cannot determine the renormalized trace/stress.

This does not refute the actual completed-Weil eigenbranch; it identifies the scale on which its extra source structure must act. The analytic burden is now to prove **uniform source-structured control on the exponential boundary layer**, or uniform convergence of the weak virial / derivative-measure mechanism strong enough to identify the same scalar stress without recovering the trace pointwise. A generic bulk `C_0+BV` statement is useful only if it controls the relevant stretched boundary profile or the virial pairing uniformly as `s->0`.

## Prove a rational-prime-specific sign or first-crossing law for the resulting derivative

The Pohozaev/virial identity does not supply the missing sign. Generic positivity, spectral gaps, transmission regularity, BV transport, ambient forcing norms and the Green trace representation do not force the rational-prime branch to move in the required direction.

The sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, an absolute-value defect identity, or another order structure unavailable to matched locally finite shift systems. Analytic existence/convergence of the stress and arithmetic control of its sign remain distinct.

## Keep fixed-order admissibility, bulk convergence, stretched-boundary control, scalar squared stress and signed boundary information separate

PL-308 closes fixed-`s` admissibility. PL-309 shows that the singular trace is concentrated on `exp(-Theta(1/s))` boundary scales and explicitly falsifies passage from ordinary bulk convergence to the renormalized trace. A moving-domain Hadamard theory may still matter for stronger boundary observables, but neither it nor high-Hölder regularity is load-bearing for the finite-`s` scalar stress. The live zero-order theorem must control the actual source on the scale consumed by the endpoint.