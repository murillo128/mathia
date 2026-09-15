# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Beat the full-packet gain/complexity budget with relational actual-zero information

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-026-upper-zero-density-cannot-improve-the-rightmost-transfer-exponent`.

RE-112--RE-133 reduce the attained finite-edge branch to a strong atom plus reciprocal-scale cancellation geometry and show that sparse formal spectra can realize nearby doublets and growing hiding clusters. RE-134--RE-138 then make finite-packet visibility and actual-zero geometry explicit.

RE-139 removes the horizontal-spread tax for finite packets. Normalize at a rightmost horizontal atom and use Turán's Second Main Theorem directly on samples inside the observation window. The lower bound depends exponentially on packet size but not on horizontal spread or vertical diameter. For actual zeros, bounded absolute vertical span gives only `O(log U)` retained modes, so superalgebraic finite-packet hiding forces the absolute vertical span itself to diverge.

RE-140 splices that finite witness with the full exterior tail. For a core truncated at height `T`, the finite contribution is governed by

`G(U,T) exp(-Lambda_kappa N_T) M_0(U)`,

where `G` is the amplitude transfer from the original strong atom to the rightmost retained atom and `N_T` is the paid Turán mode count.

RE-141 improves the exterior side using the actual off-critical source law. Ingham zero density, partial summation of the `gamma^-2` Robin coefficients and horizontal damping give

`||S_0-S_(0,T)||_infty << T^(-2+nu_I(Theta)+epsilon)(log T)^C + exp(-c_epsilon U) log T/T`,

with `nu_I(Theta)=3(1-Theta)/(2-Theta)`. For `T=U^B`, `M_0>=U^-A`, `G>=T^-eta` and `N_T<=alpha log T`, a sufficient closing condition is

`A/B + eta + Lambda_kappa alpha < 2-nu_I(Theta) = (1+Theta)/(2-Theta)`.

RE-142 now proves that the remaining geometry-free transfer exponent `eta=2` cannot be improved from the current **upper-envelope** source information. A single infinite formal zero-like spectrum can satisfy the relevant upper zero-density laws, the zero-free region, functional symmetry and an exact Riemann--von Mangoldt background while, along lacunary cutoffs,

`G(U_j,T_j)=T_j^(-2+o(1))`

and simultaneously

`N_(T_j)=o(log T_j)`.

Thus the `T^-2` transfer loss can persist even when the effective Turán complexity coefficient tends to zero. A stronger upper zero-density exponent can improve the omitted tail but, by itself, cannot force a farther-right retained atom to appear at comparable ordinate or acquire enough horizontal gain.

The live theorem is therefore **relational rather than another one-point upper envelope**. It must couple a strong atom to rightward recurrence/first-occurrence height, couple horizontal extremality to ordinate, derive a lower-population statement in the relevant right strip, obtain signed exterior cancellation, or replace rightmost anchoring by a target-aware/infinite-packet certificate that avoids paying the `T^-2` transfer.

## Keep atom extraction, finite-packet visibility, source-weighted tail suppression, retained-core complexity and rightward recurrence separate

RE-130 prices the size of an extracted atom. RE-139 makes every finite rightmost-anchored packet visible without a horizontal-spread penalty. RE-141 shows that source sparsity at high ordinate can strongly suppress the omitted tail even though the same zero-density estimate does not solve the Turán cardinality term. RE-142 shows something stronger: even when that cardinality cost is negligible, the rightmost transfer can remain at the generic two-power loss under all currently imported upper source envelopes.

These are different currencies. Failure of the full-packet certificate does not imply actual cancellation; it says the guaranteed core floor is below the available tail envelope. Any closing argument must state which zeros enter the core, how the rightmost anchor is selected, how many modes are paid for, what amplitude transfer is available, and which **relational source theorem** prevents the strong atom and the rightmost atom from separating in precisely the way allowed by RE-142.

## Keep the exact binary tie local

The surviving first/depth-two Four-Exponentials contingency remains local and does not control the finite-edge packet analysis. A global argument should remain robust to that binary alternative unless exact transcendence becomes load-bearing.