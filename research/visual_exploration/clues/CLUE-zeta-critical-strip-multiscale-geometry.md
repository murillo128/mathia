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
  - research/visual_exploration/findings/VIS-113-lifted-homometric-growing-lag-constant-amplitude.md
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

`VIS-112` separates that information-admission result from effect-size claims. For the same sparse witness, empirical averaging over admissible starts turns the exact raw difference `1` into `2/N`, which vanishes with word length. Thus escaping every fixed block quotient does not by itself provide a scale-stable normalized effect.

`VIS-113` shows that the `VIS-112` dilution is not forced by the information boundary. It lifts the Fourier-homometric macro pair of `VIS-108` into an exact order-`r` closed-block family. The lifted words have identical complete two-point autocorrelation and identical complete length-`(r+1)` block inventories, yet at fixed macroscopic lag fractions `2/29` and `8/29` their empirical third-order averages differ exactly by `1/21` for every `r`. Thus fixed-block escape and nonvanishing normalized synthetic amplitude can coexist even after the complete ordinary power spectrum is held fixed.

The representational admission and synthetic-amplitude possibility questions are therefore settled for one concrete higher-order class. The live frontier is source specificity: whether a mathematically motivated, predeclared growing-scale statistic and normalization show a residual on zeta-zero data that is nontrivial relative to matched finite-size null fluctuations after exact lower-information conditioning and fresh confirmation.

## Research question

Is there a mathematically specified visual or multiscale carrier for zeta-zero structure that retains information beyond an explicit lower-information quotient, has a reproducible normalized effect relative to a predeclared finite-size null, and then shows a source-specific residual under fresh confirmation material?

For the higher-order spectral continuation, can an independently motivated growing-lag scaling law, normalization, and low-dimensional statistic be frozen before inspecting new source values? Does the statistic escape the admitted lower-information quotient, and is its observed effect non-negligible relative to the fluctuation scale of an appropriate finite-size CUE or other non-arithmetic control? If a finite-order statistic is studied instead, can its claim be kept explicitly at that finite-memory level rather than interpreted as global chronology?

## Why it may matter

`VIS-107` sharpens the local information accounting: the area-area mechanism is algebraically real, but the exact local quotient removes two of its three nominal coordinates before source testing. `VIS-108` shows that moving to an apparently global magnitude spectrum is not enough because complete two-point autocorrelation can still identify distinct exact-type assemblies. `VIS-109` then gives a positive information result without claiming source specificity: third-order correlation crosses the order-three quotient boundary at minimal span four on the same exact witness.

`VIS-110` separates that relative boundary from a genuinely nonlocal one: every bounded-lag continuation remains inside a finite-block hierarchy. `VIS-111` proves that this obstruction is not absolute by giving a growing-lag family that escapes every uniformly fixed block length. `VIS-112` then warns that non-factorization alone does not guarantee normalized amplitude.

`VIS-113` supplies the missing synthetic counterexample to treating that warning as a universal obstruction. Its lifted pair preserves the complete ordinary autocorrelation and every fixed local inventory eventually, but keeps an exact `1/21` empirical third-order separation at macroscopic lags. The higher-order representation class therefore has enough information and amplitude capacity in principle; neither property says that the zeta source actually uses that capacity.

This leaves the decisive third question. **Does zeta exhibit an unusual residual after the statistic, scale law, normalization, lower-information conditioning, and finite-size source null are frozen?** Nothing so far establishes that.

## Decisive test

Do not extend the `VIS-105`--`VIS-106` adjacent-window panel. If `P_AA` is reused, acknowledge `VIS-107`: after exact order-three Markov-type conditioning its centered support has only the `B_1-B_3` direction. Before looking at new source values, freeze a separately motivated height/source regime, window family, statistic, normalization, and combined decision rule. A positive conditional residual must then survive a matched finite-size CUE or otherwise appropriate non-arithmetic source control before being called zeta-specific.

For a finite-order bispectral/third-order continuation, respect both `VIS-109` and `VIS-110`. A fixed maximum lag `R` is exactly a length-`(R+1)` block statistic. If such a statistic is used, predeclare `R`, the low-dimensional functional, normalization, the exact lower-order conditioning, and the narrow claim being tested. Do not call a positive result “nonlocal” merely because `R>3`; interpret it as a finite-order source effect and compare it against the matched finite-size CUE or other non-arithmetic source control.

For a genuinely nonlocal/multiscale continuation, use `VIS-111` and `VIS-113` only as information/amplitude admissibility witnesses, not as reasons to copy their arbitrary synthetic lag fractions or block encodings onto zeta data. Before source inspection, predeclare a mathematically motivated lag law `R(N)` or equivalent global higher-order functional, the lower-information quotient it is intended to escape, the normalization or variance-stabilizing transformation, confirmation windows, and combined decision rule. Give an information audit showing that the chosen statistic does not collapse to a uniformly fixed block inventory, and give an amplitude audit against the matched finite-size null showing the scale on which departures are to be judged. Then test on untouched source material against finite-size CUE or another appropriate non-arithmetic control. Any interpretation must also be audited against known finite-height zeta corrections rather than treating every CUE departure as new arithmetic structure.

A source-positive result need not have an absolute `O(1)` normalized contrast, but it must replicate on fresh material and be nontrivial relative to the predeclared matched-null fluctuation scale. Kill the route if the statistic is determined by the admitted lower-information inventory, reduces to two-point autocorrelation, is reproduced by the matched source control at the declared scale, or depends on post-hoc lag/frequency/window/growth-law/normalization selection.

For any other new visual/multiscale carrier, state exactly what information the representation preserves and forgets and explicitly test the `VIS-108` homometric pair, the `VIS-111` sparse growing-lag family, the `VIS-113` constant-amplitude homometric lift, or another exact witness appropriate to the claimed information level. If the carrier is compared across scales, state separately how its normalization behaves and what null fluctuation scale makes a residual scientifically meaningful.

## Evidence boundary

`VIS-097` proves chronology capacity in principle, not source specificity. `VIS-099`--`VIS-100` establish exact conditional-null mechanics after quantization. `VIS-101`, `VIS-102`, `VIS-105`, and `VIS-106` are finite source negatives under specific frozen statistics/designs. `VIS-104` gives the exact canonical area-area projection. `VIS-107` proves only that this projection has one assembly-sensitive centered direction under the exact order-three Markov-type quotient. `VIS-108` proves only that one explicit nontrivial exact-type pair has equal complete Fourier magnitude while differing at signature degree four. `VIS-109` proves the corresponding exact third-order-correlation boundary and that this pair has unequal bispectra. `VIS-110` proves that every bounded-lag cylinder/higher-order-correlation statistic remains a finite-block statistic. `VIS-111` proves that one sparse growing-lag third-order family escapes every uniformly fixed block quotient. `VIS-112` proves that this sparse family's empirical-average contrast vanishes as `2/N`. `VIS-113` proves that a different lifted family can preserve every fixed local inventory eventually and the complete ordinary autocorrelation while retaining an exact `1/21` empirical third-order separation at macroscopic lags.

These results do not establish that zeta-zero chronology has a nonzero growing-lag bispectral residual after conditioning, that any such residual is arithmetic-specific, that either synthetic lag law is natural for zeta, that a chosen zeta statistic escapes all relevant growing-memory controls, that the finite-size matched-null variance has any particular scale, that bicoherence or another normalization is preferable, that higher-order spectra outperform path signatures, that quantization preserves all relevant continuous information, that zeta and finite-size CUE differ for a frozen higher-order statistic, or that any multiscale geometry yields a new RH criterion.

## Research disposition

Accepted in further narrowed form. The adjacent-block `P_AA` replication route is closed negatively by `VIS-106`; the structural affine-line audit is resolved by `VIS-107`; magnitude-only Fourier/power-spectrum views are excluded by `VIS-108` as generally sufficient replacements for chronology beyond the exact local-block quotient; `VIS-109` shows that third-order correlation/bispectrum crosses the order-three quotient at minimal span; `VIS-110` shows that any fixed bounded-lag version remains inside the finite-block hierarchy; `VIS-111` gives an exact growing-lag family that escapes every uniformly fixed block quotient; `VIS-112` shows that its sparse normalized contrast vanishes; and `VIS-113` shows that this amplitude collapse is not universal by producing a Fourier-homometric exact-type family with constant empirical third-order separation.

The live question is now source specificity under a **predeclared growing-scale statistic and normalization**, with independently motivated scale law, exact lower-information accounting, explicit matched-null fluctuation calibration, untouched confirmation material, and a matched non-arithmetic source control. A finite-order continuation remains valid only for the correspondingly narrower finite-memory source claim.