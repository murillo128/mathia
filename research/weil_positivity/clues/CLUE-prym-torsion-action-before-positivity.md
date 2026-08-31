---
id: CLUE-weil-positivity-prym-torsion-action-before-positivity
type: research-clue
status: proposed
origin: mind
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-055-minimal-cyclotomic-double-cover-hodge-transfer-is-degree-flat.md
  - research/weil_positivity/findings/WP-056-prym-polarization-stores-log-p-in-integral-discriminant.md
  - research/weil_positivity/findings/WP-057-prym-discriminant-is-torsion-invisible-to-real-quadratic-positivity.md
---

# Can the Prym torsion carrier act on non-torsion data before positivity is formed?

## Observation

The granted hyperelliptic old-prime cover tower has reached a sharp category boundary. `WP-056` shows that the Prym polarization kernel remembers the prime degree intrinsically through `|K_{n,p}|=p^{2g_n}`, hence through the normalized logarithmic discriminant `log p`. `WP-057` then proves that this carrier cannot itself support the desired ordered real quadratic form: it is finite torsion, Néron--Tate pairing kills it even against non-torsion points, and its intrinsic theta-group pairing is alternating and phase-valued.

The same theta group nevertheless has a canonical finite-Heisenberg action on a genuine vector space. `WP-057` only shows that the obvious normalized Hermitian geometry sees `p` through representation dimension/cardinality, not that every **relative action on larger non-torsion data** is dimension-only.

## Research question

Does the Prym polarization kernel or its theta/Heisenberg extension act canonically on a non-torsion geometric or analytic space associated with the cover tower in such a way that a positive **relative** pairing, spectral shift, or determinant response retains a normalized one-step `log p` term without first extracting `log |K|` by hand?

The action must be derived from the old-prime cover/polarization structure itself. It should not define a positive operator by inserting the already-computed scalar `log p` or by taking the logarithm of representation dimension and multiplying the identity.

## Why it may matter

This is the narrowest surviving way to use the strongest local finite-prime carrier found by the positivity line while respecting `WP-057`. If the torsion acts nontrivially **before** the real positive pairing is formed, the prime scale might enter through a relative spectral or index mechanism rather than through a quadratic form on torsion points. A negative classification showing that every canonical positive action invariant factors only through cover degree, `|K|`, or representation dimension would close the Prym route much further.

## Decisive test

Starting from the exact cyclic cover and its Prym polarization, construct the candidate action and identify the non-torsion target space without using zeta zeros or the desired Weil coefficient. Then:

1. prove the proposed pairing/operator is canonical and positive for an independent reason;
2. compute its one-step and `p^k`-step relative response;
3. test whether the normalized response contains `log p` linearly rather than only through `log |K|`, dimension, or universal cover degree;
4. compare against non-arithmetic cyclic covers with the same degree, genus, ramification type, and polarization type.

A matched-control equality or a factorization through those universal cover invariants rejects the mechanism. A surviving response would still require a separate global archimedean/polar and Weil-sign audit.

## Evidence boundary

No such positive relative action invariant is currently established. The hyperelliptic lift itself is a granted minimal enrichment rather than a structure forced by the original Prime Circle. `WP-056` establishes only the integral discriminant carrier, and `WP-057` decisively excludes direct real quadratic/height pairing on that carrier while identifying the theta/Heisenberg action as the strongest canonical structure left. This clue is therefore a research lead, not evidence for positivity, novelty, or RH.
