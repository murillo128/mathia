# MI-037 — Support height and time height control the whole retained Gram boundary

**Evidence level:** supported by [AF-324](../../findings/AF-324-bounded-prime-height-quantifies-fixed-time-phase-covering.md), [AF-325](../../findings/AF-325-bounded-support-height-uniformizes-prime-antipodal-conditioning.md), [AF-326](../../findings/AF-326-toeplitz-moment-positivity-couples-singular-second-and-third-harmonics.md) and [AF-327](../../findings/AF-327-prime-height-time-separates-lacunary-moment-gram-boundary.md). No exact middle-singular incidence theorem or downstream sufficiency theorem is claimed.

The conditioning picture now has a source modulus and a destination boundary certificate on the same finite-resource scale. AF-324 shows that bounded prime supports still become dense in finite phase space as the support cap `H` grows. AF-325 gives the complementary finite-height exclusion: for eight primes `p_j<=H` and `|t|>=1`, the prime phase orbit stays a quantitatively controlled distance from the four-antipodal-pair singularity, with a Baker--Wüstholz envelope of the form

`exp[-C (log H)^2 log(e+|t| log H)]`.

AF-326 transferred that source separation, conditional on the centered middle-singular incidence, into one retained coordinate through

`4-|s_2| >= |s_3|^2/64`.

AF-327 strengthens the destination statement. For the retained monomials `{1,z,z^2,z^4}`, let `G_0124` be the normalized moment Gram and `D_0124=det G_0124`. Cauchy--Binet expresses `D_0124` as a sum of nonnegative four-subset certificates. Rank loss forces at most four distinct phases, hence two disjoint collisions; the prime phase relation lattice excludes that geometry at every nonzero common time. Therefore

`D_0124(Z_P(t))>0`,

and the same height/time arithmetic separation plus a semialgebraic Łojasiewicz inequality gives

`D_0124(Z_P(t)) >= exp[-C (log H)^2 log(e+|t| log H)]`.

Because `trace G_0124=4`, this also lower-bounds `lambda_min(G_0124)` up to an absolute factor. The source margin therefore reaches the **whole four-feature rank boundary**, not only the recovery denominator `|s_3|` or the extremal face seen by `|s_2|`.

On the hypothetical stratum `s_1=e_4=0`, the exact identity

`4096 D_0124 = 8(16-|s_2|^2)(32+|s_2|^2) - (64-|s_2|^2)|s_3|^2`

shows precisely which curved equality face is excluded at finite `H,t`. This is stronger than saying that a coordinate remains nonzero: it gives a target-native slack with an operator-conditioning interpretation.

The remaining gate is not generic stability. Exact incidence of `s_1=e_4=0` is still undecided, and even a positive Gram margin helps only if the downstream theorem consumes this retained four-feature geometry at a compatible quantitative scale. Support height, observation time, incidence and destination slack must therefore remain separate currencies.

**Boundary.** The exponent in AF-327 is structural rather than sharp; `D_0124>0` does not imply exact middle-singular incidence or complete prime recovery; and the condition-number consequence concerns only the retained four-feature Gram.