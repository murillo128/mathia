---
id: CLUE-weil-positivity-translation-total-positivity-after-pick-universality
type: research-clue
status: resolved
origin: mind
target_line: weil_positivity
based_on:
  - research/arithmetic_fidelity/findings/AF-371-hankel-positivity-vs-total-positivity-target-fidelity.md
  - research/weil_positivity/mind/RESEARCH_LINES.md
  - research/mind/intuition/MI-002-the-surviving-arithmetic-variable-is-relational.md
---

# Can ordered translation total positivity escape finite Pick-jet universality?

## Observation

The current Weil-positivity frontier rules out finite scalar Pick matrices and finite confluent Pick jets as sign-producing arithmetic certificates: their positivity is inherited from a universal resolvent-Gram representation for arbitrary positive scalar Herglotz sources.

AF-371 supplies a mathematically different positivity benchmark for the same RH target class. For an entire `Psi` with the stated reciprocal-Laplace hypotheses, positivity of every Hankel moment matrix is still not enough to force `Psi` into the Laguerre--Pólya class, whereas Schoenberg's ordered translation determinants

`det(Lambda(x_j-y_k)) >= 0`

at every finite order are equivalent to the Pólya-frequency/Laguerre--Pólya condition. The distinction is therefore relational geometry, not merely the number of positivity inequalities.

## Research question

Does the actual scalar source object used by the Weil-positivity line admit a **canonical, source-derived** passage to a translation kernel `Lambda(x-y)` or an equivalent ordered kernel whose total-positivity minors are not already universal consequences of positive Herglotz measure?

The passage must be derived from the line's existing arithmetic/analytic source data; it must not insert `Xi`, its zeros, or an RH-equivalent Pólya-frequency kernel as an external target label. If no such natural passage exists, that itself kills this transfer.

## Why it may matter

Finite Pick-jet positivity has been exhausted because every such matrix stays inside one universal Gram category. AF-371 shows that an exact RH-equivalent positivity criterion can live in a different category: ordered translation total positivity. If the Weil source naturally produces such a kernel and some low-order or structural minors genuinely depend on arithmetic support rather than positivity alone, this would identify a concrete scalar direction outside the closed Pick-jet family. If the same positive-measure matched controls make the translation minors automatic, the clue would instead extend the universality obstruction.

## Decisive test

Start with the exact current Weil/Herglotz source representation and attempt to derive, without target import, a translation-invariant kernel `K(x,y)=Lambda(x-y)` or an explicitly equivalent ordered kernel.

Then perform the first nontrivial matched-control audit:

1. compute the `2x2` and `3x3` ordered minors from the source representation;
2. determine whether their sign follows for every admissible positive scalar Herglotz measure, or instead uses exact arithmetic support/mass coupling;
3. if the sign is universal, construct/identify a matched non-arithmetic positive source with the same mechanism and reject this route;
4. if the sign is nonautomatic, identify the exact additional source hypothesis and test whether the resulting kernel really falls under a Schoenberg-type reciprocal-Laplace/Laguerre--Pólya theorem rather than merely resembling it.

A successful first stage needs only a genuine nonuniversal ordered minor tied canonically to the source; full total positivity is a later theorem.

## Evidence boundary

AF-371 proves the Hamburger/Schoenberg separation in its own reciprocal-entire-function setting. The current Weil-positivity mind proves only that finite scalar Pick/confluent-jet positivity is universal in its Herglotz/resolvent category. No persisted result currently identifies the Weil source with a Pólya-frequency translation kernel, proves any nontrivial total-positivity minor, or shows that Schoenberg's criterion transfers to the existing Weil construction. This clue proposes that exact transfer test; it does not assert that the required kernel exists or that total positivity is easier than RH.

## Research disposition
Outcome: narrowed

Resolved by:
- [[research/weil_positivity/findings/WP-324-direct-laplace-translation-of-mangoldt-herglotz-source-is-strictly-sign-regular-not-polya-frequency.md]]

The direct source-native Laplace passage fails already at the first nontrivial ordered minor: its `2x2` and `3x3` translation determinants are strictly negative, and in fact all orders have the fixed sign `(-1)^(m(m-1)/2)` for every nondegenerate positive source measure. Reversing the orientation gives a Hankel kernel that is totally positive for every positive measure, so that repair is matched-control universal rather than arithmetic-selective. A future transfer would therefore need a genuinely different nonlinear or non-Laplace construction with an independent source-forced sign theorem.
