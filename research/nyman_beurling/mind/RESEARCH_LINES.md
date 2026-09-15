# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Turn source-specific recurrence visibility into a quantitative target margin

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal` through `MI-022-actual-zero-counting-restores-recurrence-visibility-below-an-explicit-rank-threshold`.

NB-123--NB-125 give a genuine source-faithful separator on geometric grids: finite zero-power packets obey annihilating recurrences, and the missing harmonic root creates a positive target-angle margin when enough recurrence depth is visible. NB-126--NB-128 show that fixed finite phase systems alias globally, while the full natural prefix restores a quantitative local ordinate modulus inside a height window of size `Theta(R)`.

NB-129 supplies the amplitude splice and its sharp ambient barrier. At height `|T|~m`, target-bearing natural-grid phase visibility requires target-angle defect `O(1/|T|)`, and an endpoint-preserving matched sequence with only `Theta(1/m)` excess energy can erase the entire phase-sensitive block.

NB-130--NB-131 then show why finite recurrence and exact prefix data do not suffice for arbitrary formal packets. Rank-`R` formal zero powers can interpolate arbitrary values on `1,...,R`, and one invertible support shape can be translated to every height with only a unitary row modulation while its formal Burnol defect tends to zero.

NB-132 now separates that formal class from genuine zeta zeros in an explicit regime. For right-half-plane zeros in a fixed-width band `(T,T+W]` with `T+W<=R^A`, symmetry plus explicit zero counting gives

`d(F) <= A(W/(4 pi)+0.10076) log R + 0.24460 log log R + O_(A,W)(1)`.

Whenever `A(W/(4 pi)+0.10076)<1/log q`, this lies below the `q`-geometric recurrence-visibility budget, so the NB-124 annihilator is actually visible inside the natural cutoff. The formal linear-rank interpolation control is therefore not source-faithful in this polynomial-height/narrow-band regime.

The live theorem inside that regime is now quantitative conditioning: turn the visible recurrence into a lower bound on the missing-root margin relative to the weighted annihilator norm at the Burnol scale. Outside the regime, especially at superpolynomial height or growing ordinate width, rank visibility itself remains open.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, natural-prefix resolution, target angle, conditioning and provenance separate

NB-128 buys local phase stability by growing the observation prefix. NB-129 shows that target visibility still costs reciprocal-height amplitude accuracy. NB-130--NB-131 show that arbitrary formal rank can defeat finite-prefix and height-blind descriptors. NB-132 shows that actual-zero counting can restore rank visibility in a concrete source-faithful regime, but it does not produce a uniform Burnol-scale gap.

The surviving discriminator is therefore not simply “actual zeros versus formal powers.” One must state which source law limits effective rank, whether the observation prefix resolves that rank, and whether the resulting annihilator remains quantitatively conditioned strongly enough for the target scale.
