# MI-003 — Arithmetic selection can survive at zero order while canonical positive completion short-circuits its global energy

**Evidence level:** supported through WP-149 by exact resultant, inertia, graph-Dirichlet, and effective-resistance controls

## Core intuition

The zero-order cyclotomic resultant is unusually faithful to finite Weil arithmetic: it retains prime-power support and the critical half-density amplitudes. Yet every simple positive completion tested so far either destroys that selector or becomes globally degenerate.

The newest obstruction is stronger than extensive finite-dimensional inertia. The canonical conservative graph-Laplacian completion is uniquely forced and positive on every finite shell set, but opening the full prime alphabet gives infinite degree at every vertex. More decisively, spectator primes create infinitely many parallel bypasses around every resultant edge, driving its effective resistance to zero. The unchanged all-prime Dirichlet energy therefore has only constant finite-energy functions, independently of the ambient vertex measure.

## Strongest justified principle

WP-140--WP-145 separate generic positive scale responses from the exact zero-order cyclotomic resultant. The resultant carries the desired sparse prime-power amplitudes, while its sign-flipped Hessian fills in the missing support and loses the arithmetic selector.

WP-146--WP-147 keep the zero-order kernel and test after-the-fact finite repair. A mixed-prime chain is already centered-indefinite, and spectator-prime replication makes both primitive inertia indices unbounded. Fixed codimension, fixed rank, and fixed finite-dimensional auxiliary/archimedean Schur sectors cannot repair the sign.

WP-148 tests the canonical diagonal escape. Requiring the off-diagonal interaction `-J` and conservation of constants uniquely forces the weighted graph Laplacian. Its finite energy is positive, but every shell has infinite fresh-prime degree, with exact edge weight `log p/sqrt(p-1)`. On natural shell-counting `ell^2`, every nonzero vector has infinite energy.

WP-149 closes the measure-only/noncompact-energy escape for the unchanged interaction. Multiplying any resultant edge by a fresh spectator prime copies the middle edge exactly and supplies two universal side edges. The resulting pairwise edge-disjoint bypasses have divergent total parallel conductance, so every nonzero resultant edge has zero effective resistance. Connectedness then forces every finite-energy function to be constant. For any faithful positive atomic vertex measure, the finite-energy intersection is at most the constant line and is never a dense nontrivial domain.

## What remains possible

Changing only the shell measure, diagonal self-energy, or finite-dimensional correction is no longer viable for the canonical resultant Dirichlet form. A surviving route must change the interaction or assembly before the all-prime limit: for example a source-forced renormalized/nonlocal conductance, a provenance-sensitive quotient that removes spectator replication, a coupled finite--archimedean/cohomological term, or a different energy whose domain and sign are derived together.

Any such operation must still preserve the prime-power selector and supply an independent global positivity/coercivity theorem. Arbitrary subtraction of the divergent spectator network would be a new input, not a consequence of the existing resultant geometry.

## Status / novelty

Cyclotomic resultants, graph Laplacians, electrical networks, Dirichlet forms, and finite-rank inertia are classical. The synthesis is the selector/sign boundary: **the faithful zero-order kernel is not merely indefinite before repair; its canonical positive all-prime energy is electrically short-circuited by exact spectator replication**.

## Falsification criterion

Construct a nonconstant finite-energy function for the unchanged WP-149 resultant network, or a faithful vertex measure on which its finite-energy domain is densely nontrivial. A modified interaction or source-forced renormalized energy would evade rather than falsify the obstruction.

## Lean-formalizable core

- Cyclotomic resultant prime-power support.
- Finite conservative graph-Laplacian positivity and uniqueness.
- Infinite fresh-prime degree.
- Spectator-prime edge replication.
- Parallel-conductance/effective-resistance collapse.
- Constancy of finite-energy functions.
