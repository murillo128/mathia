# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation threshold

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-031-franel-energy-duality-loses-geometric-tail-contraction`.

Prime-extension energy is the exact source-side relation currency. For a squarefree-supported source `a`, with `delta=a-mu`, the quantities `D_(a,q)` and `M_(a,q)` measure coefficient displacement and prime-extension inconsistency. FD-187--FD-188 show that on the physical-prime fibre, subcritical relation energy plus sublinear coefficient mass forces `a=mu`; source-side arithmetic rigidity is therefore available once the observation exposes those currencies.

FD-189--FD-194 make the dyadic signed-Fourier observation threshold exact. At a geometric horizon `H=B^m`, modes through `k<=c sqrt(H)` cover every sufficiently large source coordinate exactly when `c>=sqrt(B)`. For dyadic horizons the sharp constant is `sqrt(2)`. Below that constant there are permanent quotient holes; at and above it there is an explicit cumulative inverse.

FD-191 closes the formerly open power endpoint under strong coordinatewise Möbius fidelity: at `alpha=1/2`, dyadic Fourier bands still admit exact null perturbations on composite squarefree coordinates even when all primes and all nonsquarefree coordinates are fixed. Together with FD-190, every `alpha<=1/2` remains noninjective in that class. FD-192 strengthens the consequence: such square-root-and-below nulls can hide order-one coefficient discrepancies and critical prime-extension energy of order `x/log x`. Coordinatewise fidelity alone therefore cannot recover the relation currency needed by FD-187--FD-188.

FD-193--FD-194 provide the complementary positive theorem. For geometric horizons, `c>=sqrt(B)` is not merely a coverage condition: the cumulative source has an explicit inverse with uniform error control. Under raw Fourier `l_infinity` noise, cumulative reconstruction has amplification at most one and coefficient increments at most two; below the threshold no inverse exists. The square-root transition is therefore a geometry/injectivity threshold rather than a conditioning pathology.

FD-195 adds a topology-sensitive warning at exactly this point. For the classical Franel/GCD quadratic energy, the dual cost of one geometric quotient witness is `C_(H,k)=Theta(1)`, even though the raw signed-Fourier inverse row for the same witness contracts like `2^omega(k)/k=n^(-1+o(1))`. Stable coordinate recovery and scalar quadratic-energy duality therefore price the same source direction differently. At the geometric horizon `H~n^2`, generic one-horizon Franel duality reaches only the `M(n)=O(n^(1+epsilon))` scale; square-root Mertens would require substantially stronger Franel energy than the RH-equivalent bound supplies.

The live question has moved away from endpoint injectivity and generic one-horizon scalar duality. The next useful observation must either be genuinely thinner than the complete square-root band while exposing cross-coordinate arithmetic relations, exploit multiplicativity/divisor compatibility so that the source class couples unsampled quotient coordinates, or use a cross-horizon/source-dependent statistic whose destination norm retains the raw inverse contraction. A proposal that only adds coordinatewise prime/Möbius fidelity or applies Cauchy--Schwarz to one Franel energy is already classified.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. Above the geometric square-root constant, stable cumulative inversion is available; below it, exact null directions remain. FD-195 now shows that even above threshold the contraction visible in the raw coordinate inverse need not survive compression to the Franel Hilbert geometry. Sample count and algebraic injectivity are not the invariants. What matters is quotient coverage, which cross-coordinate relations the source class forces, and the dual norm in which the destination asks to recover them.

Any lower bound should therefore declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; the source class and relation graph; the observation/noise topology; and whether support count, weighted amplitude, relation energy, scale coverage or quadratic-energy dual cost is the relevant currency. Only then do bandwidth, rank or inverse modulus have mathematical meaning.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root threshold still does not prove the RH-critical discrepancy estimate. Conversely, FD-187--FD-188 say what a relation-sensitive observation would have to expose: enough control of `D_q` and `M_q` to force the Möbius source without reconstructing every coordinate. FD-195 rules out treating the scalar Franel energy as a lossless proxy for the contractive raw inverse on geometric quotient witnesses. The high-value frontier is therefore a destination-relevant relation statistic or cross-horizon structure, not a wider version of a band that is already classified exactly.
