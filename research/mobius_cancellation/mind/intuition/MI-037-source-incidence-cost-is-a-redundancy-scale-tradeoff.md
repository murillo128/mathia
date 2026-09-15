# MI-037 — Source-incidence cost is a redundancy/scale tradeoff, not direction cardinality

**Evidence level:** exact/literature-derived source-incidence consequence from [MC-312](../../findings/MC-312-generalized-hamming-source-redundancy-scale-tradeoff.md), built on the source-cut theorem [MC-308](../../findings/MC-308-source-prime-cuts-force-quotient-occupancy.md) and classical generalized Hamming/Singleton theory.

MC-311 forces exponentially many Page-expensive endpoint directions, but it deliberately leaves open whether those directions can reuse one compact source package. MC-312 answers the first nonshareability question at the level of a **common representation code**.

Choose any fixed lower-prime representatives for the `R` independent endpoint generators. Let `A` be their binary source-incidence matrix, `n` the number of distinct lower-prime coordinates in the union support and `Z` the largest such prime. The row space `C_A` is an `[n,R]` binary code. A `t`-dimensional subcode with small generalized Hamming support is exactly a high-rank source cut: all its endpoint combinations are carried by that small set of source primes.

Generalized Singleton guarantees a `t`-dimensional subcode supported on at most `n-R+t` coordinates. Feeding that support into the exact MC-308 quotient-occupancy bound gives

`(n-R+t) log Z >= (1-(2+o(1))(R+1)/2^t) log y - O(1)`.

Choosing `t~2 log_2 R` makes the right side `(1-o(1))log y`, hence

`(n-R+O(log R)) log Z >= (1-o(1)) log y`.

This is the first source resource in the current endpoint program that cannot be shared away merely by reusing the same representatives. If all source primes stay near the equal-share scale `y^(1/R)`, then the package needs essentially another full rank of distinct coordinates: `n>=2R-o(R)`. If the package keeps only `R+o(R)` coordinates, at least one source prime must move far above that scale. The Page-scale specialization likewise forces linear redundancy in the reciprocal regime.

The reusable lesson is **many expensive directions are not the same thing as expensive common support, but generalized support geometry can force a dichotomy between support redundancy and coordinate scale**. The correct source accounting object is not the number of endpoint functionals; it is the hereditary support profile of the representation code together with the arithmetic size of the coordinates in that support.

This changes the live proof obligation. It is no longer enough to ask whether Page-expensive directions overlap. They may overlap, but overlap itself is now priced. A closing theorem must show that the endpoint cannot tolerate either branch of the tradeoff: too many distinct source coordinates or a much larger source-prime scale. Conversely, an arithmetic matched control that realizes one branch while preserving the bad endpoint would identify the next missing resource.

**Boundary.** The theorem applies to any fixed common representative package for the exact one-defect endpoint, but different representative choices can change `n`, `Z` and the code. It does not prove an optimal package, add source costs across directions, estimate `M(x)`, or exclude high redundancy/large source primes. Generalized Hamming theory supplies the support compression; the arithmetic cost still comes from the MC-308 source-cut theorem.