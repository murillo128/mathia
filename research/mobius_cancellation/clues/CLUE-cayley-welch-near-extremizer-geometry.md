---
id: CLUE-mobius-cancellation-cayley-welch-near-extremizer-geometry
type: research-clue
status: resolved
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md
  - research/mobius_cancellation/findings/MC-386-welch-energy-makes-source-exception-threshold-sharp.md
  - research/mobius_cancellation/findings/MC-387-near-welch-concentration-forces-annihilator-stability.md
---

# Must near-minimal exceptional source frames look like annihilator subgroups?

## Observation

`MC-386` shows that every rank-at-most-`R` endpoint Cayley Gram kernel on a surviving group `W` of size `H` carries at least `H/R-1` off-zero squared correlation energy. It also gives an exact abstract extremizer: when the Fourier eigenvalue support is a subgroup of size `R`, the physical correlation kernel is the indicator of its annihilator, so exactly `H/R-1` nonzero differences carry all the off-diagonal energy and every other difference has zero correlation.

`MC-387` now proves the corresponding finite-harmonic stability statement. If a PSD Cayley kernel nearly saturates the Welch floor and almost all of its energy is concentrated on essentially `H/R` physical modes, then its Fourier probability measure is close to uniform on a coset of a subgroup and its physical concentration set is close to the corresponding annihilator subgroup. Thus the generic frame question is no longer whether arbitrary near-extremizers exist: near extremizers are forced into near-subgroup geometry.

What remains unknown is whether an **arithmetic source frame** built from primitive quadratic characters can approach that extremal geometry.

## Research question

Suppose the actual endpoint source kernel `g` nearly saturates the frame-energy lower bound while almost all of its off-zero energy is concentrated on a set `B subset W\{0}` with

\[
|B|=(1+o(1))H/R.
\]

`MC-387` forces `B union {0}` to be close to an annihilator subgroup and the nonzero Fourier eigenvalues to be close to a uniform measure on a dual coset. Can the lower-prime source-conductor map, primitive-conductor reduction, or quadratic-character multiplication law rule out that near-subgroup pattern at the source-cost scales relevant to the endpoint program?

The desired bridge is now specifically from **near-annihilator frame geometry** to a concrete arithmetic restriction on which source differences can remain exceptional.

## Why it may matter

Ambient exceptional-modulus counts fail because they do not see how the thin source-conductor image intersects the exceptional set. `MC-386` shows that cardinality alone cannot do better than `H/R`; `MC-387` sharpens this by proving that near-optimal concentration cannot occur on an arbitrary set of that size.

The surviving problem is therefore structurally narrower: an endpoint escape must organize its bad source differences into an approximate subgroup/annihilator pattern. Multiplication of quadratic characters, primitive-conductor reduction, and lower-prime source provenance interact with subgroup closure, so this shape may be arithmetically impossible even though it is abstractly optimal. Conversely, an explicit arithmetic realization would show that the `H/R` exceptional scale is genuinely reachable by the source family and would close this escape negatively.

## Decisive test

The finite harmonic stage is resolved by `MC-387`; do not repeat generic Welch, uncertainty, or frame-stability arguments.

Work in the exact endpoint source-character/conductor dictionary. Pull a hypothetical near-coset Fourier support and near-annihilator physical exceptional set through multiplication of the primitive quadratic source characters. Determine whether approximate subgroup closure forces one of the following at the relevant scales: excessive reuse of a small set of source primes, repeated primitive conductors, collapse of distinct source differences to the same primitive character, or a source-incidence pattern incompatible with the rank and source-cost constraints already proved in `MC-374`--`MC-386`.

Kill the clue if an explicit family of admissible endpoint source characters realizes the near-coset/annihilator geometry while respecting those conductor and source-cost constraints. Accept a positive arithmetic conclusion only if the contradiction uses the actual source/conductor structure and not merely another abstract rank, energy, or cardinality bound already saturated by `MC-386`.

## Evidence boundary

`MC-387` establishes the finite-harmonic stability implication, but **no arithmetic incompatibility is established**. It does not show that actual primitive quadratic source characters cannot realize or approximate the near-coset pattern. No stronger source-cost bound, Möbius estimate, or RH consequence follows yet.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/mobius_cancellation/findings/MC-388-endpoint-simplex-rank-excludes-near-annihilator-sharpness.md]]

`MC-388` identifies the Bochner support of every exact endpoint partition frame as the projection of the translated coordinate simplex `1+e_z`. Its affine dimension is at least `dim W-1`. In the rank-linear source-cost branch `MC-381` retains `dim W>=3R/4`, whereas the near-extremizer forced by `MC-387` would require that support to be `o(R)`-close to an `R`-point coset of dimension only `O(log R)`. An exact rank argument forces `Omega(R)` support points outside every such coset, so the near-annihilator realization is impossible in the relevant high-dimensional endpoint regime before primitive-conductor details enter.

This resolves the clue's live high-dimensional branch negatively. It does not improve the `H/R` exceptional-count scale by itself: obtaining a stronger frame contradiction now requires a quantitative additive-energy or physical-spread gap for high-affine-rank projected endpoint simplices.