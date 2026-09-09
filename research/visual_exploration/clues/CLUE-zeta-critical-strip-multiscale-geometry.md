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
  - research/visual_exploration/findings/VIS-111-growing-lag-third-order-escapes-fixed-block.md
  - research/visual_exploration/findings/VIS-112-growing-lag-witness-empirical-average-dilution.md
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual line has progressively removed representations whose apparent richness is already forced by lower-information structure: local zero portraits reduce to analytic normal forms; circular modulus shells to Poisson--Jensen data; phase winding to divisor count; raw gap geometry has strong finite-size random-matrix baselines; ordinary one-dimensional persistence forgets chronology; and low-degree delay signatures are largely fixed by local block inventories.

The three-delay level-four branch did identify a genuine chronology carrier in principle. `VIS-097` showed that different Eulerian assemblies of the same local four-block inventory can differ through an area-area commutator, while `VIS-099`--`VIS-100` supplied an exact finite order-three Markov-type null after fixed quantization. Source tests were then negative: `VIS-101`, `VIS-102`, and `VIS-105` found no unusual conditional residual for their frozen statistics, and `VIS-106` completed a predeclared four-block replication panel with exact tail probabilities `7/11`, `20/21`, `13/20`, and `209/248`, all far above the Bonferroni threshold `1/80`.

`VIS-107` resolves the structural question exposed by that panel. For every exact order-three Markov type of the ordinary scalar three-delay path, the canonical area-area coordinates satisfy constant `q_2` and constant `q_1+q_3`. After centering, the nominal three-dimensional `P_AA` support is universally confined to the single direction `B_1-B_3`. The affine-line behavior seen in `VIS-105`--`VIS-106` was therefore structural, not a finite-class accident.

`VIS-108` adds a different information-loss control at the current frontier. It constructs two binary words in one exact order-three Markov type whose degree-four three-delay signatures differ, while their complete Fourier magnitudes and aperiodic autocorrelations agree exactly. The pair is not related by a global translation or reflection. Hence a raw magnitude spectrum or power spectrum can erase chronology that is known to survive the admitted local-block quotient; visually richer spectral plots do not automatically buy new information.

`VIS-109` identifies the first higher-order spectral carrier that passes that exact information-admission witness. Every third-order correlation `C(k,l)` with `max(k,l)<=3` is forced by the exact order-three Markov type, but the `VIS-108` pair already differs at the first larger span: `C_a(1,4)=1` and `C_b(1,4)=0`. Equivalently their bispectra differ although their complete power spectra agree. This establishes information beyond the admitted order-three quotient, not source specificity.

`VIS-110` closes an interpretive loophole in that positive admission result. Any bounded-lag higher-order correlation with maximum lag `r` is exactly a linear functional of the length-`(r+1)` block inventory. For the `VIS-108` witness, the span-four bispectral distinction is precisely a difference in length-five block counts. Thus “beyond the order-three quotient” is not the same as “genuinely nonlocal”: a fixed span-four statistic advances one local block order, and any uniformly bounded lag panel remains inside a finite-memory hierarchy.

`VIS-111` supplies the exact positive complement. For every `r>=2` it constructs two binary words in the same exact order-`r` Markov type, hence with the same complete length-`(r+1)` block inventory, while the third-order coefficient at lags `r+1` and `2r+3` is respectively `1` and `0`. The word length is `4r+6`, so these lags scale to one quarter and one half of the observation window. This growing-lag statistic therefore does not factor through any block inventory of uniformly fixed length.

`VIS-112` separates that information-admission result from effect-size claims. For the same witness, empirical averaging over admissible starts turns the exact raw difference `1` into `2/N`, which vanishes with word length. Thus escaping every fixed block quotient does not by itself provide a scale-stable normalized effect. Conversely, a vanishing normalized effect is not automatically undetectable unless its matched-null fluctuation scale is known. Information admission, normalization/amplitude, and source specificity are three distinct gates.

The purely representational admission question is now settled for one concrete class: a growing-lag third-order carrier can in principle retain assembly information that every fixed finite-memory quotient eventually forgets. The live frontier is whether a mathematically motivated, predeclared growing-scale statistic has a nontrivial effect at a frozen normalization relative to its matched-null fluctuations and then shows a source-specific residual on zeta-zero data after exact lower-information conditioning and fresh confirmation.

## Research question

Is there a mathematically specified visual or multiscale carrier for zeta-zero structure that retains information beyond an explicit lower-information quotient, has a reproducible normalized effect relative to a predeclared finite-size null, and then shows a source-specific residual under fresh confirmation material?

For the higher-order spectral continuation, can an independently motivated growing-lag scaling law, normalization, and low-dimensional statistic be frozen before inspecting new source values? Does the statistic escape the admitted lower-information quotient, and is its observed effect non-negligible relative to the fluctuation scale of an appropriate finite-size CUE or other non-arithmetic control? If a finite-order statistic is studied instead, can its claim be kept explicitly at that finite-memory level rather than interpreted as global chronology?

## Why it may matter

`VIS-107` sharpens the local information accounting: the area-area mechanism is algebraically real, but the exact local quotient removes two of its three nominal coordinates before source testing. `VIS-108` shows that moving to an apparently global magnitude spectrum is not enough because complete two-point autocorrelation can still identify distinct exact-type assemblies. `VIS-109` then gives a positive information result without claiming source specificity: third-order correlation crosses the order-three quotient boundary at minimal span four on the same exact witness.

`VIS-110` separates that relative boundary from a genuinely nonlocal one: every bounded-lag continuation remains inside a finite-block hierarchy. `VIS-111` then proves that this obstruction is not absolute. A deliberately growing-lag third-order family can distinguish exact-type assemblies while escaping every uniformly fixed block length. The representation class therefore has enough information capacity in principle.

`VIS-112` adds a second independent requirement. The exact `VIS-111` witness has only `O(1)` raw separation, so the natural empirical-average contrast is `O(1/N)`. A representation can therefore admit genuinely growing-scale information while its normalized contrast disappears. That does not kill the route: detectability depends on the matched-null fluctuation scale. It does mean that a source experiment must freeze and justify both the information scale and the amplitude/normalization scale before source inspection rather than inheriting the synthetic witness's raw coefficient as though it were macroscopic.

This keeps three questions distinct. **Can the representation carry information omitted by every fixed local quotient?** `VIS-111` says yes for one exact growing-lag family. **Does the chosen normalization retain a meaningful effect relative to the matched finite-size null?** `VIS-112` shows that this is an additional question, not a consequence of non-factorization. **Does zeta exhibit an unusual residual after those two gates are frozen?** Nothing so far establishes that.

## Decisive test

Do not extend the `VIS-105`--`VIS-106` adjacent-window panel. If `P_AA` is reused, acknowledge `VIS-107`: after exact order-three Markov-type conditioning its centered support has only the `B_1-B_3` direction. Before looking at new source values, freeze a separately motivated height/source regime, window family, statistic, normalization, and combined decision rule. A positive conditional residual must then survive a matched finite-size CUE or otherwise appropriate non-arithmetic source control before being called zeta-specific.

For a finite-order bispectral/third-order continuation, respect both `VIS-109` and `VIS-110`. A fixed maximum lag `R` is exactly a length-`(R+1)` block statistic. If such a statistic is used, predeclare `R`, the low-dimensional functional, normalization, the exact lower-order conditioning, and the narrow claim being tested. Do not call a positive result “nonlocal” merely because `R>3`; interpret it as a finite-order source effect and compare it against the matched finite-size CUE or other non-arithmetic source control.

For a genuinely nonlocal/multiscale continuation, use `VIS-111` only as an information-admission witness and `VIS-112` as an amplitude warning, not as a reason to copy the arbitrary synthetic lag pair or its raw normalization onto zeta data. Before source inspection, predeclare a mathematically motivated lag law `R(N)` or equivalent global higher-order functional, the lower-information quotient it is intended to escape, the normalization or variance-stabilizing transformation, confirmation windows, and combined decision rule. Give an information audit showing that the chosen statistic does not collapse to a uniformly fixed block inventory, and give an amplitude audit against the matched finite-size null showing the scale on which departures are to be judged. Then test on untouched source material against finite-size CUE or another appropriate non-arithmetic control. Any interpretation must also be audited against known finite-height zeta corrections rather than treating every CUE departure as new arithmetic structure.

A source-positive result need not have an absolute `O(1)` normalized contrast, but it must replicate on fresh material and be nontrivial relative to the predeclared matched-null fluctuation scale. Kill the route if the statistic is determined by the admitted lower-information inventory, reduces to two-point autocorrelation, is reproduced by the matched source control at the declared scale, or depends on post-hoc lag/frequency/window/growth-law/normalization selection.

For any other new visual/multiscale carrier, state exactly what information the representation preserves and forgets and explicitly test the `VIS-108` homometric pair, the `VIS-111` growing-lag family, or another exact witness appropriate to the claimed information level. If the carrier is compared across scales, state separately how its normalization behaves and what null fluctuation scale makes a residual scientifically meaningful.

## Evidence boundary

`VIS-097` proves chronology capacity in principle, not source specificity. `VIS-099`--`VIS-100` establish exact conditional-null mechanics after quantization. `VIS-101`, `VIS-102`, `VIS-105`, and `VIS-106` are finite source negatives under specific frozen statistics/designs. `VIS-104` gives the exact canonical area-area projection. `VIS-107` proves only that this projection has one assembly-sensitive centered direction under the exact order-three Markov-type quotient. `VIS-108` proves only that one explicit nontrivial exact-type pair has equal complete Fourier magnitude while differing at signature degree four. `VIS-109` proves the corresponding exact third-order-correlation boundary and that this pair has unequal bispectra. `VIS-110` proves that every bounded-lag cylinder/higher-order-correlation statistic remains a finite-block statistic. `VIS-111` proves only that one explicit family of growing-lag third-order coefficients escapes every uniformly fixed block quotient on synthetic binary assemblies. `VIS-112` proves only that the displayed `VIS-111` raw unit difference becomes `2/N` under its natural admissible-start empirical average, and therefore does not by itself supply a macroscopic normalized-amplitude witness.

These results do not establish that zeta-zero chronology has a nonzero growing-lag bispectral residual after conditioning, that any such residual is arithmetic-specific, that the synthetic `VIS-111` lag law is natural for zeta, that a chosen zeta statistic escapes all relevant growing-memory controls, that a shrinking normalized effect is detectable or undetectable without a null-variance calculation, that bicoherence or another normalization is preferable, that higher-order spectra outperform path signatures, that quantization preserves all relevant continuous information, that zeta and finite-size CUE differ for a frozen higher-order statistic, or that any multiscale geometry yields a new RH criterion.

## Research disposition

Accepted in further narrowed form. The adjacent-block `P_AA` replication route is closed negatively by `VIS-106`; the structural affine-line audit is resolved by `VIS-107`; magnitude-only Fourier/power-spectrum views are excluded by `VIS-108` as generally sufficient replacements for chronology beyond the exact local-block quotient; `VIS-109` shows that third-order correlation/bispectrum crosses the order-three quotient at minimal span; `VIS-110` shows that any fixed bounded-lag version remains inside the finite-block hierarchy; `VIS-111` gives an exact growing-lag family that escapes every uniformly fixed block quotient; and `VIS-112` shows that the same witness's natural empirical-average contrast still vanishes as `2/N`.

The live question is now source specificity under a **predeclared growing-scale statistic and normalization**, with independently motivated scale law, exact lower-information accounting, explicit matched-null fluctuation calibration, untouched confirmation material, and a matched non-arithmetic source control. A finite-order continuation remains valid only for the correspondingly narrower finite-memory source claim.