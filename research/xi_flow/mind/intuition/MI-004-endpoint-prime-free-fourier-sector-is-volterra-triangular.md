# MI-004 — Endpoint prime-free Fourier transport is Volterra-triangular and the matched memory selector stays empty at fixed heat time

**Evidence level:** supported through XF-054 by the explicit endpoint normal form, convolution-ideal heat jets, and the moving-high-line uniform matched-statistic estimate

## Core intuition

The positive-frequency Xi carrier has a genuine source-selected endpoint gap, and its one-sided heat evolution cannot import higher-frequency prime data downward by finite-order Volterra transport. More strongly, for the actual moving memory-band statistic, the apparent infinite-order endpoint escape can be suppressed uniformly over every fixed heat interval by evaluating the same height-independent carrier on a source-compatible high line.

The endpoint problem is therefore no longer an uncontrolled singular transport problem. The prime-free selector survives the exact matched statistic; the remaining bridge is to turn that source exclusion into transition-side signed coercivity.

## Strongest justified principle

XF-048--XF-051 establish the structural carrier. Below the first prime frequency `lambda_2=log 2/2` the endpoint selector can be made exactly prime-free; finite one-sided transport survives complex roots and collisions; and the infinite horizontal logarithmic derivative gives a canonical positive-frequency distribution with exact Burgers/Volterra evolution.

XF-052 makes the endpoint datum explicit. On `0<xi<lambda_2`, the carrier equals the deterministic background

`B(xi)=e^xi+e^-xi-e^-xi/(1-e^-4xi)`,

with singular normal form `-1/(4 xi)+7/4+O(xi)`. Arithmetic atoms begin only at `lambda_2`.

XF-053 shows that the high-frequency arithmetic sector is a convolution ideal for the one-sided Burgers vector field. Every finite heat-time jet below `lambda_2` is therefore determined entirely by the background, and every fixed Taylor polynomial has `o(1)` pairing with the shrinking XF-050 memory probe. Any order-one replenishment would have to be genuinely nonperturbative in the moving endpoint limit.

XF-054 closes that escape at the statistic level. Because the carrier is independent of the auxiliary zero-free height, choose `a_T=A log T`. Reflection moves the logarithmic derivative into a right half-plane where the Euler product makes the arithmetic factor polynomially small uniformly for `0<=t<=t_0`; the deterministic gamma/polar heat background varies only on the physical `T` scale and is killed by the probe's `W omega~log^2 T` oscillation. Hence

`sup_{0<=t<=t_0} |S_T(t)| = o(1)`

for every fixed `t_0`, without RH or real-root assumptions.

## What remains possible

XF-054 does not give a pointwise endpoint regularity theorem and does not itself bound the de Bruijn--Newman constant. It proves exactly the non-escape property needed for the compact matched memory statistic. The live problem is now downstream: connect this uniform source selector to the Cauchy/flux rigidity developed near transition and derive the signed tapered estimate required by the zero-side coercive argument.

A new endpoint observable is justified only if that source-to-transition bridge provably loses the selector. Reopening complex-root, collision, finite-jet, or raw infinite-sum objections would duplicate closed structural questions.

## Status / novelty

The explicit formula, Mellin/Fourier transforms of gamma factors, one-sided convolution support, heat equation, Euler product, Stirling estimates, and integration by parts are classical. The persisted Xi-flow synthesis is the exact source-transport statement: **the prime-free endpoint quotient is triangular to all finite heat orders, and the actual shrinking memory statistic remains uniformly source-empty over fixed heat time after a height-independent high-line comparison**.

## Falsification criterion

Exhibit a prime-power contribution to the carrier below `lambda_2`, a finite heat jet that imports high-frequency arithmetic mass into that band, or a fixed heat interval and matched XF-050 probe for which the moving-high-line estimate fails to make `S_T(t)=o(1)`.

## Lean-formalizable core

- Support-ideal preservation for one-sided convolution and the finite jet recurrence.
- Algebraic separation of the explicit prime-free endpoint background from the first arithmetic atom.
- Finite-dimensional/analytic lemmas underlying the matched-statistic height-independence reduction.
