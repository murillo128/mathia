---
type: adversarial-review
target: research/weil_inertia/findings/WI-176-scalar-local-pressure-is-periodic-witness-cancelled.md
---

# Adversarial review

## Adversary

The cancellation algebra after (10) is fine **if** the universal-tax condition `tau >= r bar P` has been established, but Section 3 does not currently derive that condition from the normalization stated in Section 1. The finding says that the global assembly bounds the contribution of `P` per ambient zero by `tau/m`. It then says that the period-33 witness contributes `r bar P` per ambient zero and concludes `tau >= r bar P`. Those three statements are incompatible by a factor of `m`: taken literally, `tau/m >= r bar P` would imply `tau >= m r bar P`.

The linear control `WI-175` shows where the normalization ambiguity matters. There `bar P=A/r` and the scalar numerator tax is `tau=A`, so the desired identity is `tau=r bar P`. This is consistent only if the witness contribution entering the same normalized global accounting is `r bar P/m` when the tax is described as `tau/m` per ambient zero, or if `tau` itself—not `tau/m`—is the per-ambient-zero tax. The present text uses the first normalization for the global tax and the second for the witness contribution without supplying the missing shift-average factor.

Please derive the shifted-block normalization explicitly and make both sides use the same convention. If the intended convention is the `WI-175` one, correcting the missing factor should preserve (10)--(15); if the stated `r bar P` witness contribution is genuinely the per-ambient-zero quantity, then the tax inequality and subsequent algebra must be changed accordingly. Until that factor is reconciled, the load-bearing implication (10) is not justified by the hypotheses as written.
