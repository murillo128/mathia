# MI-007 — Stable fidelity is distance from the admitted collision boundary, and repair is relative to target transport

**Evidence level:** supported by exact Hilbert, Euclidean, smooth-compact, Lipschitz, finite-channel, metric-refinement, powered-lift, and horofunction classifications

## Core intuition

Exact recoverability, stable recoverability, and distance to a repaired structural target are different claims. Stability is controlled by distance from the relevant collision set in the **specific perturbation geometry**, while a repair radius is intrinsic only after the target family is transported compatibly with the representation equivalences that the category declares harmless.

The newer safe-lift results add a sharper asymptotic layer. Even after the source and target set are fixed, the existence of a finite repair above a prescribed base point can change under arbitrarily small renorming. In finite-dimensional smooth normed spaces the complete first-order horofunction boundary sees only the convex hull; every nontrivial powered threshold is therefore a higher-order boundary phenomenon whose exponent is set by the decay of the residual distance excess and by the source norm, not by a universal Hilbert scale.

## Strongest justified principle

AF-041--AF-045 identify stable fidelity with a quantitative distance from admitted collisions in linear, smooth, and Lipschitz categories. AF-046--AF-051 show that the failure relation and discrepancy must also be specified: law equality, zero-error support fidelity, TV, KL, and quadratic costs induce genuinely different repair geometries.

AF-052--AF-054 isolate target transport. A refinement can be Blackwell reversible and isometric for the ambient discrepancy while an unrestricted refined target acquires non-descending points and moves closer. For an isometric refinement `C:X->Y`, AF-054 gives the maximal safe envelope

`E_C(S)={y in Y : d(Cx,y) >= dist(x,S) for every x}`,

and characterizes exactly which target enlargements preserve every source repair radius.

AF-055--AF-059 classify the finite-lift boundary in concrete metric categories. Singleton linear envelopes are best-coapproximation fibers; Hilbert set targets reduce to convex-roof/Delaunay geometry. For Euclidean powered products the finite-lift base set has the exact phase diagram

`B_1(S)=R^d`, `B_p(S)=conv(S)` for `1<p<=2`, and `B_p(S)=S union int(conv(S))` for `p>2`.

AF-060--AF-061 show that this transition is not intrinsic under merely topological or near-isometric equivalence. Fixed-base finite lifting can disappear under arbitrarily small norm distortion, and for an `ell^r` source the critical product exponent is exactly `r`, not universally `2`.

AF-062--AF-063 identify the mechanism behind those examples. Powered finite-lift existence is equivalent to boundedness of the weighted positive distance excess

`(d(x,m)+d(m,S))^(p-1) (d(x,S)-d(x,m))_+`.

In finite-dimensional smooth strictly convex normed spaces the first-order horofunction margin is exactly the signed distance from `m` to `conv(S)`: positive outside the hull, negative in its interior, and zero precisely on its boundary. Thus exterior failure and interior safety are first-order; only hull-boundary ties can carry higher-order target provenance, and their critical power is the decay exponent of the residual excess.

## What remains possible

The live frontier is to identify representation categories in which collision geometry, target transport, perturbation metric, asymptotic boundary, and admissible refinements are all intrinsic to the mathematical construction. On a hull boundary, a higher-order invariant can still retain information erased by the first horofunction layer, but its exponent or finiteness has to be proved invariant under the declared source geometry rather than inferred from a preferred norm.

For arithmetic applications, a discriminator should therefore pass three separate robustness tests: positive distance from the matched-control collision set; target descent through every information-preserving equivalence; and invariance of any higher-order boundary scale under the admitted metric/renorming class. A positive coordinate margin or critical exponent that changes under reversible re-encoding or near-isometric renorming is not yet an intrinsic arithmetic separation.

## Status / novelty

The functional-analytic, channel-decision, coapproximation, convex-hull, horofunction, and norm-comparison mechanisms are classical or direct. The persisted Mathia synthesis is the joint gate: **robust fidelity is relative to a collision geometry; robust repair is additionally relative to target transport; and higher-order boundary fidelity is relative to the asymptotic metric category**.

## Falsification criterion

For stability, exhibit a covered category where the stated lower modulus disagrees with distance to admitted collision. For repair, give an isometric/reversible refinement and a target enlargement outside the AF-054 safe envelope that nevertheless preserves every source repair radius. For the higher-order claim, exhibit a smooth finite-dimensional normed example where the first horofunction margin distinguishes more than the convex hull or where the AF-062 weighted-excess criterion gives the wrong powered-lift threshold.

## Lean-formalizable core

- Range-kernel transversality and closed-secant stability.
- Maximal safe target envelope under isometric refinement.
- Euclidean powered-lift phase diagram.
- Weighted-distance-excess equivalence for powered defects.
- Horofunction margin as signed convex-hull distance.
- Near-isometric renorming counterexamples and `ell^r` critical exponent.
