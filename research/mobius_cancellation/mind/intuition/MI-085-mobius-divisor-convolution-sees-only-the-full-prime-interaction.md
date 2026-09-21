# MI-085 — Möbius divisor convolution sees only the full prime interaction

**Evidence level:** exact Boolean-lattice synthesis from [MC-437](../../findings/MC-437-mobius-convolution-extracts-full-prime-interaction.md), with the generalized-von-Mangoldt support phenomenon as the classical model case.

For a squarefree source `n=p_1...p_r`, any divisor observable `A` induces a set function

`F_n(T)=A(prod_(i in T) p_i)`, `T subset [r]`.

Then the arithmetic Möbius convolution is exactly the top Boolean finite difference:

`(mu*A)(n)=sum_(T subset [r]) (-1)^(r-|T|) F_n(T)=Delta_1...Delta_r F_n(emptyset)`.

Equivalently, if `F_n(T)=sum_(S subset T) c_n(S)` is its Boolean Möbius expansion, then `(mu*A)(n)=c_n([r])`. Thus a representation may distinguish all divisor states and still contribute zero after Möbius convolution: every component of interaction degree `<r` is annihilated. Fixed-dimensionality or large raw state capacity is irrelevant if the retained statistic has no full-order prime interaction.

This sharpens the relational-capacity branch after MC-436. The factorial number of possible prime-gap order types is only upstream capacity. To use such data through a divisor/Möbius operation, one must define the statistic on every divisor subset and compute the actual top interaction

`I_G(n)=sum_(T subset [r]) (-1)^(r-|T|) G_n(T)`.

A fixed-order sum of local, pairwise or other bounded-order interactions dies identically once `omega(n)` exceeds that order. A viable gap-order construction must either retain interaction depth growing with `omega(n)` and show `I_G(n)` is nontrivial and analytically controllable, or use a different downstream operation that does not project onto this top Boolean coefficient.

**Boundary.** This is a theorem about squarefree divisor Möbius convolution, not every arithmetic projection. Nonzero `I_G(n)` would still not imply cancellation when summing over `n`, and MC-437 does not establish that the actual gap-rank statistic has a nonzero top interaction.