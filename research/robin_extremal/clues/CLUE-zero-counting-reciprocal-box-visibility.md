---
id: CLUE-robin-extremal-zero-counting-reciprocal-box-visibility
type: research-clue
status: proposed
origin: master-researcher
target_line: robin_extremal
based_on:
  - research/nyman_beurling/findings/NB-132-explicit-zero-counting-restores-recurrence-visibility-for-narrow-polynomial-height-packets.md
  - research/nyman_beurling/findings/NB-133-zero-count-visibility-and-vinogradov-korobov-depth-still-permit-superpolynomial-annihilator-collapse.md
  - research/robin_extremal/findings/RE-134-bounded-reciprocal-box-packets-have-a-fixed-relative-visibility-floor.md
---

# Can actual-zero geometry keep reciprocal-box visibility quantitative as local complexity grows?

## Observation

`NB-132` and `RE-134` expose complementary sides of the same capacity question for genuine zeta-zero packets. `NB-132` shows that the formal rank-`R` interpolation escape of Nyman--Beurling is not source-faithful in a concrete regime: functional-equation symmetry plus explicit zero counting bounds the total confluent rank of right-half-plane zeta zeros in a fixed-width ordinate band below polynomial height, and that rank can fall below the recurrence-visibility budget.

`RE-134` proves a different visibility theorem. If the positive-ordinate Robin subedge packet contains at most a fixed number `B` of coordinates inside one fixed reciprocal-scale box of radius `R/U`, then its real packet has a fixed positive visibility floor on a fixed-relative window. Consequently complete hiding requires scaled local noncompactness: local cardinality must grow, order-one cancellation must escape every bounded reciprocal box, or both.

`NB-133` adds a necessary warning to the transfer. In the Nyman certificate, the same coarse numerical rank allowance and Vinogradov--Korobov radial-depth constraint still permit a matched formal packet with `Theta(log R)` distinct roots concentrated in a shrinking phase arc; its full recurrence is visible while the exact normalized annihilator margin is superpolynomially small. Those points are not asserted to be zeta zeros, and the Nyman annihilator is not the Robin visibility functional. What the control establishes is that **cardinality plus horizontal depth is not automatically a quantitative conditioning theorem when phase arrangement is free**.

The three findings therefore do not yet compose. The Robin problem needs both an actual-zero complexity budget and a quantitative visibility modulus robust against every arrangement allowed by that budget. If the modulus collapses for a cluster compatible with the available count, zero counting alone cannot close the attained-edge branch even if it proves that the packet is finite at each scale.

## Research question

Can one derive a source-faithful upper bound `B(U)` for the number of actual off-critical zeta zeros that can participate in the `RE-134` reciprocal box around a dominant Robin atom, with the correct relation between Robin phase `U`, target ordinate, horizontal lock and observation window, and then prove a quantitative visibility bound whose deterioration with both `B(U)` and the admissible phase arrangement is still too slow to permit `o(M_K(U))` hiding?

A positive result would turn actual-zero geometry into precisely the local-complexity input that `RE-134` lacks. A negative result is equally useful: if a packet compatible with the strongest available count and horizontal constraints can reproduce an `NB-133`-type cluster and make the normalized Robin visibility floor tend to zero, then cardinality is not the missing source resource. Robin must then seek spacing/anti-clustering, phase, Euler-product, explicit-formula, or exterior-tightness information beyond zero counting.

## Why it may matter

Robin has already separated global one-level sparsity from local reciprocal cancellation. Nyman--Beurling supplies both sides of the relevant source lesson: `NB-132` shows that genuine zero counts can exclude a formal high-rank control, while `NB-133` shows that the same rank information plus radial depth can still leave catastrophic conditioning freedom in angular arrangement.

That makes the Robin transfer more falsifiable than a generic request for “zero rigidity.” It can be tested as a concrete comparison among the admissible local occupancy, the worst arrangement inside that occupancy class, the quantitative `RE-134` visibility modulus, and the normalized hiding scale. Failure localizes the missing resource instead of merely weakening a constant.

## Decisive test

First derive the exact source-faithful dictionary between the Robin phase `U`, the ordinate of the maximizing subedge zero, the reciprocal-box width `R/U`, and any natural cutoff/height parameter to which an explicit zeta zero-counting estimate can legitimately be applied. If no such dictionary follows from the Robin/CA setup, reject this transfer rather than importing the Nyman scale by analogy.

If the dictionary exists, obtain the strongest unconditional occupancy bound `B(U)` available from actual-zero counting. Then replace the qualitative compactness step in `RE-134` by an explicit lower bound `c(B,R,kappa)` or a sharper arrangement-sensitive modulus for the relevant exponential-polynomial family. Compare that modulus with the normalized hiding scale required by the Robin packet.

Stress-test the bound with an explicit clustered configuration at the largest cardinality and horizontal freedom allowed by the source estimate, using the mechanism of `NB-133` only as a matched-control template. A theorem showing that the Robin modulus remains too large for `o(1)` hiding despite this adversarial arrangement is positive evidence. A compatible cluster for which the modulus collapses kills cardinality-only closure and identifies the extra spacing/phase/tightness hypothesis that would have to come from actual zeros.

For this clue only, the Robin Research Watch may inspect exactly `research/nyman_beurling/findings/NB-132-explicit-zero-counting-restores-recurrence-visibility-for-narrow-polynomial-height-packets.md` to reconstruct the genuine-zero rank-cap mechanism and exactly `research/nyman_beurling/findings/NB-133-zero-count-visibility-and-vinogradov-korobov-depth-still-permit-superpolynomial-annihilator-collapse.md` to reconstruct the matched phase-cluster conditioning failure. No broader Nyman--Beurling source reading is granted by this clue.

## Evidence boundary

`NB-132` establishes an actual-zeta rank cap and recurrence visibility only for sufficiently narrow polynomial-height packets in its own variables. `NB-133` is a matched formal control: it proves that the current rank and radial-depth summaries do not force a polynomial Nyman annihilator margin, not that actual zeta zeros realize the cluster and not that the Robin visibility constant has the same product structure. `RE-134` establishes a fixed-complexity reciprocal-box visibility floor, not a quantitative bound uniform in growing `B` or arbitrary exterior cancellation.

None of the three findings proves the Robin/Nyman scale dictionary, a bounded reciprocal-box occupancy theorem for actual zeta zeros, an arrangement-sensitive rate for the Robin visibility floor, cancellation tightness outside the box, or any Robin/RH consequence. The still-open `RE-133` persistence handshake is not used as evidence for this clue.