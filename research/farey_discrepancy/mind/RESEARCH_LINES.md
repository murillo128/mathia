# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Use short-interval source cancellation below the deterministic host scale

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-049--FD-055 reduce residual occupation collapse to a low-row source-localization problem and show that sufficiently strong short-interval Möbius cancellation transfers a zero-frontier spike to nearby nonsquarefree occupation. FD-056--FD-058 distinguish sparse represented-start sampling from maximal ambient-window localization.

FD-059 identifies the deterministic critical scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable residue-class selection plus the one-Lipschitz source forces a constant-fraction nonsquarefree twin at `q\asymp Q_X`. FD-060 shows that subpower slack above `Q_X` can instead be spent on multiplicity.

FD-062 crosses the deterministic scale with a growing packet when physical short-interval cancellation is available. If `A_X(\log X)^B\ge X^\vartheta` with `\vartheta>0.55` and `B+\kappa<1/3`, packet width `K_X\le(\log X)^\kappa` can grow while `qA_X/X\asymp(\log X)^{-B}\to0`.

FD-063 removes the remaining CRT host-selection cost from that occupation mechanism. Put `R_X=A_X(\log X)^B`, `K_X=\lfloor(\log X)^\kappa\rfloor`, and `Y_X=X/(8R_X)`. The same short-interval transfer holds uniformly for **every** host `Y_X\le q\le2Y_X`, and the trivial density of multiples of four supplies at least `K_X/4+O(1)` nonsquarefree rows. Consequently

\[
U_{qX,D}\ge\left(\frac1{4\zeta(2)}-o(1)\right)K_XA_X^2
\]

uniformly across the whole below-critical corridor. A positive proportion of those hosts are squarefree. Packet existence therefore no longer consumes host entropy through a growing CRT congruence.

The remaining localization boundary is the analytic input itself: the present theorem still uses `\vartheta>0.55` and the logarithmic budget `B+\kappa<1/3`. The unresolved source problem is what can replace that input for `\Theta\le0.55` or improve the available budget.

## Sharpen the same-horizon denominator across the available host corridor

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-061 measures the global loss of the packet mechanism: generic zero-frontier bounds for the full energy denominator absorb the available subpower gains. FD-062 improves the local geometry without fixing this, and FD-063 now shows that the packet lower bound is uniform on a corridor of `\asymp X/(A_X(\log X)^B)` hosts.

The next global theorem should exploit that new quantifier. It may average `E_{qX,D}` over the host corridor, select a favorable host after estimating the denominator, or prove a source-coupled same-horizon bound. If all of those fail, the obstruction is genuinely in physical energy across the corridor rather than in packet availability or CRT sparsity.

## Keep transfer accuracy, packet multiplicity, host entropy, host scale, and normalized occupation as different currencies

Bounded increments have a sharp deterministic host-scale bill. Genuine short-interval cancellation crosses it and supports growing local multiplicity. Four-adic row density then makes that multiplicity uniform over a macroscopic host corridor. None of these statements yields a positive fraction of the full energy.

Any use of the zero-frontier exponent must therefore keep the source amplitude, `qA_X/X`, packet width, host-corridor size, packet horizon, same-horizon denominator, localization range, and normalized occupation exponent explicit. Uniform packet availability and positive global occupation remain different statements.