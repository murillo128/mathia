# MI-001 — Farey transfer is governed by source coherence, reciprocal-mesh capture, and denominator normalization

**Evidence level:** supported by the exact source/occupation reductions through FD-069 plus the cited all-short-interval Möbius theorem; no normalized RH obstruction at an adaptively selected zero-frontier spike is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-066 separate deterministic transfer, short-interval cancellation, host placement, packet multiplicity, horizon normalization, and Schur-head leverage. FD-066 isolates the invariant direct-transfer threshold. If a zero-frontier spike `A_X=X^{Theta+o(1)}` stays comparable on a backward window `L_X=X^{ell+o(1)}`, then the coherent packet improves the terminal scalar obstruction exactly when

\[
\ell>2(1-\Theta).
\]

Host exponent and head exponent redistribute this source-coherence budget but do not change its sign.

FD-067--FD-068 expose a different multiplicative recurrence. For q-subcovariant head schedules, normalized nonsquarefree occupation satisfies a dilation inequality whose logarithmic integration telescopes over all horizons. Polynomial heads therefore have a positive global logarithmic geometric-mean occupation bound. Extremely low normalized occupation cannot be typical, but an adaptively selected zero-frontier spike sequence could still lie in a logarithmically negligible exceptional set.

FD-069 adds the missing deterministic pointwise link without selecting a favorable host. At any later horizon `T`, round the real row `T/X` upward to the next multiple of four. The corresponding nonsquarefree reciprocal sample lies within

\[
0\le X-\left\lfloor\frac{T}{r_{T,X}}\right\rfloor
\le \frac{4X^2}{T}+1.
\]

Since the physical source is one-Lipschitz, whenever that row survives the head,

\[
U_{T,D}
\ge
\frac1{\zeta(2)}
\left(A_X-\frac{4X^2}{T}-1\right)_+^2.
\]

Thus a spike of height `A_X` becomes visible at constant factor once `T` reaches order `X^2/A_X`, and remains visible on every sufficiently later admissible horizon. For a frontier spike `A_X=X^{Theta+o(1)}`, this onset is `T=X^{2-Theta+o(1)}` and the witnessing row has exponent

\[
\alpha_\Theta=\frac{1-\Theta}{2-\Theta}.
\]

With a moving head `D_T=T^{delta+o(1)}`, the power onset is the larger of the source-sampling scale `2-Theta` and the head-survival scale `1/(1-delta)`. The same `alpha_Theta` is the crossover where those obstructions exchange dominance.

The resulting picture has three distinct quantifiers. Source coherence controls how a **packet** survives a selected transfer. Logarithmic recurrence controls how often normalized occupation can be tiny. Reciprocal sampling says that a **single pointwise source spike** eventually forces a large nonsquarefree numerator on every later admissible horizon. None controls the same-horizon energy denominator.

The live obstruction is therefore no longer absence of a pointwise spike-to-row map. It is **normalization**: prove that the denominator cannot grow fast enough to dilute every persistently captured frontier spike, or find a different source-to-target currency in which the captured row already carries the correct normalized weight.

**Boundary.** FD-069 is an exact numerator lower bound and backward exclusion cone. It does not prove a lower bound for `U_(T,D)/E_(T,D)`, a new zero-free region, or that frontier spikes occur with any prescribed density. FD-066, FD-068, and FD-069 constrain different parts of the transfer ledger and must not be substituted for one another.
