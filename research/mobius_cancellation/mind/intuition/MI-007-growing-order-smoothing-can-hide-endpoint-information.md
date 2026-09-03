# MI-007 — Endpoint-vanishing smoothing has an explicit information-transport delay

**Evidence level:** supported by exact kernel bounds and inversion identities in MC-042--MC-046; the terminal-prime population uses the persisted short-interval prime input

## Core intuition

Changing the Riesz order with scale can manufacture smallness through normalization and can suppress current endpoint information even after that mass effect is removed. The newer result makes the second loss genuinely multiscale: the same fixed terminal-prime perturbation remains hidden throughout a long future window, and every endpoint-vanishing kernel has a calculable delay before the missing coefficients return at power scale.

Thus smoothing is not just a change of norm. It is an **information transport law in scale**. A smoothed estimate can support an ordinary-sum theorem only if the available future window reaches the kernel's visibility threshold or another localized/inverse mechanism supplies the missing endpoint data.

## Strongest justified principle

MC-042 closes every fixed Riesz order analytically: its Mellin multiplier is zero-free in the target half-plane, so the complete same-order transform carries the same reciprocal-zeta burden as ordinary Möbius cancellation.

MC-043 shows that growing order can cross square-root size through universal Gamma normalization even for bounded coefficients. MC-044 then shows that, after mass normalization, an order-`k` endpoint zero suppresses a terminal block by roughly `(L/X)^(k+1)` and moves fixed-strength visibility to later scales.

MC-045 supplies an exact-support multiplicative control. Flipping a terminal slab of primes changes the ordinary endpoint sum by `X^(alpha+o(1))`, with `17/30<alpha<3/4`, while fixed positive Riesz orders remain subcritical at the same cutoff.

MC-046 follows that **same fixed function** forward. For `Y=X+X^beta`, the order-`k` Riesz discrepancy has exponent `alpha+k beta-k` once the future shift dominates the slab width, so its square-root visibility threshold is

`beta_k^*=1-(alpha-1/2)/k`.

More uniformly, for every fixed `beta<14/15` one can choose the present short-interval-prime control so that all positive integer Riesz orders remain `o(X^1/2)` throughout `X<=Y<=X+X^beta`, while the ordinary discrepancy stays polynomially above square-root size. The numerical `14/15` is source-limited by the current prime interval theorem, not an intrinsic smoothing constant.

The exact differential inversion of a full same-order Riesz trajectory remains valid. What fails is the inference from a diagonal or too-short future window.

## What remains possible

A viable smoothing route may use translated/localized kernels with order-one endpoint weight, same-order future control beyond the visibility threshold, derivative data, or a source-specific Tauberian theorem that excludes the terminal-slab family. Strong power-aware pretentiousness from MC-047 is one example of additional information that detects this control, but it does not by itself supply Möbius cancellation.

## Status / novelty

Riesz summability, endpoint kernel estimates, differential inversion, and short-interval prime asymptotics are classical. The persisted synthesis is the scale-coherence boundary: **endpoint-vanishing smoothing delays arithmetic information, and multiscale usefulness is governed by a quantitative visibility horizon rather than by formal invertibility alone**.

## Falsification criterion

Derive ordinary square-root-scale cancellation from smoothed data restricted to a future window that still admits the MC-046 terminal-slab family with subcritical response, or exhibit a kernel satisfying the stated endpoint zero whose response violates the derived visibility law.

## Lean-formalizable core

- Growing-order normalization-vacuity bound.
- Endpoint block sensitivity.
- Exact future response of a terminal prime slab.
- Riesz visibility threshold `beta_k^*`.
- Same-order differential inversion versus diagonal-window insufficiency.
