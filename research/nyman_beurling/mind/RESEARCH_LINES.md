# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Separate actual-zero geometry from formal high-rank interpolation

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal` through `MI-021-linear-rank-formal-zero-powers-are-natural-prefix-universal`.

NB-123--NB-125 give a genuine source-faithful separator on geometric grids: finite zero-power packets obey annihilating recurrences, and the missing harmonic root creates a positive target-angle margin when enough recurrence depth is visible. NB-126--NB-128 then show that fixed finite phase systems alias globally, while the full natural prefix restores a quantitative local ordinate modulus inside a height window of size `Theta(R)`.

NB-129 supplies the amplitude splice and its sharp ambient barrier. At height `|T|~m`, target-bearing natural-grid phase visibility requires target-angle defect `O(1/|T|)`, and an endpoint-preserving matched sequence with only `Theta(1/m)` excess energy can erase the entire phase-sensitive block.

NB-130 closes the immediate appeal to finite recurrence or exponential-polynomial analyticity **by themselves**. For every prefix length `R`, arbitrary values on `1,...,R` are interpolated exactly by `R` distinct formal zero powers with common real part in `(1/2,1)`, arbitrarily high ordinate, and ordinates confined to an arbitrarily short interval. The interpolant still satisfies a genuine degree-`R` recurrence; the issue is that only `O(log R)` geometric samples lie below the natural cutoff, so the recurrence has no leverage at linear rank.

NB-131 closes the remaining fixed-height loophole. Once one such support shape is invertible, translating it vertically multiplies the prefix evaluation matrix only by a unitary row phase. The same prefix is therefore reinterpolated **exactly at every height** with no additional height-dependent condition-number cost, while the formal finite-packet Burnol defect tends to zero like `S^-2`. Along simultaneous phase returns, even the re-solved coefficients and any fixed collection of periodic recurrence observables return to their initial values. Exact finite-prefix equality plus height-blind finite descriptors therefore cannot certify positive Burnol mass in the formal packet class.

The live theorem must distinguish the **actual zeta-zero packet** from this formal interpolation class quantitatively. Viable inputs are actual zero locations/counting/spacing, a rank bound relative to visible prefix depth, or coefficient/model-space conditioning uniform in the growing cutoff. Generic analyticity, high ordinate, narrow ordinate support, finite recurrence, exact fixed-prefix data and finite periodic recurrence descriptors are no longer source separators without such a quantitative law.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, natural-prefix resolution, target angle, conditioning and provenance separate

NB-128 buys local phase stability by growing the observation prefix. NB-129 shows that target visibility still costs reciprocal-height amplitude accuracy. NB-130 shows that recurrence/analyticity impose no finite-prefix restriction once model rank is allowed to grow linearly with the prefix. NB-131 then shows that absolute support height itself is not the missing conditioning resource: vertical translation is unitary on the natural-prefix rows and can drive formal Burnol mass to zero while keeping the prefix exact.

The surviving discriminator is therefore whether **actual-zero geometry keeps the effective rank and conditioning inside the regime where recurrence/model-space structure is visible to the target**. The bad conditioning may grow with `R` or narrow internal spacing, and actual zeta zeros cannot be translated freely; those are genuine source-specific gates rather than technical nuisances.
