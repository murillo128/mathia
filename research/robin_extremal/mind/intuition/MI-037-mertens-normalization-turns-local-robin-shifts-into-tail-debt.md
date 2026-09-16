# MI-037 — Mertens normalization turns local Robin shifts into tail debt

**Evidence level:** exact/literature-backed synthesis from [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), [RE-164](../../findings/RE-164-korobov-vinogradov-fidelity-controls-robin-source-ambiguity.md) through [RE-169](../../findings/RE-169-mertens-normalization-turns-post-selector-ambiguity-into-remote-compensation-debt.md). Classical Mertens normalization is external mathematics; the exact Robin-kernel debt identity and critical precision are line-specific.

RE-165--RE-168 show that a quantitative PNT/Korobov--Vinogradov envelope still allows order-one normalized Robin motion whenever enough displacement width is available near the moving capacity center. Those matched generalized-source controls preserve the Chebyshev envelope but were deliberately free to change the asymptotic Mertens product.

RE-169 identifies the missing invariant. With

`h(t)=-log(1-t^(-1))/log t`,

define the source Mertens constant `Gamma(Q)` by the asymptotic difference between `int h d theta_Q` and `log log x`. For two sources that agree below `T`, integration by parts gives the exact sum rule

`Gamma(Q_2)-Gamma(Q_1)=int_T^infty (theta_(Q_2)(t)-theta_(Q_1)(t))(-h'(t)) dt`.

The normalized Robin coordinate uses the **same kernel**. Therefore its accumulated post-selector difference up to height `U` equals the scaled Mertens-constant difference minus the still-unseen weighted tail. If the Mertens constants agree, every local Robin displacement is an exact compensation debt that must be repaid later.

Quantitative PNT fidelity then limits how long that debt can survive. Under the same KV envelope as RE-164--RE-168, the entire remaining compensation above `U` is bounded by the remote-tail capacity

`K_b(p,U)=sqrt(p) log p exp(-bV(U))/V(U)`.

A fixed nonzero normalized debt can therefore persist only while `K_b(p,U)` stays order one. In the intrinsic `V` coordinate it must be repaid within `O(1)` of the moving remote capacity-one center.

The precision scale is load-bearing. A compact matched relocation producing order-one normalized Robin displacement changes `Gamma` by only

`Theta((sqrt(p) log p)^(-1))`.

Hence the moving generalized controls still satisfy the qualitative statement `Gamma(Q_p)=gamma+o(1)`. Merely adding “Mertens holds asymptotically” does not repair source fidelity. The obstruction disappears only if the comparison class preserves `Gamma` to `o((sqrt(p) log p)^(-1))`, or exactly, and also has too little KV tail capacity to repay the debt later.

This creates a useful distinction between **envelope fidelity** and **normalization fidelity**. A pointwise source envelope limits how much weighted discrepancy can be stored in a region; a global normalization fixes the net weighted charge. Together they can convert a locally flexible source class into a globally constrained one even though neither does so alone at coarse precision.

For the ordinary-prime problem this is not yet the missing selector theorem. `Gamma(P)=gamma` is an exact global identity, but using it without an independent estimate on the selector-selected prefix would simply recycle the same conservation law. The live question is whether CA/ordinary-prime structure forces the compensation to occur on the favorable side or before the selector-sensitive Robin excursion can become dangerous.

**Boundary.** The sum rule assumes the relevant Mertens constants exist; this is automatic for the finite matched modifications used to audit the prior controls but not a consequence of bare PNT for arbitrary generalized primes. The result constrains source ambiguity and compensation location. It does not prove Robin's inequality, RH, or a sign theorem for ordinary CA selectors.
