# MI-007 — Stable fidelity is positive distance from the collision boundary in the admitted topology

**Evidence level:** supported by exact Hilbert, Euclidean, smooth-compact, and Lipschitz classifications

## Core intuition

Exact recoverability and stable recoverability are not merely qualitative and quantitative versions of the same slogan. In the natural normed spaces studied so far, the stability modulus is exactly a distance to loss of injectivity: stable fidelity means that the representation lies a positive distance from the closure of exact collisions in the **specific topology in which perturbations are admitted**.

## Strongest justified principle

AF-041 gives the linear-composition prototype. If `A` has closed range and `B` has closed range, then `BA` is exactly injective when `Ran(A)` misses `ker(B)`, but is bounded below only when the two subspaces are uniformly transverse. The transversality modulus quantitatively controls the lower modulus of the composite.

AF-042--AF-043 turn this into a geometric statement. On a compact smooth carrier, a `C^1` representation is stably faithful exactly when it is an injective immersion. For a linear compression of an arbitrary Euclidean set `S`, the exact object is the closed unit-secant carrier: exact injectivity avoids the kernel on actual secants, while stable fidelity avoids it on all limiting secants as well. Tangent directions are precisely the extra limiting secants that appear for compact smooth manifolds.

AF-044 identifies the perturbative meaning exactly. The closed-secant modulus `kappa_S(B)` is the operator-norm distance from `B` to stable fidelity failure and also the distance to the set of actual pair-collapsing operators; the stable-failure set is the closure of the collision set. AF-045 removes finite-dimensional linearity: for a pointed metric space and Banach-valued Lipschitz map `f`, the lower Lipschitz modulus `beta(f)` is exactly the Lipschitz-norm distance to noninjective maps and to their closed stable-failure set. Lipschitz-free linearization identifies normalized elementary molecules as the intrinsic secant carrier.

Thus the stable/exact distinction has a reusable geometric form:

`exact fidelity = no admitted collision`, while `stable fidelity = positive topological distance from collision`.

The topology is essential. Operator norm, Lipschitz norm, Hilbert lower-frame geometry, and other categories need not induce the same boundary, so this principle does not license moving a positive margin from one category to another.

## What remains possible

The next useful question is to classify distance-to-loss formulas for nonlinear operator families, quotient/moduli problems, stochastic channels, and asymptotic completions where the natural perturbation topology is not automatically obvious. Composition is especially important: AF-041 shows that individually stable stages can approach a downstream kernel and make the composite unstable.

For arithmetic applications, a representation that distinguishes rational primes only at zero distance from a matched-control collision set is structurally fragile even if every finite instance is injective. A meaningful robust discriminator should come with a positive margin in the topology required by the final theorem.

## Status / novelty

The underlying closed-range, secant, embedding, perturbation, and Lipschitz-free facts are classical or direct. The persisted Mathia synthesis is the exact identification of a common stability object — distance to the collision boundary — across these categories, with an explicit warning that the ambient topology is part of the claim.

## Falsification criterion

Find a category covered by AF-041--AF-045 in which the stated lower modulus is positive but arbitrarily small admitted perturbations create a collision, or conversely where the modulus vanishes while a positive perturbation radius to every collision remains. Extensions must specify the perturbation space and norm before claiming the same principle.

## Lean-formalizable core

- Range-kernel transversality bounds for composition.
- Closed-secant characterization of stable linear compression.
- Distance from a linear map to collision/stable-loss sets.
- Lipschitz lower modulus as distance to noninjectivity.
