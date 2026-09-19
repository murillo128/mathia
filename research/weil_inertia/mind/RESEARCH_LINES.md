# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Leave generic fixed-aperture feature geometry and retain source-specific signed covariance

**Linked intuitions:** `MI-036-exact-zero-density-locks-bow-reciprocal-scale-at-riemann-siegel-length` through `MI-049-phase-orbit-dimension-is-the-complexity-currency-between-projective-and-generic-bow-geometry`.

WI-331--WI-342 classify ordinary local Gowers smallness and its scalar repairs at the bow scale. Matched-energy Rademacher sources survive below the relevant deterministic walls; deleting diagonals, sparse geometric deletion, deterministic scalar reweighting, linear mixing of orders and canonical multiplicative-derivative coupling all remain inside generic Walsh/cube quotients rather than forcing the distinguished `Lambda-Lambda^sharp` covariance sign.

WI-343--WI-352 classify generic feature enrichment at fixed logarithmic aperture. Linear, fixed-degree, uniformly analytic, projective-continuous and ordinary phase-sensitive feature families all pay an explicit source-resolution or sensitivity/transmission tariff if their normalized output Gram rank grows. The destination remains source-specific signed covariance. The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` is still the clean test: retain `Lambda^sharp` in the same norm and prove the required negative off-diagonal contribution, or prove that the proposed statistic cannot force it.

## Keep compressed pair correlation separate from full localized Weil energy and use the correct threshold topology

**Linked intuitions:** `MI-010-pair-correlation-slack-is-a-shared-exceptional-budget` and `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing`.

WI-354 audits Wang's September 2026 short-interval pair-correlation theorem against sparse-defect exclusion. Its present arithmetic interface needs a strict Fourier-support versus interval-length gap, and after normalization by the local zero count every fixed-power interval still tolerates finitely many or zero-density off-critical defects. The cheap bootstrap `bulk proportion -> shorter windows -> individual-defect exclusion` therefore fails for that compressed statistic.

WI-355 shows that this blindness is interface-specific rather than a universal localization obstruction. Suzuki's localized full Weil form has lowest energy `lambda(a)=inf Q_W(v)/||v||_2^2` on test functions supported in `(-a,a)`. The imported theory gives continuity, positivity for sufficiently small `a`, and `not RH` iff `lambda(a)<0` for some finite `a`; nested test spaces give monotonicity. Hence any RH failure has a canonical finite first-crossing radius `a_*` with `lambda(a_*)=0`, and zero is then a ground-state eigenvalue. At fixed radius the arithmetic kernel uses only prime powers `n<=e^(2a)`.

WI-356 identifies the topology needed to study the discrete prime-power thresholds inside that first-crossing program. When a new prime power `q` activates at `a_q=(log q)/2`, the corresponding compressed-translation channel is **not** small in bounded-operator norm on `L^2(-1,1)`: for every `a>a_q` sufficiently close to the threshold its norm is exactly `Lambda(q)/sqrt(q)`, while it is zero at the threshold itself. Thus ordinary `L^2` norm-continuous perturbation induction is exactly false.

The same channel is nevertheless infinitesimally small relative to Suzuki's universal logarithmic form. Writing `epsilon=2-log(q)/a`, WI-356 proves

`|P_(q,a)(w)| <= [2 Lambda(q)/sqrt(q)] / log(1/(2 epsilon)) * L(w)`.

The coefficient tends to zero as `a downarrow a_q`. Norm-saturating witnesses must concentrate order-one mass in shrinking endpoint strips and therefore have divergent logarithmic form energy. The viable threshold interface is consequently form coercivity, not `L^2` operator norm.

The live source-side problem is now sharper: prove enough pre-threshold coercive reserve in the logarithmic form topology, bound the logarithmic energy of a hypothetical first-crossing null state, or use the exact null/source equation to prevent a threshold crossing. Merely observing that the new overlap strip is short is insufficient unless the argument prices endpoint concentration through the same form that makes it expensive.

## Keep feature resolution, localization support, defect normalization and perturbation topology as separate currencies

The current ledger now contains genuinely different localization channels. Feature geometry prices source resolution, transmission, phase-orbit complexity and covariance sign. Short-interval pair correlation prices vertical interval length, Fourier support, prime-side error and normalization by local zero count. Full localized Weil energy retains the complete quadratic form and has a monotone variational ground state. WI-356 adds another distinct currency: a perturbation can be singular in `L^2` operator norm while vanishing in the form topology relevant to bounded-energy states.

A proposed bridge should therefore state which channel supplies individual-defect sensitivity and which topology controls threshold activation. Stronger matrix inequalities cannot repair information already erased by pair-correlation normalization, while bounded-operator perturbation theory cannot exploit a channel that jumps in norm. Conversely, form-smallness alone does not prove positivity propagates; the missing source-side coercivity remains the RH-facing step.
