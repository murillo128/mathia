# MI-035 — Fixed-prime conditioning has zero uniform gap but a polynomial finite-height modulus

**Evidence level:** supported by AF-320--AF-322 for a fixed support of eight distinct rational primes. No exact middle-singular incidence theorem or support-uniform exponent is claimed.

AF-320 separates exact recovery from generic dimension counting: on the centered eight-prime branch `s_1=e_4=0`, the deeper denominator failure `s_3=0` would force four antipodal pairs, which prime-log arithmetic excludes exactly. AF-321 then shows why this is not yet stable recovery. Rank-one matched controls can approach the regular-octagon closure with `s_3 -> 0`, so relation rank by itself supplies no positive conditioning margin.

AF-322 identifies the missing quantitative layer for the **actual fixed prime orbit**. Baker-type lower bounds prevent the orbit from approaching the four-antipodal-pair set faster than a fixed power of its time height, while Kronecker recurrence still makes the infimum distance zero at arbitrarily large times. Łojasiewicz transfer on the middle-singular semialgebraic set then yields, conditional on an exact hit, a polynomial lower bound

`|s_3(Z_P(t))| >= c_P (1+|t|)^(-K_P)`.

Thus the right stability currency is neither a uniform gap nor exact nonincidence alone. A fixed arithmetic source can have **zero asymptotic margin and still possess an effective finite-height exclusion modulus**. That modulus is enough to bound the deterioration of the AF-320 inverse polynomially in height, but it says nothing about whether the middle-singular branch is ever hit.

The remaining questions split cleanly. First decide exact prime-source incidence of `s_1=e_4=0`. If hits exist, determine whether the polynomial modulus is strong enough in the downstream metric. If the support grows, prove a support-uniform version or account explicitly for the degeneration of the Baker/Łojasiewicz constants.

**Boundary.** The result is fixed-support and conditional on the middle-singular event when transferred to `s_3`. Kronecker recurrence concerns approach to the antipodal geometry, not a sequence of exact middle-singular hits. Exact incidence, finite-height conditioning and growing-support uniformity remain distinct.