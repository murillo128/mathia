# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-236 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows: negative eigenvalues may approach zero and normalized eigenvector mass may escape. WI-237 closes the tempting raw-Hilbert-space repair. The unconditional simple critical-line exponentials are complete in `L^2(E)` on every bounded positive-measure window, while their density prevents them from forming a Bessel family. Ordinary positive-angle, Riesz, or blanket linear-independence arguments therefore cannot exclude the collapse alternative.

The surviving Bombieri-side currency is the **coefficient price** of approximating a finite off-line packet by critical-line exponentials under the normalized `ell^2` budget inherited from the finite negative eigenvectors, plus height tightness when the off-line divisor is infinite. A useful theorem must distinguish these eigenvector-selected relations from arbitrary complete-span approximation.

## Use finite-radius source nondegeneracy as an alternative to zero-side passage-to-limit

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238 integrates Suzuki's localized Weil theory with the sparse-defect diagnosis. RH failure forces a finite first support radius `a_*` at which the localized self-adjoint Weil operator has a nonzero zero mode. The lowest eigenvalue is continuous and nonincreasing in the radius, so the obstruction appears as a genuine finite crossing rather than only as a cofinal zero-side limit.

For fixed `a`, the source kernel uses only von Mangoldt data `Lambda(n)` with `n<=exp(2a)` plus explicit archimedean terms. Thus an off-critical zero anywhere in the global divisor forces a **finite-prime, finite-support, source-side zero mode**. This does not make RH easy—the all-radius nondegeneracy criterion is itself RH-equivalent—but it removes Bombieri coefficient tightness as a logically mandatory bridge.

The live alternative is to exploit the first-crossing structure or prove source-side nondegeneracy of the localized operator from its finite-prime kernel in a way cheaper than reasserting Weil positivity. This branch should be compared against the Bombieri coefficient-budget route rather than conflated with it.

## Treat finite inertia, ambient completeness, and localized source nondegeneracy as distinct objects

Finite negative index counts defects but does not quantify their distance from the critical line. Raw critical exponentials can approximate every local target but may require unbounded coefficient cost. Suzuki localization moves the decision to a different finite-support source operator whose zero crossing is exact but infinite-dimensional. Future arguments should state which of these three currencies they control and should not transfer coercivity claims between them without an explicit theorem.
