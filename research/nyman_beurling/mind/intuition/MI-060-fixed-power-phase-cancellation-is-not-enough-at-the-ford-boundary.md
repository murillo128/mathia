# MI-060 — Fixed-power phase cancellation is not enough at the Ford boundary

**Evidence level:** exact matched-control synthesis from [NB-225](../../findings/NB-225-sublinear-ford-shells-remain-population-blind.md) and [NB-226](../../findings/NB-226-fixed-power-phase-cancellation-does-not-rescue-sublinear-ford-shells.md), using the zeta-population inputs audited there.

NB-225 shows that at exact Ford scale a sublinear logarithmic source shell `H=o(R)` cannot be closed from the currently used zero-free and population information alone. One may place an admissible packet of near-one zeros at vertical spacing `Theta(1/X)` whose moving-shell phases align and whose horizontal depth is tuned so the weighted residue remains order one.

NB-226 strengthens that method boundary: **generic phase cancellation of any fixed positive power is still insufficient**. For every fixed `0<vartheta<1`, the matched packet can be assigned phases so that every consecutive vertical subpacket of `m` zeros obeys

`|sum e^(iX(gamma-t))| << m^vartheta`,

while the full weighted moving-shell residue remains bounded away from zero and all of the population constraints used in NB-225 remain satisfied. In particular, square-root cancellation on every consecutive subpacket does not rescue a sublinear shell.

The mechanism is exact. A packet of size `M` is given a global phase bias of order `M^vartheta`, while its common horizontal depth is chosen so the Ford carrier contributes the reciprocal damping `M^(-vartheta)`. The product stays order one. The obstruction therefore does not come from complete phase alignment; it comes from the ability to trade **horizontal depth against the amount of allowed vertical phase bias**.

The right object is consequently weighted and joint. At depth `D`, the quantity that must be forced small is of the form

`e^(-Y D) |sum_(rho at depth D) e^(iX(gamma-t))|`,

or its exact residue-weighted analogue. A theorem of the form “raw phase sums have a fixed power saving in local population” does not couple the two variables strongly enough, because the depth can be moved to neutralize any fixed exponent.

This leaves a sharper source-side frontier than the generic phrase “use phase information.” A useful theorem must make phase cancellation **improve with horizontal depth**, directly control the weighted residue coefficients, or give a joint depth-window population bound that removes the packets before their phase discrepancy can be traded against damping.

**Boundary.** NB-226 is a logical insufficiency result for the current sublinear-width Ford mechanism. It does not claim actual zeta zeros realize the matched packet, rule out a depth-sensitive exponential-sum theorem, prove a Nyman--Beurling distance lower bound, or show that linear source width is intrinsically necessary once new joint zero information is available.
