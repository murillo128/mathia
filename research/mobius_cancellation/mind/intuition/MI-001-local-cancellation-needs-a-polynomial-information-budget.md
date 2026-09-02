# MI-001 — Local or qualitative cancellation needs a polynomial information budget to control a global square-root target

**Evidence level:** supported by MC-001, MC-004--MC-006, and current short-interval/correlation prior art

## Core intuition

Very strong local, almost-everywhere, or qualitative pseudorandomness can still be quantitatively too weak for a uniform global square-root target. What matters is not only that most local sums or every fixed correlation eventually cancels, but whether the retained data control coherent exceptional mass and anchored bias at a **polynomial rate**.

The new matched controls show that this is not merely a weakness of one short-interval theorem. Exact square-free support, full qualitative fixed-shift Chowla behavior, multiplicativity, or vanishing normalized mean can each coexist with global sums far above every fixed power saving when the quantitative coupling to the anchored sum is absent.

## Strongest justified principle

MC-001 proves the exact generic short-window transfer

`|T(X)| <= eta X + B + 2H`

from relative local size `eta`, exceptional measure `B`, and boundedness. Current almost-all Möbius short-interval inputs therefore yield only logarithmic global saving through this black-box channel; an RH-scale conclusion would require the combined error budget itself to be polynomially small or an additional signed mechanism that avoids the `L^1` loss.

MC-004 gives a stronger information control. There are deterministic `{-1,0,1}` sequences with exactly the Möbius square-free support and the full qualitative index-two Chowla property, yet with partial sums of order at least `X/log X` along an infinite subsequence. Qualitative fixed-shift cancellation is unchanged by a density-zero coherent overwrite and therefore has no uniform polynomial information budget by itself.

MC-005 restores multiplicativity while keeping exact square-free support and normalized mean zero. Explicit multiplicative controls have

`sum_{n<=x} a_q(n) ~ C_q x/(log x)^(2/(q-1))`,

so multiplicativity plus one-point qualitative cancellation still permits arbitrarily slow logarithmic decay. The missing quantitative datum is localized at the prime-value distribution rather than at support or multiplicative consistency alone.

MC-006 makes the correlation rate explicit. Van der Corput gives

`|S(X)|/X << H^(-1/2) + R(X,H)^(1/2)`

for the averaged absolute two-point correlation budget `R`. A fixed power saving requires polynomially long shift range and polynomially small averaged correlation. The current averaged Chowla theorem supplies only logarithmic decay, so its black-box consequence is only logarithmic and is weaker than the classical unconditional Mertens bound.

## What remains possible

A useful advance must retain a datum that couples local or correlation information to the anchored sum at polynomial strength: signed overlap between windows, multiplicative prime-local constraints, multiscale compatibility of exceptional sets, bilinear/Type-I-II structure, or higher correlations with a quantitative range uniform enough to survive the transfer.

The decisive object is a transfer inequality, not a randomness analogy. Full qualitative Chowla, exact support, or multiplicativity can remain important ingredients, but they count only when combined with a theorem that rules out the matched coherent controls at the required scale.

## Status / novelty

The moving-window and van-der-Corput inequalities, Chowla framework, square-free support, and Selberg--Delange mechanisms are classical. The persisted Mathia synthesis is the quantitative information-budget gate: a statistic becomes RH-relevant only when it controls the anchored sum at polynomial strength or carries enough additional structure to beat the generic absolute-loss transfer.

## Falsification criterion

Give a source-faithful local/correlation statistic claimed to beat the gate and construct compatible sequences with near-linear partial sums, or prove a transfer inequality with a strict polynomial gain after all exceptional-set, correlation-range, and endpoint losses are included.
