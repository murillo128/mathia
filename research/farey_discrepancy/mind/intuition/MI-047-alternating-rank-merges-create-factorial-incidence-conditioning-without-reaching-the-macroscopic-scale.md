# MI-047 — Alternating rank merges create factorial exact-omission conditioning without reaching the macroscopic scale

**Evidence level:** exact divisor-poset synthesis from [FD-250](../../findings/FD-250-alternating-rank-merges-beat-every-fixed-loglog-power.md), building on the weighted incidence inverse in FD-248 and the single-star lower bound in FD-249. Rank-selected Boolean-lattice Möbius coefficients and alternating-permutation counts are classical ingredients; the line-specific content is their exact adjacent-pair omission realization.

FD-250 shows that exact omissions can realize much stronger weighted incidence conditioning than one high-arity star. A nested rank-selected squarefree divisor component can place factorial-size Möbius coefficients on a reciprocal-heavy rank while the omission count remains subpolynomial:

`K=N^(o(1))`,

and along an infinite family

`log kappa(D_N) >= (1-o(1)) (log log log N)(log log log log N)`.

Equivalently, `kappa(D_N)` beats every fixed power of `log log N`. The mechanism is not long-chain depth by itself: alternating retained ranks create large incidence-Möbius coefficients, and the reciprocal divisor mass of the selected rank lets those coefficients survive the `q/d` weighting in the exact inverse norm.

This materially moves the response-side frontier. Bounded depth, forest geometry, a single merge count, or any fixed polylogarithmic-in-`log log N` heuristic is too weak to control exact-omission amplification. The relevant question is the maximal weighted incidence complexity permitted by the genuine adjacent-pair support constraint `D subset E union (E+1)`.

The result still does **not** bridge the main scale gap. Hiding macroscopic coefficient mass with `K=o(N)` requires `kappa(D)` on the order of `N/K`, whereas the present construction is subpolynomial in `N`. The durable next question is therefore whether exact adjacent-pair supports can amplify all the way toward that scale or whether a universal subpolynomial/subpower upper bound survives.

**Boundary.** This is a signed response-space construction. It does not impose positivity, finite prime-reservoir capacity, squarefree physical-source realizability beyond the designed divisor component, or full arithmetic coherence. Those source-side restrictions may still exclude the large inverse directions and must be audited separately.