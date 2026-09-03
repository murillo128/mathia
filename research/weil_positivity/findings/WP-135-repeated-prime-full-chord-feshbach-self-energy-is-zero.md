# WP-135 — Repeated-prime full-chord Feshbach self-energy is exactly zero

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + POSITIVE-FORM + MATCHED-CONTROL + COMPUTATION-CHECKED + PRIOR-ART-CLASSICALIZATION` for the canonical coarse/fiber decomposition of the normalized full primitive-shell inverse-square chord energy under refinements that add no new prime support.

`WP-134` proved that the fiber-constant compression of the normalized full-chord energy is stationary under repeated-prime refinement, but deliberately left open a possible escape: perhaps the discarded zero-mean fiber modes couple back to the coarse modes, so that a Schur/Feshbach elimination or positive boundary response acquires a nontrivial repeated-prime self-energy. `PC-156` now gives the missing full-fiber classification. It closes that escape exactly.

Let

\[
A_N:=N^{-2}L_N^{\rm int}
\]

be the normalized full inverse-square primitive-shell Laplacian of `WP-134`/`PC-155`. Let `d,m>=1` satisfy

\[
\operatorname{rad}(m)\mid\operatorname{rad}(d),
\tag{1}
\]

so that passing from `d` to `dm` only deepens primes already present at the coarse level. Write

\[
J:\ell^2(U(d))\longrightarrow \ell^2(U(dm))
\]

for the normalized pullback to functions constant on each reduction fiber, and put

\[
P:=JJ^*,\qquad Q:=I-P.
\tag{2}
\]

Then the fiber-constant space is not merely a subspace on which the compressed energy agrees with `A_d`: it is an exact **reducing subspace** of the complete fine operator. Equivalently,

\[
\boxed{
A_{dm}J=JA_d,
\qquad
QA_{dm}P=PA_{dm}Q=0.
}
\tag{3}
\]

Consequently every Schur/Feshbach elimination of the complete zero-mean fiber sector has **zero self-energy**. Whenever the fine block appearing in the resolvent is invertible,

\[
\boxed{
P(A_{dm}-z)P
-
PA_{dm}Q\,[Q(A_{dm}-z)Q]^{-1}QA_{dm}P
=
J(A_d-z)J^*.
}
\tag{4}
\]

At `z=0`, in every nontrivial refinement, the `Q` block is positive definite because the full weighted complete-graph Laplacian has only the global constant vector in its kernel, and that vector lies in `P`. Hence the ordinary energy-minimizing Schur complement is also exact:

\[
\boxed{
\inf_{\eta\in Q\ell^2(U(dm))}
\langle Jf+\eta,A_{dm}(Jf+\eta)\rangle
=
\langle f,A_df\rangle.
}
\tag{5}
\]

There is therefore no hidden positive coarse--fine response from which the repeated Mangoldt tower can emerge. The zero coupling is stronger than the stationarity of `WP-134`: it says that allowing the full fine fiber and then eliminating it does not alter the coarse positive form at all.

## 1. `PC-156` makes the coarse space reducing, not merely stationary after compression

Under (1), every unit modulo `d` has a complete cyclic `m`-fiber modulo `dm`, and `PC-156` proves the exact fiber Fourier decomposition

\[
A_{dm}
\cong
\bigoplus_{k=0}^{m-1}
D_{m,k}\,\mathcal P_d(k/m)\,D_{m,k}^{-1},
\tag{6}
\]

with

\[
\mathcal P_d(t)
=
\frac1{d^2}
\left(
L_d^{\rm int}
+\frac t2 C_d
-\frac{t^2}{2}I
\right).
\tag{7}
\]

The fiber-constant space is exactly the Fourier sector `k=0`. Since `D_{m,0}=I` and

\[
\mathcal P_d(0)=A_d,
\tag{8}
\]

the complete fine operator is block diagonal with respect to

\[
\operatorname{im}J\oplus(\operatorname{im}J)^\perp.
\tag{9}
\]

This proves (3). In particular, the possible coarse/detail coupling explicitly left open in Section 6 of `WP-134` is not present in this canonical repeated-prime full-chord geometry.

The distinction matters. Compression alone only states `J^*A_{dm}J=A_d`; a generic positive matrix can satisfy such an identity while still having a nonzero off-diagonal block, in which case eliminating the complement changes the effective coarse form. Equation (6) supplies the stronger symmetry statement needed to exclude that possibility here.

## 2. Feshbach, Schur, and variational responses all collapse to the coarse operator

In the decomposition (9), write

\[
A_{dm}
=
\begin{pmatrix}
JA_dJ^*&0\\
0&A_Q
\end{pmatrix}.
\tag{10}
\]

The usual Schur/Feshbach correction is quadratic in the off-diagonal block. Since that block is exactly zero, the correction vanishes identically at every spectral parameter for which the expression is defined. This gives (4) without approximation or limiting argument.

The same statement has a purely positive variational form that does not require an inverse. Since `A_{dm}\succeq0`,

\[
\begin{aligned}
\langle Jf+\eta,A_{dm}(Jf+\eta)\rangle
&=\langle f,A_df\rangle+\langle\eta,A_Q\eta\rangle\\
&\ge \langle f,A_df\rangle,
\end{aligned}
\tag{11}
\]

and equality is attained at `eta=0`. Thus even if one defines the effective response as the minimum fine energy compatible with prescribed coarse data, the answer is exactly the pre-existing coarse energy and is independent of the repeated-prime depth.

This is the relevant positivity statement: nonnegativity follows from the intrinsic chord Laplacian itself, not from RH, zero data, or a Weil kernel. Its arithmetic output is nevertheless trivial in the repeated-prime direction.

## 3. Fixed positive spectral functional calculus cannot rescue the coarse channel

Reducing-subspace invariance also propagates through functional calculus. For every fixed continuous function `Phi` on the finite spectrum (and, equivalently here, every polynomial or Borel spectral function),

\[
\boxed{
J^*\Phi(A_{dm})J=\Phi(A_d).
}
\tag{12}
\]

Therefore the same exact stationarity holds for standard positive spectral constructions such as powers, heat kernels and shifted resolvents:

\[
J^*A_{dm}^rJ=A_d^r,
\qquad
J^*e^{-tA_{dm}}J=e^{-tA_d},
\qquad
J^*(A_{dm}+sI)^{-1}J=(A_d+sI)^{-1}
\tag{13}
\]

for the usual admissible `r,t,s`. If `Phi>=0` on the spectrum, the resulting compressed operator is positive, but it still contains no repeated-depth increment.

This closes another narrow loophole left by `WP-134`: applying a fixed nonlinear **spectral function before the canonical coarse compression** does not help. It does **not** classify nonlinear scalar observables of the entire fine spectrum, such as a full determinant, pseudodeterminant or trace over all fiber sectors; those retain the `k/m` samples of (6) and are a different route.

## 4. Consequence for the repeated Mangoldt tower

The finite side of a Weil explicit formula contains a nonzero event at every prime-power depth,

\[
\Lambda(p^a)=\log p\qquad(a\ge1).
\tag{14}
\]

Suppose `p|d` and take `m=p^r`. Equations (3)--(5) hold for every `r>=1`. Thus neither the coarse energy, nor the self-energy generated by eliminating all fiber fluctuations, nor any fixed positive spectral functional calculus followed by the same coarse compression changes when the `p`-adic depth is increased.

Hence a route of the form

\[
\text{repeated-prime fine chord geometry}
\to
\text{positive coarse/fiber elimination}
\to
\text{new coarse boundary response}
\to
\Lambda(p^a)
\tag{15}
\]

is impossible under the canonical reduction-fiber decomposition. Repeating the unchanged coarse response once for every externally supplied value of `a` would insert the prime-power indexing rather than derive it from geometry.

The statement is actually simultaneous in all already-present primes: any `m` satisfying (1) can deepen several old prime factors at once, yet the same coarse response survives unchanged.

## 5. Matched controls and surviving escapes

The zero self-energy is not a generic property of full-chord refinement. When a genuinely new prime `q\nmid d` is adjoined, the reduction fiber has `q-1` rather than `q` points and the missing residue destroys the full cyclic fiber symmetry. `PC-155` then gives the nontrivial compressed transformation

\[
J_{d,q}^*A_{dq}J_{d,q}
=
\frac{q-2}{q-1}A_d
+
\frac{1}{q^2(q-1)}V_qA_dV_q^{-1}.
\tag{16}
\]

Thus the exact decoupling proved here is specifically a **no-new-prime-support** phenomenon, matching the arithmetic distinction between prime birth and prime-power depth.

Several routes remain outside the theorem. It does not rule out an observable living entirely inside the `k>0` pencil sectors of (6); a scalar trace/determinant/log-determinant of the complete fine operator; a rectangular operator retaining several conductor levels at once; nonlinear interactions inserted between different fiber sectors; the genuinely new-prime fine fibers not classified by `PC-156`; or a finite--archimedean coupling performed before the reduction-fiber symmetry is imposed. Those mechanisms would need their own independent sign theorem and explicit-formula bridge.

A coordinate-subset Kron reduction that does not respect the canonical reduction map is also not covered. Such a choice can manufacture coarse/fine coupling by changing what is called the boundary, but it would need an intrinsic Mathia reason for that noncanonical boundary choice before it could count as evidence for this branch.

## 6. Finite checks

The reducing-subspace claim was independently checked by constructing `A_{dm}` directly and the fiber Fourier isometries for

\[
(d,m)=(6,3),(10,5),(12,4),(18,9).
\tag{17}
\]

In every case the operator norm of the cross block between the fiber-constant sector and every nonzero fiber Fourier sector was at roundoff (`<3e-17`), while the constant-sector compression agreed with `A_d` at the same scale. The smallest eigenvalue of the zero-mean block was positive in all four tests, consistent with the exact complete-graph Laplacian kernel argument. These checks only audit the implementation and normalization; the proof is the exact sector decomposition (6).

## 7. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the abstract linear algebra. Fourier diagonalization of cyclic/block-circulant fibers and the fact that a Schur/Feshbach correction vanishes when the off-diagonal block vanishes are standard. The existing `WP-017` literature audit already places positive Laplacian Schur complements and effective-resistance/Kron-type reductions inside classical persistent-Laplacian machinery. The weighted cotangent/cosecant identities underlying (6) are separately audited in `PC-156` against the classical Dedekind-cotangent distribution literature and modern root-of-unity weighted trigonometric sums.

A bounded literature search found those standard ingredients but no independent claim that the Mathia primitive-unit inverse-square chord refinement has the exact reduction-fiber decomposition (6), nor the resulting repeated-Mangoldt obstruction (15). Absence from that search is not evidence of historical priority. The durable contribution here is the cross-line consequence: `PC-156` closes a specifically identified `WP-134` positivity loophole by showing that the discarded fine modes have exactly zero self-energy on the canonical coarse sector.

This finding also stays on the safe side of the branch's main novelty boundary. It produces no zeta function, zero-defined spectrum, imported Weil positivity functional, arbitrary regularization, or hand-picked kernel. It is a finite exact negative result about a Mathia-native positive energy.

## 8. Falsification boundary and research consequence

The claim is falsified if, under condition (1) and the exact full-chord operator convention of `PC-156`, any nonzero Fourier fiber sector couples to the constant sector, or if the `k=0` block differs from `A_d` after the stated normalization. Either event would make the self-energy term in (4) potentially nonzero. The direct finite tests challenge precisely those points, while `PC-156` proves them generally.

The no-go should not be broadened beyond that scope. In particular, `PC-156` shows that the internal fluctuation sectors are samples of a nontrivial Hermitian quadratic pencil, so the fine space is not empty or spectrally trivial. What fails is their ability to feed back into the canonical coarse positive form under repeated-prime refinement.

For the Weil-positivity program, the repeated-prime full-chord route is therefore narrower than after `WP-134`. A viable construction cannot rely on a hidden Schur/Feshbach correction from old-prime fiber fluctuations. It must either extract a new intrinsic positive structure **inside** the fluctuation pencil, retain multiple levels before reduction, use genuinely new-prime fine fibers, or introduce a justified finite--archimedean/global coupling before the symmetry that makes (3) exact.

## Cross-references

- `research/weil_positivity/findings/WP-134-repeated-prime-full-chord-coarse-compression-is-exactly-stationary.md`
- `research/prime_circle/findings/PC-155-full-chord-primitive-refinement-compression-is-a-commuting-invertible-conjugacy-polynomial.md`
- `research/prime_circle/findings/PC-156-repeated-prime-full-chord-fibers-collapse-to-a-fixed-quadratic-pencil.md`
- `research/weil_positivity/findings/WP-017-prime-lattice-persistent-laplacian-positivity-is-universal.md`