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
  - research/mobius_cancellation/findings/MC-013-discrete-tanaka-l1-feedback-carrier.md
  - research/mobius_cancellation/findings/MC-016-random-walk-excursion-overconstraint-path-energy.md
  - research/mobius_cancellation/findings/MC-019-path-energy-coarse-riesz-rh-equivalence.md
  - research/mobius_cancellation/findings/MC-044-growing-riesz-endpoint-visibility-delay.md
  - research/mobius_cancellation/findings/MC-115-mean-absolute-mertens-mellin-zero-free.md
---

# Can a source-natural local statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The current local and averaged inputs remain below the polynomial information budget needed for RH-scale summatory control. `MC-001` isolates the exceptional-mass barrier for almost-all short intervals, while `MC-006` shows that the available averaged two-point Chowla input yields only logarithmic saving through the audited black-box van der Corput route.

The endpoint is now cleaner than when this clue was created. Define

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` proves directly, without the fresh Pintz theorem, that

`RH iff D_M(X)=O_epsilon(X^(1/2+epsilon)) for every epsilon>0`.

The reason is absolute Mellin convergence: an RH-scale upper bound for the first absolute moment analytically continues `1/zeta(s)` into every half-plane `Re(s)>1/2+epsilon` and therefore excludes off-critical zeros. `MC-009` now has a narrower role: Pintz's still-audited theorem proposes the stronger full logarithmic-order identity tying `D_M`, a terminal-window maximum, and the rightmost zero boundary.

## Research question

Can a source-natural signed local, bilinear, multiplicative, or multiscale Möbius statistic control `D_M(X)` with a genuine polynomial-gain transfer inequality strong enough to yield

`D_M(X)=O_epsilon(X^(1/2+epsilon))`

without first proving a pointwise RH-scale bound for `M(X)` or inserting an equivalent global/coarse statistic into the hypotheses?

The missing bridge is now entirely arithmetic: once the mean-absolute estimate is proved, zero exclusion is automatic by `MC-115`.

## Why it may matter

Mean-absolute control is formally weaker than pointwise Mertens control and is insensitive to some sparse pointwise spikes. It is nevertheless RH-complete. A successful transfer to this endpoint could therefore avoid solving a needlessly strong uniform problem while still closing the RH implication exactly.

Conversely, a matched control showing that the proposed local information coexists with mean-absolute exponent strictly above `1/2` would demonstrate that the local-to-global information budget remains insufficient even for this weaker endpoint.

## Decisive test

Fix an explicit source-natural statistic and prove one of two outcomes:

1. derive a source-compatible implication from a quantitatively polynomial hypothesis on that statistic to `D_M(X)=O_epsilon(X^(1/2+epsilon))`, with exceptional sets, scale transitions, correlation range, coarse modes, smoothing, and reconstruction losses explicit; or
2. construct a source-compatible matched control satisfying the proposed local/multiscale hypothesis while its mean-absolute partial-sum process retains exponent `>1/2`.

A candidate fails if the proposed transfer input already contains an RH-equivalent fixed Riesz/coarse mode, if smoothing makes the desired scale vacuous, if inversion reintroduces the original partial-sum burden, or if the only gain comes from a triangle inequality that spends the polynomial saving on exceptional mass.

## Evidence boundary

`MC-115` independently establishes the RH implication of the mean-absolute upper bound, so that implication no longer inherits the `NEEDS-AUDIT` status of `MC-009`. The stronger Pintz claims about the **full limiting logarithmic exponent** and the terminal-window maximum remain audit-sensitive and must not be treated as independently verified.

No current local theorem in this line proves the required RH-scale bound for `D_M`. The direct Mellin bridge reduces the literature dependency of the endpoint; it does not reduce the upstream arithmetic difficulty of producing the bound.

## Research disposition

**Accepted, sharpened by `MC-115`.** Earlier work eliminated several tempting but over-strong or information-losing carriers. The Tanaka/excursion branch showed that long excursions can coexist with diffusive mean-absolute behavior; the path-energy branch exposed an RH-equivalent first Riesz coarse mode; fixed-order Riesz smoothing remains RH-equivalent, while growing-order smoothing either becomes normalization-vacuous or delays endpoint visibility and requires a nontrivial inversion carrier.

The active residual is therefore narrower: find a statistic that is genuinely weaker than the target, preserves enough signed/multiscale information to control the **first absolute moment** of the Mertens path, and transfers with a strict polynomial margin. The endpoint itself needs no new zero theorem: `MC-115` closes that step exactly. The clue remains accepted rather than resolved because no such arithmetic production mechanism has yet been established.