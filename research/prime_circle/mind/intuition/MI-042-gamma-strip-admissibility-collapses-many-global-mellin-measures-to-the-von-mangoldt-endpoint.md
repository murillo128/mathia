# MI-042 — Gamma-strip admissibility collapses many global Mellin measures to the von Mangoldt endpoint

**Evidence level:** exact synthesis from [PC-335](../../findings/PC-335-bounded-indefinite-mellin-symbols-cannot-separate-prime-powers.md)--[PC-339](../../findings/PC-339-critical-gamma-strip-collapses-global-mellin-measures.md). The bounded-analytic/Blaschke uniqueness mechanism used in PC-339 is classical; the Mathia content is its application to the prime-circle Mellin shell response and the resulting representation boundary.

PC-338 had already classified compactly supported distributions in Mellin frequency: exact semiprime-null scalar shell response is invisible away from `s=1`, while the endpoint response reduces to ordinary von Mangoldt. A natural escape was to abandon compact support and use a genuinely global Mellin-frequency measure.

PC-339 shows that global support alone is not enough. Let `T` be a finite complex Borel measure on the real Mellin frequency line whose weighted variation is compatible with the critical Gamma strip, in particular satisfying the boundary-admissibility condition carried by the `Gamma` factor. If its scalar shell functional annihilates every distinct semiprime, then the same dichotomy survives:

- off the endpoint line `sigma!=1`, the shell response vanishes identically on every `n>1`;
- on `sigma=1`, the visible response is a scalar multiple of `Lambda(n)`.

The mechanism is not compact support but analytic uniqueness. The `Gamma` decay gives a bounded holomorphic continuation in a horizontal strip of half-width `pi/2`. Prime-log zeros become a sequence approaching the strip boundary whose conformal images violate the Blaschke summability condition because `sum_p 1/p` diverges. A bounded strip function carrying all those zeros must therefore vanish identically. The semiprime-null condition again leaves only the endpoint von-Mangoldt component.

This changes the representation frontier. “Use noncompact Mellin support” is not yet a distinct mechanism if the global measure remains tame enough for the natural Gamma-strip boundary control. A surviving scalar radial selector must leave the **boundary-admissible measure class**, not merely the compact-support class, or else change category entirely: a non-measure analytic functional, shell-dependent symbol/order, nonlinear operation, matrix-valued refinement, or genuinely cross-shell coupling before scalar evaluation.

The reusable warning is that support size and analytic class are different resources. Compactness was sufficient for the earlier uniqueness argument but not essential. Once the native Gamma factor supplies enough strip control, a global measure can still be rigidly determined by the same prime-log zero set. A proposed “global” selector should therefore state its exact boundary growth before being credited as an escape from compact-frequency no-go results.

**Boundary.** PC-339 does not classify arbitrary noncompact distributions or measures outside the Gamma-strip admissibility condition, analytic functionals of faster boundary growth, nonlinear or matrix-valued selectors, or cross-shell constructions. Escaping the measure class or the boundary condition is only a representation escape; it still needs an independent zero-sensitive destination theorem rather than mere arithmetic source reconstruction.
