# MI-020 — Centered same-source Gram formation erases coordinatewise orientation before averaging

**Evidence level:** exact pre-averaging reflection quotient from [PC-301](../../findings/PC-301-centered-window-cyclic-carriers-are-coordinatewise-reflection-blind.md)

PC-300 shows that independent cyclic sampling destroys relational information by factorizing averaged loops through one reflection-even Hankel matrix. PC-301 identifies an earlier loss that survives even when independence is removed: with the centered source window, the same-source cross-Gram carrier itself satisfies

`G_(-s)=G_s`.

Therefore every cyclic word assembled only after the map `s -> G_s` is invariant under an independent reflection of each source coordinate, pointwise and before expectation. An arbitrary correlated or reused-source law can still preserve relations among the unoriented classes `{s,-s}`, but every joint Fourier component odd under at least one coordinate reflection has already been discarded.

This separates two mechanisms. **Independence** can collapse a noncommuting hierarchy to powers of one averaged matrix, but **centered Gram formation** quotients orientation even when the source variables are maximally dependent. Correlation alone cannot restore information that was erased before the correlation-sensitive contraction is formed.

The live escape must therefore break or bypass `s -> G_s`: retain oriented frames before same-source contraction, justify an asymmetric window/observable, use a cross-level carrier not determined by the centered `G_s`, or prove that the RH-relevant relation genuinely lives on the coordinatewise sign quotient and does not need the missing orientation. Higher loop order or arbitrary source coupling inside the same centered Gram carrier cannot recover it.
