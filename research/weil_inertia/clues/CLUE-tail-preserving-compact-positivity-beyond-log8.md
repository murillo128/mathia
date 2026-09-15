---
id: CLUE-weil-inertia-tail-preserving-compact-positivity-beyond-log8
type: research-clue
status: resolved
origin: mind
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-302-liu-source-exact-certificate-claims-positivity-through-17-16.md
  - research/weil_inertia/findings/WI-303-finite-rank-tail-rank-is-noncanonical.md
---

# Is a finite positive tail correction the minimal source-exact mechanism that can cross the `log 8 / 2` compact-positivity threshold?

## Observation

WI-302 records a recent author-certified computational claim of compact Weil positivity through aperture `17/16`, beyond the `log 8 / 2` threshold where a simpler tail-dropping localization ceases to be justified. The claimed construction keeps the arithmetic source exact and retains a positive rank-two tail inside a block-Schur certificate instead of discarding the complement.

That external certificate has not yet been independently replayed or analytically audited at the standard required by this line, so its positivity claim is not current Mathia theorem-level evidence. What is already useful is the structural contrast it exposes: the first claimed crossing of the threshold changes the localization architecture by preserving finite positive tail directions.

## Research question

Within the same source-exact compact-window decomposition, is some nontrivial positive tail correction **mathematically necessary** once the aperture crosses `log 8 / 2`, and if so what is the minimal rank/structure required?

More concretely, can the tail-preserving block decomposition be derived independently enough to prove either that rank zero/one corrections cannot close the post-threshold Schur complement while rank two can in principle, or that the apparent rank-two mechanism is merely one implementation of a more general positive-tail invariant?

## Why it may matter

A necessity theorem would turn an unverified certificate architecture into a reusable structural discriminator. It would tell future compact-positivity searches which degrees of freedom must be retained when new prime-power channels enter, instead of treating larger numerical matrices as the mechanism. Conversely, a rank-one or tail-free counterconstruction would show that the architecture seen in WI-302 is not structurally forced and should not guide the line before independent replay.

This question also preserves source exactness: it asks what finite positive complement information must survive the localization, not whether a truncated surrogate can be tuned to fit a desired sign.

## Decisive test

Reconstruct the source-exact finite/complement block decomposition around the first aperture above `log 8 / 2` without importing the numerical verdict of the external package. Identify the exact Schur-complement contribution of the omitted tail and its positive rank.

Then prove one of the following on the smallest post-threshold source configuration: a rank-`<=1` impossibility under the exact source constraints; an explicit source-exact rank-`<=1` positive certificate; or a representation theorem showing that the claimed rank-two term is equivalent to a lower-dimensional invariant. The test must be symbolic/exact at the structural level; reproducing a floating-point positive eigenvalue alone does not settle minimality.

## Evidence boundary

WI-302 does **not** currently establish Mathia-level positivity at `17/16`: the recorded package is author-certified but independent replay and analytic audit are still missing. This clue therefore does not assume that the rank-two certificate is correct, necessary, or novel. It asks only whether the architectural change recorded in the persisted finding corresponds to a genuine post-threshold structural requirement.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/weil_inertia/findings/WI-303-finite-rank-tail-rank-is-noncanonical.md]]

WI-303 shows exactly that Liu's rank-two term is a noncanonical finite-rank Loewner minorant extracted from a stronger noncompact positive tail operator. Source-exact rank-zero, rank-one and higher-rank extractions are available, so rank two is not structurally minimal. The surviving structural distinction is instead between retaining noncompact/source-exact tail information and trying to repair a tail-dropped comparison by a fixed compact correction. Whether rank zero or one still closes Liu's particular `N=448` finite matrix is a certificate-specific question, not a post-threshold rank invariant.