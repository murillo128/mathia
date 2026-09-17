# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Identify the interaction behind the `L^(-3/2)` frontier after gamma-normalized source-energy closure

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-035-laplace-null-packets-cannot-beat-a-sign-blind-wang-remainder-by-adding-signed-moments`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The representation problem is largely resolved. VIS-271 identifies the theorem/source coordinate mismatch, VIS-272 gives the exact Green-potential dictionary between Wang's diagonal field and the Rodgers weighted prime-power measure, and VIS-274 shows that a fixed physical `q` packet has a finite leading Laplace limit after the concentrating Wang main term is retained and rescaled at its natural `1/log T` width.

VIS-275 shows that adding signed packet moments cannot improve the currently certified remainder once the proof has taken the sign-blind envelope

`(1/log T) int |h(q)| e^(-4pi q)dq`.

VIS-276 localized the apparent lost sign to the mean of Wang's explicit-formula remainder. VIS-277 then showed that the nonzero limit of that convention-dependent coordinate is the classical gamma normalization `-log(2*pi)`: recentering can move it between `B` and `E` but cannot change the combined source.

VIS-278 now closes the first normalization-invariant **pure source-energy** question. For fixed source `x` on compact subsets of `(1,infinity)`, define

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Then

`R_x(t)=zeta'/zeta(3/2-it)+O_K(t^-1)`,

so its short-interval mean is `O_K(H^-1+T^-1)` while

`(1/H) int |R_x(t)|^2 dt = C_Lambda+o_K(1)`,

where

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3=sum_p (log p)^2/(p^3-1)>0`.

The gamma-normalized residual is therefore centered but has a classical positive prime-power variance floor. In the fixed-`q` packet scaling this standalone source-energy correction enters at order `L^(-2)`, below the larger `L^(-3/2)` theorem-level remainder still present in Wang's current interface.

The live question has consequently moved out of `|B+E|^2`. Identify which **non-source interaction or cross term** produces the `L^(-3/2)` scale and determine whether that contribution has a normalization-invariant signed representation before the proof takes absolute values. A useful next calculation should decompose the full theorem-level remainder by interaction sector at fixed physical `q`, retain the signed term responsible for `L^(-3/2)`, and only then test whether a packet can cancel it. Another recentering of `B,E`, another estimate of the pure combined-source energy, or extra signed moments applied after the absolute envelope cannot answer this question.

## Keep packet conditioning, arithmetic selectivity and theorem coordinates separate

Shrinking moment packets have a seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling a universal leading functional.

VIS-274--VIS-278 sharpen the theorem-coordinate ledger. A large moving-test seminorm is not automatically fatal when it resolves a structured boundary layer, but after the structured main term is removed both **where sign is discarded** and **which decomposition quantities are normalization-invariant** become first-class resources. The original remainder mean was signed but convention-dependent; the gamma-normalized combined residual is invariant and has nonzero classical energy, yet that energy sits at `L^(-2)` rather than the currently limiting `L^(-3/2)` scale.

A future visual/analytic probe should therefore state its physical source window first, retain structured terms through the induced coordinate rescaling, normalize the classical gamma baseline once and consistently, locate the exact interaction sector at the limiting exponent, preserve its sign/covariance until after packet design, and only then engineer cancellations. Exact coordinate dictionaries and visual concentration remain intermediate resources until that signed interaction is controlled strongly enough to survive the destination scaling.