# MI-017 — Finite rank localization can miss an orthogonal additive prime-factor coordinate

**Evidence level:** exact matched-control obstruction from [FD-138](../../findings/FD-138-clt-scale-rank-localization-still-hides-an-orthogonal-prime-color-ancestry-wall.md), using the weighted squarefree Erdos--Kac input audited there

FD-137 shows that exact multiplicative-rank conditioning exposes the moving `omega(n)` wall hidden by scale averages. FD-138 demonstrates that this repair is source-specific rather than generically coercive.

Define the additive prime-color coordinate

`D(n)=sum_(q|n) chi_4(q)`

on squarefree integers and flip the Möbius sign across the half-space `D(n)=0`, while preserving a fixed finite-rank Möbius anchor. This produces one common infinite source with positive-density coefficient disagreement.

Now restrict to a single factor-two shell and to the central CLT-scale rank window

`|omega(n)-loglog T| <= 2 sqrt(loglog T)`.

Even there, the mean prime-ancestry defect tends to zero uniformly over **all prime directions**, in both counting and harmonic normalization. The hidden transition has moved from multiplicative rank into an asymptotically independent additive prime-factor coordinate. Conditioning on a positive-Gaussian-mass rank window therefore does not prevent a source from rotating the defect into another unresolved additive direction.

The reusable obstruction is that `omega(n)` is only one low-dimensional statistic of the prime-factor vector. A coercive average cannot be justified merely by localizing physical scale and one central additive coordinate; it must explain why every source direction capable of carrying a macroscopic sign wall is controlled, or why the arithmetic construction restricts the admissible source family enough that such orthogonal walls cannot occur.

This does **not** imply that all finite families of additive coordinates fail, nor that an infinite coordinate hierarchy is required. It identifies the next proof obligation: characterize which source-native additive directions are actually admissible and find a finite or structural control that cannot be evaded by moving the interface into another direction without collapsing into exact source reconstruction.

**Boundary.** The FD-138 source is a matched obstruction to approximate ancestry-to-source coercivity. It is not asserted to satisfy the physical Mertens envelope or the repeated-square Farey endpoint.