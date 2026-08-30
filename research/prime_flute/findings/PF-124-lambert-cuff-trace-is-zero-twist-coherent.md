# PF-124 — PF-121 Lambert cuff traces are exactly zero-twist coherent

**Status:** `EXACT-DERIVED + POSITIVE/BOUNDARY`. PF-121 already constructs asymptotically bilipschitz homeomorphisms of the one-parameter ideal Lambert quadrilaterals. The project-specific result here is that its explicit formula also supplies a **neighbor-independent finite-cuff parametrization**: after reflecting the half-cuff trace, the resulting full-cuff map commutes exactly with the canonical zero-twist orientation reversal. Thus shared finite cuffs and pant doubling do not create an additional coherence obstruction in the accepted prime/shift-clone relative-operator program. The bounded-height split-ray transition remains open, so no global metric equivalence, compact relative resolvent, scattering statement, or RH consequence is claimed.

## Claim

Use the PF-121 log-polar model

\[
D_a=\{(u,w):0\le u\le a,\ 0\le w\le W_a(u)\},
\qquad
W_a(u)=\arcsin\frac{\cosh u}{\cosh a},
\]

for the canonical ideal Lambert quadrilateral `Q(a)`. Its finite cuff side is `w=0`, with `u` equal to hyperbolic arclength from one endpoint. Let

\[
a'=a+\delta,\qquad \delta\ge0,
\qquad
c=\frac{\cosh a'}{\cosh a},
\]

and put

\[
u_1=\operatorname{arcosh}(c\cosh1),
\qquad
f(u)=\operatorname{arcosh}(c\cosh u).
\]

The PF-121 map restricts to the finite side as

\[
\boxed{
T_{a,a'}(u)=
\begin{cases}
 u_1u,&0\le u\le1,\\[4pt]
 f(u),&1\le u\le a.
\end{cases}}
\tag{1}
\]

This trace has four properties needed by the global zero-twist gluing problem:

1. it depends **only** on the cuff pair `(a,a')`, not on the other finite cuff of the pant;
2. it maps endpoints exactly,
   \[
   T_{a,a'}(0)=0,
   \qquad
   T_{a,a'}(a)=a';
   \tag{2}
   \]
3. for `a` large and `delta` small,
   \[
   \boxed{\operatorname{Bilip}(T_{a,a'})\le1+C\delta}
   \tag{3}
   \]
   with an absolute `C`;
4. after the canonical reflection across the two seam feet, it extends to a full cuff map that commutes exactly with the zero-twist gluing involution.

More explicitly, parameterize a full cuff of length `2a` by

\[
C_a=\mathbb R/(2a\mathbb Z)
\]

with the two seam feet at `0` and `a`. Define

\[
\boxed{
\widehat T_{a,a'}(s)=
\begin{cases}
 T_{a,a'}(s),&0\le s\le a,\\[4pt]
 2a'-T_{a,a'}(2a-s),&a\le s\le2a,
\end{cases}}
\tag{4}
\]

modulo `2a'`. If

\[
J_a(s)=-s\pmod{2a}
\]

is the orientation-reversing cuff isometry fixing the two seam feet, then

\[
\boxed{
\widehat T_{a,a'}\circ J_a
=
J_{a'}\circ\widehat T_{a,a'}.
}
\tag{5}
\]

Consequently two matched pants that are glued with zero twist along a cuff `C_a` can be mapped to the corresponding target pants and glued along `C_{a'}` with **no boundary mismatch and no induced twist**, provided each pant uses the PF-121 trace on that cuff.

For the exact prime/shift-clone half-cuffs

\[
a_n=\frac{\ell_n}{2},
\qquad
a_n^+=\frac{\ell_n^+}{2},
\]

PF-107 gives

\[
\delta_n:=a_n^+-a_n
=\frac1{p_{n-1}}+o(p_{n-1}^{-1})
\longrightarrow0.
\tag{6}
\]

Therefore

\[
\boxed{
\operatorname{Bilip}(\widehat T_{a_n,a_n^+})\longrightarrow1.
}
\tag{7}
\]

The divergence of `sum delta_n` is irrelevant to the **coherence** statement: equation (5) is exact cuff by cuff. PF-123 also shows that the eventual compact-resolvent step, if a global metric comparison is constructed, requires only metric coefficients tending to one rather than summability of these boundary costs.

## 1. The PF-121 formula already chooses a canonical cuff trace

PF-121 constructs its quadrilateral map in two pieces. On `0<=u<=1`,

\[
F_{\rm base}(u,w)=(u_1u,R(u)w),
\]

while on `u>=1`,

\[
F_{\rm tail}(u,w)=(f(u),w).
\]

Restricting to `w=0` gives exactly (1). The two formulas agree at `u=1` because `f(1)=u_1`, so `T_{a,a'}` is continuous. It is strictly increasing because both derivatives are positive. Equation (2) follows from

\[
f(a)
=\operatorname{arcosh}(c\cosh a)
=\operatorname{arcosh}(\cosh a')
=a'.
\]

Nothing in (1) contains the neighboring pant parameter `b`. This is the useful point that was not extracted in PF-121: the one-parameter Lambert factorization of PF-119 did not merely remove the other cuff from the interior shape; it also removed it from the actual finite-cuff boundary parametrization furnished by the explicit near-isometry.

The dependence on `(a,a')` is quantitatively mild. Since

\[
\log c
=\log\cosh(a+\delta)-\log\cosh a
=\int_a^{a+\delta}\tanh t\,dt,
\]

we have

\[
0\le\log c\le\delta.
\tag{8}
\]

For the tail branch PF-121 computes

\[
f'(u)
=\frac{c\sinh u}{\sinh f(u)},
\qquad
1-f'(u)^2
=\frac{c^2-1}{c^2\cosh^2u-1}.
\tag{9}
\]

Uniformly for `u>=1` and sufficiently small `delta`, (8)--(9) give

\[
1-C_1\delta\le f'(u)\le1.
\tag{10}
\]

On the base branch, `T'=u_1`; smooth dependence of `arcosh(c cosh 1)` at `c=1` gives

\[
1\le u_1\le1+C_2\delta.
\tag{11}
\]

Equations (10)--(11) prove (3). They also show that the trace itself is uniformly close to arclength identity in the natural endpoint coordinates:

\[
\boxed{
\sup_{0\le u\le a}|T_{a,a'}(u)-u|
\le C_3\delta.
}
\tag{12}
\]

For `u>=1`, one may differentiate `arcosh(e^r\cosh u)` in `r=log c`; the derivative is `coth(f(u))<=coth(1)`, and (8) gives the bound. The base branch follows from (11).

## 2. Reflection produces an exact full-cuff map

A hyperbolic pair of pants is the double of its canonical right-angled hexagon, with the one-cusp case obtained by replacing one boundary side by an ideal vertex. On every finite cuff the two seam feet divide the cuff into the two congruent half-cuffs used by PF-119--PF-121.

Equation (4) is therefore the natural reflection of the PF-121 half-cuff trace. It is continuous at `s=a` because both branches equal `a'`, and it closes continuously at `s=0=2a` because the two values are `0` and `2a'` modulo the target circumference. Its derivative on the reflected half is `T'(2a-s)`, so it has exactly the same bilipschitz bound as `T`.

The reflection-equivariance (5) is an identity. For `0<=s<=a`,

\[
\widehat T(J_a s)
=\widehat T(2a-s)
=2a'-T(s)
=J_{a'}(\widehat T(s)),
\]

and the other half follows by the same calculation. No limiting argument, summation, or prime estimate enters this step.

The same identity also removes a separate apparent issue in **doubling a pentagon to a pant**. If a label-preserving pentagon map is defined on one canonical half, define it on the reflected half by conjugating with the source and target pant reflections. Along every seam the reflection fixes the seam set, so the two definitions agree there. On the finite cuff the induced full boundary map is exactly (4).

## 3. Zero-twist gluing now commutes exactly

Take two source pants sharing a cuff `C_a` and their two target pants sharing `C_{a'}`. In seam-based arclength coordinates the zero-twist gluing is the orientation-reversing identification

\[
s\longmapsto -s,
\]

up to the harmless choice of which seam foot is called `0`. The target zero-twist gluing has the same form with circumference `2a'`.

Equation (5) says precisely that the square formed by the source gluing, the two copies of `widehat T`, and the target gluing commutes. Hence the two pant maps descend through the quotient to a single continuous map across the shared cuff. Because the same pair `(a,a')` is seen from both adjacent pants, **no neighboring cuff length or prime-gap ratio can change this boundary trace**.

Thus the accepted clue's former requirement

```text
choose a finite-cuff trace depending only on (a_n,a_n^+)
so that adjacent pants glue with zero twist
```

is not an additional construction problem. PF-121 already contains such a trace once its formula is read on the finite side and reflected canonically.

This conclusion is stronger than merely saying that the boundary lengths are close. A pair of arbitrary near-isometries on adjacent pants could still induce incompatible parametrizations of their common cuff. Here the parametrization itself is fixed by a one-parameter formula and satisfies the exact gluing conjugacy (5).

## 4. Specialization to the all-composite shift clone

PF-107 proves

\[
\ell_n^+-\ell_n
=\frac{2}{p_{n-1}}+o(p_{n-1}^{-1}),
\]

so (6) follows. Combining this with (3)--(5) gives the tail statement

\[
\boxed{
\text{shared-cuff mismatch}=0,
\qquad
\text{cuff-trace bilipschitz cost}=1+o(1).
}
\tag{13}
\]

The first statement is exact and the second is pointwise along the escaping cuffs. One must **not** turn the `O(1/p_n)` bound into an `ell^1` claim: PF-107 explicitly shows that the additive cuff defect has a divergent reciprocal-prime component. There is no need to do so here. Coherence is algebraic, and PF-123's compact-resolvent criterion is rate-free once the complete metric coefficients converge.

This also explains why the nonsummable reverse arc-distance floor in PF-118 is not a cuff-gluing obstruction. That floor comes from the shrinking cross-cuff seam. The finite-cuff trace can still be chosen coherently on every pant with distortion tending to one.

## 5. Consequence for the accepted relative-operator clue

PF-119--PF-123 had reduced the geometric side of the clone comparison to a boundary-coherence problem. PF-124 removes the **finite-cuff and zero-twist** part of that problem.

The remaining local gate is now only the following. On each normalized PF-119 pentagon, reconcile the two PF-121 Lambert maps with the PF-122 map on `y>=1` across a bounded-height region so that

1. the two lower Lambert pieces induce one identical trace on their artificial split ray;
2. their outer finite-cuff traces remain the fixed maps `T_{a,a'}` from (1);
3. the transition bilipschitz constant tends to `1` uniformly even when the split ratio tends to `0` or `1`.

Once such a **single pentagon map** exists, there is no further independent doubling or shared-cuff choice: reflect it to the second half of each pant, use (5) on every finite cuff, and the zero-twist chain glues automatically. The only subsequent geometric check is that the resulting complete-surface metric tensor tends uniformly to the identity; PF-123 then supplies compact relative resolvent and equality of essential spectra.

So the unresolved bridge has sharpened to

\[
\boxed{
\text{bounded-height split-ray reconciliation}
\quad\text{rather than}\quad
\text{cuff parametrization or zero-twist accumulation}.}
\tag{14}
\]

No spectral conclusion follows from PF-124 by itself.

## 6. Prior-art / novelty audit

No novelty is claimed for the standard facts that hyperbolic pants are doubles of right-angled hexagons/pentagons, that seam feet split each geodesic boundary into two equal half-cuffs, or that zero twist is expressed by aligning the seam markings. These are ordinary Fenchel--Nielsen geometry. Likewise, reflecting a boundary homeomorphism and checking a commuting gluing square is elementary topology.

PF-118 already audits Alessandrini--Disarlo's arc-distance theorem. Their optimal boundary-respecting Lipschitz maps do not provide the homeomorphic, prescribed boundary parametrization required for this infinite gluing problem. PF-121 supplies the missing explicit homeomorphism locally. The present result uses **its exact formula**, not a new general extension theorem.

Directed literature searches for prescribed bilipschitz boundary parametrizations of hyperbolic pants, zero-twist-compatible pants maps, and Lambert-quadrilateral boundary traces found the standard Fenchel--Nielsen/seam framework but no statement corresponding to the exact trace (1) for the PF-121 map or its prime/shift-clone specialization. The durable Mathia content is therefore deliberately narrow:

\[
\boxed{
\text{PF-121 explicit Lambert map}
\Longrightarrow
\text{neighbor-independent }T_{a,a'}
\Longrightarrow
\text{exact zero-twist cuff coherence}.}
\tag{15}
\]

This is a project-specific boundary lemma for the accepted operator program, not a broad novelty claim about Teichmüller theory and not evidence for RH.

## 7. Falsification core

The result has five direct gates:

1. restrict the two explicit PF-121 formulas to `w=0` and verify (1);
2. check `T(0)=0`, `T(a)=a'`, strict monotonicity, and the derivative bounds (8)--(11);
3. reflect `T` by (4) and verify continuity plus the exact commutation relation (5);
4. check that the canonical zero-twist marking identifies seam feet by the corresponding orientation-reversing cuff map, so (5) is exactly the quotient compatibility condition;
5. specialize only after those geometric steps, using PF-107 to obtain `delta_n->0` and hence (7).

Failure of any of steps 1--4 invalidates the claimed removal of the cuff-coherence gate. Even if all five hold, the accepted clue remains unresolved until the bounded-height split-ray transition is constructed or obstructed.