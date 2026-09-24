# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Require an explicit source-to-response theorem before testing qutrit decoder capacity

VIS-367--VIS-407 reduce the intrinsic centered source-subspace problem to a scale-free qutrit observable and identify exact capacity tests for pre-fixed decoder classes. In particular, a fixed Lipschitz budget is equivalent to a uniform mass floor, while finite-basis or polynomial budgets imply explicit floors. VIS-407 also shows that regularity imposed in a singular invariant chart can be a coordinate artifact even when the intrinsic source path is regular.

VIS-408 closes the direct Wang-packet handoff. The actual final Wang packet class is infinite-dimensional and has no packet-uniform derivative, finite-basis, polynomial-degree or Lipschitz budget; its variational cosine optimizer is a scalar zero-pair kernel with no proved source-to-qutrit response dictionary. The missing theorem is therefore an intrinsic map from the Wang arithmetic source decomposition to the qutrit tangent/response object together with a target-independent complexity bound on that map. Without that map, decoder capacity is an externally chosen representation restriction rather than arithmetic evidence.

## Test gauge-invariant cross-shell structure through bandwidth-normalized Wang small values

VIS-409--VIS-411 separate faithful representation from new source structure. A one-shell Wigner portrait is equivalent to the same rank-one state; a full cross-Wigner matrix for genuinely separate shells retains already-present labelled coherence; and for projective shell data the representative phases quotient to Bargmann cycle holonomies. Pairwise interference phases are therefore not intrinsic unless the source fixes representatives, while closed-cycle products are the first phase-sensitive gauge invariants.

The subsequent Wang analysis removes the simplest way such cycle structure could become selective. Constant finite-shell sign patterns can be gauge-trivialized, so their apparent frustration does not by itself define source-rigid arithmetic holonomy. VIS-415 supplies a local sign-change certificate from the shell margin and coefficient derivative budget.

VIS-416 separates the generic spectral scale from the candidate source-dependent part. For a finite Wang shell `F_i` with frequency radius `Omega_i` and real-axis sup norm `M_i`, Bernstein's inequality gives `||F_i'||_infinity<=Omega_i M_i`. Thus the coefficient-free certified balance radius is

`beta_i(T)=a_i(T)/Omega_i`,

where `a_i(T)=|F_i(T)|/M_i`. Combining this with the VIS-415 coefficient budget gives the sharper denominator `min(L_i,Omega_i M_i)`. A shrinking **raw** balance radius can therefore be caused solely by increasing bandwidth; it is not arithmetic evidence. Amplitude rescaling also cancels from `a_i` and `beta_i`.

The live question is now a matched-control theorem for the **bandwidth-normalized small-value geometry**. Determine whether the lower envelope or distribution of `a_i(T)` (equivalently `Omega_i beta_i(T)` for the Bernstein certificate) across growing arithmetic Wang shell families differs from controls matched in `Omega_i`, shell count and a pre-specified coarse energy statistic. A source claim must survive gauge trivialization, coefficient regrouping and this bandwidth normalization. VIS-416 does not establish that normalized amplitudes are arithmetic-specific; a matched band-limited surrogate may reproduce them.
