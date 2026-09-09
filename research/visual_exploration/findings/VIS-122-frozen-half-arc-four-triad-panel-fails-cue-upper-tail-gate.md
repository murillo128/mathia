# VIS-122 — frozen half-arc four-triad panel fails its CUE upper-tail gate

## Claim

The predeclared high-zero confirmation protocol in `CLUE-zeta-half-arc-collision-free-cue-confirmation.md` fails its own primary decision rule on the fixed Odlyzko `zeros5` table.

The protocol froze three nominal windows near zero indices `10^22+2000`, `10^22+5000`, and `10^22+8000`, effective CUE size `N=11`, the hard half-circle source/null dictionary, the collision-free panel

`P={(1,1),(1,2),(1,3),(2,2)}`,

the exact `VIS-121` finite-window centering/whitening, the statistic `Q=||Z||^2`, one `200000`-sample Haar `CUE_11` null ensemble with PCG64 seed `20260909`, and the one-sided empirical upper-tail rule

`p = #{Q_null >= Q_source}/200000`.

The candidate was declared to survive only if **all three** predeclared windows had `p<=0.05`. The observed values were

| Nominal index | Selected index offsets from `10^22` | Count | `Q` | Upper-tail count / `200000` | `p` |
|---|---|---:|---:|---:|---:|
| `10^22+2000` | `1998–2002` | 5 | `3.15473714775976` | `130408` | `0.65204` |
| `10^22+5000` | `4999–5003` | 5 | `1.01237500656552` | `194927` | `0.974635` |
| `10^22+8000` | `7998–8002` | 5 | `3.60798509411792` | `118008` | `0.59004` |

All three values fail the frozen upper-tail threshold. Therefore this exact four-triad, three-window, half-arc CUE confirmation panel supplies **no positive source-specific residual under its predeclared gate**.

**Evidence/status:** `COMPUTATIONAL-EVIDENCE + PREDECLARED-FRESH-CONFIRMATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

This is a bounded finite-table negative result. It does not refute higher-order or nonlocal zeta-zero structure, prove equality with CUE, certify the underlying zero ordinates, or establish any RH implication.

## 1. The decision rule was frozen before source inspection

The accepted clue specified the source dictionary and decision rule before any `zeros5` ordinate was read. Smooth unfolding used

`Nbar(t)=(t/(2*pi))*(log(t/(2*pi))-1)+7/8`,

with effective finite-CUE size

`N_e(T)=log(T/(2*pi))/sqrt(12*Lambda)`

and the literature value `Lambda=1.573151071...`. The three nominal centers were defined from their indices, not from observed zero positions. Independent Lambert-W inversion and bisection at 90 decimal digits reproduced the frozen integer size `N=11` for all three windows before source access.

Each source window then selected all ordinates whose smooth unfolded coordinate lay in the prescribed interval of length `N/2`; the selected count was allowed to vary and was not conditioned after inspection. The selected points were linearly compactified to a full circle, transformed through the `VIS-120` collision-free third-factorial triads, centered and whitened by the exact hard-half-arc CUE moments of `VIS-121`, and reduced to the single frozen radial statistic `Q`.

The compute evidence records no change after source inspection to the windows, panel, effective size, compactification, whitening rule, statistic, null ensemble, seed, or estimator. Reserve seeds were not used. The resulting classification is therefore the mechanical consequence of the accepted clue's rule rather than a post-hoc choice.

## 2. Null and source sanity gates passed before classification

The exact finite-window CUE calibration was evaluated through the `VIS-121` Toeplitz/permutation-cycle machinery, including all 34 cross-identification patterns required for the four-triad second moments. Independent 50- and 100-decimal-digit interval evaluations agreed to below `5e-41` per covariance entry, the real covariance had support rank 8, and the full-circle specialization recovered the expected low-degree Haar means `(18,16,14,14)` together with independently checked Hermitian and pseudo-covariance boundaries.

The one allowed Monte Carlo ensemble used `200000` Haar `U(11)` matrices generated from phase-corrected complex-Gaussian QR with PCG64 seed `20260909`. Maximum reported unitarity error was `1.89e-15`. All eight simulated real means and all 64 covariance entries passed the predeclared five-Monte-Carlo-standard-error comparison against the exact quantities; the largest standardized discrepancies were `2.392616` for means and `2.885611` for covariance entries. Aggregate eigenangle harmonics 1–4 were also consistent with the expected rotational uniformity at the reported Monte Carlo precision.

Direct ordered-distinct-triple evaluation agreed with the algebraic collision-free formula on 30 CUE configurations and on all three source windows. The maximum CUE discrepancy was `1.89e-14`, while arbitrary-precision source discrepancies were below `9e-90`. These checks matter because the negative classification is useful only if the exact transformed statistic and its matched null were implemented faithfully.

## 3. Source provenance and finite-data boundary

The source was Andrew Odlyzko's official `zeros5` table, downloaded only after the null-side gates had passed. The execution recorded URL

`https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros5`,

byte count `170318`, SHA-256

`250ac4ba722c6face4d07c05777376fc2b9bc021b05232e8f53c91b1eb2b7e0d`,

base ordinate `1370919909931995300000`, declared index range `10^22+1` through `10^22+10000`, parsed count `10000`, and strict monotonicity. The downloaded decimal table was evaluated at 90 decimal digits so the large common ordinate did not destroy the small local offsets.

Odlyzko describes the tabulated ordinates as having probable accuracy around `10^-6`, not as formally certified zeros. This finding therefore treats the downloaded decimal table as the fixed empirical object that was tested. The numerical stability checks do not upgrade its external source guarantee.

Complete reproducibility evidence, including the selected decimal offsets, source panels, whitened residual vectors, exact moments, Monte Carlo calibration, package versions, and validation diagnostics, is preserved in GitHub issue `#138`, especially comment:

`https://github.com/murillo128/mathia/issues/138#issuecomment-5602641162`.

## 4. What the failure does and does not close

The negative result closes the **specific frozen candidate** represented by this source dictionary and statistic. There is no upper-tail excess in any of the three predeclared windows; indeed the observed `Q` values lie well inside the empirical finite-CUE null distribution. The correct disposition is therefore not to replace a window, enlarge the panel, switch to a directional statistic, reinterpret the large p-values as a lower-tail discovery, condition on the observed count, or spend the reserved seeds looking for a more favorable calibration.

Those changes would define new experiments after seeing the confirmation data. They cannot rescue the frozen candidate without sacrificing the fresh-data interpretation that made this test informative.

The result is much narrower than a statement about the zeta zero process. `VIS-019` already warns that finite-height zeta spacing statistics contain known finite-size and arithmetic corrections. `VIS-120` and `VIS-121` isolate and calibrate one particular collision-free third-factorial channel, not all third-order information. Failure here does not rule out another higher-order/nonlocal carrier, another independently motivated source dictionary, a statistic sensitive to a different information quotient, or an arithmetic correction that was never represented by this four-coordinate panel.

## 5. Prior-art and novelty assessment

The random-matrix and finite-height boundaries are already anchored in `research/visual_exploration/SOURCES.md`. Forrester–Mays and Bornemann–Forrester–Mays establish finite-size circular-ensemble comparisons for zeta-zero spacings; Nishigaki's 2026 analysis records the effective-size rule used by `VIS-019` and shows that finite-height arithmetic effects can survive beyond the leading CUE correction. Bogomolny–Keating provides an explicit prior-art boundary for three-point zeta statistics with universal and arithmetic contributions.

The collision-free factorial decomposition and deterministic hard-window CUE calibration are likewise bounded by the classical point-process/DPP machinery recorded in `VIS-120`–`VIS-121`. No general random-matrix, zeta-zero, factorial-moment, or statistical-testing result is claimed as new here.

The Mathia-specific contribution is only the outcome of a frozen experiment designed from those persisted controls: after exact collision removal and matched finite-window CUE calibration, this particular predeclared four-triad panel does not show the required fresh high-zero upper-tail departure.

## Boundary and falsification

This finding depends on the faithful execution of the accepted protocol and the preserved issue evidence. A material error in source provenance, index mapping, unfolding, effective-size resolution, exact `VIS-121` moments, whitening support, triad implementation, null generation, or the reported upper-tail counts would invalidate the disposition and require correction rather than reinterpretation.

The effective-size transfer itself remains an assumed source dictionary for this third-order observable; it is motivated by finite-height RMT literature but is not proved here to be the unique or exact third-order CUE correspondence. The source ordinates retain Odlyzko's stated probable-accuracy boundary. The empirical p-values are finite Monte Carlo tail frequencies under the one frozen ensemble, not exact symbolic tail probabilities.

None of those limitations reverses the protocol-level conclusion: **conditional on the protocol exactly as accepted and executed, the all-three upper-tail survival rule fails decisively because every reported p-value is above `0.05`.**

## Research consequence

Resolve `CLUE-zeta-half-arc-collision-free-cue-confirmation.md` with outcome `refuted`: the candidate it froze did not survive its own confirmation gate. Resolve `CLUE-zeta-half-arc-frozen-panel-negative-disposition.md` with outcome `supported`: its proposed bounded negative disposition survives independent Research Watch audit and is materialized by this finding.

Future work should not iterate post-hoc variants of the same failed panel on the already inspected confirmation windows. A new zero-configuration thread is justified only by a genuinely independent mathematical reason for a different statistic, source dictionary, information carrier, or control, with its own predeclared falsification gate and fresh evidence boundary.