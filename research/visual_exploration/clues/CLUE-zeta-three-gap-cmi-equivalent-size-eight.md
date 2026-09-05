---
id: CLUE-visual-exploration-zeta-three-gap-cmi-equivalent-size-eight
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-three-gap-cue-deficit-arithmetic-audit.md
  - research/visual_exploration/clues/CLUE-zeta-three-gap-conditional-residual.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-020-three-gap-markov-closure-maxent-information-baseline.md
  - research/visual_exploration/findings/VIS-035-three-gap-ca-spectrum-maximal-correlation.md
  - research/visual_exploration/findings/VIS-036-three-gap-empirical-ca-pearson-null-floor.md
  - research/visual_exploration/findings/VIS-037-three-gap-lrt-pearson-local-equivalence-control.md
  - research/visual_exploration/findings/VIS-038-three-gap-lrt-pearson-cubic-residual-correction.md
  - research/visual_exploration/findings/VIS-039-three-gap-cmi-even-finite-size-expansion.md
  - research/visual_exploration/findings/VIS-040-markov-closure-fisher-normal-cmi-quadratic.md
  - research/visual_exploration/SOURCES.md
---

# Why do all three zeta windows have descriptive three-gap CMI-equivalent size eight?

## Observation

Independent compute execution of [GitHub issue #113](https://github.com/murillo128/mathia/issues/113) measured the exact finite-`N` CUE curve under one common partition. Equal-probability edges for each `B in {4,6,8}` were frozen from `300,032` independent-reference `CUE_64` gaps and then applied unchanged to every CUE size and zeta window. With `200` independent replicates of exactly `50,040` within-matrix cyclic triples per size, the primary curve was:

| `N` | mean `I_4` (sd) | mean `I_6` (sd) | mean `I_8` (sd) |
| ---: | ---: | ---: | ---: |
| 4 | `0.062416 (0.001732)` | `0.082911 (0.001819)` | `0.095787 (0.001789)` |
| 5 | `0.030917 (0.000354)` | `0.040276 (0.000364)` | `0.046926 (0.000434)` |
| 6 | `0.022502 (0.000903)` | `0.029272 (0.000994)` | `0.034553 (0.001033)` |
| 8 | `0.016945 (0.000745)` | `0.022142 (0.000864)` | `0.026544 (0.000913)` |
| 12 | `0.014032 (0.000635)` | `0.018442 (0.000746)` | `0.022458 (0.000769)` |
| 16 | `0.013219 (0.000642)` | `0.017400 (0.000728)` | `0.021282 (0.000815)` |
| 24 | `0.012618 (0.000693)` | `0.016675 (0.000766)` | `0.020485 (0.000787)` |
| 32 | `0.012423 (0.000648)` | `0.016391 (0.000752)` | `0.020242 (0.000840)` |
| 64 | `0.012225 (0.000663)` | `0.016095 (0.000750)` | `0.019883 (0.000781)` |

The three analytic-density-unfolded zeta windows gave, in increasing height order,

| window | `I_4` | `I_6` | `I_8` |
| --- | ---: | ---: | ---: |
| near `9.916e7` | `0.016322` | `0.022314` | `0.025943` |
| near `2.999e9` | `0.015931` | `0.020907` | `0.025101` |
| near `2.9999e10` | `0.016078` | `0.020957` | `0.024952` |

Every one of these nine values first enters a CUE central 95% replicate interval at `N=8`; each is below the interval at `N<=6` and above it at `N>=12`. The same descriptive bracket holds in all `36` predeclared combinations of three windows, three bin counts, two unfoldings, and `CUE_32`- versus `CUE_64`-derived reference edges. This is a CMI-equivalent size bracket only, not a fitted physical effective size.

Relative to the pair-derived nearest sizes from issue #110 (`N=4` for the lowest window and `N=5` for the other two), the zeta values remain lower by `26.61`--`53.16` replicate standard deviations. Moving along the measured CUE curve to `N=64` accounts for `90.7%`--`92.0%` of that deficit in the lowest window and `79.4%`--`81.3%` in the other two. The curve actually crosses zeta at `N=8` and continues below it: the primary zeta values sit `5.59`--`8.29` standard deviations above `CUE_64`. Under issue #113's evidence semantics, the result is therefore **finite-circle scale sufficient, with a crossing rather than an asymptotic-match qualifier**. Statistic-dependent finite-circle dependence is quantitatively sufficient as an alternative explanation of the original deficit, but neither `CUE_8` nor `CUE_64` is thereby identified as the correct zeta process.

The large-`N` diagnostic is compatible with an even-power finite-CUE correction. For `N=(12,16,24,32)`, the values of `N^2 Delta_B(N)`, where `Delta_B(N)=mean(I_B(CUE_N))-mean(I_B(CUE_64))`, were respectively `(0.260,0.255,0.226,0.203)` for `B=4`, `(0.338,0.334,0.334,0.303)` for `B=6`, and `(0.371,0.358,0.347,0.368)` for `B=8`. The expected decline induced by subtracting the still-finite `N=64` reference is visible; no unrestricted curve was fitted.

The frozen inputs were exactly byte range `0-1999999` of `zeros_99146000.dat`, `zeros_2999246000.dat`, and `zeros_29998946000.dat`, with SHA-256 values `91dd1c47b2b4d79bb222dfe79095e86aacd425f3145fa24ad7eed3e8dfc5c054`, `6df3fee8bcd18fa5785fb1254170983691c0214d73e1e52ecf70be9417dd2320`, and `ceb58e60d77c844d0f09e556946a67be02997bde601acb5911dfce6b5b16045e`. They decoded the required zero-index intervals `245754700`--`245804742`, `9061794705`--`9061844747`, and `101632223675`--`101632273717` using exact integer increments at scale `2^-101`; gap subtraction used cancellation-free `long double` arithmetic. Analytic unfolded means were within `1.6e-5` of one.

The computation used Python `3.12.3`, NumPy `2.5.2`, master seed `11309052026`, independently addressed `SeedSequence` streams, and complex-Gaussian QR Haar sampling. Across `10,782,463` checked matrices, maximum unitarity error was `2.23e-15`, maximum per-matrix unfolded-mean error was `4.45e-16`, and the eigenphase and determinant-phase resultants were `2.52e-5` and `1.27e-4`. Closure marginals agreed to `2.78e-17`, and direct KL agreed with entropy-form CMI to `3.61e-15`. First-`150` versus all-`200` replicate means shifted by at most `0.104` final standard deviations and standard deviations by at most `7.5%`. Twenty `10,000`-triple random-root replicates at each required sanity size differed from same-sample-size all-cyclic prefixes by at most `0.629` random-root replicate standard deviations. Changing the reference partition moved any CUE mean by at most `1.34e-4` and any zeta value by at most `1.17e-4`; the sensitivity normalization used a centered `1,001`-gap mean with symmetric windows truncated at the two data endpoints and moved a zeta value by at most `8.79e-5`.

No zeta table had a fitted expected count below five. Primary CUE tables had no such cells for `B=4`, at most one for `B=6`, and at most nine of `512` for `B=8`, with at most two occupied sparse cells. Fitted-positive but unobserved cells numbered at most `1`, `8`, and `27` respectively. The `eta<1` local Pearson/LRT equivalence gate was not used for any table where it failed; in particular several `B=8` tables and the small-`N` controls lie outside that local regime.

## Research question

VIS-039 and VIS-040 constrain how this crossing can be interpreted. A generic even finite-size correction in the cell law can produce an even correction in scalar CMI; at a strictly positive Markov limiting law, `P_epsilon=P+epsilon A+O(epsilon^2)` gives `I=(epsilon^2/2)||A-Pi_P A||_P^2+O(epsilon^3)`. This leading value records the norm of the normal residual and forgets its direction. Equal CMI can therefore coexist with different irreducible three-gap tensors. These population formulas are conditional on their stated smoothness/positivity assumptions and are not asserted to describe the actual zeta or CUE limiting law.

Is the common descriptive `N=8` crossing the first evidence of a statistic-dependent finite-circle transfer scale for three-gap conditional dependence, or is it an accidental balance between the CUE circle constraint, the plug-in CMI estimator, and the unresolved arithmetic/local-process correction?

More sharply: as the pair-derived effective size `N_e(T)` grows, does the CMI-equivalent bracket move systematically with it, or does a residual zeta-minus-CUE curve retain the signed `O(N_e^-3)` behavior expected from the arithmetic term? The present three windows span pair-derived sizes only from about `3.8` to `5.1`, so their common integer bracket cannot distinguish those mechanisms.

## Why it may matter

The original CUE deficit no longer needs an arithmetic correction merely to reach the observed numerical scale. Exact small-circle dependence spans the deficit and explains most of its magnitude under a partition that no longer moves with `N`. This makes transfer of the pair-derived effective size to three-gap order the immediate baseline question, while the continued descent below zeta by `N=64` preserves a smaller, signed process-mismatch question rather than declaring an exact CUE null.

A reproducible order-specific transfer law would change how finite-height zeta controls are constructed for every statistic beyond pair correlation. Conversely, failure of the `N=8` bracket to move at higher pair-derived size, together with an arithmetic-rate residual, would show that the current crossing is only a finite-window coincidence.

## Decisive test

Predeclare independent zeta windows in the already cited higher regimes near pair-derived `N_e≈7.74` and `11.30`, retain the same sample size, unfolding pair, and frozen common-partition principle, and measure the same integer CUE curve without fitting a new effective-size formula. The finite-circle-transfer interpretation survives only if the descriptive bracket moves coherently with height and the pair-matched deficit contracts as predicted by the measured curve across at least two bin counts. The arithmetic interpretation gains force if the residual to the appropriate curve instead has stable sign/shape and the parameter-free `O(N_e^-3)` scale after a mathematically valid positive arithmetic process or three-gap Janossy law is supplied.

Kill the proposed order-specific-scale reading if the bracket is unstable across those higher windows, partitions, or sample sizes, or if a matched arithmetic correction absorbs the crossing without a distinct finite-circle transfer.

Before inspecting the new windows, also freeze one direction-sensitive comparison of the residual table `P-M(P)` using a common positive reference metric and identical support conventions. A fixed set of signed contrasts or the full tensor in common whitened coordinates is suitable; selecting singular vectors separately to maximize apparent agreement is not. Determine whether the CUE size bracket selected by scalar CMI also predicts that residual geometry on independent windows. If only the scalar norms match, retain the result as a scalar calibration rather than a transferred three-gap process law. This uses the full-residual question already owned by the accepted conditional-residual clue, without opening a duplicate experiment.

Separate Monte Carlo precision of the CUE curve from uncertainty of a finite zeta window. Use independent windows and process-aware resampling/controls for the latter; overlapping triples are not independent observations. Fix sample sizes, reference partitions, sparse-cell treatment, and the joint comparison rule before the new data. Do not interpret three-bin agreement or CMI/Pearson agreement as independent confirmations, and do not infer an arithmetic `N_e^-3` law merely from a generic scalar Taylor expansion.

## Evidence boundary

This is finite-sample numerical evidence from three public-data windows and exact finite-`N` CUE simulation, not a theorem, asymptotic law, RH criterion, novelty claim, or identification of zeta with `CUE_8`. “CMI-equivalent size” is only the smallest tested integer whose finite-sample central interval contains the selected statistic; it is not a new physical estimator or effective-size formula. The same curve's `CUE_64` end lies significantly below zeta, so finite-circle scale sufficiency does not establish an exact large-`N` CUE explanation or exclude the known arithmetic correction. The arithmetic kernel was not simulated because the persisted source still does not supply the required exact positive three-gap process.

VIS-040 does not establish residual-direction agreement for these data. A discrepancy of directions would refute a stronger process-transfer interpretation while leaving a descriptive CMI crossing intact; no target result is inferred from either outcome alone.
