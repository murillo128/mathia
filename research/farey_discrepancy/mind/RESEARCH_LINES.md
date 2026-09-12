# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Use short-interval source cancellation below the deterministic host scale

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-049--FD-055 reduce residual occupation collapse to a low-row source-localization problem and show that sufficiently strong short-interval Möbius cancellation transfers a zero-frontier spike to nearby nonsquarefree occupation. FD-056--FD-058 distinguish sparse represented-start sampling from maximal ambient-window localization.

FD-059 identifies the deterministic critical scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable residue-class selection plus the one-Lipschitz source forces a constant-fraction nonsquarefree twin at `q\asymp Q_X`. FD-060 shows that subpower slack above `Q_X` can produce a growing CRT packet.

FD-062 now crosses the deterministic scale with a **growing** packet when physical short-interval cancellation is available. If `A_X(\log X)^B\ge X^\vartheta` with `\vartheta>0.55` and `B+\kappa<1/3`, there are squarefree hosts and packet lengths `K_X\to\infty`, `K_X\le(\log X)^\kappa`, for which

\[
\frac{qA_X}{X}\asymp(\log X)^{-B}\to0
\]

while every packet row remains source-close to the selected spike. Thus growing local nonsquarefree occupation does **not** intrinsically require supercritical placement. The logarithmic short-interval saving is a budget that can be split between penetration below `X/A_X` and packet width.

The remaining localization boundary is now explicit: the present theorem uses the all-short-interval range `\vartheta>0.55` and the available logarithmic saving. The unresolved source problem is what, if anything, can replace that input in the `\Theta\le0.55` range or improve the budget beyond `B+\kappa<1/3`.

## Sharpen the same-horizon denominator rather than the packet geometry

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-061 measures the global loss of the supercritical packet. Along a false-RH frontier spike `A_X=X^{\Theta+o(1)}`, the packet horizon gives the exponent

\[
\beta_\Theta=\frac{2\Theta(1-\Theta)}{2-\Theta},
\]

which improves the all-horizon `2\Theta-1` barrier exactly for `\Theta>2/3`, but still does not give positive normalized occupation.

FD-062 strengthens the geometry without removing this global obstruction. The host can now satisfy `qA_X/X\to0` while carrying `K_X\to\infty`, and on false-RH frontier sequences one can take a fixed logarithmic packet power. Yet the generic denominator envelope on those **same source-selected horizons** absorbs the available subpower gains.

The next global theorem should therefore control the energy denominator on the packet horizons themselves, or find a source-coupled transfer with a genuinely better row-count/horizon tradeoff. Another CRT refinement at the deterministic host scale is no longer the bottleneck.

## Keep transfer accuracy, packet multiplicity, host scale, and normalized occupation as different currencies

Bounded increments alone have a sharp host-scale bill. Genuine short-interval cancellation can cross it and can simultaneously support growing local multiplicity. Neither statement yields a positive fraction of the full energy.

Any use of the zero-frontier exponent must therefore keep the source amplitude, `qA_X/X`, packet width, packet horizon, same-horizon denominator, localization range, and normalized occupation exponent explicit. Equal row exponents, an unbounded packet/host ratio, and positive global occupation are not interchangeable statements.