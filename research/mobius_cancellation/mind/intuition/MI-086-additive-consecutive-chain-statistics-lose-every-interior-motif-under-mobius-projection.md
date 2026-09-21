# MI-086 — Additive consecutive-chain statistics lose every interior motif under Möbius projection

**Evidence level:** exact Boolean-inclusion-exclusion synthesis from [MC-438](../../findings/MC-438-consecutive-block-mobius-projection-boundary-collapse.md), refining the full-interaction gate in [MC-437](../../findings/MC-437-mobius-convolution-extracts-full-prime-interaction.md).

Let `n=p_1...p_r` be squarefree with ordered prime factors. For a fixed `k>=2` and a kernel `W` on increasing `k`-tuples, define `A_(W,k)(m)` by summing `W` over consecutive `k`-blocks of the ordered prime factors selected by the divisor `m`. Selection-dependent adjacency can have arbitrarily high Boolean degree, so the bounded-degree vanishing test of MC-437 does not apply directly.

Nevertheless the full Möbius interaction is exact:

`(mu*A_(W,k))(n) = (-1)^(r-k) sum_(1=i_1<...<i_k=r) W(p_(i_1),...,p_(i_k))`.

Every motif that leaves a freely selectable prime outside its span cancels by inclusion-exclusion. Only blocks containing both global endpoint primes `p_1` and `p_r` survive. For `k=2` this collapses completely to

`(mu*A_(W,2))(n)=(-1)^(r-2) W(p_1,p_r)`.

Thus the factorial gap-order capacity exposed upstream does not survive merely by making a local statistic adjacency-dependent. Sums of fixed-size consecutive motifs can encode rich interior chain data on individual divisors while their top Boolean interaction forgets all interior motifs. Nonlinearity of the local kernel does not change that endpoint collapse.

The surviving gap-order question must therefore leave this additive local-motif class: use a genuinely global nonadditive functional of the whole induced gap-order permutation, a statistic whose labels depend on the surrounding selected set and whose full interaction can be derived, a block size that grows with `omega(n)`, or a different downstream operation. In every case the actual top interaction must be computed before source capacity is credited.

**Boundary.** The identity does not bound the information content of a surviving endpoint-spanning kernel value, does not cover arbitrary global/rank-dependent functionals, and does not turn a nonzero top interaction into analytic cancellation. It is specific to divisor Möbius convolution on squarefree sources.