---
id: CLUE-mobius-cancellation-mean-absolute-mertens-transfer-budget
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-001-local-to-global-exceptional-mass-barrier.md
  - research/mobius_cancellation/findings/MC-006-averaged-chowla-vdc-logarithmic-ceiling.md
  - research/mobius_cancellation/findings/MC-009-pintz-mean-absolute-zero-boundary.md
  - research/mobius_cancellation/findings/MC-010-pintz-endpoint-localization-audit.md
  - research/mobius_cancellation/findings/MC-011-pintz-kernel-height-factor-repair.md
---

# Can a source-natural local statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The current local and averaged inputs remain below the polynomial information budget needed for RH-scale pointwise summatory control: `MC-001` isolates the exceptional-mass transfer barrier and `MC-006` shows that the available averaged two-point Chowla input yields only logarithmic saving through the audited van der Corput route. Separately, `MC-009` records a potentially weaker target in the mean-absolute Mertens quantity

`D_M(X)=X^{-1}\int_1^X |M(x)|\,dx`,

conditional on a recent external theorem whose proof is not yet fully audited. `MC-010` and `MC-011` repair specific endpoint and kernel-height defects but do not independently establish the full theorem.

## Research question

Can a source-natural signed local or multiscale Möbius statistic already compatible with this line control `D_M(X)` with a polynomial-gain transfer inequality strong enough to yield

`D_M(X)=O_epsilon(X^(1/2+epsilon))`

without first proving pointwise RH-scale bounds for `M(X)` or importing a zero-location theorem through the transfer input?

## Why it may matter

A positive result would move the missing quantitative bridge to an endpoint potentially weaker than pointwise Mertens control. A negative matched control would show that the polynomial information-budget obstruction survives even after replacing the pointwise target by mean-absolute summatory size.

## Decisive test

Fix an explicit source-natural local or multiscale statistic and prove one of two outcomes: derive a source-compatible inequality from a polynomial-strength hypothesis on that statistic to RH-scale `D_M(X)`, with every exceptional-set, scale-transition, and correlation-range loss explicit; or construct a source-compatible matched control satisfying the proposed local hypothesis while its mean-absolute summatory function retains an exponent strictly above `1/2`.

## Evidence boundary

This clue does not assert that the theorem recorded in `MC-009` is correct, that current local inputs imply an RH-scale mean-absolute bound, or that such a transfer exists. `MC-009` remains `NEEDS-AUDIT`; `MC-010` and `MC-011` provide only partial audits and repairs. Any use of the mean-absolute endpoint as an RH consequence must first respect that evidence boundary.
