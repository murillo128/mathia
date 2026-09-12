# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Break the direct-transfer normalization barrier rather than only enlarge the packet

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-059 identifies the deterministic critical host `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`. FD-062--FD-063 show that genuine all-short-interval Möbius cancellation crosses that deterministic scale and supports growing packets uniformly across a whole host corridor; host selection and CRT sparsity are no longer the main local bottleneck.

FD-064 classifies the stronger power-gap regime. On a zero-frontier spike `A_X=X^{\Theta+o(1)}`, hosts `q\asymp X^\lambda` with `1-\Theta<\lambda\le1-\vartheta` support polynomial packets `K_X=X^{\kappa+o(1)}` whenever `\kappa<\Theta+\lambda-1`. The local gain is genuine, but after normalization at `T=qX` the optimized exponent

\[
b_\Theta(\lambda)=\frac{1-\Theta+(2\Theta-1)\lambda}{1+\lambda}
\]

has derivative `(3\Theta-2)/(1+\lambda)^2`. Thus the entire direct power-gap family preserves the same `\Theta=2/3` crossover: for `\Theta>2/3` the best host returns to the critical boundary, while for `\Theta<2/3` the all-horizon FD-049 estimate remains stronger. At `\Theta=2/3`, every admissible host gives the same `1/3` loss.

The next global theorem must therefore change the normalization ledger, not merely buy more packet width. Concrete possibilities already left open by the evidence are a source-coupled same-horizon denominator, an averaging/selection theorem over the host corridor, or a source estimate with a different quantifier surface that can be coupled to the adaptive hosts.

## Reach or bypass the square-root / cube-root phase boundary

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-064 shows that packet rows satisfy `r=T^{\lambda/(1+\lambda)+o(1)}`. A direct all-short-interval input with threshold exponent `\vartheta>1/2` keeps every reachable row strictly inside the cube-root Jordan core. Reaching `r\asymp T^{1/3}` is equivalent to transferring over intervals of square-root scale.

This makes the analytic target precise. Either obtain cancellation at or below the square-root interval scale in the exact source family, exploit a maximal/almost-all theorem whose exceptional set can be reconciled with the host corridor, or find a mechanism that does not require direct endpoint transfer row by row. Merely improving constants or polynomial packet multiplicity above the current threshold cannot cross this phase boundary.

## Keep local capacity, host entropy, horizon cost, and normalized occupation separate

A physical short-interval theorem can buy subcritical placement, a macroscopic host corridor, and even polynomial packet multiplicity. None of those facts alone yields positive normalized occupation. The later horizon can consume the same power gained by the packet.

Any proposed advance must therefore state the source amplitude `A_X`, host scale, transfer interval scale, packet exponent, row location, physical horizon, same-horizon denominator, and resulting normalized occupation exponent. The live bottleneck is no longer packet existence in the present direct-transfer family; it is escaping the exact normalization/analytic phase barriers exposed by FD-064.