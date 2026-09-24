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

The live question is to classify **which exact relational or differential lifts of the arithmetic boundary data produce a source-forced carrier that remains quantitatively transverse to the closed admissible nuisance geometry on the observation window actually available**. AF-528 supplies one exact shape variable in a narrow co-tuned family; AF-533 supplies the finite-dimensional precision projection; AF-534 identifies closure as the infinite-dimensional stability boundary. What remains is a source theorem connecting the arithmetic observable to a carrier with enough closed-quotient Cameron--Martin/precision energy for uniform discrimination. Algebraic non-membership in the raw nuisance span, exact recoverability at infinite precision, raw sample count and unprojected carrier energy are all insufficient by themselves.

## Classify quotient-visible contact through admission and no-contact accessibility rates

AF-495--AF-508 isolate a separate fidelity mechanism in critical translated-distance problems. Closed quotient geometry determines the asymptotic threshold, membership of the nearest transverse point in the actual quotient image determines whether finite-time contact occurs, and the admission height determines when a plateau begins. In the no-contact branch the exact carrier is the accessibility profile: with `rho(r)=dist(0,C_r)^2-lambda^2`, the distance excess is the one-sided quadratic envelope `inf_r [rho(r)+(r-t)_+^2]`.

The unresolved step is arithmetic realization rather than abstract convex geometry. Identify a natural arithmetic nuisance quotient and admission rule, determine whether its critical transverse point is admitted, and in the no-contact case prove a source-derived law for `rho` (or its inverse admission profile) strong enough to survive the quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant.
