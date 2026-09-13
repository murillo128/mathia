# MI-033 — Parity controls generic harmonic recovery; source structure repairs the eight-point singular fiber one harmonic later

**Evidence level:** exact for centered unit-circle multisets through [AF-316](../../findings/AF-316-parity-controls-minimal-harmonic-lift.md), with the higher-even-support singular boundary sharpened by [AF-317](../../findings/AF-317-antipodal-extension-recursion-breaks-six-point-singular-rigidity.md), [AF-318](../../findings/AF-318-antipodal-extension-has-residual-rank-one-character-lattice.md), and the eight-prime singular repair [AF-320](../../findings/AF-320-eight-prime-singular-recovery-is-repaired-by-the-fifth-harmonic.md). Rational-prime first incidence and stable conditioning remain separate.

Let `Z={z_1,...,z_n} subset S^1` satisfy `s_1=sum_j z_j=0`, write `s_r=sum_j z_j^r`, and let `E=prod_j z_j`. Newton identities recover the lower elementary symmetric coefficients from the low harmonics, while unit-circle roots impose

`e_(n-k) = E conjugate(e_k)`.

For odd support `n=2m+1`, no coefficient is self-paired. The lower block `(s_2,...,s_m)` is generically short by one real degree, and the missing degree is `E in S^1`; `(s_2,...,s_m,E)` recovers the unordered multiset globally and uses the generic `n-2` real dimensions. If one insists on harmonics only, `(s_2,...,s_(m+1))` recovers on `e_m != 0` with one exact real redundancy.

For even support `n=2m`, the middle coefficient is self-paired. On `e_m != 0`, its phase determines `E`, so `(s_2,...,s_m)` is already dimension-tight and recovers the unordered multiset. On `e_m=0` this phase-recovery step disappears; adding `E` always repairs exact recovery, but whether the source reaches that singular fiber and whether `E` itself can be reconstructed from nearby harmonics are separate questions.

The six-point case is exceptionally rigid and must not be generalized. There `e_3=0` forces the degree-six root polynomial to be even, hence three antipodal pairs; AF-310 makes that geometry incompatible with a nonzero common rational-prime time. AF-317 proves that this implication breaks at eight points by constructing exact centered nontorsion configurations with `e_4=0` that are not globally antipodally invariant. AF-318 closes the next source-independent escape: inside its explicit eight-point singular family, the normalized integer-character relation lattice is generically exactly rank one, already compatible with the AF-310 prime-phase rank budget.

AF-320 shows that the rational-prime source nevertheless supplies one further exact restriction. At a centered common-time configuration of eight distinct primes, `e_4=0` cannot also have `e_3=0`: that deeper degeneracy would make the root polynomial even and force four antipodal pairs, contradicting the prime-log character-rank restriction. Hence on every source-realizable middle-singular hit one has `e_3 != 0`. The fifth Newton identity and self-inversivity then give

`E = (6 s_5 - 5 s_2 s_3)/(10 conjugate(s_3))`.

Therefore `(s_2,s_3,s_4,s_5)` recovers the complete unordered eight-prime phase multiset **globally on the centered source class**: the generic branch uses the dimension-tight lower harmonics, while the fifth harmonic repairs the exceptional `e_4=0` branch. The singular fiber is not removed; its representation failure is repaired by source structure.

This separates three currencies that happened to coincide at small support: **generic recovery singularity**, **source admissibility of the singular fiber**, and **stable conditioning inside that fiber**. AF-320 settles exact representation on the eight-prime source class without settling whether a common-time hit with `s_1=0,e_4=0` exists. It also gives no quantitative lower bound on `|e_3|=|s_3|/3`, so the repaired formula may be badly conditioned near the deeper forbidden stratum even though exact failure is impossible.

After quotienting common rotation, the generic shape dimension remains `n-3`. The durable lesson is not that one should keep adding harmonics indiscriminately, but that the minimal observation bill can jump on a source-reachable exceptional stratum and then be repaired by a source-specific exclusion one level deeper.

**Boundary.** AF-320 does not prove first eight-prime incidence, exclude the middle-singular hit, provide a uniform separation from `s_3=0`, or establish an analogous one-extra-harmonic repair for every larger even support. Exact recovery is still not stable recovery, and no RH consequence follows from the eight-point reconstruction alone.
