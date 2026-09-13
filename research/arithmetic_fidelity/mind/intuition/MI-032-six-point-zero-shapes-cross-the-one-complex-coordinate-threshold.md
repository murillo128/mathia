# MI-032 — Six-point zero shapes cross the one-complex-coordinate threshold

**Evidence level:** exact for centered six-point unit-circle multisets through [AF-315](../../findings/AF-315-six-point-zero-shapes-need-three-real-harmonic-coordinates.md). The rational-prime specialization is conditional on a hypothetical nonzero six-prime exact hit. No first-incidence theorem or uniform conditioning bound follows.

Let `Z={z_1,...,z_6} subset S^1` with `s_1=sum_j z_j=0` and `s_m=sum_j z_j^m`. On the open stratum `s_3 != 0`, self-inversive symmetry plus Newton identities determine the entire monic root polynomial from `(s_2,s_3)`, so those two harmonics recover the unordered phase multiset exactly.

After quotienting common phase, the intrinsic information bill is smaller than two complex numbers but larger than one. Under `Z -> rho Z`, `(s_2,s_3)` has weights `(2,3)`, and

`R(Z) = ( |s_3|, kappa(Z) )`, with `kappa=s_2^3/s_3^2`,

is a complete invariant on `s_3 != 0`. The generic centered six-point configuration space has real dimension `4`; quotienting common rotation leaves a generic unordered shape space of real dimension `3`. By invariance of domain, no continuous invariant valued in one complex scalar can be faithful on a generic open shape patch. Thus the three real coordinates in `R` are dimension-tight.

This is the first support size where the five-point phenomenon stops. At five points, the zero-fiber relation between `|s_2|` and `|s_3|` lets the single complex invariant `kappa` retain the whole two-real-dimensional shape quotient. At six points the two harmonic magnitudes are generically independent, so one extra real modulus is unavoidable even though the same low-harmonic pair still reconstructs the raw unordered phases.

For six distinct rational primes at a hypothetical nonzero exact hit, AF-315 proves `F_P(2t) != 0` and `F_P(3t) != 0`: a second-harmonic zero would force cubic-torsion orbits and a third-harmonic zero would force antipodal pairing, both incompatible with unique factorization for distinct primes at one common nonzero time. Therefore every such hypothetical prime hit lies in the faithful stratum, and

`( |F_P(3t)|, F_P(2t)^3/F_P(3t)^2 )`

recovers its unordered phase shape modulo common phase.

The distinction remains load-bearing: **post-incidence recoverability, quotient dimension, first incidence and stability are different resources**. AF-315 settles the continuous quotient-coordinate threshold at six points and removes the obvious low-harmonic singular strata for prime hits, but it gives no mechanism forcing or excluding the first six-prime hit and no positive distance from the singular geometry.

**Research consequence.** Count information after quotienting the actual nuisance symmetry and imposing source-valid algebraic relations. Raw observation count can overstate the needed representation, while a one-complex-coordinate summary can become dimensionally impossible as the admissible fiber grows. For larger centered supports, the useful question is whether a small low-harmonic family still gives exact recovery with a quotient coordinate count matching the true generic shape dimension, and which singular strata rational-prime arithmetic excludes; that question is separate from the still-open nontorsion first-incidence problem.