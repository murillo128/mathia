# MI-084 — Global ordinal prime relations can saturate source capacity only by paying identity-scale information

**Evidence level:** exact source-capacity synthesis from [MC-435](../../findings/MC-435-bounded-local-decorations-source-diversity-budget.md) and [MC-436](../../findings/MC-436-prime-divisor-gap-rank-permutations-saturate-source-capacity.md). Finite-word counting, Stirling asymptotics and the prime number theorem are classical; the line-specific content is the capacity threshold after quotienting the universal prime-order scaffold.

Once the canonical increasing-prime successor chain has been recognized as a universal rank scaffold, source variation must come from its decoration. If the retained decoration has total finite-alphabet budget

`B_r=sum_j log |A_(r,j)|`,

then the number of realized decorated source types satisfies `T_r<=exp(B_r)`. Along the primorial scale `log N_r~r log r`, any `B_r=o(r log r)` therefore gives only `T_r=N_r^(o(1))`. In particular, `O(r)` bounded or `r^(o(1))`-valued local marks cannot retain a fixed polynomial fraction of source-type diversity.

MC-436 shows that this threshold is sharp at the level of unconstrained realizability. The global rank order of the `r-1` adjacent selected-prime gaps realizes every permutation in `S_(r-1)`, so

`T_r^gap=(r-1)!=N_r^(1-o(1))`.

This escape is not cheap merely because it is ordinal. The permutation itself carries `Theta(r log r)` information, exactly the identity-scale budget demanded by MC-435. Low numerical precision can therefore coexist with near-lossless combinatorial source information.

The capacity question is now secondary. The decisive audit is whether some source-varying part of such an identity-scale relation is available at a controlled source height and survives a natural Möbius/divisor operation without effectively retaining the factors themselves. A global relation that has factorial type count but is erased by coefficient formation, or that is analytically usable only after reducing to bounded local bins, has not produced cancellation leverage.

**Boundary.** MC-436 proves every gap-order permutation only without a uniform size bound on the realizing squarefree integer. It supplies no Möbius cancellation estimate and no theorem that the ordinal relation survives multiplicative aggregation. Source-height efficiency and post-projection analytic survival remain independent gates.