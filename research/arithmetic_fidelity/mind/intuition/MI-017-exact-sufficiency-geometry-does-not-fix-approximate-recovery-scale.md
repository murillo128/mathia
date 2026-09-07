# MI-017 — Exact sufficiency does not fix the stable recovery scale

**Evidence level:** proved on the finite Blaschke control families through AF-171

## Core intuition

Endpoint-faithful information has three distinct layers: exact identifiability, quantitative inversion in the chosen data norm, and the asymptotic scale at which the endpoint itself is observed. AF-167--AF-168 show that an exactly sufficient witness can become singular at divisor collisions. AF-169--AF-170 show a different failure: even simple, uniformly regular divisors can become asymptotically indistinguishable because the forward representation contracts a source direction exponentially with degree.

AF-171 supplies the positive counterpart. The same radial family is uniformly recoverable once the natural compressed coordinate and boundary-layer endpoint scale are used. Stable fidelity is therefore not determined by the abstract sufficiency geometry alone; it is a property of the **representation metric + admissible family + endpoint normalization**.

## Strongest justified principle

For a degree-`n` finite Blaschke divisor, AF-167 proves exact recovery from degree plus the first `n` phase-gradient moments, and AF-168 quantifies the collision singularity of that inverse. AF-169 then removes collisions from the explanation: regular simple divisors with radii `r` and `s` fixed inside the disk have a fixed bottleneck separation while their relevant moment data differ by only exponentially small terms. The Jacobian itself has exponentially small radial singular values.

AF-170 strengthens the obstruction from a truncated witness to the complete finite inner function. For the symmetric radial family,

`B_(n,r)(z)=(z^n-r^n)/(1-r^n z^n)`,

the full `H^infinity` distance between fixed `r<s<1` tends to zero even though the divisors do not approach each other in the unscaled endpoint metric. Completeness of the analytic representation therefore does not imply degree-uniform fidelity.

AF-171 identifies the exact compressed coordinate: the `H^infinity` distance is controlled by the pseudohyperbolic separation of `r^n` and `s^n`. On the boundary layer `u=-n log r`, `v=-n log s` with `u,v` in a fixed compact positive interval, this representation metric is uniformly bi-Lipschitz to `|u-v|`, while the correctly rescaled divisor distance has the same limit. The apparent information loss is repaired only after matching the endpoint scale to the coordinate actually retained.

## Counterevidence / boundary

The boundary-layer rescue is proved for a highly symmetric control family; it is not a universal prescription to multiply every endpoint distance by degree. General divisors can also suffer multiplicity, separation, or conditioning losses that require different normal forms. The correct scale must come from the representation and the downstream discriminator, not from retrospective renormalization.

## Epistemic status

**Proved on the declared finite Blaschke families; supported as a general fidelity principle.** No claim is made that every complete representation admits a useful rescaling.

## Falsification criterion

Produce a degree-uniform recovery modulus from the fixed-interior `H^infinity` data to the unscaled radial divisor metric despite AF-170, or show that the AF-171 pseudohyperbolic/boundary-layer comparison fails on its stated compact regime. More generally, a source-forced downstream theorem that consumes the unscaled endpoint while remaining stable under the collapsing control would narrow this principle.