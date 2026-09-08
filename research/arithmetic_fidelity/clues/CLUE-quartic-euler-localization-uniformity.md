---
id: CLUE-arithmetic-fidelity-quartic-euler-localization-uniformity
type: research-clue
status: proposed
origin: research-watch
target_line: arithmetic_fidelity
based_on:
  - research/arithmetic_fidelity/findings/AF-195-minimal-moment-flat-stencils-are-divided-difference-controls.md
  - research/arithmetic_fidelity/findings/AF-197-mirror-symmetric-quartic-stencils-beat-equispaced-parity.md
  - research/arithmetic_fidelity/findings/AF-198-quartic-symmetric-stencil-is-strict-unrestricted-local-optimum.md
---

# Which localization makes the quartic moment optimizer control the full Euler discrepancy?

## Observation

AF-197 proves a fixed-shape small-scale expansion for the full fixed-band Euler discrepancy, while AF-198 proves only local unrestricted optimality of its leading scale-free coefficient. Independent compute execution under GitHub issue #131 certified that this coefficient `Q` is globally minimized, uniquely modulo scale, by gaps proportional to `(1,t_*,t_*,1)`.

That computation quotients common scale and retains only the first nonvanishing moment coefficient. The full Euler observable is not homogeneous and also sees physical source diameter and higher moments. Consequently, allowing the projective shape to vary with `W_1 = delta -> 0` can invalidate the fixed-shape Taylor regime. In the symmetric family, taking `t=delta^3` makes the required outer scale grow like `delta^(-2)`, while the coefficient at the fixed endpoint is `O(delta^6)` and the remaining Euler contributions are exponentially suppressed. This indicates that `W_1` alone does not make the leading-moment optimization uniform.

## Research question

What is the weakest source-localization or equicoercivity condition under which the full five-node fixed-band Euler objective, normalized by `delta^4`, converges uniformly to its quartic moment objective as `W_1 = delta -> 0`, forcing minimizing shapes to converge modulo scale to `(1,t_*,t_*,1)`?

Compare bounded support-diameter-to-`W_1` ratio, compact gap-ratio control, and weaker tightness conditions. Determine which retained condition is necessary rather than merely convenient.

## Why it may matter

This separates an exact optimizer of the local fourth-order response from a genuine optimizer of the full arithmetic observation. Without such a theorem, the globally certified result of issue #131 cannot be promoted from a leading local coefficient to a full Euler minimax statement. A sharp condition would also identify the missing source resource that must accompany `W_1` in this control class.

## Decisive test

First certify the degenerating symmetric family above and its uniform fixed-band Euler bound, establishing failure under `W_1`-only normalization. Then impose one explicit localization condition and prove a uniform Taylor remainder and sublevel compactness sufficient for Gamma-convergence to the issue-#131 objective. Use uniqueness of the certified `Q`-minimizer to prove convergence of full-objective minimizers, or construct a localized counterexample.

Kill stronger proposed conditions by exhibiting a strictly weaker one that still gives uniformity, and kill the whole direction if the escape family fails under the exact Euler discrepancy or if AF-197's existing estimate is already uniform over the required source class.

## Evidence boundary

Issue #131 certifies only the homogeneous quartic objective and does so computer-assistively. AF-197's remainder is fixed-shape, not uniform over degenerating projective shapes. No full-Euler minimizer, sharp localization condition, growing-band result, or RH consequence is established here. The degenerating family remains a compute-audit lead until independently derived and persisted through the normal Research Watch evidence gate.
