# MI-007 — Stable fidelity is positive distance from the collision boundary in the admitted topology

**Evidence level:** supported by exact Hilbert, Euclidean, smooth-compact, Lipschitz, and finite-channel classifications

## Core intuition

Exact recoverability and stable recoverability are not merely qualitative and quantitative versions of the same slogan. In the natural normed spaces studied so far, the stability modulus is a distance to loss of the relevant distinction: stable fidelity means that the representation lies a positive distance from the closure of admitted collisions in the **specific topology in which perturbations are allowed**.

The target failure notion is part of that statement. AF-046 shows that two channel rows can remain positively separated as probability laws while exact zero-error support fidelity has zero total-variation robustness. Thus `distance to collision` is meaningful only after both the collision relation and the ambient perturbation category are fixed.

## Strongest justified principle

AF-041 gives the linear-composition prototype. If `A` has closed range and `B` has closed range, then `BA` is exactly injective when `Ran(A)` misses `ker(B)`, but is bounded below only when the two subspaces are uniformly transverse. The transversality modulus quantitatively controls the lower modulus of the composite.

AF-042--AF-043 turn this into a geometric statement. On a compact smooth carrier, a `C^1` representation is stably faithful exactly when it is an injective immersion. For a linear compression of an arbitrary Euclidean set `S`, the exact object is the closed unit-secant carrier: exact injectivity avoids the kernel on actual secants, while stable fidelity avoids it on all limiting secants as well. Tangent directions are precisely the extra limiting secants that appear for compact smooth manifolds.

AF-044 identifies the perturbative meaning exactly. The closed-secant modulus `kappa_S(B)` is the operator-norm distance from `B` to stable fidelity failure and also the distance to the set of actual pair-collapsing operators; the stable-failure set is the closure of the collision set. AF-045 removes finite-dimensional linearity: for a pointed metric space and Banach-valued Lipschitz map `f`, the lower Lipschitz modulus `beta(f)` is exactly the Lipschitz-norm distance to noninjective maps and to their closed stable-failure set. Lipschitz-free linearization identifies normalized elementary molecules as the intrinsic secant carrier.

AF-046--AF-050 add a complementary finite-channel boundary. Law equality has a positive TV collision margin when rows are separated, whereas zero-error support overlap is dense and destroys any positive TV zero-error margin. Distances **to repair** the same zero-error target then depend sharply on the discrepancy: average TV, row-sup TV, forward/reverse KL, and general `f`-divergences induce different exact partition objectives.

AF-051 adds a representation audit. Quadratic/Brier repair is exact but changes under statistically reversible uniform output cloning. Hence an exact metric projection can still be non-intrinsic if the metric distinguishes presentations that the information category regards as equivalent.

## What remains possible

The next useful question is to classify distance-to-loss and distance-to-repair formulas for nonlinear operator families, quotient/moduli problems, stochastic channels, and asymptotic completions while requiring invariance under the category's own harmless refinements. Composition is especially important: individually stable stages can approach a downstream kernel and make the composite unstable.

For arithmetic applications, a representation that distinguishes rational primes only at zero distance from a matched-control collision set is structurally fragile even if every finite instance is injective. Conversely, a positive coordinate distance is not enough when a reversible re-encoding can change that distance. A meaningful robust discriminator should come with a positive, representation-invariant margin in the topology required by the final theorem.

## Status / novelty

The underlying closed-range, secant, embedding, perturbation, channel-projection, and Lipschitz-free facts are classical or direct. The persisted Mathia synthesis is the identification of a common stability object — distance to the relevant collision boundary — together with the newer requirement that the failure relation, topology, and information-preserving representation equivalences all be declared before that distance is interpreted.

## Falsification criterion

Find a covered category in which the stated lower modulus is positive but arbitrarily small admitted perturbations create the relevant collision, or conversely where the modulus vanishes while a positive perturbation radius remains. For proposed intrinsic repair costs, exhibit a reversible refinement that changes the cost, or prove invariance under the full admitted equivalence class.

## Lean-formalizable core

- Range-kernel transversality bounds for composition.
- Closed-secant characterization of stable linear compression.
- Distance from a linear map to collision/stable-loss sets.
- Lipschitz lower modulus as distance to noninjectivity.
- Finite-channel law-collision versus zero-error-support margins.
