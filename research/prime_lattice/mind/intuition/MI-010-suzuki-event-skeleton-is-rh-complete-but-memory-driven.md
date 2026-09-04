# MI-010 — Suzuki's prime-power event skeleton is RH-complete at one-sided boundedness, but its decisive state is cumulative history rather than terminal recovery geometry

**Evidence level:** supported by PL-150 and PL-153; PL-154 is excluded while its adversarial review remains open

## Core intuition

The completed Suzuki scalar can be sampled only at its ordered prime-power events without losing the RH sign problem. In fact, one-sided boundedness of those event values is already equivalent to RH. But the local geometry between events becomes asymptotically too small to explain that equivalence: after the last event, convex recovery has vanishing drawdown controlled by the next prime gap.

The event skeleton is therefore an exact **carrier of the completed criterion**, not yet a generative mechanism. Its load-bearing information is accumulated event history and the globally completed state entering each checkpoint, not the terminal interpolation shape.

## Strongest justified principle

PL-150 proves that the recovery drawdown after a prime-power event is `O(q^-0.45)` in the stated unconditional regime and that recoveries occur infinitely often. Large negative minima cannot be attributed to the final convex recovery segment; they must be inherited from the accumulated event history before that segment.

PL-153 sharpens the discrete reduction dramatically. If `E_j` denotes the completed scalar at the ordered prime-power checkpoints, then RH is equivalent to either one-sided bound

`sup_j E_j < infinity`

or

`inf_j E_j > -infinity`.

If RH fails, the same event sequence has both `limsup E_j=+infinity` and `liminf E_j=-infinity`. Thus the discrete skeleton is RH-complete even without a sign-at-every-checkpoint formulation.

This does not explain why a one-sided bound should hold. The completion, zero-sensitive transform, and long event memory are already built into `E_j`. PL-154 is not used here because its growth-exponent proof is still under adversarial review.

## What remains possible

A positive mechanism should represent the cumulative event history in a source-forced state space and derive a one-sided coercive bound before invoking the RH equivalence. Local prime-gap recovery estimates can simplify the carrier by removing terminal interpolation, but they cannot supply the missing global sign by themselves.

## Status / novelty

The Suzuki criterion and explicit-formula ingredients are literature-backed; the event reductions are persisted exact findings. The synthesis is the mechanistic separation: **RH completeness of the event sequence does not make its local event geometry explanatory; the unresolved resource is cumulative completed memory**.

## Falsification criterion

Derive a one-sided checkpoint bound from source information that does not already assume an RH-equivalent completed criterion, or show that terminal/local event geometry contributes an order-one obstruction contrary to PL-150.

## Lean-formalizable core

- Prime-power checkpoint reduction.
- One-sided-boundedness equivalence.
- Vanishing terminal recovery drawdown.
- Separation of event interpolation from cumulative state.
