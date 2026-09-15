# MI-017 — Even exact rank localization can miss an orthogonal additive prime-factor coordinate

**Evidence level:** exact matched-control obstruction from [FD-138](../../findings/FD-138-clt-scale-rank-localization-still-hides-an-orthogonal-prime-color-ancestry-wall.md), sharpened to every exact central rank by [FD-139](../../findings/FD-139-exact-central-rank-conditioning-still-hides-the-prime-color-wall.md), using the audited squarefree Erdos--Kac/Sathe--Selberg inputs recorded there

FD-137 shows that exact multiplicative-rank conditioning exposes the moving `omega(n)` wall hidden by scale averages. FD-138 demonstrates that this repair is source-specific rather than generically coercive.

Define the additive prime-color coordinate

`D(n)=sum_(q|n) chi_4(q)`

on squarefree integers and flip the Möbius sign across the half-space `D(n)=0`, while preserving a fixed finite-rank Möbius anchor. This produces one common infinite source with positive-density coefficient disagreement.

FD-138 already shows that inside a single factor-two shell and a positive-Gaussian-mass central rank window, the mean prime-ancestry defect tends to zero uniformly over all prime directions. FD-139 removes the remaining possibility that the width of that rank window is hiding the wall. For every exact central rank `omega(n)=m` in a fixed CLT band, the squarefree Sathe--Selberg parent cell remains of order `T/sqrt(loglog T)`, while the boundary `D in {-1,0}` occupies only order `T/loglog T`. Hence the normalized ancestry defect is still `O(1/sqrt(loglog T))` uniformly over all primes inside **each exact rank cell**.

The mechanism is geometric in source-coordinate space. Conditioning on `omega` fixes essentially the sum of the two mod-4 prime-color populations, while `D` measures their difference; the transverse fluctuation survives with square-root width. Exact localization is therefore coercive only when the source wall is measurable in the coordinate being conditioned on. FD-137 succeeded because its witness put the wall in `omega`; FD-139 shows that exactness of the conditioning itself supplies no generic coercivity.

The reusable obstruction is that a finite statistic of the prime-factor vector controls only the directions it actually resolves. A coercive ancestry law must explain why every source direction capable of carrying a macroscopic sign wall is controlled, or why the admissible arithmetic source family forbids such transverse walls. Adding a coordinate merely because it kills the previous witness is not enough; the coordinate family must be justified by the Farey/Möbius source geometry.

This does **not** imply that every finite family of additive coordinates fails, nor that an infinite coordinate hierarchy is required. It identifies the next proof obligation: determine whether a natural finite source-native coordinate family is complete enough to prevent further wall rotation without collapsing into exact source reconstruction, or construct a general matched source showing that every fixed finite family leaves another transverse additive direction.

**Boundary.** The FD-138/FD-139 source is a matched obstruction to approximate ancestry-to-source coercivity. It is not asserted to satisfy the physical Mertens envelope or the repeated-square Farey endpoint, and no general impossibility theorem for all finite source-coordinate families has been proved.