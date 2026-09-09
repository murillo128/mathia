---
id: CLUE-zeta-half-arc-frozen-panel-negative-disposition
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-half-arc-collision-free-cue-confirmation.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-118-cue-trace-bispectrum-low-degree-orthogonality.md
  - research/visual_exploration/findings/VIS-119-wrapped-zero-block-not-haar-cue-trace-null.md
  - research/visual_exploration/findings/VIS-120-collision-free-block-triad-factorial-third-order.md
  - research/visual_exploration/findings/VIS-121-finite-cue-window-third-factorial-calibration.md
  - research/visual_exploration/SOURCES.md
---

# Should the frozen half-arc four-triad candidate receive a negative disposition?

## Observation

Independent compute execution of [issue #138](https://github.com/murillo128/mathia/issues/138), using repository inputs at `8b3bdddb0bd6521b15d5f5e2753798e91f132c17`, classified the accepted confirmation protocol as **FROZEN PANEL FAILS**. All three prescribed upper-tail probabilities exceed `0.05`. [Issue evidence](https://github.com/murillo128/mathia/issues/138#issuecomment-5602641162) preserves the reproduction code, exact-moment values, source panels, whitened residuals, and validation details.

The official [Odlyzko zeros5 table](https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros5) contained 170318 bytes, SHA-256 `250ac4ba722c6face4d07c05777376fc2b9bc021b05232e8f53c91b1eb2b7e0d`, and exactly 10000 strictly increasing decimal offsets from base `1370919909931995300000`. Its declared zero indices are `10^22+1` through `10^22+10000`; first/last offsets are `8226.68016095` and `9568.33538975`. Header and official source metadata matched this contract. Full ordinates and unfolding were evaluated at 90 decimal digits, preserving the small offsets.

Before any source ordinate was read, independent Lambert-W inversion and bisection resolved every effective size to `11`. The VIS-121 finite Toeplitz cycle-trace machinery and 34 partial matchings gave stable support rank 8 at 50 and 100 decimal digits; covariance entry differences were below `5e-41`, with eigenvalues from `2.965848731640831` to `44.43503418240983`. The full-circle specialization recovered means `(18,16,14,14)` and independently checked Hermitian/pseudo-covariance boundaries.

Exactly one null ensemble of 200000 Haar `CUE_11` matrices used PCG64 seed `20260909`, phase-corrected complex-Gaussian QR, hard arc `[0,pi)`, and compactification `psi=2 theta`. Reserve seeds were unused. All eight real means and all covariance entries passed the five-Monte-Carlo-standard-error gate before source inspection; maximum discrepancies were `2.392616` and `2.885611`. Unitarity error was below `1.89e-15`; aggregate eigenangle harmonics 1–4 were consistent with rotational uniformity. Direct ordered distinct-triple checks agreed with the algebraic panel on 30 CUE configurations and every source window.

The frozen panel order is `((1,1),(1,2),(1,3),(2,2))`. Source windows have smooth-unfolded endpoints `10^22+k ± 11/4`, left inclusive and right exclusive, and the prescribed linear compactification. Selected ranges below are offsets from index `10^22`; counts were not conditioned or fixed.

| Nominal offset k | Selected index offsets | Count | Q | Null upper-tail count / 200000 | p |
|---|---|---:|---:|---:|---:|
| 2000 | 1998–2002 | 5 | 3.15473714775976 | 130408 | 0.65204 |
| 5000 | 4999–5003 | 5 | 1.01237500656552 | 194927 | 0.974635 |
| 8000 | 7998–8002 | 5 | 3.60798509411792 | 118008 | 0.59004 |

Selected decimal offsets from the common base were:

- `k=2000`: `8494.73712981, 8494.89804787, 8494.98316458, 8495.07329614, 8495.20655779`.
- `k=5000`: `8897.23178002, 8897.33982097, 8897.54512111, 8897.69031867, 8897.79857955`.
- `k=8000`: `9299.78333865, 9299.85353684, 9299.95516342, 9300.09871799, 9300.27703033`.

The source panels below are rounded displays of the high-precision evaluations; the issue evidence retains more digits. `Z` uses coordinate order `(Re F11, Re F12, Re F13, Re F22, Im F11, Im F12, Im F13, Im F22)` and the symmetric inverse square root of the exact CUE real covariance, identically applied to null and source.

- `k=2000`: `F=(4.239871076659-0.740536724416i, 3.599664825842+0.503772838776i, -0.443462368280+1.214616547145i, 8.387722501165+0.079493903875i)`; `Z=(-0.874763819293, -0.005261458911, -0.840056439275, 1.088180194811, -0.420371680855, 0.278161465399, 0.495025933533, 0.023020468095)`.

- `k=5000`: `F=(8.440488458335+0.127004973057i, 6.330313281174-0.702476510845i, 6.150557448950+0.632662077025i, 6.565104901918-0.853893668434i)`; `Z=(0.357829793501, 0.195645202754, 0.603464776918, 0.488817361342, 0.073315068862, -0.358574470536, 0.244753096360, -0.221559973682)`.

- `k=8000`: `F=(6.222469314676+1.745735834036i, 3.947830000408+2.655580566646i, -0.461638066234+0.172008259742i, 1.448933216845-1.405351901012i)`; `Z=(-0.038958472514, -0.088035901983, -0.675637642136, -0.161259435612, 1.026437361016, 1.388008192114, 0.120377582722, -0.348704778526)`.

No source window, frequency, size, null ensemble, whitening rule, or statistic changed after source inspection. Empirical survival is exactly `#{Q_null >= Q_source}/200000`, without an add-one correction. The smallest source-window endpoint margin in unfolded units exceeded `0.107`; direct/algebraic source differences were below `9e-90`, and float panel checks differed by less than `7e-15`.

## Research question

Should the owning Research Watch resolve the accepted confirmation candidate with a negative disposition confined to this exact four-triad, three-window upper-tail gate, rather than continue it through replacement windows or a changed statistic?

## Why it may matter

The accepted clue previously left a concrete calibrated source test open. Its frozen decision now fails in every window, closing that specific empirical gate without spending additional confirmation data. It supplies a bounded disposition question, not a new arithmetic residual or a general claim about higher-order zero structure.

## Decisive test

Audit the linked execution evidence against the accepted protocol: reconstruct the source dictionary, exact finite-window centering/covariance, source selections, panel values, and prescribed upper-tail counts. If the contract is faithfully implemented, the all-three rule fails and the owner can record that precise negative outcome in the accepted clue's disposition. A material provenance, implementation, or calibration error would invalidate this handoff and require correcting the computation before disposition.

Do not reinterpret the high upper-tail probabilities as a discovered lower-tail mechanism, replace windows, or infer a new test from the observed residual directions. Any future distinct higher-order/nonlocal question needs its own independently motivated protocol and fresh evidence.

## Evidence boundary

This is numerical evidence about the fixed published decimal table, not a rigorous theorem about certified zeta zeros. Odlyzko gives probable accuracy around `10^-6`, not a guarantee. Stable arithmetic and exact finite-CUE moment formulas do not certify the underlying ordinates or prove the effective-size dictionary for this third-order observable.

Failure of this gate neither refutes all higher-order/nonlocal channels nor proves equality of the zeta and CUE point processes. The five-point counts and ordinary-size Q values do not establish a new mechanism. Known finite-height three-point arithmetic corrections, including the Bogomolny–Keating boundary already anchored in SOURCES.md, remain relevant to any future claimed residual. No arithmetic correction was fitted here, and no novelty or RH implication follows. This proposed clue asks for Research Watch disposition; it does not itself alter the accepted clue or create a canonical finding.
