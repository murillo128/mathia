---
id: CLUE-weil-inertia-wang-endpoint-localization-cancellation
type: research-clue
status: proposed
origin: mind
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-439-wang-endpoint-localization-already-forces-the-support-gap.md
---

# Can a signed or smoothed zero-window localization beat Wang's endpoint support loss?

## Observation

WI-439 shows that Wang's current comparison between the interval-zero object `A_I(x,t)` and the full explicit-formula object `A(x,t)` already produces `O(xL^3)` before the prime-polynomial mean-square step. After `x=T^alpha` and support integration this becomes `O(T^lambda L^2)`, reproducing the same fixed support restriction `lambda<theta` for `H=T^theta` even if the later arithmetic dephasing estimate were perfect.

The displayed proof reaches `O(xL^3)` by bounding `(|A_I|+|A|)|A_I-A|` in absolute value against the two endpoint tails. That identifies a precise interface where cancellation or smoother localization is currently discarded, but it does not establish that such cancellation exists.

## Research question

Is there a source-independent height-localization scheme, or a signed/coupled estimate for `A_I-A`, that replaces the current endpoint comparison by an error whose support integral is `o(HL)` in a regime reaching the boundary `lambda=theta` or beyond, while preserving the explicit-formula structure needed by Wang's short-interval pair-correlation argument?

## Why it may matter

WI-439 rules out improving only the prime polynomial `D_x` as a way to enlarge support. If the endpoint term can instead be reduced at its own interface, the arithmetic improvements studied elsewhere become relevant again. If it cannot, the support barrier is anchored earlier in the proof than the dephasing analysis and future work can stop revisiting prime-side refinements that leave localization unchanged.

## Decisive test

Start from the exact `A_I`/`A` decomposition used in Wang's localization lemma and replace only the endpoint-localization argument, keeping all later steps and normalizations fixed. Derive an explicit bound `E_loc(T,H,x)` such that for some fixed support range with `lambda>=theta`,

`int_0^lambda E_loc(T,H,T^alpha) d alpha = o(H log T)`.

The estimate must be uniform over the required height interval and must not use the desired pair-correlation or zero-density conclusion as an input. Kill the direction if every admissible smoothing or signed rearrangement still leaves an endpoint contribution of order `T^lambda log^2 T` at exponent level, or if any apparent gain is paid back by an equal or larger transition/tail term elsewhere in the same localization step.

## Evidence boundary

WI-439 proves only that the **current** endpoint comparison already carries the full support-scale loss and that prime-side dephasing alone cannot remove it. It does not prove a lower bound for all possible localizations, does not supply cancellation in `A_I-A`, and does not show that smoother windows improve the final theorem. This clue records those specific unproved escape interfaces without promoting them to an intuition or research theorem.
