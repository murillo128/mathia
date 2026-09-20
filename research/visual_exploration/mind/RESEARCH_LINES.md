# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find theta-remainder localization that genuinely pays the variable-bank phase-entropy budget

**Linked intuitions:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`, `MI-042-fixed-polynomial-smoothing-preserves-the-korobov-vinogradov-envelope-class`, `MI-043-finite-scalar-wang-dilation-banks-have-a-vandermonde-cancellation-ceiling`, `MI-044-translations-split-wang-tail-cancellation-into-independent-phase-fibers`, `MI-045-phase-resolving-wang-windows-inherit-the-fiberwise-moment-cost`, `MI-046-turan-nazarov-forces-fixed-wang-cancellation-onto-microscopic-windows`.

VIS-330--VIS-340 establish the transform/source boundary. Wang smoothing attenuates high log frequency by one order and exact inversion charges one derivative; the surviving prime and square-log summatory sources are exact functionals of the same normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`.

VIS-341--VIS-346 price fixed scalar smoothing: a power gain requires growing effective order, pure dilates pay that order in distinct scales, translations split cancellation into phase fibers, phase-resolving windows inherit the moment cost, and Turán--Nazarov propagation forces a fixed `B`-phase escape onto windows at least as small as the `X^(-1/(B-1))` coarse threshold.

VIS-347 now prices the genuinely scale-dependent finite-bank loophole. Let `B_X` be the number of active first-moment phase fibers, `Delta_X` their minimum gap, `ell_X` the working-window length, `S_X` the first inverse-scale moment vector and `T_X=sum_j |c_(j,X)|/a_(j,X)^2`. If order-`>=2` attenuation holds on `J_X subset [X,2X]`, then with

`L_X=4(B_X-1)/Delta_X`, `e_X=min(ell_X,L_X)`, `D_X=C_0/2+2T_X`,

one necessarily has

`(B_X-1) log(A L_X/e_X) >= log( X ||S_X||_2 / (sqrt(2) D_X) )`.

When `D_X/||S_X||_2=X^(o(1))`, the left side must carry `(1-o(1))log X`. For fixed `B`, power-law windows/gaps `ell_X=X^(-alpha+o(1))`, `Delta_X=X^(-beta+o(1))` require `(B-1)(alpha+beta)>=1`. For macroscopic windows and uniformly separated phases, `B_X log B_X` must be at least order `log X`, hence `B_X=Omega(log X/log log X)` up to constants.

The live source question is therefore not simply “let the bank vary with scale.” A candidate must actually meet this entropy/conditioning budget while keeping coefficient norms, first moments, scale count and finite-frequency leakage controlled, and then show a signed/source-dependent property of `G` that survives Wang's downstream derivative repayment. Frequency- or source-dependent coefficients and infinite expansions remain outside the finite-bank theorem, but their advantage must be stated as source cancellation rather than uniform scalar-multiplier smallness.

## Quotient packet and summatory geometry through theta before crediting arithmetic structure

Proper prime powers remain too small at the relevant scale, and the centered prime measure and prime-only square-log summatory source remain exact images of `G`. Proposed packets, weights or multiscale organizations should therefore first be translated into a quantitative statement about `G`.

For finite translated-dilate banks, VIS-341--VIS-347 now give a quantitative resource ledger covering fixed and variable phase geometry. A shrinking window, coalescing phases or growing phase count is an escape only to the extent that it pays the displayed Turán--Nazarov budget without degenerating `S_X` relative to `T_X`. A surviving mechanism must use source information beyond this scalar concentration problem and still close the destination ledger without reconstructing the unsmoothed source through `Q'` or an equivalent derivative channel.