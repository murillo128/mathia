# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete in `L^2(E)` on every bounded positive-measure window and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving Bombieri-side currency is the coefficient price of the eigenvector-selected approximation together with height tightness.

## Make the finite-radius route a von-Mangoldt compensation theorem, not a generic first-crossing argument

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238 moves the alternative route to Suzuki's localized Weil operator: RH failure produces a finite support radius with a zero/negative mode using only finitely many von Mangoldt coefficients plus explicit non-prime completion data.

WI-239 closes the abstract first-crossing escape. The universal logarithmic core alone has an exactly translated spectrum `lambda_{0,k}(a)=mu_k-1-log a`, hence a genuine finite first zero mode with simple positive even ground state. Nesting, compact resolvent, parity, the logarithmic singularity, and an attained first crossing are therefore not coercive.

WI-240 goes further. After deleting only the von Mangoldt term and retaining the full gamma and pole contributions, the odd negative index tends to infinity with support radius. Thus the non-prime completion cannot by itself select the positive branch. If the full zeta Weil form remains nonnegative, the signed prime contribution must compensate increasingly many negative directions. This does **not** say that the prime term is sign-definite; it identifies its indispensable role.

The live finite-radius theorem is consequently source-specific: prove nondegeneracy/positivity by exploiting the actual von Mangoldt translation/correlation term against the negative non-prime background, or identify a finite-prime invariant that forces such compensation. Generic crossing geometry is now a matched control, not a route to contradiction.

## Treat finite inertia, ambient completeness, and prime-compensated localized positivity as distinct objects

Finite negative index counts zero-side defects but may lose quantitative coercivity. Ambient critical exponentials can approximate local targets with uncontrolled coefficient cost. Localized source operators avoid that limit but, after WI-239--WI-240, their decisive currency is explicitly the zeta prime contribution relative to a non-prime form that is itself strongly indefinite. Future arguments should state which of these currencies they control and not transfer coercivity between them without a theorem.