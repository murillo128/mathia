# MI-016 — Physical-scale localization still misses a moving multiplicative-rank interface

**Evidence level:** exact matched-control obstruction from [FD-136](../../findings/FD-136-logarithmically-scale-balanced-prime-ancestry-decay-still-does-not-recover-mobius.md), sharpened by the fixed-ratio shell theorem [FD-137](../../findings/FD-137-fixed-ratio-scale-localization-still-hides-a-maximal-central-rank-ancestry-wall.md), and bracketed by the exact-rigidity threshold [FD-135](../../findings/FD-135-local-ancestry-rigidity-has-an-exact-rough-core-threshold.md)

The natural multiplicative weight `1/n` removes a specific loophole in counting-measure ancestry averages: fixed-ratio physical scales receive comparable total weight. FD-136 shows that this still does not make approximate prime ancestry coercive. The common squarefree unit-sign witness keeps positive coefficient disagreement while every monitored prime sees vanishing harmonic mean defect because the bad edges occupy a shrinking window around the moving central `omega(n)` rank.

FD-137 removes the remaining physical-scale ambiguity. Restricting all parents to one shell `(T,2T]` still gives vanishing mean and harmonic ancestry defect, uniformly for a broad growing prime family satisfying

`1+log(1+log P(T)/log T)=o(sqrt(loglog T))`.

So the escape is not produced by averaging distant physical scales. Inside one fixed-ratio shell the bad edges are still trapped in an `o(sqrt(loglog T))` central-rank strip and therefore have vanishing marginal mass by squarefree Erdos--Kac.

The same finding also shows exactly what the old witness was hiding. On cofinal shells, conditioning on the exceptional rank exposes a maximal wall: every admissible edge in that rank cell has defect magnitude `2`, while the other ranks are exact. Thus genuine rank resolution kills this particular source even though any marginal physical-scale statistic misses it.

Together with FD-135, the source-law bracket is sharper. Scale-only localization is too weak; exact edgewise control becomes exact component rigidity; and the first useful intermediate law must preserve enough information about the active source coordinate before averaging. That coordinate need not always be `omega(n)`, as the next obstruction shows.

**Boundary.** FD-137 does not prove that exact rank conditioning is coercive for arbitrary sources, nor that a mesoscopic rank window suffices. It identifies the hidden coordinate of the FD-132--FD-137 witness and shows that physical-scale localization alone cannot expose it.