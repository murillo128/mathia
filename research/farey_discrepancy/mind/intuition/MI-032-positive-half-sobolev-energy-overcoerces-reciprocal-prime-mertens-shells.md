# MI-032 — Positive half-Sobolev energy overcoerces reciprocal-prime Mertens shells

**Evidence level:** exact synthesis from [FD-196](../../findings/FD-196-weighted-fourier-duality-phase-diagram.md), [FD-197](../../findings/FD-197-random-squarefree-multiplicative-source-saturates-noncritical-fourier-energy-line.md), and [FD-198](../../findings/FD-198-prime-square-root-fourier-shell-forces-subpower-mertens-rms.md).

A positive quadratic observation can be simultaneously **too weak for one inverse direction and too strong as a global source requirement**. Farey Discrepancy now exhibits both effects in the same square-root band.

Write `K=floor(sqrt(H))` and

`B_H(k)=sum_(d|k) d M(floor(H/d))`.

For every prime `K/2<p<=K`, FD-198 gives the exact centered identity

`B_H(p)-B_H(1)=p M(floor(H/p))`.

Consequently the positive half-Sobolev energy `E_(H,1/2)(K)=sum_(k<=K)|B_H(k)|^2/k` controls the whole reciprocal-prime shell at once. If

`E_(H,1/2)(K)=H^(gamma+o(1))`,

then the RMS over the `Theta(K/log K)` distinct samples `M(floor(H/p))`, all at arguments `Theta(K)`, obeys

`RMS << K^(gamma-1+o(1))`.

At the FD-196 RH-facing budget `gamma=1`, this becomes subpower RMS `K^o(1)`. That is much stronger on this growing sparse family than the pointwise RH-scale bound `K^(1/2+epsilon)`. By contrast the squarefree Rademacher multiplicative baseline of FD-197 has `gamma=3/2`, and therefore lands exactly at square-root RMS.

This changes how the missing half power should be read. FD-195--FD-196 already showed that scalar quadratic energy loses the `n^(-1+o(1))` contraction visible in a raw inverse row. FD-198 adds the opposite audit: lowering the positive energy far enough to recover one RH-scale coordinate also suppresses many other coordinates simultaneously far below the RH pointwise scale. The same norm is therefore poorly matched to the target in two directions: its dual geometry throws away rowwise contraction, while its positivity couples many rows into an overcoercive global demand.

The reusable diagnostic is: **before treating a positive energy estimate as the right critical theorem because it implies the desired pointwise bound, compute the strongest simultaneous source consequence forced by the same budget.** A sufficient energy may be mathematically much stronger than the target statement even when a one-row Cauchy--Schwarz estimate makes it look exactly critical.

A more economical Farey route could therefore require an indefinite or signed cross-mode statistic, cross-horizon cancellation, or another destination norm that preserves the useful divisor-inverse contraction without forcing every retained square-root-band mode to be small independently. This is a direction suggested by the obstruction, not an established replacement theorem.

**Boundary.** FD-198 does not prove the critical half-Sobolev estimate false, does not show RH cannot imply it, and does not transfer the reciprocal-prime RMS statement to other observation norms. The overcoercivity statement is specific to this positive energy and its exact prime-shell rows.