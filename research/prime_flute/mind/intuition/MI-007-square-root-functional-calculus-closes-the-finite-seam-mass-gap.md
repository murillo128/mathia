# MI-007 — The square-root source closes the seam mass gap and fixes the leakage at the critical exponent

**Evidence level:** proved

## Core intuition

The naked finite seam has supercritical low-output decay because its positive Green representation starts at nonzero mass. The physical Robin-normalized source applies a square root that moves the representing continuum down to the mass-one threshold. That threshold is not removed by normalization: the normalized source is analytic across the relevant Fourier points and has a nonzero branch coefficient there.

The consequence is now exact rather than diagnostic. The fixed-axis normalized leakage is critical up to logarithms, so no `q>1` low-output exponent can be recovered from this architecture.

## Strongest justified claim

PF-272 proves strict supercritical sublinear leakage for the naked finite seam. PF-273 shows that the square-root source factor replaces the positive lowest Green mass by an absolutely continuous measure reaching `t=0`, hence `mu=1`. PF-274 diagonalizes the fixed-axis scalar functional calculus in the symmetric continuous-Hahn representation.

PF-276 proves the Robin normalization is inverse-positive and leaves a strictly positive threshold moment. PF-277 upgrades this to a genuine Fourier statement: the normalized source transform is holomorphic on `|Im xi|<2` and nonzero at `xi=±i`; multiplication by the square-root seam symbol therefore creates a nonremovable mass-one branch germ.

PF-278 transfers that branch through the exact corridor basis. For every fixed output row,

`||P_i B_w E_N|| asymp N^(-1) (log N)^(-3/2)`,

with an explicit nonzero constant. Hence `N^q ||P_iB_wE_N|| -> infinity` for every `q>1`. Any polynomial, logarithmic, or fixed low-output window containing that row fails the supercritical PF-271 bound.

## Synthesis of evidence

The earlier open question—whether noncommuting Robin normalization might suppress the mass-one continuum strongly enough to restore a fixed power—has been resolved negatively. The logarithmic factor is real but does not create a polynomial margin. The fixed-axis functional-calculus problem is therefore no longer a place to search for the missing exponent.

This also clarifies what a future modification must change. It must alter the source/propagation architecture before the mass-one branch reaches the destination, or replace the decision statistic with one for which critical leakage is sufficient. Merely refining the same continuous-Hahn asymptotic cannot cross the `q>1` gate.

## Counterevidence / boundary cases

PF-278 is fixed-axis and fixed-row. It does not classify every sheared or variable-corridor architecture, nor does it rule out cancellations created by a materially different coupled source. It closes the accepted fixed-axis Robin-homotopy route because that route already demands the failed fixed-row estimate.

The naked seam result PF-272 remains valid; what fails is inheritance of its mass gap through the physical square-root normalization.

## Epistemic status

**Exact route closure:** the physical fixed-axis Robin-normalized source has a nonzero mass-one branch and sharp leakage `N^-1(log N)^-3/2`, so the supercritical fixed-row gate fails for every `q>1`.

## Novelty/prior-art status

No broad novelty claim is made beyond the persisted PF-273--PF-278 audits. This note records the completed internal implication.

## Falsification criterion

Invalidate the nonzero threshold value or branch-to-coefficient transfer in PF-277--PF-278, or exhibit within the same fixed-axis normalized operator a cancellation that changes the fixed-row asymptotic while preserving its hypotheses. Either would reopen the route.
