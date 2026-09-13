# MI-021 — Support-matched high moments reduce to arithmetic information in the Legendre sign distribution

**Evidence level:** the amplification threshold is exact through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md); [MC-265](../../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md) rules out first-order balance plus termwise absolute values; [MC-266](../../findings/MC-266-tensor-pair-krawtchouk-radial-source-walk-collapse.md) collapses the weighted pair geometry to a radial Boolean-cube source walk; and [MC-267](../../findings/MC-267-krawtchouk-source-hierarchy-amplitude-duality.md) proves that this radial hierarchy is exactly a Krawtchouk change of basis for the original shell-amplitude distribution. The required arithmetic cancellation remains open.

The surviving blind relation lives on a shell-prime subset of size `t`. At the first admissible support `t~(1/log 2)log log y`, MC-264 shows that moment order `2(t+1)` has enough diagonal leverage to exclude one blind atom if a near-diagonal moment estimate can be proved. MC-265 shows that generic first-order Hamming balance is far too weak after absolute values.

MC-266 rewrites the moment as

`S_(2m,y)(t)=sum_(s even) C_(2m,k_y)(s) H_(s,y)(t)`,

where `H_(s,y)(t)` is the signed shell aggregate over products of exactly `s` lower primes. MC-267 identifies what this representation does and does not buy. If `b_y(T)` is the number of negative lower-prime Legendre signs on a shell subset `T`, then

`H_(s,y)(t)=sum_(|T|=t) K_s(b_y(T);k_y)`.

Thus the complete support profile is exactly the Krawtchouk transform of the empirical Hamming-weight histogram of the original sign vectors. At finite depth the even layers `H_0,H_2,...,H_(2m)` are triangularly equivalent to the even amplitude moments `M_0,M_2,...,M_(2m)`.

This makes the algebraic boundary precise. Krawtchouk orthogonality, the three-term recurrence, Hamming-association-scheme identities and radial hypercube-walk structure are **information-neutral** until extra arithmetic input is inserted. They can reorganize the target moment but cannot themselves force the missing cancellation. A neighboring-layer recurrence is useful only if its coefficients or right-hand side are controlled by a theorem about the actual Legendre sign image, not if it is merely the universal Krawtchouk recurrence in another notation.

The live route is therefore a source theorem: constrain the distribution of `T -> (sigma_p(T))_p`, its Hamming histogram `A_(y,t)(b)`, a genuinely non-radial refinement, or an equivalent signed combination strongly enough at `m=t+1` to beat the MC-264 threshold before absolute values destroy cancellation. The `H_s` basis may still be the easiest place to state such a theorem, but success must come from arithmetic, not from the basis transform itself.

**Boundary.** MC-267 proves no new moment estimate and excludes no blind relation. Full Krawtchouk invertibility does not make individual support-layer estimates useless; it says only that universal transform identities add no scalar-distribution information. The surviving gain may still arise from arithmetic cancellation visible more naturally in the support basis than in raw amplitude moments.
