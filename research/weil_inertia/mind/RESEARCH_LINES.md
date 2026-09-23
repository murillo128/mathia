# Weil-inertia research lines

This file records the current mathematical questions that survive the Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Keep finite-budget defect sensitivity separate from formal global continuation

WI-399--WI-408 show that the Widder/superzeta hierarchy can create clean finite-height horizontal-defect charges, but canonical meromorphic continuation and any fixed finite exponent jet do not turn those local charges into a coercive global RH criterion. Finite logarithmic moments, even all fixed orders separately, can coexist with sparse off-line defects. Any global superzeta route still needs a defect-determining matched finite-part identity or another source theorem stronger than mere finiteness of continued quantities.

WI-409--WI-416 expose the complementary half-plane budget obstruction. Centered or translated Blaschke probes trade height/depth sensitivity against finite total variation; exact all-depth flatness uniquely forces Haar scale density in the tempered class; continuum height/depth coverage is extensive; and target-adaptive discrete placement can drive the cost of a finite target set to zero. The missing resource is therefore non-oracular regularity of the admissible probe field, not a more elaborate formal sum of one-target charges.

## Derive zeta-side regularity that makes the bounded-density Poisson capacity coercive

WI-417 computes the exact one-target problem under an independently fixed two-dimensional density cap `B`. The optimal positive source is a kernel superlevel set, and for shallow depth `d` the minimum source mass is asymptotic to `Q^2/(4 pi B d^2)`. WI-418 shows that nearby targets can reuse essentially one such budget, while WI-419 shows asymptotic additivity for sufficiently separated same-depth targets.

WI-420 resolves the previously open critical separation scale. For fixed target number and comparable depths `d_(j,s)=delta_j s`, with ordinate offsets `gamma_(j,s)=gamma_0+c_j/s`, the rescaled Blaschke kernel converges to the upper-half-plane Poisson kernel

`P_j(A,Y)=2 delta_j A/(A^2+(Y-c_j)^2)`.

The scaled minimum source mass converges exactly to the bounded-density Poisson capacity

`C_B = inf { integral g : 0<=g<=B, integral P_j g >= Q_j for all j }`,

and this infinite-dimensional problem has the finite-multiplier dual

`C_B = sup_(lambda_j>=0) [ sum_j lambda_j Q_j - B integral (sum_j lambda_j P_j-1)_+ ]`.

One may choose a bang-bang optimizer supported on the superlevel set of the dual Poisson field. For two equal finite-separated critical targets the capacity lies strictly between one and two one-target costs, tending to the reuse endpoint as the scaled separation vanishes and to additivity as it diverges. Thus the whole `S asymp 1/d` crossover for fixed comparable-depth configurations is a precise scale-invariant capacity problem, not an unspecified interpolation.

The live mathematical question has moved upstream: **what independently justified zeta arithmetic forces a density cap or comparable regularity on the admissible source and places hypothetical defects in configurations whose Poisson capacity exceeds that source budget?** WI-420 itself supplies neither input. It also leaves singular regimes such as growing target number and scale-separated depth ratios to be analyzed as limits of, or extensions to, the capacity problem rather than assumed to inherit the fixed-configuration law.

A valid global argument must therefore connect three quantities without oracle dependence: the admissible source budget/regularity, the arithmetic geometry of the defect set, and the Poisson capacity of that geometry. Counting defects alone is insufficient because clustered targets reuse budget; local one-target costs alone are invalid because the critical capacity is genuinely nonadditive; and a density cap chosen after seeing the target configuration would simply encode the desired conclusion.