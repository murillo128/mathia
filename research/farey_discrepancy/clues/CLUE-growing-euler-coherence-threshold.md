---
id: CLUE-farey-growing-euler-coherence-threshold
type: research-clue
status: resolved
origin: mind
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-215-finite-euler-factor-coherence-still-preserves-all-integer-switched-blindness.md
  - research/mobius_cancellation/findings/MC-395-moving-cutoff-quantifies-full-rank-source-cost.md
---

# How fast can imposed Möbius Euler coherence grow before all-integer switched blindness breaks?

## Observation

`FD-215` closes every **fixed finite** Euler-coherence repair of the Farey countermodel. For any fixed finite prime set, one can impose the exact relations `xi_(pn)=-xi_n` on the relevant squarefree support while retaining a bounded all-integer switched blind mode with supercritical summatory growth. The construction uses a finite Euler-product inverse/Green operator, so the proof is deliberately non-uniform in the chosen prime set and leaves scale-growing multiplicative coherence open.

Independently, `MC-395` shows in a different Möbius-cancellation endpoint architecture that a moving source cutoff develops a quantitative analytic tariff and that the transition becomes visible near a `log log` scale. That result does **not** transfer a threshold to Farey discrepancy. It is only evidence that fixed-parameter absorption can conceal the cost that appears when the number or range of source relations grows with scale.

## Research question

Let `P_N` be a prime set that grows with the Farey horizon. Can the `FD-215` blind construction be made uniform while enforcing

`xi_(pn)=-xi_n`

for every `p in P_N` and every relevant squarefree `n`, still keeping exact all-integer switched blindness and partial sums of order `N^(1/2+delta)` for some fixed `delta>0`?

Determine the largest regime that can be certified in terms of `|P_N|`, the largest constrained prime, or the norm/size of the finite Euler inverse. In particular, decide whether **any** unbounded `|P_N|` is compatible with the blind construction before asking whether a special scale such as `log log N` is meaningful.

## Why it may matter

Squarefree support, ternary unit amplitudes and every fixed finite collection of exact Möbius Euler relations are now known to be insufficient discriminators. A quantitative growing-coherence threshold would distinguish two very different possibilities: either the missing arithmetic law is simply the accumulation of sufficiently many exact local multiplicative constraints, or even substantial scale-growing Euler coherence can still be absorbed and the decisive information must be more global than primewise sign compatibility.

This also provides a controlled cross-line comparison with the source-cost phenomenon in Möbius cancellation without asserting that the two ledgers are the same.

## Decisive test

Redo the `FD-215` construction with `P=P_N` variable and expose every dependence on `P`: the Euler inverse/Green-operator coefficients, support density, rounding margin, switched-filter error and final summatory exponent. Test canonical families such as the first `k(N)` primes and all primes up to a cutoff `y(N)`.

A positive result must give an explicit unbounded regime in which all constraints, blindness and supercritical growth hold simultaneously. A negative result must prove that some quantified growth of the prime set forces the correction norm or residual error to overwhelm the blind construction; failure of the existing proof to remain uniform is not such an obstruction.

Only after this Farey-specific dependence is derived should its scale be compared with the `MC-395` `log log` transition. A numerical resemblance of thresholds is not evidence of a common mechanism.

## Evidence boundary

`FD-215` proves only fixed-finite-prime coherence and permits its constants to deteriorate with the prime set. `MC-395` concerns a different source package, endpoint geometry and analytic differencing argument; it neither predicts nor bounds the Farey threshold. No growing-prime-set countermodel, obstruction, `log log N` law, improved Mertens estimate or RH consequence is established here.

## Research disposition

Outcome: supported

Resolved by:
- [[research/farey_discrepancy/findings/FD-216-logarithmically-growing-euler-coherence-remains-horizon-locally-blind]]

`FD-216` gives the requested explicit unbounded regime: for any fixed `c<1/(2 log 2)`, the first `floor(c log N)` prime Euler relations can be imposed exactly in an `N`-dependent squarefree ternary countermodel while the switched Farey filter remains sub-square-root on the target scale and the partial sum is `N^(alpha-o(1))`, `alpha>1/2`. The constant is a sufficient threshold from a crude `2^k` Euler-cube cost, not an optimal barrier. The same finding also separates this finite-horizon statement from the coherent global limit: one fixed squarefree source satisfying an eventually exhaustive nested family of exact prime relations is necessarily the Möbius function itself.