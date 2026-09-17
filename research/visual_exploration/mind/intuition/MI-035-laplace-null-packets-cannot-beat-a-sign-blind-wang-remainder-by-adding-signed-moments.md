# MI-035 — Laplace-null packets cannot beat a sign-blind Wang remainder by adding signed moments

**Evidence level:** literature+derived synthesis from [VIS-274](../../findings/VIS-274-wang-fixed-q-rescaled-laplace-limit.md), [VIS-275](../../findings/VIS-275-wang-laplace-null-source-bound-floor.md), and [VIS-276](../../findings/VIS-276-wang-source-floor-localizes-to-explicit-remainder-mean.md). The obstruction concerns the rate certified after a sign-destructive majorization; VIS-276 identifies the signed source quantity hidden immediately before that step.

At fixed physical `q`, VIS-274 shows that Wang's concentrating main term should be retained and rescaled rather than Taylor-collapsed. The normalized statistic then has a finite leading Laplace functional. A natural move is to choose a signed packet with

`int h(q)e^(-4pi q)dq = 0`

and add further weighted moment cancellations in the hope of pushing below the resulting `1/log T` remainder scale.

VIS-275 shows why the current absolute proof interface cannot certify such an improvement. After the same fixed-`q` rescaling, the dominant available bound contains

`O((1/log T) int |h(q)| e^(-4pi q)dq)`.

For every fixed nonzero packet this weighted absolute norm is positive, so no finite family of signed polynomial-Laplace moment constraints can make that majorant `o(1/log T)`.

VIS-276 sharpens the lesson by locating the lost sign. In Wang's decomposition `A=-D+B+E`, the deterministic variation of `B=log(t+2)/x` is already power-smaller on the short interval. The first unresolved contribution comes from the signed `B,E` cross term and is controlled by

`M_T(x) = (x/H) Re int_T^(T+H) E_x(t) dt`.

The pointwise estimate `E_x(t)=O(1/x)` replaces this signed mean by `M_T=O(1)` and thereby produces the sign-blind `1/log T` envelope. Thus the barrier is not evidence that the true residual has size `1/log T`; it records exactly where the available proof stops exploiting cancellation in `t`.

This gives a precise source-side target. If `M_T(e^(2pi q))=o(1)` uniformly on a fixed compact `q` window, the current `1/log T` floor disappears without imposing any additional packet moments. If `M_T=O((log T)^(-1/2))`, the already exposed remaining terms are at the next `O((log T)^(-3/2))` scale.

The reusable distinction is between **engineering cancellation in the test packet and proving cancellation in the source remainder**. Packet orthogonality can act only on signed structure that survives the theorem interface. Once the proof takes an absolute envelope, extra signed constraints cannot restore that information; the correct move is to estimate the signed source quantity before majorization.

**Boundary.** No estimate for `M_T` is proved by VIS-276, and the actual residual for a special packet may be smaller than the current certificate. The localization is tied to Wang's present decomposition and fixed-source scaling. Moving source windows, a different explicit-formula remainder convention, or `T`-dependent packets require a separate same-scale audit.