---
id: CLUE-visual-exploration-zeta-three-gap-conditional-residual
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-020-three-gap-markov-closure-maxent-information-baseline.md
  - research/visual_exploration/findings/VIS-023-three-gap-cmi-markov-order-likelihood-ratio.md
  - research/visual_exploration/findings/VIS-024-three-gap-residual-interaction-pearson-geometry.md
  - research/visual_exploration/findings/VIS-025-three-gap-pearson-fibers-correspondence-analysis.md
  - research/visual_exploration/findings/VIS-035-three-gap-ca-spectrum-maximal-correlation.md
  - research/visual_exploration/findings/VIS-036-three-gap-empirical-ca-pearson-null-floor.md
  - research/visual_exploration/findings/VIS-037-three-gap-lrt-pearson-local-equivalence-control.md
  - research/visual_exploration/findings/VIS-057-markov-closure-total-variation-orientation-stability.md
  - research/visual_exploration/findings/VIS-058-overlapping-triple-dependence-fisher-orientation-error.md
  - research/visual_exploration/findings/VIS-059-overlap-collisions-are-periodic-cylinder-masses.md
  - research/visual_exploration/SOURCES.md
---

# Does an adjacent-pair-marginal-preserving three-gap residual expose zeta-specific higher-order structure?

## Observation

`VIS-019` closes every visual observable determined only by one or two consecutive unfolded gaps unless the finite-size CUE/arithmetic baseline is removed. The accepted multiscale clue explicitly leaves three-or-more-gap organization as a live channel, but raw higher-order spacing statistics are themselves established random-matrix objects. A sharper object is therefore the part of a three-gap joint law not determined by its two overlapping adjacent-pair marginals.

For a fixed finite partition of unfolded gaps, write `P3(i,j,k) = P(G_{n-1} in i, G_n in j, G_{n+1} in k)`, with adjacent-pair marginals `P12(i,j)`, `P23(j,k)` and middle marginal `P2(j)`. The first-order Markov closure carrying those two pair marginals is `Q(i,j,k) = P12(i,j) P23(j,k) / P2(j)` wherever `P2(j) > 0`. Thus `Delta = P3 - Q` isolates coarse three-gap conditional dependence beyond the adjacent two-gap marginals.

`VIS-020` and `VIS-023` make the scalar information side exact: `Q` is the unique maximum-entropy completion of the two adjacent-pair marginals, `D(P3 || Q)=I(G_{n-1};G_{n+1}|G_n)`, and the empirical conditional mutual information is the log-likelihood-ratio statistic for testing first-order Markov closure under the fixed partition.

`VIS-024`, `VIS-025`, and `VIS-035` make the visual geometry equally explicit. In each fixed middle-gap fiber, Pearson-whitening turns the residual into a correspondence-analysis matrix whose nontrivial singular values are the classical principal-inertia modes; the leading normalized singular value is the Hirschfeld-Gebelein-Renyi maximal correlation between the two outer gap bins conditioned on that middle bin. The full weighted squared spectrum is exactly the Pearson `chi^2` divergence from the same Markov closure, and `I<=log(1+chi_P^2)`.

`VIS-036` fixes the empirical scale of that visual spectrum. With `m` overlapping triples and empirical fiber counts `n_j`, `X_P^2 = m chi_P^2 = sum_j n_j sum_l rho_hat_(j,l)^2` is exactly the classical Pearson first-order-versus-second-order Markov statistic. Under a regular fully supported first-order `s`-state null it has asymptotic `chi^2` law with `nu=s(s-1)^2` degrees of freedom, so the empirical aggregate CA energy has positive floor `E[chi_P^2]=nu/m+o(1/m)` even when the population conditional dependence is zero. A visually nonzero empirical singular spectrum is therefore not itself evidence of genuine higher-order structure.

`VIS-037` links the two scalar sides at the level of each finite fitted table. If `e_ijk` are the fitted Markov-closure counts and `eta = max_(e_ijk>0) |n_ijk/e_ijk-1| < 1`, then `|G^2-X_P^2| <= [eta/(3(1-eta)^2)] X_P^2`. Thus in a well-occupied local-residual regime, `G^2` and total `X_P^2` are deterministically forced to be the same quadratic interaction channel to first order. Their agreement is a useful implementation check but not independent replication. When `eta` is large or fitted-positive cells are empty, their separation primarily diagnoses departure from that local regime and must itself be matched against the control process before receiving arithmetic interpretation.

`VIS-057`--`VIS-059` now separate a second issue that the earlier formulation left too implicit: **geometric residual stability and statistical observation stability are different layers**. `VIS-057` gives a deterministic finite-alphabet `L^1` propagation bound from raw three-gap law error through recomputed Markov closure to Fisher-residual orientation. `VIS-058` gives the exact mean-squared error of an empirical law built from overlapping triples in terms of lagged block-collision covariances rather than an i.i.d. effective-size guess. `VIS-059` identifies the exceptional overlap lags exactly: for triples, the `h=1` and `h=2` collision channels are the `aaaa` and `ababa` periodic cylinders, with population-triple-law ceilings through `aaa` and `aba` mass. Long-lag uncertainty is therefore a separate process-dependence question, not something that can be hidden inside the short-range overlap correction.

The candidate signal is a reproducible **zeta-minus-matched-control difference in these already identified dependence quantities or in the allocation of their Pearson energy across CA modes**, after both lower-order structure and a defensible source-specific uncertainty model are accounted for. Nonzero dependence inside zeta alone, or a Fisher direction whose uncertainty cone includes arbitrary rotations, is not a signal.

## Research question

For high unfolded zeta zeros near height `T`, does the residual tensor `Delta_T`, its conditional mutual information, or its conditional principal-inertia/maximal-correlation spectrum differ from the corresponding finite-size CUE or sine-kernel-plus-arithmetic baseline after the known one-gap and two-gap laws are matched? Is any surviving difference stable across pre-registered partitions, unfoldings, disjoint windows, and multiple heights, with an uncertainty budget that explicitly separates deterministic overlap geometry from genuine long-range dependence?

The target is not nonzero `Delta`, nonzero CMI, nonzero maximal correlation, a dominant correspondence-analysis mode, rejection of a first-order Markov null, or a finite-sample difference between `G^2` and `X_P^2` by itself: generic determinantal processes can have genuine higher-order dependence, finite samples generate positive fitted residual floors, and sparse/nonlocal tables can separate different power-divergence coordinates. The candidate signal is the **zeta-minus-matched-RMT residual of the irreducible three-gap conditional-dependence structure with a nontrivial process-aware stability margin**.

## Why it may matter

This is one of the smallest information channels that genuinely lies beyond `VIS-019`. It removes the two overlapping adjacent-pair marginals algebraically before searching for geometry, rather than comparing a raw three-gap cloud with Poisson or infinite-size random-matrix theory. The later findings give complementary but mathematically linked views of exactly the same residual channel: nonlinear information distance through CMI, quadratic interaction energy through Pearson divergence, a visually interpretable spectrum through conditional principal inertia/maximal correlation, and a deterministic perturbation route from raw-law uncertainty to Fisher-direction uncertainty.

The process-aware layer is important because the observations used to form consecutive triples overlap. `VIS-058` and `VIS-059` show that replacing the number of triples by a guessed effective sample size confounds two mathematically different effects: finite periodic self-overlap and separated-block dependence. If a reproducible zeta-minus-control excess survives finite-size CUE/arithmetic baselines and remains outside the propagated orientation uncertainty on every pre-registered view, it would localize candidate arithmetic information at irreducible three-gap order. If it does not, the experiment closes without mistaking estimator dependence for residual geometry.

## Decisive test

Use large high-zero windows at several heights for which finite-size baselines are meaningful. Pre-register a small family of stable partitions before looking at zeta-minus-control differences. Fix the partition, support rule, unfolding convention, closure convention, and common Fisher reference within each comparison panel. In each window, estimate `P3`, `P12`, `P23`, and `P2`, form that window's own maximum-entropy closure `Q`, and compute the same fixed battery on every dataset: `I=D(P3||Q)`; `G^2=2mI`; the Pearson interaction divergence `chi_P^2`; `X_P^2=m chi_P^2`; the maximum fitted-relative-residual diagnostic `eta=max_(e_ijk>0)|n_ijk/e_ijk-1|`; and the complete per-fiber principal-inertia spectrum, including the leading HGR coefficient with its middle-state weight/count.

Use the exact identity `X_P^2=sum_j n_j sum_l rho_hat_(j,l)^2` as an internal consistency check. Whenever `eta<1`, also verify the deterministic `VIS-037` bound between `G^2` and `X_P^2`; violation means inconsistent counts, fitted closure, support, or normalization rather than an interesting data feature. Do not count agreement of `G^2` and total `X_P^2` as two independent confirmations.

For the uncertainty layer, treat the observed consecutive triples as an overlapping-block sample rather than as `m` independent observations. For any stochastic/process model actually invoked, evaluate or conservatively bound the exact `VIS-058` raw-law second moment

`V_m = (1/m^2)[m(1-q_3)+2 sum_(h=1)^(m-1)(m-h)(c_h-q_3)]`.

Handle the exceptional lags separately. Use `VIS-059` to expose `c_1=Pr(aaaa)` and `c_2=Pr(ababa)` when extension information is available, or the safe population-triple-law envelopes based on `p_1=P3(aaa)` and `p_2=P3(aba)` when only the triple law is justified. For `h>=3`, use only a source-appropriate dependence theorem, validated block/resampling model, or explicit conservative envelope; do not insert an i.i.d. or generic mixing rate merely because it produces a finite error bar. Propagate the resulting raw-law radius through `VIS-057` and require the zeta/control Fisher-direction separation to exceed the resulting orientation uncertainty by a pre-specified margin.

The two sources do not automatically have the same inferential semantics. Independent finite-size CUE matrices provide a genuine ensemble when sampled as such. A fixed table of Riemann zeros is deterministic; disjoint height windows give valuable replication/robustness checks but do not by themselves manufacture an i.i.d. population model. Any probabilistic confidence statement on the zeta side must state the stationarity/ergodicity, random-window, block-resampling, or other process assumption that makes it meaningful. Without such a model, keep the zeta comparison descriptive and require replication across pre-registered disjoint windows rather than attaching a pseudo-confidence interval.

Apply the identical residual construction separately to `CUE_{N_e(T)}` and, where available, the finite-height Riemann-kernel/arithmetic correction rather than a Poisson or shuffled-gap control. Compare zeta-minus-control differences in the pre-registered scalar statistics and in the full weighted singular spectrum with the process-aware uncertainty above. Do not select a favorable middle-gap fiber, singular mode, binning, height, dependence envelope, or support edit after seeing the separation. Changes of partition/support/reference are separate robustness analyses and require their own stability accounting rather than being folded into the fixed-representation `VIS-057` bound.

Keep the direction only if a zeta-minus-baseline effect reproduces across heights/windows, survives the matched finite-size/arithmetic baseline, and remains outside the propagated uncertainty margin under a defensible dependence model. Kill it if the residual agrees with the matched determinantal baseline, if the Fisher-direction margin collapses after overlap/dependence accounting, or if the apparent separation is a partition, finite-size, support, multiplicity, sparsity, unfolding, or resampling-model artifact.

## Evidence boundary

The Markov-closure/max-entropy identity, likelihood-ratio interpretation, Pearson interaction geometry, correspondence analysis, principal inertia components, HGR maximal correlation, `D<=log(1+chi^2)` comparison, Pearson Markov-order chi-square calibration, and local relationship between Pearson and likelihood-ratio power-divergence statistics are classical probability/statistics/information-theory structures specialized to this three-gap setup in `VIS-020`, `VIS-023`, `VIS-024`, `VIS-025`, `VIS-035`, `VIS-036`, and `VIS-037`. Higher-order consecutive-spacing correlations are established random-matrix prior art. The total-variation propagation, exact overlapping-block second-moment interface, and periodic-cylinder decomposition in `VIS-057`--`VIS-059` are durable Mathia-side control results, not evidence that zeta possesses an anomalous residual.

The first-order-Markov floors in `VIS-023` and `VIS-036` are not models of zeta or CUE. The `VIS-037` `eta` gate is a finite-table representation diagnostic, not a statistical null model. Likewise, the `VIS-058` mixing example is conditional: it does not establish that zeta gaps or a chosen CUE construction satisfy a particular mixing law. `VIS-059` isolates the short-lag overlap channels but does not supply the missing long-lag process model. A fixed deterministic zeta window does not become a repeated stochastic sample merely because overlapping words can be counted.

This clue proposes a controlled residualization test designed to remove the exact lower-order channel closed by `VIS-019` while preventing estimator dependence from being mistaken for residual geometry. Its accepted status means the question has survived scope, mathematical-coherence, and baseline/prior-art triage; it does not assert that a zeta-specific residual exists.

## Research disposition

Accepted as a live experiment, now with the inferential boundary pinned as tightly as the geometry. The residual object, scalar information coordinates, Pearson/CA/HGR geometry, local power-divergence consistency check, raw-law perturbation map, overlapping-triple variance identity, and short-range periodic collision channels are all explicit. The remaining unresolved question is empirical and source-specific: whether zeta zeros exhibit a reproducible excess over matched finite-size CUE/arithmetic controls **after** a defensible long-range uncertainty model leaves a nontrivial residual-orientation margin. Further Fisher algebra is not the next gate; obtaining or falsifying that source-specific uncertainty model is.