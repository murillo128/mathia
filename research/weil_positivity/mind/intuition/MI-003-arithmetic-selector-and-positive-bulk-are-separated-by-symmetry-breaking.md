# MI-003 — Arithmetic selection can survive at zero order while every simple positive completion misses or fights it

**Evidence level:** supported through WP-147 by exact Kron, Fisher, resultant-Hessian, conditional-sign, replication, and finite-rank controls

## Core intuition

Positivity does not automatically erase arithmetic, but the operation that exposes an easy sign can act at the wrong derivative or coupling level. The zero-order cyclotomic resultant is unusually faithful to the finite Weil arithmetic: it keeps prime-power support and the critical `log p/p^(k/2)` amplitudes. Yet differentiating it into canonical positive curvature fills in the missing support, while keeping it at zero order produces mixed-prime two-sided inertia that ordinary centering cannot repair.

The gate is therefore stronger than “preserve provenance before differentiating.” A viable sign theorem must preserve the selector **and** alter its mixed-prime assembly through genuinely global structure; fixed finite-dimensional cleanup after the arithmetic block is formed is insufficient.

## Strongest justified principle

WP-140--WP-144 isolate universal positive logarithms and scale anomalies: scale-invariant SPD/Kron responses can be independently positive while remaining composite-matched. WP-145 then shows that the exact cyclotomic log-resultant has the desired sparse prime-power amplitudes, but its sign-flipped vertex Hessian couples every primitive-shell pair, including resultant-one controls. The easy positive curvature differentiates the arithmetic support away and does not supply a unified finite--archimedean curvature.

WP-146 tests the opposite strategy: keep the zero-order normalized resultant and seek positivity only after quotienting constants. The exact chain `6 -> 12 -> 36` retains the critical weights `log 2/sqrt 2` and `log 3/sqrt 3`, but their inequality makes the centered three-node form indefinite. An equal-weight path is conditionally negative, so the obstruction is tied to the arithmetic mismatch rather than path topology alone. Row-plus-column gauges and a separate unchanged global sector do not repair the witness.

WP-147 proves that this is extensive, not a one-block accident. Multiplying the chain by distinct spectator primes produces infinitely many exact resultant-orthogonal copies with identical bad weights. Both positive and negative primitive inertia indices therefore grow without bound. Any fixed bounded-codimension constraint, fixed-rank Hermitian correction, or fixed finite-dimensional auxiliary/archimedean sector eliminated by Schur complement leaves both signs once enough blocks are included.

## What remains possible

A surviving resultant route must change the finite arithmetic block before the sign theorem by an operation whose rank/codimension grows with the arithmetic sector or is intrinsically infinite-dimensional/nonseparable. Possibilities include a genuinely coupled finite--archimedean/cohomological completion, full-rank nonlocal modification, or a source-forced infinite-dimensional quotient. Arbitrary diagonal or full-rank repair is not ruled out mathematically, but its canonicity and preservation of the prime-power selector must be derived independently.

## Status / novelty

Kron reduction, cyclotomic resultants, graph Laplacians, Schoenberg conditional kernels, inertia, and finite-rank perturbation theory are classical. The synthesis is the selector/sign boundary: **the faithful zero-order arithmetic kernel has extensive mixed-prime inertia, while its canonical positive derivative loses the selector; finite-dimensional after-the-fact repair closes neither gap**.

## Falsification criterion

Construct a fixed finite-dimensional or fixed-codimension completion contradicting the WP-147 inertia amplification, or derive a canonical growing/infinite completion that preserves exact prime-power amplitudes and supplies the required finite--archimedean sign without inserted zero data.

## Lean-formalizable core

- Cyclotomic resultant prime-power support.
- Full-support positive resultant Hessian.
- Three-chain centered indefiniteness.
- Direct-sum inertia amplification and finite-rank/codimension obstruction.
