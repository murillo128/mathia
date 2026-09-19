---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: proposed
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-382-iterated-q-vdc-has-an-intrinsic-loglog-source-horizon.md
  - research/mobius_cancellation/findings/MC-383-small-doubling-family-mean-value-retains-global-modulus-horizon.md
  - research/mobius_cancellation/findings/MC-396-paired-block-packing-removes-inverse-gap-depth-tax.md
---

# Can endpoint source averaging be kept inside q-vdC before modewise collapse?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` then shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

There is, however, concrete prior art for a different kind of escape. Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) improves the exponent of distribution for primes to smooth moduli by modifying the q-van der Corput step so that an additional summation variable in the Type I exponential sums is not treated trivially. The gain comes from the precise multi-variable phase and from retaining averaging through the differencing argument, not from a better bound for each individual character sum after all other variables have been frozen.

That theorem is not an endpoint-source theorem and does not directly apply here. Its relevance is narrower: it gives an existence proof that the specific escape left open by `MC-382`—avoiding a purely modewise q-vdC recursion by preserving extra averaging—can be mathematically real in a nearby smooth-modulus setting.

## Research question

Can the Selberg/prime-frame transfer underlying `MC-377`--`MC-396` be reorganized *before* source modes are bounded one at a time so that a genuine source, sieve-divisor, or shell variable remains averaged inside the q-vdC phase, in a form structurally analogous to Stadlmann's modified Type I step?

The target is not an averaged theorem by name. It is an exact representation in which the endpoint frame quantity that must be controlled is expressed as one multi-variable exponential sum (or a bounded number of such sums) whose differencing acts while a nontrivial source-family variable is still live. The representation is useful only if this prevents the terminal saving from being raised through `2^{-k}` independently for every conductor layer and also avoids the fixed `P^theta` global-modulus tariff ruled out in `MC-383`.

## Why it may matter

After `MC-396`, further block-packing improvements inside the same single-character recursion can change constants but not the exponential source-depth scale. A successful variable-retaining reformulation would attack exactly that remaining analytic bottleneck rather than another combinatorial source-cost loss.

Conversely, an exact collapse showing that every natural pre-absolute-value source average either diagonalizes by character orthogonality, reduces to the already-audited common-modulus mean-value shape of `MC-383`, or recreates the individual Proposition-7 recursion would close a concrete class of the main escape routes left open by `MC-382`.

## Decisive test

Start from the actual normalized prime-frame/Selberg expression used to turn endpoint source characters into shell-bias bounds in `MC-377`--`MC-396`, before applying triangle inequality or a character-by-character incomplete-sum estimate. Keep simultaneously visible the source-mode index, the sieve divisor variables, and the interval/shell summation variable.

First derive the exact result of summing over a rank-`d` endpoint subgroup at this stage. If character orthogonality immediately collapses the expression to signature/coset incidences with no oscillatory variable left, record that as a kill: Stadlmann-style extra averaging is unavailable in this representation. If a genuinely mixed phase survives, identify one explicit variable that was previously frozen and carry one q-vdC/Cauchy step with that variable still averaged.

The direction survives only if the resulting estimate has a resource scaling qualitatively different from both known barriers: it must avoid a `2^{-Omega(A)}` saving produced solely by sequential conductor depth and avoid a fixed positive power `P^theta` of the global common radical. Merely averaging the already-derived individual bounds, invoking a large sieve after absolute values, or obtaining another `exp(O(R))` family-cardinality gain against `P^theta` rejects the candidate.

As a literature control, reconstruct the exact role of the previously-trivial summation variable in Stadlmann's Section 3 Type I/q-vdC argument and verify that any proposed endpoint dictionary preserves the feature responsible for the gain rather than only the phrase “additional averaging.”

## Evidence boundary

No collective endpoint character-sum estimate is established here, and Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setup. Nothing in that work implies improved Möbius cancellation or the endpoint source-cost bound sought by this line.

The only established point is the prior-art narrowing: modified q-vdC with retained auxiliary averaging is a concrete analytic mechanism in a nearby smooth-modulus problem, while `MC-382`, `MC-383`, and `MC-396` show exactly which two resource tariffs an endpoint adaptation would have to avoid. Whether the endpoint frame possesses the required mixed variable is the unresolved mathematical test.
