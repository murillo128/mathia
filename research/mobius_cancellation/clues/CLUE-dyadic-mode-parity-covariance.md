---
id: CLUE-mobius-cancellation-dyadic-mode-parity-covariance
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-033-annular-product-fiber-sign-coherence.md
  - research/mobius_cancellation/findings/MC-034-random-multiplicative-annulus-critical-rms.md
  - research/visual_exploration/visualizations/mobius-huxley-dyadic-mode-parity.md
  - research/visual_exploration/clues/CLUE-mobius-huxley-zscore-scale-geometry.md
---

# Does matched cross-kernel covariance explain the alternating dyadic sign geometry in the fixed Huxley–Watt panel?

## Observation

The fixed, validated issue-#105 panel has no scalar anomaly: all individual Möbius z-scores lie inside `|Z| <= 2.429`. A joint visual inspection nevertheless exposes a post-hoc dyadic sign template across the six reciprocal modes `h=2^j`: after multiplying by `p_j=(-1)^(j+1)`, `31/36` cells are positive. The pattern survives every single-scale deletion (`25` to `28` matches out of `30`) and every single-mode deletion (`25` to `26` out of `30`), with aggregate signed alignment remaining between `0.840` and `0.963` or between `0.859` and `0.932`, respectively.

This cannot be interpreted with independent-binomial intuition. In `MC-034`, every bounded radial kernel is evaluated on the same random multiplicative prime-sign character, so different reciprocal modes have a nontrivial exact covariance that the scalar z-score normalization does not remove.

## Research question

Does that exact matched-control cross-kernel covariance already explain the observed alternating dyadic sign geometry, or does the deterministic Möbius point remain unusually aligned after the joint covariance is quotiented?

For fixed `N` and reciprocal kernels `K_j(x)=sin(2 pi 2^j x)`, `MC-034` gives coefficient vectors `W_(N,j)(a)`. The same Walsh orthogonality used there yields the exact covariance matrix

`C_N(j,k) = sum_(a>1) W_(N,j)(a) W_(N,k)(a)`.

Let `D_N=diag(sigma_(N,j))`, where `sigma_(N,j)^2=C_N(j,j)`, and let `R_N=D_N^(-1) C_N D_N^(-1)` on nondegenerate coordinates. For the fixed template `p=(-1,+1,-1,+1,-1,+1)` and the observed z-score vector `z_N`, a natural joint diagnostic is

`T_N = p^T z_N / sqrt(p^T R_N p)`.

Under the matched random multiplicative ensemble, this linear statistic has mean zero and variance one whenever the denominator is nonzero. The question is whether the Möbius values remain ordinary under this exact joint normalization.

## Why it may matter

`MC-034` already shows that each individual Huxley–Watt annular kernel has the correct critical power scale in matched-control RMS, but it does not classify relations between kernels. If the alternating visual pattern collapses to an order-one `T_N`, it is a concrete explanation for why a striking signed picture is still only joint-kernel control geometry. If it survives the exact covariance quotient strongly enough to merit further work, it isolates a much sharper deterministic target than another collection of marginal z-scores: correlation of the all-minus Möbius prime-sign point with a specific cross-kernel direction in the Huxley–Watt weight family.

## Decisive test

Reconstruct the same `W_(N,j)(a)` vectors used by issue #105 for the existing fixed panel only. First verify `C_N(j,j)` against the already-persisted `sigma_(N,j)^2` values; then compute `R_N`, `p^T R_N p`, and `T_N` for the six existing scales. Do not add new `N`, new kernels, optimized sign templates, or fitted mode weights before this control is evaluated.

Kill the visual lead if the alternating direction is ordinary under the exact joint matched-control covariance. If it remains unusually large across the fixed scales, the next step must still test higher-moment/non-Gaussian behavior and deterministic matched multiplicative comparators before treating it as an arithmetic-specific mechanism.

## Evidence boundary

The `31/36` sign agreement and alignment ratios are finite, post-hoc descriptors of one fixed panel. No independence assumption, binomial p-value, Gaussian joint law, asymptotic dyadic parity law, novelty claim, Mertens estimate, or RH consequence is established. The covariance identity is an immediate cross-kernel consequence of the Walsh orthogonality already used in `MC-034`; what remains unknown is the value and explanatory power of that covariance for this specific fixed mode family and the deterministic Möbius point.

## Research disposition

Accepted for a bounded exact matched-control test. The mathematical premise is already grounded by `MC-034`: the six reciprocal kernels share the same square-free Walsh characters, so their covariance is the deterministic Gram matrix of the corresponding `W_(N,j)` vectors. The fixed panel and post-hoc template are frozen by issue #105 and the retained visualization, so the missing quantity can be evaluated without adding a new search degree of freedom.

The unresolved question is only whether the fixed alternating direction remains unusual after normalization by its full matched-control covariance. That finite computation has been delegated as GitHub issue #107. Acceptance does not validate the visual pattern, assign it a p-value, or establish any asymptotic Möbius structure; a durable mathematical continuation would still require higher-moment or deterministic arithmetic control if the joint statistic survives.