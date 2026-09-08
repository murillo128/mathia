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
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual-exploration line has progressively closed many visually rich channels that do not add an independent arithmetic information carrier. Infinitesimal zero portraits collapse to the local analytic normal form; complete concentric `log|F|` shells reduce to Poisson-Jensen source plus boundary data; phase/modulus and overlapping-disk phase information collapse to ordinary analytic continuation up to global phase; phase winding is divisor count; raw two-consecutive-gap geometry has a finite-size RMT/arithmetic baseline; and ordinary one-dimensional persistence is exactly the unordered adjacent-gap multiset.

The delay-geometry branch gives a sharper information hierarchy. `VIS-093` shows that ordinary fixed-window persistence forgets visitation order. `VIS-094` shows that freezing consecutive delay transitions as a static value-quotiented graph retains exactly one extra local block order while forgetting the distinguished Eulerian traversal. `VIS-095` and `VIS-096` show that ordinary unaugmented delay-path signatures through level three are still determined by the same oriented local-edge inventory, and in the planar two-delay case level four is also determined by that inventory.

`VIS-097` proves that this boundary is sharp in three delay dimensions: two paths can share endpoints and the complete unordered length-four-block inventory yet differ at signature level four through an exact area-area commutator. Thus three-dimensional level four is a genuine chronology carrier in principle.

`VIS-098` adds the matched-null admission gate. If the fixed-length delay windows are pairwise distinct, the exact local-block transition graph is a directed simple path and the exact block-preserving Eulerian reassembly class is a singleton. More generally, repeated states are necessary but not sufficient for exact reassembly ambiguity. Therefore the exact local-four-block quotient is a valid theoretical information boundary, but it is not automatically a usable resampling ensemble for continuous-valued arithmetic data.

`VIS-099` identifies one principled replacement rather than leaving “coarsening” underspecified. After a **fixed finite quantization**, the quantized length-four block table is an order-three Markov type. Conditional on that table and the initial quantized triple, every sequence in the type class has exactly the same probability under every homogeneous order-three Markov chain on the symbols. Uniform type-class reassembly is therefore a parameter-free exact conditional null on the quantized representation whenever the class is non-singleton.

The live issue is now **source-specific chronology after an explicit finite local quotient**, not merely whether a higher signature can remember order or whether an arbitrary approximate null can be invented.

## Research question

Does one pre-registered fourth-level or log-signature observable of a zeta-derived **quantized three-delay path** retain organization beyond its complete quantized length-four-block table, under the exact uniform Markov-type null from `VIS-099`?

If such a residual survives, is it stable enough under independently fixed nearby quantizers/embeddings and appropriately matched higher-order spectral controls to justify interpreting it as source-specific rather than as a consequence of the chosen quotient, generic long memory, nonstationarity, or random-matrix structure?

The broader visual question remains open as well: after the classified analytic, spacing, persistence, finite-memory, and low-signature quotients, is there any mesoscopic or nonlocal geometry of the zeta zero configuration that survives appropriately matched source controls in a statement meaningful without the rendering?

## Why it may matter

`VIS-097` identifies an exact degree of freedom absent from the complete unordered local-four-block inventory: order-dependent interaction between nonparallel local area modes. `VIS-098` prevents the false next step of treating exact real-valued local-block preservation as automatically resampleable. `VIS-099` then supplies an exact conditional experiment after a finite quotient: the null has no fitted Markov transition parameters once the quantized block table is conditioned on.

This separates three notions that are easy to conflate visually: generic chronology capacity, chronology beyond a specified finite local quotient, and arithmetic/source specificity. A separation from the `VIS-099` null would establish the middle statement only. That is still useful because it turns the next step into a falsifiable residual test with an exact sample space rather than a loosely matched simulation. Stronger arithmetic interpretation requires surviving representation controls and relevant non-arithmetic spectral/source baselines.

## Decisive test

Use one coherent source-specificity experiment and freeze its choices before confirmation.

First, fix the source representation: unfolding convention, finite observation window, three-delay coordinates, endpoint treatment, a finite quantizer `Q`, and a fixed numerical embedding of its symbols for the path statistic. Choose the quantizer using only exploratory/training material or an external rule; do not tune thresholds or alphabet size on confirmation residuals.

Build the quantized three-context transition multigraph and its complete quantized length-four-block count table. Determine the corresponding Markov type-class size. Reject this quantizer for the chronology test if the class is singleton or too small to provide a meaningful conditional comparison; do not loosen the quantizer after looking at the target statistic merely to manufacture alternatives.

Before sampling controls, pre-register one direction-sensitive fourth-level tensor/log-signature coordinate, invariant, or low-dimensional projection. Evaluate it on the fixed numerical embedding of the quantized source path and on uniform reassemblies from the exact type class. The controls must preserve the initial quantized triple and all quantized length-four block counts exactly.

Treat the quantized quotient itself as part of the hypothesis. Check the chosen statistic under independently fixed nearby representation choices sufficient to expose obvious threshold/embedding artifacts, and record how much real-valued information the quantizer discards. Do not claim that the conditional null applies to a statistic evaluated on the original real-valued path: any within-bin reconstruction or dequantization introduces a new model and requires a separate leakage audit.

Only after the quantized null is admitted should the pre-registered statistic be evaluated on untouched windows, heights, or scales. Keep the route only if the same directional residual survives confirmation without retuning. A positive result rejects the conditioned homogeneous order-three Markov local-memory explanation on that fixed quotient; it does **not** yet distinguish zeta arithmetic from generic longer-memory, nonstationary, or random-matrix mechanisms. That stronger interpretation requires matched higher-order source controls.

Kill or narrow the quantized route if the type class is degenerate, the effect disappears on confirmation, it depends materially on arbitrary threshold/embedding choices, or a relevant matched non-arithmetic source reproduces it.

For any alternative topological or multiscale route, state the metric/graph/path/filtration and the information carrier explicitly, then apply the analogous quotient test: identify what information the construction actually retains, construct a nondegenerate control preserving the admitted lower information, and test the residual rather than the visual texture.

## Evidence boundary

`VIS-008` and `VIS-013` through `VIS-019` are analytic, topological, information-loss, or prior-art controls; they do not classify every possible nonlocal zero statistic. `VIS-092` through `VIS-096` exactly bound several persistence, transition-graph, and low-signature constructions by local gap/block information. `VIS-097` proves only that fixed three-delay signature level four can distinguish some alternative assemblies with the same local edge inventory; it does not establish source specificity, reconstruction, or a zeta effect.

`VIS-098` proves a sufficient uniqueness condition for exact real-valued local-block reassembly and the corresponding almost-sure genericity statement under absolutely continuous finite-dimensional laws. It does not invalidate quantized controls. `VIS-099` proves the exact conditional-uniform Markov-type law **only on the fixed finite-alphabet quotient** and only supplies a nontrivial experiment when the observed type class contains alternatives. It does not prove that a useful quantizer exists, that the original continuous-valued statistic is matched, or that a departure from the null is arithmetic-specific.

No finding in this chain establishes a mesoscopic fractal dimension, a new zeta-zero statistic, an RH criterion, or a distinction between zeta and a suitably matched higher-order point-process/control ensemble. This remains an accepted research direction, not evidence of such a distinction.

## Research disposition

Accepted in further narrowed form. The first concrete nondegenerate replacement null after `VIS-098` is now finite pre-registered quantization followed by the exact uniform Markov-type reassembly law from `VIS-099`. The next positive result must first show chronology beyond quantized four-block counts on untouched data, and only then ask whether that residual survives representation controls and matched non-arithmetic source models.