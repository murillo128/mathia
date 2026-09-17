# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the first normalization-invariant fixed-source correction after the gamma baseline

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-035-sign-destructive-wang-bounds-must-be-repaired-at-a-normalization-invariant-source-interface`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The representation problem is largely resolved. VIS-271 identifies the theorem/source coordinate mismatch, VIS-272 gives the exact Green-potential dictionary between Wang's diagonal field and the Rodgers weighted prime-power measure, and VIS-274 shows that a fixed physical `q` packet has a finite leading Laplace limit after the concentrating Wang main term is retained and rescaled at its natural `1/log T` width.

VIS-275 shows that adding signed packet moments cannot improve the currently certified remainder once the proof has taken the sign-blind envelope

`(1/log T) int |h(q)| e^(-4pi q)dq`.

VIS-276 localized that floor to the signed mean of the explicit-formula remainder in Wang's decomposition `A=-D+B+E`, suggesting `M_T(x)=(x/H) Re int E_x(t)dt` as the source-side quantity to sharpen before majorization.

VIS-277 now resolves that literal target. Uniformly on compact fixed-source windows,

`M_T(x) = -log(2*pi) + O_K(H^-1+T^-1)`.

The nonzero limit is the classical gamma-factor normalization already present in `log(t/(2*pi))`, not a new arithmetic residual. Recentring `B` by `-log(2*pi)/x` makes the corresponding remainder mean vanish, but the same constant moves into `|B|^2` and leaves the full `1/log T` source correction unchanged. The decomposition pieces are convention-dependent; the combined source contribution is not.

The next theorem question is therefore the first **normalization-invariant** unresolved correction after the classical `log(t/(2*pi))` baseline is removed consistently from the complete source `B_x+E_x`. Only after that kernel is exposed is it meaningful to design signed packets against it or ask whether the already visible `L^(-3/2)` scale is attainable. Further work should not try to prove cancellation of Wang's original `M_T` to zero or infer progress from a recentering that merely relocates the same deterministic term.

## Keep packet conditioning, arithmetic selectivity and theorem coordinates separate

Shrinking moment packets have a seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling a universal leading functional.

VIS-274--VIS-277 sharpen the theorem-coordinate ledger. A large moving-test seminorm is not automatically fatal when it resolves a structured boundary layer, but after the structured main term is removed both **where sign is discarded** and **which decomposition quantities are normalization-invariant** become first-class resources. The original remainder mean was signed but convention-dependent; the next useful object must survive harmless redistribution between explicit and remainder pieces.

A future visual/analytic probe should therefore state its physical source window first, retain structured terms through the induced coordinate rescaling, normalize the classical gamma baseline once and consistently, isolate the first invariant signed residual before applying a majorant, and only then engineer cancellations. Exact coordinate dictionaries and visual concentration remain intermediate resources until that residual is controlled strongly enough to survive the destination scaling.