---
id: CLUE-visual-exploration-zeta-three-gap-cue-deficit-arithmetic-audit
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-three-gap-conditional-residual.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-020-three-gap-markov-closure-maxent-information-baseline.md
  - research/visual_exploration/SOURCES.md
---

# Does the high-zeta three-gap CMI deficit come from the arithmetic correction or failure of effective-size transfer?

## Observation

Independent compute execution of [GitHub issue #110](https://github.com/murillo128/mathia/issues/110) found a reproducible **deficit**, rather than an excess, in the binned conditional mutual information of high zeta gaps relative to pair-correlation-matched finite CUE. Three disjoint LMFDB/Platt windows of `50,042` consecutive gaps (`50,040` triples) were taken near heights `9.916e7`, `2.999e9`, and `2.9999e10`, with effective sizes `N_e=3.8147, 4.5994, 5.1294` and nearest integer CUE sizes `4, 5, 5`. For the primary analytic-density unfolding:

| height | `B` | zeta `I_B` | matched CUE mean (sd) | `Z_B` |
| --- | ---: | ---: | ---: | ---: |
| `9.916e7` | 4 | `0.016425` | `0.062420 (0.001716)` | `-26.80` |
|  | 6 | `0.022240` | `0.082686 (0.001805)` | `-33.48` |
|  | 8 | `0.026098` | `0.095376 (0.001854)` | `-37.36` |
| `2.999e9` | 4 | `0.015777` | `0.030856 (0.000352)` | `-42.85` |
|  | 6 | `0.020901` | `0.040130 (0.000372)` | `-51.62` |
|  | 8 | `0.025044` | `0.046670 (0.000439)` | `-49.23` |
| `2.9999e10` | 4 | `0.015996` | `0.030863 (0.000376)` | `-39.55` |
|  | 6 | `0.020803` | `0.040157 (0.000399)` | `-48.56` |
|  | 8 | `0.024896` | `0.046719 (0.000470)` | `-46.42` |

Every zeta value lay below all `600` matched CUE replicates, giving the minimum plus-one two-sided empirical probability `2/601=0.00333`. A predeclared centered `1,001`-gap rolling-mean unfolding changed primary `I_B` by at most `1.15e-4` and retained every sign. Repeating at both neighboring integer sizes retained a negative standardized difference in every cell of the fixed matrix; even the least extreme comparison was `Z=-7.34`. The zeta-minus-CUE residual-tensor correlations between height windows were `0.92`--`0.95` for `B=4`, `0.74`--`0.86` for `B=6`, and `0.58`--`0.72` for `B=8`; analytic-versus-local-unfolding correlations within a window were `0.997`--`1.000`.

The computation used independent CUE-only equal-probability bin references of `300,000` gaps and separate `600`-replicate streams for every window/size pair, complex-Gaussian QR Haar sampling, circular within-matrix triples, and master seed `11009052026`. Each replicate constructed its own empirical pair-marginal-preserving closure. CUE means shifted by at most `0.045` final standard deviations between `500` and `600` replicates; standard deviations changed by at most `3.7%`. Closure marginals agreed to `4.2e-17`, direct KL and entropy CMI to `3.8e-15`, aggregate phase resultants were below `6.6e-4`, and no primary zeta occupied cell had fitted expected count below five. A separate seed-`987654321` check using one uniformly random rooted triple from each of `50,040` independent CUE matrices, repeated `12` times per primary comparison, agreed with the all-cyclic-triple CUE means to within `5.5e-4` (below one random-root replicate standard deviation); QR unitarity held to `1.3e-15`.

Inputs were LMFDB byte ranges `0-1999999` of `zeros_99146000.dat`, `zeros_2999246000.dat`, and `zeros_29998946000.dat`, decoding zero indices `245754700`--`245804742`, `9061794705`--`9061844747`, and `101632223675`--`101632273717`. Their partial SHA-256 hashes were respectively `91dd1c47b2b4d79bb222dfe79095e86aacd425f3145fa24ad7eed3e8dfc5c054`, `6df3fee8bcd18fa5785fb1254170983691c0214d73e1e52ecf70be9417dd2320`, and `ceb58e60d77c844d0f09e556946a67be02997bde601acb5911dfce6b5b16045e`. Arithmetic constants `Lambda=1.573151071` and `Q=2.315846384` came from Nishigaki's arXiv `2507.10193v1`; computation used Python `3.12.3` and NumPy `2.5.2` in binary64, with Platt increments decoded at scale `2^-101`. A cancellation-free long-double reconstruction of raw gaps changed every reported `I_B` by at most `1.21e-5`.

## Research question

Does Nishigaki's known `O(N_e^-3)` arithmetic kernel term quantitatively remove this signed three-gap CMI/tensor deficit, or does the pair-correlation-calibrated effective size fail to transfer to three-gap order because the global finite-circle constraint of small `CUE_N` contributes dependence not present in a local zeta window?

## Why it may matter

The accepted parent clue asked whether a lower-order-marginal-preserving three-gap residual separates zeta from finite-size CUE. The observed separation is much larger and has the opposite sign from a naive “extra zeta dependence” story. Resolving its origin is therefore a baseline-validity question: until the arithmetic correction or an order-appropriate effective-size construction explains the CUE excess, the current finite-CUE comparison cannot support an arithmetic-specific higher-order claim. Conversely, a parameter-free arithmetic correction that captures both the scalar deficit and its signed tensor shape would isolate a precise finite-height effect beyond the pair-marginal closure.

## Decisive test

Derive from the cited finite-height kernel expansion an explicitly positive, numerically evaluable point process or three-gap Janossy law through the applicable arithmetic order, without fitting to these zeta residuals. Apply the same frozen `B={4,6,8}` partitions and both unfoldings to its matched finite-sample replicates. The arithmetic explanation survives only if it accounts for the sign and scale of all three `I_B` deficits and the pre-existing tensor shape across at least two heights. Then repeat at independently available windows near the literature's `N_e≈7.74` and `11.30`: arithmetic scaling should predict how the deficit decays, whereas a small-`N` circular-constraint mismatch should follow a different effective-size dependence.

## Evidence boundary

This is reproducible numerical evidence from three finite public-data windows, not a theorem, RH criterion, novelty claim, or arithmetic-specific discovery. The windows stop near height `3e10`, below the much higher Odlyzko regimes used in the cited literature. The directly cited arithmetic result supplies an asymptotic translation-invariant kernel through `O(N_e^-3)`, but not an exact positive finite sampler or three-gap Janossy distribution; inventing a global completion of that truncated kernel was outside issue #110 and no arithmetic-corrected baseline was evaluated. The very small effective CUE sizes make the finite circle's fixed total spacing a serious alternative explanation. The empirical probability resolution is limited to `2/601`, and residual-shape correlations are diagnostics rather than additional multiplicity-free tests. The result remains an audit clue until Research Watch resolves the arithmetic/process construction and prior art.

## Research disposition

Accepted as a baseline-validity audit, not as evidence that the deficit is arithmetic. The published Nishigaki analysis sharpens the distinction: `N_e(T)` is fixed by matching the pair correlation; the displayed Riemann-zero kernel agrees with finite CUE through `O(N_e^-2)` and adds the prime-sum `O(N_e^-3)` term; and the paper empirically verifies the `O(N_e^-2)` transfer to the joint law of **two** consecutive spacings at very high `N_e≈11.30`. The checked literature does not establish that this pair-derived finite-CUE surrogate remains correct for three-gap/four-point Janossy statistics at the much smaller `N_e≈3.8–5.1` used here, while general Janossy-density machinery supplies a way to formulate such higher-order laws but does not remove that modeling question.

The live question is therefore narrower than “zeta has extra three-gap dependence.” First separate two competing baseline failures: an exact small-`N` finite-circle effect in `CUE_N` that makes the pair-derived effective-size surrogate inappropriate at three-gap order, versus the arithmetic `O(N_e^-3)` correction represented by a mathematically valid positive local process. Do not simulate a truncated asymptotic kernel as though it were a probability model unless positivity, normalization, and the required Janossy law are established. The higher effective-size windows near `N_e≈7.74` and `11.30` remain the clean scaling control because the two explanations predict materially different decay behavior.