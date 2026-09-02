# MI-007 — Stable fidelity is distance from the admitted collision boundary, and repair is relative to target transport

**Evidence level:** supported by exact Hilbert, Euclidean, smooth-compact, Lipschitz, finite-channel, and metric-refinement classifications

## Core intuition

Exact recoverability, stable recoverability, and distance to a repaired structural target are different claims. Stability is controlled by distance from the relevant collision set in the **specific perturbation geometry**, while a repair radius is intrinsic only after the target family is transported compatibly with the representation equivalences that the category declares harmless.

The newer channel/refinement results make the second clause essential. A representation map can be statistically reversible and even exactly isometric for the ambient discrepancy while an unrestricted target on the refined presentation acquires new non-descending points and moves closer. Thus an invariant source metric does not by itself make distance to structure invariant.

## Strongest justified principle

AF-041 gives the linear-composition prototype. If `A` and `B` have closed range, exact injectivity of `BA` only requires `Ran(A)` to miss `ker(B)`, whereas stable injectivity requires uniform transversality. AF-042--AF-045 identify the same geometry through closed secants, injective immersions, operator-norm distance to pair collisions, and the Lipschitz lower modulus. In these settings the stable-fidelity modulus is literally a distance to the closure of admitted collisions.

AF-046--AF-051 show that the failure relation and discrepancy must also be specified. Law equality can have a positive total-variation margin while zero-error support fidelity has zero TV robustness; average TV, row-sup TV, KL directions, general `f`-divergences, and quadratic costs induce different repair problems. Quadratic repair is exact but changes under statistically reversible output cloning.

AF-052--AF-054 isolate the deeper target-transport issue. Uniform cloning is Blackwell reversible and TV-isometric, yet the unrestricted zero-error repair radius drops because the refined alphabet admits new support partitions that do not descend. Adding null symbols collapses the presentation-relaxed TV repair radius all the way to Bayes risk. In general, for an isometric refinement `C:X->Y`, AF-054 gives the unique maximal **safe target envelope**

`E_C(S)={y in Y : d(Cx,y) >= dist(x,S) for every x}`

and proves that enlarging the transported target preserves every source repair radius exactly iff the enlargement stays inside this envelope. A split nonexpansive retraction supplies a descent criterion and a quantitative bound on contraction.

AF-055--AF-057 then classify how much of this geometry is classical and how metric-dependent it is. Singleton linear envelopes are best-coapproximation fibers; finite-dimensional Hilbert set targets reduce to convex-roof/Delaunay radius geometry. But even equivalent finite-dimensional product norms can disagree sharply on whether a finite safe lift exists: for a two-point Euclidean target, the midpoint has a finite vertical lift for product exponent `p<=2` and none for `p>2` or the max metric.

## What remains possible

The live frontier is not another coordinate formula for repair. It is to identify representation categories in which the collision relation, target transport, perturbation metric, and admissible refinements are all intrinsic to the mathematical construction. Non-Hilbert metrics, nonlinear refinements, asymptotic completions, quotient/moduli problems, and arithmetic-specific target constraints remain legitimate because the classical coapproximation/convex-roof reductions no longer settle them automatically.

For arithmetic applications, a discriminator should therefore pass two independent robustness tests: it must lie a positive distance from the matched-control collision set in the topology used downstream, and the structural target whose distance is being measured must descend through every equivalence declared information-preserving. A positive coordinate margin that changes under reversible re-encoding is not yet an intrinsic arithmetic separation.

## Status / novelty

The closed-range, secant, embedding, Lipschitz-free, channel-decision, Blackwell, coapproximation, convex-roof, and Delaunay mechanisms are classical or direct. The persisted Mathia synthesis is the joint gate: **robust fidelity is relative to a collision geometry, while robust repair is additionally relative to an equivalence-compatible target family**. AF-054 supplies an exact maximal-envelope theorem for the latter rather than only an example.

## Falsification criterion

For stability, exhibit a covered category where the stated lower modulus disagrees with distance to admitted collision. For repair, give an isometric/reversible refinement and a target enlargement outside the AF-054 safe envelope that nevertheless preserves every source repair radius, or prove that a proposed arithmetic target and metric are invariant under the full declared equivalence category.

## Lean-formalizable core

- Range-kernel transversality bounds for composition.
- Closed-secant characterization of stable linear compression.
- Distance from a linear/Lipschitz map to collision or stable-loss sets.
- Finite-channel law-collision versus zero-error-support margins.
- Maximal safe target envelope under isometric refinement and descent-defect bounds.
- Hilbert convex-roof/Delaunay description and product-metric threshold examples.
