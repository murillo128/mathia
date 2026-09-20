# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Find genuinely scale-dependent theta-remainder localization beyond the Turán--Nazarov fixed-bank gate

**Linked intuitions:** `MI-041-wang-natural-window-is-a-taper-weighted-prime-ratio-occupancy-problem`, `MI-042-fixed-polynomial-smoothing-preserves-the-korobov-vinogradov-envelope-class`, `MI-043-finite-scalar-wang-dilation-banks-have-a-vandermonde-cancellation-ceiling`, `MI-044-translations-split-wang-tail-cancellation-into-independent-phase-fibers`, `MI-045-phase-resolving-wang-windows-inherit-the-fiberwise-moment-cost`, `MI-046-turan-nazarov-forces-fixed-wang-cancellation-onto-microscopic-windows`.

VIS-330--VIS-340 establish the transform/source boundary. Wang smoothing attenuates high log frequency by one order and exact inversion charges one derivative. Proper prime powers are below the live envelope, while the surviving prime and square-log summatory sources are exact functionals of the same normalized Chebyshev-theta remainder `G(u)=e^(-u)theta(e^u)-1`.

VIS-341--VIS-343 price scalar smoothing order: any fixed or subpolynomial truncation order preserves the Korobov--Vinogradov power class, a fixed power gain requires polynomially growing effective order, and a pure-dilation Wang bank needs at least the same number of distinct scales because its high-frequency moments form a Vandermonde system. VIS-344 then shows that fixed translations cannot pool those cancellations across phase fibers.

VIS-345 extends the obstruction to moving windows that resolve the fixed phase spacings. VIS-346 removes most of the remaining fixed-bank short-window loophole without requiring the working window itself to resolve the phases. A phase-resolving reference interval gives a coefficient lower bound, and Turán--Nazarov propagation implies that a nonzero `k`-th moment vector with `B_k` active phase fibers can coexist with `O(X^-r)` cancellation only if `X*min(ell_X,1)^(B_k-1)=O(1)`. In particular a fixed `B`-fiber bank on power-law windows `ell_X=X^-alpha` can escape only at the coarse scale `alpha>=1/(B-1)`.

The source question is now quantitatively microscopic. Does `G` possess a controlled localization on windows at or below that threshold, or can a bank whose phase count, spacing, scales or coefficients vary with `X` exploit a regime that the fixed Turán--Nazarov argument does not cover? Alternatively, can frequency- or source-dependent coefficients use signed arithmetic cancellation in `G` rather than making one scalar multiplier uniformly small? Any candidate must keep coefficient conditioning, finite-frequency leakage and Wang's downstream derivative repayment explicit.

## Quotient packet and summatory geometry through theta before crediting arithmetic structure

Proper prime powers remain too small at the relevant scale, and the centered prime measure and prime-only square-log summatory source remain exact images of `G`. Proposed packets, weights or multiscale organizations should therefore first be translated into a quantitative statement about `G`.

For any fixed finite translated-dilate bank, VIS-341--VIS-346 now supply a nearly complete scalar control: polynomial gain requires polynomial order, order requires enough scales, distinct phase fibers cannot share asymptotic moments, long windows inherit the same cost, and even short windows above the Turán--Nazarov shrinking threshold do not escape it. A surviving mechanism must be genuinely scale-dependent, ultra-local, adaptive or source-signed, and must still close the destination ledger without reconstructing the unsmoothed source through `Q'` or an equivalent derivative channel.