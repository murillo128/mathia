# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Recover signed structure in the first fixed-window Wang residual

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-035-laplace-null-packets-cannot-beat-a-sign-blind-wang-remainder-by-adding-signed-moments`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The representation problem is largely resolved. VIS-271 identifies the theorem/source coordinate mismatch, VIS-272 gives the exact Green-potential dictionary between Wang's diagonal field and the Rodgers weighted prime-power measure, and VIS-274 shows that a fixed physical `q` packet has a finite leading Laplace limit after the concentrating Wang main term is retained and rescaled at its natural `1/log T` width.

The live question after leading Laplace cancellation is no longer how many additional signed moments to impose. VIS-275 propagates the proof-level remainder without collapsing its weights and identifies the unique theorem-level `1/log T` term as

`(1/log T) int |h(q)| e^(-4pi q)dq`.

Because this is an absolute weighted norm, a fixed nonzero Laplace-null packet cannot improve the certified rate by adding any finite family of signed polynomial-Laplace moment constraints. The present proof interface has discarded precisely the sign information those constraints would need.

The next theorem question is therefore source-side: can the dominant `H log T e^(-2 log(T) alpha)` remainder in Wang's proof be decomposed or expanded with signed structure after fixed-`q` rescaling, or can its rate be sharpened below `1/log T`? A signed first-order kernel would reopen packet engineering; without such an upgrade, increasingly elaborate null packets only reorganize mass inside a positive majorant.

## Keep packet conditioning, arithmetic selectivity and theorem coordinates separate

Shrinking moment packets have a seminorm cost, and theorem error must beat that conditioning before a coefficient can be extracted. Separately, a packet can have nonzero low-order moments while being exactly prime-power blind if its support misses all arithmetic frequencies. Conversely, a fixed Rodgers band can isolate a prime contribution while cancelling a universal leading functional.

VIS-274 and VIS-275 together sharpen the theorem-coordinate ledger. A large moving-test seminorm is not automatically fatal when it resolves a structured boundary layer, but after the structured main term is removed the **sign structure of the remainder bound** becomes a first-class resource. Same-scale rescaling must therefore be followed by an audit of whether the proof retains the phase/sign information required by the proposed cancellation.

A future visual/analytic probe should state its physical source window first, identify which theorem functionals it cancels, retain structured terms through the induced coordinate rescaling, and distinguish the actual signed residual from an absolute envelope. Exact coordinate dictionaries and visual concentration remain intermediate resources until the residual itself is controlled in a form that can support arithmetic cancellation.