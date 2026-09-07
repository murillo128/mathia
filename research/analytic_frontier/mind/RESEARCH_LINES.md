# Analytic-frontier research lines

This file holds the current mathematical questions suggested by the durable analytic-frontier intuitions. It is not a roadmap, task queue, status page, or history.

## Convert Montgomery--Taylor projection taxes into separable-quotient stability

**Linked intuitions:** `MI-001-global-conjugation-geometry-carries-horizontal-information` and `MI-005-one-pair-collapse-is-curvature-seeded-before-higher-order-effects`.

ANF-081 closes every finite real multiset, ANF-083 gives a fixed complex-height strip independent of pair count, and ANF-085 proves all-height safety for separable center-height occupation. ANF-086 then gives a fixed Hilbert tube around that separable cone: any configuration defeating the affine certificate must stay a definite distance from the cone while being Montgomery--Taylor near-extremal. ANF-087--ANF-088 identify the exact extremizers and decompose near-extremal excess into explicit nonnegative projection, multiplicity, tensor-signature, and spectral-tail taxes.

ANF-089 makes the conditioning-to-geometry step quantitative. With `chi_s(W)=b_s(W)/a(W)`, where `a` is the source exponential Gram minimum and `b_s` the destination pair-collapse defect Gram maximum,

`d_sep(W)^2 <= [chi_s(W)/(2 q_s)] Delta(W)/L(W)`.

Thus bounded cross-metric conditioning closes every corresponding subclass. But ANF-090 supplies the decisive control: raw `chi_s` can diverge exponentially on product configurations that are themselves exactly separable and globally safe. The raw real-collapse condition number is therefore not an intrinsic measure of nonseparability and cannot be uniformly bounded on any broad class containing the safe cone.

The surviving all-cardinality gate is now **separable-quotient conditioning**. Either derive a direct projection-tax-to-`d_sep` estimate after removing the nearest safe product directions, or construct a genuinely nonseparable near-extremal family whose source ill-conditioning retains destination mass after that quotient. Generic pair count, height, multiplicity, exact rank, and raw Gram singularity are no longer the frontier.

## Treat relative Xi source reconstruction as solved until destination conditioning fails

**Linked intuition:** `MI-006-relative-xi-source-reconstruction-moves-the-gate-to-destination-conditioning`.

ANF-084 gives an unconditional moving-line relative periodization of the actual Xi source at `sigma_T=1+1/log T`, with Gaussian width `log T` and period `(log T)^3`. The function and fixed logarithmic derivatives are recovered with polynomial factors times `exp(-(log T)^4/8)`, while prime leakage is exponentially smaller on the relevant scale.

The live handoff is downstream: whether the source/reference transport reaches the finite guarded Xi state with enough quantitative margin. The existing Xi clue owns that cross-line question.

## Introduce higher-order carriers only after quotient-aware conditioning fails

ANF-088 shows that a complex near-extremizer must make specific finite exponential Gram/Schur complements anomalously small; ANF-089 converts one such conditioning ratio into a destination-distance estimate. ANF-090 then shows why raw source conditioning is too coarse: finite differences can make it arbitrarily bad inside the exact separable cone.

Before introducing a higher-order carrier, quotient away the already-safe separable directions and test whether the remaining near-extremal taxes can still support destination mass. A higher-order mechanism becomes justified only after a concrete **nonseparable** family survives both the exact projection-tax controls and a quotient-aware separable-distance test.

## Keep diffraction realizability separate from the affine counting certificate

Any spectral or geometric reformulation still has to prove that the proposed object exists with the required positivity, support, normalization, and conjugation properties. A suggestive diffraction or operator picture is not evidence unless it reproduces the exact affine certificate and survives the same matched controls.