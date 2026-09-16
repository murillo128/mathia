# MI-042 — Universal nonnegative mode selection saturates the half-loading and quartic source floor

**Evidence level:** proved for the reciprocal-endpoint architecture of MC-323--MC-326, with the universal mode-selection ceiling established in [MC-326](../../findings/MC-326-universal-mode-selection-half-loading-barrier.md).

The quartic common-radical frontier is not a peculiarity of pair modes or sparse even Hamming layers. Let `F` be any nonempty family of nonzero modes `a in F_2^R`, give them arbitrary nonnegative weights `w_a`, and write `W=sum_a w_a`. For a possible nonzero source column `s`, its weighted loading is

`L(s)=sum_(a in F, a·s=1) w_a`.

Every fixed nonzero mode sees exactly `2^(R-1)` of the `2^R-1` possible nonzero source columns. Averaging `L(s)` over those columns therefore gives

`(1/(2^R-1)) sum_(s!=0) L(s) = [2^(R-1)/(2^R-1)] W`.

Hence some column satisfies

`L(s)/W >= 2^(R-1)/(2^R-1) = 1/2 + 1/[2(2^R-1)]`,

and this finite-`R` constant is sharp when all nonzero modes carry equal weight. No irregular mode selection or nonnegative reweighting can drive the **universal** loading asymptotically below one half.

Combined with the individual near-quadratic conductor bill from MC-323, a proof that only sums independent nonnegative mode costs and protects against every possible source column can certify at most

`(2-delta)(2^R-1)/2^(R-1) < 4-2delta`

in the common-radical exponent. Pair modes already approach this optimum, and MC-325's Krawtchouk half-balance is a structured special case of the same universal averaging law.

The remaining escape is source-specific, not combinatorial family design. The actual columns are only `S_A={s_p}`. To beat one half one must prove that high-loading abstract columns cannot occur there, or carry too little logarithmic prime mass to matter. The other genuine escape is a joint or signed conductor relation that cannot be represented as a positive sum of independent bills; a stronger individual conductor horizon would also change the numerical ceiling.

This is a ceiling for the stated proof architecture, not an upper bound on the true common radical and not an estimate for `M(x)`. The reusable audit is: distinguish **mode count**, **universal loading over all abstract columns**, and **arithmetic restrictions on the columns actually realized** before interpreting a larger mode family as source leverage.
