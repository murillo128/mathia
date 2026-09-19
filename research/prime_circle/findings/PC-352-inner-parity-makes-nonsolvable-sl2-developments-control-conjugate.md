# PC-352 — inner parity makes non-solvable SL2 developments matched-control conjugate

- **Finding ID:** `PC-352`
- **Status:** `EXACT-DERIVED`
- **Status detail:** `DECISIVE-NEGATIVE`
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact
- **Prime dependence:** none beyond the source-native cyclotomic radial profile; the obstruction is forced by the calibration/transverse parity and applies shellwise or to any finite transverse shell package
- **RH relevance:** high as a boundary result: replacing the triangular decoder of PC-351 by a genuinely non-solvable `SL_2` development does not by itself create a control-selective spectrum when the reciprocal sign flip is represented by an inner parity involution

## Claim

PC-351 left open a natural repair: keep the faithful centered radial data of PC-350 but develop it in a genuinely non-triangular, non-solvable matrix group before taking spectral or class-function invariants. The smallest obvious target is `SL_2`. That repair still fails for the source-respecting parity class.

The reason is structural. The matched reciprocal control used in PC-351 acts on the centered radial variables by a simultaneous sign flip. If a target representation places the canonical calibration direction in the even part of a `Z/2` grading and the centered shell directions in the odd part, and if that parity automorphism is inner, then the arithmetic development and its matched reciprocal control are conjugate at every cutoff. This remains true after the reciprocity closing factor and in every finite-dimensional representation. Consequently no conjugacy-invariant spectral determinant or zero set can distinguish the cyclotomic source from that control.

The obstruction is not confined to solvable matrices. There are explicit choices whose generated Lie algebra is all of `sl_2(C)`.

## 1. The centered radial connection has an exact control parity

Retain the canonical shell-`2` clock and centered profile from PC-350/PC-351:

\[
X_2(r)=\log(1+r),
\qquad
X_n(r)=\log\Phi_n(r),
\qquad
W_n(r)=X_n(r)-\varphi(n)X_2(r).
\]

For one target shell `n != 2`, let `A,B` be matrices in a target Lie algebra and define the shell-letter substitution

\[
\rho(e_2)=A-\varphi(n)B,
\qquad
\rho(e_n)=B,
\qquad
\rho(e_m)=0\quad(m\notin\{2,n\}).
\]

Because the reciprocity ray is

\[
H=\sum_m\varphi(m)e_m
\]

and `varphi(2)=1`, this gives exactly

\[
\rho(H)=A.
\]

The radial connection therefore becomes

\[
\boxed{
\Omega_n=A\,dX_2+B\,dW_n.
}
\]

The matched reciprocal twin from PC-351 is

\[
\widetilde X_n=2\varphi(n)X_2-X_n,
\]

so its centered profile is

\[
\widetilde W_n=-W_n
\]

while its residue and reciprocal closure are unchanged. Under the same target substitution the control connection is

\[
\boxed{
\widetilde\Omega_n=A\,dX_2-B\,dW_n.
}
\]

The same statement holds for a finite collection of centered shells by replacing `B dW_n` with `sum_j B_j dW_j` and flipping all transverse `W_j` simultaneously.

## 2. Inner parity forces conjugacy before any limit is taken

Assume there is a fixed invertible matrix `J` such that

\[
JAJ^{-1}=A,
\qquad
JBJ^{-1}=-B.
\]

Then pointwise along the radial path

\[
\widetilde\Omega_n=J\Omega_nJ^{-1}.
\]

Use the same right-ordered convention as PC-350/PC-351. If `U_R` is the cutoff development solving

\[
U'=U\Omega_n,
\qquad
U(0)=I,
\]

then uniqueness of the matrix ODE gives

\[
\widetilde U_R=J U_R J^{-1}.
\]

The reciprocity regularization uses the closing factor determined by the image of the residue ray,

\[
C_R=\exp[-(\log R)A].
\]

Since `J` fixes `A`, it commutes with `C_R`. Therefore the regularized defects satisfy the exact finite-cutoff identity

\[
\boxed{
\widetilde D_R
=\widetilde U_R C_R
=J\,D_R\,J^{-1}.
}
\]

No convergence assumption is needed for this identity. If a regularized limit exists, the same conjugacy passes to the limit. If the target matrices depend analytically on a spectral parameter while preserving the same parity, the identity holds pointwise in that parameter as well.

Hence every class function of the development is identical for the cyclotomic source and the matched reciprocal control. In particular this includes characteristic polynomials, traces of powers, eigenvalue multisets, determinants such as `det(I-zD)`, and the zero sets of any spectral determinant assembled functorially from those conjugacy classes.

If `J` is unitary in the chosen realization, the obstruction is stronger: singular values, pseudospectra, numerical ranges, and other unitary-conjugacy invariants also agree exactly.

## 3. The obstruction survives a genuinely non-solvable SL2 target

Take the standard basis

\[
H_0=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
E=
\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
F=
\begin{pmatrix}0&0\\1&0\end{pmatrix}
\]

of `sl_2(C)`, with

\[
[H_0,E]=2E,
\qquad
[H_0,F]=-2F,
\qquad
[E,F]=H_0.
\]

Choose

\[
A=\alpha H_0,
\qquad
B=\beta E+\gamma F,
\qquad
\alpha\beta\gamma\neq0.
\]

Then

\[
[A,B]=2\alpha(\beta E-\gamma F).
\]

The two vectors `B` and `[A,B]` recover `E` and `F` separately, and their bracket recovers `H_0`. Thus

\[
\boxed{
\operatorname{Lie}\langle A,B\rangle=\mathfrak{sl}_2(\mathbb C).
}
\]

This target is therefore genuinely non-solvable and cannot be simultaneously triangularized. It lies strictly outside the no-go class proved in PC-351.

Nevertheless set

\[
J=\operatorname{diag}(i,-i)\in SL_2(\mathbb C).
\]

Its adjoint action is

\[
\operatorname{Ad}_J(H_0)=H_0,
\qquad
\operatorname{Ad}_J(E)=-E,
\qquad
\operatorname{Ad}_J(F)=-F.
\]

Therefore

\[
JAJ^{-1}=A,
\qquad
JBJ^{-1}=-B,
\]

and the exact matched-control conjugacy from the previous section applies. The first non-solvable repair of PC-351 is thus not control-selective despite using the full `sl_2` Lie algebra.

## 4. Higher-dimensional SL2 representations do not rescue the same mechanism

Let `pi` be any finite-dimensional representation of `SL_2(C)`. Applying `pi` to the group-level identity gives

\[
\boxed{
\pi(\widetilde D_R)
=\pi(J)\,\pi(D_R)\,\pi(J)^{-1}.
}
\]

Thus passing to a higher-spin or otherwise higher-dimensional representation of the same `SL_2` development does not restore any similarity-invariant discriminator. The control involution remains implemented by one fixed conjugating element.

Moreover `J` belongs to the compact subgroup `SU(2)`. After equipping a finite-dimensional representation with an `SU(2)`-invariant Hermitian form, `pi(J)` is unitary, so the same conclusion extends to the usual metric operator invariants in that normalization.

This matters because increasing representation dimension can expose more signature coordinates, but it cannot defeat a symmetry already realized by inner conjugation. More matrix entries are not a new spectral mechanism when the matched control occupies the same conjugacy orbit.

## 5. General inner-parity no-go

The `SL_2` example is a corollary of a broader statement. Suppose a target Lie algebra has a `Z/2` decomposition with the calibration image in the even sector and every centered-shell image in the odd sector. Let the parity automorphism

\[
\theta(A)=A,
\qquad
\theta(B_j)=-B_j
\]

be implemented by conjugation with a fixed group element `J`. Then the simultaneous reciprocal sign-flip control is exactly `Ad_J` of the arithmetic connection and hence of every regularized development.

Therefore a necessary condition for a surviving representation-based spectral route is stronger than merely **non-triangular** or **non-solvable**. The reciprocal control involution must fail to be inner-equivalent on the proposed observable quotient, or the observable must retain some additional source-forced structure that is not invariant under that equivalence.

This does not prove that all non-solvable targets fail. A representation whose arithmetic/control involution is not implemented by a fixed inner conjugacy is outside the theorem. So is a genuinely control-selective quotient that deliberately retains information not descending to the conjugacy class. Such a quotient would still need an independent zero-sensitive destination theorem to qualify as progress toward RH rather than source reconstruction.

## Prior-art audit

The use of finite-dimensional Lie-group developments and semisimple targets is established mathematics rather than a novel ingredient. In particular, Boedihardjo, Geng and Wang, **Cartan's Path Development, the Logarithmic Signature and a Conjecture of Lyons-Sidorova** (arXiv:2506.18207, 2025), explicitly use developments into complex semisimple Lie algebras `sl_m(C)` to extract finite-dimensional information from path signatures. This is a nearby structural warning: replacing a solvable decoder by `SL_2` is not itself a new mechanism.

The parity computation used here is elementary Lie theory: the involution fixing `H_0` and negating the two root spaces of `sl_2` is inner, implemented by `diag(i,-i)`. A targeted search found no prior result asserting the specific prime-circle reciprocal-control obstruction above. No novelty is claimed for either semisimple path development or this elementary `sl_2` automorphism; the durable content is their exact interaction with the source-native PC-350 centering, PC-351 matched reciprocal control, and the RH falsification requirement.

The external paper is contextual prior art rather than a dependency of the proof. The exact no-go is self-contained and rests only on line-local identities plus the displayed matrix conjugacy, so no new durable source anchor is required for the derivation.

## Falsification / disproof audit

- **Non-solvable check:** with `alpha beta gamma != 0`, the generated Lie algebra is exactly `sl_2(C)`, so the result is not secretly another triangular/solvable collapse.
- **Finite-cutoff check:** conjugacy holds before taking `R -> infinity`; it cannot be an artifact of a divergent or lossy regularization limit.
- **Residue check:** the shell-letter substitution sends the exact reciprocity vector to `A`, so the closing factor is the same for source and control and is fixed by `J`.
- **Matched-control check:** `tilde(X)_n=2 varphi(n) X_2-X_n` preserves the same residue and inversion law while sending only the centered profile to its negative, exactly as in PC-351.
- **Spectral-parameter check:** any parameter dependence that preserves the even/odd target parity remains conjugate pointwise; adding a parameter does not by itself create a selective zero set.
- **Boundary check:** arbitrary `sl_2` pairs need not satisfy the displayed parity. The theorem intentionally does not claim that every non-solvable `SL_2` development is control-conjugate.
- **Gauge-information check:** oriented matrix coefficients can distinguish conjugate representatives after a gauge choice, but then the observable has not descended to a basis-free spectral quotient. That returns to source-coordinate information rather than solving the control-selection problem.

## Boundary assessment

PC-351 showed that the faithful PC-350 decoder is spectrally trivial throughout the triangular sector. PC-352 sharpens the surviving frontier: **non-solvability alone is insufficient**. The natural parity-graded `SL_2` lift can generate the full semisimple Lie algebra and still be exactly indistinguishable from a matched reciprocal control by every conjugacy-invariant spectral readout.

A viable continuation must therefore break this inner-parity equivalence in a source-forced way. Candidates must state, before spectralization, why the arithmetic source and the reciprocal control cannot be related by a fixed target automorphism on the proposed quotient, and then exhibit a destination invariant with independent zeta-zero sensitivity. Merely moving to larger matrices, higher-spin `SL_2` representations, or another inner-parity semisimple realization does not cross that boundary.

## Artifact status

Single durable finding. No clue disposition changes: the broader signed-radial-flux clue remains open because this theorem closes only the inner-parity representation branch, not every noncommutative assembly.