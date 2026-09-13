# MI-020 — Complete one-signed screening and support topology still saturate the log-2 packing ceiling

**Evidence level:** exact on the relaxed one-signed first-crossing class through [WI-281](../../findings/WI-281-complete-one-signed-prime-screening-forces-log2-support-packing-and-a-smaller-archimedean-budget.md)--[WI-283](../../findings/WI-283-support-domination-does-not-lower-screened-packing-supremum.md). No theorem that the first null mode is one-signed, no exact-null-equation realization, and no RH consequence is claimed.

WI-281 shows that if a hypothetical first null mode satisfies `v>=0` and all active prime-power autocorrelations vanish, the powers of two already force its positive set to be a measurable selector modulo `L=log 2`. Hence `|{v>0}|<=L`, and Riesz rearrangement lowers the positive archimedean budget from the unrestricted `K_+` to

`K_pack=(1/2) lambda_max(T_L)<K_+`.

WI-282 identifies the first sharpness boundary. Every positive von-Mangoldt lag is at least `log 2`, so the top eigenfunction on one interval of length `L` already screens **all** prime-power lags, not only powers of two. Qualitative full span does not lower the supremum either: arbitrarily small endpoint satellites can enforce span while the profiles converge in `L^2` back to the `K_pack` optimizer.

WI-283 shows that even the source-specific support domination extracted from the actual Suzuki null equation remains too weak after amplitudes are forgotten. A maximal open set avoiding the finite active prime-power distances is automatically dominating under those translations. Starting from a near-`K_pack` screened core, one can saturate its support in this sense and then place arbitrarily small positive `L^2` mass throughout the saturated open set. The closed essential support obeys the exact prime-translation domination condition, while `B_+` changes arbitrarily little.

Therefore the relaxed class with

`nonnegativity + normalization + complete prime-power screening + full essential span + prime-translation support domination`

still has exact supremum `K_pack`. There is no positive gap available from these hypotheses alone.

The key distinction is now **support topology versus amplitude transport**. Support domination says that every point is touched by the support or one of its prime translates, but it does not price how much mass reaches those contacts. Topology can be changed by vanishing-mass additions while an `L^2`-continuous endpoint functional barely notices. A strict decrement must use a source law that forces non-negligible amplitude or signed balance, not merely closure contact.

The remaining one-signed candidates are correspondingly sharper: the full equation `A_a v=0`, quantitative lower mass in translated regions, regularity/nodal/boundary-flux constraints that convert contact into amplitude, source-weighted archimedean/prime balance, a first-crossing spectral-area margin, or simultaneous-cut relations coupling more than autocorrelation zero sets. The next theorem has to distinguish actual null modes from the screened near-extremizers in a currency that `B_+` can feel.

**Boundary.** The saturated profiles are not Suzuki null modes and say nothing about the sign-changing branch. A quantitative two-sided mass or operator constraint can still lower the budget; WI-283 rules out only the support-topological shadow of such a constraint.
