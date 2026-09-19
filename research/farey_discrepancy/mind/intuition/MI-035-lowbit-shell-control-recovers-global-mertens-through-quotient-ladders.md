# MI-035 — Lowbit shell control reaches global Mertens, but the positive root anchor is already RH-complete

**Evidence level:** exact synthesis from [FD-204](../../findings/FD-204-lowbit-tree-achieves-logarithmic-resistance-at-near-critical-random-cost.md), [FD-205](../../findings/FD-205-binary-quotient-ladders-promote-lowbit-shell-control-to-an-rh-criterion.md), and [FD-206](../../findings/FD-206-root-aligned-lowbit-anchor-is-an-rh-equivalent-dyadic-mertens-criterion.md).

FD-204 constructs a source-localized multiscale observation geometry with two properties that had previously competed: anchored inverse resistance is only logarithmic, while each physical Möbius slab is reused only once per dyadic scale, so the squarefree-random comparator pays `H^(1+o(1))` rather than the older `H^(3/2)` tariff.

FD-205 proves that the lowbit shell sensors have enough recovery semantics to reconstruct global Mertens values. Its quotient-coordinate viewpoint remains useful: physical primes and horizons may change across scales while exact source increments telescope through an internal arithmetic coordinate.

FD-206 identifies a much shorter recovery path and corrects one boundary of FD-205. Let `p_n` be the largest prime at most `n` and set `H_n=n p_n`. Then `p_n` is exactly the terminal prime/root of the critical shell and

`S_(2,H_n)(p_n)=M(2n)-M(n)`.

The anchored lowbit energy therefore contains the positive summand

`K_n |M(2n)-M(n)|^2`.

A critical-power bound on this single cofinal horizon family already forces `M(2n)-M(n)=O_epsilon(n^(1/2+epsilon))`. No lowbit point-evaluation resistance is needed. More importantly, the doubling increment alone is RH-complete: if `N=2n+b`, `b in {0,1}`, then

`M(N)-M(n)=[M(2n)-M(n)] + b mu(2n+1)`.

Descending through binary prefixes therefore reconstructs arbitrary `M(N)` from doubling increments plus an `O(log N)` bounded correction. Thus square-root control of `M(2n)-M(n)` is equivalent to the classical square-root Mertens criterion for RH.

This changes the interpretation of the lowbit success. The graph geometry genuinely improves inverse resistance and random source reuse, but the deterministic positive energy target already contains an RH-equivalent scalar subproblem as one coordinate. A favorable random comparator is therefore not evidence that the full energy estimate is an easier route to RH when its root anchor must itself satisfy square-root cancellation.

The reusable distinction is between **recovery power** and **analytic leverage**. A representation may recover the destination perfectly, and its auxiliary geometry may be near-critical, while the proposed norm still hides the original hard problem in one nonnegative coordinate. Before treating a derived energy as progress, isolate its anchors and ask whether any cofinal source specialization turns one anchor into a destination-complete scalar estimate.

**Boundary.** FD-206 does not invalidate the exact lowbit tree, its logarithmic resistance, or its source-localized edge structure. It shows that the current positive anchoring does not by itself lower the analytic barrier. A surviving Farey route must derive the root increment from additional signed/cross-scale structure, or replace the positive standalone anchor by an observable where cancellation can occur before that RH-complete coordinate is bounded.