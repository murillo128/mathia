# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Turn source-specific recurrence visibility into a quantitatively conditioned target margin

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal` through `MI-023-recurrence-visibility-plus-radial-depth-does-not-control-annihilator-conditioning`.

NB-123--NB-125 give a genuine source-faithful separator on geometric grids: finite zero-power packets obey annihilating recurrences, and the missing harmonic root creates a positive target-angle margin when enough recurrence depth is visible. NB-126--NB-128 show that fixed finite phase systems alias globally, while the full natural prefix restores a quantitative local ordinate modulus inside a height window of size `Theta(R)`.

NB-129 supplies the amplitude splice and its sharp ambient barrier. At height `|T|~m`, target-bearing natural-grid phase visibility requires target-angle defect `O(1/|T|)`, and an endpoint-preserving matched sequence with only `Theta(1/m)` excess energy can erase the entire phase-sensitive block.

NB-130--NB-131 show why finite recurrence and exact prefix data do not suffice for arbitrary formal packets. Rank-`R` formal zero powers can interpolate arbitrary values on `1,...,R`, and one invertible support shape can be translated to every height with only unitary row modulation while its formal Burnol defect tends to zero.

NB-132 separates that formal class from genuine zeta zeros in an explicit regime. For right-half-plane zeros in a fixed-width band `(T,T+W]` with `T+W<=R^A`, symmetry plus explicit zero counting can force the confluent rank below the `q`-geometric recurrence-visibility budget. The formal linear-rank interpolation control is therefore not source-faithful in that polynomial-height/narrow-band regime.

NB-133 now blocks the obvious conditioning splice. A simple matched formal packet can obey the same numerical rank allowance and lie safely on the allowed side of the Vinogradov--Korobov horizontal zero-free boundary, while `Theta(log R)` sampled roots cluster in a shrinking phase arc around the missing target root. Its full recurrence is visible, yet the exact normalized NB-124 annihilator margin is superpolynomially small:

`mathfrak s_R <= R^(-(4c/3+o(1)) log log R)`.

Thus rank visibility plus radial zero-free depth does not yield a polynomial target margin. Inside the NB-132 regime, the live theorem must now be source-specific in **root arrangement**: prove enough angular anti-clustering/spacing for actual sampled zeta roots, couple several multiplicatively independent bases before scalarizing the margin, exploit stronger natural-grid phase geometry, or replace the product annihilator certificate by a target-bearing functional whose conditioning is not destroyed by a narrow phase cluster. Outside the regime, especially at superpolynomial height or growing ordinate width, rank visibility itself remains open.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, natural-prefix resolution, target angle, radial depth, phase arrangement, conditioning and provenance separate

NB-128 buys local phase stability by growing the observation prefix. NB-129 shows that target visibility still costs reciprocal-height amplitude accuracy. NB-130--NB-131 show that arbitrary formal rank can defeat finite-prefix and height-blind descriptors. NB-132 shows that actual-zero counting can restore rank visibility in a concrete source-faithful regime. NB-133 shows that even there, coarse population and horizontal-depth information leave the visible annihilator arbitrarily ill-conditioned through angular clustering.

The surviving discriminator is therefore not simply “actual zeros versus formal powers.” One must state which source law limits effective rank, whether the observation prefix resolves that rank, what controls the relative phase arrangement of the sampled roots, and whether the resulting target certificate remains quantitatively conditioned at the Burnol scale.
