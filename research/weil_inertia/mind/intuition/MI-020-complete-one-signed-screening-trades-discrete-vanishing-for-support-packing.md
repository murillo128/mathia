# MI-020 — Complete one-signed screening reaches the log-2 packing ceiling even with all prime lags and full span

**Evidence level:** exact on the relaxed one-signed first-crossing class isolated by [WI-281](../../findings/WI-281-complete-one-signed-prime-screening-forces-log2-support-packing-and-a-smaller-archimedean-budget.md) and sharpened by [WI-282](../../findings/WI-282-complete-prime-screening-and-full-span-do-not-lower-the-log2-packing-budget.md). No theorem that the first null mode is one-signed, no exact-null-equation realization, and no RH consequence is claimed.

WI-281 shows that if a hypothetical first null mode satisfies `v>=0` and all active prime-power autocorrelations vanish, the powers of two already force its positive set to be a measurable selector modulo `L=log 2`. Hence `|{v>0}|<=L`, and Riesz rearrangement lowers the positive archimedean budget from the unrestricted `K_+` to

`K_pack=(1/2) lambda_max(T_L)<K_+`.

WI-282 identifies the exact limit of this support-packing mechanism. Every positive von-Mangoldt lag is at least `log 2`, so the top eigenfunction on one interval of length `L` already screens **all** prime-power lags, not only powers of two. Therefore complete prime-power screening has exact relaxed supremum `K_pack`.

Qualitative first-crossing full span does not lower that supremum either. One can truncate the interval optimizer, add arbitrarily small boundary satellites reaching both aperture endpoints, and remove the finitely many core points that create active forbidden distances. The resulting nonnegative profiles screen every active prime-power lag, have full essential span, and converge in `L^2` to the `K_pack` optimizer. Thus no uniform gap

`B_+(f) <= K_pack-c(a)`

can follow from nonnegativity, normalization, complete screening and full essential span alone.

The source-specific bootstrap has therefore reached a precise relaxation boundary. “Use the other primes” and “use full span” are closed as standalone scalar refinements. Any strict improvement must use information excluded by the relaxation: the exact null equation `A_a v=0`, quantitative mass in separated regions, nodal/regularity constraints, balance between archimedean and prime source terms, a first-crossing spectral-area margin, or a simultaneous-cut identity coupling more than the zero set of autocorrelations.

The durable point is that a source constraint can shrink the continuous admissible class without shrinking it enough. Once the relaxed class contains profiles arbitrarily close to the packing extremizer, adding more constraints that are already satisfied by those profiles cannot improve the budget. The next theorem has to distinguish actual null modes from those relaxed near-extremizers.

**Boundary.** The sharpness construction is not a Suzuki null mode and says nothing about the sign-changing branch. The full-span satellites may carry vanishing mass, so a *quantitative* two-sided mass condition could still lower the budget.