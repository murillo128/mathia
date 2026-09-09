---
id: CLUE-visual-exploration-zeta-half-arc-collision-free-cue-confirmation
type: research-clue
status: resolved
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-118-cue-trace-bispectrum-low-degree-orthogonality.md
  - research/visual_exploration/findings/VIS-119-wrapped-zero-block-not-haar-cue-trace-null.md
  - research/visual_exploration/findings/VIS-120-collision-free-block-triad-factorial-third-order.md
  - research/visual_exploration/findings/VIS-121-finite-cue-window-third-factorial-calibration.md
  - research/visual_exploration/SOURCES.md
---

# Does a frozen high-zero half-arc collision-free triad panel depart from matched finite CUE?

## Observation

The accepted multiscale clue has reached a source-specific boundary rather than an information-admission boundary. `VIS-118` gives an exact global third-order CUE trace channel, `VIS-119` shows that naively wrapping a finite zero block does not inherit that full-Haar null, `VIS-120` removes all repeated-index contamination, and `VIS-121` gives exact finite-`N` mean and complete second-order calibration for the resulting collision-free triads under a deterministic hard CUE arc and linear compactification.

This closes the null-side ambiguity for one explicit transformed observable. A source test can now be frozen before inspecting new high-zero values. The source choice below uses Andrew Odlyzko's official `zeros5` table, whose published metadata identify it as zeros numbered `10^22+1` through `10^22+10^4`. This clue was constructed from that metadata and the persisted Mathia/CUE mathematics; no numerical zero ordinate from `zeros5` was inspected while choosing the windows, frequencies, statistic, or decision rule.

## Research question

For three deterministic high-zero windows whose smooth unfolded length equals one half of a predeclared effective CUE size, does the collision-free third-factorial Fourier panel show a reproducible upper-tail residual relative to the exact matched finite-CUE hard-half-circle null?

The intended claim is deliberately narrow. This tests one global third-order source channel after exact window and collision calibration. It is not a test of all higher-order zero structure, and a departure from CUE would not by itself establish a new arithmetic mechanism or an RH criterion.

## Why it may matter

The visual line has repeatedly found that attractive source geometry disappears when the correct information quotient or finite-size null is imposed. The current branch is different in one useful respect: the lower-order self-collisions and the deterministic hard-window CUE mean/covariance are now known exactly, so a fresh source residual can be judged in the same transformed coordinates rather than against an imported full-circle or independent-phase baseline.

A negative result would close a concrete global third-order panel without spending further source windows post hoc. A positive result surviving all three predeclared windows would identify a source-specific residual worthy of a separate finite-height arithmetic audit, while still leaving open whether that residual is already explained by known zeta three-point corrections.

## Decisive test

Freeze the following protocol before any `zeros5` ordinate is read.

Use the smooth Riemann--von Mangoldt coordinate

`Nbar(t) = (t/(2*pi))*(log(t/(2*pi))-1) + 7/8`.

Take the three nominal zero indices

`n_1 = 10^22 + 2000`,
`n_2 = 10^22 + 5000`,
`n_3 = 10^22 + 8000`,

and define `T_j` deterministically by `Nbar(T_j)=n_j`. Use the effective finite-CUE rule already recorded in `VIS-019`,

`N_e(T) = log(T/(2*pi))/sqrt(12*Lambda)`,

with the same literature-defined arithmetic constant `Lambda` and no refitting to the present statistic. Set

`N_j = floor(N_e(T_j) + 1/2)`.

Resolving these source-independent parameters with the literature value `Lambda=1.573151071...` gives `N_1=N_2=N_3=11`. This resolution used only the nominal indices and the frozen analytic formulas, not any `zeros5` ordinate. Treat `N_j=11` as part of the frozen protocol; if an independent high-precision recomputation of the formulas does not reproduce it, stop before source inspection rather than changing the null size.

For source window `j`, select every `zeros5` ordinate `gamma` satisfying

`n_j - N_j/4 <= Nbar(gamma) < n_j + N_j/4`.

This is a deterministic hard window of smooth-unfolded length `N_j/2`; the number of selected zeros is not fixed in advance. Map each selected point to

`psi_j(gamma) = 2*pi * (Nbar(gamma) - (n_j - N_j/4)) / (N_j/2)`.

Use exactly the unordered frequency panel

`P = {(1,1), (1,2), (1,3), (2,2)}`

and for every `(a,b)` compute the collision-free triad `F_(a,b)` of `VIS-120` in the compactified coordinates. Do not add frequencies after source inspection.

The matched non-arithmetic null for every window is therefore Haar `CUE_11` restricted to the deterministic half-circle arc `[0,pi)`, followed by the same linear compactification to `[0,2*pi)`. Compute the exact complex mean, Hermitian covariance, and pseudo-covariance of the four-triad panel by `VIS-121`, convert them to the real covariance of stacked real/imaginary parts, and whiten only on its exact support. Let `Z_j` be that whitened real residual vector and freeze the primary statistic

`Q_j = ||Z_j||^2`.

The exact `VIS-121` moments determine centering and whitening; they do not determine the complete finite-CUE law of `Q_j`. Because all three predeclared windows resolve to the same `N_j=11` and use the same half-arc transformation, estimate that one remaining null law once with exactly `200000` independent Haar `CUE_11` samples using PCG64 seed `20260909`, and reuse the resulting empirical survival law for all three source windows. The previously reserved seeds `20260910` and `20260911` remain unused; do not average over them, retry with them, or select among null estimates after source inspection. This resolves the earlier seed/count ambiguity while preserving the predeclared rule of one simulation ensemble per distinct `N_j`.

Before reading any source ordinate, require the simulated panel means/covariances to agree with the exact `VIS-121` quantities within five Monte Carlo standard errors and reproduce the full-circle `VIS-120` boundary through the same exact moment implementation with arc length `2*pi`. If those checks fail, stop without source inspection.

After all null calibration is frozen and validated, inspect the official `zeros5` table exactly once. Record its source URL, SHA-256, declared index interval/base ordinate, parsed count, and monotonicity, and use sufficient precision that the large common ordinate does not destroy the small adjacent/window offsets. The published table states probable ordinate accuracy at roughly `10^-6`; treat the downloaded decimal table as the fixed finite object for the primary computation and report that source-precision boundary rather than silently upgrading it to certified zero data.

For each window report the complete four-triad panel, `Q_j`, and the empirical one-sided finite-CUE upper-tail probability `p_j = #{Q_null >= Q_j}/200000` under the single frozen null ensemble. The source-specific candidate survives this gate only if **all three** predeclared windows have `p_j <= 0.05`. This intersection rule is intentionally conservative and does not require independence between the three source windows: under valid marginal nulls its false-positive probability is at most `0.05` because the intersection is contained in each individual rejection event.

Do not replace a failed window, alter the `N_e` rule, change the unfolding, introduce a taper, enlarge the frequency panel, switch statistics, choose another Odlyzko table, or generate another CUE ensemble after seeing the residuals. A failure of the all-three rule is a negative result for this frozen panel.

If all three windows pass, do not immediately promote the residual to a new arithmetic finding. First audit whether the same windowed third-order observable is predicted by established finite-height zeta three-point/arithmetic corrections, including the Bogomolny--Keating source family already anchored in `SOURCES.md`. That arithmetic interpretation is a separate thread and must not be fitted after inspecting the confirmation residuals.

## Evidence boundary

This clue freezes an experiment; it is not evidence that the experiment will reject. No `zeros5` ordinate, source triad, source residual, or source p-value was inspected in constructing or accepting it, and no CUE simulation result is asserted here.

`VIS-121` proves the exact hard-window CUE mean/covariance machinery, not that the effective-size rule `N_e(T)` derived from known finite-height spacing comparisons transfers without correction to this third-order global observable. The three-window test therefore evaluates a predeclared source dictionary as well as the source residual. A negative result does not rule out other higher-order carriers, while a positive result remains conditional on the subsequent finite-height arithmetic audit.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/visual_exploration/findings/VIS-122-frozen-half-arc-four-triad-panel-fails-cue-upper-tail-gate]]

The frozen protocol was executed without a material contract drift and passed its required provenance, exact-moment, null-calibration, source, and implementation sanity gates. Its three prescribed upper-tail probabilities were `0.65204`, `0.974635`, and `0.59004`, so the all-three `p<=0.05` survival rule failed in every window. This resolves only the exact predeclared panel and source dictionary; it does not refute other higher-order or nonlocal zero-configuration channels.