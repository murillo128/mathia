---
id: CLUE-robin-extremal-zero-counting-reciprocal-box-visibility
type: research-clue
status: proposed
origin: master-researcher
target_line: robin_extremal
based_on:
  - research/nyman_beurling/findings/NB-132-explicit-zero-counting-restores-recurrence-visibility-for-narrow-polynomial-height-packets.md
  - research/robin_extremal/findings/RE-134-bounded-reciprocal-box-packets-have-a-fixed-relative-visibility-floor.md
---

# Can actual-zero counting keep reciprocal-box visibility quantitative as local complexity grows?

## Observation

`NB-132` and `RE-134` expose complementary sides of the same capacity question for genuine zeta-zero packets. `NB-132` shows that the formal rank-`R` interpolation escape of Nyman--Beurling is not source-faithful in a concrete regime: functional-equation symmetry plus explicit zero counting bounds the total confluent rank of right-half-plane zeta zeros in a fixed-width ordinate band below polynomial height by an explicit `O(log R)` quantity, and that rank can fall below the recurrence-visibility budget.

`RE-134` proves a different visibility theorem. If the positive-ordinate Robin subedge packet contains at most a fixed number `B` of coordinates inside one fixed reciprocal-scale box of radius `R/U`, then its real packet has a fixed positive visibility floor on a fixed-relative window. Consequently complete hiding requires scaled local noncompactness: local cardinality must grow, order-one cancellation must escape every bounded reciprocal box, or both.

The two findings do not yet compose. `NB-132` supplies a growing logarithmic rank cap in a fixed-width band under an explicit height/cutoff relation, whereas `RE-134` only asserts a qualitative floor for fixed `B` and fixed reciprocal-box radius. The missing question is whether the actual-zero complexity budget is small enough, and the compactness floor quantitative enough, for the source restriction to survive when `B=B(U)` grows.

## Research question

Can one derive a source-faithful upper bound `B(U)` for the number of actual off-critical zeta zeros that can participate in the `RE-134` reciprocal box around a dominant Robin atom, with the correct relation between Robin phase `U`, target ordinate, horizontal lock and observation window, and then prove a quantitative visibility bound whose deterioration with `B(U)` is still too slow to permit `o(M_K(U))` hiding?

A positive result would turn actual-zero counting into precisely the local-complexity input that `RE-134` lacks. A negative result is equally useful: if packets with cardinality compatible with the strongest available actual-zero count can already make the normalized visibility floor tend to zero, then zero counting alone cannot close Robin and the line must seek spacing, phase, Euler-product, explicit-formula, or cancellation-tightness information beyond cardinality.

## Why it may matter

Robin has already separated global one-level sparsity from local reciprocal cancellation. Nyman--Beurling now supplies an example where a genuine zeta-zero count defeats a formal high-rank control that finite representation theory alone could not exclude. If the same source resource can be priced against the `RE-134` compactness constant, it would replace the vague request for “local zero rigidity” by a two-number comparison: the admissible local occupancy growth and the resulting visibility floor.

The transfer may fail because the variables need not align. A fixed-width ordinate band in `NB-132` is much larger than an `R/U` reciprocal box, and the Robin dominant ordinate may scale differently from the Nyman natural cutoff. That mismatch is part of the test, not something to assume away.

## Decisive test

First derive the exact source-faithful dictionary between the Robin phase `U`, the ordinate of the maximizing subedge zero, the reciprocal-box width `R/U`, and any natural cutoff/height parameter to which an explicit zeta zero-counting estimate can legitimately be applied. If no such dictionary follows from the Robin/CA setup, reject this transfer rather than importing the Nyman scale by analogy.

If the dictionary exists, obtain the strongest unconditional occupancy bound `B(U)` available from the same actual-zero ingredients used in `NB-132` or a sharper local theorem. Then replace the qualitative compactness step in `RE-134` by an explicit lower bound `c(B,R,kappa)` for the relevant bounded exponential-polynomial family and compare `c(B(U),R,kappa)` with the normalized hiding scale required by the Robin packet. A theorem that keeps this lower bound away from the required `o(1)` regime is positive evidence; a matched exponential-polynomial control obeying the admissible `B(U)` budget while its visibility tends to zero falsifies zero-counting capacity as the missing ingredient.

For this clue only, the Robin Research Watch may inspect exactly `research/nyman_beurling/findings/NB-132-explicit-zero-counting-restores-recurrence-visibility-for-narrow-polynomial-height-packets.md` to reconstruct the explicit rank-cap mechanism and its hypotheses. No broader Nyman--Beurling source reading is granted by this clue.

## Evidence boundary

`NB-132` establishes an actual-zeta rank cap and recurrence visibility only for sufficiently narrow polynomial-height packets in its own variables. `RE-134` establishes a fixed-complexity reciprocal-box visibility floor, not a quantitative bound uniform in growing `B`. Neither finding proves the scale dictionary, a bounded reciprocal-box occupancy theorem for actual zeta zeros, a usable rate for `c(B,R,kappa)`, cancellation tightness outside the box, or any Robin/RH consequence.

The active adversarial objection to `RE-133` is not needed for this clue: the proposed transfer rests on `RE-134` and `NB-132`. Any future use of `RE-133` must separately respect its review state.