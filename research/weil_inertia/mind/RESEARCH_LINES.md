# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Leave generic fixed-aperture feature geometry and retain source-specific signed covariance

**Linked intuitions:** `MI-036-exact-zero-density-locks-bow-reciprocal-scale-at-riemann-siegel-length` through `MI-049-phase-orbit-dimension-is-the-complexity-currency-between-projective-and-generic-bow-geometry`.

WI-331--WI-342 classify ordinary local Gowers smallness and its scalar repairs at the bow scale. Matched-energy Rademacher sources survive below the relevant deterministic walls; deleting diagonals, sparse geometric deletion, deterministic scalar reweighting, linear mixing of orders and canonical multiplicative-derivative coupling all remain inside generic Walsh/cube quotients rather than forcing the distinguished `Lambda-Lambda^sharp` covariance sign.

WI-343--WI-352 classify generic feature enrichment at fixed logarithmic aperture. Linear, fixed-degree, uniformly analytic, projective-continuous and ordinary phase-sensitive feature families all pay an explicit source-resolution or sensitivity/transmission tariff if their normalized output Gram rank grows. The destination remains source-specific signed covariance. The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` is still the clean test: retain `Lambda^sharp` in the same norm and prove the required negative off-diagonal contribution, or prove that the proposed statistic cannot force it.

## Keep compressed pair correlation separate from full localized Weil energy

**Linked intuitions:** `MI-010-pair-correlation-slack-is-a-shared-exceptional-budget` and `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing`.

WI-354 audits Wang's September 2026 short-interval pair-correlation theorem against sparse-defect exclusion. Its present arithmetic interface needs a strict Fourier-support versus interval-length gap, and after normalization by the local zero count every fixed-power interval still tolerates finitely many or zero-density off-critical defects. The cheap bootstrap

`bulk proportion -> shorter windows -> individual-defect exclusion`

therefore fails for that compressed statistic.

WI-355 shows that this blindness is interface-specific rather than a universal localization obstruction. Suzuki's localized full Weil form has lowest energy

`lambda(a)=inf Q_W(v)/||v||_2^2`

on test functions supported in `(-a,a)`. The imported theory gives continuity, positivity for sufficiently small `a`, and `not RH` iff `lambda(a)<0` for some finite `a`. Nested test spaces add the exact monotonicity `lambda(b)<=lambda(a)` for `b>a`. Hence any RH failure has a canonical finite first-crossing radius `a_*` with `lambda(a_*)=0`, and zero is then a ground-state eigenvalue of the localized operator.

At fixed radius the arithmetic kernel uses only prime powers `n<=e^(2a)`. Thus a hypothetical RH failure has a finite-radius witness with finite prime-power input even though the localized operator remains infinite-dimensional. This does not make positivity automatically decidable, but it removes the need for cofinal negative-index stability merely to detect a failure.

The live source-side problem is therefore to prove coercivity `Q_W^a(v)>=c(a)||v||_2^2` with `c(a)>0` for every finite `a`, or derive a propagation rule preventing the first zero crossing as successive prime-power thresholds enter the localized kernel. Pair-correlation improvements remain useful only if their compressed output is coupled to an individual-defect-sensitive coercive mechanism.

## Keep feature resolution, localization support and defect normalization as separate currencies

The current ledger now contains genuinely different localization channels. Feature geometry prices source resolution, transmission, phase-orbit complexity and covariance sign. Short-interval pair correlation prices vertical interval length, Fourier support, prime-side error and normalization by local zero count. Full localized Weil energy instead retains the complete quadratic form and has a monotone variational ground state.

A proposed bridge should state which channel supplies individual-defect sensitivity. Stronger matrix inequalities cannot repair information already erased by pair-correlation normalization, while WI-355 demonstrates that changing to an uncompressed variational observable can alter that detectability. Conversely, finite-radius detectability is not yet a proof of positivity at every radius; the missing source-side coercivity remains the RH-facing step.
