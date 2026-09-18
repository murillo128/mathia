# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation threshold

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-032-positive-half-sobolev-energy-overcoerces-reciprocal-prime-mertens-shells`.

Prime-extension energy is the exact source-side relation currency. For a squarefree-supported source `a`, with `delta=a-mu`, the quantities `D_(a,q)` and `M_(a,q)` measure coefficient displacement and prime-extension inconsistency. FD-187--FD-188 show that on the physical-prime fibre, subcritical relation energy plus sublinear coefficient mass forces `a=mu`; source-side arithmetic rigidity is therefore available once the observation exposes those currencies.

FD-189--FD-194 make the dyadic signed-Fourier observation threshold exact. At a geometric horizon `H=B^m`, modes through `k<=c sqrt(H)` cover every sufficiently large source coordinate exactly when `c>=sqrt(B)`. For dyadic horizons the sharp constant is `sqrt(2)`. Below that constant there are permanent quotient holes; at and above it there is an explicit cumulative inverse.

FD-191 closes the formerly open power endpoint under strong coordinatewise Möbius fidelity: at `alpha=1/2`, dyadic Fourier bands still admit exact null perturbations on composite squarefree coordinates even when all primes and all nonsquarefree coordinates are fixed. Together with FD-190, every `alpha<=1/2` remains noninjective in that class. FD-192 strengthens the consequence: such square-root-and-below nulls can hide order-one coefficient discrepancies and critical prime-extension energy of order `x/log x`. Coordinatewise fidelity alone therefore cannot recover the relation currency needed by FD-187--FD-188.

FD-193--FD-194 provide the complementary positive theorem. For geometric horizons, `c>=sqrt(B)` is not merely a coverage condition: the cumulative source has an explicit inverse with uniform error control. Under raw Fourier `l_infinity` noise, cumulative reconstruction has amplification at most one and coefficient increments at most two; below the threshold no inverse exists. The square-root transition is therefore a geometry/injectivity threshold rather than a conditioning pathology.

FD-195 adds a topology-sensitive warning at exactly this point. For the classical Franel/GCD quadratic energy, the dual cost of one geometric quotient witness is `C_(H,k)=Theta(1)`, even though the raw signed-Fourier inverse row for the same witness contracts like `2^omega(k)/k=n^(-1+o(1))`. Stable coordinate recovery and scalar quadratic-energy duality therefore price the same source direction differently. At the geometric horizon `H~n^2`, generic one-horizon Franel duality reaches only the `M(n)=O(n^(1+epsilon))` scale; square-root Mertens would require substantially stronger Franel energy than the RH-equivalent bound supplies.

FD-196 makes that loss exact across the weighted Fourier family `E_(H,sigma)`: a square-root band with energy exponent `gamma` recovers `M(n)=O(n^(gamma+sigma-1+epsilon))`, so the RH-facing line is `gamma+sigma<=3/2`. Classical Franel transfer stays on `gamma+sigma=2` for every `0<=sigma<=1`; changing Sobolev weight alone never recovers the missing half power.

FD-197 shows that the same noncritical line is the exact logarithmic second-moment baseline of a squarefree Rademacher random multiplicative source. On `K~sqrt(H)`, `E E_(H,sigma)^f(K)=H^(2-sigma+o(1))`; in particular the half-Sobolev energy has mean `H^(3/2+o(1))`, not the `H^(1+epsilon)` needed by the FD-196 recovery theorem.

FD-198 sharpens the interpretation of that missing half power. For primes `K/2<p<=K`, the exact centered row identity

`B_H(p)-B_H(1)=p M(floor(H/p))`

puts `Theta(K/log K)` distinct Mertens samples of size `Theta(K)` inside the same positive half-Sobolev budget. If `E_(H,1/2)(K)=H^(gamma+o(1))`, their RMS is `<<K^(gamma-1+o(1))`. Thus the FD-196 critical budget `H^(1+epsilon)` would force subpower RMS on the whole reciprocal-prime shell, whereas the FD-197 random-multiplicative baseline `gamma=3/2` gives the natural square-root RMS. The positive energy is therefore not merely lossy relative to raw inversion: at the RH-facing exponent it is simultaneously much more coercive than the pointwise RH target on a growing sparse family.

The live question has moved away from endpoint injectivity, generic one-horizon scalar duality and random-sign multiplicativity heuristics. A plausible route should expose deterministic Möbius-specific signed coherence, a cross-mode/cross-horizon statistic, or another destination quantity that retains the contractive divisor inverse **without requiring uniform positive suppression of the entire reciprocal-prime shell to subpower RMS**. A proposal that only strengthens the same positive half-Sobolev norm now has to explain why this stronger simultaneous consequence is a natural RH-level theorem rather than an avoidable overcoercive surrogate.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. Above the geometric square-root constant, stable cumulative inversion is available; below it, exact null directions remain. FD-195--FD-198 show that even above threshold the contraction visible in the raw coordinate inverse need not survive compression to quadratic Farey energy, and that the critical positive half-Sobolev budget would simultaneously overcontrol a reciprocal-prime Mertens shell.

Sample count and algebraic injectivity are not the invariants. What matters is quotient coverage, which cross-coordinate relations the source class forces, the source covariance beyond generic multiplicativity, whether the destination norm preserves sign/cross-mode structure, and what simultaneous family of source coordinates that norm controls.

Any lower bound should therefore declare whether it concerns unrestricted recovery, one-target testing, pairwise recovery or quotient recovery; the source class and relation graph; the observation/noise topology; and whether support count, weighted amplitude, relation energy, scale coverage, covariance structure or quadratic-energy dual cost is the relevant currency. Only then do bandwidth, rank or inverse modulus have mathematical meaning.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root threshold still does not prove the RH-critical discrepancy estimate. Conversely, FD-187--FD-188 say what a relation-sensitive observation would have to expose: enough control of `D_q` and `M_q` to force the Möbius source without reconstructing every coordinate. FD-195--FD-198 rule out treating the scalar Franel energy, a Sobolev reweighting, generic random multiplicativity or one-row dual recovery as a lossless proxy for the contractive raw inverse on geometric quotient witnesses.

The high-value frontier is therefore a deterministic Möbius-specific suppression mechanism with a credible simultaneous interpretation, a signed destination-relevant relation statistic, or cross-horizon structure. A wider positive band is not progress by itself: its source consequences must be audited collectively, not one recovered coordinate at a time.