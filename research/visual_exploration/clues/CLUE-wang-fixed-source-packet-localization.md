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
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-291` isolate Wang's source channel and show that fixed-interior packet localization does not create new information: the complete statistic on compact power panels reduces to the linear source law plus the classical Korobov--Vinogradov arithmetic envelope. `VIS-292` and `VIS-293` then rule out two cheap escapes: the symmetric smoother has no exact blind frequency, while excluding all poles of the squared-von-Mangoldt source transform in `Re(s)>1/2` is already RH-equivalent.

The lower moving-source branch has now been narrowed further. `VIS-294` identifies `x=O(sqrt(L))`, `L=log T`, as the first unresolved scale at **absolute `H` resolution** after retaining the explicit gamma contribution. `VIS-295` shows that the gamma-subtracted residual nevertheless keeps its relative linear law throughout `x^2 log x >> L`, so merely going below `sqrt(L)` does not create a new relative source regime.

`VIS-296` isolates the finite relative boundary `x^2 log x/L -> kappa` to one order-one quantity, the interval mean `Q_E` of Wang's explicit-formula remainder. `VIS-297` resolves that mean:

`Re Q_E -> -log(2*pi)`.

The surviving constant comes from the classical gamma factor hidden by Wang's coarse baseline `log(t+2)/x`; the absolutely convergent right-half-plane zeta term has zero interval mean and the pole/trivial-zero terms vanish. Thus the finite relative crossover is a deterministic normalization effect, not evidence for new arithmetic source information.

## Research question

Three genuinely distinct routes remain.

At the **absolute lower boundary** `x=O(sqrt(L))`, after replacing the coarse gamma baseline by its natural gamma normalization, can the terms presently controlled only at `H` scale be sharpened, recombined, or given a structured limit? A surviving term must not be the deterministic `-log(2*pi)` correction already closed by `VIS-297`.

For the **fixed-power real-axis source**, is there a property of `mu=sum Lambda(n)^2/n delta_(log n)`, strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

The **upper source ceiling** remains separate because Wang fixes `lambda<theta`; none of the present findings permits `lambda` to drift toward `theta` with `T`.

## Why it may matter

The inexpensive lower-boundary interpretations have now been removed at two resolutions. At relative resolution, both the broad regime `x^2 log x >> L` and the finite `x^2 log x/L` crossover are accounted for by Wang's existing diagonal structure plus deterministic gamma normalization. A genuinely new lower-source effect must therefore appear in the harder absolute-`H` accounting, not in the already-resolved mean normalization.

That leaves a sharper test of whether Wang's machinery contains source information not already explained by classical zeta input. Success would require either a new absolute-boundary mechanism, a source-specific real-axis arithmetic estimate with explicitly weaker analytic cost than RH, or a new theorem-uniformity argument near the upper ceiling.

## Decisive test

For the lower-boundary branch, predeclare `x=O(sqrt(L))` and rederive the load-bearing pieces of Wang's Proposition 2.6 using the refined gamma normalization exposed by `VIS-297`, rather than subtracting only `H L^2/(2*pi x^2)` and interpreting the leftover constant. Track separately the origins of the `H sqrt(L)/x`, `H L/x^2`, and any cross terms after the gamma correction. Prove a sharper bound, cancellation, or limiting profile before calling any residual arithmetic. Kill the branch if the apparent `H`-scale structure is forced by the refined gamma baseline or by existing deterministic explicit-formula terms.

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, `B_x`, `E_x`, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For a near-ceiling branch, keep Wang's theorem parameter fixed unless a new uniformity proof is supplied. A family with `beta(T)->theta` cannot be justified by silently allowing `lambda` to drift.

## Evidence boundary

`VIS-283`--`VIS-297` establish reductions, regime extractions, negative controls, and the deterministic identity of the finite relative-boundary remainder mean. They do **not** prove an absolute-`H` asymptotic at `x=O(sqrt(L))`, show that the square-root-log crossover is intrinsic rather than a limitation of the current theorem, improve the Korobov--Vinogradov arithmetic scale, or give a source ceiling approaching `theta`.

In particular, `VIS-297` closes only the order-one mean isolated by `VIS-296`. It does not show that every component of Wang's absolute error budget near `sqrt(L)` is deterministic or negligible.

## Research disposition

Outcome so far: **narrowed further**.

The finite relative crossover is closed as gamma normalization and should no longer be treated as a candidate arithmetic signal. The active lower branch begins at the absolute `H`-resolution boundary near `x=O(sqrt(log T))`, now with the refined gamma baseline explicitly accounted for. The fixed-power real-axis source question and the moving upper ceiling remain independently unresolved.