# Arithmetic-fidelity research lines

This file records the current mathematical questions that survive the Arithmetic-Fidelity evidence. It is not a roadmap, task queue, status page, or history.

## Which source relations remain observable after matched controls, nuisance closure and finite-resolution noise?

AF-523--AF-527 show that a rigid positive prime-to-composite transport can make source participation vanish while preserving the leading boundary-curvature profile, and can even make the first nonzero curvature-defect amplitude agree super-algebraically after the anchor cutoff and multiplier are co-tuned. AF-528 proves that this scalar collision does not extend automatically to relational shape: for power-separated anchors the logarithmic derivative of the exact carrier ratio at `t=0`, after the stated `log log A/log A` normalization, recovers the hidden anchor exponent. That recovery is exact but infinitesimal; across the physical layer `0<t<=1/A` the available change can still be too small for stable observation.

AF-533 gives the correct Gaussian conditioning object once nuisance directions are present. In a linear observation model `Y_A=s_A a+B_A eta+epsilon_A` with covariance `Sigma_A`, whitening and profiling the nuisance span `W_A=col(Sigma_A^{-1/2}B_A)` leaves the transverse carrier

`h_perp,A=(I-P_W_A) Sigma_A^{-1/2} h_A`,

and the effective discrimination scale is

`I_A^eff = delta_A^2 ||h_perp,A||^2`.

AF-534 shows that in an infinite-dimensional Gaussian shift experiment the nuisance space must be **closed in the Cameron--Martin geometry** before this distance is interpreted as a stability margin. For a target carrier `u_A` and linear nuisance space `N_A`, exact target aliasing occurs only when `u_A in N_A`, but stable distinguishability is governed by

`d_A = dist_(H_A)(u_A, closure(N_A))`,

with `J_A=delta_A^2 d_A^2`. One can therefore have algebraic identifiability with zero robust margin when `u_A in closure(N_A) \ N_A`. For a fixed compact target interval, AF-534 proves uniform nuisance-robust consistency exactly when `J_A -> infinity`.

AF-535 adds the observation/compression gate in a regular semiparametric experiment. If `e=(I-P_Lambda)s` is the source efficient score, `C=E[.\mid Y]` is the conditional-expectation contraction of a parameter-independent observation channel, and `M=closure(C Lambda)` is the downstream nuisance tangent space, then the downstream efficient score is

`e_Y=(I-P_M) C e`,

and the exact information loss splits as

`I_X^eff-I_Y^eff = (||e||^2-||Ce||^2) + ||P_M Ce||^2`.

The first term is direct loss of the efficient score through compression; the second is nuisance recontamination created after observation. Equality holds exactly when the upstream efficient score is measurable from the retained observation. Adjoining `e` itself gives a minimal first-order lift, but that repair is target-, baseline- and nuisance-dependent and is therefore not automatically a source-natural arithmetic representation.

AF-536 sharpens the deterministic case. If `Y=T(X)`, `P=E[.\mid Y]`, `K=ker P`, and `Lambda` is the upstream closed nuisance tangent space, then the downstream efficient information is exactly

`I_Y^eff = dist(e, closure(Lambda+K))^2`,

so deterministic compression identifies the target only modulo the closed nuisance-plus-invisible subspace. Full first-order fidelity is equivalent to `e` being `Y`-measurable, while total collapse occurs already when `e in closure(Lambda+K)`; an exact algebraic decomposition into one nuisance and one invisible direction is not required. For nested deterministic statistics these closed loss spaces increase monotonically and the information drop between stages is the squared norm of the newly admitted orthogonal component.

AF-537 gives the corresponding sequential statement for general parameter-independent Markov compression when the downstream model may enlarge the nuisance semantics. With `N_(j+1)=closure(C_j Lambda_j)` and `D_(j+1)=Lambda_(j+1) cap N_(j+1)^perp`, the stage loss splits exactly into direct channel erasure, pushed-nuisance recontamination, and new-nuisance reclassification. These nonnegative losses telescope along the chain. Even a lossless observation can therefore lose target information if the downstream model newly declares part of the surviving efficient direction to be nuisance; no observation-side lift repairs that loss while the enlarged nuisance equivalence is kept fixed.

AF-538 upgrades that scalar bookkeeping to a finite-dimensional target. If `E_j:R^d->H_j` is the efficient-score operator and `J_j=E_j^*E_j`, then every stage has a positive-semidefinite matrix loss `J_j-J_(j+1)`. Its kernel is the **fidelity subspace** of target combinations preserved at that stage, and end-to-end exact survival is the intersection of those stagewise kernels. When `J_0` is positive definite, `J_0^(-1/2) J_m J_0^(-1/2)` gives a coordinate-free first-order fidelity spectrum in `[0,1]`: eigenvalue `1` marks fully preserved combinations, intermediate eigenvalues quantify directional weakening, and `0` marks complete first-order loss. This is a statistical geometry theorem, not yet an arithmetic representation theorem; the target family, nuisance semantics and observation chain must still be source-derived.

AF-539 returns to the exact AF-528 carrier and identifies a sharp source-admissibility threshold for one natural nuisance family. If the outer tail multipliers are changed from `C_A` to `\widetilde C_A`, the normalized projective log-slope becomes

`(log log A/log A) (log R_A)'(0) = 1-theta + lambda_A + o(1)`,

with `lambda_A=(log log A/log A)(g(\widetilde C_A)-g(C_A))` and `g(C)=C log C/(C-1)`. Every AF-525-admissible multiplier family has `lambda_A->0`, so the anchor-shape signal `1-theta` survives that nuisance class. The first scale at which the nuisance can cancel the signal is instead `log C_A` of order `log A/log log A`. This is a source-constrained transversality statement for the exact carrier, not a generic conditioning theorem: the threshold is first-order, fixed-`theta`, and can be reproduced by matched generalized sources with the same Mertens moments.

AF-540 shows that this first-jet nuisance threshold is not an obstruction to the full local projective germ. For the same exact carrier and `B_A=floor(A^theta)`, every fixed derivative order `k>=2` satisfies

`(log log A/(log A)^k) (log R_A)^(k)(0) -> (-1)^(k+1)(1-theta^k)/k`

uniformly over **arbitrary** integer multiplier sequences `C_A,\widetilde C_A>=2`, with no growth or co-tuning restriction. The reason is exact: after taking logs the only multiplier term that can grow with `C` is affine in `t`, so every derivative of order at least two annihilates it, while the retained prime-prefix cumulant has size `(log A)^k/log log A`. In particular the second log-jet recovers `theta` even when the first log-slope can be cancelled. This remains an exact infinitesimal carrier theorem, not a finite-resolution stability result or a prime-specific discriminator: arbitrary `t`-dependent nuisance curvature could still cancel the second jet, and matched generalized sources with the same reciprocal-prime moment hierarchy can reproduce the limit.

AF-541 closes the finite-resolution gap for this exact scalar-multiplier family without taking a higher derivative. For `0<h<=A^(-1)`, the weighted two-point contrast

`Q_(A,h)=log R_A(h)-(1+h)log R_A(0)`

annihilates the only unbounded multiplier direction `(1+t)log C` exactly, leaving a uniformly bounded multiplier remainder whose contribution is `O(h)`. Uniformly over arbitrary integer multiplier sequences,

`(log log A/(h log A)) Q_(A,h) -> 1-theta`.

At the physical scale `h=A^(-1)` the carrier is of order `(1-theta)log A/(A log log A)`, so deterministic log-sample errors must be `o(log A/(A log log A))` for consistent recovery. Within nonzero linear point-sample contrasts that remain uniformly bounded as the multiplier grows, one point cannot suffice and the two-node annihilator is unique up to scale. The gain is therefore genuinely finite-resolution but still exact-carrier-level: AF-541 does not transfer the contrast to physical boundary observations, defeat arbitrary `t`-dependent nuisance curvature, or make the signal prime-specific against matched generalized sources.

AF-542 now shows that this exact-carrier finite-resolution contrast is **not stable under the raw normalized-curvature representation** at its natural endpoint. With a common admissible multiplier `C_A` satisfying `C_A log log A/log A -> 0` and `h_A=A^(-1)`, the exact carrier ratio and the physical normalized-curvature ratio differ in logarithmic increment by a first nonlinear correction of order `C_A/log A`. After the AF-541 transverse two-point normalization, that correction contributes

`(-log theta) A(C_A-1) log log A/(log A)^2 (1+o(1))`,

which diverges, while the desired exact-carrier signal remains `1-theta`. Thus the value-level relative approximation from carrier to curvature is far too weak for this downstream discriminator: an error that is small before differencing can dominate after applying the contrast at its shrinking target scale. The obstruction is the first nonlinear carrier-to-curvature correction, not drift of the common scalar multiplier.

The live question is therefore to classify **which relational or differential lifts remain quantitatively transverse after the actual representation map, in the topology or seminorm consumed by the final discriminator**. AF-528, AF-539--AF-541 establish a genuine exact-carrier shape coordinate and exact nuisance annihilation, but AF-542 rules out simply transporting the minimal two-node contrast through raw normalized curvature at `h=A^(-1)`. A successful physical route must either subtract or estimate the nonlinear curvature defect at finer accuracy than the target contrast, use a curvature-native renormalization whose transverse error is controlled, retain enough pre-compression information to reconstruct the correction, or choose another representation/scale whose approximation error is small **after** the discriminator is applied. AF-533--AF-538 give the closure and efficient-information geometry in which that stability must be stated. Algebraic recovery at infinite precision, a hand-picked derivative, value-level `1+o(1)` representation fidelity, raw sample count, unprojected carrier energy, and a target-dependent score-adjoining lift remain insufficient by themselves.

## Classify quotient-visible contact through admission and no-contact accessibility rates

AF-495--AF-508 isolate a separate fidelity mechanism in critical translated-distance problems. Closed quotient geometry determines the asymptotic threshold, membership of the nearest transverse point in the actual quotient image determines whether finite-time contact occurs, and the admission height determines when a plateau begins. In the no-contact branch the exact carrier is the accessibility profile: with `rho(r)=dist(0,C_r)^2-lambda^2`, the distance excess is the one-sided quadratic envelope `inf_r [rho(r)+(r-t)_+^2]`.

The unresolved step is arithmetic realization rather than abstract convex geometry. Identify a natural arithmetic nuisance quotient and admission rule, determine whether its critical transverse point is admitted, and in the no-contact case prove a source-derived law for `rho` (or its inverse admission profile) strong enough to survive the quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant.
