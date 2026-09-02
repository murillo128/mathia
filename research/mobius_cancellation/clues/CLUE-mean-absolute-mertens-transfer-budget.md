---
id: CLUE-mobius-cancellation-mean-absolute-mertens-transfer-budget
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-001-local-to-global-exceptional-mass-barrier.md
  - research/mobius_cancellation/findings/MC-006-averaged-chowla-vdc-logarithmic-ceiling.md
  - research/mobius_cancellation/findings/MC-009-pintz-mean-absolute-zero-boundary.md
  - research/mobius_cancellation/findings/MC-010-pintz-endpoint-localization-audit.md
  - research/mobius_cancellation/findings/MC-011-pintz-kernel-height-factor-repair.md
  - research/mobius_cancellation/findings/MC-012-pintz-section7-window-parameter-repair.md
  - research/mobius_cancellation/findings/MC-013-discrete-tanaka-l1-feedback-carrier.md
  - research/mobius_cancellation/findings/MC-014-character-control-tanaka-cancellation-excursion-square-budget.md
  - research/mobius_cancellation/findings/MC-015-qualitative-chowla-excursion-square-obstruction.md
---

# Can a source-natural local statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The current local and averaged inputs remain below the polynomial information budget needed for RH-scale pointwise summatory control: `MC-001` isolates the exceptional-mass transfer barrier and `MC-006` shows that the available averaged two-point Chowla input yields only logarithmic saving through the audited van der Corput route. Separately, `MC-009` records a potentially weaker target in the mean-absolute Mertens quantity

`D_M(X)=X^{-1}\int_1^X |M(x)|dx`,

conditional on a recent external theorem whose proof is not yet fully audited. `MC-010`, `MC-011`, and `MC-012` repair specific endpoint, kernel-height, and Section-7 window defects but do not independently establish the full theorem.

## Research question

Can a source-natural signed local or multiscale Möbius statistic already compatible with this line control `D_M(X)` with a polynomial-gain transfer inequality strong enough to yield

`D_M(X)=O_epsilon(X^(1/2+epsilon))`

without first proving pointwise RH-scale bounds for `M(X)` or importing a zero-location theorem through the transfer input?

## Why it may matter

A positive result would move the missing quantitative bridge to an endpoint potentially weaker than pointwise Mertens control. A negative matched control would show that the polynomial information-budget obstruction survives even after replacing the pointwise target by mean-absolute summatory size.

## Decisive test

Fix an explicit source-natural local or multiscale statistic and prove one of two outcomes: derive a source-compatible inequality from a polynomial-strength hypothesis on that statistic to RH-scale `D_M(X)`, with every exceptional-set, scale-transition, and correlation-range loss explicit; or construct a source-compatible matched control satisfying the proposed local hypothesis while its mean-absolute summatory function retains an exponent strictly above `1/2`.

## Evidence boundary

This clue does not assert that the theorem recorded in `MC-009` is correct, that current local inputs imply an RH-scale mean-absolute bound, or that such a transfer exists. `MC-009` remains `NEEDS-AUDIT`; `MC-010`, `MC-011`, and `MC-012` provide only partial audits and repairs. Any use of the mean-absolute endpoint as an RH consequence must first respect that evidence boundary.

## Research disposition

Accepted in narrowed form after `MC-013` identified an exact candidate interface and `MC-014` stress-tested how that interface may be used. The discrete Tanaka decomposition gives a source-natural signed carrier `mu(n) * sgn(M(n-1))` plus a zero-departure local-time term, but `MC-014` shows with the completely multiplicative character modulo `3` that these two triangular components can each be quadratic while their sum has only linear size. Independent polynomial bounds for the two components are therefore not a cancellation-faithful generic route.

The surviving candidate is coupled excursion-level information. If `ell_j` are the lengths of maximal blocks on which the Mertens partial sum is nonzero, `MC-014` proves the exact pathwise transfer

`N D_M(N) <= (sum_j ell_j^2 + N)/2`.

`MC-015` now supplies a direct matched-control obstruction at this interface: the exact-support qualitative-Chowla sequence from `MC-004` has, along a subsequence, `D_a(N) >> N/log^2 N` and `sum_j ell_j^2 >> N^2/log^2 N`. Thus exact Möbius square-free support plus all qualitative fixed-shift Chowla limits are still insufficient even for the weaker mean-absolute endpoint and cannot yield the required excursion-square estimate as a black box.

The active residual question is therefore stricter: can genuinely **quantitative growing-scale** correlation/local information, or specifically multiplicative consistency that rules out the sparse coherent blocks of `MC-015`, control the excursion-length second moment or a truncated multiscale tail with polynomial strength? The clue remains accepted rather than resolved because no such arithmetic estimate is currently established.