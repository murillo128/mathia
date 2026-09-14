# MI-010 — Fixed rational anchor histories are periodic Möbius filters

**Evidence level:** exact representation classification from [FD-116](../../findings/FD-116-fixed-rational-anchor-horizon-dynamics-is-a-periodic-mobius-transform.md), using the canonical denominator-shell identity already stored in the line. This does not bound Mertens cancellation and does not cover moving or growing-denominator anchors.

For a fixed reduced rational endpoint `A=a/b`, the only absolute discrepancy coordinate left open by FD-115 has exact horizon increments

`D_Q(A)-D_(Q-1)(A)=e_Q(A)=sum_(m|Q) mu(Q/m) g_A(m)`,

where `g_A` is a zero-mean `b`-periodic sequence. Equivalently,

`D_Q(A)=A+sum_(m<=Q) f_A(m) M(floor(Q/m))`.

Thus retaining the anchor through many horizons does not create a second Farey state: it feeds one finite periodic table through the same Möbius/Mertens source already present in the denominator shells. For finitely many fixed rational anchors, the vector kernel is still periodic with period the lcm of their denominators.

The useful boundary is exact. A higher-dimensional embedding, Plücker coordinate, antisymmetric statistic or nonlinear functional of finitely many fixed anchor histories may still prove a stronger estimate for this Möbius-filtered object, but it cannot claim information independence merely from the added coordinates. A genuinely new anchor channel must make its kernel vary with scale: a moving endpoint `A_Q`, denominator or family size growing with `Q`, a global cross-cone selection law, or another source-conditioned construction not reducible to a fixed periodic filter.

This is a representation obstruction, not a smallness theorem. The filtered path may remain arithmetically difficult because it still contains Mertens cancellation; what is removed is the hypothesis that fixed rational cross-horizon anchoring supplies new Farey geometry beyond that source.
