---
id: CLUE-xi-flow-common-baseline-quotient-jacobi-acquisition
type: research-clue
status: accepted
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

AF-568 is a generalized-prime **real** identification experiment with a free output origin; its constants and query count are not Jacobi theorems. XF-194/195/196 do not cover a shared unknown complex baseline. No quotient-stable `O(Q)` construction, converse beyond the original `Omega(Q)`, source-faithful Xi measurement implementation, zero-exclusion or RH implication is yet established.

## Research disposition

Accepted as a distinct acquisition-nuisance question. For a fixed bank of `M` scales, fitting one unrestricted complex baseline is exactly projection off the constant vector: `inf_(c in C) ||v-c1||_2 = ||(I-11*/M)v||_2`. XF-197's pointwise and Euclidean margins do not alone establish a projected margin: a constant comparison vector projects to zero. The decisive source-specific test is a uniform lower bound on **within-block centered** complete-Jacobi finite chords over the smaller candidate radius's matched block, followed by assembly of at most `O(Q)` distinct rows under one fixed total `ell^2` noise budget. The zero-transcript lower bound persists with baseline zero. AF-568 makes the additive-origin nuisance substantive, but its real-profile constants and three-query conclusion do not transfer to Jacobi. This acceptance establishes neither quotient stability nor physically justified Xi-source access.
