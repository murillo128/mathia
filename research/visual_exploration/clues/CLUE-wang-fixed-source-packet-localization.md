---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-284-wang-fixed-source-packet-projection-bound.md
  - research/visual_exploration/findings/VIS-285-wang-q-zero-source-observable-analytic.md
  - research/visual_exploration/findings/VIS-286-wang-large-source-diagonal-linearizes.md
  - research/visual_exploration/findings/VIS-287-wang-fixed-power-source-escape-linear.md
  - research/visual_exploration/findings/VIS-288-wang-fixed-power-residual-h-frontier.md
  - research/visual_exploration/findings/VIS-289-wang-fixed-power-residual-o-h.md
  - research/visual_exploration/findings/VIS-290-wang-fixed-power-classical-pnt-envelope.md
  - research/visual_exploration/findings/VIS-291-wang-fixed-power-korobov-vinogradov-envelope.md
  - research/visual_exploration/findings/VIS-292-wang-symmetric-smoothing-green-resolvent.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md
  - research/visual_exploration/findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md
  - research/visual_exploration/findings/VIS-296-wang-relative-boundary-reduces-to-explicit-formula-remainder-mean.md
  - research/visual_exploration/findings/VIS-297-wang-boundary-remainder-mean-is-gamma-normalization.md
  - research/visual_exploration/findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-291` isolate Wang's source channel and show that fixed-interior packet localization does not create new information: the complete statistic on compact power panels reduces to the linear source law plus the classical Korobov--Vinogradov arithmetic envelope. `VIS-292` and `VIS-293` then rule out two cheap escapes: the symmetric smoother has no exact blind frequency, while excluding all poles of the squared-von-Mangoldt source transform in `Re(s)>1/2` is already RH-equivalent.

`VIS-294`--`VIS-297` progressively narrowed the apparent lower moving-source boundary. They separated absolute from relative resolution, isolated the finite relative crossover, and identified its remaining order-one mean as deterministic gamma normalization rather than new arithmetic.

`VIS-298` now closes the **entire moving lower-source branch at absolute `H` resolution** under Wang's fixed theorem ceiling. Recombining the exact Landau decomposition before applying norm bounds gives, for every `x=x(T)->infinity` with `x<=T^lambda` and fixed `lambda<theta`,

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`.

The earlier `x~sqrt(L)` boundary was therefore a Cauchy--Schwarz/error-packaging artifact: the coarse terms `H sqrt(L)/x` and `H L/x^2` are not load-bearing once the explicit gamma and absolutely convergent right-half-plane zeta pieces are estimated according to their actual frequency structure.

## Research question

Two genuinely distinct source routes remain.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`,

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **upper source ceiling**, can Wang's source-uniform theorem be sharpened so that the admissible exponent approaches `theta` with `T`, rather than remaining below one fixed `lambda<theta`? Any such claim must prove the needed uniformity instead of silently letting the theorem parameter drift.

A genuinely bounded source `x=O(1)` is not covered by `VIS-298`, but it is a different regime from the now-closed moving-source escape. It should be reopened only if it exposes information not already exhausted by the fixed-source findings `VIS-283`--`VIS-286`.

## Why it may matter

The lower-boundary thread no longer offers a cheap escape from the fixed-power negative controls. Neither `sqrt(log T)` nor `sqrt(log T/log log T)` marks a new moving arithmetic regime in the exact fixed-ceiling decomposition; all `x->infinity` are already resolved to `o(H)` after natural gamma recentering.

What remains is substantially sharper. A fixed-power advance must beat or structurally refine the genuinely arithmetic source envelope, while an upper-boundary advance must improve theorem uniformity itself. Either route would address information not removed by the normalization and frequency accounting already completed.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, gamma/zeta, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For a near-ceiling branch, derive source-uniform estimates with a quantitatively tracked dependence on the gap between the source exponent and `theta`. A family with `beta(T)->theta` is admissible only after proving that every implied constant and localization error remains controlled in that moving regime. Kill the route if it merely substitutes a drifting `lambda(T)` into a theorem whose constants were proved only for fixed `lambda<theta`.

Do not reopen a moving lower-source branch unless a new hypothesis invalidates the exact recombination of `VIS-298`; changing only the rate at which `x->infinity` is not such a hypothesis.

## Evidence boundary

`VIS-283`--`VIS-298` establish reductions, negative controls, exact decomposition identities, normalization corrections, and the closure of the fixed-ceiling moving lower-source branch. They do **not** improve the Korobov--Vinogradov arithmetic input, control a genuinely bounded source through the same `o(H)` formula, or justify a source ceiling approaching `theta`.

`VIS-298` also does not claim that Wang's theorem is optimal or that no other statistic can reveal lower-scale structure. It shows only that this particular moving-source route, for the complete Wang statistic under one fixed ceiling, has no unresolved absolute-`H` transition once its explicit pieces are recombined correctly.

## Research disposition

Outcome so far: **narrowed further**.

The moving lower-source branch is closed and should no longer consume research effort. The accepted clue remains live only for the fixed-power source-specific arithmetic question and the moving upper-ceiling uniformity question; bounded-source work is separate and needs an independently motivated residual target.