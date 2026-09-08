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
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual-exploration line has progressively closed several attractive channels that do not add an independent arithmetic information carrier. Infinitesimal zero portraits collapse to the local analytic normal form; concentric `log|F|` shells reduce to Poisson-Jensen source plus boundary data; phase/modulus and overlapping-disk phase information collapse to ordinary analytic continuation up to global phase; phase winding is divisor count; raw adjacent-gap geometry has strong finite-size random-matrix baselines; and ordinary one-dimensional persistence is exactly the unordered adjacent-gap multiset.

The delay-geometry branch gives a sharper information hierarchy. `VIS-093` through `VIS-096` show that ordinary fixed-window persistence, static delay graphs, and unaugmented delay-path signatures through level three are determined by increasingly local block inventories; planar level four is also locally determined. `VIS-097` proves the first genuine escape: in three delay dimensions, level four can distinguish different Eulerian assemblies of the same length-four-block inventory through an exact area-area commutator. Thus level four can carry chronology in principle.

`VIS-098` through `VIS-100` then make the source-specific null exact. Exact real-valued block reassembly is generically degenerate, but after a fixed finite quantization the complete quantized length-four-block table is an order-three Markov type. Conditional on that table and the initial triple, every compatible word has the same probability under every homogeneous order-three Markov chain. Whittle's formula gives the exact type-class cardinality and completion counts give exact uniform sampling.

The first two frozen low-zero source tests are both negative. `VIS-101` uses a binary median quantizer trained on `g_1,...,g_70`, the untouched block `g_71,...,g_106`, and the pre-existing coordinate `S^4_(1,2,1,3)`; its exact conditional tail probability is `493/750`. `VIS-102` changes only the information carrier to three nearly balanced training-defined bins, producing an exact type class of size `1752`, yet the same coordinate is even more central: `p=209/219`.

The live issue is therefore no longer whether level four retains chronology, nor whether a slightly richer coarse amplitude quotient on this same block rescues the fixed coordinate. Both questions now have answers. What remains is whether a **different independently justified chronology functional or a genuinely new source scale** retains organization beyond its complete finite local quotient without post-hoc search.

## Research question

Can a pre-frozen direction-sensitive fourth-level or log-signature observable, evaluated on a **new untouched zeta-zero confirmation window or height regime**, separate the source from its exact quantized order-three Markov-type null after the representation and statistic have been fixed independently?

The next test should not refine thresholds again on `g_71,...,g_106`; that block has already informed both binary and ternary results. If the next route changes the statistic, delay representation, quantizer, or scale in response to `VIS-101`/`VIS-102`, freeze the new design first and move to fresh confirmation material.

If a residual survives, does it also survive independently fixed nearby representation choices and matched non-arithmetic source controls strongly enough to distinguish quotient-specific chronology from generic longer memory, nonstationarity, or finite-size random-matrix structure?

The broader visual question remains open: after the classified analytic, spacing, persistence, finite-memory, and low-signature quotients, is there any mesoscopic or nonlocal geometry of the zeta zero configuration that survives appropriately matched source controls in a statement meaningful without the rendering?

## Why it may matter

`VIS-097` identifies a real nonlocal degree of freedom: ordered interaction between nonparallel local area modes. `VIS-099` and `VIS-100` turn that degree of freedom into an exact finite conditional experiment after quantization, with no model-parameter fitting or approximate reassembly required.

`VIS-101` and `VIS-102` show that generic chronology capacity is not enough. The same mathematically legitimate level-four coordinate is ordinary under two distinct training-defined finite quotients of the same low-zero block. This removes a simple rescue hypothesis — that the binary result failed only because two bins discarded too much coarse amplitude information — while leaving other independently chosen level-four/log-signature functionals and scales untested.

This keeps three notions separate: generic chronology capacity, chronology beyond a specified finite local quotient, and arithmetic/source specificity. A future separation from the conditioned Markov-type null would establish only the middle statement. Arithmetic interpretation would still require relevant non-arithmetic spectral/source controls.

## Decisive test

Choose the next design **before inspecting its new confirmation residual**. Freeze the new source window or height regime, unfolding convention, delay coordinates, endpoint treatment, finite quantizer and symbol embedding, and one direction-sensitive fourth-level/log-signature statistic or low-dimensional projection. Because the old confirmation block has now been used twice, any design choice informed by those outcomes must be evaluated on fresh untouched source material.

Build the quantized three-context transition multigraph and complete quantized length-four-block table. Compute the exact Whittle cardinality `W`; reject the representation if `W=1`. Use exhaustive enumeration when feasible, otherwise the exact completion-count sampler with sampling uncertainty reported separately. Controls must preserve the initial quantized triple and every quantized length-four-block count exactly.

Keep a chronology route only if the frozen directional residual survives fresh confirmation and reasonable independently fixed representation perturbations. A positive result rejects only the conditioned homogeneous order-three Markov explanation on that finite quotient. Before any arithmetic claim, compare against matched non-arithmetic source models, including finite-size random-matrix or other spectral controls appropriate to the observable.

Kill or narrow the route if the type class is degenerate, the effect disappears on fresh confirmation, a matched source control recreates it, or the separation depends on post-hoc threshold/statistic/window selection. The binary and ternary `(1,2,1,3)` experiments on `g_71,...,g_106` are closed and must not be recycled as purported fresh confirmation.

For any alternative topological or multiscale route, state the metric/graph/path/filtration and information carrier explicitly, identify what lower information it preserves, and test the residual against a nondegenerate matched quotient rather than the visual texture.

## Evidence boundary

`VIS-008` and `VIS-013` through `VIS-019` are analytic, topological, information-loss, or prior-art controls; they do not classify every possible nonlocal zero statistic. `VIS-092` through `VIS-096` bound several persistence, transition-graph, and low-signature constructions by local gap/block information. `VIS-097` proves only generic level-four chronology capacity in three delay dimensions.

`VIS-098` proves an exact-real-valued reassembly uniqueness condition. `VIS-099` proves the exact conditional-uniform law only on a fixed finite-alphabet quotient. `VIS-100` supplies the classical exact type-class count and uniform completion sampler.

`VIS-101` and `VIS-102` are finite negative statements for two training-defined quantizers, one low-zero training/target split, and the same pre-existing fourth-level coordinate. They do not show that every quantized chronology statistic is null, that higher zeros behave identically, or that the Markov-type null is a complete non-arithmetic source model. Conversely, those two inspected results prohibit treating further adaptive threshold/statistic search on the same confirmation block as independent evidence.

No finding in this chain establishes a mesoscopic fractal dimension, a new zeta-zero law, an RH criterion, or a distinction between zeta and a suitably matched higher-order point-process/control ensemble. This remains an accepted research direction, not evidence of such a distinction.

## Research disposition

Accepted in further narrowed form. Exact null mechanics are closed by `VIS-099` and `VIS-100`; the binary and balanced ternary source tests are both exact negatives. The next substantive chronology result must move to fresh confirmation material and change a more meaningful axis than threshold granularity alone — most naturally a pre-justified level-four/log-signature functional or source scale — while preserving the exact finite conditional-null discipline.
