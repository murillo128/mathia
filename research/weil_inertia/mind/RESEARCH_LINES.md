# Weil-inertia research lines

This file records the current mathematical questions that survive the Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Keep finite-budget defect sensitivity separate from formal global continuation

WI-399--WI-408 show that the Widder/superzeta hierarchy can create clean finite-height horizontal-defect charges, but canonical meromorphic continuation and any fixed finite exponent jet do not turn those local charges into a coercive global RH criterion. Finite logarithmic moments, even all fixed orders separately, can coexist with sparse off-line defects. Any global superzeta route still needs a defect-determining matched finite-part identity or another source theorem stronger than mere finiteness of continued quantities.

WI-409--WI-416 expose the complementary half-plane budget obstruction. Centered or translated Blaschke probes trade height/depth sensitivity against finite total variation; exact all-depth flatness uniquely forces Haar scale density in the tempered class; continuum height/depth coverage is extensive; and target-adaptive discrete placement can drive the cost of a finite target set to zero. WI-421 sharpens the last point: every positively homogeneous, subadditive source gauge that assigns locally bounded cost to interior Dirac atoms inherits the same zero-cost oracle failure. Ordinary Carleson and vanishing-Carleson control are explicit examples. The missing resource is therefore not generic Hardy-space regularity but a non-oracular, concentration-sensitive restriction that actually excludes or quantitatively prices atomic targeting.

## Derive zeta-side regularity in the source space selected by the Blaschke kernel

WI-417 computes the exact one-target problem under an independently fixed two-dimensional density cap `B`. The optimal positive source is a kernel superlevel set, and for shallow depth `d` the minimum source mass is asymptotic to `Q^2/(4 pi B d^2)`. WI-418 shows that nearby targets can reuse essentially one such budget, while WI-419 shows asymptotic additivity for sufficiently separated same-depth targets.

WI-420 resolves the critical separation scale. For fixed target number and comparable depths `d_(j,s)=delta_j s`, with ordinate offsets `gamma_(j,s)=gamma_0+c_j/s`, the rescaled Blaschke kernel converges to the upper-half-plane Poisson kernel

`P_j(A,Y)=2 delta_j A/(A^2+(Y-c_j)^2)`.

The scaled minimum source mass converges exactly to the bounded-density Poisson capacity

`C_B = inf { integral g : 0<=g<=B, integral P_j g >= Q_j for all j }`,

with a finite-multiplier dual and bang-bang optimizers. For two equal finite-separated critical targets the capacity lies strictly between one and two one-target costs, tending to the reuse endpoint as the scaled separation vanishes and to additivity as it diverges. Thus the whole `S asymp 1/d` crossover for fixed comparable-depth configurations is a precise scale-invariant capacity problem, not an unspecified interpolation.

WI-421 gives a decisive admissibility test for the source side of that capacity. Finite total variation, Carleson control and even vanishing-Carleson control still permit arbitrarily cheap target-adaptive atoms, whereas an `L^infinity(da db)` density cap excludes atoms and yields the positive `d^(-2)` capacity of WI-417--WI-420. More generally, any proposed source norm should first be tested on `R(delta_x)` as `x` approaches a target: if the local atomic cost stays bounded, the Blaschke singularity defeats the route before any global zero geometry enters.

WI-422 now shows that atom exclusion alone still does not identify the right one-norm source class. For the translated-Blaschke kernel `q_d`, the exact distribution law gives `q_d in L^s` precisely for `s>2`, with the endpoint `q_d in L^(2,infinity)` but not in any finite-index `L^(2,r)`. Consequently the bare response functional `f -> integral q_d f` is bounded on global `L^p` **if and only if `1<p<2`**. At `p=1` local concentration defeats boundedness; at `p=2` the kernel is only weak-`L^2`; and for `p>2`, including `p=infinity`, diffuse far-field mass can produce arbitrarily large response at fixed norm. The sharp Lorentz endpoint `L^(2,1)` does control the response.

This changes the admissibility test qualitatively. A useful source regularity must control both **local concentration and the two-dimensional `1/r` far tail** in the dual geometry of the translated-Blaschke kernel. Merely saying that the source is absolutely continuous or belongs to some `L^p` is insufficient. WI-422 also shows that when finite total variation is retained as a second budget, every `L^p` density constraint with `p>1` restores positive one-target TV coercivity, but with distinct subcritical, critical and supercritical depth regimes. Mixed budgets can therefore be coercive even when the bare norm is not.

WI-423 separates the canonical defect source from the auxiliary source to which those coercive spaces could apply. For the exact shifted zeta Blaschke potential `U`, the Riesz identity is

`-Delta U = 2 pi mu_off`,

where `mu_off` is the atomic counting measure of off-critical zeros in the right half-plane. Hence an exact representation `U=G(f dA)+h` with `f` locally integrable and `h` harmonic would force the atomic measure `mu_off` to equal the absolutely continuous measure `f dA`; both must vanish. Planar absolute continuity, and therefore any `L^p(dA)` regularity, of the **canonical exact Riesz source** is already an RH-level conclusion rather than an intermediate source theorem.

The source-regularity route must therefore keep two objects distinct. WI-417--WI-422 concern an auxiliary probe/coefficient measure whose independently fixed norm can be tested against Blaschke capacity. WI-423 shows that this auxiliary source cannot be obtained merely by re-describing the canonical Riesz source while preserving exact Green-potential equality modulo a harmonic term. Smoothing `mu_off` can create a density, but then the changed potential and its correction are precisely the quantity that must be controlled; regularity of the smoothed density alone is not evidence of coercivity.

The live mathematical question has moved upstream again: **can accessible prime-side, boundary, or explicit-formula data generate an auxiliary source `nu` with a target-independent concentration-and-tail budget, together with an exact or quantitatively controlled coupling from its probe potential to `mu_off`?** Candidate budgets may use the bare `1<p<2` range, the endpoint Lorentz class, finite-TV-plus-`L^p`, or another space selected by the kernel, but the source object and its norm must be fixed without inspecting the hypothetical defects. A proposal that simply proves absolute continuity of the canonical Riesz source has hidden the target conclusion in its hypothesis.

A valid global argument must connect three quantities without oracle dependence: the independently generated auxiliary source budget/regularity, the arithmetic geometry of the defect set, and the Poisson capacity of that geometry. Counting defects alone is insufficient because clustered targets reuse budget; local one-target costs alone are invalid because the critical capacity is genuinely nonadditive; and a concentration penalty chosen after seeing the target configuration would simply encode the desired conclusion. Singular regimes such as growing target number and scale-separated depth ratios remain to be analyzed rather than assumed to inherit the fixed-configuration law.