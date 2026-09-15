# MI-037 — Source-incidence cost is a redundancy/scale tradeoff, but generic code geometry can realize its coarse frontier

**Evidence level:** exact/literature-derived source-incidence consequence from [MC-312](../../findings/MC-312-generalized-hamming-source-redundancy-scale-tradeoff.md), sharpened by the generalized-weight/erasure boundary in [MC-313](../../findings/MC-313-generalized-griesmer-erasure-list-boundary.md), built on the source-cut theorem [MC-308](../../findings/MC-308-source-prime-cuts-force-quotient-occupancy.md) and classical generalized Hamming, Singleton, Griesmer and erasure-list theory.

MC-311 forces exponentially many Page-expensive endpoint directions, but it deliberately leaves open whether those directions can reuse one compact source package. MC-312 answers the first nonshareability question at the level of a **common representation code**.

Choose fixed lower-prime representatives for the `R` independent endpoint generators. Let `A` be their binary source-incidence matrix, `n` the number of distinct lower-prime coordinates in the union support and `Z` the largest such prime. The row space `C_A` is an `[n,R]` binary code. A `t`-dimensional subcode with generalized Hamming support `d_t` is exactly a high-rank source cut carried by `d_t` source coordinates.

MC-308 therefore gives the direct hierarchy bound

`d_t log Z >= (1-(2+o(1))(R+1)/2^t) log y - O(1)`

whenever the exponent is positive. Generalized Singleton then recovers MC-312's coarse tradeoff. With `t~2 log_2 R`,

`(n-R+O(log R)) log Z >= (1-o(1)) log y`.

If all source primes stay near the equal-share scale `y^(1/R)`, the package needs essentially another full rank of coordinates: `n>=2R-o(R)`. If the package keeps only `R+o(R)` coordinates, at least one source prime must move far above that scale.

MC-313 identifies the exact coding-theoretic boundary of this argument. The condition `d_t>s` is equivalent to adversarial erasure-list decodability from `s` erased source coordinates with ambiguity dimension at most `t-1`. At the live scale `t_R=ceil(2 log_2(R+1))`, the generalized Griesmer bound collapses **exactly** to generalized Singleton throughout every `n=O(R)` candidate, because `d_t<2^t-1`. Merely swapping in a stronger classical single-weight bound cannot increase the forced redundancy.

More importantly, generic code geometry actually matches the coarse source hierarchy. For all large `R` there are full-length binary `[2R,R]` codes with

`d_t > R-ceil(4R/t)`

simultaneously for `t_R<=t<=R/2`; in particular `d_(t_R)=R-O(R/log R)`. Thus rate-one-half binary codes can have essentially the erasure-list profile demanded by the current arithmetic inequality. The obstruction is no longer “generic codes cannot carry this much hereditary support.”

The reusable lesson is now two-layered. **Many expensive directions are not the same as expensive common support**, so the correct source accounting object is the hereditary support profile plus arithmetic coordinate scale. But once that profile is forced only to the current coarse order, **generic representation-code geometry is flexible enough to realize it**. The next coercive resource must distinguish arithmetic source-incidence matrices from generic binary codes.

This changes the live proof obligation. A closing theorem must exploit arithmetic realizability of the incidence columns, sharpen the source-scale inequality beyond the `O(R/log R)` generic control slack, couple several generalized weights in a way generic rate-one-half codes cannot match, or identify another source constraint absent from arbitrary binary codes. Recounting expensive directions, invoking a stronger classical bound at one generalized weight, or repeating the linear redundancy conclusion cannot close the endpoint.

**Boundary.** MC-313 does not construct an admissible arithmetic endpoint package. Its `[2R,R]` control has abstract binary columns, not lower-prime Legendre incidence columns. It also leaves open sharper second-order source-prime caps and joint hierarchy constraints. The theorem therefore kills a generic coding obstruction at the current precision; it does not show that the arithmetic source can realize the generic control or estimate `M(x)`.