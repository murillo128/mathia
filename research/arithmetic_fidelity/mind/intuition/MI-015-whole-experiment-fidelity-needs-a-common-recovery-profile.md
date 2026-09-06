# MI-015 — Whole-experiment fidelity needs common recovery, source-reference provenance, and separate calibration

**Evidence level:** exact finite/classical results through AF-150

## Core intuition

The composable information object is one reverse channel shared by the whole family, but three issues must remain separate: whether such a recovery exists, whether the common reference used to construct it retains source provenance through the compression chain, and whether the chosen divergence numerically calibrates recovery at the effective family complexity.

## Strongest justified principle

AF-142--AF-145 separate local/pairwise fidelity from family-wide recovery and show that a propagated common reference gives composable Bayes/Petz reverses with telescoping chi-square loss. AF-146--AF-148 then prove that references restricted to in-family mixtures can suffer family-size dilution; for general `f`-divergences the private-label calibration boundary is exactly the endpoint diameter.

AF-149 identifies a canonical escape from that particular dilution: the normalized Shtarkov/NML likelihood envelope is the minimax `D_infinity` dominating reference, generally lies outside the experiment convex hull, and on the private-label control makes the Pearson recovery loss vanish at the same scale as the actual deficiency. The recovery inequality never required the reference to be an in-family mixture.

AF-150 identifies the same reference as the order-infinity Sibson information-radius center and `log C` as maximal leakage. Under compression the propagated source center and the recomputed output center need not agree; their drift is bounded by the maximal-leakage drop, whose logarithmic budget telescopes. Crucially, approximate recoverability of the experiment does not imply approximate functoriality of the recomputed center. A canonical reference therefore remains useful only if its provenance is propagated or a separate source theorem controls recanonicalization drift.

## What remains possible

A source-natural arithmetic family may admit a bounded-complexity Shtarkov-type center, another canonical dominating law, or an equivalent compatibility object with a small leakage-drop budget and a well-calibrated recovery profile. Those properties must be derived from source structure rather than inferred from recoverability alone.

## Status / novelty

Shtarkov NML, Sibson order-infinity information, maximal leakage, Bayes reversal, and `f`-divergence geometry are classical. The durable synthesis is: **family recovery, canonical-reference transport, and certificate calibration are distinct gates; a source-selected center can repair mixture dilution but must be propagated unless its recanonicalization drift is independently controlled**.

## Falsification criterion

Invalidate the common-reference recovery inequality or composition law, produce a private-label counterexample to AF-149's Shtarkov calibration, or show that vanishing recovery deficiency alone forces propagated and recomputed Shtarkov centers to converge under the stated finite-experiment hypotheses.
