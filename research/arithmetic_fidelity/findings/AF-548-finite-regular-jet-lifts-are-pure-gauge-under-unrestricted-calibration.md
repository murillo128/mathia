# AF-548 — Finite regular jet lifts are pure gauge under unrestricted calibration

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `CALIBRATION` · `JET-LIFT` · `NO-GO` · `NO-NOVELTY-CLAIM`

## Claim

AF-547 shows that unrestricted cubic scalar recalibrations generate an infinite-dimensional Lie closure, so adding more finitely many scalar branches cannot produce a universal quantitative invariant. A natural escape is to retain derivatives of those branches. For regular branches, that escape also fails at every finite jet order.

Let (I\subset\mathbb R) be an open interval, let (n,k\ge1), and let (q_i:(\mathbb R,0)\to I) be (C^k) germs with pairwise distinct base values (x_i=q_i(0)) and nonzero first derivatives (v_i=q_i'(0)\ne0). The orientation-preserving calibration pseudogroup acts diagonally by postcomposition,
[
(q_1,\dots,q_n)\mapsto(\phi\circ q_1,\dots,\phi\circ q_n),\qquad \phi'>0.
]

Then two regular (k)-jet tuples ((j_0^k q_i)_i) and ((j_0^k\widetilde q_i)_i) lie in the same orbit whenever and only whenever they have the same labelled order type of base values and the same sign of the first derivative on each branch:
[
x_i<x_j\Longleftrightarrow \widetilde x_i<\widetilde x_j,
\qquad
\operatorname{sgn}q_i'(0)=\operatorname{sgn}\widetilde q_i'(0).
]

Consequently, on each regular order/sign chamber, the prolonged action is transitive at every finite jet order. Any invariant depending only on finitely many finite-order branch jets and invariant under all orientation-preserving smooth recalibrations is constant on that chamber.

Thus **adding finitely many derivatives of finitely many separated regular scalar branches does not repair AF-547's unrestricted-calibration loss**. Jet order is not the missing resource. A nontrivial quantitative repair must retain structure that prevents the calibration jet at one observed value from being chosen independently of the calibration jet at another.

## Derivation

For an orientation-preserving calibration (phi), (phi'(x)>0), so labelled order and the sign of each first derivative are preserved.

Faà di Bruno gives
[
(\phi\circ q_i)^{(m)}(0)
=
\sum_{r=1}^m
\phi^{(r)}(x_i)
B_{m,r}\bigl(q_i'(0),\dots,q_i^{(m-r+1)}(0)\bigr).
\tag{1}
]
The coefficient of the highest calibration derivative is
[
B_{m,m}(q_i'(0))=q_i'(0)^m\ne0.
\tag{2}
]

Given a target regular jet, prescribe
[
\phi(x_i)=\widetilde x_i,
\qquad
\phi'(x_i)=\frac{\widetilde q_i'(0)}{q_i'(0)}>0.
\tag{3}
]
Recursively, once the lower derivatives of (phi) at (x_i) are fixed, (1)--(2) determine a unique (phi^{(m)}(x_i)) giving the requested (m)-th target derivative. Thus every target branch jet in the same sign chamber gives a compatible positive finite jet of the calibration at (x_i).

Because the (x_i) are distinct, choose pairwise disjoint neighborhoods. Standard finite smooth jet interpolation realizes the prescribed calibration jet at each marked point. Shrink those neighborhoods until the derivative stays positive. Since the target marked values have the same order, the complementary gaps can be joined by smooth positive derivatives with the required integrals. Integrating and extending monotonically to the interval ends produces one orientation-preserving smooth diffeomorphism realizing all prescribed jets.

Therefore the order/sign conditions are both necessary and sufficient. Every connected component of the regular finite-jet configuration space determined by those discrete data is one orbit.

## Singular-jet control

Regularity is load bearing. If
[
q'(0)=\cdots=q^{(r-1)}(0)=0,
\qquad q^{(r)}(0)\ne0,
]
then
[
(\phi\circ q)(u)-\phi(q(0))
=
\phi'(q(0))\frac{q^{(r)}(0)}{r!}u^r+O(u^{r+1}),
]
so the first nonzero derivative order and the sign of its leading coefficient survive orientation-preserving recalibration. AF-548 does not classify singular strata.

The theorem is therefore not “all derivatives are useless.” It is that ordinary finite derivative data of regular separated scalar branches are not extra structure against an unrestricted output diffeomorphism.

## Fidelity / representation audit

AF-547 left derivative/jet information among the possible lifts after finite point values became fully mobile. AF-548 narrows that boundary. A derivative lift can become useful only when coupled to additional structure that removes independent calibration-jet freedom at distinct output values: an external reference field, fixed calibration anchors, a restricted nuisance class, repeated or overlapping branch values, or a metric/operator/dynamical structure that the calibration must preserve. Merely differentiating the same scalar outputs does not create such coupling.

## Prior-art / novelty audit

No novelty is claimed for the underlying mathematics.

- J. W. Bruce, T. Gaffney, and A. A. du Plessis, *On Left Equivalence of Map Germs*, *Bulletin of the London Mathematical Society* 16(3), 303–306 (1984), DOI `10.1112/blms/16.3.303`, places target-diffeomorphism equivalence of map germs inside classical singularity theory.
- Francis Valiquette, *Solving Local Equivalence Problems with the Equivariant Moving Frame Method*, *SIGMA* 9 (2013), 029, DOI `10.3842/SIGMA.2013.029`, develops local equivalence and differential invariants for prolonged Lie pseudogroup actions on jets.
- Boris Kruglikov and Valentin Lychagin, *Global Lie–Tresse theorem*, *Selecta Mathematica* 22(3), 1357–1411 (2016), DOI `10.1007/s00029-015-0220-z`, gives the broader differential-invariant framework for algebraic pseudogroup actions.

The triangular formula is classical Faà di Bruno calculus, and simultaneous interpolation of finitely many smooth jets is standard smooth interpolation. The durable Arithmetic Fidelity delta is its placement after AF-546/AF-547: once the nuisance class reaches unrestricted scalar diffeomorphism freedom, finite derivative enrichment of regular separated branches is still inside the same orbit rather than being an independent lift.

## Boundaries and failure modes

- Every fixed finite jet order is covered; arbitrary full germs, analytic germs, and nonlocal profiles are not classified.
- Singular contact order can survive.
- Coincident branch values force the same calibration jet to act more than once and can create relative invariants.
- Finite-dimensional calibration families remain in the AF-546 regime.
- Higher-dimensional target diffeomorphisms have different jet geometry.
- Nothing here distinguishes rational primes or constrains zeta zeros.

## Decisive audit test

For any proposed scalar-compression repair based on finitely many branch derivatives, write the nuisance action on the retained jets first. If branch values are distinct and regular and the nuisance contains the full orientation-preserving smooth calibration pseudogroup, equations (1)--(3) make the action triangularly surjective onto every target jet chamber. The proposal is then pure gauge unless it identifies an additional condition coupling calibration jets at different output values.

## Consequence for the research line

AF-546 found the affine/projective finite-dimensional invariant hierarchy. AF-547 showed that unrestricted cubic generators cross into infinite Lie closure and kill finite-point relational quotients. AF-548 closes the immediate derivative escape: **finite regular jets of finitely many separated branches do not restore quantitative fidelity under unrestricted monotone calibration**.

The next nontrivial question is not “how many derivatives should be retained?” but what forces calibration information at distinct observed values to be shared rather than independently programmable. Range overlap, recurrent value incidence, anchored reference geometry, or a restricted nuisance law are now the structurally meaningful places to look.
