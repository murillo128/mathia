# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the first residual after the fixed-physical-window Wang limit

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-034-wang-diagonal-is-a-green-potential-of-the-rodgers-prime-measure`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The representation problem is largely resolved. Rodgers' low-frequency expansion separates universal zero-frequency structure from prime-power curvature samples. VIS-271 identifies the coordinate mismatch with Wang, and VIS-272 repairs it exactly: after `q=log x/(2pi)`, Wang's diagonal source field is the exponential Green potential of the same weighted prime-power measure used by Rodgers.

VIS-274 corrects the apparent theorem-scale obstruction previously recorded in VIS-273. A fixed physical `q` packet pulls back to a Wang test of width `Theta(1/log T)` and derivative norm `Theta(log T)`, but that derivative growth occurs on exactly the scale of the concentrating exponential main term. Keeping that term intact and rescaling directly gives a finite leading Laplace functional with only `O_h(1/log T)` normalized remainder. Fixed physical prime windows are therefore accessible at leading order; the former `O(1)` barrier was an artifact of collapsing the main term to a fixed-test Taylor approximation before rescaling.

The live question is now the **Laplace-null residual**. If the packet satisfies `int h(q)e^(-4pi q)dq=0`, the leading Wang contribution vanishes and the normalized statistic is only known to be `O_h(1/log T)`. A useful next result should identify the `1/log T` coefficient or improve the remainder to `o(1/log T)` for a source-selective family, while preserving the exact prime-power Green dictionary from VIS-272.

## Keep packet conditioning, arithmetic selectivity and theorem coordinates separate

Shrinking moment packets have a seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling a universal leading functional.

VIS-274 adds a refinement to the theorem-coordinate ledger: a large moving-test seminorm is not automatically fatal when it measures variation of a structured main term on its natural concentration scale. The correct audit is to map the physical source window into theorem coordinates, retain and rescale every structured main component at that scale, and only then compare the residual theorem error with the arithmetic signal.

A future visual/analytic probe should therefore state its physical source window first, identify which leading theorem functionals it cancels, and compute the remaining signal and error after same-scale rescaling. Exact coordinate dictionaries and visual concentration remain intermediate resources until the residual—not a prematurely Taylor-collapsed main term—is controlled.