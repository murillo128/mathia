# WP-089 — Cover-coherent finite global couplings freeze to one collective block

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + FINITE-GLOBAL-COUPLING + COHERENCE-GATED + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-088` proves that, on a common-multiple tower `n=kL`, every fixed bounded construction from finitely many pointed-cover projections has only one collective target mode plus `k-1` repeated bulk modes. It therefore makes every fixed additive spectral readout affine in `k`, but deliberately leaves open a genuinely nonseparable finite--archimedean escape: couple the repeated finite block to a fixed auxiliary/global sector **before** scalarization, allowing the coupling itself to move spectral data.

There is an exact obstruction for the canonical refinement-coherent version of that escape.

Let `H=E_L` be the fixed `L`-cell space. Every self-adjoint finite-only family covered by `WP-088` can be written

\[
F_k=I_k\otimes A+J_k\otimes\Delta,
\qquad
J_k=|e_k\rangle\langle e_k|,
\qquad
e_k=\frac1{\sqrt k}(1,\ldots,1),
\tag{1}
\]

for fixed self-adjoint operators `A,Delta` on `H`. Let `K` be any fixed finite-dimensional auxiliary sector with fixed self-adjoint operator `D`, and let

\[
C_k:K\longrightarrow \mathbb C^k\otimes H
\tag{2}
\]

be the finite--global coupling. If the coupling is coherent under normalized repetition of common-multiple cells, then necessarily

\[
\boxed{C_k=e_k\otimes B}
\tag{3}
\]

for one fixed `B:K->H`. The full coupled operator

\[
Q_k=
\begin{pmatrix}
F_k&C_k\\
C_k^*&D
\end{pmatrix}
\tag{4}
\]

then has the exact decomposition

\[
\boxed{
Q_k\cong
A^{\oplus(k-1)}
\oplus
\begin{pmatrix}
A+\Delta&B\\
B^*&D
\end{pmatrix}.
}
\tag{5}
\]

Thus the auxiliary sector changes **one fixed collective block only**. Every fixed additive spectral scalarization remains affine in `k`, while its difference from the finite-only readout is actually independent of `k`. Positivity can hold independently, but it is equally scale-free: `Q_k>=0` for all `k` exactly when the fixed bulk block and fixed collective block are positive.

A complementary positivity bound shows that the other obvious normalization also fails. If one repeats a nonzero coupling with fixed local strength,

\[
C_k=\mathbf1_k\otimes B,
\tag{6}
\]

then its collective strength is `sqrt(k)B`. Positivity of (4) for arbitrarily large `k` forces `B=0`. More generally, for `C_k=c_k\mathbf1_k\otimes B` with fixed nonzero `B`, positivity forces

\[
|c_k|=O(k^{-1/2}).
\tag{7}
\]

The normalized `k^{-1/2}` law is exactly the refinement-coherent law (3), and that law freezes the collective spectrum instead of producing `log k`.

This is not a no-go for **arbitrary** degree-dependent finite--global coupling. The scope boundary is sharp. If coherence is dropped, the positive two-dimensional collective block

\[
\begin{pmatrix}
1&\sqrt{1-1/k}\\
\sqrt{1-1/k}&1
\end{pmatrix}
\succeq0
\tag{8}
\]

has determinant `1/k` and therefore

\[
-\log\det=\log k.
\tag{9}
\]

So a moving principal angle can create exact logarithmic degree while preserving positivity. This is the same mechanism class exposed intrinsically but reference-relatively by `WP-085`; it is precisely what refinement coherence forbids. A surviving global route must therefore explain, from new Mathia geometry rather than an inserted degree-dependent coefficient, why the auxiliary/global sector develops such a moving angle or another nonperiodic scale.

The result closes only **fixed finite auxiliary sectors with common-multiple refinement coherence**, not infinite auxiliary sectors, unbounded scale operators, noncoherent/global cross-cell couplings, or nonadditive invariants. It is nevertheless substantive because it converts an explicit escape left open by `WP-088` into a dichotomy: local-strength repetition is incompatible with positivity, while isometric coherent repetition is compatible with positivity but spectrally degree-flat apart from repeated multiplicity.

## 1. WP-088 already has the collective/bulk normal form

Fix a finite reference dictionary

\[
M=\{m_1,\ldots,m_r\},
\qquad
L=\operatorname{lcm}(m_1,\ldots,m_r),
\]

and the target tower `n=kL`. On the target cell,

\[
E_{kL}\cong\mathbb C^k\otimes E_L.
\tag{10}
\]

`WP-088` proves

\[
P_m^{(kL)}=I_k\otimes P_m^{(L)}
\qquad(m\mid L),
\]

and

\[
P_{kL}^{(kL)}=J_k\otimes J_L.
\tag{11}
\]

For any fixed self-adjoint bounded expression in these projections, its action on the `L`-cell constant line and its orthogonal complement gives exactly a fixed bulk operator plus one collective correction. Equivalently there are fixed self-adjoint `A,Delta in B(H)` such that (1) holds.

The decomposition

\[
\mathbb C^k=e_k^\perp\oplus\mathbb Ce_k
\tag{12}
\]

then gives

\[
\boxed{
F_k\cong A^{\oplus(k-1)}\oplus(A+\Delta).
}
\tag{13}
\]

This rewrites the affine-spectrum theorem of `WP-088` in the form needed to test a finite global coupling.

## 2. Normalized cell repetition forces the auxiliary coupling into the collective line

The exact common-multiple decomposition has a canonical normalized repetition map. For positive integers `k,l`, define

\[
R_{k,l}:\mathbb C^k\otimes H
\longrightarrow
\mathbb C^{kl}\otimes H
\tag{14}
\]

on the repeated-cell basis by

\[
R_{k,l}(e_i\otimes v)
=
\frac1{\sqrt l}
\sum_{a=1}^l e_{(i,a)}\otimes v.
\tag{15}
\]

This is an isometry and satisfies the exact refinement law

\[
R_{kl,m}R_{k,l}=R_{k,lm}.
\tag{16}
\]

It is the normalized replication isometry of the **common-multiple cell module**. No claim is made that it is an additional arithmetic operator already supplied by the original Hardy semigroup; it is simply the canonical isometric identification obtained by repeating each `L`-cell `l` times.

Call a fixed auxiliary coupling family refinement-coherent when

\[
\boxed{
C_{kl}=R_{k,l}C_k
\qquad(k,l\ge1).
}
\tag{17}
\]

Taking `k=1` determines the entire family. Put `B=C_1:K->H`. Since

\[
R_{1,k}v=e_k\otimes v,
\tag{18}
\]

we obtain exactly

\[
\boxed{
C_k=e_k\otimes B.
}
\tag{19}
\]

Thus a coherent fixed auxiliary sector can couple only to the normalized collective copy of `H`; it has zero matrix element against every zero-sum cell direction in `e_k^perp`.

This is the key point. The finite reference algebra already treats the `k-1` zero-sum cell directions as identical bulk copies, and refinement coherence prevents the auxiliary sector from distinguishing them one by one.

## 3. The full coupled spectrum is one fixed block plus repeated bulk

Insert (19) into the block family (4). Under

\[
(\mathbb C^k\otimes H)\oplus K
=
(e_k^\perp\otimes H)
\oplus
((\mathbb Ce_k\otimes H)\oplus K),
\tag{20}
\]

the first summand does not see `J_k` or `C_k`, while the second identifies canonically with `H\oplus K`. Hence

\[
Q_k\cong
A^{\oplus(k-1)}\oplus Q_{\rm coll},
\tag{21}
\]

where

\[
\boxed{
Q_{\rm coll}
=
\begin{pmatrix}
A+\Delta&B\\
B^*&D
\end{pmatrix}
}
\tag{22}
\]

is independent of `k`.

Let `f` be any fixed scalar function defined on the relevant finite spectra. Whenever the trace exists,

\[
\boxed{
\operatorname{Tr}f(Q_k)
=(k-1)\operatorname{Tr}f(A)
+\operatorname{Tr}f(Q_{\rm coll}).
}
\tag{23}
\]

This includes ordinary trace powers, fixed positive spectral energies, Schatten-power traces in the positive case, and reduced log-determinant/pseudolog readouts with a fixed convention for zero modes.

For the finite-only family (13),

\[
\operatorname{Tr}f(F_k)
=(k-1)\operatorname{Tr}f(A)
+\operatorname{Tr}f(A+\Delta).
\tag{24}
\]

Subtracting gives the stronger exact identity

\[
\boxed{
\operatorname{Tr}f(Q_k)-\operatorname{Tr}f(F_k)
=
\operatorname{Tr}f(Q_{\rm coll})
-\operatorname{Tr}f(A+\Delta),
}
\tag{25}
\]

which is independent of `k`. A coherent finite auxiliary sector therefore supplies a fixed spectral anomaly, not an archimedean/global counterterm with new logarithmic tower dependence.

Since exact Möbius primitive `Lambda` requires a preprimitive `G(1)+log n`, the same three-scale obstruction as in `WP-088` remains: an affine response on `kL` cannot equal `log(kL)` for all `k`.

## 4. Independent positivity survives, but it does not generate scale

Equation (21) also makes the sign theorem exact. For the entire tower,

\[
\boxed{
Q_k\succeq0\text{ for all }k\ge1
\iff
A\succeq0\text{ and }Q_{\rm coll}\succeq0.
}
\tag{26}
\]

The forward implication uses any `k>=2` to see the bulk block `A`; the reverse implication is immediate from the direct sum.

Thus a genuinely geometric theorem may well make the coupled object positive. What it cannot do under (17) is create the missing arithmetic scale: positivity is decided by two fixed operators, and all `k`-dependence is only the multiplicity of `A`.

This is stronger than saying a fixed-dimensional sector gives only a finite-rank perturbation. The auxiliary block can couple nontrivially and can change its collective eigenvalues by an order-one amount; the exact point is that coherence confines all of that change to a **fixed** collective block.

## 5. Fixed local coupling strength is incompatible with positivity across the tower

One might reject normalized coherence and instead ask that the same local coupling be attached to every repeated `L`-cell with unchanged strength. That means

\[
C_k=\mathbf1_k\otimes B
=\sqrt k\,e_k\otimes B.
\tag{27}
\]

The collective block becomes

\[
Q_{\rm coll}(k)
=
\begin{pmatrix}
A+\Delta&\sqrt k\,B\\
\sqrt k\,B^*&D
\end{pmatrix}.
\tag{28}
\]

Assume (28) is positive semidefinite for arbitrarily large `k`. For arbitrary `x in H` and `y in K`, positivity of the compressed `2 x 2` scalar matrix gives

\[
\boxed{
k|\langle By,x\rangle|^2
\le
\langle(A+\Delta)x,x\rangle
\langle Dy,y\rangle.
}
\tag{29}
\]

The right-hand side is independent of `k`. Letting `k` grow forces every matrix coefficient of `B` to vanish, hence

\[
\boxed{B=0.}
\tag{30}
\]

No invertibility or Schur-complement hypothesis is needed.

More generally, if

\[
C_k=c_k\mathbf1_k\otimes B
\tag{31}
\]

with one fixed nonzero `B`, the same argument gives

\[
\boxed{|c_k|=O(k^{-1/2})}
\tag{32}
\]

along every unbounded positive tower. On the other hand, the refinement law (17) gives

\[
c_{kl}=\frac{c_k}{\sqrt l},
\]

and therefore

\[
\boxed{c_k=\frac{c_1}{\sqrt k}.}
\tag{33}
\]

So the canonical isometric normalization sits exactly at the positivity-compatible scale. But after multiplying by `\mathbf1_k`, (33) makes the collective coupling constant, which is why the spectrum freezes as in (21).

This yields the local-to-global dichotomy

\[
\boxed{
\begin{array}{ccl}
\text{fixed local strength}&\Longrightarrow&\text{positivity forces decoupling},\\[2mm]
\text{isometric refinement strength}&\Longrightarrow&\text{positive coupling survives but is degree-flat}.
\end{array}}
\tag{34}
\]

## 6. Sharp boundary: a moving principal angle can manufacture exact `log k`

The coherence hypothesis is load-bearing and cannot be removed.

Take `H=K=C`, let the bulk and auxiliary diagonal entries both be `1`, and define a degree-dependent collective coupling

\[
t_k=\sqrt{1-\frac1k}.
\tag{35}
\]

Then

\[
Q_{\rm move}(k)
=
\begin{pmatrix}
1&t_k\\
t_k&1
\end{pmatrix}
\tag{36}
\]

has eigenvalues `1+-t_k`, both nonnegative, and

\[
\det Q_{\rm move}(k)=1-t_k^2=\frac1k.
\tag{37}
\]

Therefore

\[
\boxed{-\log\det Q_{\rm move}(k)=\log k.}
\tag{38}
\]

Embedding this as the collective sector alongside `k-1` unit bulk copies leaves the same determinant. A fixed one-dimensional auxiliary space is therefore enough to generate logarithmic scale **if its angle with the collective finite mode is allowed to move with `k`**.

This is not a global Weil construction. The coefficient (35) was chosen only to expose the exact scope boundary, and no Gamma or polar term is present. But the mechanism is not artificial in kind: `WP-085` already finds an intrinsic pointed-cover principal angle whose positive defect has eigenvalue `1/n` on the appropriate nonnested degrees. The lesson is therefore not that moving angles should be rejected, but that a surviving finite--global route must derive their motion from a Mathia-native global geometry rather than from fixed periodic repetition.

In particular, `WP-089` must **not** be read as saying that every fixed-dimensional archimedean sector is harmless. `WP-088` correctly left arbitrary noncoherent coupling open, and (36)--(38) show why.

## 7. Matched controls and relation to nearby findings

Nothing in the proof uses primality, zeta, zero data, the functional equation, or the distribution of rational primes. The same result holds for an all-integer consecutive-block cover system with the same repeated-cell geometry. It is therefore a structural theorem about coherent finite coupling to the `WP-088` periodic projection module.

The result is distinct from the nearby negative routes:

- `WP-019` and `WP-020` concern supersymmetric/Hodge supertrace cancellation and index collapse, not repeated-cell coupling.
- `WP-026` concerns passive `M`-matrix/Kron elimination and the sign of finite Weil self-energy; no passivity assumption is used here.
- `WP-035` shows that a fixed-dimensional correction cannot repair the unbounded positive inertia of the Prime-Circle boundary form. Here the finite block may already be positive; the obstruction is lack of new scale under refinement coherence.
- `WP-045`--`WP-047` concern radial Schur elimination and divergent self-energy, again with different finite data.
- `WP-069` gives a dimension-free Cauchy--Schwarz obstruction to representing a specific unbounded Hardy Mangoldt anchor by a finite-energy auxiliary state. The present theorem instead concerns additive spectra of the finite cover-projection algebra and remains meaningful even when no Mangoldt anchor functional has yet been formed.
- `WP-085` is the sharp positive control: a moving noncommuting principal angle can produce a logarithm. `WP-088` then freezes every fixed finite reference dictionary on its common-multiple tower; the present result shows that a **coherent fixed auxiliary sector** also freezes rather than reintroducing that angle motion.

Thus the new information is not generic block-matrix theory but the exact interaction among three Mathia-native facts: common-multiple repetition, the one-collective-mode normal form, and refinement-compatible coupling.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed for decomposing the permutation module into its constant and zero-sum subspaces, for positivity of `2 x 2` compressions, or for spectral decomposition of block/arrowhead matrices. These are classical finite-dimensional linear algebra and representation-theoretic facts. Modern arrowhead/diagonal-plus-rank-one spectral literature, for example Barlow--Eisenstat--Jakovcevic Stor--Slapnicar, *Deflation for the Symmetric Arrowhead and Diagonal-Plus-Rank-One Eigenvalue Problems*, SIAM Journal on Matrix Analysis and Applications **43** (2022), 681--709, DOI `10.1137/21M139205X`, lies well inside that classicalized boundary.

A directed audit for permutation-invariant/repeated-block couplings, positive block matrices, rank-one/arrowhead perturbations, and invariant finite-dimensional auxiliary sectors found standard machinery but no external theorem needed for (17)--(34). The claim here is only a **Mathia-specific derived obstruction**: once the exact pointed-cover common-multiple algebra of `WP-088` is required to couple to a fixed auxiliary sector through its normalized repeated-cell refinement, all nontrivial global interaction is forced into one fixed collective block.

The sharp counterexample (36) is intentionally retained to prevent overclaiming. It also aligns the novelty boundary with `WP-085`: principal-angle logarithms are already present in the repository and belong to classical projection geometry. What remains potentially new would be a Mathia-intrinsic reason for a global finite--archimedean object to force the required moving angle **and** the full Weil finite/archimedean/polar decomposition with an independent sign theorem.

## 9. Exact falsification surface

The finding is falsified if any of the following fails under its stated hypotheses:

1. the `WP-088` common-multiple family cannot be written as `F_k=I_k tensor A+J_k tensor Delta` with fixed `A,Delta`;
2. the normalized repetition maps (15) fail the isometry or composition law (16);
3. coherence (17) does not imply `C_k=e_k tensor B` from `k=1`;
4. the coupled family then fails to decompose as (21);
5. a fixed additive spectral readout of (21) can have non-affine `k`-dependence;
6. the relative readout (25) can depend on `k`;
7. positivity of (28) for arbitrarily large `k` can hold with fixed nonzero `B`;
8. for a nonzero fixed `B`, positivity of `c_k 1_k tensor B` does not force `c_k=O(k^-1/2)`;
9. the counterexample (36) is not positive semidefinite or does not satisfy `-log det=log k`.

Items 1--4 are exact tensor identities, items 5--6 follow from direct-sum multiplicity, items 7--8 from the scalar `2 x 2` PSD determinant bound, and item 9 is an elementary exact calculation. No numerical evidence is load-bearing.

## Research consequence

The finite--global escape left open by `WP-088` now has a sharper target.

A **fixed finite auxiliary sector is not enough merely by being nonseparably coupled before scalarization**. If that coupling respects the canonical isometric repetition of common-multiple cells, its entire effect is one `k`-independent collective block. If instead the same local coupling is repeated without normalization, positivity itself drives the coupling to zero.

The viable finite-dimensional survivor is therefore much narrower and more concrete: a Mathia-native global/boundary structure must force a **noncoherent moving collective angle or comparable nonperiodic scale** before additive spectral scalarization. Equation (36) shows that such motion can in principle coexist with positivity and produce exactly `log k`; `WP-085` shows that Mathia cover geometry can generate the same type of singular principal-angle scale locally, but only reference-relatively. The next decisive question is whether any intrinsic global completion can generate that motion without choosing a reference, importing `log n`, or re-encoding known Weil/zero data, and simultaneously supply the archimedean and polar terms with an independent positivity theorem.