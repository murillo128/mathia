# MI-002 — Fisher-gauge geometry is a small exact quotient with separately controlled conditioning and class-law drift

**Evidence level:** exact through VIS-056

## Core intuition

Coordinate safety is necessary but not sufficient, and exact information loss should be distinguished from perturbative instability. On the nondegenerate two-ratio Fisher locus the invariant angle preserves the magnitude of the one-dimensional source contrast exactly and quotients only its orientation. The difficult regions are the quotient fixed point and saturation, where inverse conditioning is poor; support motion inside the fixed two-ratio model can nevertheless be controlled by a natural transport metric.

## Strongest justified principle

VIS-048--VIS-053 establish exact gauge invariance, the one-coordinate reduction, the cumulant hierarchy, and the sign-variation/parity constraints on balance returns. If the first unmatched cumulant has order `r`, Fisher-angle variation starts at order `2r`; exact equality of all finite class cumulants gives true degeneracy.

VIS-054 turns the doubled contact order into a conditioning theorem. At a balance return of multiplicity `m`, signed-coordinate perturbations localize nearby roots at scale `eta^(1/m)`, while angle-only perturbations can do no better than `delta^(1/(2m))`; for a simple return this is linear versus square-root stability, and the weaker exponent is sharp.

VIS-055 supplies the exact inversion: the Fisher cosine determines `|q|`, two analytic contrast paths with the same curve differ only by one global sign, and one signed nonbalance observation fixes the branch. The inverse is singular at balance and exponentially ill-conditioned near saturation.

VIS-056 adds support-moving control without requiring identical atoms. For class laws supported in `[-H,H]`, Wasserstein-1 drift bounds the changes of the signed balance equation and its derivative, the hidden log-moment contrast, and the rendered Fisher angle. Simple remote balance roots are therefore linearly stable under sufficiently small class-law transport. This is a forward/model perturbation theorem inside the frozen outer two-ratio geometry, not a bound on changes of the partition, residual tensors, baseline `kappa`, closure, or empirical sampling process.

## What remains possible

A useful empirical residual should retain one signed source-sensitive scalar alongside the invariant Fisher geometry and decompose its error budget into class-law transport, partition/closure model error, and sampling error. Another quotient may preserve orientation more robustly. Further exact algebra on the frozen two-ratio Fisher curve does not create a new signal by itself.

## Status / novelty

Fisher geometry, analytic uniqueness, root perturbation, inverse conditioning, and Kantorovich--Rubinstein transport bounds are classical. The durable synthesis is exact: **gauge invariance can reduce to a small symmetry quotient whose exact information, inverse conditioning, and model-transport stability must be audited as separate layers**.

## Falsification criterion

Exhibit a valid two-ratio configuration where different `|q|` values give the same exact Fisher cosine, two analytic contrast paths with the same curve that are not global sign reflections, violate the VIS-056 Wasserstein moment/derivative bounds, or produce a simple return satisfying its margins that is not stable under the stated class-law drift.
