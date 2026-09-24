# Arithmetic-fidelity research lines

This file records the current mathematical questions that survive the Arithmetic-Fidelity evidence. It is not a roadmap, task queue, status page, or history.

## Which source relations remain observable after matched controls, nuisance quotienting and finite-resolution noise?

AF-523--AF-527 show that a rigid positive prime-to-composite transport can make source participation vanish while preserving the leading boundary-curvature profile, and can even make the first nonzero curvature-defect amplitude agree super-algebraically after the anchor cutoff and multiplier are co-tuned. AF-528 proves that this scalar collision does not extend automatically to relational shape: for power-separated anchors the logarithmic derivative of the exact carrier ratio at `t=0`, after the stated `log log A/log A` normalization, recovers the hidden anchor exponent. That recovery is exact but infinitesimal; across the physical layer `0<t<=1/A` the available change can still be too small for stable observation.

AF-533 gives the correct Gaussian conditioning object once nuisance directions are present. In a linear observation model `Y_A=s_A a+B_A eta+epsilon_A` with covariance `Sigma_A`, whitening and profiling the nuisance span `W_A=col(Sigma_A^{-1/2}B_A)` leaves the transverse carrier

`h_perp,A=(I-P_W_A) Sigma_A^{-1/2} h_A`,

and the effective discrimination scale is

`I_A^eff = delta_A^2 ||h_perp,A||^2`.

Raw sample count, source density, or even large unprojected precision-weighted carrier energy is therefore not enough: a carrier can be statistically useless if it lies asymptotically inside the nuisance span. Conversely, stable recovery requires the source-derived relational observable to retain transverse precision energy at the scale actually available to the experiment.

The live question is to classify **which exact relational or differential lifts of the boundary data produce a source-forced carrier whose transverse precision energy survives admissible nuisance quotients and realistic observation windows**. AF-528 supplies one exact shape variable in a narrow co-tuned family; AF-533 supplies the correct stability criterion after Gaussian nuisance profiling. What remains is a source theorem connecting the arithmetic observable to a carrier outside the nuisance span with enough projected energy for uniform discrimination, rather than merely exact recoverability at infinite precision. Any proposed discriminator must state the source class, nuisance class, observation window and normalization under which `I_A^eff` stays nondegenerate or diverges.

## Classify quotient-visible contact through admission and no-contact accessibility rates

AF-495--AF-508 isolate a separate fidelity mechanism in critical translated-distance problems. Closed quotient geometry determines the asymptotic threshold, membership of the nearest transverse point in the actual quotient image determines whether finite-time contact occurs, and the admission height determines when a plateau begins. In the no-contact branch the exact carrier is the accessibility profile: with `rho(r)=dist(0,C_r)^2-lambda^2`, the distance excess is the one-sided quadratic envelope `inf_r [rho(r)+(r-t)_+^2]`.

The unresolved step is arithmetic realization rather than abstract convex geometry. Identify a natural arithmetic nuisance quotient and admission rule, determine whether its critical transverse point is admitted, and in the no-contact case prove a source-derived law for `rho` (or its inverse admission profile) strong enough to survive the quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant.
