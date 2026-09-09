# NB-001 — complete generator Gram data do not determine Nyman target distance

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + NEGATIVE/OBSTRUCTION + TARGET-AWARE-FINITE-CERTIFICATE`. In the Hardy-space form of the Nyman--Beurling/Báez-Duarte problem, the complete finite Gram matrix of the discrete generators does not determine their distance to the fixed target. The missing datum is exactly the target-pairing vector. For the canonical discrete generators this vector is explicit, and the finite best-approximation error is the Schur-complement quantity

\[
d_N^2
=1-b_N^*G_N^+b_N,
\]

where `G_N^+` is the Moore--Penrose pseudoinverse. A common inner multiplier preserves **every** generator--generator inner product while changing the target pairings. The explicit half-plane Blaschke factor

\[
B_*(s)=\frac{s-1}{s}
\]

preserves the entire generator Gram matrix but makes the fixed target orthogonal to the whole twisted finite span. Thus Gram spectra, condition numbers, determinants of the generator block, and any statistic determined solely by that block cannot certify Nyman target approximation. The target-aware augmented Gram data are necessary already at finite dimension.

This is an exact matched-control obstruction, not a new approximation rate. It does not show that the canonical Nyman family fails, because the inner-twisted family is a synthetic control rather than an alternative admissible arithmetic generator family. Its role is to identify the finite information that any quantitative Nyman argument must retain before taking a growing-section limit.

## 1. Canonical Hardy-space finite sections have an explicit target vector

Use the Hardy space

\[
\mathcal H=H^2(\Omega),
\qquad
\Omega=\{s\in\mathbb C:\operatorname{Re}s>1/2\},
\]

with the boundary norm normalized as in Bagchi,

\[
\|F\|_{\mathcal H}^2
=\frac1{2\pi}\int_{-\infty}^{\infty}
|F(1/2+it)|^2\,dt.
\tag{1}
\]

The Mellin transform identifies the classical `L^2(0,1)` Nyman problem isometrically with this Hardy-space formulation. The reproducing kernel at `w\in\Omega` is

\[
k_w(s)=\frac1{s+\overline w-1}.
\tag{2}
\]

Hence the Nyman target is exactly

\[
E(s)=\frac1s=k_1(s),
\qquad
\|E\|^2=k_1(1)=1,
\tag{3}
\]

and for every `F\in\mathcal H`,

\[
\langle F,E\rangle=F(1)
\tag{4}
\]

under the convention linear in the first slot.

For integers `k\ge2`, take the standard discrete Hardy generator

\[
G_k(s)
=\left(k^{-s}-k^{-1}\right)\frac{\zeta(s)}s.
\tag{5}
\]

The apparent singularity at `s=1` is removable. Since

\[
k^{-s}-k^{-1}
=-\frac{\log k}{k}(s-1)+O((s-1)^2),
\qquad
\zeta(s)=\frac1{s-1}+O(1),
\]

we obtain the exact target pairing

\[
\boxed{
 b_k:=\langle G_k,E\rangle
 =G_k(1)
 =-\frac{\log k}{k}.
}
\tag{6}
\]

Thus the target vector is not an unknown numerical side quantity. It is an elementary source-fixed vector attached to the same finite section.

For `N\ge2`, let

\[
V_N=\operatorname{span}\{G_2,\ldots,G_N\},
\]

and write

\[
G_N=(\langle G_j,G_k\rangle)_{2\le j,k\le N},
\qquad
b_N=(b_k)_{2\le k\le N}.
\tag{7}
\]

If `A_N:\mathbb C^{N-1}\to\mathcal H` is the synthesis map with columns `G_k`, then

\[
G_N=A_N^*A_N,
\qquad
b_N=A_N^*E.
\]

The orthogonal projector onto `V_N=\operatorname{ran}A_N` is

\[
P_N=A_NG_N^+A_N^*,
\]

so the exact squared residual is

\[
\boxed{
 d_N^2
 :=\operatorname{dist}(E,V_N)^2
 =1-b_N^*G_N^+b_N.
}
\tag{8}
\]

No invertibility assumption is needed. If the chosen generators are independent, (8) is equivalently the Schur complement of the generator block in the augmented Gram matrix

\[
\begin{pmatrix}
1 & b_N^*\\
b_N & G_N
\end{pmatrix}.
\tag{9}
\]

Equation (8) is invariant under every invertible change of finite generator coordinates when the target vector is transported with the same change. It also states precisely how near-null Gram modes matter: only their target-weighted coordinates contribute to the projection. An eigenvalue list without those coordinates is insufficient.

## 2. A common inner factor preserves the full Gram matrix but changes the target distance

Let `B\in H^\infty(\Omega)` be inner: its boundary values have modulus one almost everywhere on `\operatorname{Re}s=1/2`. Multiplication

\[
M_B:F\mapsto BF
\]

is an isometry of `\mathcal H`. Therefore the twisted finite family

\[
\widetilde G_k=BG_k
\tag{10}
\]

has exactly the same complete Gram matrix:

\[
\boxed{
\langle\widetilde G_j,\widetilde G_k\rangle
=\langle G_j,G_k\rangle
\quad\text{for all }j,k.
}
\tag{11}
\]

But the target is fixed rather than co-multiplied. Reproduction at `s=1` gives

\[
\widetilde b_k
=\langle BG_k,E\rangle
=(BG_k)(1)
=B(1)b_k.
\tag{12}
\]

Consequently the twisted distance is

\[
\boxed{
\widetilde d_N^2
=1-|B(1)|^2 b_N^*G_N^+b_N
=(1-|B(1)|^2)+|B(1)|^2d_N^2.
}
\tag{13}
\]

This produces a continuous family of target distances while the entire generator Gram matrix remains fixed.

The sharpest control needs no abstract interpolation theorem. Take

\[
B_*(s)=\frac{s-1}{s}.
\tag{14}
\]

For `s=1/2+it`, `|s-1|=|s|`; inside `\Omega`,

\[
|s|^2-|s-1|^2=2\operatorname{Re}s-1>0.
\]

Hence `B_*` is a bounded inner function on the half-plane and `B_*(1)=0`. Equations (11)--(13) give

\[
\boxed{
\widetilde G_N=G_N,
\qquad
\widetilde b_N=0,
\qquad
\operatorname{dist}(E,B_*V_N)=1
\quad\text{for every }N.
}
\tag{15}
\]

Equivalently, every vector of `B_*V_N` vanishes at `s=1`, so it is orthogonal to the reproducing kernel `E=k_1`.

For the canonical family, by contrast, `b_2=-\log 2/2\ne0`, so `E` has a nonzero projection onto every `V_N` containing `G_2`; in particular `d_N<1`. Thus two finite families can have **identical full generator Gram data** and different target distances, including the maximal-distance control (15).

## 3. Exact consequence for finite Nyman certificates

The matched control proves the following finite information boundary:

> No rule depending only on the complete generator Gram matrix can determine, upper-bound nontrivially, or certify decay of the distance from the fixed Nyman target without an additional target-relative hypothesis.

This includes any rule based only on Gram eigenvalues, condition numbers, singular values, determinants of the generator block, block-compressibility, or another invertible re-expression of generator--generator inner products. Such quantities may still be useful once a theorem controls how the fixed target sits in their eigenvectors; (15) only blocks treating the Gram geometry itself as that theorem.

Conversely, `(G_N,b_N,\|E\|^2)` is an exact complete finite certificate for the best-approximation error through (8). It also immediately supplies a finite dual witness. If

\[
r_N=E-P_NE,
\qquad d_N=\|r_N\|>0,
\]

then

\[
\ell_N(F)=\frac{\langle F,r_N\rangle}{d_N}
\tag{16}
\]

has norm one, annihilates `V_N`, and satisfies

\[
\ell_N(E)=d_N.
\tag{17}
\]

This is standard Hilbert duality rather than a new arithmetic obstruction. Its value here is to make the remaining burden explicit: a useful asymptotic lower or upper bound must control the target-aware quantity `b_N^*G_N^+b_N`, or an equivalent normed residual functional, uniformly as the section grows.

## 4. Prior art and novelty boundary

The underlying Hardy-space formulation is classical in this literature. Báez-Duarte proved that integer dilations suffice for the strengthened Nyman--Beurling criterion; Bagchi gives a clean Hardy-space/Mellin formulation, including the discrete generators and the inner-function/isometry structure. The finite projection identity (8), reproducing-kernel evaluation, Schur complements, and the Blaschke factor (14) are standard Hilbert/Hardy-space tools. **No theorem-level novelty is claimed for these ingredients individually.**

The nearest modern Gram-focused work also reinforces the distinction rather than removing it. Hugh Carvill, *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing* (arXiv:2510.18132), studies unconditional decay and block-compressibility of a Beurling--Nyman Gram family. Those are generator-geometry results; (11)--(15) show why a separate target-alignment estimate is still logically necessary before such structure can certify the fixed Nyman target distance.

The quantitative asymptotic problem is known to be much deeper than the finite identity. Burnol derives a zero-sensitive lower bound for the Nyman--Beurling approximation error, and Bettin--Conrey--Farmer obtain the matching optimal constant only conditionally on RH together with a bound on reciprocal zeta-derivative moments. Therefore (8) is not presented as a new `1/\log N` estimate, nor does the explicit vector (6) bypass the known zero-sensitive asymptotic difficulty.

Authoritative anchors used here:

- Luis Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis*, Rend. Lincei Mat. Appl. 14 (2003), 5--11; arXiv:math/0202141.
- Bhaskar Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, Proc. Indian Acad. Sci. Math. Sci. 116 (2006), 137--146; arXiv:math/0607733; DOI `10.1007/BF02829783`.
- Jean-François Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, Adv. Math. 170 (2002), 56--70; arXiv:math/0103058; DOI `10.1006/aima.2001.2066`.
- Sandro Bettin, J. Brian Conrey, David W. Farmer, *An optimal choice of Dirichlet polynomials for the Nyman-Beurling criterion*, arXiv:1211.5191.

A targeted literature search did not identify the exact matched-control statement (15) being used as a named Nyman theorem, but that absence is not evidence of novelty. The durable contribution of this finding is the **Mathia evidence boundary**: complete finite Gram information is formally non-identifying for the fixed target, while the canonical target vector is explicit and the remaining asymptotic question can be stated without a Gram-only ambiguity.

## 5. Research consequence and falsification boundary

This finding answers the finite part of the local target-aware clue but does not resolve its asymptotic question. The next live quantity is

\[
q_N:=b_N^*G_N^+b_N=1-d_N^2,
\tag{18}
\]

with

\[
(b_N)_k=-\frac{\log k}{k}.
\]

A substantive continuation must do more than diagonalize `G_N`: it must control the target mass in its small-eigenvalue directions, construct an explicit admissible approximant with a norm-certified residual, or build a norm-controlled dual witness whose target value has an asymptotically informative bound. Any proposed spectral cutoff must account for the discarded `b_N` mass.

The main falsification controls are strict. The inner-twisted family is **not** claimed to be another canonical Báez-Duarte family, so (15) does not refute the criterion. Co-transforming the target by `B` would preserve the distance and therefore would not be a valid matched control for target identification. A basis change inside the same canonical span also changes `(G_N,b_N)` covariantly and leaves (8) unchanged; it cannot manufacture a target gain. Finally, a finite decrease of `d_N` does not imply closure or any asymptotic rate.

No improved zero-free region, unconditional Nyman approximation rate, or RH consequence follows from NB-001 alone. Its exact effect is to remove Gram-only finite-section evidence from the live route and to identify the target-aware scalar that future arithmetic estimates must actually control.