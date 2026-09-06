# MI-017 — Endpoint recovery needs both a quotient-adequate witness and a stable inverse

**Evidence level:** exact finite-experiment, decision-theoretic, Hardy-factorization, moment-reconstruction, and root-stability results through AF-168

## Core intuition

Exact sufficiency geometry does not determine quantitative recoverability. The destination first decides which source distinctions matter; only then can one ask for the smallest retained witness that separates those endpoint classes. Even after such a witness is exactly injective, a limiting arithmetic problem still needs its inverse to remain quantitatively usable on the admissible family.

The durable hierarchy is therefore: **declare the endpoint quotient, identify an intrinsic endpoint-faithful witness, and then prove a recovery modulus at the relevant scale.** Exact recovery without a stable inverse can be mathematically correct and asymptotically useless.

## Strongest justified principle

AF-160--AF-165 calibrate the source side. A recoverable barycentric reference has an exact likelihood-complexity penalty, provenance composition depends on the admissible identity code, and whole-source recovery may be stronger than the endpoint requires. Endpoint entropy and cross-endpoint overlap, not hidden-source cardinality, are the intrinsic decision costs.

AF-166 makes the quotient concrete in Hardy space. Boundary modulus determines the outer factor but is blind to the inner factor; finite Blaschke multiplication can alter the entire disk zero divisor while preserving the retained modulus. The correct repair depends on the endpoint: winding/phase degree can recover only zero count, Blaschke information is needed for the divisor, and full inner data are needed for the full analytic function.

AF-167 then shows that a full phase field is excessive for a finite divisor. For a degree-`n` finite Blaschke product, the phase-gradient mean gives `n` and the first `n` positive Fourier coefficients give the power sums; Newton--Girard reconstructs the divisor exactly, while `n-1` moments fail uniformly by a root-of-unity matched control.

AF-168 supplies the missing quantitative boundary. The same moment map has a globally sharp `1/n`-Hölder inverse, a locally sharp `1/m` exponent at maximum multiplicity `m`, and a locally analytic/Lipschitz inverse only at simple separated divisors. The Vandermonde determinant locates the collision singularity, while its shrinking value warns that even simple-root families can lose uniform conditioning as separations collapse.

## What remains possible

A concrete arithmetic endpoint may tolerate coarse zero location, quotient multiple roots, or use a witness whose inversion is better conditioned than raw power sums. Those are legitimate ways to reduce the stability burden, but they must be stated as changes in the endpoint or witness rather than inferred from exact injectivity.

Conversely, a growing-degree divisor problem cannot cite AF-167 alone. It must control the degree-dependent constants, multiplicities, separations, and the forward error with which phase moments are actually obtained, or replace the witness by one with a source-calibrated stable inverse.

## Status / novelty

Sufficiency, Le Cam recovery, Shtarkov/NML complexity, Hardy inner--outer factorization, Poisson phase derivatives, Newton identities, Vandermonde geometry, and root perturbation are classical ingredients. The durable Arithmetic Fidelity synthesis is the three-stage gate: **quotient correctness, exact witness sufficiency, and quantitative inverse stability are separate requirements.**

## Falsification criterion

Produce an endpoint for which distinctions inside a declared quotient fiber necessarily affect the endpoint; invalidate the finite-Blaschke `n`-moment reconstruction or its `n-1` collision control; or derive a uniform inverse exponent stronger than `1/n` on the full degree-`n` class despite the root-of-unity splitting family. Any such result would change the hierarchy above.