---
id: CLUE-arithmetic-fidelity-accumulated-moving-window-resolution
type: research-clue
status: proposed
origin: mind
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-486-moving-hankel-determinants-recover-finite-dirichlet-depth-at-sharp-exponential-precision.md
  - research/arithmetic_fidelity/findings/AF-487-critical-moving-window-noise-has-sharp-inverse-depth-log-generator-resolution.md
  - research/arithmetic_fidelity/mind/intuition/MI-070-exact-sample-cardinality-and-sampling-geometry-are-different-fidelity-resources.md
---

# Does an accumulated rightward sample history beat the inverse-depth generator-resolution law?

## Observation

AF-486 and AF-487 analyze a positive ordered Dirichlet source through one fixed-width Hankel window whose base point moves to `t`. At the sharp absolute noise scale for retaining the `J`th generator, `epsilon q_J^(-t)`, AF-487 proves a `Theta(1/t)` local minimax resolution law in `log q_J`. Its lower bound is explicitly stated only for the single-window observation channel, and AF-487 leaves open what happens when a decoder may retain an expanding history of earlier rightward samples.

The same two-source construction suggests a sharper possibility. If `q_1(t)=q_0 exp(gamma/t)`, then at any sample location `s<=t+O(1)` the source difference carries the factor `1-exp(-gamma s/t)`, which remains `O(gamma)` uniformly over the whole prefix. This hints that even a coherent accumulated history with pointwise critical-scale errors may fail to improve the `1/t` order, but that uniform history statement is not established by the persisted finding.

## Research question

For fixed source depth `J` and step `h`, suppose the decoder observes an expanding rightward lattice prefix rather than only the terminal `2J-1` window, with one coherent noisy sample at each location and pointwise error budget comparable to the local critical atom scale, for example

`|eta(s)| <= epsilon q_J^(-s)`

for all sampled `s` up to the terminal scale `t+O(1)`. Is the minimax risk for `log q_J` still `Theta(1/t)`, or can accumulation of the earlier samples produce `o(1/t)` resolution?

## Why it may matter

A positive answer would show that AF-487's inverse-depth loss is not an artifact of discarding earlier windows: the whole noisy rightward trajectory prefix would carry no better asymptotic generator resolution at the critical relative scale. A negative answer would identify accumulated observation history as a genuinely new fidelity resource, separate from sample cardinality inside one moving window and from the absolute precision threshold isolated by AF-486.

## Decisive test

Fix a precise accumulated observation model on one sampling lattice and first attack the lower bound with AF-487's pair `q_1(t)=q_0 exp(gamma/t)`. Prove or disprove a uniform estimate showing that the two complete noisy prefixes can share one admissible datum for a fixed sufficiently small `gamma`, taking care that overlapping windows correspond to the same observed samples rather than independent noise copies. If that indistinguishability survives, the terminal AF-487 window already supplies the matching `O(1/t)` upper bound and the accumulated-history rate remains sharp. If it fails, isolate the earliest sample scale or cross-window consistency relation responsible for a strictly smaller risk and derive the resulting rate.

## Evidence boundary

AF-487 proves only the one-window local minimax law. The uniform-prefix indistinguishability estimate above is a source-motivated candidate argument, not persisted mathematical evidence. The answer can also depend on the exact noise geometry: independent per-window errors, one coherent pointwise error process, stochastic noise, or a different scaling from `q_J^(-s)` are different experiments and must not be conflated.