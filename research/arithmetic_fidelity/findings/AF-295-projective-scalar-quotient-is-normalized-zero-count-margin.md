# AF-295 — Projective scalar quotient exactly realizes normalized zero-count margin

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `GAUGE-QUOTIENT`, `PROJECTIVE`, `CONDITIONING`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-290 introduced the normalized boundary-zero margin

\[
\delta_D(b):=\frac{\operatorname{dist}(b,D)}{\|b\|},
\]

and AF-291--AF-294 showed that this margin collapses for finite eta truncations and cannot be repaired for free by diagonal Hilbert scaling, bounded-condition dense Hilbert mixing, or uniformly quasisymmetric nonlinear reparameterization.

There is an obvious remaining objection: the denominator `||b||` might be an artifact of retaining an irrelevant amplitude direction. For zero-based targets that objection can be removed exactly.

Let `H` be a finite-dimensional complex Hilbert space, let `D subset H` be a nonempty **complex cone**,

\[
\lambda D\subseteq D\qquad(\lambda\in\mathbb C),
\]

and let `b notin D`, `b != 0`. Write `P(H)` for complex projective space and

\[
\mathbb P D:=\{[d]:d\in D\setminus\{0\}\}.
\]

For nonzero `x,y`, define the projective gap metric

\[
d_{\mathrm{gap}}([x],[y])
:=
\sqrt{1-
\frac{|\langle x,y\rangle|^2}
{\|x\|^2\|y\|^2}}
=
\|P_x-P_y\|_{\mathrm{op}},
\]

where `P_x` is orthogonal projection onto the line `C x`. Then

\[
\boxed{
\operatorname{dist}_{\mathrm{gap}}([b],\mathbb P D)
=
\frac{\operatorname{dist}(b,D)}{\|b\|}.
}
\]

Equivalently, for the Fubini--Study geodesic distance normalized by

\[
d_{\mathrm{FS}}([x],[y])
=
\arccos\frac{|\langle x,y\rangle|}{\|x\|\|y\|},
\]

one has

\[
\boxed{
\operatorname{dist}_{\mathrm{FS}}([b],\mathbb P D)
=
\arcsin\!\left(
\frac{\operatorname{dist}(b,D)}{\|b\|}
\right).
}
\]

Thus whenever the failure set is homogeneous under nonzero scalar multiplication, the usual normalized distance-to-discriminant is not an arbitrary Euclidean normalization. It is **exactly the natural distance to the failure set after quotienting the irrelevant complex scalar gauge**.

For finite Dirichlet zero count, the boundary-zero discriminant `Delta_{Gamma,N}` is such a cone because

\[
P_{\lambda b}(s)=\lambda P_b(s),
\]

so multiplication of all coefficients by `lambda != 0` changes neither the zero set nor the zero count. Consequently AF-290's normalized margin is literally the projective quotient margin. In particular, projectivizing away global amplitude does **not** repair the AF-291 eta collapse: it reveals that the collapse is angular/projective rather than radial.

## Exact cone-to-projective identity

Normalize `b` to `u=b/||b||`. Fix any nonzero `d in D` and put `v=d/||d||`. Since `D` is a complex cone, every scalar multiple `lambda v` belongs to `D`. Orthogonal projection onto the complex line `C v` gives

\[
\inf_{\lambda\in\mathbb C}
\|u-\lambda v\|^2
=
1-|\langle u,v\rangle|^2.
\]

Therefore the best Euclidean approximation to the source ray by the bad ray satisfies

\[
\inf_{\lambda\in\mathbb C}
\|u-\lambda v\|
=
d_{\mathrm{gap}}([b],[d]).
\]

Taking the infimum over all nonzero bad directions gives

\[
\frac{\operatorname{dist}(b,D)}{\|b\|}
=
\inf_{[d]\in\mathbb P D}
d_{\mathrm{gap}}([b],[d]).
\]

The formula does not require `D` to be linear, convex, smooth, algebraic, or a single hypersurface; conic homogeneity is the only structural input. If `D` is closed, the left side is positive exactly when the projective source ray is separated from the projectivized bad set.

Because every Fubini--Study distance lies in `[0,pi/2]` and

\[
d_{\mathrm{gap}}=\sin d_{\mathrm{FS}},
\]

monotonicity and continuity of `arcsin` give

\[
\operatorname{dist}_{\mathrm{FS}}([b],\mathbb P D)
=
\arcsin\bigl(\operatorname{dist}_{\mathrm{gap}}([b],\mathbb P D)\bigr).
\]

This is the exact quotient statement: Euclidean radial scale disappears, while the relative distance to failure survives as projective angle.

## Dirichlet boundary-zero discriminant

For

\[
P_b(s)=\sum_{n=1}^N b_n n^{-s},
\]

AF-290 defines

\[
\Delta_{\Gamma,N}
=
\{c\in\mathbb C^N:\exists z\in\Gamma,\ P_c(z)=0\}.
\]

It is a union of complex hyperplanes and hence a complex cone. With the canonical coefficient inner product,

\[
\delta_{\Gamma,N}(b)
:=
\frac{\operatorname{dist}_2(b,\Delta_{\Gamma,N})}{\|b\|_2}
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}
{\|b\|_2 H_N(\operatorname{Re}z)}.
\]

The cone identity therefore gives the exact projective formulas

\[
\boxed{
\operatorname{dist}_{\mathrm{gap}}
\bigl([b],\mathbb P\Delta_{\Gamma,N}\bigr)
=
\delta_{\Gamma,N}(b),
}
\]

and

\[
\boxed{
\operatorname{dist}_{\mathrm{FS}}
\bigl([b],\mathbb P\Delta_{\Gamma,N}\bigr)
=
\arcsin\delta_{\Gamma,N}(b).
}
\]

The point-hyperplane version is equally explicit. For fixed `z`, let

\[
r_z=(n^{-\overline z})_{n=1}^N.
\]

Then `ker L_z=r_z^perp`, and the sine of the projective angle from `[b]` to `P(ker L_z)` is

\[
\frac{|r_z^*b|}{\|r_z\|_2\|b\|_2}
=
\frac{|P_b(z)|}{H_N(\operatorname{Re}z)\|b\|_2}.
\]

Thus the normalized evaluation ratio already appearing in AF-290 is exactly the angular separation from one projective bad hyperplane; minimizing over the contour gives the projective discriminant distance.

## Arbitrary Hilbert geometry descends the same way

The identity is not special to the Euclidean coefficient metric. Let `G>0` be Hermitian and write

\[
\langle x,y\rangle_G=x^*Gy,
\qquad
\|x\|_G=(x^*Gx)^{1/2}.
\]

Equip projective space with the gap/Fubini--Study geometry induced by this Hilbert structure. Since `Delta_{Gamma,N}` is still the same scalar-invariant cone,

\[
\boxed{
\operatorname{dist}_{\mathrm{gap},G}
\bigl([b],\mathbb P\Delta_{\Gamma,N}\bigr)
=
\delta^{(G)}_{\Gamma,N},
}
\]

where AF-293's normalized Hilbert margin is

\[
\delta^{(G)}_{\Gamma,N}
=
\min_{z\in\Gamma}
\frac{|\eta_N(z)|}
{(b^*Gb)^{1/2}(r_z^*G^{-1}r_z)^{1/2}}
\]

for the eta coefficient vector.

Hence AF-293's condition-number budget is already a theorem about the best projective separation obtainable by changing Hilbert geometry. If

\[
\mathcal D_{\Gamma,N}(K)
=
\sup_{G>0:\,\kappa(G)\le K}
\delta^{(G)}_{\Gamma,N},
\]

then equivalently

\[
\sup_{\kappa(G)\le K}
\operatorname{dist}_{\mathrm{gap},G}
\bigl([b^{(N)}],\mathbb P\Delta_{\Gamma,N}\bigr)
\asymp_\Gamma
\min\left\{1,
\frac{\sqrt K}{\sqrt N H_N(\alpha)}\right\}.
\]

Projectivization therefore removes the scalar nuisance exactly but does not remove the AF-293 conditioning bill. A projective Hilbert geometry can make the bad set order-one distant only by becoming anisotropic at the same reciprocal-margin scale already identified before quotienting.

## Eta-truncation consequence

For

\[
b^{(N)}=\bigl((-1)^{n-1}\bigr)_{n=1}^N,
\qquad
\eta_N(s)=P_{b^{(N)}}(s),
\]

AF-291 gives on every fixed eta-zero-free compact Jordan curve `Gamma subset {Re(s)>0}` with

\[
\alpha=\min_{z\in\Gamma}\operatorname{Re}z>0
\]

the sharp canonical margin law

\[
\delta_{\Gamma,N}(b^{(N)})
\asymp_\Gamma
\frac1{\sqrt N H_N(\alpha)}.
\]

AF-295 turns this directly into a quotient statement:

\[
\boxed{
\operatorname{dist}_{\mathrm{gap}}
\bigl([b^{(N)}],\mathbb P\Delta_{\Gamma,N}\bigr)
\asymp_\Gamma
\frac1{\sqrt N H_N(\alpha)}
\longrightarrow0.
}
\]

The Fubini--Study distance has the same asymptotic law because `arcsin t ~ t` at zero. In particular,

\[
\operatorname{dist}_{\mathrm{FS}}
\bigl([b^{(N)}],\mathbb P\Delta_{\Gamma,N}\bigr)
\asymp_\Gamma
\begin{cases}
N^{-1/2}, & \alpha>1/2,\\
(N\log N)^{-1/2}, & \alpha=1/2,\\
N^{-(1-\alpha)}, & 0<\alpha<1/2.
\end{cases}
\]

If the contour surrounds a critical-line point, then necessarily `alpha<1/2`; writing `alpha=1/2-epsilon` gives projective margin

\[
\asymp_\Gamma N^{-1/2-\varepsilon}.
\]

Thus the vanishing eta zero-count margin is **not caused by the coefficient norm paying for an irrelevant global amplitude coordinate**. After quotienting that coordinate out exactly, the source ray itself approaches the projectivized boundary-zero discriminant at the same rate.

## Prior art and novelty assessment

The projective geometry used here is classical and no general novelty is claimed.

- The Fubini--Study metric on complex projective space is induced by the Hermitian inner product and satisfies
  `cos d_FS([x],[y])=|<x,y>|/(||x||||y||)`. A standard reference is the *Encyclopedia of Mathematics*, **“Fubini-Study metric”**, which records this distance formula and the unitary invariance of the metric.
- Distance-to-ill-posedness and homogeneous/projective conditioning are classical themes in numerical analysis and numerical algebraic geometry. James W. Demmel, **“On condition numbers and the distance to the nearest ill-posed problem,”** *Numerische Mathematik* 51(3), 251--289 (1987), DOI `10.1007/BF01400115`, is the general condition-number reference already used in AF-290--AF-294.
- Felipe Cucker, Teresa Krick, Gregorio Malajovich, and Mario Wschebor, **“A Numerical Algorithm for Zero Counting. II: Distance to Ill-posedness and Smoothed Analysis,”** *Journal of Fixed Point Theory and Applications* 6(2), 285--294 (2009), DOI `10.1007/s11784-009-0127-4`, gives a condition-number theorem in which zero-count conditioning is inverse normalized distance to an ill-posed set in a different polynomial-system setting.
- Peter Burgisser, **“Condition of Intersecting a Projective Variety with a Varying Linear Subspace,”** *SIAM Journal on Applied Algebra and Geometry* 1(1), 111--132 (2017), DOI `10.1137/16M1077222`, is neighboring projective condition-number prior art: it relates an intersection condition number to distance from an ill-posed Schubert variety.

The cone-to-projective identity itself is an elementary Hilbert/projective calculation, not a new theorem of projective geometry. The retained Arithmetic Fidelity contribution is its exact placement at the current eta frontier: AF-290's normalization is identified as the intrinsic scalar-gauge quotient metric, and AF-291/AF-293 become projective conditioning statements without changing their decay or condition-number laws.

## Boundaries and failure modes

- The exact quotient identity uses **complex scalar homogeneity** of the bad set. A target whose failure set is not invariant under global complex scaling need not admit this projective reduction.
- Projectivization removes only the `C*` amplitude/phase gauge. It does not remove other nuisance directions, such as source symmetries or acquisition gauges, unless those are separately proved target-null.
- The result does not say that every quotient preserves a vanishing margin. A genuinely target-relevant quotient can change the problem if it identifies additional directions on which the target is constant. The point here is that the most immediate scalar quotient is already exactly accounted for by the normalized margin.
- Changing the projective metric by an `N`-dependent Hilbert form can enlarge the margin, but AF-293 quantifies the required anisotropy. The quotient itself supplies no free improvement.
- A non-Hilbert projective geometry or a quotient that changes the bad set lies outside this theorem. Such a proposal must state its native metric and explain why the altered target geometry is source-natural rather than chosen to separate the answer.
- The result concerns finite zero count on a fixed contour. It does not establish zero locations, simplicity, an unbounded-height zero divisor, or RH.
- The Fubini--Study formula is invariant under global scalar multiplication but still depends on the chosen underlying Hilbert structure. AF-293 prices changes of that structure relative to the canonical coefficient geometry; AF-295 does not make all Hilbert choices equivalent.

## Decisive audit test

For any homogeneous target whose proposed instability is measured by a normalized distance

\[
\frac{\operatorname{dist}(b,D)}{\|b\|},
\]

first test whether `D` is a complex cone. If it is, compute the corresponding projective gap distance to `P D`. If the two coincide by the cone identity, then quotienting global scale cannot be invoked as an independent repair: the normalization has already performed exactly that quotient geometrically.

For finite Dirichlet zero count this test is decisive because `Delta_{Gamma,N}` is conic. Any proposal claiming that AF-291's collapse is merely a radial artifact must therefore exhibit an additional target-null quotient beyond global scalar multiplication, or a genuinely different source-natural target geometry.

## Consequence for the research line

AF-294 left a target-relevant quotient as one possible way to escape the representation-only conditioning obstruction. AF-295 closes the most canonical candidate: the global complex-scalar gauge under which the complete zero set is unchanged.

The normalized eta margin is already the exact projective distance from the coefficient ray to the projectivized boundary-zero discriminant. Its collapse survives removal of amplitude and global phase with the same asymptotic law, and AF-293's condition-number threshold survives as the exact price of changing the induced projective Hilbert geometry.

The live quotient question is therefore narrower. A useful quotient must identify **additional directions that are independently proved invisible to the RH-relevant target**, not merely remove radial scale. Equivalently, any claimed target-geometry rescue should specify which new equivalence relation changes the bad-set separation and why that relation follows from the source mathematics rather than being designed around the desired zero behavior.