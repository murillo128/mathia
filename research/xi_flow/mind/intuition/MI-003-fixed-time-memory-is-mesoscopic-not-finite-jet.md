# MI-003 — Fixed-time Xi memory is mesoscopic; translated source counting turns borderline flux control into strong lattice rigidity

**Evidence level:** supported through XF-037; finite-range null modes, translated counting, flux inversion, and variation-collapse statements are exact in their stated regimes

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. Finite-range translation-invariant scale-invariant shape bulk has exact affine log-gap null modes, but the source-side picture is now sharper than simple nested-span rigidity: the full translated Xi counting law destroys macroscopic folded realizations already at the borderline inverse-buffer flux scale.

Conditional on `M V_M=O(1)`, the source does not merely make geometric ramps flat. It forces the whole super-mesoscopic gap block to be uniformly lattice-like and collapses the total logarithmic gap variation. The missing theorem has therefore moved upstream to the **dynamical derivation of that borderline flux bound, with collision-safe taper sign**.

## Strongest justified principle

XF-006--XF-031 establish the mesoscopic carrier, collision-safe normalized discriminants, positive overlap, exact nonlinear taper product rule, and the two-conductance bulk-alignment formulation. XF-032--XF-033 then identify the exact universal null family: every finite-range sliding scale-invariant local shape assembly has zero interior first variation on an affine log-gap profile, equivalently a geometric gap ramp.

XF-034 shows that an exact or uniformly near-geometric ramp persisting across a super-mesoscopic Xi buffer must flatten by nested zero-counting spans. XF-035 quantifies what is available if the source is compressed to only those two spans: `M V_M=o(1)` closes the stability bridge, while a fixed-amplitude tent with `V_M=Theta(1/M)` is a sharp static control for that reduced data package.

XF-036 restores the full source information. Rodgers--Tao counting applies uniformly to every translated fixed-fraction subwindow inside the buffer. Combined with the borderline condition

`M V_M=O(1)`,

this makes the log-gap profile equi-Lipschitz on the macroscopic index scale and forces

`max_k |log(g_k/h_T)| = o(1)`.

The XF-035 tent fails these translated averages by an order-one amount and is therefore not source-admissible.

XF-037 extracts the first-order consequence. Under the same hypotheses,

`sum_k |log(g_{k+1}/g_k)| = o(1)`,

so order-`1/M` nonlattice contrasts can occupy only a vanishing fraction of the block. The triple-flux `ell^1` mass and reciprocal-gap total variation also vanish. What can still survive statically is a sparse sub-super-mesoscopic microfold with pointwise contrast `Theta(1/M)`.

## What remains possible

A positive continuation should derive `V_M=O(1/M)`, or a comparable compactness estimate, from the exact interaction between the local `L_lambda` shape force and the long-range `L_w` dynamics while retaining XF-028 collision-positive coverage. Once that source resource is available, the remaining task is to control the signed tapered derivative rather than to prove another static near-kernel theorem.

A decisive negative must now be dynamically source-compatible. It should exhibit sparse/sub-super-mesoscopic misalignment that respects translated counting and the relevant zero-motion law, or show that the dynamics cannot supply the borderline flux-variation budget. Macroscopic tents and positive-density near-lattice waves no longer qualify.

## Status / novelty

Patch-test null modes, bounded-variation interpolation, and local-average rigidity are classical ingredients. The persisted synthesis is the frontier shift: **translated Xi counting converts a borderline `1/M` flux-variation resource into uniform and total-variation lattice rigidity; the unresolved mechanism is whether Xi dynamics supplies that resource with the required sign through collisions**.

## Falsification criterion

Construct a source-valid super-mesoscopic Xi block satisfying translated counting and `M V_M=O(1)` but violating uniform gap flattening or vanishing total log-gap variation, contradicting XF-036/037. A dynamically derived `V_M=O(1/M)` estimate would close the current source-coercivity gate rather than falsify it.

## Lean-formalizable core

- Finite-range geometric-ramp null classification.
- Inverse-Lipschitz triple-flux coordinate.
- Translated super-mesoscopic span law.
- Equi-Lipschitz plus translated-average uniform flattening.
- Block interpolation from flux variation to vanishing total log-gap variation.
