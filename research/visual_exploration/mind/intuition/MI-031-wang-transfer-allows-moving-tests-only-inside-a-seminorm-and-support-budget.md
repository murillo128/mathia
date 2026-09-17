# MI-031 — Critical moving tests must retain the concentrated main term before seminorm collapse

**Evidence level:** corrected exact synthesis from [VIS-266](../../findings/VIS-266-wang-moving-test-bound.md), [VIS-271](../../findings/VIS-271-wang-fixed-alpha-prime-scale-mismatch.md), [VIS-272](../../findings/VIS-272-wang-source-green-kernel-recovers-rodgers-prime-measure.md) and [VIS-274](../../findings/VIS-274-wang-fixed-q-rescaled-laplace-limit.md). The earlier VIS-273 obstruction was withdrawn; its `O(1)` barrier came from applying a fixed-test Taylor reduction at the same scale as the concentrating main term.

A fixed physical prime window in the logarithmic coordinate `q=log x/(2pi)` pulls back to a Wang test of the form

`g_T(alpha)=h((log T)|alpha|/(2pi))`,

so its width is `Theta(1/log T)` and `||g_T'||=Theta(log T)`. That derivative growth is real, but VIS-274 shows it is **not by itself a theorem-transfer obstruction**. It is the expected cost of resolving the same `1/log T` boundary layer on which Wang's exponential diagonal main term concentrates.

If one first replaces the structured main term by a fixed-test approximation at `alpha=0`, the generic derivative remainder `||g_T'||/log T` becomes order one and appears to destroy the signal. Keeping the concentrated exponential term intact and rescaling directly to `q` instead gives

`(2pi/(H log T)) W_I(g_T) = 4pi int h(q)e^(-4pi q)dq + O_h(1/log T)`,

with an explicit smaller `1/(log T)^2` deterministic correction. Thus the fixed physical `q` window is theorem-accessible at leading order.

The reusable lesson is that **seminorm growth must be compared to the proof component it controls, not to a main term that has already been Taylor-collapsed away**. When the test family concentrates on the same scale as a structured kernel, rescale the kernel and test together before invoking generic moving-test bounds. Otherwise an artifact of a coarse fixed-test corollary can be mistaken for a genuine physical-resolution barrier.

There is still a real boundary after the leading Laplace functional is cancelled. If `int h(q)e^(-4pi q)dq=0`, VIS-274 leaves only an `O_h(1/log T)` normalized remainder and does not identify its coefficient. At that point a sharper first-order expansion or an `o(1/log T)` theorem is genuinely needed to extract source-selective residual information.

**Boundary.** VIS-274 does not transfer arbitrary shrinking packets, does not justify differentiating unknown remainders, and does not produce a new pair-correlation or RH criterion. It corrects the earlier claim that fixed physical prime windows are automatically excluded by the derivative budget.