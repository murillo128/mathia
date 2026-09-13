# MI-033 — Parity controls generic harmonic recovery; even singular fibers are source-specific arithmetic gates

**Evidence level:** exact for centered unit-circle multisets through [AF-316](../../findings/AF-316-parity-controls-minimal-harmonic-lift.md), with the higher-even-support singular boundary sharpened by [AF-317](../../findings/AF-317-antipodal-extension-recursion-breaks-six-point-singular-rigidity.md) and [AF-318](../../findings/AF-318-antipodal-extension-has-residual-rank-one-character-lattice.md). Rational-prime incidence, conditioning, and downstream access to the required lift remain separate.

Let `Z={z_1,...,z_n} subset S^1` satisfy `s_1=sum_j z_j=0`, write `s_r=sum_j z_j^r`, and let `E=prod_j z_j`. Newton identities recover the lower elementary symmetric coefficients from the low harmonics, while unit-circle roots impose

`e_(n-k) = E conjugate(e_k)`.

For odd support `n=2m+1`, no coefficient is self-paired. The lower block `(s_2,...,s_m)` is generically short by one real degree, and the missing degree is `E in S^1`; `(s_2,...,s_m,E)` recovers the unordered multiset globally and uses the generic `n-2` real dimensions. If one insists on harmonics only, `(s_2,...,s_(m+1))` recovers on `e_m != 0` with one exact real redundancy.

For even support `n=2m`, the middle coefficient is self-paired. On `e_m != 0`, its phase determines `E`, so `(s_2,...,s_m)` is already dimension-tight and recovers the unordered multiset. On `e_m=0` this phase-recovery step disappears; adding `E` always repairs exact recovery, but whether the source can reach the singular fiber is an arithmetic question.

The six-point case is exceptionally rigid and must not be generalized. There `e_3=0` forces the degree-six root polynomial to be even, hence three antipodal pairs; AF-310 then makes that geometry incompatible with a nonzero common rational-prime time. AF-317 proves that this implication breaks at eight points by constructing exact centered nontorsion configurations with `e_4=0` that are not globally antipodally invariant.

AF-318 closes the next source-independent escape. Inside AF-317's explicit eight-point antipodal-extension family, after normalizing by the appended phase, the integer-character relation lattice is

`L_B = 2 Z e_7`

on a dense residual subset of the nondegenerate hexagon parameter space. Thus the singular family generically has **exactly one** forced relation, which already fits the rank-at-most-one budget allowed by AF-310 for a common nonzero rational-prime time. The universal alternative “`e_4=0` forces a second independent character relation” is false.

So the even singular set has two distinct layers that happened to coincide at six points: **recovery singularity** (`e_m=0` destroys the elementary phase formula) and **source inadmissibility** (the source orbit cannot meet that geometry). From eight points onward neither nontorsion geometry nor character-lattice rank supplies source inadmissibility by itself. The remaining eight-point gate is actual rational-prime/common-time incidence in the singular fiber, or a finer prime-log restriction stronger than exact integer-character rank.

After quotienting common rotation, the generic shape dimension remains `n-3`; AF-318 does not reopen generic identifiability. It instead proves that an exact ambient singular stratum can already satisfy the strongest elementary character-rank restriction. Any source exclusion must therefore use information that distinguishes the rational-prime orbit from a residual rank-one ambient family, while conditioning near `e_m=0` and observation access to `E` remain separate transport questions.

**Boundary.** AF-318 is residual only inside its antipodal-extension family and does not produce an eight-prime hit, quantify distance of the prime orbit from the singular set, or prove a rank-zero singular point. Exact recovery is still not stable recovery, and no RH consequence follows from ambient rank compatibility alone.
