# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Beat the zero-density-lifted full-packet gain/complexity budget with actual-zero source information

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-025-rightmost-turan-observability-removes-the-horizontal-spread-tax-but-full-packet-closure-pays-a-gain-complexity-tail-budget`.

RE-112--RE-133 reduce the attained finite-edge branch to a strong atom plus reciprocal-scale cancellation geometry and show that sparse formal spectra can realize nearby doublets and growing hiding clusters. RE-134--RE-138 then make finite-packet visibility and actual-zero geometry explicit.

RE-139 removes the horizontal-spread tax for finite packets. Normalize at a rightmost horizontal atom and use Turán's Second Main Theorem directly on samples inside the observation window. The lower bound depends exponentially on packet size but not on horizontal spread or vertical diameter. For actual zeros, bounded absolute vertical span gives only `O(log U)` retained modes, so superalgebraic finite-packet hiding forces the absolute vertical span itself to diverge.

RE-140 splices that finite witness with the full exterior tail. For a core truncated at height `T`, the finite contribution is governed by

`G(U,T) exp(-Lambda_kappa N_T) M_0(U)`,

where `G` is the amplitude transfer from the original strong atom to the rightmost retained atom and `N_T` is the paid Turán mode count.

RE-141 now improves the exterior side of that budget using the actual off-critical source law. Ingham zero density, partial summation of the `gamma^-2` Robin coefficients and horizontal damping give

`||S_0-S_(0,T)||_infty << T^(-2+nu_I(Theta)+epsilon)(log T)^C + exp(-c_epsilon U) log T/T`,

with `nu_I(Theta)=3(1-Theta)/(2-Theta)`. For `T=U^B`, `M_0>=U^-A`, `G>=T^-eta` and `N_T<=alpha log T`, a sufficient closing condition is

`A/B + eta + Lambda_kappa alpha < 2-nu_I(Theta) = (1+Theta)/(2-Theta)`.

The cutoff budget is therefore strictly better than the crude absolute-tail threshold `1` whenever `Theta>1/2`. But the problem does not disappear: the geometry-free amplitude transfer still corresponds to `eta=2`, while `2-nu_I(Theta)<2` for every attained `Theta<1`, and raw polynomial zero-density counts are still useless if charged directly inside the exponential Turán mode penalty.

The live theorem is now sharply source-specific. Improve the rightmost height/amplitude transfer, prove an `O(log T)` or otherwise affordable **effective** mode count, obtain a stronger signed-tail estimate, or replace the finite-core splice by infinite-packet observability. Zero density has already been spent where it is quantitatively productive: on the weighted exterior tail.

## Keep atom extraction, finite-packet visibility, source-weighted tail suppression and retained-core complexity separate

RE-130 prices the size of an extracted atom. RE-139 makes every finite rightmost-anchored packet visible without a horizontal-spread penalty. RE-141 shows that source sparsity at high ordinate can strongly suppress the omitted tail even though the same zero-density estimate does not solve the Turán cardinality term. RE-140--RE-141 leave the rightmost amplitude transfer and effective retained complexity as independent costs.

These are different currencies. Failure of the full-packet certificate does not imply actual cancellation; it says the guaranteed core floor is below the available tail envelope. Any closing argument must state which zeros enter the core, how the rightmost anchor is selected, how many modes are paid for, what amplitude transfer is available, and whether exterior control uses density-weighted absolute mass or signed phase cancellation.

## Keep the exact binary tie local

The surviving first/depth-two Four-Exponentials contingency remains local and does not control the finite-edge packet analysis. A global argument should remain robust to that binary alternative unless exact transcendence becomes load-bearing.