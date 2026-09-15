# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Derive source-native coercivity that pays either endpoint concentration or typical ancestry depth

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 classify the binary coefficient-side obstruction exactly. For an anchored seed `D`, binary orientations satisfy

`C^(bin)_(q,D) = h_D(nu,eta)^(-1/q)`,

where `h_D` is the infimum of boundary observation mass divided by flipped vertex mass over all admissible anchored cuts. Connectivity only says no such cut has zero boundary; stable finite-`L^q` recovery requires a uniform positive cut-exposure constant in the actual weights.

FD-148 closes the naive one-step reweighting escape for a fixed finite divisor-closed seed. The complement-of-`D` cut forces vanishing expansion when the parent marginal has `o(T)` amplification or the child marginal has `o(log T)` amplification. Positive anchored expansion at one step therefore requires a **singular endpoint allocation**: order-one edge mass on a fixed seed boundary, average parent amplification of order `T`, or logarithmic child/prime-ray amplification.

FD-149 quantifies the alternative “make ancestry genuinely nonlocal.” For positive ancestry edges allowed to jump at most `L` prime adjunctions, bounded child-marginal distortion `K_T=O(1)` still gives vanishing expansion at every fixed depth. More sharply, if `h_(D,T)^(<=L_T)` stays bounded below, squarefree Erdős--Kac forces

`L_T >= log log T - O(sqrt(log log T))`.

Thus a bounded-distortion ancestry interface must reach essentially the **typical squarefree prime-factor depth**. Any depth `L_T <= (1-delta) log log T` is still too local. The live coefficient-side theorem must therefore derive one of two expensive resources from genuine Farey/arithmetic structure: singular endpoint mass, or nonlocal reach of order `log log T` with the right destination control. Merely saying “use nonuniform weights” or “allow a few more ancestry steps” no longer specifies a mechanism.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a separate lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. This is a later information threshold, not a substitute for the cut theorem. Conversely, sufficiently direct high-information coordinates can reconstruct the source and risk circularity.

Future ancestry proposals should therefore be audited in this order: **anchor geometry -> reachable-depth/endpoint exposure -> source justification for the required depth or weight concentration -> information and precision budget -> destination relevance**. `L^infinity` remains qualitatively different because for binary data it sees any visible bridge rather than its normalized mass.

## Keep binary cut coercivity and nonlocal destination coercivity separate

FD-147--FD-149 concern binary Möbius orientations, finite `L^q`, divisibility ancestry and a fixed finite anchor. They do not rule out a growing source-native anchor, `L^infinity`, deliberately singular but independently justified arithmetic weights, ancestry reach at the typical `log log T` depth, or genuinely nonlocal Farey/Fourier observables that are not represented by this positive ancestry edge model. Any escape should state which hypothesis changes and why the new destination does not simply reconstruct the source.