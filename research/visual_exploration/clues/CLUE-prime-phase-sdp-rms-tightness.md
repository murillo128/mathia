---
id: CLUE-visual_exploration-prime-phase-sdp-rms-tightness
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-213-worst-start-prime-phase-torus-optimization.md
  - research/visual_exploration/findings/VIS-216-normalized-magnetic-gap-certificate.md
  - research/visual_exploration/findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md
  - research/visual_exploration/findings/VIS-220-simple-cycle-packing-universal-envelope-ceiling.md
  - research/visual_exploration/findings/VIS-221-sdp-stress-certificate-retains-torus-interactions.md
---

# Can the full correlation SDP compress prime-phase worst starts to Haar-RMS scale?

## Observation

`VIS-218` closes the normalized magnetic-ground-state relaxation throughout the strictly subcritical regime, and `VIS-220` closes the fractional simple-cycle packing relaxation by a universal envelope ceiling. Neither result lower-bounds the exact torus optimum from `VIS-213`.

`VIS-221` identifies a strictly stronger static certificate family. The correlation SDP preserves one unit diagonal constraint per prime and all pairwise Hermitian couplings. Its dual allows an independent diagonal stress at every vertex; the `VIS-216` magnetic bound is only the special dual ansatz in which that stress is proportional to weighted degree on each connected component. When a stationary torus point has positive-semidefinite stress, the SDP is rank-one tight and certifies the exact finite torus optimum.

The live quantitative question is therefore whether this stronger global interaction relaxation reaches the destination scale that the weaker certificates cannot.

## Research question

For the canonical prime coefficient matrices `A_(y,H)` in the strictly subcritical regime, what is the asymptotic scale of

`U_abs(y,H)=max(U_+(A_(y,H)),U_+(-A_(y,H)))`,

where `U_+` is the correlation-matrix SDP from `VIS-221`?

Does

`U_abs(y,H)=O(sqrt(R_v(y,H)))`

hold in any nontrivial growing regime, or does the SDP itself remain parametrically above Haar RMS? When finite SDP solutions are rank one, can their stationary stress matrices be certified positive semidefinite and thereby solve the exact fixed-modulus torus problem at those parameters?

## Why it may matter

This is the first post-`VIS-220` certificate in the current branch that is not already ruled out by the known spectral or simple-cycle ceiling. A bounded SDP/RMS ratio would immediately prove a static worst-start bound for the true torus objective, because the SDP is an upper relaxation. Rank-one tightness would be even stronger: it would identify and certify the exact finite torus maximizer.

Conversely, a large high-rank SDP value would diagnose failure of this certificate without falsely promoting the relaxation gap into an arithmetic obstruction. That clean separation is important after two earlier relaxation families were shown to be destination-scale insufficient.

## Decisive test

Freeze a growing family of canonical `(y,H)` values and, for both signs of `A_(y,H)`, evaluate or analytically bound the SDP

`max Tr(±A X)` subject to `X>=0`, `diag(X)=1`.

Normalize by the exact Haar scale `sqrt(R_v(y,H))` and track the SDP rank/eigenvalue profile and dual stress. The mathematical target is not merely a numerical decrease relative to the coefficient envelope. Prove one of the following:

1. `U_abs/sqrt(R_v)=O(1)` in a stated growing regime, which gives a genuine RMS-scale upper bound on the exact torus optimum;
2. rank-one tightness with the `VIS-221` stationary PSD stress certificate, which gives the exact finite torus optimum;
3. an asymptotic lower bound on the SDP value showing `U_abs/sqrt(R_v)->infinity`, which closes this **certificate** at RMS scale but leaves the exact torus optimum open unless accompanied by a matching torus lower bound.

Use matched controls preserving the weight matrix while scrambling only admissible edge phases when interpreting any arithmetic specificity. A finite numerical panel is exploratory until converted into a durable analytic bound or exact certificate.

## Evidence boundary

`VIS-221` proves the SDP hierarchy and exact rank-one stress certificate; it does not estimate the SDP value for the prime matrices. The classical phase-synchronization literature shows that SDP tightness can occur in structured/noisy synchronization models, but no such theorem is imported for the deterministic prime-phase matrices here.

A bounded SDP/RMS ratio would be sufficient evidence for a static pointwise upper bound. A divergent high-rank SDP/RMS ratio would **not** prove that prime-phase worst starts are large; it would show only that this convex relaxation is too loose at the desired scale. One-parameter prime-log access time remains separate from this static question.
