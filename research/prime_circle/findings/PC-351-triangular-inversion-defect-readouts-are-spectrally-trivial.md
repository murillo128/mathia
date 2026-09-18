# PC-351 - Triangular inversion-defect readouts are spectrally trivial despite faithful off-diagonal decoding

- **Finding ID:** `PC-351`
- **Status:** `EXACT-DERIVED`
- **Status detail:** `DECISIVE-NEGATIVE`
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact
- **Prime dependence:** the full centered shell profile can survive in oriented off-diagonal coefficients, but ordinary spectra of triangular developments and basis-free operator readouts of the canonical 2x2 decoder are source-blind under a matched reciprocal control
- **RH relevance:** high as a boundary result: the faithful decoder of PC-350 does not become a new RH spectral mechanism by taking eigenvalues, determinants, traces, Jordan data, singular values, pseudospectra, numerical ranges, or other invariants preserved by simultaneous unitary conjugacy

## Claim

PC-350 showed that the full reciprocal inversion defect is faithful: a source-native `2 x 2` unipotent development recovers the complete centered radial profile through a Fourier transform. The natural next question is whether that faithful matrix object has a useful basis-free spectral quotient. It does not, for the entire simultaneously upper-triangular class, and the canonical decoder admits an exact matched-control obstruction stronger than mere eigenvalue collapse.

Let

\[
X_n(r)=\log \Phi_n(r),\qquad a_n=\varphi(n),\qquad X_2(r)=\log(1+r),
\]

and define the centered reciprocal profile

\[
W_n(r)=X_n(r)-a_nX_2(r).
\]

For `n>1`, cyclotomic reciprocity gives

\[
X_n(r)=a_n\log r+X_n(1/r),
\]

hence

\[
W_n(r)=W_n(1/r),\qquad W_n(0)=W_n(\infty)=0.
\]

### 1. Every simultaneously upper-triangular regularized development has trivial limiting spectrum

Take finitely many shell matrices `M_n` that are simultaneously upper triangular over `C`. For a radial cutoff `R`, form the same residue-subtracted development used by the reciprocal-defect construction,

\[
D_R(M)=\mathcal P\exp\!\left(\int_0^R\sum_n M_n\,dX_n(r)\right)
\exp\!\left[-(\log R)H_M\right],
\qquad
H_M=\sum_n a_nM_n.
\]

Upper-triangularity is preserved by the ordered exponential and by the closing factor. If `m_{n,jj}` denotes the `j`th diagonal entry of `M_n`, scalarity on the diagonal gives exactly

\[
(D_R)_{jj}
=
\exp\!\left(\sum_n m_{n,jj}[X_n(R)-a_n\log R]\right)
=
\exp\!\left(\sum_n m_{n,jj}X_n(1/R)\right).
\]

Therefore

\[
(D_R)_{jj}\longrightarrow 1\qquad(R\to\infty).
\]

So every eigenvalue tends to `1`. Whenever the regularized matrix limit exists, the limiting defect is upper-unitriangular and consequently

\[
\boxed{\operatorname{Spec}D(M)=\{1\}},\qquad
\boxed{\det D(M)=1},\qquad
\boxed{\operatorname{tr}D(M)^k=d}
\]

for a `d x d` representation and every positive integer `k`. The source can remain fully encoded in nilpotent/off-diagonal coordinates while the ordinary spectrum is completely blind to it.

This is not a statement about arbitrary noncommutative representations. It is a no-go for the simultaneously triangularizable sector, including all finite-dimensional upper-triangular decoders of the type used to make the PC-350 reconstruction explicit.

### 2. The canonical PC-350 decoder is faithful but spectrally constant

PC-350 constructs the `2 x 2` readout

\[
T_n(\lambda)=
\begin{pmatrix}
1 & V_n(\lambda)\\
0 & 1
\end{pmatrix},
\qquad
V_n(\lambda)=\int_0^\infty (1+r)^\lambda\,dW_n(r),
\]

initially in its convergent half-plane and then with the equivalent interior/Fourier description used there. The family `V_n(i\tau)` is faithful to the centered profile by Fourier uniqueness, but

\[
\operatorname{Spec}T_n(\lambda)=\{1,1\},\qquad
\det T_n(\lambda)=1,\qquad
\operatorname{tr}T_n(\lambda)=2
\]

for every `n` and `lambda`. Its similarity class contains only one bit: `V_n(lambda)=0` gives the identity, while every `V_n(lambda) != 0` is similar to the same Jordan block `J_2(1)`. Thus the information established as faithful in PC-350 resides in an oriented matrix coefficient, not in the ordinary spectrum.

### 3. A matched reciprocal sign-flip control is globally unitarily equivalent

The stronger obstruction appears before specializing to cyclotomic shells. Use the matched reciprocal control class already underlying the PC-350 audit: let `Y_0(r)=log(1+r)` and let a transverse source `Y_j` have residue `a_j`, origin normalization, and reciprocity

\[
Y_j(r)=a_j\log r+Y_j(1/r).
\]

Write its centered profile as

\[
Z_j(r)=Y_j(r)-a_jY_0(r).
\]

Define a distinct matched source by

\[
\widetilde Y_j(r)=2a_jY_0(r)-Y_j(r).
\]

It has the same residue and the same reciprocal closure:

\[
\widetilde Y_j(r)=a_j\log r+\widetilde Y_j(1/r),
\]

while

\[
\widetilde Z_j=-Z_j.
\]

Therefore its decoder coefficient is exactly

\[
\widetilde V_j(\lambda)=-V_j(\lambda).
\]

Now set

\[
S=\operatorname{diag}(1,-1).
\]

The same fixed unitary works for every shell and every spectral parameter:

\[
\boxed{T(-V)=S\,T(V)\,S^{-1}.}
\]

Hence the complete decoder family of a source and that of its matched reciprocal sign-flip twin are globally unitarily equivalent. Every observable invariant under simultaneous unitary conjugacy is therefore identical for the pair. This includes eigenvalues, the identity/nonidentity Jordan pattern, singular values, pseudospectra, and numerical ranges. More generally, any proposed basis-free operator invariant that factors through this unitary-equivalence class fails the mandated matched-control test.

The obstruction is stronger than saying that the eigenvalues are constant: even nonnormal basis-free geometry cannot distinguish the cyclotomic decoder from this exact reciprocal control twin. To retain the PC-350 information one must keep an oriented off-diagonal coordinate (or equivalent gauge choice), which is reconstruction of the source rather than a new spectral quotient.

### 4. Cyclotomic positivity makes the real-parameter Jordan behavior universal

For the actual cyclotomic source there is an additional exact degeneration. For every `n>2` and `r>0`, pair primitive roots conjugately. A pair `zeta=e^{i theta}`, `bar(zeta)` contributes

\[
(r-\zeta)(r-\bar\zeta)=r^2-2r\cos\theta+1.
\]

No primitive root is `-1` when `n>2`, so `cos(theta)>-1`, and therefore

\[
r^2-2r\cos\theta+1<(1+r)^2.
\]

Multiplying the primitive conjugate pairs gives the strict inequality

\[
0<\Phi_n(r)<(1+r)^{\varphi(n)},
\]

or equivalently

\[
\boxed{W_n(r)<0\qquad(n>2,\ r>0).}
\]

For real `lambda<1`, the boundary term vanishes and integration by parts yields

\[
V_n(\lambda)
=-\lambda\int_0^\infty W_n(r)(1+r)^{\lambda-1}\,dr
=\lambda\int_0^\infty[-W_n(r)](1+r)^{\lambda-1}\,dr.
\]

Thus

\[
\boxed{\operatorname{sign}V_n(\lambda)=\operatorname{sign}\lambda}
\]

for real `lambda<1`, with the unique real zero at `lambda=0`. Equivalently, after `y=log(1+r)`,

\[
\frac{V_n(\lambda)}{\lambda}
=
\int_0^\infty q_n(y)e^{\lambda y}\,dy,
\qquad
q_n(y)=-W_n(e^y-1)>0.
\]

Consequently the canonical Jordan class on the entire real decoder line `lambda<1` is universal across all `n>2`: identity at zero and the same nontrivial unipotent class everywhere else. This does **not** imply a complex zero-free region for `V_n`; no such claim is made. Any complex zero set is in any case preserved by the exact sign-flip control above.

## Consequences

The faithful all-depth reconstruction of PC-350 and spectral usefulness are sharply separated. Passing from the oriented matrix coefficient to eigenvalues destroys all shell information in every triangular representation, and passing to richer unitary-invariant data still fails because a matched reciprocal control is globally unitarily equivalent to the cyclotomic decoder after a sign flip of the centered source.

This closes the natural route

`faithful reciprocal Chen/Fourier decoder -> finite-dimensional triangular matrix -> basis-free spectral/operator invariant -> new RH mechanism`.

A surviving operator route must therefore leave this class in a mathematically forced way. In particular, it would need a genuinely non-triangular/non-solvable source-forced representation or another strict quotient that is both information-reducing and selective against matched reciprocal controls. Merely preserving all off-diagonal reconstruction data is not enough: that returns to the full-source encoding already classified by PC-350.

## Prior-art audit

The abstract ingredients used here are classical. Spectra of triangular matrices are their diagonal entries; unitary similarity preserves singular values, pseudospectra, numerical ranges, and all ordinary basis-free operator data of the corresponding family. No novelty is claimed for those linear-algebra facts. Likewise, signature reconstruction and uniqueness are already anchored in this line through the Hambly-Lyons and Lyons-Xu literature recorded for PC-348--PC-350.

The line-specific content is their exact interaction with cyclotomic reciprocity and residue subtraction: the closing term forces every triangular diagonal to `1`, while the broad matched reciprocal source class has an explicit sign-flip involution implemented by one fixed unitary on the PC-350 decoder. A targeted novelty audit found no prior result asserting this prime-circle reciprocal-defect obstruction as an RH mechanism; the result should therefore be read as an exact boundary theorem for this construction, not as a new general theorem about triangular matrices or signatures. No new durable literature dependency is required beyond the existing source anchors.

## Falsification / disproof audit

- **Dimension-one control:** the result reduces to the scalar reciprocal closure and gives the identity, as it must.
- **`n=2` control:** `W_2=0`, so the canonical decoder is exactly the identity. The strict positivity argument is intentionally stated only for `n>2`.
- **Matched-control check:** `tilde(Y)_j=2a_jY_0-Y_j` preserves the origin normalization, residue, and reciprocity exactly, while reversing only the centered profile. The same fixed unitary `S` conjugates the whole `lambda`-family, not just one parameter value.
- **Complex-parameter check:** the positivity argument proves only the real statement `lambda<1`; it does not assert that the analytic continuation or imaginary-axis Fourier transform has no nonreal zeros.
- **Representation boundary:** a genuinely non-triangular representation is outside the theorem. The result does not infer triangularizability from noncommutativity alone.
- **Information boundary:** keeping the signed/off-diagonal coefficient can distinguish the matched control and can reconstruct the source, exactly as PC-350 proved. The negative result concerns spectral or basis-free quotients of that faithful encoding.

## Boundary assessment

This is a decisive negative for the most direct spectralization of the current live frontier, not a no-go for all noncommutative prime-circle operators. PC-350 remains intact: its full inversion defect is faithful. What PC-351 adds is that **faithful does not mean spectrally informative**. Within the finite-dimensional triangular sector, reciprocity pushes all arithmetic information into nilpotent coordinates, and the canonical decoder's basis-free operator geometry is defeated by an exact matched reciprocal control.

The next admissible branch must therefore specify, before computation, a source-forced non-triangular/non-solvable representation or a strict control-selective quotient with an independently zero-sensitive destination. Otherwise the construction is either spectrally trivial or merely reconstructs the original centered source.

## Artifact status

Single durable finding. No source-anchor update is required because the derivation introduces no new literature dependency; it uses only exact line-local identities plus classical linear algebra already covered by the existing audit surface.
