# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Require an explicit source-to-response theorem before testing qutrit decoder capacity

VIS-367--VIS-407 reduce the intrinsic centered source-subspace problem to a scale-free qutrit observable and identify exact capacity tests for pre-fixed decoder classes. In particular, a fixed Lipschitz budget is equivalent to a uniform mass floor, while finite-basis or polynomial budgets imply explicit floors. VIS-407 also shows that regularity imposed in a singular invariant chart can be a coordinate artifact even when the intrinsic source path is regular.

VIS-408 closes the direct Wang-packet handoff. The actual final Wang packet class is infinite-dimensional and has no packet-uniform derivative, finite-basis, polynomial-degree or Lipschitz budget; its variational cosine optimizer is a scalar zero-pair kernel with no proved source-to-qutrit response dictionary. The missing theorem is therefore an intrinsic map from the Wang arithmetic source decomposition to the qutrit tangent/response object together with a target-independent complexity bound on that map. Without that map, decoder capacity is an externally chosen representation restriction rather than arithmetic evidence.

## Test bandwidth-normalized Wang small values against beat-aware and phase-anchored matched controls

VIS-409--VIS-411 separate faithful representation from new source structure. A one-shell Wigner portrait is equivalent to the same rank-one state; a full cross-Wigner matrix for genuinely separate shells retains already-present labelled coherence; and for projective shell data the representative phases quotient to Bargmann cycle holonomies. Pairwise interference phases are therefore not intrinsic unless the source fixes representatives, while closed-cycle products are the first phase-sensitive gauge invariants.

The subsequent Wang analysis removes the simplest way such cycle structure could become selective. Constant finite-shell sign patterns can be gauge-trivialized, so their apparent frustration does not by itself define source-rigid arithmetic holonomy. VIS-415 supplies a local sign-change certificate from the shell margin and coefficient derivative budget.

VIS-416 separates the generic spectral scale from the candidate source-dependent part. For a finite Wang shell `F_i` with frequency radius `Omega_i` and real-axis sup norm `M_i`, Bernstein's inequality gives `||F_i'||_infinity<=Omega_i M_i`. Thus the coefficient-free certified balance radius is

`beta_i(T)=a_i(T)/Omega_i`,

where `a_i(T)=|F_i(T)|/M_i`. Combining this with the VIS-415 coefficient budget gives the sharper denominator `min(L_i,Omega_i M_i)`. A shrinking **raw** balance radius can therefore be caused solely by increasing bandwidth; it is not arithmetic evidence. Amplitude rescaling also cancels from `a_i` and `beta_i`.

VIS-417 shows that bandwidth normalization is still not a complete matched control for finite-window persistence. The exact two-mode family

`F_delta(t)=1/2(cos t-cos((1-delta)t))`

has fixed maximum frequency, mode count, coefficient magnitudes, long-time mean energy and global supremum, yet its low-amplitude component through the origin has length of order `epsilon/delta`. A shrinking frequency gap therefore creates arbitrarily long quiet windows without changing those coarse summaries. Frequency-gap/beat geometry must be preserved or explicitly controlled before local persistence can be interpreted as source-specific.

VIS-418 closes the next fixed-height loophole. Even after the **entire two-mode frequency set and its gap are fixed**, translating the waveform preserves frequencies, coefficient magnitudes, long-time energy and global supremum while moving an arbitrarily long quiet interval onto or away from any prescribed observation height. Thus two different observables must be kept separate: existence of quiet windows somewhere, for which translation is irrelevant but beat geometry matters; and anomalous alignment of a distinguished arithmetic height with a quiet window, for which phase/time-origin alignment is itself part of the statistic.

The live source question is now the proposed phase-anchored self-null: for canonical finite Wang shells, compare the normalized amplitude or persistence at **pre-specified distinguished arithmetic heights** with the translation orbit of the same realized shell, using a pre-specified shift ensemble and without scanning shifts or heights after inspection. This baseline preserves the complete frequency geometry, coefficient magnitudes and beat scales and changes only alignment. For periodic shells it should average over a full period; for quasiperiodic finite sums the finite-window or Kronecker calibration must be justified rather than replaced by independent random phases without proof.

A positive result would establish only a source-sensitive phase-alignment channel, not an RH mechanism. A null result would close another visually attractive route. Any claim must retain the VIS-416 bandwidth normalization, the VIS-417 beat-scale controls and the VIS-418 distinction between translation-invariant quiet-window existence and fixed-height anchoring.
