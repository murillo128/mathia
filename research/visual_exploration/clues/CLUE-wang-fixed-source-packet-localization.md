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
  - research/visual_exploration/findings/VIS-299-wang-pointwise-moving-ceiling-h-over-log-cubed.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-291` isolate Wang's source channel and show that fixed-interior packet localization does not create new information: the complete statistic on compact power panels reduces to the linear source law plus the classical Korobov--Vinogradov arithmetic envelope. `VIS-292` and `VIS-293` then rule out two cheap escapes: the symmetric smoother has no exact blind frequency, while excluding all poles of the squared-von-Mangoldt source transform in `Re(s)>1/2` is already RH-equivalent.

`VIS-294`--`VIS-298` close the apparent moving lower-source boundary. Exact gamma recentering removes the square-root-log `H` barrier and yields

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`

for every moving `x->infinity` below one fixed exponent ceiling.

`VIS-299` now removes that fixed exponent gap as a **pointwise** obstruction. Re-running Wang's localization proof rather than substituting a moving theorem parameter shows that the same asymptotic holds whenever

`x L^3 / H -> 0`.

Equivalently, for `x=T^beta(T)`,

`(theta-beta(T))L - 3 log L -> +infinity`.

Thus `beta(T)` may approach `theta`; the first unresolved upper layer in the current proof is where the explicit localization remainder `O(xL^3)` itself reaches `H` scale, around `x asymp H/L^3`.

## Research question

Two genuinely distinct source routes remain.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`,

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **upper localization layer**, can the comparison

`2*pi F_I(x) = integral_I |A(x,t)|^2 dt + O(xL^3)`

be sharpened, recombined, or given a structured leading correction when `xL^3/H` is no longer negligible, especially near `x asymp H/L^3`? The question is now about interval-localization tails, not merely about allowing a fixed `lambda` to drift.

A genuinely bounded source `x=O(1)` remains separate. A moving-support version of Wang's integrated Theorem 2.2 is also separate: `VIS-299` controls the pointwise source statistic and does not establish uniformity for a test function whose support changes with `T`.

## Why it may matter

The source-scale search space has been compressed substantially. Neither the moving lower boundary nor a fixed exponent gap below `theta` is a live pointwise obstruction. Any upper-source signal within Wang's present framework must now enter through the localization layer where the full-zero statistic is replaced by the interval-restricted explicit-formula energy, or through arithmetic information stronger than the generic PNT envelope.

This distinction prevents theorem-parameter bookkeeping from masquerading as mathematical structure. It also gives a concrete scale at which a further argument could matter: a gain over `O(xL^3)` would immediately enlarge the pointwise source window beyond `o(H/L^3)`.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, gamma/zeta, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the upper branch, return to the proof of Wang's Lemma 2.4 and isolate the actual contribution of zeros outside `I` to `A-A_I` and to the energy difference. Test whether the `O(xL^3)` bound is saturated by an admissible configuration, whether its endpoint pieces admit cancellation or a deterministic correction, or whether a sharper dependence on `x,H,L` follows from the zero geometry already available. A valid advance must work directly in the moving range; do not infer it by inserting `lambda(T)` into a fixed-parameter theorem.

Kill the upper route if the only improvement is available after assuming the desired pair-correlation or zero-distribution conclusion, or if the `H/L^3` layer is recreated by a matched admissible control with no arithmetic-specific content.

Do not reopen a moving lower-source branch unless a new hypothesis invalidates the exact recombination of `VIS-298`; changing only the rate at which `x->infinity` is not such a hypothesis.

## Evidence boundary

`VIS-283`--`VIS-299` establish reductions, negative controls, exact decomposition identities, normalization corrections, closure of the moving lower-source branch, and extension of the **pointwise** source asymptotic through every `x=o(H/L^3)`. They do **not** improve the Korobov--Vinogradov arithmetic input, control a genuinely bounded source by the same formula, evaluate the localization boundary `x asymp H/L^3`, or prove a moving-support version of Wang's integrated pair-correlation theorem.

In particular, `VIS-299` identifies the first unresolved scale of the current localization proof; it does not prove that `H/L^3` is an intrinsic barrier of `F_I`.

## Research disposition

Outcome so far: **narrowed further**.

The moving lower-source branch remains closed. The pointwise upper-ceiling branch is now reduced from a fixed exponent gap to the explicit `xL^3/H` localization layer. The accepted clue remains live for that localization question and for the separate fixed-power source-specific arithmetic question; bounded-source and moving-test-function questions require independently justified targets.