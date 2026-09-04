# WI-137 — Lamzouri's full finite slack is an exact distance from a 2/1/0 quantized operator

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-INTERFACE`. WI-126 decomposes Lamzouri's finite Hilbert-space inequality into four nonnegative remainders, and WI-136 recombines two of them to show that simple-real directions cannot screen off-line odd directions for free. Keeping the **off-diagonal Bessel coefficients** instead of discarding them gives a sharper exact normal form: the entire finite deficit is the squared Hilbert--Schmidt distance of Lamzouri's symmetric tensor operator from the block-quantized target `2` on `U`, `1` on `V\ominus U`, `0` on `W\ominus V`, plus the already identified population/horizontal charges.

More precisely, in Lamzouri's notation let

\[
\Delta:=n-(2N-Q)=Q-(2N-n),
\]

let `U\subset V\subset W` be his nested spaces, put `M:=V\ominus U`, `H:=W\ominus V`, `d=\dim U`, and let

\[
B:=A_U-2d\ge0
\]

be the exact `U`-coefficient excess from WI-126. On the real Hilbert form fixed by Lamzouri's symmetry `\overline\Phi(u)=\Phi(-u)`, define the self-adjoint operator associated with his two-variable tensor `F` by

\[
\mathcal A_F
:=
\sum_{x\in R}m_x\,f_x\otimes f_x
+2\sum_{z\in Z_+}m_z\,(g_z\otimes g_z-h_z\otimes h_z),
\]

where `Z_+` contains one representative of each non-real conjugate pair and `v\otimes v` denotes the real rank-one operator `w\mapsto\langle w,v\rangle v`. Let

\[
\mathcal D:=P_U+P_V.
\]

Then `\mathcal D` has eigenvalue `2` on `U`, `1` on `M`, and `0` on `H`, and the exact identity is

\[
\boxed{
\Delta
=
\|\mathcal A_F-\mathcal D\|_{\mathrm{HS}}^2
+2B+4H_V,
}
\tag{A}
\]

where

\[
H_V:=\sum_{z\in Z_+}m_z\|P_{V^\perp}h_z\|^2.
\]

Using WI-126's exact formula

\[
B=S_1+E_{\mathbb R}+2E_{\mathbb C}+2H_U,
\]

this becomes

\[
\boxed{
\Delta
=
\|\mathcal A_F-(P_U+P_V)\|_{\mathrm{HS}}^2
+2S_1+2E_{\mathbb R}+4E_{\mathbb C}+4H_U+4H_V.
}
\tag{B}
\]

Thus near saturation does not merely force the off-line odd directions toward `U`: it forces the **whole Lamzouri tensor operator** to approach an integer-valued spectral pattern. No unconditional zeta-zero percentage changes in this finding.

## 1. Primary-source interface

The source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1 and its proof. Lamzouri takes a finite conjugation-invariant multiset `Z`, a real even compactly supported function `eta` with `\widehat{\eta^2}(0)=1`, and defines

\[
f_z(u)=\eta(u)e^{-2\pi iuz},\qquad
 g_z=\frac{f_z+f_{\bar z}}2,\qquad
 h_z=\frac{f_z-f_{\bar z}}{2i}.
\]

Grouping non-real elements by conjugate pairs gives his exact two-variable expansion

\[
F
=
\sum_{x\in R}m_x f_x\otimes f_x
+2\sum_{z\in Z_+}m_z(g_z\otimes g_z-h_z\otimes h_z).
\tag{1}
\]

All `f_x`, `g_z`, and `h_z` appearing in (1) satisfy Lamzouri's real symmetry

\[
\overline\Phi(u)=\Phi(-u).
\tag{2}
\]

The inner product of two such vectors is real, so their span has a canonical real Hilbert-space form. Lamzouri applies Gram--Schmidt inside this form to obtain an orthonormal basis `(psi_j)` adapted to `U\subset V\subset W`. The public `AxiomMath/ZetaZeros` formalization independently encodes the same `g/h` expansion and proves that the corresponding diagonal Bessel coefficients are real; this supports the source-level algebra but does not contain the stability identity (A).

Lamzouri's kernel identity gives

\[
Q=\|F\|^2.
\tag{3}
\]

Because every tensor factor in (1) lies in `W`, we actually have `F\in W\otimes W`. Therefore Parseval in the **full** tensor-product basis is an equality, not merely the diagonal Bessel inequality used in the published proof.

## 2. Recover the off-diagonal part of Bessel exactly

For an adapted orthonormal basis `(psi_1,\ldots,psi_{D_W})`, define

\[
c_{ij}:=\langle F,\psi_i\otimes\psi_j\rangle.
\tag{4}
\]

The symmetry of `F` and the real structure make `C=(c_{ij})` a real symmetric matrix. Lamzouri's diagonal coefficients are exactly

\[
\alpha_i=c_{ii}.
\tag{5}
\]

Full Parseval and (3) give

\[
Q=\sum_{i,j}c_{ij}^2.
\tag{6}
\]

Hence the Bessel remainder introduced in WI-126,

\[
R_B:=Q-\sum_i\alpha_i^2,
\]

has the exact interpretation

\[
\boxed{R_B=\sum_{i\ne j}c_{ij}^2.}
\tag{7}
\]

So `R_B` is not an opaque proof loss. It is precisely the off-diagonal Hilbert--Schmidt mass of the Lamzouri tensor in an adapted basis.

The matrix `C` is the matrix of the basis-independent self-adjoint real operator `\mathcal A_F` defined above. Under a different orthonormal basis respecting the same real form and the same nested subspaces, `C` changes by real orthogonal conjugation. The target

\[
D:=\operatorname{diag}(2I_U,I_M,0_H)
\tag{8}
\]

is the matrix of the canonical operator `P_U+P_V`, so `\|C-D\|_F=\|\mathcal A_F-(P_U+P_V)\|_{HS}` is basis-independent.

## 3. Completion of the four Lamzouri remainders

WI-126 proves the exact decomposition

\[
\Delta=R_B+R_U+R_M+R_H,
\tag{9}
\]

with

\[
R_U=\sum_{i\in U}(\alpha_i^2-2\alpha_i),
\qquad
R_M=\sum_{i\in M}(\alpha_i-1)^2,
\]

\[
R_H=\sum_{i\in H}(\alpha_i^2-2\alpha_i).
\tag{10}
\]

Write `A_U=\sum_{i\in U}\alpha_i=2d+B`. Then

\[
\begin{aligned}
R_U-\sum_{i\in U}(\alpha_i-2)^2
&=2\sum_{i\in U}(\alpha_i-2)\\
&=2B.
\end{aligned}
\tag{11}
\]

On `H`, Lamzouri's exact sign formula gives `\alpha_i\le0`. Put `b_i=-\alpha_i`. WI-126 reconstructs

\[
\sum_{i\in H}b_i
=2\sum_{z\in Z_+}m_z\|P_Hh_z\|^2
=2H_V.
\tag{12}
\]

Therefore

\[
R_H-\sum_{i\in H}\alpha_i^2
=-2\sum_{i\in H}\alpha_i
=4H_V.
\tag{13}
\]

Combining (7), (10)--(13),

\[
\begin{aligned}
\Delta
&=\sum_{i\ne j}c_{ij}^2
 +\sum_{i\in U}(\alpha_i-2)^2
 +\sum_{i\in M}(\alpha_i-1)^2
 +\sum_{i\in H}\alpha_i^2
 +2B+4H_V\\
&=\|C-D\|_F^2+2B+4H_V,
\end{aligned}
\]

which is (A).

There is no lost inequality in this step. It is an exact repackaging of all four remainders. Moreover, the `U`-diagonal part already contains the convexity term from WI-136:

\[
\sum_{i\in U}(\alpha_i-2)^2
=
\sum_{i\in U}\left(\alpha_i-\frac{A_U}{d}\right)^2
+\frac{B^2}{d}
\tag{14}
\]

when `d>0`. Thus WI-136 is recovered by lower-bounding the Hilbert--Schmidt term in (A) by `B^2/d` and discarding its remaining nonnegative pieces.

## 4. Near saturation forces a 2/1/0 spectrum

Let the eigenvalues of `\mathcal A_F` be ordered decreasingly,

\[
\lambda_1\ge\cdots\ge\lambda_{D_W},
\qquad D_W=d+n+k,
\]

where `k=\dim H` is the number of distinct off-real conjugate pairs. The target `\mathcal D=P_U+P_V` has ordered spectrum

\[
\underbrace{2,\ldots,2}_{d},
\underbrace{1,\ldots,1}_{n},
\underbrace{0,\ldots,0}_{k}.
\tag{15}
\]

The classical Hoffman--Wielandt theorem for Hermitian matrices gives

\[
\boxed{
\sum_{i=1}^{d}(\lambda_i-2)^2
+\sum_{i=d+1}^{d+n}(\lambda_i-1)^2
+\sum_{i=d+n+1}^{D_W}\lambda_i^2
\le
\|\mathcal A_F-\mathcal D\|_{HS}^2
\le\Delta.
}
\tag{16}
\]

Consequently, if a sequence of finite Lamzouri configurations satisfies

\[
\Delta=o(N),
\tag{17}
\]

then its complete tensor spectrum is `o(N)` in squared distance from the quantized `2/1/0` pattern with the **correct block multiplicities**. For every fixed `epsilon>0`, at most

\[
\frac{\Delta}{\epsilon^2}
\tag{18}
\]

eigenvalues can be `epsilon`-far from their corresponding target cluster. A near-extremizer therefore cannot merely arrange the diagonal coefficients correctly while hiding large off-diagonal tensor mass: both effects are controlled simultaneously by (A).

The Hoffman--Wielandt inequality is classical matrix perturbation theory: A. J. Hoffman and H. W. Wielandt, *The variation of the spectrum of a normal matrix*, Duke Math. J. 20 (1953), 37--39. No novelty is claimed for that theorem or for Hilbert--Schmidt/Parseval identities.

## 5. Negative spectral mass is quantitatively charged

Because `\mathcal D\succeq0`, (A) immediately controls the negative part of `\mathcal A_F`. If `\mathcal A_{F,-}` denotes the negative spectral part, then the positive-semidefinite cone is closed in Hilbert--Schmidt norm and

\[
\|\mathcal A_{F,-}\|_{HS}^2
=\operatorname{dist}_{HS}(\mathcal A_F,\mathrm{PSD})^2
\le\|\mathcal A_F-\mathcal D\|_{HS}^2.
\]

Therefore

\[
\boxed{
\sum_{\lambda_i<0}\lambda_i^2
\le\Delta.
}
\tag{19}
\]

This is a quantitative inertia statement, but it is deliberately weaker than a count of off-line zeros. A matrix may have many tiny negative eigenvalues while the square mass in (19) is small. Thus (19) does **not** turn Lamzouri's theorem into RH, and it does not identify the uncertified complement with negative inertia.

What it does is isolate the missing bootstrap obligation sharply: a positive-density off-line population can coexist with near saturation only if its negative spectral directions collapse toward zero while the full operator simultaneously approaches the target `2/1/0` spectrum. Any independent arithmetic or local-geometry theorem that gives a lower bound on a positive-density portion of those negative eigenvalue magnitudes would feed directly into `\Delta`.

## 6. The exceptional populations remain separated

Substituting WI-126's exact formula for `B` gives (B), with

\[
S_1=\sum_{x\in R_1}\|P_Uf_x\|^2,
\qquad
E_{\mathbb R}=\sum_{x\in R_2}(m_x-2),
\]

\[
E_{\mathbb C}=\sum_{z\in Z_+}(m_z-1),
\qquad
H_U=\sum_{z\in Z_+}m_z\|P_{U^\perp}h_z\|^2.
\tag{20}
\]

Hence a near-sharp sequence must satisfy simultaneously

\[
\|\mathcal A_F-(P_U+P_V)\|_{HS}^2=o(N),
\quad S_1=o(N),
\quad E_{\mathbb R}=o(N),
\quad E_{\mathbb C}=o(N),
\quad H_U=o(N).
\tag{21}
\]

This preserves the mandate's distinction between exceptional mechanisms. Real doubles remain genuinely free: a configuration containing only simple real points and real doubles can attain the exact `1/2` target eigenvalues on the corresponding `M/U` directions. Higher critical-line multiplicity is separately charged by `E_R`. Off-line multiplicity is charged by `E_C`, while even a simple off-line pair must make its odd direction almost representable by `U` and its tensor contribution spectrally collapse toward the zero block. Pure proof slack is retained in the Hilbert--Schmidt term rather than being relabelled as off-line mass.

For the two one-point equality controls, the identity is exact. A single simple real point has `\mathcal A_F=P_V` and `\Delta=0`; a single real double has `\mathcal A_F=2P_U` and `\Delta=0`. This matches Lamzouri's finite inequality and WI-126. A finite non-real pair cannot attain equality because `H_U>0` by linear independence, again matching WI-126.

## 7. Relation to WI-136 and the Schur frontier

WI-136's strongest new information is that off-line odd directions must approach the smaller exceptional span `U`, not the larger retained span `V`. The present finding does not replace that geometric statement. Instead it shows that it is only one component of a stronger simultaneous rigidity package.

The `U`-projection charge in WI-136 is contained in `2B`, while the operator distance in (A) additionally retains:

- the complete off-diagonal Bessel mass `R_B`;
- the variance of the `U` diagonal coefficients around their required value `2`;
- the full middle-block deviation from coefficient `1`;
- the quadratic part of the horizontal-block coefficients.

Those quantities were all nonnegative in WI-126 but had not been assembled into one canonical spectral object. In particular, a countermodel that self-screens the normalized odd Schur family from WI-136 is still not a near-extremizer unless it also makes the **entire** tensor operator close to `P_U+P_V`.

This gives a second way to attack the remaining defect-to-zero problem. The current Schur program asks whether a positive-density off-line family can make its odd directions almost lie in the exceptional span `U`. The operator formulation adds a compatibility test: can that same family simultaneously quantize the full Lamzouri tensor spectrum to `2/1/0` while respecting zeta-accessible local-density and correlation constraints? A proof that one of these two requirements forces extensive slack would improve the baseline; an explicit zeta-count-compatible construction satisfying both would be a decisive no-go for this bootstrap architecture.

## 8. Prior-art and novelty audit

The literature-backed inputs are Lamzouri's Proposition 2.1, its `g/h` decomposition, nested spaces and diagonal coefficient inequalities; the public `AxiomMath/ZetaZeros` project independently formalizes the published finite proposition and its real-coefficient infrastructure. WI-126 supplies the exact four-remainder reconstruction, and WI-136 supplies the exact `B` expansion and the stronger `U`-projection interpretation. Parseval, real symmetric tensor/operator identification, Hilbert--Schmidt norm algebra and Hoffman--Wielandt are classical.

A targeted audit of Lamzouri's preprint and current public discussions/formalization, together with searches for equality/stability, Hilbert--Schmidt, operator-distance and spectral-quantization refinements of Proposition 2.1, did not locate an external statement of (A), (B), or the `2/1/0` near-spectrum consequence (16). Absence from those searches is not evidence of priority and no priority claim is made. The durable Mathia deduction is only the exact recombination of already established Lamzouri/WI-126 coefficients into the canonical operator distance and the resulting near-extremizer constraint.

## 9. Research implication

The Lamzouri route now has a stricter falsification target than scalar horizontal transversality. Any asymptotic configuration that keeps the present lower bound nearly sharp must simultaneously satisfy

\[
\mathcal A_F\approx P_U+P_V
\quad\text{in Hilbert--Schmidt density},
\]

while off-line odd directions approach `U` and multiplicity excess vanishes. Equivalently, the whole finite tensor must become spectrally almost integer-valued with prescribed multiplicities `2/1/0`.

The next high-value test is therefore to look for a zeta-accessible invariant that obstructs this quantization: a trace/mixed-moment of `\mathcal A_F` not already determined by `N` and `Q`, a principal-minor or determinant lower bound on the negative/zero block, or a local-density/correlation constraint forcing a positive-density spectral tail away from `{0,1,2}`. Such an invariant would couple directly to the exact slack instead of merely re-estimating the same pair-correlation scalar. Conversely, a screened model satisfying both the `U`-Schur condition and the `2/1/0` tensor quantization would close a substantial branch of the present bootstrap program.