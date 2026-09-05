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
  - research/visual_exploration/SOURCES.md
---

# Does an adjacent-pair-marginal-preserving three-gap residual expose zeta-specific higher-order structure?

## Observation

`VIS-019` closes every visual observable determined only by one or two consecutive unfolded gaps unless the finite-size CUE/arithmetic baseline is removed. The accepted multiscale clue explicitly leaves three-or-more-gap organization as a live channel, but raw higher-order spacing statistics are themselves established random-matrix objects. A sharper object is therefore the part of a three-gap joint law not determined by its two overlapping adjacent-pair marginals.

For a fixed finite partition of unfolded gaps, write `P3(i,j,k) = P(G_{n-1} in i, G_n in j, G_{n+1} in k)`, with adjacent-pair marginals `P12(i,j)`, `P23(j,k)` and middle marginal `P2(j)`. The first-order Markov closure carrying those two pair marginals is `Q(i,j,k) = P12(i,j) P23(j,k) / P2(j)` wherever `P2(j) > 0`. Thus `Delta = P3 - Q` isolates coarse three-gap conditional dependence beyond the adjacent two-gap marginals.

`VIS-020` and `VIS-023` make the scalar information side exact: `Q` is the unique maximum-entropy completion of the two adjacent-pair marginals, `D(P3 || Q)=I(G_{n-1};G_{n+1}|G_n)`, and the empirical conditional mutual information is the log-likelihood-ratio statistic for testing first-order Markov closure under the fixed partition.

`VIS-024`, `VIS-025`, and `VIS-035` make the visual geometry equally explicit. In each fixed middle-gap fiber, Pearson-whitening turns the residual into a correspondence-analysis matrix whose nontrivial singular values are the classical principal-inertia modes; the leading normalized singular value is the Hirschfeld-Gebelein-Renyi maximal correlation between the two outer gap bins conditioned on that middle bin. The full weighted squared spectrum is exactly the Pearson `chi^2` divergence from the same Markov closure, and `I<=log(1+chi_P^2)`.

`VIS-036` now fixes the empirical scale of that visual spectrum. With `m` overlapping triples and empirical fiber counts `n_j`,

`X_P^2 = m chi_P^2 = sum_j n_j sum_l rho_hat_(j,l)^2`

is exactly the classical Pearson first-order-versus-second-order Markov statistic. Under a regular fully supported first-order `s`-state null it has asymptotic `chi^2` law with `nu=s(s-1)^2` degrees of freedom, so the empirical aggregate CA energy has positive floor `E[chi_P^2]=nu/m+o(1/m)` even when the population conditional dependence is zero. A visually nonzero empirical singular spectrum is therefore not itself evidence of genuine higher-order structure.

The candidate signal is a reproducible **zeta-minus-matched-control difference in these already identified dependence quantities**, not nonzero dependence inside zeta alone.

## Research question

For high unfolded zeta zeros near height `T`, does the residual tensor `Delta_T`, its conditional mutual information, or its conditional principal-inertia/maximal-correlation spectrum differ from the corresponding finite-size CUE or sine-kernel-plus-arithmetic baseline after the known one-gap and two-gap laws are matched? Is any surviving difference stable across partitions, unfoldings, disjoint windows, and multiple heights, with a coherent effective-size scaling?

The target is not nonzero `Delta`, nonzero CMI, nonzero maximal correlation, a dominant correspondence-analysis mode, or rejection of a first-order Markov null by itself: generic determinantal processes can have genuine higher-order dependence, and finite samples also generate a positive fitted residual floor. The candidate signal is the **zeta-minus-matched-RMT residual of the irreducible three-gap conditional-dependence structure**.

## Why it may matter

This is one of the smallest information channels that genuinely lies beyond `VIS-019`. It removes the two overlapping adjacent-pair marginals algebraically before searching for geometry, rather than comparing a raw three-gap cloud with Poisson or infinite-size random-matrix theory. The later findings now give complementary but mathematically linked views of exactly the same residual channel: nonlinear information distance through CMI, quadratic interaction energy through Pearson divergence, a visually interpretable spectrum through conditional principal inertia/maximal correlation, and a classical finite-sample Pearson calibration for the complete empirical spectrum.

That linkage reduces the risk of inventing a visually appealing descriptor or mistaking plug-in noise for structure after inspecting zeta data. If a reproducible excess survives finite-size CUE and known arithmetic corrections simultaneously in the pre-registered information and spectral summaries, it would localize candidate arithmetic information at irreducible three-gap order. If it does not, it closes the next natural extension of the adjacent-gap visual program.

## Decisive test

Use large high-zero windows at several heights for which finite-size baselines are meaningful. Pre-register a small family of stable partitions before looking at zeta-minus-control differences. In each window, unfold locally, estimate `P3`, `P12`, `P23`, and `P2`, form that window's own maximum-entropy closure `Q`, and compute the same fixed battery on every dataset: `I=D(P3||Q)`; `G^2=2mI`; the Pearson interaction divergence `chi_P^2`; `X_P^2=m chi_P^2`; its fixed-alphabet scale control `chi_P^2/(s-1)` when the outer alphabets have equal size `s`; and the complete per-fiber principal-inertia spectrum, including the leading HGR coefficient `rho_(j,1)` with the corresponding middle-state weight/count.

Use the exact identity `X_P^2=sum_j n_j sum_l rho_hat_(j,l)^2` as an internal consistency check. For synthetic or otherwise justified first-order-Markov calibration, compare `G^2` and `X_P^2` against the common `nu=s(s-1)^2` asymptotic scale, or use exact/process-level Monte Carlo when occupancy is sparse. Treat this only as an estimator/model-order sanity check; do not subtract `nu/m` from zeta and interpret the remainder as arithmetic.

Apply the identical construction separately to `CUE_{N_e(T)}` and, where available, the finite-height Riemann-kernel/arithmetic correction rather than a Poisson or shuffled-gap control. Compare zeta-minus-control differences in the pre-registered scalar statistics and in the full weighted singular spectrum with multiplicity-aware uncertainty. Do not select a favorable middle-gap fiber, singular mode, binning, or height after seeing the zeta/control separation. Repeat with disjoint windows and the pre-registered estimator/bin perturbations, preserving the same support rule on both sides.

Keep the direction only if a zeta-minus-baseline effect reproduces across heights/windows and remains visible in a mathematically coherent combination of CMI/Pearson/spectral summaries, without being explained by finite-sample bias, unfolding drift, support trimming, known higher-order random-matrix spacing statistics, or the arithmetic correction already encoded in the established kernel expansion. Kill it if the residual agrees with the matched determinantal baseline or if the apparent separation is a partition, finite-size, support, multiplicity, or unfolding artifact.

## Evidence boundary

The Markov-closure/max-entropy identity, likelihood-ratio interpretation, Pearson interaction geometry, correspondence analysis, principal inertia components, HGR maximal correlation, `D<=log(1+chi^2)` comparison, and Pearson Markov-order chi-square calibration are classical probability/statistics/information-theory structures specialized exactly to this three-gap setup in `VIS-020`, `VIS-023`, `VIS-024`, `VIS-025`, `VIS-035`, and `VIS-036`. Higher-order consecutive-spacing correlations are established random-matrix prior art. No new arithmetic signal, asymptotic scaling, or RH criterion is established here.

The first-order-Markov floors in `VIS-023` and `VIS-036` are not models of zeta or CUE. They only prevent finite-sample fitted residuals from being over-interpreted before the matched-process comparison. The bounded Pearson normalization is likewise only a scale control for a fixed alphabet size; it does not make different partitions equivalent. The CA/HGR spectrum is invariant to relabeling/orthogonal contrast choices inside a fixed table but not to changing the partition, unfolding, estimator, height window, or support rule.

This clue proposes a controlled residualization test designed to remove the exact lower-order channel closed by `VIS-019`. Its accepted status means the question has survived scope, mathematical-coherence, and baseline/prior-art triage; it does not assert that a zeta-specific residual exists.

## Research disposition

Accepted as a live experiment. The baseline is now pinned on both scalar and visual sides: `VIS-023` supplies the likelihood-ratio/CMI test and its first-order-Markov sampling floor; `VIS-024`, `VIS-025`, and `VIS-035` identify the Pearson/CA/HGR geometry; and `VIS-036` shows that the complete empirical CA energy is exactly the Pearson Markov-order statistic with its own `nu/m` first-order-null floor. The unresolved question is therefore whether zeta zeros exhibit a reproducible excess over matched finite-size CUE/arithmetic controls in this pre-specified family of three-gap dependence summaries after both estimator noise and ordinary determinantal higher-order dependence are accounted for.