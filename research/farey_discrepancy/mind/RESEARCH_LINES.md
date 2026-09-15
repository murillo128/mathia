# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Replace qualitative ancestry reachability by a source-native anchored cut theorem

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 now classify the binary coefficient-side obstruction exactly. FD-145 identifies the `Z_2` orientation gauge when an ancestry component is disconnected from the Möbius anchor. FD-146 shows that restoring the full connected squarefree ancestry graph does not give finite-`L^q` coercivity under uniform normalization. FD-147 identifies the common object: for an anchored seed `D`, binary orientations satisfy

`C^(bin)_(q,D) = h_D(nu,eta)^(-1/q)`,

where `h_D` is the infimum of boundary observation mass divided by flipped vertex mass over all admissible anchored cuts. Connectivity is only the statement that no such cut has zero boundary; stable recovery requires a uniform positive cut-exposure constant in the actual source/destination weights.

For the full squarefree ancestry graph with uniform vertex and edge measures, every fixed finite prescribed seed still fails this test. A source can agree with Möbius on the seed while flipping the whole complement of its finite divisor closure. Its coefficient error tends to `2`, but its normalized ancestry defect is only

`Theta_S((log T log log T)^(-1/q))`,

forcing every binary anchored Poincare constant to grow at least like `(log T log log T)^(1/q)`. The previous fixed-rank wall was therefore not the essential obstruction; the finite anchor itself can sit behind a vanishing normalized cut.

The live coefficient-side theorem must now change the observation geometry. Either derive source-native nonuniform weights for which **every** macroscopic admissible orientation cut has nonvanishing exposure, or leave local coefficient recovery for a genuinely nonlocal Farey/Fourier destination functional. Merely adding more uniformly weighted ancestry edges, enlarging a finite seed, or proving connectivity cannot succeed.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after component anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, FD-142 shows that sufficiently direct high-information coordinates can reconstruct the source and therefore risk circularity.

Future ancestry proposals should therefore be audited in this order: **anchor connectivity -> quantitative cut exposure in the claimed norm -> information/precision budget -> destination relevance**. `L^infinity` remains qualitatively different: for binary data it sees any visible bridge and therefore reduces to connectivity rather than boundary mass.

## Keep binary cut coercivity and nonlocal destination coercivity separate

FD-147 is exact for binary Möbius orientations and finite `L^q`; it does not rule out source-native nonuniform edge weights, `L^infinity`, direct anchors growing with the problem, or nonlocal Farey/Fourier observables. Any escape should state which of those hypotheses it changes and why the new destination does not simply reconstruct the source.