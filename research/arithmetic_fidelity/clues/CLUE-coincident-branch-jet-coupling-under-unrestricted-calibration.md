---
id: CLUE-arithmetic-fidelity-coincident-branch-jet-coupling
type: research-clue
status: proposed
origin: mind
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-548-finite-regular-jet-lifts-are-pure-gauge-under-unrestricted-calibration.md
---

# Do coincident regular branches create a stable shared-jet escape from unrestricted calibration?

## Observation

AF-548 proves transitivity of the unrestricted orientation-preserving calibration action on every finite-jet order/sign chamber for finitely many **separated regular branches**. Its interpolation step is load-bearing: because the base values are distinct, the calibration jet can be prescribed independently at each observed value.

The finding explicitly leaves coincident branch values outside that classification and notes that shared base values force the same calibration jet to act more than once, so relative jet invariants can appear. It does not classify those invariants or show that exact/shared-value incidence is available from the arithmetic source.

## Research question

For the smallest nontrivial coincident regular configuration, classify the finite-jet orbits under common orientation-preserving smooth postcomposition. Which relative jet quantities survive because several branches sample the **same** calibration jet, and do any of them remain quantitatively stable under the source perturbations or near-coincidences that a physical arithmetic representation can actually produce?

The important distinction is between an invariant that exists only on an exact collision stratum and a source-natural coupling with a nonzero destination margin.

## Why it may matter

AF-547 and AF-548 jointly remove both extra finite branch count and extra regular finite derivative depth as generic repairs when nuisance values and jets are independently programmable. Coincident/shared-value structure is one of the few explicit finite-dimensional places where that independence fails. A robust shared-jet invariant could identify a genuinely different relational lift; a purely singular exact-incidence invariant would instead close another apparent escape.

## Decisive test

Start with two regular branches sharing one base value and classify the prolonged action at first and second jet order, then extend only as needed to identify the general pattern. Separate discrete contact data from continuous relative invariants and verify completeness by an orbit calculation, not by dimension counting alone.

Next perturb the common base value by a gap `epsilon != 0`. Determine whether the candidate invariant has a source-independent stability modulus or whether unrestricted calibration immediately restores independent programmability for every nonzero separation. Kill the direction as a fidelity mechanism if all nontrivial invariants are confined to exact coincidence with zero robust margin, or if the arithmetic source supplies no independent reason for shared-value incidence. Keep it live only if a source-forced overlap/contact law yields a stable transverse quantity in the destination seminorm.

## Evidence boundary

AF-548 establishes the separated regular no-go and identifies coincident values only as an unclassified boundary where relative invariants **may** occur. It does not prove a complete coincident-jet classification, a stability theorem, a source mechanism producing coincidence, or any arithmetic/RH consequence. Those missing steps are exactly why this is a proposed clue rather than an intuition or finding.
