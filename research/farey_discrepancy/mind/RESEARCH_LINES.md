# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Penetrate below the deterministic critical host scale

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-049--FD-055 reduce residual occupation collapse to a low-row source-localization problem and show that sufficiently strong short-interval cancellation transfers a zero-frontier spike to nearby nonsquarefree quadratic occupation.

FD-056--FD-058 distinguish sparse represented-start sampling from maximal ambient-window localization. A maximal source theorem can avoid the reciprocal-sample cardinality penalty, but its exceptional measure must still be smaller than the containing-start corridor at the desired transfer scale.

FD-059 identifies the deterministic critical scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable residue-class selection plus the one-Lipschitz source already forces a constant-fraction nonsquarefree twin at `q\asymp Q_X`. FD-060 shows that subpower slack above `Q_X` can produce a growing CRT packet of nonsquarefree rows carrying the same physical spike.

The deterministic source bill is therefore sharp at mechanism level. At `qA_X/X\asymp1`, bounded increments guarantee only bounded packet length; a growing fixed-fraction packet requires `qA_X/X\to\infty`. For `qA_X/X\to0`, even fixed-fraction one-row transfer needs genuine source cancellation/localization or a different source-coupled mechanism. The live below-critical theorem is to cross `X/A_X`, not merely reproduce its power exponent with subpower overhead.

## Improve the packet-horizon global occupation exponent or turn it into positive occupation

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-061 closes the first denominator gap left by FD-060 at the power-exponent scale. Along a false-RH frontier spike `A_X=X^{\Theta+o(1)}`, `1/2<\Theta<1`, the CRT packet occurs at

\[
T_X=X^{2-\Theta+o(1)}
\]

and the global nonsquarefree occupation satisfies, for every `eta>0`,

\[
T_X^{\beta_\Theta+\eta}\nu_{T_X,D}\to\infty,
\qquad
\beta_\Theta=\frac{2\Theta(1-\Theta)}{2-\Theta}.
\]

Combined with the all-horizon exponent `2\Theta-1` from FD-049, the packet gives a strictly stronger polynomial-loss barrier exactly when `\Theta>2/3`; the two exponents meet at `\Theta=2/3`.

This is still not positive occupation. The generic global energy envelope is too coarse to prove `\liminf U/E>0`, and increasing the CRT packet by another subpower factor cannot improve the power exponent because the longer packet pushes the evaluation horizon outward. A stronger result must either sharpen the denominator on the **same packet horizons** or move many source-bearing nonsquarefree rows to a better row-count/horizon tradeoff.

## Keep transfer accuracy, packet multiplicity, and normalized occupation as different currencies

At `qA_X/X\asymp1`, favorable host selection gives constant-factor one-row transfer. At `qA_X/X\to\infty`, the same deterministic budget can produce `K_X\to\infty` fixed-fraction rows. FD-061 shows that this local multiplicity does not become an extra global power after division by the full energy: the horizon displacement absorbs it at exponent scale.

Any use of the zero-frontier exponent must therefore keep the hidden subpower ratio `qA_X/X`, packet size, packet horizon, global energy envelope, and normalized occupation exponent explicit. Equal row exponents, an unbounded local packet/host ratio, and a positive global occupation fraction are not interchangeable statements.