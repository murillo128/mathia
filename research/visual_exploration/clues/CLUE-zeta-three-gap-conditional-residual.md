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
  - research/visual_exploration/findings/VIS-062-simplex-replicate-l1-dimension-penalty.md
  - research/visual_exploration/findings/VIS-063-quadratic-markov-witness-paired-control-certificate.md
  - research/visual_exploration/SOURCES.md
---

# Does an adjacent-pair-marginal-preserving three-gap residual expose zeta-specific higher-order structure?

## Observation

The line has isolated one precise higher-order channel. For a fixed finite partition of consecutive unfolded gaps, the adjacent-pair-preserving Markov completion

`Q(i,j,k)=P12(i,j) P23(j,k)/P2(j)`

removes exactly the two overlapping adjacent-pair marginals, and `Delta=P3-Q` is the remaining coarse three-gap conditional-dependence tensor. `VIS-020`, `VIS-023`, `VIS-024`, `VIS-025`, and `VIS-035` identify the same residual through conditional mutual information, likelihood ratio, Pearson interaction energy, correspondence-analysis principal inertia, and conditional HGR maximal correlation. `VIS-036` and `VIS-037` delimit the empirical Pearson floor and the local equivalence of Pearson and likelihood-ratio coordinates, so visually nonzero residual energy and agreement between those scalar statistics are not independent evidence.

The later stability results separate representation geometry from observation uncertainty. `VIS-057` propagates raw triple-law `L^1` error through the recomputed nonlinear Markov closure into a fixed-reference Fisher residual/direction error. `VIS-058` gives an exact second-moment interface for empirical laws formed from overlapping triples, and `VIS-059` identifies the exceptional short-lag collision terms with concrete periodic cylinders (`aaaa` and `ababa` for triples) rather than hiding them inside an effective-sample-size heuristic.

`VIS-060` sharpens the inferential boundary. A fixed finite zeta table does **not** need a stochastic process model merely to ask whether its residual vector or direction differs from the population residual of an independently simulated matched control. Once the zeta table and representation are frozen, a valid control-side raw-law radius alone yields a rigorous residual-distance/orientation interval whose probability is over the control simulation only. A zeta-side stochastic model is needed only for stronger claims that generalize beyond the frozen table or attach sampling semantics to the zeta sequence itself.

`VIS-061` supplies a conservative way to obtain that missing control-side radius without pretending the overlapping triples inside a CUE matrix are independent. If `B` independently generated control matrices each contribute their entire empirical triple table on a fixed `K`-cell support, their average table obeys an explicit bounded-differences `L^1` radius with leading expectation scale `sqrt((K-1)/B)`. Independence is used only across complete control replicates; all within-matrix dependence is absorbed into each simplex-valued table.

`VIS-062` closes the obvious generic escape route. Uniform one-hot simplex replicates already force expected `L^1` error at least `(1/2)sqrt((K-1)/B)` once the binomial variance is at least one, and classical discrete-distribution minimax theory has the same `sqrt(K/B)` scale. Therefore a materially tighter **full-law** control radius must exploit additional CUE/internal structure, a coarser predeclared representation, a different propagated error geometry, or more independent matrices; a different distribution-free whole-replicate inequality cannot simply erase the support-size penalty.

`VIS-063` instantiates one of those allowed alternatives without claiming full-law recovery. It introduces the denominator-free conditional-dependence tensor

`C(P)_(ijk)=P_Y(j)P_(ijk)-P_XY(i,j)P_YZ(j,k)=P_Y(j)Delta(P)_(ijk)`

on positive middle fibers. For one frozen `||w||_infty<=1` direction, the quadratic contrast `tau_w(P)=<w,C(P)>` has an unbiased estimator from disjoint pairs of independent **whole control replicates**, with the dimension-free confidence radius

`r_B(rho)=min(4,sqrt(8 log(2/rho)/floor(B/2)))`.

This gains control efficiency by asking one predeclared scalar question rather than certifying the entire `K`-cell law or Fisher residual vector. It therefore complements rather than contradicts `VIS-061`/`VIS-062`.

The candidate signal remains a reproducible **zeta-minus-matched finite-size/arithmetic-control difference in irreducible three-gap structure**, not nonzero dependence within zeta alone.

## Research question

For high unfolded Riemann-zero windows, does the fixed lower-order-residualized three-gap tensor `Delta`, its CMI/Pearson magnitude, its Fisher/CA orientation, or a predeclared denominator-free quadratic residual witness differ from the appropriate finite-size CUE or finite-height arithmetic baseline after the representation and confirmation rule are frozen?

At the lowest-assumption claim level, can a frozen zeta window be shown to lie outside either a control-population residual ball/direction cone using `VIS-060`/`VIS-061`, or a predeclared scalar control interval using `VIS-063` and fresh independent matched-control simulations? If such a fixed-window separation exists, does it then replicate across predeclared disjoint heights strongly enough to justify a broader source-specific uncertainty model rather than remaining an isolated finite-table anomaly?

## Why it may matter

This is one of the smallest channels beyond adjacent-gap geometry that is not algebraically determined by the one-gap and two-gap marginals. The current corpus now gives an unusually explicit audit chain from the raw triple table to information-theoretic and visual residual coordinates, from raw-law error to direction error, and from independent whole-control replication to two honest confidence geometries of different strength.

`VIS-060` avoids a false methodological dichotomy. The experiment need not pretend that a deterministic zeta window is an i.i.d. sample, but it need not remain purely qualitative either. `VIS-061` removes the analogous shortcut on the control side: independent CUE matrices provide genuine replication even when the overlapping triples within each matrix remain dependent. `VIS-062` prevents the conservative full-law certificate from becoming an endless generic-inequality optimization problem. `VIS-063` then shows what a legitimate reduction looks like: freeze a mathematically interpretable residual direction and calibrate that scalar quadratic functional directly, rather than claiming the same full-vector guarantee with a mysteriously dimension-free radius.

## Decisive test

Predeclare the zeta windows, unfolding, finite partition, declared support, Markov closure, common positive Fisher reference when the Fisher route is used, target statistics, and any family-wise rule before confirmation. Generate fresh independent finite-size CUE controls at the effective matrix sizes appropriate to those heights; when a finite-height arithmetic correction is the intended baseline, include it explicitly rather than substituting infinite-size sine-kernel or shuffled-gap controls.

The **full-vector route** remains the conservative baseline. For each fixed comparison panel, let every independent control matrix contribute its whole empirical three-gap table `X_b` and average those tables to `P_hat`. Use the `VIS-061` radius

`delta_B(rho)=min(2,[sqrt(K-1)+sqrt(2 log(1/rho))]/sqrt(B))`

and propagate it through `VIS-057` to `a_B=6 delta_B/sqrt(h_min)`. For each frozen zeta table `Z`, require the observed fixed-zeta/control residual distance to exceed that Fisher radius, or require the observed orientation interval from `VIS-060` to exclude the null direction being claimed.

If that full-law ball is too loose, use the **lower-dimensional witness route** only after freezing one `||w||_infty<=1` direction independently of the confirmation controls. The direction may be specified mathematically in advance, derived from the frozen zeta table alone, or learned from a separate pilot control ensemble and then frozen. Pair fresh independent confirmation controls as in `VIS-063`, compute `T_hat_w`, and require

`|tau_w(Z)-T_hat_w| > r_B(rho)`

with

`r_B(rho)=min(4,sqrt(8 log(2/rho)/floor(B/2)))`.

Do not optimize `w` on the same confirmation controls and then attach the single-witness radius to the selected direction. If several witnesses, windows, partitions, or gauges are tested, predeclare the family and cover the multiplicity or use fresh confirmation data. Optimizing over the full `L^infty` witness ball recovers an `L^1` residual comparison and forfeits the low-dimensional advantage.

In parallel keep the scalar CMI/Pearson/CA consistency diagnostics from `VIS-023`--`VIS-037`, and do not count algebraically linked statistics as independent confirmations. If a sharper control construction or later zeta-population model uses overlapping-block sampling internally, account for it with the exact `VIS-058` collision interface and the short-lag periodic channels from `VIS-059` rather than a guessed effective sample size.

Only if a predeclared fixed-window separation survives should the experiment ask for the stronger claim. Repeat on disjoint, predeclared heights and then state explicitly what stationarity/ergodicity, random-window, block-resampling, or other zeta-side model would justify population-level uncertainty. Kill the arithmetic interpretation if the effect disappears under finite-size/arithmetic controls, does not clear the chosen control-only confidence geometry, changes under the predeclared representation perturbations, or fails to replicate across heights.

## Evidence boundary

All current exact results concern the representation, its lower-order closure, its information/Pearson/CA geometry, and its perturbation/overlap/control-calibration boundaries. No canonical finding establishes an anomalous zeta three-gap residual.

`VIS-060` proves only that control-side probability is enough for a fixed-table versus control-population comparison. `VIS-061` supplies a generic full-law replicate-level radius, and `VIS-062` shows that its leading support-size scale is generically unavoidable. `VIS-063` supplies a dimension-free radius only for **one frozen scalar quadratic witness**; it does not certify equality or separation of the complete residual tensor, Fisher orientation, CMI, or an adaptively selected family of visual directions.

These results do not turn one zeta window into a random sample, make a selected window representative of other heights, supply a p-value for a data-dependent visual search, or prove that actual CUE whole-matrix tables attain either the worst-case simplex geometry or a zeta-specific discrepancy.

Finite-size CUE corrections, higher-order spacing correlations, and finite-height arithmetic corrections are established prior art and remain mandatory baselines. Adaptive choices must be covered by fresh confirmation controls or a simultaneous construction. The clue therefore stays `accepted`, not `resolved`.

## Research disposition

Accepted as a live empirical experiment with two explicitly separated fixed-window calibration modes. The strongest lowest-assumption route is the full `VIS-061` control-law ball propagated by `VIS-057`/`VIS-060`. If that is impractical at the frozen support size, `VIS-063` permits a weaker but scalable predeclared quadratic witness test using fresh whole-control replicates, without chasing a generic dimension-free full-law bound forbidden by `VIS-062`.

The immediate frontier is now empirical rather than another generic concentration refinement: obtain the actual higher-window zeta tables, freeze the representation and either the full-vector or witness-level confirmation target, generate genuinely fresh matched controls, and test the fixed arithmetic table against the corresponding control-population certificate. A source-specific stochastic model for zeta remains a later requirement only if a fixed-window effect survives and the claim is to generalize beyond those frozen windows.