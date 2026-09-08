---
id: CLUE-arithmetic-fidelity-quartic-euler-localization-uniformity
type: research-clue
status: accepted
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

Issue #131 certifies only the homogeneous quartic objective and does so computer-assistively. AF-197's remainder is fixed-shape, not uniform over degenerating projective shapes. No full-Euler minimizer, sharp localization condition, growing-band result, or RH consequence is established here.

## Research disposition

`AF-200` independently verifies the clue's first decisive test and strengthens it: for every fixed positive `W_1=delta`, the fixed-band Euler discrepancy tends to zero along the symmetric degeneration `t downarrow 0`, so no positive recovery modulus depending only on `W_1` exists even before taking `delta -> 0`. The specific `t=delta^3` family satisfies `D_T ~ (M_0/2) delta^6`, hence `D_T/delta^4 -> 0`.

AF-200 also rewrites the full normalized Euler discrepancy exactly through the AF-199 Peano B-spline carrier. Its barycentric displacement from the fixed endpoint is `(1+t)h`, and a uniform derivative estimate gives the explicit sufficient varying-shape gate

`delta (1+t)^11 (2t+1) / (t^3 (3t+1)^5) -> 0`.

AF-201 resolves the observation-side localization topology on any two-sided bounded homogeneous profile `0<q_-<=Q<=q_+<infinity`. For the normalized Peano probability carrier `beta`, uniform transfer of the full finite-band Euler transform to the quartic endpoint model is equivalent to weak concentration `beta => delta_x`. A single real-axis defect

`Lambda_sigma(beta) = 1 - int F_sigma^(4) d beta / F_sigma^(4)(x)`

is equivalent to that weak concentration and gives explicit tail bounds. This is strictly weaker as a topology than requiring convergence of the carrier first moment; AF-200's `Q W_1(beta,delta_x)->0` condition is therefore sufficient but not the intrinsic finite-band requirement.

AF-202 translates that observation topology exactly back to fixed-order minimal-support source geometry. By the classical Genocchi-Hermite/Dirichlet representation, the normalized Peano carrier is the law of a uniform-simplex convex combination of the knots. If `D=u_4-x` is the anchored five-knot diameter, then

`2^-4 c(D/2) <= Lambda_sigma(beta) <= c(D)`,

so `Lambda_sigma(beta)->0`, weak carrier concentration, and `D->0` are equivalent. Compact gap-ratio control and bounded `D/W_1` are therefore stronger than the intrinsic localization requirement.

AF-203 now closes the projective-properness test left open after AF-202. Every five-node quartic minimal-support source satisfies the exact nonsharp inequality

`D <= 3 Q W_1`.

Hence bounded `Q` together with `W_1->0` already forces `D->0`; no separate source-localization assumption is needed on a bounded-profile class. Combining the same inequality with the Peano derivative estimate gives the purely profile-scale sufficient gate

`Q^2 W_1 -> 0`,

which allows `Q` to grow and still yields uniform fixed-band transfer.

The unrestricted normalized full-Euler objective does not generate this coercivity automatically: AF-200's escape family lies in vanishing normalized Euler sublevels while `Q->infinity` and the physical diameter escapes. Thus unrestricted full-Euler sublevel compactness, and with it unrestricted minimizer transfer to the homogeneous `Q`-optimizer, is ruled out by existing evidence.

The clue remains accepted because the **weakest** varying-profile gate is still open. The live residual is now to characterize the sharp relation among `Q`, `D`, `W_1`, and the Peano/Euler localization defect that is necessary and sufficient for transfer, and to determine whether a mathematically natural constrained Euler problem supplies that relation. `Q=O(1)` is sufficient, and `Q^2W_1->0` is a weaker sufficient condition; neither is yet shown to be the intrinsic minimal condition.