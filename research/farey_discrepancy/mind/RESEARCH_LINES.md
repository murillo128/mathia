# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Transport enough packet strength through the sharp logarithmic source-neutral window

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`, `MI-002-odd-prime-square-reembedding-localizes-recursive-failure-to-dyadic-channel`, `MI-003-normalized-record-defect-is-the-composition-loss`, `MI-004-multiplicative-horizon-descent-can-preserve-the-source-quotient`, `MI-005-source-neutral-carrier-descent-spends-a-strict-finite-row-potential`.

FD-094--FD-101 close one-step representation, projective composition loss, the current endpoint regularity gain, fixed-carrier inventory and cumulative rounding. FD-102 then removes adaptive retagging as an independent escape: the carrier-free potential

`A(H,x)=log_2((H-1)/(8x-1))`

drops by one at every nonhead step unless the retag pays through genuine source descent. On the false-RH frontier, source-neutral nonhead depth is at most `(1-Theta+delta+o(1)) log_2 H` even with arbitrary carrier reselection.

FD-103 proves this logarithmic coefficient is geometrically sharp. Power-dense source records generate actual dyadic ladders with constant sampled source whose length saturates `A(H,x)` up to `o(1)`, while projective quality at the top is still only polynomially small. The deterministic source budget therefore cannot be improved merely by sharper floor geometry, carrier bookkeeping or source-record recurrence.

The live theorem is an **energy-uniformization theorem at logarithmic depth**. Either prove that frontier-sharp packet occupation/projective quality survives for slightly more than the carrier-free budget, forcing a head or source drop while the packet is still useful, or show that the head/source-descending events themselves accumulate enough source progress. Arbitrary fixed-depth diagonalization is insufficient; the depth must scale like `c log H` with explicit quality accounting.

## Determine whether the polynomial projective tax still leaves a contradiction-strength packet

FD-103 gives the matched sharpness scale

`Q_sigma(H_0) >= H_0^(-2Theta(1-Theta)-o(1))`

on the frontier-scaled dyadic ladder. This is not a fixed-occupation theorem, but it prices the deterministic cost of reaching the end of the source-neutral window.

The next quantitative question is whether the actual predecessor transport can be uniformized with a polynomial loss whose exponent remains below the margin needed by the false-RH source record, or whether mass selection degrades faster and escapes the deterministic budget. This comparison must retain the same normalized-energy/projective variables used by the final predecessor argument; a bound in a stronger but irrelevant coordinate does not close the line.

## Keep entry recurrence, deterministic source budget and packet transport distinct

Source records provide recurrent entry states; FD-102 provides an index-free deterministic charge that already survives arbitrary retagging; FD-103 shows that charge is sharp on actual carriers. The remaining uncertainty is analytic rather than genealogical: whether enough selected energy follows the deterministic sequence for logarithmically many steps, and what source movement is forced when it does not. Reintroducing a separate carrier-switching invariant is no longer necessary unless a future predecessor branch violates the hypotheses of the current carrier-free potential.