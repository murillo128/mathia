# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove completed-Weil compactness on the universal stretched Green profile and identify its amplitude

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-297--PL-304 isolate the state-side obstruction: renormalized boundary stress does not control the half-Sobolev moment, generic spectral stability does not preserve BV, and the exact logarithmic resolvent is not an ordinary `L^p`- or measure-to-BV smoother. PL-305 proves that once a fixed state is in `C_0 cap BV_0`, the lower-order prime-shift and completion terms are already `C^1` through aperture activations.

PL-306--PL-308 remove fixed-order shape calculus and regularity as independent gates. For every fixed `s>0`, the actual completed-Weil right-hand side admits a finite Grubb `mu`-transmission bootstrap, and the low-regularity Pohozaev identity yields the exact weak stress law

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w)+a^(2s)[b_a(w)+V_a(w)]`.

PL-309 shows why ordinary bulk compactness cannot close the singular limit. The explicit one-dimensional fractional Green trace has stretched coordinate `r=-s log((1-x)/2)`, so fixed `r=O(1)` samples physical distances `exp(-Theta(1/s))` from the boundary. Smooth forcings with `||f_s||_infty=O(sqrt(s))->0` can nevertheless prescribe a finite limit of `tau_(s,+)/sqrt(s)`.

PL-310 now determines the principal stretched Green geometry exactly. After pushing the interval Green measure into the coordinate `x_s(r)=1-2e^(-r/s)`, one has for fixed `r`

`d mu_(s,r) => e^(-r-q) 1_(0<q<r) dq + e^(-2r) delta_r`.

The limiting operator

`(TF)(r)=e^(-2r)F(r)+e^(-r) integral_0^r e^(-q)F(q)dq`

has a one-dimensional nonzero fixed cone,

`F(r)=C/sqrt(e^(2r)-1)`.

Its `r->0` face is the logarithmic-Laplacian `r^(-1/2)` boundary scale and its `r->infinity` face is the fixed-order fractional `e^(-r)` scale. This profile is universal: it comes from the fractional principal operator and survives bounded matched lower-order perturbations. It is therefore not rational-prime evidence by itself.

The analytic endpoint is now narrower than “control an arbitrary boundary layer.” For the actual completed-Weil branch, prove enough compactness/uniform integrability of `U_s(r)=s^(-1/2)w_s(x_s(r))` to pass through the Green representation, or recover the same scalar through a uniformly convergent weak virial. Under the natural bounded-source hypothesis, every nonzero subsequential stretched-profile limit is already forced to the `PL-310` shape. The remaining data are its amplitude `C` and the justification that the actual branch reaches the limiting operator.

## Prove a rational-prime-specific sign or first-crossing law for the resulting amplitude/stress

The Pohozaev/virial identity and the universal Green profile do not supply the missing sign. Generic positivity, spectral gaps, transmission regularity, BV transport, ambient forcing norms and the principal stretched shape are all compatible with matched lower-order perturbations.

The sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, an absolute-value defect identity, a source-sensitive amplitude matching condition, or another order structure unavailable to matched locally finite shift systems. Analytic existence of the limiting amplitude/stress and arithmetic control of its sign remain distinct.

## Keep fixed-order admissibility, bulk convergence, stretched-profile compactness, universal shape, amplitude and signed arithmetic information separate

PL-308 closes fixed-`s` admissibility. PL-309 identifies the exponential layer and falsifies passage from ordinary bulk convergence to the renormalized trace. PL-310 then shows that once one can pass to the stretched limit, the principal Green operator leaves only one profile degree of freedom. A moving-domain Hadamard theory may still matter for stronger observables, but neither it nor generic bulk regularity is load-bearing for this endpoint.

The live zero-order theorem must therefore control the actual branch strongly enough to reach the universal fixed profile or the equivalent scalar virial limit, and then identify the **source-specific amplitude/sign**. Re-deriving the profile from generic fractional geometry cannot advance the arithmetic endpoint.