# MI-016 — Harmonic scale balancing still misses the moving multiplicative-rank interface

**Evidence level:** exact matched-control obstruction from [FD-136](../../findings/FD-136-logarithmically-scale-balanced-prime-ancestry-decay-still-does-not-recover-mobius.md), sharpening the mean-ancestry escapes in `FD-130`--`FD-134` and complementing the exact-rigidity threshold in [FD-135](../../findings/FD-135-local-ancestry-rigidity-has-an-exact-rough-core-threshold.md)

The natural multiplicative weight `1/n` removes a specific loophole in counting-measure ancestry averages: every fixed-ratio parent scale now contributes comparable total mass. It still does not make approximate prime ancestry coercive.

For the squarefree unit-sign witness `a^(K)` of FD-132--FD-134, define the primewise harmonic defect

`L_(p,r,H)(a)= [sum_(n<=H/p, squarefree, p∤n) |a_(pn)+a_n|^r/n] / [sum_(n<=H/p, squarefree, p∤n) 1/n]`.

Under the same almost-full active-prime regime `p<=P(H)` with `Y=H/P -> infinity` and

`1+log(log H/log Y)=o(sqrt(log log Y))`, 

FD-136 proves, for every fixed finite `r>=1`,

`sup_(p<=P(H)) L_(p,r,H)(a^(K)) -> 0`,

while the same `1/n` metric still sees a fixed amount of coefficient error:

`[sum_(n<=H)|a_n^(K)-mu(n)|^r/n] / [sum_(n<=H)1/n] -> 2^(r-1)/zeta(2)`.

Equivalently, the disagreement set has logarithmic density `1/(2 zeta(2))=3/pi^2`.

The failure is therefore not physical-scale dilution. On essentially every multiplicative shell the ancestry defects occupy a shrinking window around the moving central `omega(n)` rank, so each shell is individually sparse in the coordinate that matters; harmonic averaging then adds many sparse shells. **Balancing `log n` does not balance multiplicative rank.**

Together with FD-135 this brackets the missing source law more tightly. Scale-only averaging remains too weak, while edgewise `L^infinity` becomes exact ancestry and can reconstruct the whole source once the rough-core threshold is crossed. Any intermediate coercive law must retain nonvanishing resolution in the moving rank direction without becoming exact component rigidity; a joint `(log n, omega(n))` localization or destination-side argument is qualitatively different from merely changing the physical-scale weight.

**Boundary.** FD-136 is an ancestry-to-source obstruction, not a construction satisfying the physical Mertens envelope or the repeated-square Farey target. It does not show that rank-conditioned harmonic norms, mesoscopic joint windows, local quantiles, or Fourier-skeleton coercivity succeed; it only shows that logarithmic scale balancing alone does not remove the moving-rank escape.