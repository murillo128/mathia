# MI-003 — Fixed heat-time memory is mesoscopic; finite local jets and bounded neighborhoods are universal

**Evidence level:** supported; finite-jet obstruction is proved under the simple double-collision hypothesis, and the mesoscopic scale is exact for the linearized lattice model

## Core intuition

High Xi zeros have a shrinking microscopic time unit. Information confined to finitely many collision derivatives or a bounded number of neighboring normalized gaps is therefore too local to remember an order-one amount of backward heat time. The first scale not eliminated by the current matched controls is **mesoscopic and grows with height**.

## Strongest justified principle

XF-006 proves that every fixed finite collision jet at a hypothetical simple double-zero threshold can be approximated arbitrarily well by finite real-rooted polynomial heat flows with an independently movable transition time. No robust continuous selector based on finitely many local collision derivatives can therefore be Xi-specific.

XF-007 gives the spatial counterpart near arithmetic-lattice equilibrium. Linearizing the exact zero ODE yields the Fourier symbol

`lambda_h(theta) = -theta(2 pi-theta)/h^2`.

At height `T`, where the mean spacing is `h_T ~ 4 pi/log T`, a perturbation involving `N` gaps relaxes on time scale `~4N/log^2 T`. Bounded-radius information loses memory on `O(log^-2 T)` time, while order-one heat-time memory requires `N ~ log^2 T` gaps, a physical zero window of length `~ log T`.

Thus increasing local derivative order and increasing a fixed local spatial radius are the same kind of failed escape: both remain below the information scale forced by the heat dynamics.

## Evidence synthesis and boundaries

The `log T` window is not asserted as a theorem for the full nonlinear Xi flow. XF-007 is perturbative around the arithmetic-lattice equilibrium, and rare large defects, higher-multiplicity collisions, or nonperturbative global structures can behave differently. Likewise XF-006 does not approximate a whole heat-time trajectory, only every fixed local jet at the collision slice.

The durable boundary is therefore informational rather than predictive: any fixed-time upper-bound mechanism must use data whose support/complexity grows with height or a genuinely nonlocal quantity not controlled by local Laguerre--Polya polynomial approximants and lattice relaxation.

## Status / novelty

Laguerre--Polya approximation, polynomial real-root preservation, the zero ODE, and Fourier diagonalization are classical or literature-backed. The synthesis is the common scale obstruction: finite jets and bounded neighborhoods are universal controls, while fixed-time memory first becomes plausible only at a mesoscopic growing window.

## Falsification criterion

Produce a source-specific continuous selector depending on a fixed finite collision jet that cannot be matched by the XF-006 polynomial controls, or show in the linearized lattice model that a bounded-radius spacing perturbation retains order-one amplitude over a fixed heat-time interval as `T -> infinity`.

## Lean-formalizable core

- Finite-jet inheritance from finitely many spatial derivatives under the heat equation.
- Linearized lattice convolution operator and Fourier symbol.
- Relaxation-time scaling from `h_T ~ 4 pi/log T`.
