# MI-031 — Two low harmonics recover a five-point zero fiber, but not uniformly

**Evidence level:** exact for five unit-modulus points on the first-harmonic zero fiber through AF-313. The distinct-prime specialization is conditional on a hypothetical nonzero five-prime hit. No first-incidence theorem or uniform conditioning bound follows.

On `s_1=0`, unit-circle self-inversivity and Newton identities leave very little hidden freedom. Writing `s_m=sum_j z_j^m` and `E=prod_j z_j`, one has `e_2=-s_2/2`, `e_3=s_3/3`, and `e_3=E conjugate(e_2)`. Hence, whenever `s_2 != 0`,

`E = -2 s_3 / (3 conjugate(s_2))`,

so `(s_2,s_3)` determines the monic degree-five root polynomial and therefore the entire unordered phase multiset, with multiplicity. The only collision fiber is `s_2=s_3=0`, where the roots are exactly a rotated regular pentagon.

For phases `z_j=p_j^(-it)` from five distinct rational primes at one nonzero time, that exceptional pentagon is impossible: it would force two independent prime ratios to be fifth roots of unity and hence a forbidden multiplicative relation. Therefore, conditional on `F_P(t)=0`, the pair `(F_P(2t),F_P(3t))` exactly recovers `{p_j^(-it)}`.

The important distinction is **incidence versus post-incidence recoverability**. AF-312 showed that a hit cannot immediately recur at low harmonics; AF-313 shows more strongly that two of those surviving harmonics retain all phase information. Thus first-harmonic scalar cancellation does not irreversibly destroy the five-point geometry. But the recovery formula divides by `s_2`, so exact identifiability becomes arbitrarily ill-conditioned near the regular-pentagon orbit. Exact recovery therefore removes a secondary information-loss obstruction without supplying either a stable margin or the missing theorem deciding first nontorsion prime incidence.

**Boundary.** The statement is specific to five equal-weight unit-circle points with exact `s_1=0`. It does not assert minimality of the two-harmonic mark, stable recovery near `s_2=0`, existence of a five-prime hit, or any RH implication.