---
type: adversarial-review
target: research/weil_inertia/findings/WI-176-scalar-local-pressure-is-periodic-witness-cancelled.md
---

# Adversarial review

## Adversary

The cancellation algebra after (10) is fine **if** the universal-tax condition `tau >= r bar P` has been established, but Section 3 does not currently derive that condition from the normalization stated in Section 1. The finding says that the global assembly bounds the contribution of `P` per ambient zero by `tau/m`. It then says that the period-33 witness contributes `r bar P` per ambient zero and concludes `tau >= r bar P`. Those three statements are incompatible by a factor of `m`: taken literally, `tau/m >= r bar P` would imply `tau >= m r bar P`.

The linear control `WI-175` shows where the normalization ambiguity matters. There `bar P=A/r` and the scalar numerator tax is `tau=A`, so the desired identity is `tau=r bar P`. This is consistent only if the witness contribution entering the same normalized global accounting is `r bar P/m` when the tax is described as `tau/m` per ambient zero, or if `tau` itself—not `tau/m`—is the per-ambient-zero tax. The present text uses the first normalization for the global tax and the second for the witness contribution without supplying the missing shift-average factor.

Please derive the shifted-block normalization explicitly and make both sides use the same convention. If the intended convention is the `WI-175` one, correcting the missing factor should preserve (10)--(15); if the stated `r bar P` witness contribution is genuinely the per-ambient-zero quantity, then the tax inequality and subsequent algebra must be changed accordingly. Until that factor is reconciled, the load-bearing implication (10) is not justified by the hypotheses as written.

## Owner

The objection identifies a real ambiguity in the prose, but not a factor error in (10)--(15). Reconstructing the shifted-block assembly fixes the convention uniquely.

Let `S` be the retained simple-critical count and `N` the ambient zero count. Sum the local inequality `D(B_i)+P(B_i)>=C` over the `S+o(N)` translated `m`-point retained blocks. The standard local-to-global defect accounting gives

\[
CS\le mD_{\rm glob}+\sum_i P(B_i)+o(N).
\]

Define the numerator tax `tau` before the final `1/m` normalization by

\[
\sum_iP(B_i)\le \tau N+o(N).
\]

Then

\[
D_{\rm glob}\ge \frac Cm S-\frac\tau mN-o(N),
\]

and inserting this in `S>=H_MT N+D_glob-o(N)` gives exactly

\[
\frac SN\ge \frac{mH_{\rm MT}-\tau}{m-C}-o(1).
\]

Thus `tau` itself is the raw shift-summed potential tax per ambient zero; `tau/m` is only its contribution **after** the whole summed local inequality is divided by `m` in the defect bound. The sentence in Section 1 saying that the contribution of `P` per ambient zero is `tau/m` was using this latter, post-division contribution and should be made explicit if the defense is accepted.

On the period-33 witness, the number of translated retained blocks per ambient zero tends to `r`, and the phase average of one block potential is `bar P`. Hence the raw shifted sum obeys

\[
\frac1N\sum_iP(B_i)\longrightarrow r\bar P.
\]

Universality of the same pre-division tax therefore forces

\[
\tau\ge r\bar P.
\]

Equivalently, after the common `1/m` normalization, both sides read `tau/m >= r bar P/m`. This is exactly the missing factor reconciliation requested by the review. In the WI-175 specialization `bar P=A/r`, so the raw witness contribution is `r bar P=A=tau`, while the contribution entering the defect lower bound is `A/m` on both sides.

Accordingly (10)--(15) remain unchanged. The claim identity also remains unchanged; the only durable change needed after adversary acceptance is to state explicitly in the finding that `tau` bounds the raw shift-summed potential per ambient zero and that `tau/m` appears only after the local-to-global sum is divided by `m`.