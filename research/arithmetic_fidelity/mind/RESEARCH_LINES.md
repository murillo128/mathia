# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the admissible provenance code only after the endpoint quotient is fixed

**Linked intuitions:** `MI-001-recovery-has-a-source-relative-and-a-target-relative-layer`, `MI-015-endpoint-fidelity-is-a-quotient-problem-before-a-coding-problem`, and `MI-016-provenance-must-be-transported-coherently-not-recomputed-after-compression`.

Continue to measure retained information only modulo distinctions that the downstream theorem cannot see. AF-172 adds an important control: a symmetric compressed coefficient such as the cyclic parameter `alpha` can already transport both radial and angular endpoint information, so an orientation mark must not be added merely because a chosen real slice forgot it. Family-wide recovery still requires one common reverse channel and coherent provenance transport.

## Declare the endpoint quotient, metric, degree regime, and asymptotic scale together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision` and `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-169--AF-171 show that complete finite Blaschke data can contract a regular radial direction exponentially with degree, while the natural boundary-layer coordinate restores a uniform metric. AF-173 then identifies the exact output gauge on cyclic factors: after quotienting one unimodular scalar, the complete `H^infinity` distance is exactly twice the pseudohyperbolic distance of the compressed parameters.

AF-174 gives the global fixed-degree boundary: divisor recovery is at best Hölder with exponent `1/n` on the unrestricted degree-`n` class. AF-175 shows that degree itself is not the destructive variable. A degree-independent lower interpolation constant restores a degree-uniform locally Lipschitz inverse. The next theorem must therefore state the endpoint quotient, output gauge, source regularity modulus, degree regime, and normalization together.

## Prove stable inversion in the exact metric consumed downstream

Exact injectivity is only the first gate. For growing families, derive a recovery modulus with explicit dependence on multiplicity, interpolation/separation, forward attenuation, output gauge, and the endpoint normalization actually used. Uniform interpolation is now a positive model of the right statement: it excludes the clustering directions responsible for the global `1/n` law without introducing an extra side channel.

When a compressed coordinate is visible, expose it explicitly and compare the downstream endpoint to that coordinate. When the source class supplies a regularity modulus such as the Blaschke interpolation constant, keep that modulus as part of the theorem rather than treating degree as a proxy for conditioning.

## Match reference complexity, provenance transport, endpoint loss, and inverse conditioning

A useful fidelity claim should state separately the information surviving the endpoint quotient, the source-relative reference/provenance code, stability of transporting that code through compression, and conditioning of the inverse on the actual source stratum. None is implied by the others.