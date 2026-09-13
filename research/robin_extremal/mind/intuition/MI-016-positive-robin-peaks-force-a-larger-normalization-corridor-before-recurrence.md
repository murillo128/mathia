# MI-016 — Positive Robin peaks force a normalization corridor larger than the intra-fan transport scale

**Evidence level:** exact for the colossally abundant recurrence geometry isolated by [RE-108](../../findings/RE-108-quantitative-robin-peaks-force-inter-block-normalization-corridors.md), combined with the false-RH quantitative block family and the intra-fan transport of RE-107. No contradiction to false RH and no RH consequence is claimed.

Let `C<D` be colossally abundant states, write `Y=log C`, `V=log D`, and suppose the Robin logarithmic excess satisfies `h(C)>0` but `h(D)<=0`. Along the CA sequence the numerator `rho(n)=sigma(n)/n` is strictly increasing, so the only way the normalized Robin ratio can return to the threshold is for the denominator `log log n` to grow enough. RE-108 converts that observation into the exact inequality

`V>Y^(1+R_C)`, where `R_C=e^(h(C))-1`,

and hence

`V-Y >= R_C Y log Y`.

Thus a quantitative positive peak carries its own mandatory **normalization corridor** before any later nonpositive CA state can occur. Under the false-RH block amplitude `R_C >= c_0 Y^(-b)`, every selected state in a compact threshold fan satisfies a corridor of order `Y^(1-b) log Y`. For successive quantitative blocks the left threshold gives

`X_(k+1)-X_k >>_J X_k^(1-b_0) log X_k`,

so the block count obeys `N_J(T)<<_J T^(b_0)/log T`.

This spacing is not itself contradictory. The normalization-only matched control, where the numerator is frozen after `C`, returns to the threshold exactly at `V=Y^(1+R_C)`, showing that the corridor exponent cannot be improved from numerator monotonicity alone. Likewise the abstract recurrence `x_(k+1)=x_k+c x_k^(1-b_0) log x_k` realizes the same packing order. Infinitely many quantitative blocks are therefore compatible with the current recurrence information.

The important scale comparison is with RE-107. The positive raw Chebyshev debt forced across one whole fan is of order `X^(1-b_1) log X`, whereas RE-108 forces a subsequent normalization corridor of order `X^(1-b_0) log X`. Since `b_0<b_1`, the uncontrolled corridor is polynomially longer. Endpoint accumulation of positive fan debts cannot therefore be treated as if successive blocks were adjacent; the source has a larger interval in which to reorganize before the next witness is seeded.

The reusable lesson is that **excursion amplitude prices recovery time, but recovery time is not recurrence rigidity**. Once a positive event forces a long normalization corridor, the next proof obligation moves from the event endpoints into the dynamics across that corridor. A contradiction must couple a source-sensitive coordinate—such as the reciprocal-Mertens phase or a Chebyshev deficit—to the descent of `h` through zero, or prove that paying the corridor destroys the capacity to regenerate the next quantitative positive witness.

**Boundary.** RE-108 uses only CA numerator monotonicity and the already-established false-RH amplitude family. It does not control primes or source phase inside the corridor, does not exclude infinitely many blocks, and does not show that the intra-fan Chebyshev debt persists until the next block. The Four-Exponentials local tie remains irrelevant to this inter-block scale law.
