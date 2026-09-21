# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Transfer the moving-boundary cubic spectral functional after removing the Abel-cusp background

**Linked intuitions:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`, `MI-045-fixed-gap-meet-join-data-collapse-to-finite-congruence-decoration`, `MI-046-growing-gap-arithmetic-complexity-pays-a-reciprocal-continuation-tariff`, `MI-047-mesoscopic-continuation-phase-can-miss-the-prime-pair-parity-sector`, `MI-048-cubic-phase-can-reopen-arithmetic-support-yet-average-to-a-universal-control`, `MI-049-abel-cubic-singular-series-asymptotics-isolate-an-rh-equivalent-zero-layer-at-model-level`, `MI-050-the-zero-sensitive-exact-kernel-bridge-now-ends-in-a-signed-prime-variance-problem`, `MI-051-cubic-source-replacement-has-a-variance-power-saving-curve`, `MI-052-cubic-filter-pushes-subleading-ramanujan-mass-to-a-moving-square-free-boundary`, `MI-053-the-abel-cusp-creates-a-deterministic-25-28-ramanujan-background`.

PL-391--PL-406 transfer the RH-equivalent model zero layer through the exact incomplete-gamma kernel, isolate the critical Ramanujan covariance, and show that the cubic test projects out the divergent diagonal. PL-407 calibrates the precision required by a generic source-subtracted short-interval variance route: at `H=X^theta`, an LPZ-shaped relative saving exponent `mu` preserves the `H^(-7/4)` layer only when `mu>3theta/(4(1-theta))` after absolute values are taken.

PL-408 first localized the model correction away from fixed Ramanujan interiors using a safe seventh-order Fourier estimate. PL-409 identifies the sharp mechanism for the declared cubic Abel kernel. Its `|x|^7` cusp forces

`Khat_eta(xi)=-(105 eta)/(16 pi^7)|xi|^(-8)+O_eta(|xi|^(-14))`,

and Poisson summation turns this into the same-sign denominator term `-(pi eta/720)J_8(q)H^(-8)`. Since the weighted sum of `J_8(q)` grows like a positive constant times `Q^7`, truncating at `Q=H^kappa` produces a deterministic correction of order `H^(-8+7kappa)`.

The exact crossover with the zero-sensitive `H^(-7/4)` layer is `kappa=25/28`. Interiors below `25/28` are negligible at that layer, the `25/28` interior contributes a nonzero Abel-regulator background at precisely the same order, and larger fixed interiors swamp the zero layer. This is a kernel-cusp threshold, not an RH exponent.

The live fork is therefore sharper. Either prove a source-subtracted prime-variance theorem above the PL-407 precision curve, or control directly the signed cubic prime/model spectral difference on the moving square-free boundary **after the explicit cusp background has been subtracted or incorporated**. A source replacement accurate only on fixed denominator sets cannot see the relevant boundary, while an unrenormalized `H^(-7/4)` signal near `Q=H^(25/28)` cannot be attributed to zeros because the regulator already contributes at that scale.

## Keep exact-kernel transfer, regulator aliasing, model boundary localization and actual prime source distinct

The continuation kernel and critical model covariance are no longer the bottlenecks, but the model-side boundary now contains a deterministic archimedean alias that must be separated from the zero-sensitive term. PL-409 does not prove that the actual prime spectral measure matches the critical Ramanujan endpoint or determine the signed prime/model difference after subtraction.

A future source-replacement proof must therefore specify whether it controls the full variance remainder or the single signed cubic functional, on the denominator/frequency scales actually selected by the kernel, and whether the Abel-cusp term has been removed consistently. Failure of an absolute-value calibration or a fixed-denominator approximation identifies discarded information; it is not evidence that the underlying statistic fails.