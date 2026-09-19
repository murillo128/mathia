---
id: CLUE-mobius-cancellation-cayley-welch-near-extremizer-geometry
type: research-clue
status: proposed
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md
  - research/mobius_cancellation/findings/MC-386-welch-energy-makes-source-exception-threshold-sharp.md
---

# Must near-minimal exceptional source frames look like annihilator subgroups?

## Observation

`MC-386` shows that every rank-at-most-`R` endpoint Cayley Gram kernel on a surviving group `W` of size `H` carries at least `H/R-1` off-zero squared correlation energy. It also gives an exact abstract extremizer: when the Fourier eigenvalue support is a subgroup of size `R`, the physical correlation kernel is the indicator of its annihilator, so exactly `H/R-1` nonzero differences carry all the off-diagonal energy and every other difference has zero correlation.

Thus `MC-385`'s exceptional-count scale is not merely an artifact of an absolute row-sum estimate. A generic PSD Cayley frame can really hide the required correlation in only about `H/R` differences. What is not known is whether an **arithmetic source frame** built from primitive quadratic characters can approach that extremal geometry.

## Research question

Suppose the actual endpoint source kernel `g` nearly saturates the frame-energy lower bound while almost all of its off-zero energy is concentrated on a set `B subset W\{0}` with

\[
|B|=(1+o(1))H/R.
\]

Does positivity plus near-minimal physical support/energy concentration force `B union {0}` to be close, in a quantitative sense, to an annihilator subgroup of `W`, with the nonzero Fourier eigenvalues correspondingly close to a uniform measure on a dual subgroup? If so, can the lower-prime source-conductor map or the quadratic-character multiplication law rule out that near-subgroup pattern at the source-cost scales relevant to the endpoint program?

The point is not to prove a generic stability theorem for its own sake. The desired bridge is from **near-extremal frame geometry** to a concrete arithmetic restriction on which source differences can remain exceptional.

## Why it may matter

Ambient exceptional-modulus counts fail because they do not see how the thin source-conductor image intersects the exceptional set. `MC-386` shows that cardinality alone cannot do better than `H/R`: an annihilator subgroup is a sharp matched control.

A stability theorem would convert the surviving problem from “exclude an arbitrary set of about `H/R` bad differences” into “exclude a highly organized near-subgroup of bad source differences.” That is a much more arithmetic target because multiplication of quadratic characters, primitive-conductor reduction, and lower-prime source provenance interact with subgroup closure. Conversely, an explicit non-subgroup near-extremizer would kill this route and show that even exceptional-set geometry is too flexible at the abstract frame level.

## Decisive test

First solve the finite harmonic problem without arithmetic. For positive-definite Cayley kernels `g` on `W=F_2^d` with `g(0)=1`, Fourier support at most `R`, and off-zero energy within `o(H/R)` of the Welch floor, determine whether concentration of all but `o(H/R)` energy on a set of size `(1+o(1))H/R` forces quantitative proximity to the subgroup/annihilator extremizers. Search the finite-group uncertainty and tight-frame literature for an existing stability theorem before deriving one.

Kill the clue immediately if there are explicit families with Fourier support at most `R`, nonnegative Fourier spectrum and near-minimal physical concentration whose heavy-correlation set stays bounded away from every subgroup/coset geometry.

Only if a genuine stability statement survives should the arithmetic step be attempted: pull the heavy set back through the exact source-character/conductor dictionary and test whether subgroup closure would force conductor reuse, source-prime incidence, or character coincidences incompatible with the endpoint hypotheses. A failure of that arithmetic incompatibility also kills the proposed escape.

## Evidence boundary

`MC-386` proves the energy floor and exhibits exact subgroup extremizers; it does **not** prove stability of near-extremizers and does not show that actual source characters cannot realize or approximate the extremal pattern. No arithmetic exclusion, stronger source-cost bound, Möbius estimate, or RH consequence is established here.
