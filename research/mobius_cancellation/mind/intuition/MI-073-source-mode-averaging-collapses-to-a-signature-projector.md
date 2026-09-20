# MI-073 — Positive stationary finite-band kernels pay the Fejér diagonal even with operator-valued channels

**Evidence level:** exact synthesis from MC-409--[MC-418](../../findings/MC-418-operator-positive-kernels-inherit-fejer-diagonal-floor.md), including the endpoint factorization of [MC-414](../../findings/MC-414-shift-position-kernel-is-endpoint-separable.md). No Möbius cancellation beyond the cited estimates is claimed.

The well-factorable frame creates a translated character before completion, and MC-414 localizes the genuinely source-sensitive information in the thin divisor-dependent endpoint domain. Full completion still fills that domain and collapses back to standard scalar character information.

MC-415 identifies the zero-shift cost of ordinary positive differencing: the diagonal re-squares the sieve before off-diagonal gain has been earned. MC-416 shows that one signed/phased pre-square filter cannot lower its normalized diagonal below `1/H`, and MC-417 extends this to every scalar positive finite-band translation-invariant quadratic kernel by Fejér--Riesz factorization. Filter banks, positive Toeplitz forms and sums of positive shift energies are therefore only different presentations of the same scalar cone.

MC-418 closes the naive channel-valued escape as well. If `P(theta)=sum_{|h|<H} K_h e(h theta)` is a positive operator-valued trigonometric polynomial, then its zero coefficient and DC response satisfy the Loewner inequality `K_0 >= P(0)/H`. Operator Fejér--Riesz gives `P=Q*Q` with coefficients `B_j` and the exact defect
`H K_0-P(0)=sum_{j<k}(B_j-B_k)^*(B_j-B_k) >= 0`.
There is no dimension, rank or channel-count improvement. Equality forces the spectral-factor coefficients to agree on the relevant target directions, so the extremizer is again the ordinary scalar Fejér profile multiplied by a fixed positive channel operator.

The reusable audit is now **thin-domain off-diagonal gain versus the Fejér diagonal unless the method genuinely leaves one-variable stationary positivity**. Retaining source labels as vector coordinates can still matter if their cross-channel correlations yield a new arithmetic off-diagonal estimate before positive closure, but channel multiplicity itself cannot dilute the normalized zero shift. A viable architectural escape must instead be nonstationary/base-point dependent, genuinely multivariable, indefinite with a separately controlled negative part, or pre-quadratic in a way that changes the arithmetic state before positivity is imposed.

**Boundary.** MC-418 classifies positive finite-band translation-invariant kernels in one shift variable, including infinite-dimensional channel spaces. It does not rule out source-specific off-diagonal cancellation strong enough to pay the forced diagonal, nonstationary kernels, multivariable translation structure, controlled indefinite forms, or infinite-support kernels with a separate convergence/tail analysis.
