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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-286` isolate the fixed-source arithmetic profile, prove that bounded packet localization is only a bounded projection, and close both obvious endpoint singularities of the isolated diagonal profile. `VIS-287`--`VIS-291` then show that the **complete** Wang statistic on every pre-fixed compact power panel has the linear source law with a residual no larger than the standard Korobov--Vinogradov PNT envelope.

`VIS-292` rules out an exact blind-frequency explanation from Wang's symmetric smoothing: on logarithmic source scale the kernel is a Green resolvent with nonvanishing Fourier/Mellin multiplier. `VIS-293` then shows that the Dirichlet transform of the squared-von-Mangoldt source equals `(log zeta)''` plus a holomorphic remainder on `Re(s)>1/2`; excluding all its poles there is already RH-equivalent.

`VIS-294` narrows the lower moving-boundary escape. If `L=log T`, one fixed `lambda<theta` is retained, and

`x/sqrt(L) -> infinity`, `x<=T^lambda`,

then

`F_I(x)=(H/(2*pi))(L^2/x^2+log x)+o(H)`.

Thus `beta(T)=log x/L ->0` is not itself an uncontrolled regime. After retaining the explicit gamma term, the present theorem remains `o(H)`-accurate down to sources just above the `sqrt(log T)` scale. The first unresolved lower boundary at `H` resolution is therefore `x=O(sqrt(log T))`, not arbitrary vanishing `beta`.

## Research question

Two genuinely distinct routes remain.

First, at the lower source boundary `x=O(sqrt(log T))`, can the terms currently bounded by `H sqrt(L)/x` and `H L/x^2` be sharpened, recombined, or shown to have a structured limit after the exact gamma baseline is retained? Any surviving effect must be arithmetic rather than an artifact of the known two-term main profile.

Second, is there a real-axis property of the weighted source `mu=sum Lambda(n)^2/n delta_(log n)`, strictly weaker than RH-equivalent half-plane holomorphy, that beats the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

The upper source-ceiling branch is still separate because Wang fixes `lambda<theta`; nothing in the current findings permits `lambda` to drift toward `theta` with `T`.

## Why it may matter

The thread has removed most inexpensive escape routes: fixed-interior packet localization, endpoint singularities, compact fixed-power source escape, a generic PNT improvement, an exact smoothing null, an unpriced analytic-continuation argument, and now the broad class of lower moving exponents whose source still satisfies `x>>sqrt(log T)`.

What remains is substantially sharper. A lower-boundary result must address the actual theorem crossover where the present errors become `H`-scale, while a fixed-power result must expose genuinely source-specific real-axis arithmetic and state its analytic cost explicitly. Either outcome would distinguish new information from a repackaging of Wang's existing main terms and classical zeta input.

## Decisive test

For the lower-boundary branch, predeclare a source law with `x=O(sqrt(L))`, retain the exact `H L^2/(2*pi x^2)` gamma term, and rederive the load-bearing pieces of Wang's Proposition 2.6 rather than substituting a moving exponent into a compact-panel asymptotic. Identify separately the origins of `H sqrt(L)/x` and `H L/x^2`; prove a sharper bound, cancellation, or limiting profile before interpreting any residual. Kill the branch if the observed `H`-scale shape is forced by the explicit gamma term or by the existing error majorants.

For the fixed-power source branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information weaker than the RH-equivalent pole exclusion of `VIS-293`, and propagate it through every `D_x`, `B_x`, `E_x`, localization, and cross-term error. Kill the route if the gain is only another generic PNT substitution, high-frequency attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For a near-ceiling branch, keep Wang's theorem parameter fixed unless a new uniformity proof is supplied. A family with `beta(T)->theta` cannot be justified by silently letting `lambda` drift.

## Evidence boundary

`VIS-283`--`VIS-294` establish only negative controls, exact reductions, and regime extractions. They do not prove an `x=O(sqrt(L))` asymptotic, show that the square-root-log crossover is intrinsic rather than a limitation of Wang's present bounds, improve the Korobov--Vinogradov PNT scale, or give a theorem with a source ceiling approaching `theta`.

The clue therefore remains `accepted`: the broad source-localization idea has been heavily narrowed, but the actual lower theorem crossover, a source-specific weaker real-axis estimate, and the moving upper ceiling remain unresolved.

## Research disposition

Outcome so far: **narrowed**.

For the lower boundary, future work should begin at `x=O(sqrt(log T))`; sources with `x>>sqrt(log T)` are already controlled to `o(H)` after the explicit gamma term is retained. For the fixed-power branch, only a precisely priced source-specific real-axis improvement remains credible. Near the upper ceiling, a new theorem-uniformity argument is required.