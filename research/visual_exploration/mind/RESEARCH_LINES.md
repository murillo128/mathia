# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Transfer a fixed physical prime window through Wang without losing theorem accuracy

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-034-wang-diagonal-is-a-green-potential-of-the-rodgers-prime-measure`.

The representation problem is largely resolved. Rodgers' low-frequency expansion separates universal zero-frequency structure from prime-power curvature samples. Fixed-prime access can coexist with cancellation of the leading universal functional in the Rodgers coordinate. VIS-271 then identifies the source-coordinate mismatch with Wang, and VIS-272 resolves it exactly: after `q=log x/(2pi)`, Wang's diagonal coefficient field is the exponential Green potential of the same weighted prime-power measure used by Rodgers.

The remaining obstacle is theorem uniformity at that exact pullback scale. A fixed physical `q` window becomes a Wang window centered and supported at `alpha=O(1/log T)`. VIS-266's audited moving-test bound contains `||g_T'||_inf/log T`. VIS-273 shows that pulling back any nontrivial fixed-width physical packet forces `||g_T'||_inf=Theta(log T)`, so this error term stays order one. Amplitude damping followed by renormalization does not improve the relative error.

Thus the current Wang proof interface cannot certify a fixed-prime Green functional even though the source dictionary is exact. The next useful result must improve the derivative dependence, derive an integrated/adjoint estimate that acts directly on the Green potential, or otherwise control `1/log T`-scale moving tests without differentiating an uncontrolled remainder.

## Keep packet conditioning, arithmetic selectivity and theorem coordinates separate

Shrinking moment packets have an unavoidable seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling the universal leading functional.

VIS-273 adds a third ledger: even a source-selective packet with an exact coordinate dictionary may land precisely on the theorem's stability boundary after pullback. Support access, source content and theorem uniformity must therefore be audited independently.

A future visual/analytic probe should state its physical source window first, then map it into the theorem coordinate, compute the forced amplitude/derivative seminorms there, and compare the actual theorem remainder with the arithmetic signal. Visual concentration or exact coefficient identities are not evidence until this same-scale transfer closes.