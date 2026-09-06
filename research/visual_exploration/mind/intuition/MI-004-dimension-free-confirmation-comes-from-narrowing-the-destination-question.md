# MI-004 — Dimension-free confirmation comes from narrowing the destination question

**Evidence level:** exact finite-replicate concentration and lower-bound geometry through VIS-063

## Core intuition

The support-size cost in a generic full-law control certificate is real, not a weakness of one concentration inequality. If each independent control replicate contributes an arbitrary probability table on `K` cells, even the one-hot subclass forces `L^1` estimation error of order `sqrt(K/B)`. A dimension-free confirmation radius becomes available only by asking a smaller destination question.

For the active three-gap residual, one such smaller question is a single frozen quadratic direction of the denominator-free Markov defect. Independent whole-control replicates can estimate that scalar functional unbiasedly with `B^{-1/2}` concentration and no `K` or Fisher-floor factor. The gain comes from reducing the claim, not from recovering the same full residual geometry more cheaply.

## Strongest justified principle

VIS-061 gives a distribution-free `L^1` radius for the mean of independent simplex-valued control replicates while allowing arbitrary dependence inside each replicate. Propagated through VIS-057/VIS-060, it supplies a rigorous full residual-ball comparison for one frozen zeta table. VIS-062 proves the leading `sqrt(K/B)` dependence is unavoidable up to constants in this information model by embedding ordinary multinomial estimation as a valid control family.

VIS-063 changes the estimand. The denominator-free residual tensor `C(P)=P_Y P_{XYZ}-P_{XY}P_{YZ}` is quadratic in the population law. For one frozen dual tensor `w`, cross-replicate multiplication gives an unbiased estimator of `tau_w(P)=<w,C(P)>`, and a bounded-kernel Hoeffding argument gives a confidence radius of order `B^{-1/2}` independent of support dimension. Optimizing `w` over the whole dual ball would recover a full `L^1` residual question and reintroduce complexity.

Thus **statistical calibration should match the exact strength of the destination claim**. Full-vector geometry pays full representation complexity; one predeclared discriminating direction need not.

## What remains possible

CUE-specific covariance or concentration may improve the full-law certificate because actual whole-matrix tables are much more structured than arbitrary simplex points. A coarser predeclared representation can also lower the generic cost. For scalable confirmation without such a theorem, the frozen-witness route is valid provided the witness is chosen without reusing the confirmation controls.

A finite-window witness separation remains only a fixed-object statement. Across-height generalization still needs fresh replication and an explicit source-side stochastic or deterministic generalization argument.

## Status / novelty

Multinomial `L^1` estimation, bounded differences, U-statistics, and Hoeffding concentration are classical. The durable synthesis is methodological and exact: **dimension-free control calibration is obtained by reducing the destination functional, not by pretending that a high-dimensional full-law uncertainty ball is dimension free.**

## Falsification criterion

Construct a distribution-free whole-simplex `L^1` estimator that uniformly beats the VIS-062 `sqrt(K/B)` lower-bound scale under the same information model, or find independent whole replicates and a fixed bounded witness for which the VIS-063 unbiasedness/range/concentration calculation fails. Otherwise full-law and frozen-witness confirmation must remain distinct claim strengths.
