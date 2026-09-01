# WP-092 — Refinement-coherent fixed infinite auxiliary sectors still freeze to one collective block

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + INFINITE-AUXILIARY + UNBOUNDED-DYNAMICS + RELATIVE-SPECTRAL-RIGIDITY + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-089` proves that a fixed **finite-dimensional** auxiliary/global sector cannot evade the common-multiple repetition of `WP-088` when its coupling is coherent under normalized cell refinement: all nontrivial interaction is confined to one fixed collective block. It deliberately leaves open infinite auxiliary sectors and unbounded global dynamics.

The finite-dimensional hypothesis is not load-bearing. If the auxiliary Hilbert space and its operator are fixed while the coupling obeys the same normalized refinement law, the exact one-collective-block decomposition survives for an **arbitrary Hilbert auxiliary sector**, even when its self-adjoint dynamics is unbounded and has continuous spectrum. More strongly, after subtracting the decoupled finite-plus-global operator, the coupled/decoupled pair differs only in one fixed finite-rank collective channel. Every standard relative resolvent trace, perturbation determinant, or spectral-shift response is therefore independent of the tower parameter.

Thus simply replacing the finite global block in `WP-089` by an infinite-dimensional or unbounded archimedean operator does not create a new scale. A surviving infinite/global route must make the auxiliary sector itself transform with refinement, use a noncoherent or domain-changing coupling, alter the repeated finite block through a genuinely global boundary condition, or leave this fixed bounded-coupling framework.

## 1. Refinement coherence does not depend on the dimension of the auxiliary sector

Retain the exact common-multiple normal form from `WP-088`--`WP-089`. Let

\[
H=E_L,
\qquad
F_k=I_k\otimes A+J_k\otimes\Delta,
\tag{1}
\]

where `H` is the fixed finite-dimensional `L`-cell space, `A,Delta` are fixed bounded self-adjoint operators on `H`,

\[
e_k=\frac1{\sqrt k}(1,\ldots,1),
\qquad
J_k=|e_k\rangle\langle e_k|.
\tag{2}
\]

Let `K` now be an **arbitrary Hilbert space**, with no finite-dimensionality or separability assumption, and let

\[
C_k:K\longrightarrow \mathbb C^k\otimes H
\tag{3}
\]

be bounded couplings. For positive integers `k,l`, let `R_{k,l}` be the normalized repeated-cell isometry of `WP-089`, characterized by

\[
R_{k,l}(e_i\otimes v)
=\frac1{\sqrt l}
\sum_{a=1}^l e_{(i,a)}\otimes v.
\tag{4}
\]

Assume the same refinement coherence,

\[
\boxed{C_{kl}=R_{k,l}C_k.}
\tag{5}
\]

Taking `k=1` already determines the whole family. Put `B=C_1:K\to H`. Since

\[
R_{1,k}v=e_k\otimes v,
\]

we obtain exactly

\[
\boxed{C_k=e_k\otimes B.}
\tag{6}
\]

No compactness, trace-class property, or finite dimension of `K` enters this argument. Coherence alone forces every auxiliary state to couple only through the normalized collective copy of `H`; all `k-1` zero-sum repeated-cell directions remain invisible to the global sector.

## 2. Unbounded fixed global dynamics still gives the same direct-sum decomposition

Let `D` be any fixed self-adjoint operator on `K`, possibly unbounded. Define

\[
Q_k=
\begin{pmatrix}
F_k&C_k\\
C_k^*&D
\end{pmatrix}
\tag{7}
\]

on

\[
\operatorname{Dom}Q_k
=(\mathbb C^k\otimes H)\oplus\operatorname{Dom}D.
\tag{8}
\]

Because `C_k` is bounded, the off-diagonal matrix is a bounded self-adjoint perturbation of `F_k\oplus D`; hence `Q_k` is self-adjoint on (8).

Now decompose

\[
\mathbb C^k=e_k^\perp\oplus\mathbb Ce_k.
\tag{9}
\]

On `e_k^perp tensor H`, both `J_k tensor Delta` and `C_k` vanish. On the collective line, `F_k` becomes `A+Delta` and `C_k` becomes `B`. Therefore

\[
\boxed{
Q_k\cong
A^{\oplus(k-1)}
\oplus
Q_{\rm coll},
}
\tag{10}
\]

where the possibly infinite-dimensional self-adjoint operator

\[
\boxed{
Q_{\rm coll}
=
\begin{pmatrix}
A+\Delta&B\\
B^*&D
\end{pmatrix}
}
\tag{11}
\]

acts on `H oplus K` with domain `H oplus Dom(D)` and is completely independent of `k`.

This is the exact infinite-sector analogue of `WP-089`. Infinite multiplicity or continuous spectrum may occur inside `D` and `Q_coll`, but no part of that spectrum is made to move by increasing the number of repeated `L`-cells.

## 3. The relative global correction is finite rank and exactly degree-flat

For an infinite auxiliary sector, absolute traces or determinants may not exist, so the correct discriminator is the **relative** coupled-versus-decoupled response. Define

\[
Q_k^{(0)}:=F_k\oplus D.
\tag{12}
\]

The same decomposition gives

\[
Q_k^{(0)}
\cong
A^{\oplus(k-1)}
\oplus
Q_{\rm coll}^{(0)},
\qquad
Q_{\rm coll}^{(0)}=(A+\Delta)\oplus D.
\tag{13}
\]

Consequently the pair `(Q_k,Q_k^(0))` is the orthogonal sum of `k-1` identical **zero perturbation pairs** `(A,A)` and the single fixed pair `(Q_coll,Q_coll^(0))`.

There is a useful strengthening. Since `H` is finite dimensional,

\[
Q_{\rm coll}-Q_{\rm coll}^{(0)}
=
\begin{pmatrix}
0&B\\
B^*&0
\end{pmatrix}
\tag{14}
\]

has rank at most `2 dim H`, regardless of the dimension or spectrum of `K`. Hence, for every nonreal `z`, the resolvent difference is trace class. Under the unitary decomposition (10)--(13),

\[
\boxed{
(Q_k-z)^{-1}-(Q_k^{(0)}-z)^{-1}
\cong
0^{\oplus(k-1)}
\oplus
\bigl((Q_{\rm coll}-z)^{-1}-(Q_{\rm coll}^{(0)}-z)^{-1}\bigr).
}
\tag{15}
\]

Therefore

\[
\boxed{
\operatorname{Tr}\!\left((Q_k-z)^{-1}-(Q_k^{(0)}-z)^{-1}\right)
\text{ is independent of }k.
}
\tag{16}
\]

The same direct-sum identity makes every standard relative invariant stable under adjoining identical summands degree-flat. In particular, whenever written in its usual finite-rank/trace-class normalization, the perturbation determinant of `(Q_k,Q_k^(0))` is exactly that of the fixed collective pair, and the corresponding Krein spectral-shift function is the fixed collective spectral shift. No regularization of the infinite spectator spectrum is needed to obtain this conclusion: the repeated bulk cancels before scalarization.

Thus the infinite auxiliary sector does not merely fail to add a new extensive term. Its entire **interaction anomaly relative to the decoupled finite-plus-global system is constant on the common-multiple tower**.

## 4. Independent positivity also reduces to fixed blocks

Equation (10) gives the sign theorem without any spectral scalarization. For the whole tower,

\[
\boxed{
Q_k\succeq0\text{ for every }k\ge1
\iff
A\succeq0\text{ and }Q_{\rm coll}\succeq0.
}
\tag{17}
\]

The reverse implication is immediate from the direct sum. For the forward implication, any `k>=2` exposes the bulk block `A`, while `k=1` exposes `Q_coll`.

So an infinite archimedean/global operator can participate in a genuine independent positivity theorem. What refinement coherence prevents is using that participation to generate a new common-multiple scale: positivity is decided by two fixed operators, while the only `k`-dependence outside them is repetition of `A`.

This distinction matters. A fixed `D` may contain a nontrivial standalone archimedean spectral profile in its own spectral/test variable; `WP-092` does **not** say otherwise. It says that attaching such a fixed profile through the coherent bounded coupling (5) leaves the finite--global interaction spectrally degree-flat. The archimedean sector is therefore still a fixed appended component rather than a source of new tower dependence forced by the interaction.

## 5. Consequence for the pointed-cover Weil route

`WP-088` shows that fixed bounded finite-reference projection constructions have only affine additive spectral responses on `n=kL`. `WP-089` then shows that a fixed finite-dimensional coherent global sector cannot create the missing moving scale. The present result removes **infinite auxiliary dimension and unbounded fixed self-adjoint dynamics** as loopholes in that same coherent-coupling mechanism.

If a finite projection carrier lacks the required logarithmic degree law, then replacing its auxiliary block by an infinite-dimensional `D` does not repair it under (5): every relative coupling response remains constant in `k`, while the finite bulk remains the same repeated `A` block. Conversely, if another finite carrier already supplies the correct `log n`, a fixed infinite `D` may coexist with it, but (15)--(16) show that the coherent interaction itself contributes no new degree law. Any claim that the interaction explains the joint finite--archimedean structure must therefore come from mathematics outside this fixed repeated-cell model.

This is especially relevant to the canonical research mandate. Merely placing a Gamma-like operator next to an exact finite carrier is a separated assembly. To obtain a genuinely new same-structure mechanism from this cover geometry, the global sector must change how refinement acts, how domains/boundaries are identified, or how the finite repeated cells couple before the collective/bulk split becomes exact.

## 6. Matched control

Nothing in (1)--(17) uses primes, `zeta`, the functional equation, zero data, or RH. The argument applies verbatim to any repeated finite-cell Hilbert module with

\[
F_k=I_k\otimes A+J_k\otimes\Delta
\]

and the normalized repetition maps (4). An arbitrary fixed infinite bath, boundary Hilbert space, or continuous-spectrum operator coupled coherently through that repetition still sees only the collective vector.

The obstruction is therefore geometric/representation-theoretic, not arithmetic evidence. The arithmetic relevance comes only from the fact that the pointed-cover system reaches exactly this repeated-cell normal form on every common-multiple tower.

## 7. Sharp scope boundary

The hypotheses are deliberately narrow enough to identify the real escape routes.

The theorem does **not** close:

1. **Auxiliary refinement dynamics.** If the global spaces or operators form a nontrivial family `K_k,D_k`, or if refinement carries its own maps `U_{k,l}` rather than leaving `K` fixed, the reduction to `C_k=e_k tensor B` need not hold in this form. Such a family can carry a genuine scale.
2. **Unbounded or domain-changing couplings.** A closable coupling whose domain changes with `k` can evade the bounded-perturbation argument and may create boundary anomalies. Its positivity and self-adjointness would require a separate theorem.
3. **Noncoherent cross-cell coupling.** As `WP-089` already shows, a moving collective principal angle can produce exact `log k`; the issue is deriving that motion intrinsically rather than inserting it.
4. **Global boundary conditions that change the finite block itself.** If coupling to the global sector changes `A` or `Delta` with `k`, the exact repeated-bulk decomposition (1) has been left behind.
5. **A genuinely nonseparable object formed before the common-multiple cell decomposition.** The theorem begins after the finite pointed-cover algebra has acquired the `I_k/J_k` normal form.
6. **Nonrelative absolute regularizations.** One can impose a `k`-dependent subtraction or determinant normalization on an infinite `D`, but that degree dependence is additional data and is not inherited from (5).

The first two escapes are the genuinely new infinite-sector possibilities. Infinite dimension or unbounded spectrum **by themselves** are not.

## 8. Prior-art and novelty audit

All abstract ingredients are classical. Decomposition into the constant and zero-sum permutation subspaces, bounded perturbations of self-adjoint operators, finite-rank resolvent differences, perturbation determinants, and Krein spectral-shift theory are standard operator theory. A directed literature check of block-operator matrices, repeated/permutation-invariant couplings, finite-rank perturbations, and spectral-shift trace formulae found standard machinery rather than a new general theorem; classical Krein theory already treats self-adjoint pairs with trace-class operator or resolvent difference.

No theorem-level novelty is claimed for any of that machinery. The durable Mathia-specific content is the exact compatibility of three previously established structures:

- the common-multiple repeated-cell normal form of `WP-088`;
- the normalized refinement coherence isolated in `WP-089`;
- the fact that the collective finite cell `H` remains finite dimensional even when the attached global sector is infinite.

Together they show that the explicit **infinite auxiliary-sector escape left open by `WP-089` does not survive if the infinite sector is fixed and coherently coupled**. The obstruction is a classification result inside this Mathia-native cover model, not a new spectral-shift theorem and not a reformulation of Weil positivity.

## 9. Exact falsification surface

The finding can be falsified under its stated hypotheses by any of the following:

1. exhibit a coherent bounded family (5) with fixed `K` for which `C_k` is not `e_k tensor C_1`;
2. exhibit fixed self-adjoint `D` and bounded `B` for which the block family (7) does not reduce as in (10);
3. find a nonreal `z` for which the relative resolvent difference in (15) acquires nontrivial `k`-dependence;
4. find a standard relative invariant stable under orthogonal direct sum with identical pairs whose value nevertheless changes with the number of zero perturbation summands;
5. produce a positive family satisfying all hypotheses for which the sign criterion (17) fails.

A construction with `K_k`, `D_k`, auxiliary refinement maps, unbounded/domain-changing couplings, noncoherent moving angles, or modified finite blocks does not falsify the theorem; it lies outside the fixed coherent category being closed.

## Research consequence

The fixed coherent pointed-cover completion now has a dimension-free rigidity boundary:

\[
\boxed{
\text{fixed finite repeated cells}
+\text{fixed arbitrary Hilbert global sector}
+\text{bounded normalized-refinement coupling}
\Longrightarrow
\text{one fixed collective interaction block}.
}
\]

Even a global sector with infinitely many modes or unbounded self-adjoint dynamics cannot generate a moving finite--global spectral scale under these hypotheses. The live boundary is therefore no longer “make the auxiliary sector infinite.” It is **make refinement act nontrivially on the global sector, change the coupling/domain with scale, or alter the finite/global geometry before periodic repetition freezes it**. Any such survivor still has to produce the exact finite and archimedean Weil structure and prove the final sign independently of RH or inserted zero data.