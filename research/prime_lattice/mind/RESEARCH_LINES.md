# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove source-structured small-order convergence of the weak virial stress

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-297--PL-304 isolate the state-side obstruction: renormalized boundary stress does not control the half-Sobolev moment, generic spectral stability does not preserve BV, and the exact logarithmic resolvent is not an ordinary `L^p`- or measure-to-BV smoother. PL-305 proves that once a fixed state is in `C_0 cap BV_0`, the lower-order prime-shift and completion terms are already `C^1` through aperture activations.

PL-306 showed conditionally that a mixed moving-domain Hadamard law would identify the scalar endpoint-square stress. PL-307 removed that theorem as an independent obligation by deriving the stress from fixed-domain Pohozaev plus the lower-order dilation generator.

PL-308 now removes fixed-order Pohozaev regularity as an independent obligation as well. For every fixed `s>0`, the actual completed-Weil right-hand side preserves enough supported Sobolev regularity for a finite Grubb `mu`-transmission bootstrap. The branch therefore reaches transmission index `sigma>s+1/2`, and the low-regularity radial Pohozaev identity yields the exact weak stress law

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w)+a^(2s)[b_a(w)+V_a(w)]`.

The translated fractional boundary fronts that obstruct naive high-Hölder hypotheses are harmless at fixed order because the weak virial `V_a(w)=2 Re<B_aw,xw'>` is defined by transmission-space duality.

The analytic burden has therefore moved entirely to the singular limit. Prove **uniform source-structured convergence of `V_a(w_(s,a))` as `s->0`**, or enough `C_0+BV`/derivative-measure compactness to identify it with the explicit PL-305 aperture derivative and pass that derivative to zero order. The number of bootstrap steps and the transmission constants are not currently uniform as `s` decreases.

## Prove a rational-prime-specific sign or first-crossing law for the resulting derivative

The Pohozaev/virial identity does not supply the missing sign. Generic positivity, spectral gaps, transmission regularity, BV transport and ambient forcing norms do not force the rational-prime branch to move in the required direction.

The sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, an absolute-value defect identity, or another order structure unavailable to matched locally finite shift systems. Analytic existence/convergence of the stress and arithmetic control of its sign remain distinct.

## Keep fixed-order admissibility, small-order compactness, scalar squared stress and signed boundary information separate

PL-308 closes fixed-`s` admissibility but explicitly leaves `s->0` uniformity open. It does not recover a signed trace, pointwise logarithmic boundary coefficient or intrinsic boundary measure. A moving-domain Hadamard theory may still matter for those stronger objects, but neither it nor high-Hölder regularity is load-bearing for the finite-`s` scalar stress.