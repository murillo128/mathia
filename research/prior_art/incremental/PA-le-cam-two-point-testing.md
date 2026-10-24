---
id: PA-le-cam-two-point-testing
type: prior-art
canonical_name: Le Cam two-point testing bound
aliases:
  - two-hypothesis testing through total variation
kind: statistical lower-bound method
topics:
  - hypothesis-testing
  - information-complexity
---

# Le Cam two-point testing bound

## What it is

For two observation laws \(P_0,P_1\), with \(\mathrm{TV}(P_0,P_1)=\sup_A|P_0(A)-P_1(A)|\), every binary decision has average error at least \((1-\mathrm{TV}(P_0,P_1))/2\). Taking two hypotheses inside a larger model gives a minimax lower bound. Yu's Lemma 1 presents the more general separated-parameter formulation using affinity and convex hulls.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]], equation (11), and [[research/xi_flow/findings/XF-204-randomized-jacobi-detection-has-a-sharp-error-stopping-tail|XF-204]], equation (17), explicitly use this classical mechanism. Their shared-seed couplings bound transcript total variation by a shrinking-region hit probability.

## Known scope and limits

The observation laws must come from fixed admitted inputs. Choosing an adversary after seeing the realized seed does not establish the claimed randomized bound. The testing theorem supplies neither the calibration witnesses nor pointwise termination; those are separate source-specific arguments. It has no RH conclusion.

## Related prior art

Yu compares the two-point method with Assouad and Fano methods. Shared use of this bound alone establishes no transfer between Mathia experiments.

## Evidence and provenance

- Bin Yu, *Assouad, Fano, and Le Cam*, in *Festschrift for Lucien Le Cam* (1997), 423–435, §29.2, Lemma 1, pp. 424–425: [Stanford-hosted scan](https://web.stanford.edu/class/stats300a/REFS/yu1997assouad.pdf).
- Live lookup triggers: `research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail.md`, “Prior art and boundary”; `research/xi_flow/findings/XF-204-randomized-jacobi-detection-has-a-sharp-error-stopping-tail.md`, “Checks, prior art, and consequences”.
