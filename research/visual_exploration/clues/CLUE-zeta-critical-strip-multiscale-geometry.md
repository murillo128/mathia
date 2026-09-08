---
id: CLUE-visual-exploration-zeta-critical-strip-multiscale-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-008-infinitesimal-zero-portraits-universal.md
  - research/visual_exploration/findings/VIS-013-zero-free-shells-poisson-determined.md
  - research/visual_exploration/findings/VIS-014-circular-zero-entry-logmeans-radial-only.md
  - research/visual_exploration/findings/VIS-015-nonzero-shell-modes-poisson-jensen-zero-sources.md
  - research/visual_exploration/findings/VIS-016-phase-modulus-boundary-uniqueness.md
  - research/visual_exploration/findings/VIS-017-overlap-connectivity-collapses-local-phase-freedom.md
  - research/visual_exploration/findings/VIS-018-phase-winding-is-divisor-count.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-092-one-dimensional-rips-persistence-gap-multiset.md
  - research/visual_exploration/findings/VIS-093-sliding-window-persistence-forgets-window-order.md
  - research/visual_exploration/findings/VIS-094-static-temporal-edge-delay-graphs-add-one-block-order.md
  - research/visual_exploration/findings/VIS-095-step-two-delay-signature-local-block-boundary.md
  - research/visual_exploration/findings/VIS-096-delay-signatures-level-three-planar-four-local-edge-boundary.md
  - research/visual_exploration/findings/VIS-097-delay-signature-level-four-cycle-order.md
  - research/visual_exploration/findings/VIS-098-exact-local-block-null-degenerate-on-distinct-windows.md
  - research/visual_exploration/findings/VIS-099-quantized-local-block-markov-type-null.md
  - research/visual_exploration/findings/VIS-100-whittle-quantized-type-class-count-sampler.md
  - research/visual_exploration/findings/VIS-101-binary-median-gap-level-four-null.md
  - research/visual_exploration/findings/VIS-102-three-bin-training-quantile-gap-level-four-null.md
  - research/visual_exploration/findings/VIS-103-degree-four-logsignature-affine-null-equivalence.md
  - research/visual_exploration/findings/VIS-104-area-area-commutator-projection.md
  - research/visual_exploration/findings/VIS-105-next-block-area-area-commutator-null.md
  - research/visual_exploration/findings/VIS-106-area-area-four-block-replication-panel-null.md
  - research/visual_exploration/findings/VIS-107-area-area-markov-type-affine-line-collapse.md
  - research/visual_exploration/findings/VIS-108-level-four-markov-pair-fourier-homometric.md
  - research/visual_exploration/findings/VIS-109-third-order-correlation-minimal-span-boundary.md
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual line has progressively removed representations whose apparent richness is already forced by lower-information structure: local zero portraits reduce to analytic normal forms; circular modulus shells to Poisson--Jensen data; phase winding to divisor count; raw gap geometry has strong finite-size random-matrix baselines; ordinary one-dimensional persistence forgets chronology; and low-degree delay signatures are largely fixed by local block inventories.

The three-delay level-four branch did identify a genuine chronology carrier in principle. `VIS-097` showed that different Eulerian assemblies of the same local four-block inventory can differ through an area-area commutator, while `VIS-099`--`VIS-100` supplied an exact finite order-three Markov-type null after fixed quantization. Source tests were then negative: `VIS-101`, `VIS-102`, and `VIS-105` found no unusual conditional residual for their frozen statistics, and `VIS-106` completed a predeclared four-block replication panel with exact tail probabilities `7/11`, `20/21`, `13/20`, and `209/248`, all far above the Bonferroni threshold `1/80`.

`VIS-107` resolves the structural question exposed by that panel. For every exact order-three Markov type of the ordinary scalar three-delay path, the canonical area-area coordinates satisfy constant `q_2` and constant `q_1+q_3`. After centering, the nominal three-dimensional `P_AA` support is universally confined to the single direction `B_1-B_3`. The affine-line behavior seen in `VIS-105`--`VIS-106` was therefore structural, not a finite-class accident.

`VIS-108` adds a different information-loss control at the current frontier. It constructs two binary words in one exact order-three Markov type whose degree-four three-delay signatures differ, while their complete Fourier magnitudes and aperiodic autocorrelations agree exactly. The pair is not related by a global translation or reflection. Hence a raw magnitude spectrum or power spectrum can erase chronology that is known to survive the admitted local-block quotient; visually richer spectral plots do not automatically buy new information.

`VIS-109` identifies the first higher-order spectral carrier that passes that exact information-admission witness. Every third-order correlation `C(k,l)` with `max(k,l)<=3` is forced by the exact order-three Markov type, but the `VIS-108` pair already differs at the first larger span: `C_a(1,4)=1` and `C_b(1,4)=0`. Equivalently their bispectra differ although their complete power spectra agree. This does not establish a zeta effect; it only shows that third-order phase coupling can carry chronology beyond both admitted lower-information quotients, with an exact local/nonlocal boundary.

The current frontier is therefore no longer to search for an arbitrary “richer spectrum.” A higher-order spectral continuation is now informationally admissible, but it must specify a sparse or low-dimensional statistic beyond the forced lag block before source inspection, condition it against the exact local type, and then ask whether the residual is source-specific under fresh controls.

## Research question

Is there a mathematically specified visual or multiscale carrier for zeta-zero structure that retains information beyond an explicit lower-information quotient and then shows a source-specific residual under fresh, predeclared confirmation material?

For any continuation of the existing area-area route, can an independently motivated source/height-scale hypothesis be stated before inspecting new data for the single surviving `B_1-B_3` direction? For a higher-order spectral continuation, is there an independently motivated third-order lag/frequency statistic outside the `VIS-109` forced local block whose conditional residual survives both the exact order-three Markov-type null and an appropriate finite-size CUE or other non-arithmetic source control?

## Why it may matter

`VIS-107` sharpens the local information accounting: the area-area mechanism is algebraically real, but the exact local quotient removes two of its three nominal coordinates before source testing. `VIS-108` shows that moving to an apparently global magnitude spectrum is not enough because complete two-point autocorrelation can still identify distinct exact-type assemblies. `VIS-109` then gives a positive information result without claiming source specificity: third-order correlation crosses the quotient boundary at minimal span four on the same exact witness.

This separates two questions that were previously entangled. **Can the representation carry the missing chronology?** For third-order spectra, the answer is now yes in principle. **Does zeta exhibit an unusual residual in that carrier?** That remains completely open and must be tested without using the same source material to choose the representation and declare the anomaly.

## Decisive test

Do not extend the `VIS-105`--`VIS-106` adjacent-window panel. If `P_AA` is reused, acknowledge `VIS-107`: after exact order-three Markov-type conditioning its centered support has only the `B_1-B_3` direction. Before looking at new source values, freeze a separately motivated height/source regime, window family, statistic, and combined decision rule. A positive conditional residual must then survive a matched finite-size CUE or otherwise appropriate non-arithmetic source control before being called zeta-specific.

For a bispectral/third-order continuation, respect the exact boundary in `VIS-109`. Lags with maximum span at most three are already determined by the admitted local-four-block inventory and cannot certify chronology beyond that quotient. Predeclare a low-dimensional lag-domain statistic or an equivalent bispectral functional using genuinely nonlocal spans, then evaluate it conditionally on the exact order-three Markov type. Do not inspect a two-dimensional source heatmap and select frequencies or lags afterward.

A source-positive result must then replicate on fresh material and survive an appropriate finite-size CUE or other non-arithmetic source comparison. Kill the route if the statistic is determined by the admitted local inventory, reduces to two-point autocorrelation, is reproduced by the matched source control, or depends on post-hoc lag/frequency/window selection.

For any other new visual/multiscale carrier, state exactly what information the representation preserves and forgets and explicitly test the `VIS-108` homometric pair or an equivalent exact witness when the carrier is intended to preserve assembly chronology generally.

## Evidence boundary

`VIS-097` proves chronology capacity in principle, not source specificity. `VIS-099`--`VIS-100` establish exact conditional-null mechanics after quantization. `VIS-101`, `VIS-102`, `VIS-105`, and `VIS-106` are finite source negatives under specific frozen statistics/designs. `VIS-104` gives the exact canonical area-area projection. `VIS-107` proves only that this projection has one assembly-sensitive centered direction under the exact order-three Markov-type quotient. `VIS-108` proves only that one explicit nontrivial exact-type pair has equal complete Fourier magnitude while differing at signature degree four. `VIS-109` proves only the corresponding exact third-order-correlation boundary and that this pair has unequal bispectra.

These results do not establish that zeta-zero chronology has a nonzero bispectral residual after conditioning, that any such residual is arithmetic-specific, that higher-order spectra outperform path signatures, that quantization preserves all relevant continuous information, that zeta and finite-size CUE differ for a frozen third-order statistic, or that any multiscale geometry yields a new RH criterion.

## Research disposition

Accepted in further narrowed form. The adjacent-block `P_AA` replication route is closed negatively by `VIS-106`; the structural affine-line audit is resolved by `VIS-107`; magnitude-only Fourier/power-spectrum views are excluded by `VIS-108` as generally sufficient replacements for chronology beyond the exact local-block quotient; and `VIS-109` shows that third-order correlation/bispectrum is informationally capable of crossing that boundary at minimal nonlocal span. The live question is now source specificity under a predeclared higher-order statistic and exact local conditioning, or a genuinely different carrier with an equally explicit information audit.