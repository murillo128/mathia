# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Preserve source-relative noncompactness through the downstream chain

**Linked intuition:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-451--AF-452 identify the exact fixed-source stability carrier: completable source-law secants. AF-453 rules out uniform total-variation control when that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that source discreteness alone is not enough: an infinite one-atom alphabet has positive TV gain exactly when its observed image is uniformly discrete, so every bounded finite-dimensional observation has zero uniform margin.

AF-455 closes the generic bounded infinite-dimensional loophole under downstream compression. If the carrier image is bounded, every compact linear post-processing makes it precompact and therefore destroys the uniform TV margin. For an orthonormal one-hot carrier, `kappa_e^TV(L) <= ||L||_e/sqrt(2)`, so a retained margin `c` requires essential norm at least `sqrt(2)c`; the even-coordinate projection shows that positive essential norm is still not sufficient because it can annihilate the actual source secants.

The live quantitative question is therefore source-relative: which natural downstream operator classes remain noncompact enough and transverse enough to the admissible completed secants to have a positive restricted lower gain? Infinite ambient dimension or positive essential norm by itself is not an answer. If a bounded infinite TV-discrete carrier passes through any compact stage, that route is already impossible; otherwise the required noncompactness must be traced through the full chain and checked on the physical secants rather than on generic vectors.

## Keep algebraic identifiability, topology, capacity and downstream stability separate

Rank, spark and Radon criteria can prove exact injectivity without a quantitative inverse margin. AF-453 shows how source topology can kill that margin on continuous motions; AF-454 shows how bounded output packing can kill it on an infinite discrete alphabet; AF-455 shows how later compact processing can erase a margin that existed in the raw infinite-dimensional carrier. A fidelity theorem therefore has to state the admissible completed secants, source metric, retained operator class and positive source-relative lower gain. Otherwise it is only exact decoding, generic noncompactness, or an impossible stability target.
