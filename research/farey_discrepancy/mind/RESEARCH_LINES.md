# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Break the direct-transfer normalization barrier by changing source coherence or cross-scale coupling, not host/head bookkeeping

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

FD-067 adds a different cross-scale constraint that the pointwise exponent ledger does not see. For every nonsquarefree integer `q>1`,

\[
U_{H,D}\ge w(q)E_{\lfloor H/q\rfloor,\lfloor D/q\rfloor},
\qquad w(q)=J_2(q)/q^2.
\]

Hence on a `q`-adic chain `H_j=q^jH_0` with a subcovariant head schedule `floor(D_j/q)<=D_(j-1)`, the actual nonsquarefree occupation telescopes:

\[
\prod_{j=1}^n\frac{U_{H_j,D_j}}{E_{H_j,D_j}}
\ge w(q)^n\frac{E_{H_0,D_0}}{E_{H_n,D_n}}.
\]

For `D_j=H_j^{\delta+o(1)}`, this forces a positive geometric-mean occupation lower bound `w(q)q^{-a_\delta(\Theta)}` with `a_\delta(\Theta)=\delta+2\Theta(1-\delta)`. On a positive lower proportion of the chain the scalar Schur loss is therefore at least order `1/D_j`; at a linear head the `q=4` occupation bound becomes the `\Theta`-independent constant `3/16`.

This does **not** defeat FD-066: an adaptive zero-frontier spike sequence may jump between multiplicative rays, so no pointwise all-horizon gap follows. It does rule out a weaker escape: growing the head cannot make the defect disappear on essentially every scale of any fixed nonsquarefree dilation chain. A genuine advance must now either produce source coherence beyond `2(1-\Theta)`, couple adaptive spike scales to recurrent multiplicative rays strongly enough to prevent cross-ray escape, derive a comparable cross-ray recurrence, or bypass the reciprocal-floor/horizon normalization.

## Reach or bypass the square-root / cube-root phase boundary

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-064 shows that packet rows satisfy `r=T^{\lambda/(1+\lambda)+o(1)}`. A direct all-short-interval input with threshold exponent above `1/2` keeps every reachable row strictly inside the cube-root Jordan core; reaching `r\asymp T^{1/3}` is equivalent to transferring over square-root-scale source intervals.

FD-066 sharpens what kind of stronger interval theorem would matter. Lowering the admissible interval threshold is useful for placement, but below `\Theta=2/3` the normalized scalar target needs coherence of the **actual spike amplitude** over `\ell>2(1-\Theta)`, not merely cancellation on shorter intervals. An almost-all/maximal theorem is useful only if its quantifiers can be coupled to the adaptive spike and provide that source-relative variation bound.

FD-067 adds that fixed multiplicative rays already contain recurrent good occupation even for moving heads. Thus an adaptive source theorem that can localize zero-frontier spikes onto a controlled family of dilation rays would buy more than another isolated packet estimate: it could convert recurrent occupation into a source-coupled obstruction. No such localization is currently proved.

## Keep local capacity, coherence length, dilation recurrence, host entropy, head location, leverage, horizon cost, and normalized occupation separate

A physical short-interval theorem can buy subcritical placement, a macroscopic host corridor, and polynomial packet multiplicity. A larger Schur head can improve a tail-occupation lower bound while losing scalar leverage. FD-066 shows that even source coherence itself has a precise normalization threshold: raw packet size is not the relevant currency once the same source window and physical horizon are priced.

FD-067 shows that pointwise and recurrent statements must also be kept separate. The moving-head scalar gap may decay like `1/D`, yet fixed nonsquarefree dilation chains cannot evade it at essentially every scale. Conversely, positive-density recurrence on each fixed ray does not control an adaptive spike sequence that is free to change rays.

Any proposed advance must therefore state the source amplitude `A_X`, coherence length/exponent, host scale, packet exponent, row location, dilation/ray structure, Schur-head scale when used, physical horizon, same-horizon denominator, scalar leverage, and resulting pointwise or recurrent normalized conclusion. The live bottleneck is explicit: **obtain source coherence beyond `2(1-Theta)`, couple adaptive spikes to the multiplicative recurrence, or change the normalization mechanism that makes the direct threshold unavoidable**.