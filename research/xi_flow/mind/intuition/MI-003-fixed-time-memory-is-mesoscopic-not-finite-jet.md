# MI-003 — Fixed-time Xi memory is mesoscopic; static source rigidity stops before microscopic flux control

**Evidence level:** supported through XF-040; translated counting, cross-ratio rigidity, static countermodels, and the exact periodic damping control are exact in their stated regimes

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. Translated Xi counting can make a super-mesoscopic block extremely lattice-like once the borderline inverse-buffer flux budget `M V_M=O(1)` is assumed, and that rigidity propagates to the whole long-range cross-ratio network.

The converse is false. Uniform gap flattening, vanishing total log-gap variation, translated span control, and asymptotic Cauchy conductances still allow microscopic alternating corrugations with `M V_M->infinity`. Yet the simplest exact dynamic realization of that corrugation is rapidly damped on the microscopic heat clock. The missing theorem is therefore specifically about **localized dynamical production, transport, and damping of flux variation**, not another static near-lattice estimate.

## Strongest justified principle

XF-006--XF-031 establish the mesoscopic carrier, collision-safe normalized discriminants, positive overlap, exact nonlinear taper product rule, and the two-conductance bulk-alignment formulation. XF-032--XF-033 identify the universal finite-range null family: affine log-gap profiles, equivalently geometric gap ramps.

XF-034--XF-037 add the source gate. Under `M V_M=O(1)`, full translated Xi counting on the super-mesoscopic buffer forces uniform gap flattening and then vanishing total logarithmic gap variation. Macroscopic tents and positive-density order-`1/M` waves are no longer source-admissible; only sparse or microscopically organized residuals can remain.

XF-038 shows that this source rigidity reaches the long-range operator. If the total log-gap variation `D_M=o(1)`, every internal cross-ratio conductance satisfies `r^2 w_ik=1+o(1)` uniformly even for separations of order `M`, and on memory-scale sub-buffers the full quadratic form is asymptotic to the lattice Cauchy form. Conditional on the flux budget, deformation of the long-range conductance network is therefore not a leading-order source of misalignment.

XF-039 proves that none of these downstream conclusions recovers the hypothesis. An explicit alternating microcorrugation can satisfy translated fixed-fraction span laws with tiny error, have `D_M=o(1)`, and already be uniformly Cauchy-rigid while `V_M->0` but `M V_M->infinity`. The missing resource is genuinely microscopic `ell^1` variation of the triple flux.

XF-040 then stress-tests that static obstruction dynamically. The exact two-gap-periodic backward-heat family `cos(delta)-exp(omega^2 t)cos(omega z)` realizes the alternating pattern and has an explicit nonlinear damping law. At Xi mean spacing its small-amplitude decay rate is of order `log^2 T`; the XF-039 amplitude reaches the `M V_M=O(1)` threshold in vanishing heat time. Thus the alternating microcorrugation is not a persistent matched-control obstruction when promoted to a global periodic heat-flow solution.

## What remains possible

A positive continuation should derive a **localized** flux-variation estimate from the exact Xi zero dynamics, showing that high-frequency microscopic variation cannot be replenished fast enough by the exterior field, boundaries, or slower modulation to violate the inverse-buffer budget on the active window. The periodic damping calculation gives the correct sign and clock for one pure mode but not the required finite-window theorem.

A decisive negative must now exploit what the global periodic control omits: finite-window/exterior forcing, modulation, boundary transport, or a slower collective mode that remains source-compatible under translated counting and survives long enough to affect the tapered derivative. Static alternating blocks alone no longer qualify.

## Status / novelty

Patch-test null modes, bounded-variation interpolation, Cauchy kernels, periodic trigonometric heat solutions, and high-frequency damping are classical ingredients. The persisted synthesis is the frontier shift: **source counting controls macroscopic shape, cross-ratio geometry then classicalizes, static microcorrugation exposes the missing flux norm, and exact dynamics show that the simplest such corrugation is rapidly damped**.

## Falsification criterion

Construct a source-valid block satisfying translated counting and `D_M=o(1)` for which XF-038 Cauchy-form convergence fails, contradicting its hypotheses; or an exact two-gap-periodic control whose alternating amplitude does not satisfy the XF-040 damping law. A finite-window dynamically forced microcorrugation with persistent `M V_M>>1` would evade the periodic control and provide the relevant negative mechanism.

## Lean-formalizable core

- Finite-range geometric-ramp null classification.
- Translated-counting rigidity under `M V_M=O(1)`.
- Uniform cross-ratio-to-Cauchy comparison from `D_M`.
- Alternating static microcorrugation counterexample to the converse.
- Exact two-gap periodic damping law and flux-amplitude relation.
