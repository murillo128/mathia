---
id: CLUE-analytic-frontier-even-moment-radial-coercivity
type: research-clue
status: resolved
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-045-two-pair-five-point-obstruction-scalarizes-to-a-strict-hilbert-coherence-gap.md
  - research/analytic_frontier/findings/ANF-057-reciprocal-sinh-control-sharpens-the-support-free-relative-height-tube.md
  - research/analytic_frontier/findings/ANF-059-exact-montgomery-taylor-curvature-transform-shrinks-the-five-point-separation-annulus.md
  - research/analytic_frontier/findings/ANF-061-quadratic-height-renormalization-closes-the-common-translation-escape.md
  - research/analytic_frontier/findings/ANF-062-validated-interval-certificate-proves-montgomery-taylor-five-point-zero-freeness.md
  - research/analytic_frontier/findings/ANF-063-endpoint-anti-concentration-closes-all-moment-orders-from-nine.md
  - research/analytic_frontier/findings/ANF-064-validated-finite-moments-complete-sharp-montgomery-taylor-radial-coercivity.md
---

# Does an even-moment inequality give the sharp all-height five-point margin?

## Observation

`ANF-062` certified the exact fixed Montgomery--Taylor five-point defect `H_MT>0`, but its direct interval cover did not explain the apparent radial rigidity of the defect. Writing

`M_n(t)=∫ α^(2n) J_MT(α) cos(2παt) dα`,

with `M_1=K_MT`, the exact height expansion from `ANF-045` suggested the stronger all-order condition

`M_n(t)/M_n(0) ≥ −2^(2n−1)/(1+2^(2n−1))`

for every integer `n≥2` and every real `t`. If true, that condition makes every height coefficient beyond the quadratic one nonnegative. The quadratic coefficient has exact floor `2π²m5`, where `m5=2M_1(0)+3 inf_t M_1(t)`.

## Research question

Does the displayed moment inequality hold globally for the exact Montgomery--Taylor spectrum, and therefore imply the sharp all-height coercivity bound

`H_MT ≥ 2π²m5 (y1²+y2²)`

with normalized defect nondecreasing under simultaneous height dilation?

The sufficient bridge is explicit. For `yj=λfj`, `f1,f2>0`, `d=t1−t2`, `A_n=f1^(2n)+f2^(2n)` and `B_n=(f1+f2)^(2n)+(f1−f2)^(2n)`, the coefficient of `λ^(2n)` in `H_MT` is `(2π)^(2n)/(2n)!` times

`2^(2n−1) A_n M_n(0) + f1^(2n) M_n(t1) + f2^(2n) M_n(t2) + B_n M_n(d)`.

The elementary inequality `B_n≤2^(2n−1)A_n` converts the proposed moment bound into nonnegativity of every coefficient for `n≥2`.

## Why it may matter

This replaces a large direct sign certificate by a structural explanation of five-point positivity and identifies the sharp boundary constant. It also separates spectra that merely pass the infinitesimal curvature gate from those whose entire positive-height expansion is radially coercive.

## Decisive test

Prove the moment bound uniformly in both `n` and `t`, allowing validated finite-order certificates only when the remaining moment orders and all horizontal tails are controlled analytically. Alternatively, one certified violating order would kill this sufficient route, though not necessarily five-point positivity itself because the coefficient estimate discards linkage between the three horizontal arguments.

## Evidence boundary

The question is now resolved for the fixed Montgomery--Taylor five-point profile. The resulting theorem does not classify all near-minimizers, extend automatically to another spectrum, settle larger conjugation-invariant multisets, or imply RH. The finite orders `n=2,...,8` remain computer-assisted statements backed by outward-rounded interval arithmetic; orders `n≥9` are analytic consequences of `ANF-063`.

## Research disposition

Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-063-endpoint-anti-concentration-closes-all-moment-orders-from-nine.md]]
- [[research/analytic_frontier/findings/ANF-064-validated-finite-moments-complete-sharp-montgomery-taylor-radial-coercivity.md]]

`ANF-063` removes the infinite moment-order tail analytically, proving the required inequality for every `n≥9` and every real frequency. The validated finite certificate canonicalized in `ANF-064` closes exactly the residual orders `n=2,...,8`, with a uniform positive order-two margin. Research Watch independently reconstructed the coefficient identity and obtains

`H_MT ≥ 2π²m5(y1²+y2²) + 2π⁴(0.00082277)(y1²+y2²)²`.

All coefficients above the quadratic one are in fact strictly positive for genuine two-pair shapes, so `H_MT(λf1,λf2;t1,t2)/λ²` is strictly increasing for `λ>0`. The sharp constant `2π²m5` is approached only on the degenerate zero-height, one-pair boundary. The clue's structural question is therefore closed; the remaining five-point work is the finer rigidity and classification of near-minimizing boundary sequences.