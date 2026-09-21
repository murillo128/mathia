# MI-083 — Sparse relational asymmetry can preserve the full factor-state exponent

**Evidence level:** exact group-action synthesis from [MC-433](../../findings/MC-433-sparse-relational-asymmetry-retains-bell-capacity.md), refining the color-entropy quotient in MC-431--MC-432. Burnside/orbit bounds and graph automorphism facts are classical; the line-specific content is their consequence for exact-factor capacity.

Let `R` be any retained relation on the `r` distinct prime coordinates of a squarefree integer and `G=Aut(R)`. If `Pi(P)` is the Bell family of unordered prime-block factorizations, the surviving states after forgetting literal labels but retaining `R` are `Pi(P)/G`, so

`B_r/|G| <= Q_R <= B_r`.

With `A(R)=log(r!/|Aut(R)|)`, Bell asymptotics give

`log Q_R >= A(R) - O(r log log r)`.

Along primorials, `log N_r~r log r`; therefore `|Aut(R)|=exp(o(r log r))` already guarantees `Q_R=N_r^(1-o(1))`. More generally, `A(R)>=alpha r log r+o(r log r)` guarantees at least exponent `alpha`.

This invalidates edge count, bounded degree, or a finite relation alphabet as standalone information budgets. A tree with `r-1` edges, maximum degree three and trivial automorphism group preserves the entire Bell family. Sparse description does not imply coarse quotient: endpoint identities can individualize all prime coordinates.

The durable first-kill statistic for a general relational lift is therefore the automorphism group of the **datum that actually survives downstream**, not the number of relation incidences. Passing this capacity test is only necessary. A rigid relation may be an externally chosen near-lossless encoding of prime identity and may still disappear under Möbius projection or contribute no signed cancellation.

**Boundary.** The automorphism bound is one-sided: a small group certifies large capacity, while a large group does not alone classify the orbit count. The asymmetric-tree example is a non-arithmetic control. A viable escape still needs canonical arithmetic provenance for the symmetry breaking and a proof that the relation survives coefficient formation/projection and does analytic work.