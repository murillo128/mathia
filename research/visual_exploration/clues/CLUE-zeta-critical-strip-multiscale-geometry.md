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
  - research/visual_exploration/findings/VIS-110-bounded-lag-higher-order-correlation-finite-block.md
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual line has progressively removed representations whose apparent richness is already forced by lower-information structure: local zero portraits reduce to analytic normal forms; circular modulus shells to Poisson--Jensen data; phase winding to divisor count; raw gap geometry has strong finite-size random-matrix baselines; ordinary one-dimensional persistence forgets chronology; and low-degree delay signatures are largely fixed by local block inventories.

The three-delay level-four branch did identify a genuine chronology carrier in principle. `VIS-097` showed that different Eulerian assemblies of the same local four-block inventory can differ through an area-area commutator, while `VIS-099`--`VIS-100` supplied an exact finite order-three Markov-type null after fixed quantization. Source tests were then negative: `VIS-101`, `VIS-102`, and `VIS-105` found no unusual conditional residual for their frozen statistics, and `VIS-106` completed a predeclared four-block replication panel with exact tail probabilities `7/11`, `20/21`, `13/20`, and `209/248`, all far above the Bonferroni threshold `1/80`.

`VIS-107` resolves the structural question exposed by that panel. For every exact order-three Markov type of the ordinary scalar three-delay path, the canonical area-area coordinates satisfy constant `q_2` and constant `q_1+q_3`. After centering, the nominal three-dimensional `P_AA` support is universally confined to the single direction `B_1-B_3`. The affine-line behavior seen in `VIS-105`--`VIS-106` was therefore structural, not a finite-class accident.

`VIS-108` adds a different information-loss control at the current frontier. It constructs two binary words in one exact order-three Markov type whose degree-four three-delay signatures differ, while their complete Fourier magnitudes and aperiodic autocorrelations agree exactly. The pair is not related by a global translation or reflection. Hence a raw magnitude spectrum or power spectrum can erase chronology that is known to survive the admitted local-block quotient; visually richer spectral plots do not automatically buy new information.

`VIS-109` identifies the first higher-order spectral carrier that passes that exact information-admission witness. Every third-order correlation `C(k,l)` with `max(k,l)<=3` is forced by the exact order-three Markov type, but the `VIS-108` pair already differs at the first larger span: `C_a(1,4)=1` and `C_b(1,4)=0`. Equivalently their bispectra differ although their complete power spectra agree. This establishes information beyond the admitted order-three quotient, not source specificity.

`VIS-110` now closes an interpretive loophole in that positive admission result. Any bounded-lag higher-order correlation with maximum lag `r` is exactly a linear functional of the length-`(r+1)` block inventory. For the `VIS-108` witness, the span-four bispectral distinction is precisely a difference in length-five block counts. Thus “beyond the order-three quotient” is not the same as “genuinely nonlocal”: a fixed span-four statistic advances one local block order, and any uniformly bounded lag panel remains inside a finite-memory hierarchy.

The current frontier is therefore no longer to search for an arbitrary “richer spectrum,” nor merely to choose a sparse coefficient outside the `VIS-109` forced block. A higher-order continuation must decide in advance whether it is testing a **finite-order source effect** or a genuinely nonlocal/multiscale chronology channel, because those require different information claims and controls.

## Research question

Is there a mathematically specified visual or multiscale carrier for zeta-zero structure that retains information beyond an explicit lower-information quotient and then shows a source-specific residual under fresh, predeclared confirmation material?

For any continuation of the existing area-area route, can an independently motivated source/height-scale hypothesis be stated before inspecting new data for the single surviving `B_1-B_3` direction? For a higher-order spectral continuation, can one either isolate a predeclared finite-order effect and interpret it honestly as such, or specify a lag scale growing with the observation window / genuinely global frequency-domain functional whose information content provably does not factor through a fixed finite-block inventory?

## Why it may matter

`VIS-107` sharpens the local information accounting: the area-area mechanism is algebraically real, but the exact local quotient removes two of its three nominal coordinates before source testing. `VIS-108` shows that moving to an apparently global magnitude spectrum is not enough because complete two-point autocorrelation can still identify distinct exact-type assemblies. `VIS-109` then gives a positive information result without claiming source specificity: third-order correlation crosses the order-three quotient boundary at minimal span four on the same exact witness.

`VIS-110` separates that relative boundary from a genuinely nonlocal one. A source anomaly at fixed span four could still be scientifically meaningful, but its correct interpretation would be dependence beyond four-block counts, not chronology beyond all finite local memory. Conversely, a multiscale/fractal claim now needs a carrier whose memory scale itself grows or whose global spectral functional is shown not to collapse to bounded block statistics.

This keeps two questions distinct. **Can the representation carry information omitted by the chosen quotient?** `VIS-109` says yes for third-order correlation relative to the order-three quotient. **What kind of information is it?** `VIS-110` says a bounded-lag version is still finite-block information. Source specificity remains open in either regime and must be tested without using the same source material to choose the representation and declare the anomaly.

## Decisive test

Do not extend the `VIS-105`--`VIS-106` adjacent-window panel. If `P_AA` is reused, acknowledge `VIS-107`: after exact order-three Markov-type conditioning its centered support has only the `B_1-B_3` direction. Before looking at new source values, freeze a separately motivated height/source regime, window family, statistic, and combined decision rule. A positive conditional residual must then survive a matched finite-size CUE or otherwise appropriate non-arithmetic source control before being called zeta-specific.

For a finite-order bispectral/third-order continuation, respect both `VIS-109` and `VIS-110`. A fixed maximum lag `R` is exactly a length-`(R+1)` block statistic. If such a statistic is used, predeclare `R`, the low-dimensional functional, the exact lower-order conditioning, and the narrow claim being tested. Do not call a positive result “nonlocal” merely because `R>3`; interpret it as a finite-order source effect and compare it against the matched finite-size CUE or other non-arithmetic source control.

For a genuinely nonlocal/multiscale continuation, predeclare either a lag scale `R(N)` that grows materially with the observation window or a frequency-domain/global higher-order functional whose expansion mixes growing lag ranges. Before source inspection, state what lower-information quotient is being conditioned away and give an information audit showing why the proposed statistic does not factor through any fixed finite-block inventory. Do not inspect a two-dimensional source heatmap and select frequencies, lags, growth laws, or windows afterward.

A source-positive result must replicate on fresh material and survive an appropriate finite-size CUE or other non-arithmetic source comparison. Kill the route if the statistic is determined by the admitted local inventory, reduces to two-point autocorrelation, is reproduced by the matched source control, or depends on post-hoc lag/frequency/window selection.

For any other new visual/multiscale carrier, state exactly what information the representation preserves and forgets and explicitly test the `VIS-108` homometric pair or an equivalent exact witness when the carrier is intended to preserve assembly chronology generally.

## Evidence boundary

`VIS-097` proves chronology capacity in principle, not source specificity. `VIS-099`--`VIS-100` establish exact conditional-null mechanics after quantization. `VIS-101`, `VIS-102`, `VIS-105`, and `VIS-106` are finite source negatives under specific frozen statistics/designs. `VIS-104` gives the exact canonical area-area projection. `VIS-107` proves only that this projection has one assembly-sensitive centered direction under the exact order-three Markov-type quotient. `VIS-108` proves only that one explicit nontrivial exact-type pair has equal complete Fourier magnitude while differing at signature degree four. `VIS-109` proves the corresponding exact third-order-correlation boundary and that this pair has unequal bispectra. `VIS-110` proves that every bounded-lag cylinder/higher-order-correlation statistic remains a finite-block statistic and reclassifies the minimal span-four distinction as the next local block layer.

These results do not establish that zeta-zero chronology has a nonzero bispectral residual after conditioning, that any such residual is arithmetic-specific, that a growing-lag or global frequency functional escapes all important lower-information quotients, that higher-order spectra outperform path signatures, that quantization preserves all relevant continuous information, that zeta and finite-size CUE differ for a frozen higher-order statistic, or that any multiscale geometry yields a new RH criterion.

## Research disposition

Accepted in further narrowed form. The adjacent-block `P_AA` replication route is closed negatively by `VIS-106`; the structural affine-line audit is resolved by `VIS-107`; magnitude-only Fourier/power-spectrum views are excluded by `VIS-108` as generally sufficient replacements for chronology beyond the exact local-block quotient; `VIS-109` shows that third-order correlation/bispectrum crosses the order-three quotient at minimal span; and `VIS-110` shows that any fixed bounded-lag version remains inside the finite-block hierarchy.

The live question is now explicit: either test a predeclared **finite-order** higher-order statistic and make only the corresponding finite-memory source claim, or design a growing-lag/global higher-order carrier with an information audit strong enough to support a genuinely nonlocal/multiscale interpretation. In both cases, source specificity requires fresh confirmation and a matched non-arithmetic control.