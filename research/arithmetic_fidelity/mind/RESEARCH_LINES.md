# Arithmetic-fidelity research lines

This file holds the current mathematical lines of investigation suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Derive the admissible provenance code only after the endpoint quotient is fixed

**Linked intuitions:** `MI-001-recovery-has-a-source-relative-and-a-target-relative-layer`, `MI-015-endpoint-fidelity-is-a-quotient-problem-before-a-coding-problem`, and `MI-016-provenance-must-be-transported-coherently-not-recomputed-after-compression`.

Continue to measure retained information only modulo distinctions that the downstream theorem cannot see. Family-wide recovery still requires one common reverse channel, and a canonical source center or provenance code must be transported coherently rather than recomputed after compression without a separate stability theorem.

## Declare the endpoint quotient, endpoint metric, and asymptotic scale together

**Linked intuitions:** `MI-007-stable-fidelity-is-distance-from-collision` and `MI-017-exact-sufficiency-geometry-does-not-fix-approximate-recovery-scale`.

AF-167--AF-168 separate finite exact sufficiency from collision conditioning. AF-169--AF-170 add a different asymptotic obstruction: even regular simple divisors can remain a fixed endpoint distance apart while their complete finite Blaschke inner factors converge in the natural `H^infinity` norm. No multiplicity collision is needed; the forward map itself contracts the radial coordinate exponentially with degree.

AF-171 identifies the corresponding positive scale. For the regular radial family, the exact `H^infinity` distance is the pseudohyperbolic distance between `r^n` and `s^n`. In boundary-layer coordinates `u=-n log r`, this metric is uniformly bi-Lipschitz to `|u-v|` on compact positive ranges, while `n` times the divisor bottleneck converges to the same scale.

The next recovery theorem must therefore specify not only **what** endpoint is reconstructed but **at what normalization and in which data metric**. A degree-uniform inverse can fail for an unscaled endpoint and become well-conditioned on a source-forced boundary layer. The scale must be derived from the representation/downstream problem, not chosen after seeing the control.

## Prove stable inversion in the exact metric consumed downstream

Exact injectivity is only the first gate. For growing families, derive a recovery modulus with explicit dependence on degree, multiplicity, separation, forward attenuation, and the chosen endpoint normalization. Test both collision singularities and regular contraction examples before calling a representation faithful.

When an exact compressed coordinate is visible, as `r^n` is in AF-170--AF-171, prefer to expose it explicitly and compare the downstream endpoint to that coordinate. This separates genuine information loss from a mismatch between the natural representation scale and an arbitrarily stronger target metric.

## Match reference complexity, provenance transport, endpoint loss, and inverse conditioning

A useful fidelity claim should state four separate costs: the information surviving the endpoint quotient, the source-relative reference/provenance code, the stability of transporting that code through compression, and the conditioning of the final inverse at the asymptotic scale actually used. None is implied by the others.