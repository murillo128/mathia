# MI-033 — Parity controls the minimal harmonic lift of centered unit-circle data

**Evidence level:** exact for centered unit-circle multisets through [AF-316](../../findings/AF-316-parity-controls-minimal-harmonic-lift.md). The rational-prime specialization remains conditional on a hypothetical exact hit; first incidence, conditioning, and the even-support singular set are separate questions.

Let `Z={z_1,...,z_n} subset S^1` satisfy `s_1=sum_j z_j=0`, write `s_r=sum_j z_j^r`, and let `E=prod_j z_j`. Newton identities recover the lower elementary symmetric coefficients from the low harmonics, while unit-circle roots impose the self-inversive relation

`e_(n-k) = E conjugate(e_k)`.

The fixed-point structure of the involution `k -> n-k` determines the information bill.

For odd support `n=2m+1`, no coefficient is self-paired. The lower block `(s_2,...,s_m)` is generically short by exactly one real degree, and the missing degree is the product phase `E in S^1`. The tuple `(s_2,...,s_m,E)` therefore recovers the whole unordered multiset globally and uses exactly `n-2` real coordinates, the generic dimension of the centered configuration space. If one insists on harmonics only, `(s_2,...,s_(m+1))` recovers on `e_m!=0`, with one exact real redundancy.

For even support `n=2m`, the middle coefficient is fixed by the involution. On `e_m!=0`, its phase determines `E`, so `(s_2,...,s_m)` already recovers the unordered multiset using exactly `n-2` real coordinates. The exceptional set `e_m=0` is the genuine phase-loss stratum; adding `E` always repairs exact recovery, but its arithmetic accessibility and minimal singular-stratum cost remain separate.

After quotienting common rotation, the generic shape dimension is `n-3`. Thus the five- and six-point cases were not isolated accidents: **parity decides whether self-inversive closure leaves one residual global phase, while the generic continuous information budget is fixed by the actual centered quotient dimension.**

**Research consequence.** The generic larger-support post-incidence representation problem is now closed at the level of exact identifiability. The arithmetic frontier should not ask again whether a bounded low-harmonic family can separate generic centered configurations. It should ask whether a prime-log orbit ever reaches the zero fiber, whether even-support prime hits can enter `e_m=0`, whether the odd product-phase lift is accessible in the downstream information class, and how conditioning degenerates near the singular strata.

**Boundary.** Exact recovery is not stable recovery. The theorem does not identify the primes attached to recovered phases, prove a first hit, exclude `e_m=0` for all even prime supports, or give a uniform inverse modulus.
