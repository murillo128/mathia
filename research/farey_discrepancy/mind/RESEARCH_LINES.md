# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Couple persistent source-spike capture to the same-horizon denominator

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-059--FD-066 isolate the direct coherent-packet threshold. If a zero-frontier spike `A_X=X^{Theta+o(1)}` remains comparable on a backward window `L_X=X^{ell+o(1)}`, then after reciprocal-floor transfer, horizon normalization, and Schur leverage are all paid, the direct packet improves the deterministic terminal obstruction exactly when

\[
\ell>2(1-\Theta).
\]

FD-067--FD-068 add an independent recurrence constraint: under q-subcovariant head growth, very low normalized nonsquarefree occupation cannot be typical in multiplicative or global logarithmic scale. That still allows an adaptively selected logarithmically sparse spike sequence.

FD-069 now supplies the missing **pointwise source-to-occupation** link at arbitrary later horizons. For

\[
A_X=|\mathcal H(X)|,
\qquad
U_{T,D}=\sum_{\substack{D<r\le T\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2,
\]

round `T/X` upward to the next multiple of four. The resulting nonsquarefree row samples the source within reciprocal mesh `O(X^2/T)`, and the one-Lipschitz source gives

\[
U_{T,D}
\ge
\frac1{\zeta(2)}
\left(A_X-\frac{4X^2}{T}-1\right)_+^2
\]

whenever that row survives the head. Equivalently,

\[
A_X
\le
1+\frac{4X^2}{T}+\sqrt{\zeta(2)U_{T,D}}.
\]

Thus every low-`U` horizon carves out a deterministic backward exclusion cone for large past source values. A spike becomes visible at constant factor once `T` reaches order `X^2/A_X`, and after that threshold the witness persists at every sufficiently later horizon rather than only on a selected host ray.

For a zero-frontier spike `A_X=X^{Theta+o(1)}`, the capture onset is

\[
T_{\rm cap}=X^{2-\Theta+o(1)},
\qquad
r=T_{\rm cap}^{\alpha_\Theta+o(1)},
\qquad
\alpha_\Theta=\frac{1-\Theta}{2-\Theta}.
\]

With a moving head `D_T=T^{\delta+o(1)}`, source capture and head survival jointly begin at power exponent

\[
\tau_*(\delta,\Theta)
=
\max\left\{2-\Theta,\frac1{1-\delta}\right\}.
\]

The same `alpha_Theta` is exactly the crossover between source-sampling and head-deletion obstruction.

The remaining normalization problem is now sharper. FD-069 gives a numerator witness `U_{T,D}` but not a lower bound for `U_{T,D}/E_{T,D}`. The next useful theorem must couple persistent spike capture to the **same-horizon denominator**, or show that zero-frontier spikes and candidate low-occupation horizons cannot remain separated by the capture/head scales above. Repeating favorable host selection is no longer the relevant quantifier improvement.

## Keep source coherence, reciprocal-mesh capture, logarithmic recurrence, head survival, leverage, and denominator growth separate

The direct coherent-packet threshold, the global logarithmic recurrence theorem, and the arbitrary-horizon four-adic sampler now control three different losses. FD-066 asks how long a large source excursion stays coherent. FD-068 says low normalized occupation cannot dominate logarithmic scale. FD-069 says a large source value itself becomes visible in the nonsquarefree numerator at every sufficiently late admissible horizon.

None of these statements alone controls the full normalized target. In particular, persistent numerator occupation can coexist with faster growth of the total energy denominator. Future progress should identify the exact coupling that prevents this dilution rather than conflate pointwise spike capture with normalized obstruction.
