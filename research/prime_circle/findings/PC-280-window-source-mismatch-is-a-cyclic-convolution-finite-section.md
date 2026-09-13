# PC-280 — window/source mismatch is a cyclic-convolution finite section

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the truncated/windowed anchor-nonlinearity escape left open by PC-279.

PC-279 proves that on the complete coefficient torus every anchored pointwise nonlinearity

\[
(h,k)\longmapsto f(hp+kr)
\]

is source-blind at the level of singular/positive spectral data: multiplication by the source coordinates merely permutes the full row and column sets. It leaves a specific escape open. If the coefficient domain is truncated to a non-invariant window, those multiplicative permutations no longer preserve the window, so source dependence can survive.

That surviving object admits an exact classification. For a symmetric coefficient window

\[
H_B:=\{-B,-B+1,\ldots,B\}\subset \mathbb Z/q\mathbb Z,
\qquad N:=2B+1\le q,
\]

an odd prime `q`, units `p,r mod q`, and an arbitrary profile `f:Z/qZ -> C`, define

\[
M_{p,r;B}^{f}(h,k):=f(ph+rk),
\qquad h,k\in H_B.
\tag{1}
\]

Then `M_{p,r;B}^f` is, up to row/column permutations, exactly a two-sided finite section of **one source-independent cyclic convolution operator**. If

\[
(C_f x)(a):=\sum_{b\bmod q}f(a-b)x(b),
\tag{2}
\]

and `E_A` denotes restriction from `l^2(Z/qZ)` to a subset `A`, then

\[
\boxed{
M_{p,r;B}^{f}
\simeq
E_{pH_B}\,C_f\,E_{rH_B}^{*}.
}
\tag{3}
\]

Thus the source pair does not create a new symbol, kernel, or two-dimensional phase operator. **All surviving source information is in the placement of the two dilated windows `pH_B` and `rH_B` inside the fixed cyclic convolution operator.**

After Fourier diagonalization this becomes an exact weighted concentration problem. With the unnormalized finite Fourier transform

\[
\widehat f(j):=\sum_{t\bmod q}f(t)e^{-2\pi ijt/q},
\tag{4}
\]

let `D_f=diag(hat f(j))`, let `F` be the unitary DFT, and define the rank-`N` projections

\[
P_{p,B}:=FQ_{pH_B}F^*,
\qquad
P_{r,B}:=FQ_{rH_B}F^*,
\tag{5}
\]

where `Q_A` is coordinate projection onto `A`. Then the complete singular spectrum of (1) is exactly the singular spectrum of

\[
\boxed{
P_{p,B}D_fP_{r,B}:
\operatorname{Ran}P_{r,B}\to\operatorname{Ran}P_{p,B}.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
\sigma_j(M_{p,r;B}^{f})^2
=
\lambda_j\!\left(
P_{r,B}D_f^*P_{p,B}D_fP_{r,B}
\big|_{\operatorname{Ran}P_{r,B}}
\right).
}
\tag{7}
\]

For the interval window the projection kernels are explicit Dirichlet kernels,

\[
\boxed{
P_{p,B}(j,\ell)
=
\frac1q\sum_{h=-B}^{B}
 e^{2\pi i(\ell-j)ph/q}.
}
\tag{8}
\]

So the truncated positive spectral branch left open by PC-279 is not an unknown two-dimensional operator family. It is a source-dilated finite-section/concentration problem for a fixed scalar Fourier multiplier. This does **not** make the finite-window spectrum source-blind; it identifies exactly where its source dependence lives.

## 1. Exact finite-section reduction

Put

\[
A:=pH_B,
\qquad
B':=rH_B.
\]

Because `p` and `r` are units modulo `q`, the maps `h -> ph` and `k -> rk` are bijections from `H_B` to `A` and `B'`. Since `H_B=-H_B`, also `B'=-B'`.

Reflect the column coordinate by `k -> -k`, which is a permutation of `H_B`. Equation (1) becomes

\[
M_{p,r;B}^{f}(h,-k)=f(ph-rk).
\tag{9}
\]

Now reindex rows by `a=ph in A` and columns by `b=rk in B'`. The resulting matrix has entries

\[
f(a-b),
\qquad a\in A,\ b\in B',
\tag{10}
\]

which are precisely the entries of the submatrix `E_A C_f E_{B'}^*`. This proves (3). No regularity, positivity, symmetry, or linearity assumption on `f` is required.

The important distinction from PC-279 is now exact. On the full torus, `A=B'=Z/qZ`, so both restrictions disappear and source multiplication is only a relabelling. On a proper window, the fixed operator `C_f` is sampled on two source-dependent subsets. The information carrier is therefore the **mismatch between the multiplicative source action and the chosen additive window**, not the pointwise anchor profile by itself.

## 2. Fourier representation as a two-sided concentration operator

The cyclic convolution operator is diagonalized by the DFT:

\[
C_f=F^*D_fF.
\tag{11}
\]

Let

\[
U_{p,B}:=E_{pH_B}F^*,
\qquad
U_{r,B}:=E_{rH_B}F^*.
\tag{12}
\]

These are coisometries:

\[
U_{p,B}U_{p,B}^*=I_N,
\qquad
U_{p,B}^*U_{p,B}=P_{p,B},
\tag{13}
\]

and likewise for `r`. Therefore (3) gives

\[
M_{p,r;B}^{f}
\simeq
U_{p,B}D_fU_{r,B}^*.
\tag{14}
\]

Restricting `U_{p,B}` and `U_{r,B}` to the ranges of their projections makes them unitary maps onto the two `N`-dimensional window spaces. Hence (14) is unitarily equivalent to the two-sided compression (6), and its positive Gram operator is (7).

For `A=pH_B`, direct multiplication gives

\[
P_{p,B}(j,\ell)
=
\frac1q\sum_{a\in pH_B}
 e^{2\pi i(\ell-j)a/q}
=
\frac1q\sum_{h=-B}^{B}
 e^{2\pi i(\ell-j)ph/q},
\]

which is (8). Thus every dependence on `p` and `r` in the positive spectrum is carried by two explicit rank-`N` Dirichlet-kernel projections surrounding the **same** diagonal multiplier `D_f`.

This is a useful separation of responsibilities. The nonlinear anchor choice selects the Fourier multiplier; the prime source selects where the finite window sits after multiplicative dilation. Neither operation manufactures an additional spectral variable.

## 3. Exact controls expose what can and cannot survive

Several extreme profiles give sharp finite controls.

### Complete torus

If `H_B=Z/qZ`, then

\[
P_{p,B}=P_{r,B}=I
\]

for every source pair, and (6) reduces to `D_f`. Hence

\[
\operatorname{SingSpec}M_{p,r}^{f}
=
\{|\widehat f(j)|:j\bmod q\},
\tag{15}
\]

recovering PC-279 exactly.

### Pure phase

Take

\[
f(t)=e^{2\pi ict/q}.
\]

Then `D_f` has one nonzero diagonal entry, equal to `q`. Consequently every finite-window matrix is rank one. Since every entry of (1) has modulus one and the phase separates into a row factor and a column factor, its unique nonzero singular value is exactly

\[
\boxed{N,}
\tag{16}
\]

independently of `(p,r)`. This recovers the fixed-mask pure-gauge obstruction of PC-278 inside the finite-section representation.

### Exact anchor selector

Take the sharpest possible anchored profile,

\[
f(t)=\mathbf 1_{\{0\}}(t).
\tag{17}
\]

Then `C_f=I`. After the column reflection, `M` is the incidence matrix for equality between the two sampled sets `pH_B` and `rH_B`. Hence

\[
\boxed{
\operatorname{SingSpec}M_{p,r;B}^{f}
=
\{1\}^{|pH_B\cap rH_B|}
\cup
\{0\}^{N-|pH_B\cap rH_B|}.
}
\tag{18}
\]

So even an absolute, maximally nonlinear anchor test reduces to a finite set-intersection statistic. The source dependence can be real, but in this limit it is purely the combinatorics of two multiplicatively dilated windows.

### Fourier-support rank bound

For arbitrary `f`,

\[
\boxed{
\operatorname{rank}M_{p,r;B}^{f}
\le
\min\bigl(N,|\operatorname{supp}\widehat f|\bigr).
}
\tag{19}
\]

Thus a profile with bounded Fourier support cannot generate an extensive new spectral carrier merely through source-dependent truncation. Extensive singular structure requires a multiplier with correspondingly growing Fourier support.

### First positive moment

Equation (3) also gives

\[
\boxed{
\|M_{p,r;B}^{f}\|_F^2
=
\sum_{a\in pH_B}\sum_{b\in rH_B}|f(a-b)|^2.
}
\tag{20}
\]

Equivalently it is the profile `|f|^2` tested against the difference-multiplicity function of the two dilated windows. The first singular moment therefore contains no hidden operator information beyond additive overlap counts. Higher moments and the full singular spectrum can retain more ordering information through repeated alternation of the two projections, so (20) is a boundary rather than a no-go for the complete finite-section spectrum.

## 4. Threshold masks become weighted prolate-type finite sections

For the anchored near-resonance threshold

\[
f_T(t):=
\mathbf 1_{\{\min(t,q-t)\le T\}},
\tag{21}
\]

PC-279 showed that the **full-torus** singular spectrum is the universal Dirichlet-kernel spectrum. In the present finite window, `D_{f_T}` is still exactly that same diagonal Dirichlet multiplier, but it is now sandwiched between `P_{p,B}` and `P_{r,B}`:

\[
P_{p,B}D_{f_T}P_{r,B}.
\tag{22}
\]

The source information is therefore not in a new threshold symbol. It is in the relative position of three classical finite objects: a source-dilated window projection, a fixed Fourier multiplier, and a second source-dilated window projection.

This is structurally the same time/frequency-limiting architecture that underlies discrete prolate/Slepian concentration problems, although the Prime-Circle specialization uses modular arithmetic-progression windows `pH_B,rH_B` and an arbitrary cyclotomic/anchor multiplier rather than the standard contiguous time window plus contiguous frequency band. The analogy is useful precisely because it prevents attributing novelty to the compression architecture itself.

It also clarifies a false escape. Making the pointwise anchor profile increasingly complicated does not by itself add source information: `D_f` remains source-independent. To obtain a genuinely new carrier inside this family one must prove that the **arithmetic placement of the two finite-section projections** has a property not reproduced by appropriate non-prime controls.

## 5. Relation to the normalized near-resonance frontier

PC-277 already shows that the normalized scalar near-resonance law is reproduced by a Li-weighted denominator-`q` rational control throughout every bandwidth satisfying

\[
\log B=o(\sqrt{\log q}),
\]

and that every denominator-`q` source collapses to exact resonance once `(B+1)^2>q`. PC-280 does not evade those matched controls by replacing the scalar minimum with a singular spectrum.

Instead it identifies the extra information retained before scalar compression. The matrix-level survivor is the pair

\[
(P_{p,B},P_{r,B})
\]

relative to the fixed multiplier `D_f`. Any RH-facing use of (7) must therefore show that some spectral statistic of this relative projection geometry distinguishes the actual prime source from a control preserving the smooth `Li` source bias and denominator-`q` geometry. A prime-versus-uniform discrepancy is still insufficient for exactly the reason isolated in PC-277.

The intermediate rational-microscopic bandwidth window remains open. What has changed is that its positive spectral problem is now sharply formulated: it is not an unspecified two-dimensional nonlinear operator problem but a family of arithmetic finite sections of one cyclic convolution operator.

## 6. Prior-art and novelty audit

The abstract operator architecture is classical. Finite time/frequency concentration operators and their discrete prolate spheroidal sequences go back to David Slepian, **Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case**, *Bell System Technical Journal* 57:5 (1978), 1371–1430, DOI `10.1002/j.1538-7305.1978.tb02104.x`. Modern work on Fourier submatrices, for example Simon Dirckx, Daan Huybrechs and Robbe Ongenae, **On the Computation of the SVD of Fourier Submatrices**, *Journal of Scientific Computing* 95 (2023), article 68, DOI `10.1007/s10915-023-02171-z`, studies the periodic discrete-prolate singular structure of finite Fourier sections. Partial/nonuniform Fourier matrices and their singular conditioning are likewise an established subject.

No novelty is claimed for cyclic-convolution diagonalization, two-sided compression, Dirichlet-kernel projections, Slepian concentration, or Fourier-submatrix singular values. The exact proof of (3)–(8) is elementary and self-contained, so these references are neighboring prior art rather than load-bearing theorem dependencies; no new `SOURCES.md` anchor is required.

The project-local mathematical delta is narrower and exact. PC-279 identified the non-invariant window as the place where source information could survive but did not classify the resulting operator. PC-280 shows that **all** truncated anchored pointwise profiles of the form `f(ph+rk)` factor through a fixed cyclic convolution operator with source dependence only in two multiplicatively dilated finite-section projections. This rules out treating the surviving branch as a new source-dependent symbol or intrinsically two-dimensional spectral operator while preserving the possibility that the arithmetic finite-section placement itself carries useful information.

A targeted novelty search against discrete Slepian/prolate concentration, Fourier submatrices, partial Fourier matrices, and finite cyclic convolution found the expected general compression framework. No independent literature mechanism was found that turns these particular prime-dilated windows into a new RH criterion; absence of such a result is not used as evidence of novelty.

## 7. Boundaries and failure modes

The theorem applies to one source pair, a rectangular symmetric coefficient window, and pointwise profiles depending on the single phase coordinate `ph+rk`. It deliberately does **not** claim source blindness of the finite-section spectrum.

It does not cover:

- genuinely non-separable coefficient-graph flux that is not a function of one linear phase coordinate;
- cross-source or cross-level operators in which no single pair of finite-section projections captures all inputs;
- source-dependent profiles `f_{p,r}` containing information beyond evaluation of a fixed anchored function on `ph+rk`;
- nonlinear operations performed on the compressed operator itself that are not spectral functions of the same finite section;
- coefficient domains whose geometry carries additional structure not reducible to row/column restriction.

The usual near-resonance convention that removes only the coefficient pair `(0,0)` from a rectangular box does not create a qualitatively different operator family: zeroing that single matrix entry is a source-independent rank-one perturbation of (1). It can change individual finite singular values, but it does not change the identification of the extensive source dependence with the window/convolution finite section.

Most importantly, source dependence is not yet arithmetic discrimination. Even a strongly varying spectrum along prime pairs is not RH evidence unless matched non-prime controls fail in the topology and normalization needed by the proposed implication.

## 8. Falsification and audit tests

The classification has direct finite checks.

1. For any prime `q`, units `p,r`, window `H_B`, and arbitrary table `f`, reflect the columns and relabel rows by `a=ph`, columns by `b=rk`. The resulting matrix must equal the submatrix `C_f[pH_B,rH_B]` entry by entry.
2. Diagonalize the full circulant `C_f` by the unitary DFT and compare the singular values of the finite section with those of (6). Any mismatch falsifies the Fourier compression claim.
3. For `f(t)=exp(2 pi i c t/q)`, the finite matrix must have rank one and unique singular value `N` for every source pair.
4. For `f=1_{0}`, the rank must equal `|pH_B intersect rH_B|`, with every nonzero singular value exactly one.
5. For any `f`, the rank must satisfy (19). A matrix rank larger than the Fourier support of `f` would contradict (11).
6. Setting `H_B=Z/qZ` must remove both projections and recover the full-torus Fourier singular spectrum of PC-279.
7. A source-dependent singular spectrum in a proper window is **not** a counterexample; it is exactly the behavior allowed by the source-dependent projections. A counterexample would require dependence not representable through those two projections and the fixed `D_f`.

Finite numerical checks at small prime `q` with arbitrary complex profiles reproduce (3), (6), and the controls above to machine precision, but the stored claim does not rely on numerics.

## 9. Consequence for the research line

The surviving positive spectral route after PC-278/PC-279 can now be stated without ambiguity:

\[
\boxed{
\text{Prime-Circle source}
\to
\text{multiplicatively dilated coefficient windows}
\to
\text{finite section of a fixed cyclic convolution}
\to
\text{singular/concentration spectrum}.
}
\]

The anchor nonlinearity supplies only the fixed multiplier `D_f`; the arithmetic source supplies only the two finite-section projections. Therefore future work in this branch should not search for a hidden zeta mechanism in the full phase symbol or in generic positive spectralization. It should test whether the **relative finite-section placement** has a source-specific mesoscopic law that survives the Li-weighted rational controls of PC-277, or else move to genuinely cross-level/non-separable constructions where this two-projection factorization no longer applies.
