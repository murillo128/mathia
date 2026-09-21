# MI-061 — Critical inherited repair cancels its polar main term and reduces to a smoothed Chebyshev error

**Evidence level:** exact source-conditioned operator synthesis from [WI-380](../../findings/WI-380-gamma-negative-source-zero-modes-localize-favorable-arithmetic-to-critical-shifts.md) and [WI-381](../../findings/WI-381-critical-prime-repair-cancels-the-polar-root-at-leading-order.md), using the exact localized Desogus operator normalization audited there. The autocorrelation and Stieltjes-summation steps are classical; the line-specific content is the cancellation on the certified source-zero gamma-negative trials.

WI-380 localizes every favorable inherited arithmetic branch on the fixed-depth source-zero trials to the cross-origin window

`log n = A_k + O(1)`, with `A_k=log(k+1)`.

Small shifts are unfavorable, the middle range is invisible, and only this critical normalized layer can contribute positive direct repair.

WI-381 shows that the gross positive mass in that annulus is not a free repair resource. With `x_k=k+1`, the critical arithmetic term is `+Theta(sqrt(x_k))`, but the exact polar rank-one term has the equal and opposite leading contribution:

`x_k^(-1/2) (Q_k^crit + Q_k^pol) -> 0`.

More sharply, if `E(u)=psi(u)-u`, then

`Q_k^crit + Q_k^pol = 4 I_(k,+) I_(k,-) - 2 x_k^(-1/2) I_(k,-)^2 + 2 int w_k(u) dE(u)`.

The remaining same-lobe arithmetic is only `O_L(1)`. Thus the unresolved arithmetic datum is the fixed-log-width smoothed Chebyshev-error functional

`E_k = 2 int w_k(u) d(psi(u)-u)`,

not the raw Mangoldt mass near `n≈k`.

This changes the direct-repair test. Comparing the positive critical annulus to the fixed gamma tariff while omitting the polar debt double-counts the same leading density. Classical PNT gives only `E_k=o(sqrt(x_k))`; it does not supply the fixed-scale sign or `O(1)`-level control needed to decide the gamma defect on these trials.

**Boundary.** No positivity or negativity conclusion for the full rooted form follows. The surviving routes are a sign/coercive estimate for the smoothed Chebyshev error strong enough at this fixed logarithmic scale, a further exact rooted identity that controls it, or an exact graph/domain condition excluding the WI-380 source-zero trials before evaluation.