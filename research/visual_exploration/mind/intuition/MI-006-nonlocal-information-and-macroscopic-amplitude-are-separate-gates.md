# MI-006 — Support-edge source specificity begins beyond the restricted-support four-level barrier

**Evidence level:** exact finite-CUE covariance, four-level identifiability, and Rudnick--Sarnak support reductions through VIS-141

## Core intuition

A shrinking arithmetic residual at the Montgomery edge cannot be interpreted from one-window behavior. The fixed-window statistic has an order-one stochastic floor, so detection requires averaging across source windows, and the averaging law is a four-level dependence question.

The obvious unconditional higher-correlation shortcut is now closed for this observable: the classical Rudnick--Sarnak support region cannot contain edge-edge covariance, and a simple support-safe redesign either removes the edge or collapses the companion frequency toward DC.

## Strongest justified principle

VIS-130--VIS-135 fix the window convention, remove the realized diagonal common mode, and prove a nondegenerate Gaussian terminal packet for the bounded CUE edge statistic. VIS-136--VIS-139 then show that the required number of source windows is determined by cross-window covariance and that, after lower-order contractions, disjoint quadratic covariance is a four-level functional not fixed by one-, two-, or three-level marginals.

VIS-140 pulls the Rudnick--Sarnak zeta support condition `sum |xi_j|<2` onto the pair-pair plane `(q,-q,r,-r)`, giving exactly `|q|+|r|<1`. The edge-edge sector near `(1,1)` is therefore separated by an order-one support gap. VIS-141 proves the design corollary: identical-factor covariance inside that theorem requires support below `1/2`, while retaining one factor at `1-epsilon` forces the other bandwidth below `epsilon`.

## Program consequence

Prioritize a direct zeta cross-height mixing/covariance estimate or genuinely wider-support four-level information for the exact moving-window family. An asymmetric edge--low-frequency or nonfactorized four-level statistic is admissible only after a separate derivation shows that it retains a source-specific arithmetic signal at the declared scale.

## Counterevidence / boundary

The Rudnick--Sarnak obstruction is an applicability boundary, not evidence that the desired covariance law is false. Wider-support unconditional theorems, a direct explicit-formula covariance argument, or a carefully designed nonfactorized test may escape. A conjectural ratios formula can guide prediction but does not satisfy the rigorous gate.

## Epistemic status

**Exact identification of the multi-window four-level requirement plus an exact support obstruction to the classical restricted-support shortcut; the required zeta-side dependence theorem remains open.**

## Falsification criterion

Derive the frozen edge covariance from the classical restricted-support theorem without violating its support/localization hypotheses, or prove that a support-safe replacement retains the same arithmetic target while avoiding any new four-level or uniform-transfer obligation.