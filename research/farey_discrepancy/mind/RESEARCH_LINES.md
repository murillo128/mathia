# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Break the direct-transfer normalization barrier by changing source coherence, not host/head bookkeeping

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-059 identifies the deterministic critical host `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`. FD-062--FD-063 show that genuine all-short-interval Möbius cancellation crosses that deterministic scale and supports growing packets uniformly across a whole host corridor; host selection and CRT sparsity are no longer the main local bottleneck.

FD-064 classifies the stronger power-gap regime. On a zero-frontier spike `A_X=X^{\Theta+o(1)}`, hosts `q\asymp X^\lambda` can support polynomial packets, but after normalization at `T=qX` the best exponent still has the exact `\Theta=2/3` crossover. FD-065 closes the most direct denominator-side repair: moving the Schur head shortens the tail but loses scalar leverage by the matching power, so the crossover is unchanged.

FD-066 identifies the invariant source-side currency behind both calculations. Suppose the spike remains comparable on a backward window

\[
L_X=X^{\ell+o(1)}.
\]

Reciprocal-floor geometry converts that window to `X^{\lambda+\ell-1+o(1)}` packet rows. After the generic zero-frontier denominator and Schur leverage are included, the packet exponent minus the deterministic terminal exponent is

\[
\frac{2-2\Theta-\ell}{1+\lambda}.
\]

Thus **every direct coherent packet beats the terminal scalar obstruction at power scale iff**

\[
\ell>2(1-\Theta).
\]

The sign is independent of host placement and Schur-head exponent. Host displacement only converts source length into row multiplicity while paying the corresponding physical horizon; head motion changes denominator and leverage together.

The current all-short-interval input guarantees coherence only for fixed powers `\ell<\Theta`, which recovers the `\Theta=2/3` crossover immediately. For `\Theta<2/3`, a direct packet would need super-amplitude coherence

\[
\ell>2(1-\Theta)>\Theta.
\]

Therefore a theorem that merely lowers the **minimum interval length** while retaining only an `o(L)` or logarithmic relative error does not change the power ledger. A genuine advance must control source variation by `o(A_X)` on windows longer than the spike-amplitude scale, localize such windows around the adaptive zero-frontier spikes, or bypass the reciprocal-floor/horizon normalization entirely.

## Reach or bypass the square-root / cube-root phase boundary

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-064 shows that packet rows satisfy `r=T^{\lambda/(1+\lambda)+o(1)}`. A direct all-short-interval input with threshold exponent above `1/2` keeps every reachable row strictly inside the cube-root Jordan core; reaching `r\asymp T^{1/3}` is equivalent to transferring over square-root-scale source intervals.

FD-066 sharpens what kind of stronger interval theorem would matter. Lowering the admissible interval threshold is useful for placement, but below `\Theta=2/3` the normalized scalar target needs coherence of the **actual spike amplitude** over `\ell>2(1-\Theta)`, not merely cancellation on shorter intervals. An almost-all/maximal theorem is useful only if its quantifiers can be coupled to the adaptive spike and provide that source-relative variation bound.

## Keep local capacity, coherence length, host entropy, head location, leverage, horizon cost, and normalized occupation separate

A physical short-interval theorem can buy subcritical placement, a macroscopic host corridor, and polynomial packet multiplicity. A larger Schur head can improve a tail-occupation lower bound. FD-066 shows that even source coherence itself has a precise normalization threshold: raw packet size is not the relevant currency once the same source window and physical horizon are priced.

Any proposed advance must state the source amplitude `A_X`, coherence length/exponent, host scale, packet exponent, row location, Schur-head scale when used, physical horizon, same-horizon denominator, scalar leverage, and resulting normalized exponent. The live bottleneck is now explicit: **obtain source coherence beyond `2(1-Theta)` or change the normalization mechanism that makes that threshold unavoidable**.