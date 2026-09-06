# MI-003 — Overlap uncertainty must be separated from residual geometry

**Evidence level:** exact fixed-partition geometry plus process-aware finite-sample identities through VIS-059

## Core intuition

A stable geometric residual is not yet a statistically stable observation of that residual. For overlapping gap blocks, the uncertainty layer should be decomposed explicitly: raw-law estimation error, nonlinear closure sensitivity, normalization conditioning, deterministic short-range overlap geometry, and genuine long-range process dependence are different quantities and should not be collapsed into one effective-sample-size heuristic.

## Strongest justified principle

VIS-057 proves that the adjacent-pair Markov completion is globally Lipschitz in finite-alphabet `L^1`, so a valid raw-law radius propagates through recomputed closure to the Fisher residual and its normalized orientation. The certificate correctly becomes weak when residual energy or the common-reference floor is too small.

VIS-058 derives the exact second moment of an empirical overlapping-block law. The dependence correction is a sum of collision covariances, with the first overlap lags kept explicit and only separated blocks delegated to a justified mixing or other process envelope. VIS-059 then shows that those short lags are not generic dependence penalties: they are masses of finite periodic cylinders. In the active three-gap case they are exactly constant-run and period-two return channels.

Thus the inferential chain is modular: **first characterize overlap geometry exactly, then supply an honest long-memory law, then convert the resulting raw-law radius through the already controlled residual map**. An image or Fisher angle should be interpreted only after this chain leaves a nontrivial orientation margin.

## What remains possible

A sharper concentration theorem can replace the coarse second-moment radius without changing the downstream geometry. Higher-order block laws can sharpen periodic-cylinder ceilings. The major unresolved issue is source-specific: justify a population/uncertainty model for finite zeta and comparison data and separately control changes of partition, support, closure convention, and common reference.

## Status / novelty

Conditional-independence completion, empirical-measure covariance, mixing bounds, and word periodicity are classical. The durable synthesis is the error architecture for the active visual experiment: **overlap, long memory, closure nonlinearity, and residual conditioning are distinct uncertainty channels with exact interfaces between them**.

## Falsification criterion

Invalidate the Markov-completion perturbation bound, the exact collision-covariance second-moment identity, or the equivalence between overlapping-block equality and periodic-cylinder structure. A weak numerical certificate does not falsify the intuition; it indicates that the current data/model do not support a stable direction claim.
