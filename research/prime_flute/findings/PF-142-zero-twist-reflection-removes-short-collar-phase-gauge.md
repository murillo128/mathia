# PF-142 — zero-twist reflection removes the short-collar phase gauge

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + NEGATIVE/BOUNDARY`. PF-141 proves that a bounded constant angular phase on one collapsing standard collar can be welded at Güneysu--Thalmaier weighted cost `O(L|tau|)`, but deliberately leaves open whether the total phase budget is summable across the complete PF-138 family of short cores. In the canonical prime/shift-clone comparison that possible obstruction is in fact a **coordinate gauge rather than an independent geometric datum**. PF-124 supplies an exactly reflection-equivariant zero-twist body trace, while PF-138 shows that every tail Margulis-short core is reflection-invariant and meets the fixed locus in exactly two points. Marking those two points by the ordered cusp-block data pins the angular origin on every matched short collar. A reflection-equivariant collar/body trace then has zero constant rotation phase. The half-turn ambiguity of an unmarked reflected circle is removed by the marking. What remains is only the nonconstant reflection-odd angular reparametrization and the transverse/radial shape mismatch of the body trace. Thus no global estimate of `sum L_eta` is needed for the **constant phase mode**, but the accepted wave-operator clue is not yet resolved.

## Claim

Let `X` be the exact zero-twist prime flute and `X_+` its exact all-composite shift clone. Let

\[
\rho:X\to X,
\qquad
\rho_+:X_+\to X_+
\tag{1}
\]

be their canonical orientation-reversing zero-twist reflections. Choose the prime/clone body comparison on each canonical half-pant by the PF-121 construction and extend it to the reflected half exactly as in PF-124. Then on every shared distinguished cuff this comparison satisfies

\[
F\circ\rho=\rho_+\circ F,
\tag{2}
\]

and the same reflection-equivariant choice is available on the pant body adjacent to every PF-138 canonical short separator.

For every sufficiently far Margulis-short closed core `eta`, PF-138 gives

\[
\rho(\eta)=\eta
\tag{3}
\]

and proves that `rho|_eta` is a reflection of the geodesic circle with exactly two fixed points. The matched clone core `eta_+` has the corresponding two fixed points. Use the ordered consecutive-cusp-block marking to distinguish the two ends of the quotient arc `eta/rho`, and hence to label the fixed points

\[
x_0,x_{1/2}\in\eta,
\qquad
x_0^+,x_{1/2}^+\in\eta_+.
\tag{4}
\]

Normalize Fermi collar coordinates by

\[
\eta=\{r=0\},
\qquad
x_0=(0,0),
\qquad
x_{1/2}=(0,1/2),
\tag{5}
\]

and similarly on the target. Then

\[
\rho(r,\theta)=(r,-\theta),
\qquad
\rho_+(r_+,\theta_+)=(r_+,-\theta_+)
\pmod 1.
\tag{6}
\]

If the interface trace of a reflection-equivariant marked comparison is

\[
f:\mathbb S^1\to\mathbb S^1,
\tag{7}
\]

then

\[
\boxed{
f(-\theta)=-f(\theta)\pmod1,
\qquad
f(0)=0,
\qquad
f(1/2)=1/2.
}
\tag{8}
\]

In particular, if its angular mismatch is decomposed relative to the marked identity as

\[
f(\theta)-\theta
=\tau+\psi(\theta)
\pmod1,
\qquad
\psi(0)=0,
\tag{9}
\]

where `tau` is the constant rotation phase, then evaluating at the marked fixed point gives

\[
\boxed{\tau=0\pmod1.}
\tag{10}
\]

Equivalently, after fixing the canonical reflection marking, a constant collar rotation is **not a free assembly parameter**. Any remaining angular discrepancy satisfies the reflection parity condition

\[
\boxed{
\psi(-\theta)=-\psi(\theta),
\qquad
\psi(0)=\psi(1/2)=0.
}
\tag{11}
\]

The finite exceptional head contains only finitely many short collars and is irrelevant to global summability.

## 1. PF-124 already supplies the required equivariant body representative

PF-124 does more than show that zero-twist cuff identifications are topologically compatible. Its full-cuff trace is obtained by reflecting the PF-121 half-cuff map and satisfies the exact identity

\[
\widehat T_{a,a'}\circ J_a
=J_{a'}\circ\widehat T_{a,a'}.
\tag{12}
\]

The same finding states that a label-preserving pentagon map defined on one canonical half can be doubled to the other half by conjugating with the source and target pant reflections. Therefore the local body comparison can be chosen from the outset so that (2) is an identity, not an asymptotic estimate.

This matters because an arbitrary bilipschitz representative could manufacture an angular phase that is absent from the marked zero-twist geometry. The wave-comparison program is an existence problem for one admissible global marked comparison; it is therefore legitimate, and strictly better conditioned, to retain the exact reflection symmetry already built into the construction.

PF-139 and PF-140 do not require breaking this symmetry: their lower-pant and cusp corrections are performed from the canonical split geometry and can be applied on one reflection half and doubled. PF-142 does not claim that every possible implementation is automatically equivariant. It records that a canonical equivariant representative exists and that no spectral conclusion should depend on a phase introduced solely by abandoning it.

## 2. Every tail short core has a canonical angular origin

PF-138 proves two facts needed here. First, every sufficiently far simple closed geodesic below the collar threshold is a canonical separator of a finite consecutive cusp block. Second, because the zero-twist reflection fixes each end, such a separator is setwise invariant and its quotient by reflection is a proper arc in the quotient disk.

The restriction of an orientation-reversing involution to the invariant geodesic circle has exactly two fixed points. Those are precisely the endpoints of the quotient arc. For a consecutive block the two complementary sides of that quotient arc are distinguished by the ordered cusp chain: one faces the earlier end of the block and the other the later end. Hence the project already carries enough marking data to label the two reflection-fixed points consistently in source and clone.

This removes a small but important ambiguity. Reflection symmetry **without** a marking would allow a target circle map to exchange the two fixed points, corresponding to a half-turn `theta -> theta+1/2`. The ordered block/seam marking excludes that exchange. Thus the correct residual symmetry is (8), not merely preservation of the unordered fixed-point pair.

## 3. Reflection equivariance kills only the constant Fourier mode

Let `f` be the angular component of an interface trace after source and target Fermi coordinates have been normalized by (4)--(6). Equation (2) gives

\[
f(-\theta)=-f(\theta)\pmod1.
\tag{13}
\]

The marked point `theta=0` must map to `theta_+=0`, so a constant phase measured by that point is exactly zero. Likewise the second marked fixed point maps to `1/2`.

It is useful to state precisely what has **not** disappeared. A nonconstant odd circle homeomorphism can satisfy (8) while still differing substantially from the identity. In a lift with `f(0)=0`, write

\[
f(\theta)=\theta+\psi(\theta).
\tag{14}
\]

Reflection equivariance gives the first relation in (11), and the second fixed point gives the second vanishing condition. Neither relation controls `psi'`, nor does it show that the body image of a standard collar boundary is itself a standard collar boundary. Therefore PF-142 does not provide the transverse/shape straightening estimate that the accepted wave clue still needs.

This is why the result is stronger than PF-141 in one direction and weaker in another. PF-141 can interpolate an **arbitrary** bounded phase even for a non-equivariant local map. PF-142 shows that the canonical equivariant marked comparison need never create that phase in the first place. But PF-141's explicit metric estimate remains relevant if an auxiliary smoothing step temporarily breaks the normalization, and neither finding estimates the nonconstant trace-shape mode.

## 4. The `sum L_eta` phase ledger is therefore unnecessary

PF-141 obtains the local bound

\[
\operatorname{Cost}_{\rm phase}(\eta)
\le C L_\eta|\tau_\eta|
\tag{15}
\]

and correctly refuses to infer convergence from an unproved statement such as

\[
\sum_\eta L_\eta<\infty.
\tag{16}
\]

For the canonical reflection-equivariant marked comparison, (10) instead gives

\[
\boxed{
L_\eta|\tau_\eta|=0
\quad\text{for every tail PF-138 short core}.}
\tag{17}
\]

So (16) is simply not the gate for the constant phase sector. The finite exceptional head may be welded individually at finite cost and has no effect on convergence.

This is a gauge elimination, not a new summability theorem. It does **not** say that the lengths of all short separators are summable, nor that every interface contribution is zero. It says only that the global comparison should not spend analytic budget on a constant angular degree of freedom that the exact zero-twist marking has already fixed.

## 5. Stress tests and failure modes

The claim survives the following checks only in its stated marked-equivariant form.

1. **Forget the marking.** Reflection alone preserves the unordered pair of fixed points and permits a half-turn. Therefore `tau=0` is false without choosing the canonical block/seam label.
2. **Choose an arbitrary non-equivariant body map.** A constant phase can be introduced by hand. PF-142 does not prohibit that; it shows that such a phase is not forced by the geometry and can be avoided by the canonical representative.
3. **Allow a nonconstant odd reparametrization.** Equation (11) permits it. Its first-derivative and transverse costs are part of the still-open interface problem.
4. **Move the collar boundary transversely.** Reflection symmetry does not control radial displacement or noncircularity. PF-128's optimized standard-collar map still has to be inserted coherently into the global body map.
5. **Infer scattering.** Equations (8)--(17) remove only one assembly mode. They do not establish the global Güneysu--Thalmaier weighted integral, complete wave operators, equality of absolutely continuous spectra, scattering matrices, resonances, determinants, or any RH statement.

## 6. Novelty / prior-art audit

No novelty is claimed for the classical facts that zero Fenchel--Nielsen twist aligns seam markings, that a symmetric pair of pants can be doubled across its seams, or that an orientation-reversing reflection of a geodesic circle has two fixed points. Those are standard hyperbolic/Teichmüller geometry and are already part of the background audited in S1 and PF-124/PF-138.

Directed searches for zero-twist pants reflections, seam-aligned Fenchel--Nielsen coordinates, reflection-equivariant cuff maps, and short-collar phase normalization found only the standard symmetry framework. No external result was found that addresses the project-specific question of whether the **constant phase term in the prime/shift-clone Güneysu--Thalmaier collar assembly** is a genuine summability variable.

The durable contribution is therefore deliberately narrow:

\[
\boxed{
\text{PF-124 equivariant body map}
+\text{PF-138 marked short-core reflection}
\Longrightarrow
\tau_\eta=0
\text{ for every tail short collar}.}
\tag{18}
\]

This is a boundary simplification of the accepted wave-comparison program, not a general theorem about Fenchel--Nielsen coordinates and not evidence for RH.

## Research consequence

PF-141 left the closed-thin interface ledger schematically as

\[
\text{length change}
+\text{constant phase}
+\text{nonconstant/transverse trace shape}.
\]

PF-128 controls the first term and PF-142 removes the second term for the canonical marked equivariant comparison. The remaining gate is therefore

\[
\boxed{
\text{nonconstant reflection-odd angular trace}
+\text{transverse/radial collar-body shape},
}
\tag{19}
\]

with a summable total Güneysu--Thalmaier weighted cost still to be proved or decisively obstructed.

The accepted clue `CLUE-shift-clone-wave-operator-equivalence` should consequently no longer treat `sum L_eta|tau_eta|` as a possible global gate. A positive resolution still requires one smooth complete globally marked comparison; a negative resolution must now locate an intrinsic obstruction in the remaining shape sector rather than in a constant phase gauge.

## Falsification core

A later adversary can test PF-142 through the following finite chain:

1. verify PF-124's exact reflection relation (12) and that the chosen half-pant maps can be doubled equivariantly;
2. verify PF-138's classification and its statement that every tail short canonical separator has exactly two reflection-fixed points;
3. check that the ordered consecutive-block/seam marking distinguishes those two fixed points in source and clone, excluding the half-turn;
4. normalize Fermi angular coordinates by those points and derive (8) directly from equivariance;
5. evaluate the angular trace at `theta=0` to obtain (10);
6. confirm that no step constrains the nonconstant odd mode or transverse boundary shape.

Failure of steps 1--3 invalidates the global phase elimination. Even if all six steps hold, PF-142 does not resolve the wave-operator clue until the remaining shape/interface weighted integral is controlled.