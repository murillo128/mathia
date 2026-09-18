# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Determine whether an intrinsic `L^(-3/2)` fixed-source frontier exists at all

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-036-a-uniform-theorem-exponent-can-disappear-after-specializing-to-the-physical-source-regime`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The representation problem is largely resolved. VIS-271 identifies the theorem/source coordinate mismatch, VIS-272 gives the exact Green-potential dictionary between Wang's diagonal field and the Rodgers weighted prime-power measure, and VIS-274 shows that a fixed physical `q` packet has a finite leading Laplace limit after the concentrating Wang main term is retained and rescaled at its natural `1/log T` width.

VIS-275 shows that adding signed packet moments cannot improve the currently certified remainder once the proof has taken the sign-blind envelope

`(1/log T) int |h(q)| e^(-4pi q)dq`.

VIS-276 localized the apparent lost sign to the mean of Wang's explicit-formula remainder. VIS-277 then showed that the nonzero limit of that convention-dependent coordinate is the classical gamma normalization `-log(2*pi)`: recentering can move it between `B` and `E` but cannot change the combined source.

VIS-278 closes the first normalization-invariant **pure source-energy** question. For fixed source `x` on compact subsets of `(1,infinity)`, define

`R_x(t)=x(B_x(t)+E_x(t))-log(t/(2*pi))`.

Then

`R_x(t)=zeta'/zeta(3/2-it)+O_K(t^-1)`,

so its short-interval mean is `O_K(H^-1+T^-1)` while

`(1/H) int |R_x(t)|^2 dt = C_Lambda+o_K(1)`,

where

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3=sum_p (log p)^2/(p^3-1)>0`.

The gamma-normalized residual is therefore centered but has a classical positive prime-power variance floor. In the fixed-`q` packet scaling this standalone source-energy correction enters at order `L^(-2)`.

VIS-279 closes the first obvious **non-source cross-term** explanation of the larger exponent. Wang's exact mean-square identity, specialized before taking the fixed-source pullback, gives `||D_x||_2=O(sqrt H)` for compact fixed `x`, while `||E_x||_2=O(sqrt H/x)`. Their signed cross term is consequently `O(H/x)` and contributes only `O(L^-2)` after the `dq/L` pullback and `1/(HL)` normalization. The earlier `L^-3/2` estimate for this sector came from a theorem-uniform `O(sqrt(HL))` bound appropriate to growing `x`, not from the physical fixed-source regime.

VIS-280 closes the remaining direct prime/source cross. Wang's explicit `D_x`--`B_x` estimate is `O_K(L)` at compact fixed source, so after the fixed-source pullback and packet normalization it contributes only `O_K(1/(HL))`, which is power-small in `T`. Consequently the entire direct interaction `D_x` against `B_x+E_x` is excluded as a compulsory `L^-3/2` mechanism: its `D-B` part is power-small and its `D-E` part is at most `L^-2`.

VIS-281 now closes the zero-window localization boundary as well. Wang's replacement of the interval-restricted zero field by the full field on the physical interval carries the theorem-uniform error `O(x L^3)`. On a fixed physical source packet `x=e^(2*pi q)` with compact `q`, this is only `O_K(L^3)` before rescaling. The `dq/L` pullback and `1/(HL)` pair-statistic normalization reduce it to `O_K(L/H)`, which is smaller than every fixed negative power of `L` because `H=T^theta`. Thus the `A_I -> A` localization step cannot generate an intrinsic `L^-3/2`, `L^-2`, or any logarithmic fixed-source frontier.

The live question has therefore moved beyond the direct source decomposition **and** this localization loss. Do not assume that the full fixed-source theorem contains an intrinsic `L^-3/2` interaction. Audit the remaining theorem-level truncation, replacement and unspecialized sectors at fixed physical `q`, and identify the actual largest surviving signed term. If some exact sector really remains at `L^-3/2`, preserve its sign/covariance and test cancellation there. If every compact-source sector falls to `L^-2` or below, the advance is a sharper fixed-source transfer theorem rather than a new cancellation packet.

## Keep packet conditioning, arithmetic selectivity, theorem coordinates and parameter-uniformity separate

Shrinking moment packets have a seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling a universal leading functional.

VIS-274--VIS-281 sharpen the theorem-coordinate ledger. A large moving-test seminorm is not automatically fatal when it resolves a structured boundary layer, but after the structured main term is removed both **where sign is discarded**, **which decomposition quantities are normalization-invariant**, **whether a quoted error scale is intrinsic to the physical source regime**, and **whether a theorem-level localization loss survives the induced source pullback** become first-class resources. The original remainder mean was signed but convention-dependent; the gamma-normalized combined residual has nonzero classical energy at `L^-2`; both direct prime/source cross terms drop to `L^-2` or below; and the zero-window localization error is power-small once its actual fixed-source scaling is restored.

A future visual/analytic probe should therefore state its physical source window first, retain structured terms through the induced coordinate rescaling, normalize the classical gamma baseline once and consistently, specialize every theorem-uniform estimate and localization/replacement error to that window, locate the exact remaining sector at the true limiting exponent, preserve its sign/covariance until after packet design, and only then engineer cancellations. Exact coordinate dictionaries and visual concentration remain intermediate resources until the surviving destination-scale term is identified and controlled.
