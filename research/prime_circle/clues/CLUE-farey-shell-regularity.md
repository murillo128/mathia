---
id: CLUE-prime-circle-farey-shell-regularity
type: research-clue
status: proposed
origin: mind
target_line: prime_circle
based_on:
  - research/prime_circle/findings/PC-251-growing-lower-shared-upper-defect-is-a-weighted-farey-collision-matching.md
  - research/farey_discrepancy/findings/FD-036-quotient-shell-lipschitz-rigidity-forces-a-pointwise-half-power-linear-prefix-gap.md
---

# Does the growing Prime-Circle collision kernel inherit a usable Farey shell-regularity law?

## Observation

PC-251 identifies the first Prime-Circle shared-upper defect whose lower state genuinely grows: after the fixed-conductor packet collapses are removed, the defect is an exact weighted Farey collision matching. Independently, FD-036 proves that a quotient-shell Lipschitz estimate is sufficient to upgrade multiplicative-scale Farey rigidity to a pointwise half-power linear-prefix gap. These facts do not establish that the Prime-Circle collision weights satisfy the Farey-discrepancy hypothesis, but they isolate a concrete regularity test that is invisible in fixed-base residue packets.

## Research question

For the normalized growing-lower collision observable in PC-251, can its contribution be decomposed into adjacent quotient shells whose increments obey a scale-uniform Lipschitz or bounded-variation estimate strong enough to prevent sparse concentration between multiplicative scales? If so, does that regularity yield a cofinal noncollapse statement for the Prime-Circle transfer defect that cannot be reconstructed from finitely many residue packets?

## Why it may matter

Prime Circle currently needs a genuinely growing relational variable after PC-250 and PC-252 close higher-rank and fixed-base nonlinear packet escapes. A shell-regularity theorem would turn the exact Farey-collision identification of PC-251 into a quantitative discriminator rather than another change of coordinates, and it would provide a source-side mechanism for ruling out sparse scale escape.

## Decisive test

Write the PC-251 normalized collision matching as an explicit sum over consecutive quotient shells. Either prove a uniform adjacent-shell estimate at the normalization consumed by the transfer defect and derive a nontrivial cofinal lower bound, or construct a valid growing-lower family whose normalized defect concentrates on sparse shells while all fixed-conductor controls remain satisfied. The latter kills this transfer route.

## Evidence boundary

FD-036 is evidence only that shell Lipschitz rigidity is sufficient in the Farey-discrepancy model. It does not imply the PC-251 collision kernel has that regularity, nor that the two normalized defects are equivalent. PC-251 supplies the exact collision representation but no pointwise/cofinal regularity theorem. This clue proposes the missing comparison and remains below finding/intuition status.