# MI-003 — Fixed heat-time memory is mesoscopic, nonlocal, and encoded in a vanishing equilibrium defect

**Evidence level:** supported; finite-jet obstruction is proved under the simple double-collision hypothesis, while the mesoscopic scale and Cauchy limit are exact for the linearized lattice model

## Core intuition

High Xi zeros have a shrinking microscopic time unit. Information confined to finitely many collision derivatives or a bounded number of neighboring normalized gaps is too local to remember an order-one amount of backward heat time. On the unique scale where perturbative memory survives for fixed heat time, the dynamics is not local diffusion: it converges to a Cauchy/half-Laplacian flow with algebraic tails, while the normalized exterior-field signal driving that order-one evolution shrinks like `log^-2 T`.

The first scale not eliminated by the current matched controls is therefore **mesoscopic, growing, nonlocal, and quantitatively fine**.

## Strongest justified principle

XF-006 proves that every fixed finite collision jet at a hypothetical simple double-zero threshold can be approximated arbitrarily well by finite real-rooted polynomial heat flows with an independently movable transition time. No robust continuous selector based on finitely many local collision derivatives can therefore be Xi-specific.

XF-007 gives the spatial counterpart near arithmetic-lattice equilibrium. Linearizing the exact zero ODE yields

`lambda_h(theta) = -theta(2 pi-theta)/h^2`.

At height `T`, where `h_T ~ 4 pi/log T`, order-one heat-time memory requires `N ~ h_T^-2 ~ log^2 T` gaps, occupying physical zero-coordinate length `~log T`. Bounded-radius information relaxes on the vanishing `O(log^-2 T)` clock.

XF-008 identifies the full fixed-time hydrodynamic limit on the mesoscopic coordinate `X=h^2 j`. The exact symbol becomes

`lambda_h(kappa) = -2 pi |kappa| + h^2 kappa^2`,

so smooth perturbations converge to `partial_t U = -2 pi |D_X| U`. The propagator is the Cauchy kernel and has only algebraic tail mass `~4t/A` outside `|X|<=A`; exponential-locality heuristics are already false in the universal lattice linearization.

The same calculation sharpens the information scale. Since `R-2=-(h^2/2)u'`, an order-one relative gap profile can evolve by order one over fixed heat time while its instantaneous normalized exterior-field defect is only `O(h^2)=O(log^-2 T)`. A fixed-time barrier must therefore resolve a vanishing equilibrium defect coherently across `Theta(log^2 T)` gaps or control an equivalent nonlocal functional.

## Evidence synthesis and boundaries

None of the Cauchy/half-Laplacian structure is Xi-specific. It is a matched-control boundary model inherited from the universal zero ODE near arithmetic equilibrium. The result is perturbative and does not classify rare large defects, higher-multiplicity events, nonlinear collision cascades, or globally non-equilibrium zero configurations.

The live arithmetic content must enter through a source-specific constraint on the mesoscopic field or through a genuinely nonperturbative observable. A useful upstream statistic needs the same scale and precision as the dynamics: roughly `log^2 T` gaps over physical length `log T`, with enough quantitative control to see a `log^-2 T` equilibrium defect and enough nonlocality to handle Cauchy tails.

## Status / novelty

Laguerre--Pólya approximation, polynomial real-root preservation, the zero ODE, Fourier diagonalization, and fractional/Cauchy diffusion are classical or literature-backed. The synthesis is the Xi normalization bridge: finite jets and bounded neighborhoods are universal controls, while the first fixed-time perturbative carrier is a mesoscopic half-Laplacian field whose dynamical signal is simultaneously nonlocal and vanishingly small.

## Falsification criterion

Produce a source-specific continuous selector depending on a fixed finite collision jet that cannot be matched by XF-006 controls; show that the exact lattice symbol does not converge to the stated Cauchy generator on `X=h^2j`; or exhibit a bounded/local exponentially decaying closure that captures the linearized fixed-time propagator uniformly as `h->0`. A positive Xi mechanism would instead derive a source-specific coercive bound on the required mesoscopic nonlocal field.

## Lean-formalizable core

- Finite-jet inheritance from finitely many spatial derivatives under the heat equation.
- Linearized lattice convolution operator and Fourier symbol.
- Mesoscopic rescaling `X=h^2j` and half-Laplacian symbol limit.
- Cauchy-kernel tail estimate.
- Relation `R-2=-(h^2/2)u'` and `log^-2 T` signal scale.
