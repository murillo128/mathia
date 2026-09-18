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
  - research/visual_exploration/findings/VIS-300-wang-localization-cross-coherence.md
  - research/visual_exploration/findings/VIS-301-wang-zero-free-localization-log-squared-window.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

`VIS-283`--`VIS-291` isolate Wang's source channel and show that fixed-interior packet localization does not create new information: the complete statistic on compact power panels reduces to the linear source law plus the classical Korobov--Vinogradov arithmetic envelope. `VIS-292` and `VIS-293` then rule out two cheap escapes: the symmetric smoother has no exact blind frequency, while excluding all poles of the squared-von-Mangoldt source transform in `Re(s)>1/2` is already RH-equivalent.

`VIS-294`--`VIS-298` close the apparent moving lower-source boundary. Exact gamma recentering removes the square-root-log `H` barrier and yields

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`

for every moving `x->infinity` below one fixed exponent ceiling.

`VIS-299` then removes the fixed exponent gap as a pointwise obstruction, extending the same asymptotic through `x=o(H/L^3)`. `VIS-300` decomposes the first apparent upper boundary and shows that the two pure localization leakage energies are already `o(H)` there; the only remaining `H`-scale term was the inside--outside coherence

`C_I(x)=Re integral_I A_I(x,t) overline(A(x,t)-A_I(x,t)) dt`.

`VIS-301` now removes that `H/L^3` localization boundary as well. Retaining the classical Vinogradov--Korobov zero-free-region bound on the real parts of the zeros inserts a factor

`q_T(x)=x^(-eta_T)`,

with `eta_T asymp L^(-2/3)(log L)^(-1/3)`, into the near-height pieces of both `A_I` and `A-A_I`. For sources near the old upper layer this factor is super-polynomially small in `L`. Re-running Wang's localization proof with that information gives

`C_I(x)=o(H)`

and the same pointwise pair-correlation asymptotic throughout

`x=o(H/L^2)`.

The next generic `H`-scale term is therefore not localization at all. It is the `O(x log^2(2x))` Montgomery--Vaughan mean-value error for Wang's Dirichlet polynomial, which reaches output scale at `x asymp H/L^2`.

## Research question

Two distinct source routes remain.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`,

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293`, that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can the exact coefficient structure of Wang's Dirichlet polynomial improve, evaluate, or prove sharp the mean-value remainder

`O(sum n a_n^2) = O(x log^2(2x))`

when `x asymp H/L^2`? In particular, is there cancellation in the off-diagonal time integral that is invisible to the generic Montgomery--Vaughan bound, or can an admissible coefficient/control model show that an `H`-scale remainder genuinely survives?

A genuinely bounded source `x=O(1)` remains separate. A moving-support version of Wang's integrated Theorem 2.2 is also separate: the current findings concern the pointwise source statistic and do not establish uniformity for a test function whose support changes with `T`.

## Why it may matter

The source-scale search space is now considerably cleaner. The moving lower boundary, the fixed exponent gap, and the apparent `H/L^3` localization wall have all collapsed under exact recombination, proof-level uniformity, or classical zero-free information. Continuing to optimize localization tails would attack a term that is already below the requested `H` resolution in the full range where the current interior mean-value argument remains asymptotic.

The next positive result must therefore act on a different information channel. A gain over the `x log^2 x` interior mean-value error would genuinely enlarge the pointwise source window; a sharpness mechanism would instead certify that the current proof has reached a real Dirichlet-polynomial barrier rather than another packaging artifact.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all `D_x`, gamma/zeta, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work directly with Wang's exact coefficients

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`

and the interval integral of `D_x`. Determine whether the generic mean-value remainder `O(sum n a_n^2)` can be replaced near `x asymp H/L^2` by an `o(H)` term, an explicit lower-order correction, or a matching lower/control construction. Preserve the actual coefficient frequencies and interval length; do not infer a gain by assuming the pair-correlation or prime-variance conclusion that the statistic is meant to test.

A decisive outcome is one of: an unconditional coefficient-specific cancellation giving `o(H)` at the `L^-2` boundary; a stable deterministic `H`-scale correction that can be separated from the main source law; or a matched admissible model showing that the generic `xL^2` scale is genuinely attainable and additional arithmetic input is necessary.

Do not reopen the `H/L^3` localization branch unless a new hypothesis invalidates the zero-free suppression used in `VIS-301`. Improving the `L^2` leakage masses or re-estimating `C_I` without changing that input is no longer a live upper-boundary test.

## Evidence boundary

`VIS-283`--`VIS-300` establish the source reductions, normalization corrections, lower-source closure, pointwise moving-source extension, and exact localization-energy decomposition. `VIS-301` additionally establishes, using the unconditional classical zero-free region, that the complete localization error is `o(H)` for every moving source with `x=o(H/L^2)`.

None of these findings improves the coefficient-specific mean-value error at `x asymp H/L^2`, improves the fixed-power Korobov--Vinogradov source envelope, controls a genuinely bounded source by the same formula, or proves a moving-support version of Wang's integrated pair-correlation theorem. In particular, `H/L^2` is currently a **proof boundary produced by the interior Dirichlet-polynomial estimate**, not an established transition of `F_I`.

## Research disposition

Outcome so far: **upper pointwise branch narrowed from localization coherence to the interior `x log^2 x` mean-value horizon**.

The moving lower-source and `H/L^3` localization branches are closed under the current hypotheses. The accepted clue remains live for the coefficient-specific `H/L^2` question and for the separate fixed-power source-specific arithmetic question; bounded-source and moving-test-function questions still require independently justified targets.