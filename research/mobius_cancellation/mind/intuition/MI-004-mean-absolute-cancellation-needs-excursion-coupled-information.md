# MI-004 — Mean-absolute Mertens control needs occurrence order, not richer finite summaries

**Evidence level:** exact endpoint reductions, literature-backed Mertens lower bounds, and matched-control obstructions through MC-132

## Core intuition

The mean-absolute endpoint is RH-complete, but the natural finite summaries tested so far forget exactly the information that endpoint consumes. The issue is no longer merely fixed local memory. MC-129--MC-132 show that increasingly rich descriptions can agree exactly while carrying radically different excursion amplitudes: full local/modular transition tensors, fixed finite-horizon path types, periodic clocks, and even polynomial timestamp moments of each transition state.

The missing source information is therefore **ordered excursion structure**. A successful theorem must retain how signed increments are arranged across occurrences and scales, or use a Möbius-specific arithmetic law that forces that order strongly enough to recover first-absolute amplitude.

## Strongest justified principle

MC-122 identifies deterministic amplitude feedback with quadratic path energy. MC-123--MC-124 close scalar state-local and fixed finite-memory sign-odd channels. MC-129 constructs product-state controls with matched local context, modular height, increment, and coarse time information but different first-absolute excursion.

MC-130 proves that any fixed finite horizon is only a larger product-state type. MC-131 shows that adjoining any fixed family of periodic clocks remains excursion-blind after taking the joint period. MC-132 then uses Prouhet--Thue--Morse macro-order controls to match, state by state, every polynomial timestamp moment through a declared degree while retaining a large excursion separation. The same obstruction survives a logarithmically growing moment degree below its explicit information threshold.

Thus “add more finite state,” “remember a bounded path window,” and “add finitely many absolute-time moments” are no longer distinct escape routes. They remain compressions of occurrence order.

## Counterevidence / boundary

The controls are generic bounded-increment words. They do not preserve Möbius multiplicativity, square-free zeros, prime values, divisor relations, or another arithmetic source law. They also do not match the complete ordered timestamp list, the full timestamp empirical measure, arbitrary adaptive/nonpolynomial weights, or an unbounded nested state whose information budget grows fast enough to reconstruct order.

Accordingly, the obstruction does not show that nonlocal or growing-memory arithmetic observables are useless. It says they must demonstrate information not already determined by the flattened finite/quasi-polynomial summaries.

## Epistemic status

**Exact generic information-loss boundary; open Möbius-specific theorem converting genuinely order-sensitive arithmetic information into RH-scale first-absolute control.**

## Falsification criterion

Exhibit a fixed finite-memory/path-type/periodic/polynomial-time summary contradicted by the exact MC-129--MC-132 controls, or derive first-absolute Mertens control from such a summary with a hypothesis satisfied by those controls. A positive escape should instead identify the ordered or arithmetic datum that the controls cannot match and prove its quantitative transfer to the endpoint.