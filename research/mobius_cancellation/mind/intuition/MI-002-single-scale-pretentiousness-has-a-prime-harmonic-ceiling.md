# MI-002 — Prime-power pretentious enrichment reaches the square-root boundary but does not by itself cross it

**Evidence level:** supported by MC-002--MC-003 and classical Halasz/pretentious and square-convolution theory

## Core intuition

The standard prime-only pretentious scalar is too small to support a polynomial cancellation theorem, but merely adding prime-power sensitivity is not automatically enough. For the canonical Möbius/Liouville comparison the first new information appears at prime squares, and both the exact convolution kernel and the power-cancellation-aware pretentious metrics acquire their sharp convergence threshold at `1/2`.

Thus prime-power enrichment repairs a genuine information loss — it distinguishes functions that agree at every prime — while still behaving mainly as a **transfer device above the square-root boundary**, not as an unconditional generator of square-root cancellation.

## Strongest justified principle

MC-002 shows that the standard Halasz parameter has only `O(log log x)` total prime-harmonic mass. A generic exponential mean-value bound would need order `log x` information for any fixed power saving. Optimizing the same prime-only scalar cannot bridge that scale mismatch.

MC-003 audits the natural enrichment suggested by Jung--Lemke Oliver. Möbius and Liouville agree at every prime but differ from the `p^2` layer onward. Their exact square-divisor identities give

`L(x)=sum_{d<=sqrt(x)} M(x/d^2)`

and the inverse formula with `mu(d)`. Absolute transfer preserves an exponent `alpha` exactly for `alpha>1/2`, loses a logarithm at `alpha=1/2`, and saturates at square-root size below it. The strengthened prime-power pretentious quantities have precisely the same threshold: their local difference begins at `p^2`, so the relevant Euler mass converges iff `beta>1/2`.

The previously proposed power-cancellation-aware clue is therefore resolved in its Möbius/Liouville form. The enrichment is mathematically real, but the strongest unconditional Liouville input is still `x^(1-o(1))`; no fixed subunit exponent is available to bootstrap into a new Möbius bound. Reapplying the same bridge cannot create the missing cancellation.

## What remains possible

Prime-power-sensitive data may still matter with a different comparator, a signed transfer that does not take absolute values, or a multiscale mechanism coupling several Euler layers. But a viable route must show a non-circular quantitative estimate that is genuinely easier than the Möbius target.

The next comparator audit should distinguish two questions: whether the arithmetic transfer factor carries new information, and whether the available analytic control of that factor can transmit an independently proved bound without masking the critical strip. MC-007--MC-008 motivate that sharper distinction.

## Status / novelty

The Halasz scale, square-divisor identities, and Jung--Lemke Oliver framework are classical. The durable synthesis is the exact alignment between the first missing prime-power layer and the square-root convergence threshold: **prime-power fidelity is necessary to distinguish Möbius from Liouville, but that fidelity alone does not supply a below-threshold cancellation mechanism**.

## Falsification criterion

Produce a prime-power-aware transfer theorem whose hypotheses can be verified unconditionally for Möbius and an independently controlled comparator and that yields a fixed power saving unavailable from the square-convolution threshold, without assuming an equally strong cancellation estimate in another guise.
