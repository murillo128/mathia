# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Penetrate below the deterministic critical host scale

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-049--FD-055 reduce residual occupation collapse to a low-row source-localization problem and show that sufficiently strong short-interval cancellation transfers a zero-frontier spike to nearby nonsquarefree quadratic occupation.

FD-056--FD-058 distinguish sparse represented-start sampling from maximal ambient-window localization. A maximal source theorem can avoid the reciprocal-sample cardinality penalty, but its exceptional measure must still be smaller than the containing-start corridor at the desired transfer scale.

FD-059 changes where that machinery becomes necessary. If `A_X=|\mathcal H(X)|` and `Q_X=X/A_X`, a squarefree host `q=3 mod 4` exists at `q asymp lambda Q_X`; `q+1` is nonsquarefree and the one-Lipschitz source preserves a fixed positive fraction of the spike. Thus a comparable nonsquarefree quadratic twin exists deterministically at the exact critical scale `q asymp X/A_X`. Along a false-RH zero-frontier spike this reaches the critical row exponent for every `Theta>1/2`, and a subpower factor above `Q_X` gives first-order transfer at the same power exponent.

The unresolved source-regularity bill begins only for `qA_X/X -> 0`, where the quotient displacement is larger than the spike height. FD-055 gives logarithmic penetration below this scale under strong short-interval cancellation; FD-056--FD-058 formulate the maximal exceptional-measure route for broader below-critical displacement. The live theorem is to penetrate below `X/A_X` or obtain a separate mechanism controlling the global occupation ratio; merely reaching the zero-frontier power exponent is no longer the hard step.

## Treat critical deterministic transfer, below-critical localization, and global occupation as different currencies

At `qA_X/X asymp 1`, favorable residue-class selection plus bounded increments already gives constant-factor quadratic transfer. At `qA_X/X -> infinity` it gives first-order transfer; at `qA_X/X -> 0` genuine source cancellation or localization is needed. None of these one-row statements alone lower-bounds `U/E`, so competition from the remaining low rows is a separate global gate.
