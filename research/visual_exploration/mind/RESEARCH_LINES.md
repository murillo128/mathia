# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Estimate the signed mean explicit-formula remainder at fixed source scale

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-035-laplace-null-packets-cannot-beat-a-sign-blind-wang-remainder-by-adding-signed-moments`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The representation problem is largely resolved. VIS-271 identifies the theorem/source coordinate mismatch, VIS-272 gives the exact Green-potential dictionary between Wang's diagonal field and the Rodgers weighted prime-power measure, and VIS-274 shows that a fixed physical `q` packet has a finite leading Laplace limit after the concentrating Wang main term is retained and rescaled at its natural `1/log T` width.

VIS-275 shows that adding signed packet moments cannot improve the currently certified remainder. After leading Laplace cancellation, the available proof-level bound contains the sign-blind term

`(1/log T) int |h(q)| e^(-4pi q)dq`,

so orthogonality has nothing left to act on inside that absolute envelope.

VIS-276 now localizes where this `1/log T` floor actually enters Wang's decomposition. The deterministic variation of `B_x(t)=log(t+2)/x` contributes only a power-smaller `o(H log T/x^2)` term on the power-short interval. The surviving first-order channel is the signed mean of the explicit-formula remainder,

`M_T(x) = (x/H) Re int_T^(T+H) E_x(t) dt`.

The pointwise estimate `E_x(t)=O(1/x)` gives only `M_T(x)=O(1)` and reproduces the current `1/log T` certificate. But `M_T(e^(2pi q))=o(1)` uniformly on each fixed compact `q` window would already cross that barrier for every fixed smooth packet; `M_T=O((log T)^(-1/2))` would expose the next existing `O((log T)^(-3/2))` scale.

The next theorem question is therefore no longer a vague request for more packet moments or a global sharpening of every term in Wang's proposition. It is the specific source-side problem of representing or estimating the short-interval signed mean of `E_x(t)` for fixed `x=e^(2pi q)`. An asymptotic for that mean would expose the first residual kernel against which packet cancellation should be designed.

## Keep packet conditioning, arithmetic selectivity and theorem coordinates separate

Shrinking moment packets have a seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling a universal leading functional.

VIS-274--VIS-276 sharpen the theorem-coordinate ledger. A large moving-test seminorm is not automatically fatal when it resolves a structured boundary layer, but after the structured main term is removed the **location at which sign is discarded** becomes a first-class resource. The current absolute envelope hides a residual whose relevant first-order piece is actually the signed scalar `M_T(x)` before absolute values are taken.

A future visual/analytic probe should therefore state its physical source window first, retain structured terms through the induced coordinate rescaling, isolate the signed residual before applying a majorant, and only then engineer cancellations. Exact coordinate dictionaries and visual concentration remain intermediate resources until the signed source remainder itself is controlled strongly enough to survive the destination scaling.