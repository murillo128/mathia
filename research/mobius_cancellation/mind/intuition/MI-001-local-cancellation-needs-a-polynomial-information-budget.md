# MI-001 — Local cancellation needs a polynomial information budget to control a global square-root target

**Evidence level:** supported by MC-001 and current short-interval prior art

## Core intuition

Very strong local or almost-everywhere cancellation can still be quantitatively too weak for a uniform global square-root target. What matters is not only that most short sums are small, but whether the retained local data control the total coherent exceptional mass and preserve enough signed dependence between windows to avoid an `L^1` triangle-inequality loss.

## Strongest justified principle

MC-001 proves the exact generic transfer

`|T(X)| <= eta X + B + 2H`

from a relative short-window bound `eta`, exceptional-set measure `B`, and boundedness. Applied to the current almost-all Möbius short-interval theorem, this black-box route yields only logarithmic global saving, even though the local theorem is qualitatively strong. To certify `X^(1/2+delta)` from this information alone, the combined error budget itself must already be polynomially that small.

The obstruction is an information statement, not a theorem that short-interval methods cannot help. The missing information may be signed overlap, multiplicative organization, multiscale coherence, or a proof-level structure that makes exceptional windows cancel rather than accumulate absolutely.

## What remains possible

A useful advance should isolate one extra source-faithful statistic beyond `(eta,B,H)` and prove that it lowers the global transfer cost by a polynomial factor. Bilinear decompositions, scale-coupling inequalities, or restrictions on coherent exceptional sets are plausible categories; their value depends on an explicit transfer theorem, not on a randomness analogy.

## Status / novelty

The moving-window averaging identity is elementary and the short-interval inputs are prior art. The durable synthesis is the quantitative information-budget gate: local pseudorandomness becomes RH-relevant only when the retained data are strong enough to control the global exceptional mass or to cancel it coherently.

## Falsification criterion

Give a source-faithful local statistic claimed to beat MC-001 and construct compatible sequences with large global partial sums, or prove a transfer inequality with a strict polynomial gain after all exceptional and endpoint errors are included.
