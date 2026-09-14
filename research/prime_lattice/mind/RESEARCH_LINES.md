# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove Pohozaev-admissible branch regularity and source-structured derivative convergence

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-297--PL-304 isolate the state-side obstruction: renormalized boundary stress does not control the half-Sobolev moment, generic spectral stability does not preserve BV, and the exact logarithmic resolvent is not an ordinary `L^p`- or measure-to-BV smoother. PL-305 proves that once a fixed state is in `C_0 cap BV_0`, the lower-order prime-shift and completion terms are already `C^1` through aperture activations.

PL-306 showed conditionally that a mixed moving-domain Hadamard law would identify the scalar endpoint-square stress. PL-307 removes that theorem as an independent obligation. Ros-Oton--Serra's fixed-domain fractional Pohozaev identity, combined with the exact dilation generator of the lower-order Weil form, gives directly

`Gamma(1+s)^2/(2s) (|tau_+|^2+|tau_-|^2) = E_s(w) - a^(2s+1) partial_a b_a(w)`

for every regularized eigenstate satisfying the required Pohozaev regularity and virial pairing. If the lower derivative passes to the zero-order limit, then

`lim (|tau_+|^2+|tau_-|^2)/(2s) = 1-a partial_a b_a(w_0)`,

and zero-order Feynman--Hellmann identifies this with `-a lambda_0'(a)`.

The live analytic work is therefore narrower: establish **Pohozaev-admissibility and the lower-order dilation pairing for the actual completed-Weil branch**, then derive source-structured `C_0+BV`/derivative-measure compactness strong enough to pass PL-305's derivative through `s->0`. A full mixed fractional Hadamard theorem is unnecessary for the scalar squared stress.

## Prove a rational-prime-specific sign or first-crossing law for the resulting derivative

The Pohozaev/virial identity does not supply the missing sign. Generic positivity, spectral gaps, BV transport and ambient forcing norms do not force the rational-prime branch to move in the required direction.

The sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, an absolute-value defect identity, or another order structure unavailable to matched locally finite shift systems. Analytic existence of the stress/derivative and arithmetic control of its sign remain distinct.

## Keep state coercivity, Pohozaev regularity, scalar squared stress and signed boundary information separate

PL-307 identifies the squared stress using an existing fixed-domain identity once its hypotheses are proved for the branch. It does not recover a signed trace, pointwise logarithmic boundary coefficient or intrinsic boundary measure. A moving-domain Hadamard theory may still matter for those stronger objects, but it is no longer a load-bearing gate for the scalar aperture stress.
