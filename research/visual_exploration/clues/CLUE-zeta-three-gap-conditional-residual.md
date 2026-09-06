---
id: CLUE-visual-exploration-zeta-three-gap-conditional-residual
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
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
  - research/visual_exploration/findings/VIS-060-fixed-window-control-only-fisher-certificate.md
  - research/visual_exploration/findings/VIS-061-independent-control-replicate-l1-radius.md
  - research/visual_exploration/SOURCES.md
---

# Does an adjacent-pair-marginal-preserving three-gap residual expose zeta-specific higher-order structure?

## Observation

The line has isolated one precise higher-order channel. For a fixed finite partition of consecutive unfolded gaps, the adjacent-pair-preserving Markov completion

`Q(i,j,k)=P12(i,j) P23(j,k)/P2(j)`

removes exactly the two overlapping adjacent-pair marginals, and `Delta=P3-Q` is the remaining coarse three-gap conditional-dependence tensor. `VIS-020`, `VIS-023`, `VIS-024`, `VIS-025`, and `VIS-035` identify the same residual through conditional mutual information, likelihood ratio, Pearson interaction energy, correspondence-analysis principal inertia, and conditional HGR maximal correlation. `VIS-036` and `VIS-037` delimit the empirical Pearson floor and the local equivalence of Pearson and likelihood-ratio coordinates, so visually nonzero residual energy and agreement between those scalar statistics are not independent evidence.

The later stability results separate representation geometry from observation uncertainty. `VIS-057` propagates raw triple-law `L^1` error through the recomputed nonlinear Markov closure into a fixed-reference Fisher residual/direction error. `VIS-058` gives an exact second-moment interface for empirical laws formed from overlapping triples, and `VIS-059` identifies the exceptional short-lag collision terms with concrete periodic cylinders (`aaaa` and `ababa` for triples) rather than hiding them inside an effective-sample-size heuristic.

`VIS-060` sharpens the inferential boundary. A fixed finite zeta table does **not** need a stochastic process model merely to ask whether its residual vector or direction differs from the population residual of an independently simulated matched control. Once the zeta table and representation are frozen, a valid control-side raw-law radius alone yields a rigorous residual-distance/orientation interval whose probability is over the control simulation only. A zeta-side stochastic model is needed only for stronger claims that generalize beyond the frozen table or attach sampling semantics to the zeta sequence itself.

`VIS-061` now supplies one conservative way to obtain that missing control-side radius without pretending the overlapping triples inside a CUE matrix are independent. If `B` independently generated control matrices each contribute their entire empirical triple table on a fixed `K`-cell support, their average table obeys an explicit bounded-differences `L^1` radius of order `[sqrt(K)+sqrt(log(1/rho))]/sqrt(B)`. Independence is used only across complete control replicates; all within-matrix dependence is absorbed into each simplex-valued table.

The candidate signal remains a reproducible **zeta-minus-matched finite-size/arithmetic-control difference in irreducible three-gap structure**, not nonzero dependence within zeta alone.

## Research question

For high unfolded Riemann-zero windows, does the fixed lower-order-residualized three-gap tensor `Delta`, its CMI/Pearson magnitude, or its Fisher/CA orientation differ from the appropriate finite-size CUE or finite-height arithmetic baseline after the representation and confirmation rule are frozen?

At the lowest-assumption claim level, can a frozen zeta window be shown to lie outside a control-population residual ball or direction cone using fresh independent matched-control simulations and `VIS-060`/`VIS-061`? If such a fixed-window separation exists, does it then replicate across predeclared disjoint heights strongly enough to justify a broader source-specific uncertainty model rather than remaining an isolated finite-table anomaly?

## Why it may matter

This is one of the smallest channels beyond adjacent-gap geometry that is not algebraically determined by the one-gap and two-gap marginals. The current corpus now gives an unusually explicit audit chain from the raw triple table to information-theoretic and visual residual coordinates and from raw-law error to direction error.

`VIS-060` avoids a false methodological dichotomy. The experiment need not pretend that a deterministic zeta window is an i.i.d. sample, but it need not remain purely qualitative either. `VIS-061` removes the analogous shortcut on the control side: independent CUE matrices provide genuine replication even when the overlapping triples within each matrix remain dependent. A fixed arithmetic object can therefore be compared quantitatively with a random control population while keeping the probability statement on the side where genuine replication exists.

## Decisive test

Predeclare the zeta windows, unfolding, finite partition, declared support, Markov closure, common positive Fisher reference, scalar statistics, direction statistics, and any family-wise rule before confirmation. Generate fresh independent finite-size CUE controls at the effective matrix sizes appropriate to those heights; when a finite-height arithmetic correction is the intended baseline, include it explicitly rather than substituting infinite-size sine-kernel or shuffled-gap controls.

For each fixed comparison panel, let every independent control matrix contribute its **whole** empirical three-gap table `X_b` under the frozen representation, and average those tables to `P_hat`. As a safe default that makes no within-matrix independence claim, use the `VIS-061` replicate-level radius

`delta_B(rho)=min(2,[sqrt(K)+sqrt(2 log(1/rho))]/sqrt(B))`.

Propagate it through `VIS-057` to `a_B=6 delta_B/sqrt(h_min)`. If this generic radius is too loose, replace it only with a sharper CUE/control concentration argument that explicitly justifies the extra structure it uses; do not substitute the raw count of overlapping triples as an i.i.d. sample size.

For each frozen zeta window `Z`, compute its residual `Delta(Z)` exactly on the declared table. Use `VIS-060` first: require the observed fixed-zeta/control residual distance to exceed the resulting Fisher radius, or require the observed orientation interval to exclude the null direction being claimed. This fixed-window statement needs no zeta sampling model.

In parallel keep the scalar CMI/Pearson/CA consistency diagnostics from `VIS-023`--`VIS-037`, and do not count algebraically linked statistics as independent confirmations. If a sharper control construction or later zeta-population model uses overlapping-block sampling internally, account for it with the exact `VIS-058` collision interface and the short-lag periodic channels from `VIS-059` rather than a guessed effective sample size.

Only if a predeclared fixed-window separation survives should the experiment ask for the stronger claim. Repeat on disjoint, predeclared heights and then state explicitly what stationarity/ergodicity, random-window, block-resampling, or other zeta-side model would justify population-level uncertainty. Kill the arithmetic interpretation if the effect disappears under finite-size/arithmetic controls, does not clear the control-only uncertainty ball/cone, changes under the predeclared representation perturbations, or fails to replicate across heights.

## Evidence boundary

All current exact results concern the representation, its lower-order closure, its information/Pearson/CA geometry, and its perturbation/overlap controls. No canonical finding establishes an anomalous zeta three-gap residual.

`VIS-060` proves only that **control-side probability is enough for a fixed-table versus control-population comparison**. `VIS-061` supplies a generic replicate-level radius for independent control matrices, but it is deliberately conservative: it ignores information available inside each matrix and can become uninformative for fine supports or small Fisher-reference cells. Neither result turns one zeta window into a random sample, makes a selected window representative of other heights, or supplies a p-value for a data-dependent visual search.

Finite-size CUE corrections, higher-order spacing correlations, and finite-height arithmetic corrections are established prior art and remain mandatory baselines. Adaptive choices must be covered by fresh confirmation controls or a simultaneous construction. The clue therefore stays `accepted`, not `resolved`.

## Research disposition

Accepted as a live empirical experiment with two explicitly separated claim levels. The immediate gate is the lower-assumption one: obtain the actual higher-window zeta tables, freeze the representation, choose an independent-control replicate budget using `VIS-061` as a safe baseline, and test the fixed zeta residual against the **control-population** uncertainty ball/cone supplied by `VIS-060`. A sharper CUE-specific uncertainty theorem is optional if the generic replicate-level radius is too conservative. A source-specific stochastic model for zeta is a later requirement only if the fixed-window effect survives and the claim is to generalize beyond those frozen windows.