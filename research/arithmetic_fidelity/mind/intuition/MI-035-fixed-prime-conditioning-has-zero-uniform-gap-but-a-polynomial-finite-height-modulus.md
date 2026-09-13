# MI-035 — Fixed-prime conditioning has zero uniform gap but a polynomial finite-height modulus

**Evidence level:** supported by AF-320--AF-323. The polynomial modulus is a fixed-support statement; AF-323 proves that no positive phase-separation modulus depending only on time can hold uniformly over unrestricted varying prime supports. No exact middle-singular incidence theorem is claimed.

AF-320 separates exact recovery from generic dimension counting: on the centered eight-prime branch `s_1=e_4=0`, the deeper denominator failure `s_3=0` would force four antipodal pairs, which prime-log arithmetic excludes exactly. AF-321 then shows why this is not yet stable recovery. Rank-one matched controls can approach the regular-octagon closure with `s_3 -> 0`, so relation rank by itself supplies no positive conditioning margin.

AF-322 identifies the quantitative layer for the **actual fixed prime orbit**. Baker-type lower bounds prevent that orbit from approaching the four-antipodal-pair set faster than a fixed power of the time height, while Kronecker recurrence still makes the infimum distance zero at arbitrarily large times. Łojasiewicz transfer on the middle-singular semialgebraic set then yields, conditional on an exact hit, a polynomial lower bound

`|s_3(Z_P(t))| >= c_P (1+|t|)^(-K_P)`.

Thus one fixed arithmetic source can have **zero asymptotic margin and still possess an effective finite-height exclusion modulus**. That modulus bounds deterioration of the AF-320 inverse polynomially in height, but it does not decide whether the middle-singular branch is ever hit.

AF-323 shows that the support dependence of `c_P,K_P` is structural rather than merely a weakness of the Baker estimate. Fix any `tau!=0`. Because successive `log p` gaps tend to zero, the prime phases `{p^{-i tau}}` are tail-dense in `S^1`; choosing distinct primes coordinatewise makes the union of `m`-prime support configurations tail-dense in `(S^1)^m`. For `m=8`, actual prime supports therefore approach the four-antipodal-pair locus, and even the regular-octagon collision, arbitrarily closely at that single fixed time. Consequently

`inf_P dist(Z_P(tau),A_8)=0`,

with the infimum unchanged after imposing any lower cutoff on the selected primes. No support-independent positive modulus depending only on `|t|` can survive unrestricted support variation.

The remaining questions split cleanly. Exact prime-source incidence of `s_1=e_4=0` is still open. On any fixed support that does hit, ask whether the AF-322 polynomial modulus is strong enough in the downstream metric. Across changing supports, a meaningful uniform theorem must retain an additional source resource—such as a restricted support family or an explicit support-height/provenance parameter—because phase data plus time height alone cannot separate the prime source from the ambient failure geometry.

**Boundary.** AF-323 is a support-union closure theorem at fixed nonzero time; it does not contradict AF-322's fixed-support Diophantine lower bound, imply equidistribution, or produce an exact middle-singular prime hit. Exact incidence, fixed-support finite-height conditioning and support-union topology are distinct.