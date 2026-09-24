# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Require an explicit source-to-response theorem before testing qutrit decoder capacity

VIS-367--VIS-407 reduce the intrinsic centered source-subspace problem to a scale-free qutrit observable and identify exact capacity tests for pre-fixed decoder classes. In particular, a fixed Lipschitz budget is equivalent to a uniform mass floor, while finite-basis or polynomial budgets imply explicit floors. VIS-407 also shows that regularity imposed in a singular invariant chart can be a coordinate artifact even when the intrinsic source path is regular.

VIS-408 closes the direct Wang-packet handoff. The actual final Wang packet class is infinite-dimensional and has no packet-uniform derivative, finite-basis, polynomial-degree or Lipschitz budget; its variational cosine optimizer is a scalar zero-pair kernel with no proved source-to-qutrit response dictionary. The missing theorem is therefore an intrinsic map from the Wang arithmetic source decomposition to the qutrit tangent/response object together with a target-independent complexity bound on that map. Without that map, decoder capacity is an externally chosen representation restriction rather than arithmetic evidence.

## Test bandwidth-normalized Wang small values against the exact fixed-shell translation self-null

VIS-409--VIS-411 separate faithful representation from new source structure. A one-shell Wigner portrait is equivalent to the same rank-one state; a full cross-Wigner matrix for genuinely separate shells retains already-present labelled coherence; and for projective shell data the representative phases quotient to Bargmann cycle holonomies. Pairwise interference phases are therefore not intrinsic unless the source fixes representatives, while closed-cycle products are the first phase-sensitive gauge invariants.

The subsequent Wang analysis removes the simplest way such cycle structure could become selective. Constant finite-shell sign patterns can be gauge-trivialized, so their apparent frustration does not by itself define source-rigid arithmetic holonomy. VIS-415 supplies a local sign-change certificate from the shell margin and coefficient derivative budget.

VIS-416 separates the generic spectral scale from the candidate source-dependent part. For a finite Wang shell `F_i` with frequency radius `Omega_i` and real-axis sup norm `M_i`, Bernstein's inequality gives `||F_i'||_infinity<=Omega_i M_i`. Thus the coefficient-free certified balance radius is

`beta_i(T)=a_i(T)/Omega_i`,

where `a_i(T)=|F_i(T)|/M_i`. Combining this with the VIS-415 coefficient budget gives the sharper denominator `min(L_i,Omega_i M_i)`. A shrinking **raw** balance radius can therefore be caused solely by increasing bandwidth; it is not arithmetic evidence. Amplitude rescaling also cancels from `a_i` and `beta_i`.

VIS-417 shows that bandwidth normalization is still not a complete matched control for finite-window persistence. The exact two-mode family

`F_delta(t)=1/2(cos t-cos((1-delta)t))`

has fixed maximum frequency, mode count, coefficient magnitudes, long-time mean energy and global supremum, yet its low-amplitude component through the origin has length of order `epsilon/delta`. A shrinking frequency gap therefore creates arbitrarily long quiet windows without changing those coarse summaries. Frequency-gap/beat geometry must be preserved or explicitly controlled before local persistence can be interpreted as source-specific.

VIS-418 closes the next fixed-height loophole. Even after the **entire two-mode frequency set and its gap are fixed**, translating the waveform preserves frequencies, coefficient magnitudes, long-time energy and global supremum while moving an arbitrarily long quiet interval onto or away from any prescribed observation height. Thus two different observables must be kept separate: existence of quiet windows somewhere, for which translation is irrelevant but beat geometry matters; and anomalous alignment of a distinguished arithmetic height with a quiet window, for which phase/time-origin alignment is itself part of the statistic.

VIS-419 resolves the fixed-shell calibration problem exactly. Every canonical finite Wang shell is a Laurent character polynomial on the torus of its **base-prime phases**, and long translation of that same realized shell is exactly the Haar pushforward of those prime phases for bounded continuous fixed-shell observables. The ratio-mode phases retain their induced character dependencies; independently randomizing every ratio frequency is generally a different and invalid null. Normalized amplitude and fixed-radius continuous persistence statistics therefore have a canonical asymptotic translation self-null for each fixed shell, independent of starting height.

VIS-420 supplies the missing first quantitative layer for finite trigonometric observables. If `G(z)=sum_m c_m z^m` and the translation frequencies are `nu_m=sum_p m_p log p`, then averaging over a window of length `V` differs from the Haar coefficient by the exact sinc-weighted nonzero-character sum. In particular the error is bounded by

`sum_(m!=0) |c_m| min(1,2/(V|nu_m|))`,

and a finite-shell energy estimate has the corresponding pairwise cost `V^(-1) sum_(j!=k)|B_jB_k|/|lambda_j-lambda_k|`. Finite-window calibration is therefore controlled by the actual small divisors of the retained base-prime character lattice, not by mode count, outer bandwidth or coefficient norm alone. VIS-420 is a fixed finite-support estimate; it does not provide a shell-uniform Diophantine lower bound as the character support grows.

The live source question is now whether **pre-specified distinguished arithmetic heights are atypical under that exact base-prime Haar self-null**, after the VIS-416 bandwidth normalization and VIS-417 beat-scale controls, and whether the required calibration remains quantitative in the physical growing-shell regime. For fixed finite observables VIS-420 makes the finite-window tariff explicit. A jointly growing shell/height theorem must now control both coefficient mass and the smallest relevant linear forms in prime logarithms strongly enough that the sinc remainder vanishes uniformly. Direct Haar tests avoid that translation-calibration step but still need a source theorem showing an arithmetic-height anomaly under the canonical base-prime law.

A positive result would establish only a source-sensitive phase-alignment channel, not an RH mechanism. A null result would close another visually attractive route. Any claim must preserve the actual shell character dependencies and distinguish exact fixed-shell Haar calibration from the much stronger jointly growing shell/height limit.
