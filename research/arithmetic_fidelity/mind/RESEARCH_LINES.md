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

AF-524 resolves the first leading-order re-entry beyond that blind layer for the same transport. At

`t_A=exp(-alpha C_A log log A)`, `alpha>0` fixed,

one still has source extinction, with `C_A Q_A(1+t_A)/P(1+t_A)->1+1/alpha`, and the first two logarithmic-moment participations remain tail-dominated, `C_A M_j^Q/M_j^P->1` for `j=1,2`. The retained prefix has, however, re-entered the zeroth moment at leading order, and the relative curvature converges to `alpha/(1+alpha)`. Thus leading curvature becomes informative precisely when the visible moment layers stop sharing one common participation factor. The crossover variable is `log(1/t)/(C_A log log A)`, not the geometric boundary `t~1/A`.

AF-525 resolves the first lower-order question *inside* the AF-523 blind layer for a rigid anchored family. If `D_A(t)` denotes its normalized first anchor-defect scale, then uniformly for `0<t<=1/A`,

`(1-kappa_Q_A(1+t)/kappa_P(1+t))/D_A(t)->1`,

with

`D_A(t) ~ C_A log log A / log(1/t)`.

Thus the leading quotient is blind while its first nonzero correction remembers the transport parameter `C_A` after division by the known anchor normalization.

AF-526 shows that this first correction is still not an intrinsic provenance marker once the anchor cutoff is allowed to vary. For two controls with the same multiplier `C_A` but cutoffs `A` and `B_A<=A`, their first curvature defects satisfy, on the common layer `0<t<=1/A`,

`Delta_B_A(t)/Delta_A(t) -> log log B_A / log log A`

uniformly whenever that ratio has a limit and both transports remain in the AF-525 regime. In particular, every fixed-power cutoff `B_A=floor(A^theta)`, `0<theta<1`, has defect ratio tending to `1` although the retained prime supports differ on an asymptotically large interval. The first correction therefore sees the anchor only through its slowly varying Mertens mass `log log A`; AF-525's recovery of `C_A` is conditional on that anchor normalization being known.

The live question is now sharper than whether a lower-order curvature term can break the common-factor degeneracy. It can, but the first such term still factors through a coarse anchor statistic on a broader matched-control class. One must identify the **smallest intrinsic curvature jet or source-derived correction that separates provenance-distinct positive transports after anchor normalization is also allowed to vary**, or prove that broader controls can continue matching successive corrections. Outside the blind region, one should likewise classify how generally the AF-524 moment-balance crossover persists and which moment layer de-locks first.

The adversarial boundary remains sharp. AF-523 is a moving-family, shrinking-window leading-order obstruction; AF-524 is a fixed-`alpha` leading-curvature calculation for the same transport; AF-525 is a uniform first-correction theorem for one anchored family; and AF-526 is a first-correction collision for variable anchor cutoffs, not equality of higher jets or complete curvature profiles. None contradicts the exact full-profile inversion of AF-509--AF-510. Any claimed robust discriminator must state the source class, scale range, anchor information and asymptotic order at which its information survives matched positive controls.

## Classify quotient-visible contact through admission and no-contact accessibility rates

AF-495--AF-508 isolate a separate fidelity mechanism in critical translated-distance problems. Closed quotient geometry determines the asymptotic threshold, membership of the nearest transverse point in the actual quotient image determines whether finite-time contact occurs, and the admission height determines when a plateau begins. In the no-contact branch the exact carrier is the accessibility profile: with `rho(r)=dist(0,C_r)^2-lambda^2`, the distance excess is the one-sided quadratic envelope `inf_r [rho(r)+(r-t)_+^2]`.

The unresolved step is arithmetic realization rather than abstract convex geometry. Identify a natural arithmetic nuisance quotient and admission rule, determine whether its critical transverse point is admitted, and in the no-contact case prove a source-derived law for `rho` (or its inverse admission profile) strong enough to survive the quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant.