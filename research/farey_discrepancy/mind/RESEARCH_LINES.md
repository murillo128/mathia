# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Break the direct-transfer normalization barrier rather than only enlarge the packet or move the Schur head

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-059 identifies the deterministic critical host `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`. FD-062--FD-063 show that genuine all-short-interval Möbius cancellation crosses that deterministic scale and supports growing packets uniformly across a whole host corridor; host selection and CRT sparsity are no longer the main local bottleneck.

FD-064 classifies the stronger power-gap regime. On a zero-frontier spike `A_X=X^{\Theta+o(1)}`, hosts `q\asymp X^\lambda` with `1-\Theta<\lambda\le1-\vartheta` support polynomial packets `K_X=X^{\kappa+o(1)}` whenever `\kappa<\Theta+\lambda-1`. After normalization at `T=qX`, however, the optimized exponent

\[
b_\Theta(\lambda)=\frac{1-\Theta+(2\Theta-1)\lambda}{1+\lambda}
\]

preserves the exact `\Theta=2/3` crossover.

FD-065 closes the most direct denominator-side repair. Let the Schur head grow as `D=X^{\delta+o(1)}` toward the packet host. The raw packet occupation lower bound does improve because the generic zero-frontier tail becomes shorter, but the Schur leverage simultaneously decays as `C_T-C_D\asymp D^{-1}`. Both the packet and terminal scalar loss exponents acquire the same penalty

\[
\frac{2\delta(1-\Theta)}{1+\lambda},
\]

so every positive head-growth exponent makes the scalar obstruction weaker and the `\Theta=2/3` crossover is unchanged. Moving the cut does not change the normalization ledger; its apparent denominator gain is overpaid by lost scalar leverage.

The next global theorem must therefore alter a load-bearing currency rather than optimize inside this family. Concrete possibilities already left open are a source-coupled same-horizon denominator, an averaging/selection theorem over the host corridor that uses numerator--denominator correlation, or a source estimate with a different quantifier surface that can be coupled to adaptive hosts.

## Reach or bypass the square-root / cube-root phase boundary

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-064 shows that packet rows satisfy `r=T^{\lambda/(1+\lambda)+o(1)}`. A direct all-short-interval input with threshold exponent `\vartheta>1/2` keeps every reachable row strictly inside the cube-root Jordan core. Reaching `r\asymp T^{1/3}` is equivalent to transferring over intervals of square-root scale.

Either obtain cancellation at or below the square-root interval scale in the exact source family, exploit a maximal/almost-all theorem whose exceptional set can be reconciled with the adaptive host corridor, or find a mechanism that does not require direct endpoint transfer row by row. Neither more packet multiplicity nor a growing Schur head crosses this phase boundary.

## Keep local capacity, host entropy, head location, leverage, horizon cost, and normalized occupation separate

A physical short-interval theorem can buy subcritical placement, a macroscopic host corridor, and polynomial packet multiplicity. A larger Schur head can also improve a tail-occupation lower bound. None of those facts alone improves the RH-facing scalar quantity: FD-065 shows explicitly that the head-dependent leverage can consume more power than the denominator saves.

Any proposed advance must therefore state the source amplitude `A_X`, host scale, transfer interval scale, packet exponent, row location, Schur-head scale when used, physical horizon, same-horizon denominator, scalar leverage, and resulting normalized exponent. The live bottleneck is escaping the normalization/analytic phase barriers, not producing another locally larger packet or shorter tail.