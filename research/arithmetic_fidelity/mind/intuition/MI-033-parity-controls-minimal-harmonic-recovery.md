# MI-033 — Parity controls generic harmonic recovery; even singular fibers are source-specific arithmetic gates

**Evidence level:** exact for centered unit-circle multisets through [AF-316](../../findings/AF-316-parity-controls-minimal-harmonic-lift.md), with the higher-even-support singular boundary sharpened by [AF-317](../../findings/AF-317-antipodal-extension-recursion-breaks-six-point-singular-rigidity.md). Rational-prime incidence, singular-fiber character rank, conditioning, and downstream access to the required lift remain separate.

Let `Z={z_1,...,z_n} subset S^1` satisfy `s_1=sum_j z_j=0`, write `s_r=sum_j z_j^r`, and let `E=prod_j z_j`. Newton identities recover the lower elementary symmetric coefficients from the low harmonics, while unit-circle roots impose

`e_(n-k) = E conjugate(e_k)`.

For odd support `n=2m+1`, no coefficient is self-paired. The lower block `(s_2,...,s_m)` is generically short by one real degree, and the missing degree is `E in S^1`; `(s_2,...,s_m,E)` recovers the unordered multiset globally and uses the generic `n-2` real dimensions. If one insists on harmonics only, `(s_2,...,s_(m+1))` recovers on `e_m != 0` with one exact real redundancy.

For even support `n=2m`, the middle coefficient is self-paired. On `e_m != 0`, its phase determines `E`, so `(s_2,...,s_m)` is already dimension-tight and recovers the unordered multiset. On `e_m=0` this phase-recovery step disappears; adding `E` always repairs exact recovery, but whether the source can reach the singular fiber is an arithmetic question.

The six-point case is exceptionally rigid and must not be generalized. There `e_3=0` forces the degree-six root polynomial to be even, hence three antipodal pairs; AF-310 then makes that geometry incompatible with a nonzero common rational-prime time. AF-317 proves that this implication breaks at eight points. For every higher even degree an antipodal-extension recursion populates `e_m=0`, and already at eight points there is an exact centered example with `e_4=0`, `e_3!=0` that is nontorsion and not globally antipodally invariant.

So the even singular set has two distinct layers that happened to coincide at six points: **recovery singularity** (`e_m=0` destroys the elementary phase formula) and **source inadmissibility** (the geometry forces too many integer-character relations for the prime-log orbit). From eight points onward the first no longer implies the second by self-inversive/cyclotomic geometry alone.

After quotienting common rotation, the generic shape dimension remains `n-3`; AF-317 does not reopen generic identifiability. It moves the live problem onto the exceptional source geometry. At support eight the decisive question is whether the centered singular fiber `s_1=0, e_4=0` contains a point whose integer-character relation lattice has rank at most one, the maximum allowed by AF-310 for a common nonzero rational-prime time. The existing proposed clue `CLUE-eight-point-middle-singular-character-rank` isolates that test.

**Boundary.** Exact recovery is not stable recovery. AF-317 does not produce an eight-prime hit, does not prove a rank-`0/1` singular point, and does not exclude one. Its explicit witness deliberately contains an antipodal relation and may have further character relations. The generic parity theorem, first incidence, singular-fiber arithmetic rank, observation access to `E`, and inverse conditioning remain separate resources.
