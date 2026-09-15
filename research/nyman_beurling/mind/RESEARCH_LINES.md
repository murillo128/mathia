# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Separate actual-zero geometry from formal high-rank interpolation

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal` through `MI-021-linear-rank-formal-zero-powers-are-natural-prefix-universal`.

NB-123--NB-125 give a genuine source-faithful separator on geometric grids: finite zero-power packets obey annihilating recurrences, and the missing harmonic root creates a positive target-angle margin when enough recurrence depth is visible. NB-126--NB-128 then show that fixed finite phase systems alias globally, while the full natural prefix restores a quantitative local ordinate modulus inside a height window of size `Theta(R)`.

NB-129 supplies the amplitude splice and its sharp ambient barrier. At height `|T|~m`, target-bearing natural-grid phase visibility requires target-angle defect `O(1/|T|)`, and an endpoint-preserving matched sequence with only `Theta(1/m)` excess energy can erase the entire phase-sensitive block.

NB-130 now closes the immediate appeal to finite recurrence or exponential-polynomial analyticity **by themselves**. For every prefix length `R`, arbitrary values on `1,...,R` are interpolated exactly by `R` distinct formal zero powers with common real part in `(1/2,1)`, arbitrarily high ordinate, and ordinates confined to an arbitrarily short interval. The interpolant still satisfies a genuine degree-`R` recurrence; the issue is that only `O(log R)` geometric samples lie below the natural cutoff, so the recurrence has no leverage at linear rank.

The live theorem must therefore distinguish the **actual zeta-zero packet** from this formal interpolation class quantitatively. Viable inputs are actual zero locations/counting/spacing, a rank bound relative to visible prefix depth, model-space/Gram conditioning, or coefficient control strong enough to prevent near-confluent Vandermonde interpolation. Generic analyticity, high ordinate, narrow ordinate support and finite recurrence are no longer source separators without such a quantitative law.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, natural-prefix resolution, target angle and conditioning separate

NB-128 buys local phase stability by growing the observation prefix. NB-129 shows that target visibility still costs reciprocal-height amplitude accuracy. NB-130 shows that recurrence/analyticity impose no finite-prefix restriction once model rank is allowed to grow linearly with the prefix: the formal class becomes exactly universal.

The surviving discriminator is therefore not “zero powers obey a recurrence.” It is whether **actual-zero geometry keeps the effective rank and conditioning inside the regime where that recurrence or model-space structure is visible to the target**. NB-130 deliberately provides no uniform coefficient norm; the exploding Vandermonde conditioning is a remaining source-specific gate, not a technical nuisance.