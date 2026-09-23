# Arithmetic-fidelity research lines

This file records the current mathematical questions that survive the Arithmetic-Fidelity evidence. It is not a roadmap, task queue, status page, or history.

## Classify extinction and multi-scale participation beyond boundary-layer curvature invisibility

AF-509--AF-510 show that the full log-Dirichlet curvature profile of a simple unit-weight positive source determines the source exactly up to global dilation, but AF-511--AF-518 show that this exact quotient injectivity is badly conditioned against remote tail edits. AF-519--AF-521 then identify the one-point boundary carrier more sharply: at `s=1+t`, positive-source curvature depends exactly on normalized zeroth, first and second logarithmic moments, and under source survival the leading law usually collapses to the zeroth/second-moment ratio unless the normalized first moment reaches the `sqrt(log(1/t))` scale.

AF-522 shows that source extinction does not restore a one-parameter law. For the anchored outward unit-weight transport that keeps every prime `p<=A` and sends each `p>A` to the distinct composite `C_A p`, one can have `Q_A(1+1/A)/P(1+1/A)->0` while the relative curvature tends to any prescribed `lambda in [0,1]`. Even a common extinction order can therefore carry different higher-moment participation.

AF-523 closes the first natural multi-scale repair. Choosing `C_A->infinity` with `C_A log log A/log A->0`, the same rigid positive prime-to-composite transport satisfies, uniformly for every `0<t<=1/A`,

`Q_A(1+t)/P(1+t)->0`

while

`kappa_Q_A(1+t)/kappa_P(1+t)->1`.

More precisely the zeroth, first and second normalized moment participations all acquire the same vanishing factor `C_A^(-1-t)(1+o(1))`, so the exact AF-521 curvature quotient cancels that common factor. A finite set of boundary scales, or even the complete leading relative-curvature profile on the shrinking layer `1<s<=1+1/A`, therefore still does not recover prime provenance.

The live question has moved beyond “add more nearby curvature samples.” One must identify information that breaks the common asymptotic dilation factor: scales `t>>1/A` where the retained anchor re-enters, lower-order curvature asymptotics that survive after the leading ratio cancels, or a richer observable whose visible layers do not share the same participation factor. Within those alternatives, the source category still has to determine which normalized moment profiles are actually realizable; arbitrary signed/complex sources, inward transports and arbitrary prescribed moment tuples are not consequences of AF-522--AF-523.

The adversarial boundary remains sharp. AF-523 is a moving-family, shrinking-window leading-order obstruction, not equality of complete curvature profiles for two fixed sources. The exact full-profile inversion of AF-509--AF-510 therefore remains intact. Any claimed robust prime discriminator must state which scale range, asymptotic order or extra observable escapes the AF-523 gauge-like collapse rather than conflating exact recoverability with stable provenance.

## Classify quotient-visible contact through admission and no-contact accessibility rates

AF-495--AF-508 isolate a separate fidelity mechanism in critical translated-distance problems. Closed quotient geometry determines the asymptotic threshold, membership of the nearest transverse point in the actual quotient image determines whether finite-time contact occurs, and the admission height determines when a plateau begins. In the no-contact branch the exact carrier is the accessibility profile: with `rho(r)=dist(0,C_r)^2-lambda^2`, the distance excess is the one-sided quadratic envelope `inf_r [rho(r)+(r-t)_+^2]`.

The unresolved step is arithmetic realization rather than abstract convex geometry. Identify a natural arithmetic nuisance quotient and admission rule, determine whether its critical transverse point is admitted, and in the no-contact case prove a source-derived law for `rho` (or its inverse admission profile) strong enough to survive the quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant.