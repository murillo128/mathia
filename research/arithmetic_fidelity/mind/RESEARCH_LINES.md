# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify observation gain only after source topology and output capacity both survive

**Linked intuition:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-451--AF-452 identify the exact fixed-source stability carrier: completable source-law secants. AF-453 rules out uniform total-variation control whenever that carrier contains weakly collapsing secants of nonvanishing TV size. AF-454 shows that making the source alphabet discrete is not enough: on an infinite one-atom alphabet, positive TV gain is equivalent to a uniformly discrete observation image, so every bounded finite-dimensional observation still has zero uniform margin.

The remaining quantitative question must therefore declare all three resources together. If the physical source is infinite and TV-discrete, what non-precompact observation resource is actually retained, and what lower gain does it have against matched controls? If the observation is bounded finite-dimensional, either restrict the source class to a finite capacity—subject to the packing bound `kappa <= R/(N^(1/d)-1)`—or use a weaker topology such as `W_1` or bounded-Lipschitz when that topology matches the physics. For `W_p`, `p>1`, the AF-452 homogeneous completion quotient cannot be imported unchanged.

## Keep algebraic identifiability, topology and stable physical inversion separate

Rank, spark and Radon criteria can prove exact injectivity without a quantitative inverse margin. AF-453 shows how topology can kill that margin on continuous source motions; AF-454 shows how output packing can kill it even on an infinite discrete alphabet. A finite-prefix fidelity theorem should therefore identify the admissible completed secants, source metric, observation norm/range and a positive lower gain in that geometry. Otherwise it is only an exact decoding statement or an impossible stability target.