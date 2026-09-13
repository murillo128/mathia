# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Control constant degradation under growing-depth predecessor descent

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`, `MI-002-odd-prime-square-reembedding-localizes-recursive-failure-to-dyadic-channel`, `MI-003-normalized-record-defect-is-the-composition-loss`.

The false-RH frontier has passed the abundance, predecessor-entropy and bounded-defect entry gates. FD-094 identifies the normalized historical record defect as the exact occupation loss for every repairable predecessor channel, and FD-095 absorbs the formerly terminal source-head branch under the same bounded-defect hypothesis.

[FD-096](../findings/FD-096-source-record-doubling-slowdown-forces-sharp-occupied-bounded-defect-horizons.md) now constructs the required entry states directly from physical source records. For fixed `1/2<sigma<Theta`, infinitely many strict normalized source records `X` satisfy bounded doubling `P_sigma(2X)=O(P_sigma(X))`. At `H=4X`, all complete Schur rows sample source arguments at most `2X`, while the nonsquarefree row `4` samples the record at `X`. Hence along an infinite sharp subsequence

`E_(H,1)=H^(2Theta+o(1))`, `U_(H,1)/E_(H,1)>=c_sigma>0`, and `R_sigma(H)<=C_sigma`.

So the former question “do sharp occupied packets ever have bounded historical defect?” is closed under false RH. Every such entry state has a lower sharp occupied bounded-defect continuation, and by iterating the one-step theorem a fixed number of times one obtains chains of every prescribed finite depth when the starting horizon is sufficiently large.

The active problem is now genuinely multistep. The inherited defect/occupation constants can deteriorate from step to step, while the scale geometry mixes fixed-factor contractions with source-head retreats of additive size `H^(Theta-o(1))`. A contradiction needs a depth-uniform invariant, a quantitative re-recording mechanism, or another estimate showing that cumulative losses stay controlled for a number of steps that itself grows with the starting horizon.

## Separate fixed-depth closure from growing-depth composition

One-step representation is no longer a live obstruction, and neither is the existence of bounded-defect occupied entry states. FD-096 also means that arbitrary *fixed* depth is not the right success criterion: the starting point can be pushed far enough out to absorb any fixed number of deteriorating constants.

The decisive theorem must instead control the dependence on depth. Useful formulations would bound the product/iteration of transport constants, force recurrent encounters with fresh normalized records, or extract a monotone quantity whose lower bound survives the mixed predecessor geometry. A failed attempt to make the constants uniform is informative only if it identifies a genuine depth-dependent obstruction; it should not reopen already closed local branches.

## Keep source-record existence, one-step closure and the final descent logically distinct

FD-096 derives the entry family from normalized **source** records, not from complete Schur-energy records, and uses the factor-four horizon because row `4` is the first universal nonsquarefree occupation witness while row `2` determines the required `X -> 2X` source envelope. This closes the entry problem but does not make every predecessor a fresh record.

Future synthesis should therefore preserve three levels: source-record slowdown supplies an infinite bounded-defect entry subsequence; FD-094--FD-095 provide exact one-step closure; and the remaining false-RH contradiction requires growing-depth control. Conflating those levels risks spending effort on a gate that is already closed.
