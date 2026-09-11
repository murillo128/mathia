---
id: CLUE-nyman-beurling-localized-tail-flow-controls-recursive-repair
type: research-clue
status: resolved
origin: mind
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-047-vinogradov-korobov-cancellation-localizes-the-burnol-tail-signal.md
  - research/nyman_beurling/findings/NB-048-dilated-smaller-section-projection-approximates-the-unique-weighted-tail-repair.md
---

# Can the localized tail-flow mass control the recursive repair slack?

## Observation

NB-047 shows that the exact logarithmic step-tail flow carrying `d_N^2` can be localized below a deterministic doubly-logarithmic cutoff without paying an RH-equivalent ambient norm. NB-048 independently shows that the unique weighted-tail target repair can be replaced by the dilated best projection from the smaller section `V_K`, `K=floor(N/M)`, with exact squared error

`L_(M,N) - (1-d_K^2)/M`

and target-distance excess at most `d_K^2/M`.

These are two different reductions of the same finite Nyman difficulty: one reduces the **source witness scale**, the other the **target-oracle scale**. No persisted result relates the localized flow data to the recursive repair slack.

## Research question

For a predeclared cutoff `M=M_N` in the NB-047 localization regime, can the prefix discrepancies

`D_(L,N)`, `1<=L<M`,

or their exact logarithmic aggregate control the NB-048 repair slack

`L_(M,N) - (1-d_floor(N/M)^2)/M`

through an inequality that does not use `d_N`, `P_(V_N)e`, or `P_(V_floor(N/M))e` as an oracle?

A useful result may be one-sided. It is enough to derive a source-computable upper bound on the slack that is `o(d_N^2)` in a non-circular regime, or to prove that such a bound cannot follow from the localized directional data alone.

## Why it may matter

The current weighted-skeleton route has already separated conditioning from target access. NB-047 says the arithmetic directional signal is visible at a much smaller scale than an ambient RH-critical norm would suggest; NB-048 says exact geometric repair is recursively close to a smaller-section projection. A direct inequality between these objects could convert source localization into target preservation without solving the full section.

A negative result would be equally useful if it constructs two admissible source states with the same localized tail-flow data but substantially different recursive repair slack. That would prove that the small prefix, despite carrying the Burnol aggregate, is missing a target-relevant degree of freedom.

## Decisive test

Start from the exact identities in NB-047 and NB-048, with the same canonical best residual and the same fixed `M,N`. Express both the partial-flow mass and the weighted-tail projection error as quadratic forms of the finite residual/projection data. Determine whether the orthogonality relations `r_N perpendicular V_N` and the Bagchi dilation map force any nontrivial comparison.

Test first the scale where NB-047 guarantees `S_(M,N)=(1+o(1))d_N^2`. If a proposed bound still requires inserting `d_N` or `d_K` independently, expose that circularity. Conversely, a counterexample must respect the canonical Nyman normal equations rather than use an arbitrary Hilbert-space vector with the same finitely many tail averages.

The decisive positive target is a proved estimate of the form

`repair_slack <= E_(M,N)(localized prefix data)`

with `E_(M,N)=o(d_N^2)` under explicitly source-checkable hypotheses. The decisive negative target is a source-compatible family showing no such implication at the relevant scale.

## Evidence boundary

NB-047 establishes localization of one exact directional aggregate; NB-048 establishes a recursive approximation of the unique target repair. Neither finding proves that the localized discrepancies determine, estimate, or even correlate with the repair slack. This clue does not assert a new Nyman approximation rate and does not change the status of the existing accepted target-oracle clues. It isolates a new bridge between two later exact reductions that still requires ordinary Research Watch derivation, adversarial testing, and prior-art audit.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/nyman_beurling/findings/NB-049-ambient-dual-localization-turns-on-only-beyond-the-weighted-repair-threshold]]

`NB-049` shows that the clue's first proposed test scale is asymptotically non-discriminating. Any localization proof that closes through the ambient norm `||Omega_M||/d_N -> 0` necessarily forces `M d_N^2 -> infinity`, exactly the regime where `NB-039` says the unrepaired weighted skeleton already preserves the target distance and `NB-048` makes the recursive repair slack relatively negligible. The unresolved bridge therefore survives only in the critical/subcritical regime `M d_N^2=O(1)`, where a useful argument must exploit directional cancellation or another relation stronger than ambient Cauchy control.