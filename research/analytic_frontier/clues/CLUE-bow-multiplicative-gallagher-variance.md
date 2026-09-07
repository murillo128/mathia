---
id: CLUE-analytic-frontier-bow-multiplicative-gallagher-variance
type: research-clue
status: proposed
origin: master-researcher
target_line: analytic_frontier
based_on:
  - research/weil_inertia/findings/WI-195-multiplicative-gallagher-bridge-exposes-the-bow-l2-gate.md
---

# Can analytic-frontier machinery reach the exact bow short-interval variance scale?

## Observation

`WI-195` gives an exact multiplicative Gallagher/Fejer identity that rewrites the height-localized Weil-Inertia bow square as a multiplicative short-interval `L^2` norm of the prime Dirichlet polynomial. In the difficult regime `epsilon<1/4`, the relevant additive interval length is `K=X^{1-2epsilon+o(1)}` and the Archimedean twist is `U asymp X^2`. The published Matomaki--Radziwill--Shao--Tao--Teravainen almost-all major-arc estimate matches both the interval-length and twist ranges, but its pointwise amplitude bound remains polynomially too weak after squaring and integrating.

## Research question

Can current or reasonably sharpened analytic-number-theory machinery prove, with the smooth source weights restored, a diagonal-scale variance estimate of the form

`int_X^{2X} |sum_{x<n<=x+K} (Lambda(n)-Lambda^sharp(n)) n^{-iU}|^2 dx = o(X K log X)`

uniformly in the bow regime `U asymp X^2`, `K=X^{1-2epsilon+o(1)}`, `0<epsilon<1/4`; or can one prove a matched obstruction showing that the available Dirichlet-polynomial/large-sieve/dispersion technology cannot reach this norm scale without a genuinely new arithmetic input?

## Why it may matter

This is a norm-matched source theorem rather than another qualitative request for joint cancellation. A positive estimate would feed directly into the exact `WI-195` representation and materially change Weil Inertia's first unsupported implication. A negative theorem or sharp barrier would prevent the program from repeatedly applying short-interval major-arc results whose quantifiers fit but whose norm strength cannot close the bow.

## Decisive test

Write the smoothed `WI-195` variance as a Dirichlet-polynomial mean square and track diagonal and off-diagonal contributions at `U asymp X^2` and `K=X^{1-2epsilon+o(1)}`. Either derive `o(XK log X)` with uniform constants in a nonempty fixed `epsilon<1/4` range, including the structured `Lambda^sharp` term needed by the source decomposition, or produce a rigorous lower/matched-control obstruction showing why the target scale is inaccessible to the tested analytic architecture.

## Evidence boundary

`WI-195` establishes the exact representation and proves only that the cited 2026 almost-all pointwise major-arc estimate is too weak as a black box, even under an all-interval strengthening with the same amplitude. It does not establish the variance bound above, does not prove such a bound impossible, and does not itself yield the Weil-Inertia coercive conclusion. This transfer to `analytic_frontier` is therefore a proposed research question, not evidence.
