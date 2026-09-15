# MI-013 — Levelwise ancestry means still dilute finite-prime coordinate cuts

**Evidence level:** exact obstruction from [FD-131](../../findings/FD-131-vanishing-worst-level-ancestry-defect-survives-every-fixed-low-rank-mobius-anchor.md)

FD-130 showed that a global edge average can hide one defective multiplicative-rank interface. FD-131 removes that escape without restoring coercivity: even the supremum over **all rankwise mean defects** tends to zero for a source that remains macroscopically different from Möbius.

The witness fixes `K+1` primes with product `Q` and flips the Möbius sign precisely on squarefree multiples of `Q`. It agrees with Möbius through rank `K`, and every prime direction outside `Q` satisfies exact ancestry globally. At rank `j`, defective edges are exactly the `K+1` coordinate directions in `Q`; their fraction is

`(K+1)/(j+1) * N_(j+1,Q)(H)/N_(j+1)(H)`.

For every fixed rank the divisibility ratio tends to zero, while the explicit `1/(j+1)` factor controls the high-rank tail. Therefore the worst rankwise mean defect vanishes even though squarefree multiples of `Q` give positive-density coefficient disagreement.

The concrete lesson is two-dimensional: approximate multiplicative ancestry must keep both **rank** and **prime direction** visible. Normalizing separately by rank prevents inter-rank dilution but not dilution across the growing set of prime coordinates inside each rank.

What remains open is not “use a stronger average” generically. A surviving law must monitor bad prime directions without averaging a fixed set to zero, let the exact anchor grow enough to freeze such coordinates, or bypass coefficient recovery with a destination inequality. FD-131 does not rule out primewise/local `L^infinity` control, growing `K(H)`, or source-structured weighted norms.