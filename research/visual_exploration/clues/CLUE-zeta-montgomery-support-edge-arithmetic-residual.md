---
id: CLUE-visual-exploration-zeta-montgomery-support-edge-arithmetic-residual
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-122-frozen-half-arc-four-triad-panel-fails-cue-upper-tail-gate.md
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond finite CUE?

## Observation

`VIS-122` closes the frozen half-arc four-triad confirmation panel and explicitly requires any new zero-configuration thread to begin from an independent mathematical reason for a different carrier, source dictionary, statistic, or arithmetic correction. Montgomery's pair-correlation transform supplies such a reason without reusing the failed third-order panel.

For zeros `1/2+i gamma` up to height `T`, Montgomery introduced the weighted Fourier statistic

`F_T(alpha) = (T/(2 pi) log T)^(-1) sum_(gamma,gamma'<=T) T^(i alpha (gamma-gamma')) w(gamma-gamma')`,

with the classical weight `w(u)=4/(4+u^2)`. Under RH, Montgomery proved the familiar asymptotic in the range `|alpha|<=1` and conjectured `F_T(alpha)=1+o(1)` for bounded `|alpha|>=1`; Goldston--Gonek--Özlük--Snyder, *Proceedings of the London Mathematical Society* 80 (2000), 31--49, DOI `10.1112/S0024611500012211`, is a standard precise reference for this support boundary and its continuation problem.

The location `|alpha|=1` is visually attractive but **is not by itself an arithmetic signal**. The CUE/GUE spectral form factor has the same universal ramp-to-plateau transition after the standard normalization: finite CUE satisfies the exact trace identity `E|Tr U^k|^2=min(|k|,N)`. A plot that merely reproduces a ramp for `|alpha|<1` and a plateau beyond it would therefore redraw the random-matrix null rather than expose new zeta structure.

The mathematically interesting object is the **finite-height residual around that support edge after the matched finite-CUE contribution has been removed**. This residual has an independent arithmetic motivation. Goldston--Montgomery type equivalences connect quantitative pair-correlation errors with mean-square prime counts in short intervals; Languasco--Perelli--Zaccagnini, *Journal of Mathematical Analysis and Applications* 394 (2012), 761--771, DOI `10.1016/j.jmaa.2012.04.058`, makes such error relations explicit. Bogomolny--Keating finite-height correlation formulas likewise separate the universal random-matrix contribution from lower-order prime-dependent terms, and Keating--Smith, *Journal of Physics A* 52 (2019), 365201, DOI `10.1088/1751-8121/ab3521`, shows heuristically that sufficiently detailed lower-order pair-correlation information can recover Hardy--Littlewood-type prime-pair correlations.

This prior art changes the visual question. The candidate is not a new pair-correlation formula and not the classical support edge. It is whether one can define a **predeclared, finite-height, matched-null edge residual** whose geometry is stable enough to serve as a discriminating visual carrier. A natural scale to audit is

`u = (alpha-1) log T`,

because then `T^alpha/T = exp(u)`: an `O(1/log T)` displacement in `alpha` corresponds to an `O(1)` multiplicative displacement of the prime-side Fourier scale around the transition `X=T`. This scaling is only a candidate coordinate at this stage; it is not asserted to be the unique or correct finite-height edge scaling.

## Research question

Can a finite-height version of Montgomery's pair-correlation transform be centered by an exact or explicitly calibrated finite-CUE baseline so that a fixed, predeclared window around `alpha=1` exposes a reproducible residual which is not explained by the universal ramp/plateau, finite-window geometry, smoothing, diagonal terms, or known generic finite-size corrections?

More specifically, is there a low-dimensional edge statistic built from values such as

`R_T(u) = F_T(1+u/log T) - F_CUE,T(1+u/log T)`

at a fixed finite set of predeclared `u` values, or from an equivalent smoothed edge profile, whose sign/shape/scale is predicted independently by the arithmetic lower-order terms and then survives on untouched high-zero material? Here `F_CUE,T` is only notation for the **matched finite-size null that still has to be derived precisely** for the chosen zero window, smoothing kernel, unfolding, and effective matrix size; replacing it by the limiting `min(alpha,1)` curve would not pass the test.

## Why it may matter

This route is independent of the failed `VIS-122` third-order panel. It returns to a two-point statistic, but for a source-driven reason: the Fourier support boundary is where the classical zero-pair transform changes regime and where the corresponding prime-side scale crosses `X=T`. The random-matrix part of that transition is already known, so a useful visualization would have to show only what remains after that structure is quantitatively removed.

A reproducible residual would provide a visually compact bridge between zero geometry and the prime-side information already known to live in pair-correlation error terms. Even then it would most likely be a new **organization or diagnostic of known arithmetic corrections**, not a new pair-correlation theorem. A null result would also be valuable: if every reasonable predeclared edge profile is absorbed by the exact finite-CUE/window baseline or by already-known finite-height corrections, then the visually tempting `alpha=1` transition should be treated as another deterministic/random-matrix control rather than an open visual carrier.

## Decisive test

Before reading confirmation zero values, choose one exact statistic family. Fix the zero-height regime and source windows, the unfolding convention, the pair weight or smoothing kernel, the finite set or compact interval of edge coordinates, the normalization, the treatment of the diagonal `gamma=gamma'` term, and one low-dimensional decision statistic. The statistic should be motivated from the arithmetic lower-order formula or from a proved edge expansion, not selected after seeing which visual feature is largest.

Derive or calibrate the **matched finite-CUE null at the same finite geometry**. In the discrete trace model the exact identity `E|Tr U^k|^2=min(k,N)` supplies the starting form-factor control, but a zeta statistic with continuous `alpha`, a finite height/window, pair weighting, smoothing, and unfolding is not automatically identical to that integer-trace formula. Establish the precise dictionary or construct a finite-CUE simulation/analytic ensemble that reproduces those choices. Include the covariance between all predeclared edge coordinates and whiten or otherwise combine them according to the frozen rule. Do not compare a finite zeta profile only to the infinite-`N` ramp/plateau.

Audit the proposed `u=(alpha-1)log T` coordinate rather than assuming it. Determine whether known pair-correlation/prime-side formulas actually predict a stable nonzero profile on that scale, a different scale, or no universal edge profile at all. If the leading arithmetic correction is known, subtract or predict it explicitly and state whether the target is reproduction, a residual beyond it, or a new invariant of its shape. Existing Bogomolny--Keating-type finite-height corrections must be treated as prior art, not rediscovered as a visual anomaly.

Only after the null, scale, and statistic are frozen should the source test use high-zero material not previously inspected for this exact design. Record source provenance and the fresh-evidence boundary. Replicate across several predeclared windows or heights and use a combined rule fixed in advance. Reasonable alternate smoothing kernels or nearby predeclared edge grids may be used as robustness checks only when their role is specified before source inspection; they are not additional opportunities to search for significance.

Kill the direction if the apparent edge residual is reproduced by the matched finite-CUE ensemble, disappears after exact window/smoothing/diagonal accounting, changes qualitatively under the predeclared reasonable representations, or reduces entirely to a known finite-height arithmetic correction with no residual question. Also kill any claim of a special `u`-profile if the literature/derivation shows that the `1/log T` edge scaling has no stable mathematical meaning for the chosen transform.

Support continued investigation only if a predeclared residual survives the matched finite-CUE control on fresh source material and its sign or scale agrees with an arithmetic prediction made independently of the confirmation data. A merely attractive ramp, cusp, plateau, heat map, or edge sharpening does not pass.

## Evidence boundary

Montgomery pair correlation, the `|alpha|=1` support boundary, CUE/GUE pair statistics, the finite-CUE trace form factor, prime-short-interval equivalences, and lower-order arithmetic corrections to zero correlations are established prior art. This clue claims none of them as new.

The proposed edge coordinate `u=(alpha-1)log T`, the exact finite-window CUE dictionary for the intended visualization, the low-dimensional residual statistic, and the existence of any reproducible source-specific residual are **not established**. No numerical zero test has been performed for this clue, no confirmation window has been selected after source inspection, and no positive anomaly is claimed.

Even a successful test would not prove RH, Montgomery's full pair-correlation conjecture, the Hardy--Littlewood prime-pair conjecture, or a new zero-correlation theorem. The purpose of the clue is narrower: determine whether the classical support edge can be converted from a visually obvious universal transition into a rigorously controlled finite-height residual carrier, or whether exact finite-size/random-matrix and known arithmetic corrections exhaust what the visualization can show.