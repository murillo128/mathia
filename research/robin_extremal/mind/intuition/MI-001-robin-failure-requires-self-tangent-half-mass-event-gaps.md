# MI-001 — Robin failure would require self-tangent source selection plus an exceptional mixed prime-race excursion

**Evidence level:** exact/literature-backed CA selection, height coupling, and prime-race reduction through RE-009

## Core intuition

A hypothetical Robin counterexample is not free to occur at an arbitrary extremal profile. The exact `log log n` normalization selects regular self-tangent colossally abundant states, and in the clean first-layer chamber their geometric location, Euler-product height, and prime-counting errors are tied to the same source.

The strongest current reduction is no longer merely a large event gap. After exact endpoint cancellation, every clean counterexample sequence must hit a **positive square-root-scale excursion of a classical mixed prime-race coordinate at the specially selected boundary primes**. The challenge is selection-specific: controlling that mixed race globally would already be RH-equivalent.

## Strongest justified principle

RE-001--RE-003 force infinitely many regular self-tangent CA counterexample peaks under RH failure and give exact secant/event-gap conditions with asymptotic half-jump thresholds. RE-004 shows higher-layer/tied transitions have zero count density, isolating a clean first-layer chamber, while RE-005 rules out generic peak monotonicity.

RE-006 gives the exact clean selector for consecutive primes `p<X<q`: the position `X-p` is the higher-layer CA mass minus the Chebyshev deficit. RE-007 computes the second-layer mass at square-root scale and obtains the dichotomy: unless `psi(p)-p` repeatedly tunes to the coefficient `-(sqrt(2)-1)`, the boundary prime gap must be `Omega(sqrt p)`.

RE-008 keeps the selector and Robin height in one exact calculation. Partial summation cancels the endpoint `vartheta(p)-p` contribution and leaves the endpoint-subtracted Mertens remainder `M_*(p)`. Along any unbounded clean counterexample sequence, `sqrt(p) log(p) M_*(p)` has liminf at least `2 sqrt(2)`.

RE-009 identifies this normalized remainder, up to `o(1)`, with the mixed error `E_{pi_l}(p)-E_theta(p)` studied in prime-race prior art. One-sided global boundedness of that difference is already equivalent to RH, so the remaining route cannot simply prove a global Mertens/Chebyshev estimate and call it intermediate.

## Program consequence

Exploit the **joint selection law** defining clean self-tangent counterexample boundary primes. A useful theorem should show that this selected subsequence is incompatible with the required mixed-race excursion, or prove that any counterexample sequence must concentrate in the zero-density exceptional event chamber.

The mixed-race coordinate is now a target-aware diagnostic. Its global behavior is too strong a target; the extra information must come from how CA geometry selects the sampling primes.

## Counterevidence / boundary

The current findings do not prove that the required selected excursions are impossible, and square-root prime-gap bounds at the needed pointwise quantifiers are unavailable. RE-009's RH-equivalent global bound does not imply that selection-specific estimates are equally hard; it only rules out forgetting the selector.

## Epistemic status

**Exact counterexample narrowing to a selected mixed prime-race excursion; not a proof of Robin's inequality or RH.**

## Falsification criterion

Find a clean counterexample peak violating the RE-006--RE-008 selector/height identities, or show that the RE-009 normalization does not match the cited mixed prime-race coordinate. A positive continuation should exploit the CA-selected subsequence rather than establish a global one-sided race bound.