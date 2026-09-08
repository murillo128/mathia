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
  - research/visual_exploration/SOURCES.md
---

# Does the critical-strip geometry of zeta contain a nontrivial multiscale or fractal signature?

## Observation

The visual-exploration line has progressively closed several attractive channels that do not add an independent arithmetic information carrier. Infinitesimal zero portraits collapse to the local analytic normal form; concentric `log|F|` shells reduce to Poisson-Jensen source plus boundary data; phase/modulus and overlapping-disk phase information collapse to ordinary analytic continuation up to global phase; phase winding is divisor count; raw adjacent-gap geometry has strong finite-size random-matrix baselines; and ordinary one-dimensional persistence is exactly the unordered adjacent-gap multiset.

The delay-geometry branch gives a sharper information hierarchy. `VIS-093` through `VIS-096` show that ordinary fixed-window persistence, static delay graphs, and unaugmented delay-path signatures through level three are determined by increasingly local block inventories; planar level four is also locally determined. `VIS-097` proves the first genuine escape: in three delay dimensions, level four can distinguish different Eulerian assemblies of the same length-four-block inventory through an exact area-area commutator. Thus level four can carry chronology in principle.

`VIS-098` through `VIS-100` make the source-specific null exact. Exact real-valued block reassembly is generically degenerate, but after a fixed finite quantization the complete quantized length-four-block table is an order-three Markov type. Conditional on that table and the initial triple, every compatible word has the same probability under every homogeneous order-three Markov chain. Whittle's formula gives the exact type-class cardinality and completion counts give exact uniform sampling.

The first two low-zero source tests were negative on `g_71,...,g_106`: `VIS-101` gave exact `p=493/750` under a binary training-median quotient, and `VIS-102` gave `p=209/219` under a balanced ternary training-defined quotient for the same pre-existing word coordinate. `VIS-103` then proved that applying that same functional to degree-four log-signature instead of signature is only a fixed translation on each exact type class.

`VIS-104` removed the remaining open-ended coordinate search by selecting the canonical three-dimensional area-area subspace `C_AA=[L_2,L_2]`, its orthogonal projector `P_AA`, and the basis-independent squared statistic

`T_AA(X)=||P_AA ell_4(X)-E_null[P_AA ell_4]||^2`.

`VIS-105` has now executed the resulting fresh-source test on the deterministic next disjoint block `g_107,...,g_142`, keeping the ternary quantizer, embedding, delay construction, exact Markov-type null, and `T_AA` fixed. The fresh class is genuinely nondegenerate: `W=416` and `P_AA` takes `114` distinct projected values. Nevertheless the observed statistic has exact upper-tail probability

`p=183/416=0.439903846...`.

Thus the first pre-frozen fresh-source area-area test is also negative. The chronology carrier exists mathematically and survives the exact local-block quotient, but it has not produced evidence that this zeta-zero block is unusual within that quotient.

## Research question

After the negative fresh `P_AA` test, is there any **predeclared source scale or materially different nonlocal information carrier** whose residual survives an exact lower-information null and then survives the appropriate non-arithmetic source controls?

For the existing area-area route, the next admissible question is no longer “does another convenient window look unusual?”. If `P_AA` is pursued further, freeze a family of disjoint zero windows or a height regime, the quantizer/embedding, and a combined or family-wise decision rule before inspecting those new residuals. The purpose would be to test replication or scale behavior rather than perform sequential one-window search.

A genuinely different visual/multiscale route remains admissible when its metric, filtration, transformation, or information carrier is specified independently and its apparent structure can be translated into a falsifiable statement beyond the lower-order objects already classified here.

## Why it may matter

`VIS-097` through `VIS-105` now separate four questions that are easy to conflate: whether a representation can remember chronology in principle; whether that information survives a precisely stated local quotient; whether a frozen zeta source instance is unusual under the quotient; and whether any surviving residual is arithmetic-specific rather than generic spectral memory.

The first two are answered positively for the area-area channel: level four can encode assembly order and the fresh ternary exact type class leaves `P_AA` nondegenerate. The third has so far answered negatively on the first clean fresh block. The fourth has therefore not yet been reached; finite-size CUE and finite-height arithmetic controls remain mandatory before any arithmetic interpretation of a future positive conditional residual.

The broader visual question remains open because the line has classified many representation-induced textures without classifying every possible mesoscopic or nonlocal observable of the zero configuration. The useful frontier is increasingly an information-design problem: retain structure not forced by the chosen coordinates or local inventory, then demand a source-specific control that could actually falsify the interpretation.

## Decisive test

For a continued `P_AA` program, predeclare the next source panel before evaluating it: disjoint windows or height bands, unfolding convention, the already fixed ternary quantizer or an independently specified replacement, symbol embedding, delay coordinates, endpoint handling, `P_AA`, and the rule that combines evidence across the panel. Each window must first pass the exact Whittle nondegeneracy gate and the stronger `P_AA` nonconstancy gate.

Use exact enumeration whenever the type class is tractable and otherwise the exact completion-count sampler with its sampling uncertainty separated from the mathematical null. Do not select a favorable window, projected component, quantizer, or stopping point after looking at the residuals and then report the corresponding single-test tail as confirmation.

A replicated conditional separation would still establish only chronology beyond the admitted finite local quotient. Before calling it zeta-specific, compare with independently generated matched finite-size CUE or another source model appropriate to the chosen height and observable, including finite-height arithmetic corrections when they are known to matter.

If a different multiscale or visual route is chosen instead, state exactly what information it preserves and forgets, construct a nondegenerate matched quotient or surrogate, and predeclare the statistic before confirmation. Kill the route when the signal is reproduced by that control, collapses to a known analytic identity, or depends on post-hoc representation/window selection.

## Evidence boundary

`VIS-008` and `VIS-013` through `VIS-019` are analytic, topological, information-loss, or prior-art controls; they do not classify every possible nonlocal zero statistic. `VIS-092` through `VIS-096` bound several persistence, transition-graph, and low-signature constructions by local gap/block information. `VIS-097` proves only generic level-four chronology capacity in three delay dimensions.

`VIS-098` through `VIS-100` establish the exact finite conditional-null mechanics after quantization. `VIS-101` and `VIS-102` are finite negatives on one old block and one previously selected scalar coordinate. `VIS-103` is an affine representation-boundary theorem. `VIS-104` supplies a canonical area-area projection and exact admission rule. `VIS-105` is a finite negative on one new disjoint block: its class is nondegenerate, but `T_AA` is ordinary with exact `p=183/416`.

None of these results proves that all zeta-zero chronology is null, that higher zeros behave identically, that the Markov-type quotient is a complete random-matrix/source null, or that no other visual/multiscale information carrier can work. Conversely, `VIS-105` prevents treating the mere existence and nondegeneracy of the area-area channel as evidence for a source-specific residual.

No finding in this chain establishes a mesoscopic fractal dimension, a new zeta-zero law, a CUE/zeta separation at this statistic, or an RH criterion.

## Research disposition

Accepted in further narrowed form. The pre-registration-ready area-area experiment proposed after `VIS-104` has now been executed once on fresh disjoint source material and is an exact negative. That single finite result does not close all chronology, but it closes the immediate one-window `P_AA` test.

Further work should either predeclare a genuine replication/scale panel for the same area-area statistic or move to a materially different information carrier with untouched confirmation. Repeated adaptive window hunting with `P_AA` would not provide independent evidence. The broader critical-strip multiscale question remains live under those stricter controls.