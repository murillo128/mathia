# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the mixed Hadamard identity and source-structured BV derivative convergence

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-297--PL-304 isolate the state-side obstruction: renormalized boundary stress does not control the half-Sobolev moment, generic spectral stability does not preserve BV, and the exact logarithmic resolvent is not an ordinary `L^p`- or measure-to-BV smoother. PL-305 proves that once a fixed state is in `C_0 cap BV_0`, the lower-order prime-shift and completion terms are already `C^1` through aperture activations.

PL-306 removes a previously separate target. If the actual fractionalized completed-Weil branch admits both fixed-domain Feynman--Hellmann and the moving-domain fractional Hadamard formula, comparison forces the renormalized squared endpoint stress from the same lower-order virial derivative. With derivative convergence,

`lim (|tau_+|^2+|tau_-|^2)/(2s) = 1-a partial_a b_a(w_0) = -a lambda_0'(a)`.

Therefore the live analytic work has **two** load-bearing gates: establish the mixed fractional/completed-Weil shape identity on the actual regularization, and derive source-structured `C_0+BV`/derivative-measure compactness strong enough to pass PL-305's derivative through `s->0`. Separate trace-square compactness is no longer required for the scalar Hadamard stress.

## Prove a rational-prime-specific sign or first-crossing law for the resulting derivative

The virial identity does not supply the missing sign. Generic positivity, spectral gaps, BV transport and ambient forcing norms do not force the rational-prime branch to move in the required direction.

The sign theorem must come from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, an absolute-value defect identity, or another order structure unavailable to matched locally finite shift systems. Analytic existence of `lambda_0'(a)` and arithmetic control of its sign remain distinct.

## Keep state coercivity, shape calculus, squared stress and signed boundary information separate

PL-306 identifies the squared stress once the first two analytic gates are met, but it does not recover a signed trace, pointwise logarithmic boundary coefficient or new arithmetic observable. Future work should not spend effort proving more endpoint compactness than the eigenvalue shape law needs unless that extra signed boundary information is itself part of the proposed arithmetic mechanism.
