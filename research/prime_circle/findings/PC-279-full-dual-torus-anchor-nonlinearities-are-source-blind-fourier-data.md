# PC-279 — full dual-torus anchor nonlinearities are source-blind Fourier data

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the source-dependent-mask / anchor-sensitive nonlinear escape left open by PC-278.

PC-278 proves that the raw two-dimensional phase window

\[
(h,k)\longmapsto \zeta_q^{hp+kr}
\]

is diagonal-unitary pure gauge whenever a source-independent mask or Hermitian kernel is spectralized. It correctly leaves open nonlinear anchoring to the distinguished phase `1`, including threshold masks selected from the source phases. Such a mask really does break the diagonal phase gauge on a truncated coefficient window. However, on the **complete coefficient torus** the source dependence disappears again for a different and stronger reason: multiplication by the source coordinates is only a permutation of the cyclic indices.

Let `q` be prime, let `p,r in (Z/qZ)^x`, and let

\[
f:\mathbb Z/q\mathbb Z\to\mathbb C
\]

be completely arbitrary. It may be discontinuous, nonlinear, thresholded, singular at selected residues, or obtained by applying any pointwise nonlinear function to the anchored phase `\zeta_q^t`. Define the full dual-torus matrix

\[
M_{p,r}^{f}(h,k):=f(hp+kr),
\qquad h,k\in\mathbb Z/q\mathbb Z.
\tag{1}
\]

Then there are permutation matrices `P_p,Q_r` such that

\[
\boxed{
M_{p,r}^{f}=P_p\,M_{1,1}^{f}\,Q_r.
}
\tag{2}
\]

Consequently every singular value, rank, Schatten norm, operator norm, Gram spectrum, and singular-value determinant of `M_{p,r}^{f}` is exactly independent of `(p,r)`. More strongly, if

\[
\widehat f(j):=\sum_{t\bmod q}f(t)\zeta_q^{-jt},
\tag{3}
\]

then

\[
\boxed{
\operatorname{SingSpec}(M_{p,r}^{f})
=
\{\,|\widehat f(j)|:j\bmod q\,\}
}
\tag{4}
\]

with multiplicity. Thus the complete positive spectral data are not merely source-blind: they are exactly the one-dimensional discrete Fourier magnitudes of the scalar profile `f`.

This closes the most symmetric version of the PC-278 source-dependent-mask escape. A full two-dimensional anchored nonlinear spectral wrapper does not create a new Prime-Circle carrier. Any source information in this family must come from **breaking the complete-torus permutation symmetry before spectral compression**, for example by a truncated coefficient window, a non-invariant boundary, a source-coupled second level, or another structure that is not a function of `hp+kr` alone.

## 1. Exact permutation collapse

Because `p` and `r` are units modulo the prime `q`, the maps

\[
h\mapsto hp,
\qquad
k\mapsto kr
\tag{5}
\]

are permutations of `Z/qZ`. Reindexing the rows by `a=hp` and the columns by `b=kr` gives

\[
M_{p,r}^{f}(h,k)=f(a+b).
\tag{6}
\]

The right-hand side is exactly the `(a,b)` entry of `M_{1,1}^{f}`. This proves (2) without any assumption on `f`.

The prime hypothesis is stronger than necessary: the same statement holds for arbitrary modulus `q` whenever both source coordinates are units modulo `q`. The prime formulation is the one relevant to the current upper-shell near-resonance setting.

Equation (2) is a matched-control statement stronger than asymptotic equidistribution. Prime sources, composite units, random units, or any two admissible source pairs are exactly singular-isospectral at each finite `q` once the complete coefficient torus is used.

## 2. The whole singular spectrum is a one-dimensional Fourier transform

Put

\[
N_f(a,b):=f(a+b).
\tag{7}
\]

Let

\[
v_j(b):=q^{-1/2}\zeta_q^{jb},
\qquad j\bmod q.
\tag{8}
\]

Then, with `t=a+b`,

\[
\begin{aligned}
(N_fv_j)(a)
&=q^{-1/2}\sum_{b\bmod q}f(a+b)\zeta_q^{jb}\\
&=q^{-1/2}\zeta_q^{-ja}
\sum_{t\bmod q}f(t)\zeta_q^{jt}.
\end{aligned}
\tag{9}
\]

Thus `N_f` sends the Fourier mode `v_j` to the opposite mode `v_{-j}` multiplied by `\widehat f(-j)`. Therefore

\[
N_f^*N_f\,v_j
=|\widehat f(-j)|^2v_j,
\tag{10}
\]

which proves (4). Equivalently, `N_f` is a cyclic convolution matrix composed with the reversal permutation; its positive spectrum is the ordinary circulant Fourier spectrum.

The apparent two-dimensionality is therefore rank-one at the level of the phase coordinate: the matrix samples only the scalar linear form `hp+kr`, and completing both coefficient axes allows the two source multiplications to be removed by permutations.

## 3. Source-selected near-resonance masks become universal Dirichlet spectra

Take an integer `T` with `0<=T<(q-1)/2` and define the anchored threshold profile

\[
f_T(t)
:=\mathbf 1_{\{\min(t,q-t)\le T\}}.
\tag{11}
\]

Then `M_{p,r}^{f_T}` is exactly the bipartite incidence matrix selecting all coefficient pairs whose phase lies within the fixed arc of radius `T/q` around the anchor `1`. This is precisely a source-dependent mask of the type excluded from PC-278's fixed-mask theorem.

Nevertheless its singular values are source-independent by (2), and (4) gives them explicitly. For `j\ne0`,

\[
\widehat f_T(j)
=
\sum_{t=-T}^{T}\zeta_q^{-jt}
=
\frac{\sin((2T+1)\pi j/q)}{\sin(\pi j/q)},
\tag{12}
\]

while `\widehat f_T(0)=2T+1`. Hence

\[
\boxed{
\operatorname{Spec}\bigl((M_{p,r}^{f_T})^*M_{p,r}^{f_T}\bigr)
=
\left\{
\left|
\frac{\sin((2T+1)\pi j/q)}{\sin(\pi j/q)}
\right|^2
:j\bmod q
\right\},
}
\tag{13}
\]

with the continuous value `(2T+1)^2` at `j=0`.

The same conclusion holds if one keeps the complex phase on the selected entries,

\[
f_T^{\mathrm{phase}}(t)=f_T(t)\zeta_q^t.
\tag{14}
\]

Multiplication by `\zeta_q^t` merely shifts the Fourier index, so the singular-value multiset is again exactly (13). The nonlinear selection can therefore be real and genuinely source-dependent entry by entry, while its complete full-torus positive spectrum remains universal.

## 4. A genuinely two-dimensional nonlocal kernel collapses as well

The same mechanism has a square Hermitian/nonlocal form on the coefficient torus `G_q=(Z/qZ)^2`. Let `s=(p,r)\ne0` and define

\[
K_s(u,v):=\kappa((u-v)\cdot s),
\qquad u,v\in G_q,
\tag{15}
\]

where `\kappa(-t)=\overline{\kappa(t)}` so that `K_s` is Hermitian. This kernel may be long-range and couples every pair of coefficient vertices, but it depends on the source only through the anchored scalar phase difference.

The Fourier character `\chi_\xi(u)=q^{-1}\zeta_q^{\xi\cdot u}` is an eigenvector. Summing first over the kernel of the linear form `w\mapsto w\cdot s` gives zero unless `\xi` lies in the one-dimensional span of `s`. For `\xi=js`,

\[
\boxed{
K_s\chi_{js}
=q\,\widehat\kappa(j)\chi_{js},
}
\tag{16}
\]

whereas all `q^2-q` characters transverse to `s` have eigenvalue zero. Therefore

\[
\boxed{
\operatorname{Spec}(K_s)
=
\{q\widehat\kappa(j):j\bmod q\}
\cup
\{0\}^{q^2-q},
}
\tag{17}
\]

independently of the source direction `s`.

So even a complete two-dimensional nonlocal Hermitian operator does not evade the collapse if its source dependence is only through the single linear phase coordinate. It is a rank-`<=q` one-dimensional cyclic convolution embedded in a `q^2`-dimensional space.

## 5. What actually carries the information in the surviving near-resonance branch

PC-272 proves that a **truncated** dual window can retain ordered source placement, and PC-273--PC-277 study how much of that survives matched controls after scalar compression. Equations (2)--(17) identify why truncation matters structurally.

On the complete coefficient torus, multiplication by `p` and `r` simply relabels the two axes, so anchored nonlinear phase profiles are universal. A box such as

\[
|h|,|k|\le B<q/2
\tag{18}
\]

is not preserved by those multiplicative permutations. Restricting `M_{p,r}^f` to that box therefore converts a pure relabeling into a source-dependent **boundary/intersection problem**. The surviving information is not in the local nonlinear profile `f` itself; it is in how the source-permuted level sets of `hp+kr` cut a distinguished finite window.

This sharpens the PC-278 boundary. “Use a source-dependent threshold mask” is not by itself a new mechanism. The only information gain comes from the additional structure that prevents the source permutation from being quotiented out. In the present dual-window branch that structure is the chosen truncation/window geometry.

## 6. Prior-art and novelty audit

The abstract linear algebra is classical. Cyclic convolution matrices are diagonalized by the discrete Fourier transform; a matrix with entries `f(a+b)` differs from a circulant convolution matrix only by a reversal permutation, so its singular values are the moduli of the Fourier coefficients. A standard reference is Robert M. Gray, **Toeplitz and Circulant Matrices: A Review**, *Foundations and Trends in Communications and Information Theory* 2:3 (2006), 155--239, DOI `10.1561/0100000006`, which reviews the Fourier diagonalization of circulant matrices. The threshold formula (12) is the classical Dirichlet-kernel / periodic-sinc identity.

A targeted prior-art check against circulant and reverse-circulant matrices, finite cyclic convolution, discrete Fourier singular spectra, and Dirichlet kernels found exactly this standard framework. No novelty is claimed for those ingredients. The proof here is deliberately elementary and does not depend on an absence-of-literature claim.

The project-local content is the exact specialization to the Prime-Circle dual-window escape left open by PC-278: **even after nonlinear anchoring or source-selected thresholding, completing the coefficient torus makes every admissible source pair permutation-equivalent, and the seemingly two-dimensional positive spectrum reduces to one scalar Fourier profile.** This identifies the finite-window boundary mismatch, rather than the anchored phase nonlinearity itself, as the only source of information in this class.

Because the external ingredient is only standard Fourier/circulant background and the complete argument is contained above, no new durable literature dependency is required in `SOURCES.md`.

## 7. Falsification and audit tests

The theorem has exact finite checks.

1. For any prime `q`, units `p,r`, and arbitrary table of values `f(t)`, explicitly reorder rows by `h->hp` and columns by `k->kr`. The resulting matrix must equal `M_{1,1}^f` entry by entry.
2. Compute the singular values of `M_{p,r}^f` for several source pairs and compare them with `|\widehat f(j)|`. Any mismatch falsifies (2) or (4).
3. For the threshold profile (11), compare the singular values against the Dirichlet-kernel values (12). The result must be independent of whether `(p,r)` are prime residues or arbitrary units.
4. For the nonlocal kernel (15), verify rank at most `q`, the `q^2-q` exact zero modes, and the nonzero eigenvalues in (17).
5. Restrict to a non-invariant window such as (18). Source dependence may then appear and is outside the theorem; treating such a counterexample as a failure of (2) would silently change the coefficient domain.

Small exact/numerical controls at `q=5,7,11` with the arc mask `T=1` reproduce (4) to machine precision for every unit source pair and give the predicted Dirichlet-kernel singular values.

## 8. Consequences for the research line

The route

\[
\text{full dual coefficient torus}
\longrightarrow
\text{arbitrary anchored pointwise nonlinearity }f(hp+kr)
\longrightarrow
\text{positive / singular spectralization}
\longrightarrow
\text{new Prime-Circle or RH carrier}
\tag{19}
\]

is closed exactly.

The same is true for the full translation-invariant two-dimensional Hermitian kernel (15): it is a source-blind one-dimensional Fourier packet with a large exact nullspace. Thus neither completing the dual window nor adding a nonlocal kernel of the scalar phase difference rescues the PC-278 spectral route.

What survives is more specific than before: truncated/windowed anchor nonlinearities whose boundary is not invariant under the source permutations; genuinely non-separable coefficient-graph flux; or relative/cross-source and cross-level constructions in which no single relabeling removes all source data. In particular, future work on the intermediate rational-microscopic window should treat the **window/source mismatch itself** as the candidate carrier and continue to test it against the Li-weighted rational controls of PC-277 rather than attributing information to the phase nonlinearity or its full-torus spectrum.