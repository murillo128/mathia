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
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual-exploration line has progressively closed many visually rich channels that do not add an independent arithmetic information carrier. Infinitesimal zero portraits collapse to the local analytic normal form; complete concentric `log|F|` shells reduce to Poisson-Jensen source plus boundary data; phase/modulus and overlapping-disk phase information collapse to ordinary analytic continuation up to global phase; phase winding is divisor count; raw two-consecutive-gap geometry has a finite-size RMT/arithmetic baseline; and ordinary one-dimensional persistence is exactly the unordered adjacent-gap multiset.

The delay-geometry branch gives a sharper information hierarchy. `VIS-093` shows that ordinary fixed-window persistence forgets visitation order. `VIS-094` shows that freezing consecutive delay transitions as a static value-quotiented graph retains exactly one extra local block order while forgetting the distinguished Eulerian traversal. `VIS-095` and `VIS-096` show that ordinary unaugmented delay-path signatures through level three are still determined by the same oriented local-edge inventory, and in the planar two-delay case level four is also determined by that inventory.

`VIS-097` proves that this boundary is sharp in three delay dimensions: two paths can share endpoints and the complete unordered length-four-block inventory yet differ at signature level four through an exact area-area commutator. Thus three-dimensional level four is a genuine chronology carrier in principle.

`VIS-098` adds the matched-null admission gate. If the fixed-length delay windows are pairwise distinct, the exact local-block transition graph is a directed simple path and the exact block-preserving Eulerian reassembly class is a singleton. More generally, repeated states are necessary but not sufficient for exact reassembly ambiguity. Therefore the exact local-four-block quotient is a valid theoretical information boundary, but it is not automatically a usable resampling ensemble for continuous-valued arithmetic data.

`VIS-099` identifies one principled replacement rather than leaving “coarsening” underspecified. After a **fixed finite quantization**, the quantized length-four block table is an order-three Markov type. Conditional on that table and the initial quantized triple, every sequence in the type class has exactly the same probability under every homogeneous order-three Markov chain on the symbols. Uniform type-class reassembly is therefore a parameter-free exact conditional null on the quantized representation whenever the class is non-singleton.

`VIS-100` closes the null mechanics. Whittle's cofactor-factorial formula computes the exact type-class cardinality from the transition table, so nondegeneracy is the explicit integer test `W>1`. The same completion counts give an exact sequential uniform sampler: at each step choose the next transition in proportion to the number of compatible completions. No graph-visual judgment, MCMC burn-in, or approximate mixing claim is needed.

`VIS-101` then executes the first frozen source-specific test rather than refining the null again. A binary median quantizer fixed on `g_1,...,g_70`, the untouched 36-gap block `g_71,...,g_106`, and the pre-selected three-delay signature coordinate `S^4_(1,2,1,3)` give a nondegenerate exact type class of size `94500`, but the observed source statistic is central under exhaustive conditional enumeration: the exact two-sided tail probability is `493/750`. This closes that specific binary quotient/statistic/window. It is evidence against treating the mere availability of level-four chronology as a source-specific zeta signal.

The live issue is therefore narrower than “does level four retain order?” It does. The remaining question is whether a **genuinely different, independently fixed information carrier or scale** retains source organization after the exact finite local quotient, without retuning around the negative binary experiment.

## Research question

Does an independently pre-registered zeta-derived representation — for example a principled multi-bin quantizer, a different direction-sensitive level-four/log-signature functional, or a higher/longer untouched zero-gap window — retain organization beyond its complete quantized length-four-block table under the exact uniform Markov-type null from `VIS-099` and `VIS-100`?

Any next attempt must differ materially from the closed `VIS-101` design. Reusing the same binary-median quotient, the same target block, and the same `(1,2,1,3)` statistic with cosmetic rendering or equivalent normalization is not a new test.

If a residual survives, is it stable under independently fixed nearby representation choices and appropriately matched non-arithmetic source controls strongly enough to distinguish quotient-specific chronology from generic longer memory, nonstationarity, or random-matrix structure?

The broader visual question remains open as well: after the classified analytic, spacing, persistence, finite-memory, and low-signature quotients, is there any mesoscopic or nonlocal geometry of the zeta zero configuration that survives appropriately matched source controls in a statement meaningful without the rendering?

## Why it may matter

`VIS-097` identifies an exact degree of freedom absent from the complete unordered local-four-block inventory: order-dependent interaction between nonparallel local area modes. `VIS-098` prevents treating exact real-valued local-block preservation as automatically resampleable. `VIS-099` supplies an exact conditional experiment after a finite quotient, and `VIS-100` makes its support size and uniform sampling constructive.

`VIS-101` is the first substantive source test of that machinery and is negative. That is useful because it removes the simplest attractive interpretation: chronology capacity by itself is not evidence that the low zeta-zero sequence occupies an exceptional location inside the admitted local-memory quotient. A surviving route now has to earn its additional information carrier rather than merely repeat the same test with a different picture.

This keeps three notions separate: generic chronology capacity, chronology beyond a specified finite local quotient, and arithmetic/source specificity. A future separation from the conditioned Markov-type null would establish only the middle statement. Stronger arithmetic interpretation still requires surviving representation controls and relevant non-arithmetic spectral/source baselines.

## Decisive test

Choose one materially new source-specific design before inspecting its confirmation residual. Freeze the source window or height regime, unfolding convention, three-delay coordinates, endpoint treatment, finite quantizer and symbol embedding, and one direction-sensitive fourth-level/log-signature statistic or low-dimensional projection. If the change from `VIS-101` is a multi-bin quantizer, derive its thresholds from disjoint exploratory/training material or an external fixed rule rather than from the confirmation block. If the change is the statistic or scale, keep the other representation choices fixed enough that the new information boundary is explicit.

Build the quantized three-context transition multigraph and complete quantized length-four-block count table. Compute the exact Whittle cardinality `W` from `VIS-100`; reject the representation if `W=1`. When exhaustive enumeration is feasible, use it. Otherwise use the exact completion-count sampler and report sampling uncertainty separately from the finite-source question. A large `W` is not itself evidence of power.

The controls must preserve the initial quantized triple and every quantized length-four-block count exactly. Treat the finite quantizer as part of the hypothesis: do not apply the exact conditional claim to the original real-valued path, and do not reconstruct within bins without a separate leakage model.

Keep a new chronology route only if the pre-registered directional residual survives untouched confirmation and reasonable independently fixed representation perturbations. A positive result rejects the conditioned homogeneous order-three Markov explanation on that finite quotient; it still does not establish zeta arithmetic. Before any arithmetic interpretation, compare against relevant matched non-arithmetic source models, including finite-size random-matrix or other spectral controls appropriate to the chosen observable.

Kill or narrow the route if the type class is degenerate, the effect disappears on confirmation, the result is recreated by the matched source control, or the separation depends materially on post-hoc threshold/statistic/window selection. The `VIS-101` binary-median `(1,2,1,3)` experiment on `g_71,...,g_106` is already killed and must not be rerun as purported confirmation.

For any alternative topological or multiscale route, state the metric/graph/path/filtration and the information carrier explicitly, then apply the analogous quotient test: identify what information the construction actually retains, construct a nondegenerate control preserving the admitted lower information, and test the residual rather than the visual texture.

## Evidence boundary

`VIS-008` and `VIS-013` through `VIS-019` are analytic, topological, information-loss, or prior-art controls; they do not classify every possible nonlocal zero statistic. `VIS-092` through `VIS-096` exactly bound several persistence, transition-graph, and low-signature constructions by local gap/block information. `VIS-097` proves only that fixed three-delay signature level four can distinguish some alternative assemblies with the same local edge inventory; it does not establish source specificity, reconstruction, or a zeta effect.

`VIS-098` proves a sufficient uniqueness condition for exact real-valued local-block reassembly and the corresponding almost-sure genericity statement under absolutely continuous finite-dimensional laws. It does not invalidate quantized controls. `VIS-099` proves the exact conditional-uniform Markov-type law **only on the fixed finite-alphabet quotient**. `VIS-100` supplies the classical exact type-class count and exact uniform completion sampler on that same quotient.

`VIS-101` proves only a finite negative statement for one binary quantizer, one low-zero training/target split, and one pre-selected fourth-level coordinate. It does not show that every quantized chronology statistic is null, that higher zeros behave identically, that a multi-bin quotient is uninformative, or that the Markov-type null is a complete non-arithmetic source model. Conversely, future work may not treat the negative binary result as permission to search many thresholds, coordinates, and windows until one appears exceptional.

No finding in this chain establishes a mesoscopic fractal dimension, a new zeta-zero law, an RH criterion, or a distinction between zeta and a suitably matched higher-order point-process/control ensemble. This remains an accepted research direction, not evidence of such a distinction.

## Research disposition

Accepted in further narrowed form. The finite-quotient null mechanics are closed by `VIS-099` and `VIS-100`, and `VIS-101` closes the first frozen binary-median source experiment with an exact negative result. The next independent result must change the information carrier or scale materially and freeze that change before confirmation; another refinement of the same null machinery or a cosmetic rerun of the killed binary design is not progress.