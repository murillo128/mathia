# MI-012 — Hamming regularization is degree-two damping before the square-root transition

**Evidence level:** exact source-level results through MC-101

## Core intuition

The source-forced Hamming deformation does become smaller as the prime-sign bias approaches zero, but throughout the broad mesoscopic regime that gain is completely explained by damping one positive degree-two shell. It is not evidence that the Möbius cancellation has become easier. The hard endpoint is small for the opposite reason: large radial degrees cancel with signs, and the path is forced to develop large negative curvature before reaching it.

## Strongest justified principle

MC-099 proves that the curvature starts positive at almost-square scale and must reverse with a comparably large negative contribution, so convexity or positive degreewise energy cannot carry the endpoint cancellation. MC-100 finds a deterministic almost-square spike at logarithmically small bias and shows that every fixed positive-length bias interval or stable fixed-geometry sample family already contains almost-square amplitude.

MC-101 gives the exact moving-scale profile. Whenever the bias is inside the degree-two-dominance window, in particular `t=N^{-alpha}` for every fixed `0<alpha<1/2`, the whole interval from zero to that bias has maximum size asymptotic to the positive degree-two term. The exponent drops continuously from two toward one only because of the explicit factor `t^2`. At the square-root boundary the diagonal scale becomes competitive and this mechanism stops deciding the source.

## What remains possible

The square-root transition and smaller biases remain open, as do signed recurrences that compare large values without taking absolute norms. A moving geometry can still be useful if its reconstruction cost is quantitatively below the exact damping gain. Different deformations may also alter the positive degree-two source term or the cubic tail and require a fresh analysis.

## Status / novelty

The Huxley--Watt source identity, polynomial interpolation, and biased multiplicative-function language are classical or previously persisted. The durable synthesis is: **before the square-root transition, shrinking-bias regularization is fully accounted for by positive degree-two damping, whereas the endpoint phenomenon is genuinely signed cross-degree cancellation**.

## Falsification criterion

Find an admissible mesoscopic bias satisfying MC-101's hypotheses where the degree-two asymptotic fails, invalidate the pair-level cubic tail or degree-two main term, or derive a strict-power fixed-interval bound contradicting MC-100's deterministic lower bound.
