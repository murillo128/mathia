# MI-033 — Parity controls generic harmonic recovery; source repair can be exact without being stable

**Evidence level:** exact for centered unit-circle multisets through [AF-316](../../findings/AF-316-parity-controls-minimal-harmonic-lift.md), with the higher-even-support singular boundary sharpened by [AF-317](../../findings/AF-317-antipodal-extension-recursion-breaks-six-point-singular-rigidity.md), [AF-318](../../findings/AF-318-antipodal-extension-has-residual-rank-one-character-lattice.md), the eight-prime exact repair [AF-320](../../findings/AF-320-eight-prime-singular-recovery-is-repaired-by-the-fifth-harmonic.md), and the conditioning obstruction [AF-321](../../findings/AF-321-rank-one-eight-point-singular-recovery-has-no-uniform-harmonic-conditioning.md). Rational-prime first incidence and any stronger source-specific stability theorem remain separate.

Let `Z={z_1,...,z_n} subset S^1` satisfy `s_1=sum_j z_j=0`, write `s_r=sum_j z_j^r`, and let `E=prod_j z_j`. Newton identities recover the lower elementary symmetric coefficients from the low harmonics, while unit-circle roots impose

`e_(n-k) = E conjugate(e_k)`.

For odd support `n=2m+1`, no coefficient is self-paired. The lower block `(s_2,...,s_m)` is generically short by one real degree, and the missing degree is `E in S^1`; `(s_2,...,s_m,E)` recovers the unordered multiset globally and uses the generic `n-2` real dimensions. If one insists on harmonics only, `(s_2,...,s_(m+1))` recovers on `e_m != 0` with one exact real redundancy.

For even support `n=2m`, the middle coefficient is self-paired. On `e_m != 0`, its phase determines `E`, so `(s_2,...,s_m)` is dimension-tight and recovers the unordered multiset. On `e_m=0` that phase formula disappears; source information or an extra mark is needed to recover the missing product phase.

The six-point case is exceptionally rigid. There `e_3=0` forces three antipodal pairs and is incompatible with a nonzero common rational-prime time. At eight points this ambient implication fails: AF-317 constructs nontorsion centered configurations with `e_4=0`, and AF-318 shows a dense residual part of that singular family already has normalized character-relation rank exactly one.

AF-320 nevertheless proves an exact **source repair** on the rational-prime eight-point class. A centered common-time hit with `e_4=0` cannot also have `e_3=0`; otherwise four antipodal pairs would violate the prime-log relation-rank restriction. Hence `s_3!=0`, and the fifth Newton identity gives

`E = (6 s_5 - 5 s_2 s_3)/(10 conjugate(s_3))`.

Thus `(s_2,s_3,s_4,s_5)` exactly recovers every centered eight-prime configuration even though the middle-singular event itself is not excluded.

AF-321 shows why this exact repair must not be read as stable compression. Inside the same rank-one middle-singular control class there are configurations approaching a regular octagon with `s_3->0`. The retained vector `(s_2,s_3,s_4,s_5)` tends to zero while the product phase can remain macroscopically separated under common rotation, so the exact inverse is not uniformly continuous. The closure fiber over zero carries all `E in S^1`. On that boundary `s_1,...,s_7` vanish and `s_8=-8E`, making the eighth harmonic the first power-sum separator of this particular lost phase.

The durable hierarchy is therefore four-way: **generic information dimension, exact exceptional-fiber repair, source incidence, and quantitative conditioning are distinct resources**. A discrete source invariant can forbid the exact denominator zero and still give zero distance from that forbidden stratum. Stable recovery requires either finer quantitative source separation or a retained mark whose target sensitivity survives on the closure fiber.

**Boundary.** AF-321's approaching rank-one controls need not themselves lie on one fixed rational-prime common-time orbit. It proves that character rank alone has no conditioning margin, not that the full prime source is unstable. AF-320--AF-321 do not decide first eight-prime incidence, give a Diophantine lower bound on `|s_3|`, prove `s_8` globally minimal among arbitrary observables, or establish the same one-extra-harmonic repair at every larger even support.