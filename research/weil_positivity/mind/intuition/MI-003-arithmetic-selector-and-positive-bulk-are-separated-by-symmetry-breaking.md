# MI-003 — The right logarithm can be a normalization anomaly while canonical positive curvature removes it

**Evidence level:** supported through WP-141 by exact positive refinement, singular determinant, and matched-composite controls

## Core intuition

Positivity does not by itself erase arithmetic, but neither does obtaining the numerically correct `log m` coefficient prove that positivity generated it. The first regular and singular refinement responses already showed that generic cover geometry has the wrong depth law. The Kron near-miss sharpens this: a canonical positive one-hole response can produce exactly the missing logarithmic scale only because a determinant ratio compares spaces of different rank.

That logarithm lives in a scale gauge. The most canonical positive geometry of the same determinant — its log-partition/Fisher Hessian — annihilates precisely that gauge direction. Thus the route cannot simultaneously treat the `log m` as a scale anomaly and inherit its sign from normalized positive curvature.

## Strongest justified principle

WP-134--WP-139 classify the first refinement responses. Repeated-prime coarse response is stationary; regular full-fiber traces are zero or extensive; the repeated-prime Green trace gives generic harmonic/log-cover growth; regular one-hole new-prime responses are bounded; and the minimal puncture pseudodeterminant finite part is bounded and prime-blind after intrinsic normalization.

WP-140 tests the nonlocal Kron repair at the minimal base. The positive star-mesh response has an exact singular determinant ratio

`log(det' C_{2,m}/det Delta_{2,m}) = log m + log 48 + log(m/(m+1))`

under the native inverse-square normalization. This is a genuine near-miss at the critical half-weight. But a common positive rescaling `c_m` changes the same readout by `-log c_m`; with unnormalized geometry the leading coefficient is `-log m`, and arbitrary power rescaling changes it again. The logarithm is therefore the determinant-line effect of one missing nonzero mode, not a scale-invariant consequence of operator positivity. The formula also holds for every odd composite matched control.

WP-141 applies the canonical positive rescue. By Matrix-Tree, the Kron pseudodeterminant is a spanning-tree partition function. In log-conductance coordinates its Hessian is the covariance/Fisher matrix of edge indicators and is positive semidefinite. Every spanning tree has fixed cardinality, however, so common conductance scaling is an exact null direction: the normalized tree law, Fisher metric, and Bregman divergence are unchanged. The positive curvature therefore quotients out the very scale gauge that manufactured the `log m` in WP-140.

## What remains possible

An equal-rank finite--archimedean determinant, a determinant-line metric not reduced to normalized spanning-tree information geometry, or a genuinely global/nonseparable construction may evade this no-go. It must fix its normalization independently, distinguish prime from matched composite refinement, and produce a sign theorem not borrowed from a gauge-dependent first derivative.

## Status / novelty

Kron reduction, pseudodeterminants, Matrix-Tree, exponential-family Fisher geometry, and scale covariance are classical. The persisted synthesis is the sharper selector/sign boundary: **a correct logarithm may come from rank-normalization bookkeeping, while the canonical positive metric removes that bookkeeping rather than explaining its sign**.

## Falsification criterion

Produce within the covered Kron geometry a scale-invariant positive quadratic form whose finite response retains the exact new-prime `log m` coefficient and distinguishes matched composites, or derive an independently forced equal-rank normalization where the determinant-line logarithm survives as a genuine positive invariant.

## Lean-formalizable core

- Exact Kron pseudodeterminant ratio.
- Rank-difference scaling law.
- Matrix-Tree log-partition Hessian as covariance.
- Uniform-scale null direction of fixed-cardinality spanning trees.
