# MI-004 — The composite clone now has two local routes toward wave equivalence; the remaining gate is global assembly

**Evidence level:** supported; compact relative resolvent and the local geometric/operator budgets are exact, while both global wave-comparison closures remain open

## Core intuition

The exact prime flute and the all-composite shift clone `q_n=p_n+1` are increasingly hard to distinguish in natural asymptotic operator categories. The local comparison has now split into two independent sufficient routes toward wave equivalence: a geometric route through a globally coherent weighted metric map, and an operator route through trace class after applying a stronger resolvent functional calculus. The remaining obstruction in both is global assembly, not another large Fenchel--Nielsen coordinate or undiscovered thin component.

## Strongest justified principle

PF-121--PF-125 give the baseline: a canonical marked asymptotically bilipschitz identification and compact first relative resolvent, hence equality of essential spectra. PF-112 shows that first-resolvent trace class is too strong for a nonisometric smooth metric comparison, so `S_1` at the first resolvent cannot be used as the universal wave-equivalence gate.

PF-126--PF-142 remove the previously suspected local geometric divergences. Body, cusp, split-ray, short-core, and handoff contributions are summable in the appropriate local currencies; all tail Margulis-short closed cores are classified; deep cusps can be made exactly isometric; and the reflection marking removes the constant collar phase.

PF-143--PF-145 identify the exact remaining collar-interface currency. Collapse does **not** suppress a nonconstant angular trace: any near-isometric welding pays a sharp cost comparable to the centered `L^1` angular displacement. Reflection makes the canonical angular trace odd/mean-zero but does not remove this cost. The radial/transverse graph has the analogous sharp `L^1` cost. Thus the geometric Güneysu--Thalmaier route has been reduced to estimating the actual prime/clone angular and radial trace amplitudes and summing them while welding all local maps coherently; one cannot hide them behind the shrinking core length.

PF-146 supplies a genuinely different operator route. On a fixed matched Dirichlet short collar, although the first relative resolvent is not trace class, the **squared** relative resolvent is trace class with a much smaller length-defect budget; its zero Fourier mode cancels exactly and the nonzero modes are controlled through Hilbert--Schmidt factorization. For prime/shift separator collars the resulting local trace norm is summable at the derived scale. If the corresponding global squared-resolvent difference can be placed in `S_1`, the Birman--Kato invariance principle and Kato--Rosenblum give complete wave operators for the original Laplacians.

This changes the operator-category lesson: failure of trace class for one resolvent function does not rule out scattering equivalence when a different monotone functional calculus lands in trace class.

## What remains possible

A positive geometric result would prove summability of the actual reflection-odd angular and reflection-even radial interface traces and construct one global weighted comparison. A positive operator result would globalize PF-146 across the full flute, including body/cusp/interface coupling, and prove trace class of the squared relative resolvent. Either route would establish wave equivalence and expose the next stronger-than-wave relative invariants for comparison with the all-composite clone.

A decisive negative must now obstruct both kinds of closure at the actual global level: an unavoidable nonsummable interface-shape term, or a global operator contribution preventing the squared-resolvent trace-class estimate. Coordinate width, cusp depth, constant twist, or first-resolvent `S_1` failure alone no longer suffices.

## Status / novelty

The compact-resolvent equivalence, thin-core classification, sharp local welding costs, and local squared-resolvent result are persisted exact findings with classical hyperbolic/scattering inputs. The synthesis is a narrowed comparison boundary, not a proof of global wave operators, scattering-matrix equality, resonance equality, determinant comparison, or RH.

## Falsification criterion

Produce a local collar welding with uniformly smaller cost than the sharp `L^1` trace scale of PF-143--PF-145, or show that the PF-146 local squared-resolvent estimate fails under its stated matched-collar hypotheses. A genuine advance should instead prove or refute one of the two global assemblies.

## Lean-formalizable core

- Sharp `L^1` angular/radial collar extension estimates.
- Zero-mode cancellation for the squared relative resolvent.
- Schatten ideal composition used in the local `S_1` bound.
- Abstract implication from trace-class functional-calculus difference to wave equivalence.
