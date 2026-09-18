# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation threshold

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-030-sub-square-root-farey-bands-remain-noninjective-under-coordinatewise-mobius-fidelity`.

Prime-extension energy is the exact source-side relation currency. For a squarefree-supported source `a`, with `delta=a-mu`, the quantities `D_(a,q)` and `M_(a,q)` measure coefficient displacement and prime-extension inconsistency. FD-187--FD-188 show that on the physical-prime fibre, subcritical relation energy plus sublinear coefficient mass forces `a=mu`; source-side arithmetic rigidity is therefore available once the observation exposes those currencies.

FD-189--FD-194 now make the dyadic signed-Fourier observation threshold exact. At a geometric horizon `H=B^m`, modes through `k<=c sqrt(H)` cover every sufficiently large source coordinate exactly when `c>=sqrt(B)`. For dyadic horizons the sharp constant is `sqrt(2)`. Below that constant there are permanent quotient holes; at and above it there is an explicit cumulative inverse.

FD-191 closes the formerly open power endpoint under strong coordinatewise Möbius fidelity: at `alpha=1/2`, dyadic Fourier bands still admit exact null perturbations on composite squarefree coordinates even when all primes and all nonsquarefree coordinates are fixed. Together with FD-190, every `alpha<=1/2` remains noninjective in that class. FD-192 strengthens the consequence: such square-root-and-below nulls can hide order-one coefficient discrepancies and critical prime-extension energy of order `x/log x`. Coordinatewise fidelity alone therefore cannot recover the relation currency needed by FD-187--FD-188.

FD-193--FD-194 provide the complementary positive theorem. For geometric horizons, `c>=sqrt(B)` is not merely a coverage condition: the cumulative source has an explicit inverse with uniform error control. Under raw Fourier `l_infinity` noise, cumulative reconstruction has amplification at most one and coefficient increments at most two; below the threshold no inverse exists. The square-root transition is therefore a geometry/injectivity threshold rather than a conditioning pathology.

The live question has moved away from endpoint injectivity. The next useful observation must either be genuinely thinner than the complete square-root band while exposing cross-coordinate arithmetic relations, or exploit multiplicativity/divisor compatibility so that the source class couples the unsampled quotient coordinates. A proposal that only adds coordinatewise prime/Möbius fidelity is already ruled out by FD-191--FD-192.

## Apply information budgets only after fixing source class, observation family and destination

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class and observation family. The new exact threshold makes the audit sharper: above the geometric square-root constant, stable cumulative inversion is available; below it, exact null directions remain. Sample count is not the invariant. What matters is the quotient coverage of source indices and which cross-coordinate relations the admissible class forces between covered and uncovered coordinates.

Any lower bound should therefore declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; the source class and relation graph; the observation/noise topology; and whether support count, weighted amplitude, relation energy or scale coverage is the relevant currency. Only then do bandwidth, rank or inverse modulus have mathematical meaning.

## Keep source coercivity and the Franel--Landau destination separate

Stable source recovery above the square-root threshold still does not prove the RH-critical discrepancy estimate. Conversely, FD-187--FD-188 say what a relation-sensitive observation would have to expose: enough control of `D_q` and `M_q` to force the Möbius source without reconstructing every coordinate. The high-value frontier is therefore a destination-relevant relation statistic, not a wider version of a band that is now already classified exactly.
