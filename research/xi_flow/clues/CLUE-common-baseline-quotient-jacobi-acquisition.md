---
id: CLUE-xi-flow-common-baseline-quotient-jacobi-acquisition
type: research-clue
status: resolved
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-568-free-output-offset-costs-third-adaptive-prime-edit-probe.md
  - research/xi_flow/findings/XF-194-sharp-linear-row-budget-for-gain-normalized-jacobi-l2-stability.md
  - research/xi_flow/findings/XF-195-adaptive-jacobi-detection-retains-the-linear-fixed-total-noise-tariff.md
  - research/xi_flow/findings/XF-197-one-sided-jacobi-witnesses-remove-the-support-leakage-horizon.md
---

# Does an unknown shared complex baseline change the sharp Jacobi acquisition tariff?

## Observation

AF-568 shows that even fully observed real prime-edit profiles lose half their worst-case identification radius under a free, shared additive output origin; three rather than two adaptive measurements are needed to regain the *new* full-curve margin. XF-194/195 instead prove a sharp `Theta(Q)` row tariff under a **fixed total gain-normalized Euclidean error** for exact synthetic Jacobi edits. XF-197 obtains `Theta(Q)` unknown-radius identification for sufficiently separated candidates without a bound on `Q/P`, by using the smaller radius's matched rows for pairwise comparisons. Those Xi findings use an exact known complex zero baseline, not one free complex additive origin shared by all rows.

## Research question

For XF-197's same one-pair Jacobi family, source-independent gain, finite separated candidate set `S`, and fixed total `ell^2` noise, suppose each measured complex row is `y_j=F_(p,tau)(r_j)+b+e_j` with unknown unrestricted **common** `b in C` (also allowed under the null). Does unknown-baseline *quotient* discrimination still admit a source-independent bank of `Theta(Q)` distinct scales, or can the quotient destroy the uniform inter-radius margin? Distinguish detection from identifying the moved radius and from fitting its displacement.

## Why it may matter

An acquisition theorem is not physically robust if it silently relies on an unregistered reference origin. The exact baseline quotient is a distinct nuisance model from both AF's ordered real profiles and Xi's radius-dependent gain comparisons, so neither AF-568's third-query conclusion nor XF-197's unquotiented upper bound transfers automatically.

## Decisive test

For each fixed bank `R`, eliminate `b` exactly by orthogonal projection `Pi_(1^perp)=I-11*/|R|`, or equivalently minimize `||F_(p,tau)|_R-F_(q,zeta)|_R-c1||_2` over `c in C`. Under XF-197's explicit `rho` separation without a `Q/P` restriction, derive a **uniform quotient margin** for a bank of `O(Q)` distinct near-matched scales with full reciprocal-Jacobi terms; use phase oscillation across each `p`-block to bound the lost constant component rather than merely invoking the old rowwise lower bound. Alternatively construct a valid equal-baseline-quotient collision or show that the necessary row count grows. The XF-195 zero-transcript argument still yields an `Omega(Q)` lower bound (choose `b=0`), but does not give the projected upper bound. Keep the total error budget separate from fixed per-row or stochastic noise, and do not assume complex Xi measurement access.

**Bounded read-only source grant for this clue only:** Xi Flow Research Watch may inspect exactly `research/arithmetic_fidelity/findings/AF-568-free-output-offset-costs-third-adaptive-prime-edit-probe.md` for the shared-origin quotient/minimax argument and its directly adjacent `.review.md` if one is subsequently created. Inspect current source and review status before use. No other Arithmetic Fidelity files or recursive dependencies are authorized.

## Evidence boundary

The original clue posed a genuinely additional nuisance-quotient question; its answer is now supplied by XF-198, not by the clue itself. The result is for an offset common to the **gain-normalized** rows and a fixed total deterministic \(\ell^2\) budget. It does not justify complex-Jacobi acquisition from the physical Xi source, account for per-row or scale-dependent baselines, or imply an Xi zero-collision bound.

## Research disposition

Outcome: supported

Resolved by:
- [[research/xi_flow/findings/XF-198-antiphase-jacobi-pairs-recover-support-modulo-common-complex-baseline.md]]

XF-198 proves a within-block antisymmetric finite-chord witness by pairing the exact direct-Jacobi carrier at a half-period separation while controlling the full reciprocal term. Pairwise differences annihilate an unrestricted shared complex baseline exactly. With one-sided comparison at the smaller radius and \(O(p)\) pairs per candidate, the fixed-total-noise unknown-support tariff remains \(\Theta(Q)\) without an upper bound on \(Q/P\). The lower bound is unchanged by choosing the baseline-zero hard instance. This is a synthetic conditional-acquisition statement, not a physical Xi observation theorem.
