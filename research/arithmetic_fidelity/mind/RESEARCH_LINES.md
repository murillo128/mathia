# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the admissible provenance code only after the endpoint quotient is fixed

**Linked intuitions:** `MI-001-recovery-has-a-source-relative-and-a-target-relative-layer`, `MI-015-endpoint-fidelity-is-a-quotient-problem-before-a-coding-problem`, and `MI-016-provenance-must-be-transported-coherently-not-recomputed-after-compression`.

Continue to measure retained information only modulo distinctions that the downstream theorem cannot see. AF-172 adds an important control: a symmetric compressed coefficient such as the cyclic parameter `alpha` can already transport both radial and angular endpoint information, so an orientation mark must not be added merely because a chosen real slice forgot it. Family-wide recovery still requires one common reverse channel and coherent provenance transport.

## Declare the endpoint quotient, metric, source regularity, degree regime, and asymptotic scale together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision` and `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-171 show that complete finite Blaschke data can contract a regular radial direction exponentially with degree, while the natural boundary-layer coordinate restores a uniform metric. AF-173 then identifies the exact output gauge on cyclic factors: after quotienting one unimodular scalar, the complete `H^infinity` distance is exactly twice the pseudohyperbolic distance of the compressed parameters.

AF-174 gives the global fixed-degree boundary: divisor recovery is at best Hölder with exponent `1/n` on the unrestricted degree-`n` class. AF-175 shows that a degree-independent lower interpolation constant restores a degree-uniform locally Lipschitz inverse. AF-176 proves on cyclic radial families that the reciprocal interpolation constant is also quantitatively necessary, and AF-177 removes the symmetry restriction: at every finite simple Blaschke divisor a Frostman shift forces local inverse slope `1/(2 delta(B))`, while AF-175 gives the matching upper scale `1/delta(B)`.

Thus the interpolation constant is not merely a convenient sufficient hypothesis. For the declared quotient/output and divisor metrics it is the intrinsic local conditioning scale up to a universal factor two. Any stable-fidelity theorem must expose the source regularity modulus that plays this role rather than substituting degree, simplicity, or exact injectivity.

## Prove stable inversion in the exact metric consumed downstream

Exact injectivity is only the first gate. For growing families, derive a recovery modulus with explicit dependence on multiplicity, interpolation/separation, forward attenuation, output gauge, and the endpoint normalization actually used. The finite-Blaschke model now provides both sides of the calibration: a nondegenerate interpolation constant is sufficient for local Lipschitz recovery and its reciprocal is necessary up to factor two.

When a compressed coordinate is visible, expose it explicitly and compare the downstream endpoint to that coordinate. When the source class supplies a regularity modulus such as the Blaschke interpolation constant, keep that modulus as part of the theorem and test whether it remains nondegenerate in the actual asymptotic regime.

## Match reference complexity, provenance transport, endpoint loss, and inverse conditioning

A useful fidelity claim should state separately the information surviving the endpoint quotient, the source-relative reference/provenance code, stability of transporting that code through compression, and conditioning of the inverse on the actual source stratum. None is implied by the others.