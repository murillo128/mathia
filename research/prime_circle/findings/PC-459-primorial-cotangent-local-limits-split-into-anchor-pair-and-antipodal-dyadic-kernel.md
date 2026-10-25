# PC-459 — Primorial cotangent local limits split into an anchor pair and an antipodal dyadic kernel

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE. In the explicitly defined conductor-mesh embedding, the primorial complete-tube cotangent operators converge strongly near the common anchor to a rank-two operator. Near its antipode they instead converge, along odd refinements, to an infinite-rank trace-class Cauchy operator on the signed positive powers of two. Even refinements recover the rank-two limit. Neither local limit is an operator-norm limit of the full matrices. This supplies common-space local limits and surviving spectral points beyond PC-458's empirical collapse, but no zeta-zero identification or RH implication.

## 1. The embedding is part of the statement

Let
\[
d_y=\prod_{p\le y}p,\qquad m_y\ge1,\qquad N_y=d_y m_y,
\qquad Y_y=\{a\bmod N_y:(a,d_y)=1\}.
\]
Here `y -> infinity`, and refinement depth is otherwise arbitrary. On `Y_y` use the raw and augmented matrices of [[research/prime_circle/findings/PC-458-conductor-scaled-cotangent-bulk-collapses-exactly-at-vanishing-primitive-density]]:
\[
C_{ab}=i\cot\frac{\pi(a-b)}{N_y}\quad(a\ne b),\qquad C_{aa}=0,
\qquad T_y=C/N_y,\quad T_y^+=(C+J)/N_y.
\tag{1}
\]
Use counting measure, equivalently the orthonormal coordinate basis of uniform probability measure. Let
\[
I_N=\{-N/2,-N/2+1,\ldots,N/2-1\}.
\]
For a center `c=0` or `c=N/2`, map the coordinate for `a` to `e_h` in `ell^2(Z)`, where `h in I_N` is the representative of `a-c mod N`. Extend the embedded matrix by zero on unused coordinates, and call it `K_y^(c)` (or `K_y^(c,+)`). Explicitly, with
\[
\chi_y^{(c)}(h)=\mathbf1_{h\in I_{N_y}}\mathbf1_{(c+h,d_y)=1},
\]
its off-diagonal entries are
\[
(K_y^{(c)})_{hk}
=\chi_y^{(c)}(h)\chi_y^{(c)}(k)
  \frac{i}{N_y}\cot\frac{\pi(h-k)}{N_y}.
\tag{2}
\]
The common anchor `1` gives `c=0`; its geometrically determined antipode `-1` gives `c=N/2`. These centers need not themselves be retained vertices. The coordinate `h` measures distance in **ambient mesh units**, not fixed angular distance. This is a specified local observation, not the fixed-base profinite embedding of PC-443, and the two embeddings below are not claimed to be canonically equivalent in the limit.

For a subset `S` of the integers define, when bounded,
\[
(L_S)_{hk}=\begin{cases}
\dfrac{i}{\pi(h-k)},&h,k\in S,\ h\ne k,\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
\]
Put
\[
S_0=\{-1,1\},\qquad S_2=\{\pm2^j:j=1,2,\ldots\}.
\]
The theorem is
\[
\boxed{\begin{aligned}
K_y^{(0,(+))}&\longrightarrow L_{S_0}&&\text{strongly, for every }m_y;\\
K_y^{(N_y/2,(+))}&\longrightarrow L_{S_2}&&\text{strongly, if }m_y\text{ is odd};\\
K_y^{(N_y/2,(+))}&\longrightarrow L_{S_0}&&\text{strongly, if }m_y\text{ is even}.
\end{aligned}}
\tag{4}
\]
Parity conditions can hold eventually or on the indicated subsequence. If both parities occur infinitely often, the antipodal sequence has these two distinct subsequential strong limits and does not converge strongly.

## 2. Exact local sieve classification

At `c=0`, every fixed integer `h` other than `+1,-1` is eventually excluded: `h=0` is never a unit, and a prime divisor of any fixed `|h|>1` eventually divides `d_y`. Both units remain.

At `c=N_y/2=m_y d_y/2`, every odd prime `p<=y` divides `c`. Thus
\[
p\nmid(c+h)\quad\Longleftrightarrow\quad p\nmid h
\qquad(p\text{ odd},\ p\le y).
\tag{5}
\]
For fixed nonzero `h`, survival of all these tests forces `|h|` to be a power of two, including `2^0=1`. For `y>=3`, `h=0` is excluded by the prime `3`. Since `d_y/2` is odd, the remaining prime `2` requires
\[
h\text{ even if }m_y\text{ is odd},\qquad
h\text{ odd if }m_y\text{ is even}.
\tag{6}
\]
Equations (5)--(6) give exactly `S_2` and `S_0`. In fact the classification is already exact on `|h|<=y` once those coordinates lie in `I_N`. It uses elementary divisibility, not a distribution theorem about primes or rough numbers.

The parity distinction is observable in one matrix entry: at offsets `2,-2`, the odd-refinement limit is `i/(4 pi)`, whereas the even-refinement limit is zero. At offsets `1,-1` the opposite inclusion holds.

## 3. From local entries to strong convergence

Entrywise convergence alone is insufficient. The necessary column-tail bound comes from the unchanged cotangent kernel.

For `h,k in I_N`, let `delta_N(h-k)` be their positive circular integer distance when `h!=k`. Since `cot t <= 1/t` for `0<t<=pi/2`,
\[
\left|\frac1N\cot\frac{\pi(h-k)}N\right|
\le\frac1{\pi\delta_N(h-k)}.
\tag{7}
\]
For a fixed `k`, the chosen representatives also give
\[
\delta_N(h-k)\ge |h|-|k|.
\]
Indeed both `|h-k|` and `N-|h-k|` are at least `|h|-|k|`, using `|h|<=N/2`. Therefore, for `R>2|k|+1`, uniformly in the center, sieve and refinement,
\[
\sum_{|h|>R}|(K_y^{(c)})_{hk}|^2
\le\frac1{\pi^2}\sum_{|h|>R}\frac1{(|h|-|k|)^2}
=O(R^{-1}).
\tag{8}
\]
The same estimate holds for each limiting column of (3). On a fixed finite window, the masks stabilize by §2 and `N^{-1}cot(pi(h-k)/N) -> 1/(pi(h-k))`. Equation (8) proves convergence in `ell^2` of every column.

The full `N`-gon cotangent matrix has eigenvalues `0,N-2j` (`1<=j<N`); its augmentation replaces the constant eigenvalue by `N`. Thus the normalized principal compressions in (1) have norms at most one, as in [[research/prime_circle/findings/PC-457-growing-base-cotangent-towers-require-conductor-scale-normalization]]. This uniform bound upgrades convergence on finitely supported vectors to strong convergence on `ell^2(Z)`. It also proves boundedness of the limiting kernels.

For the augmentation, each embedded column of `J/N` has squared norm at most `N/N^2=1/N`, and the operator norm is at most one. Hence the augmentation tends strongly to zero by the same dense-subspace argument. Along primorials its operator norm is exactly `|Y_y|/N_y=varphi(d_y)/d_y -> 0`, but that stronger arithmetic fact is not needed for (4).

## 4. A rank-two limit and an infinite trace-class limit

On `span{e_1,e_-1}`, the first limit has matrix
\[
L_{S_0}=\begin{pmatrix}0&i/(2\pi)\\-i/(2\pi)&0\end{pmatrix}.
\]
Its nonzero eigenvalues are exactly `+1/(2 pi),-1/(2 pi)`.

For the dyadic limit, its matrix entries are absolutely summable. For `k>j>=1` in the first bound and all `j,k>=1` in the second,
\[
\frac1{2^k-2^j}\le2^{1-k},\qquad
\frac1{2^k+2^j}\le2^{-\max(k,j)}.
\tag{9}
\]
Summing over both signs bounds the total absolute sum by a constant times `sum_(k>=1) k 2^-k < infinity`. The expansion into coordinate rank-one operators therefore converges in trace norm: **`L_(S_2)` is trace class**.

It has infinite rank. Its block from negative to positive powers is, up to `i/pi`, the Cauchy matrix
\[
H_{jk}=\frac1{2^j+2^k},\qquad j,k\ge1.
\]
Every finite leading block is strictly positive definite, because
\[
\sum_{j,k=1}^r\overline{a_j}a_k H_{jk}
=\int_0^\infty\left|\sum_{j=1}^r a_j e^{-2^j t}\right|^2dt>0
\quad(a\ne0).
\tag{10}
\]
Distinct real exponentials are linearly independent (successively isolate the slowest decaying one as `t -> infinity`). Thus block ranks, and hence the rank of `L_(S_2)`, are unbounded.

Reflection `R e_h=e_-h` satisfies `R L_S R=-L_S` for both sets. The compact self-adjoint spectral theorem now gives infinitely many positive and negative dyadic-limit eigenvalues, counted with multiplicity, accumulating only at zero, with summable absolute values. This is a genuine infinite discrete local spectrum, but it is the spectrum of an explicit sparse Cauchy kernel, not an identified zeta spectrum.

## 5. What the limits imply for finite spectra, and what escapes them

Every nonzero eigenvalue `lambda` of a limit in (4) is approached by eigenvalues of the corresponding finite matrix (1). If `v` is its unit eigenvector, strong convergence gives
\[
\|(K_y^{(c,(+))}-\lambda)v\|\longrightarrow0,
\qquad
\operatorname{dist}(\lambda,\sigma(K_y^{(c,(+))}))
\le\|(K_y^{(c,(+))}-\lambda)v\|.
\tag{11}
\]
The inequality follows directly by expanding in an orthonormal eigenbasis of the finite block plus its zero complement. Since `lambda!=0`, the nearby spectral points eventually belong to the finite block, not the artificial zero complement. Thus the anchor pair yields two persistent nonzero spectral locations for every refinement sequence, and odd refinements additionally approximate every nonzero dyadic-limit eigenvalue. This does not establish convergence of the full finite spectrum or of individual finite eigenvectors.

**There is no operator-norm convergence to either local limit.** In the anchor-centered embedding, consider the retained pair near the opposite center `c=N/2`. If `m` is odd, the offsets `c-2,c+2` are units modulo `d_y`; if `m` is even, `c-1,c+1` are units. Their embedded coordinates escape to infinity, while their normalized off-diagonal magnitude tends respectively to
\[
\frac1{4\pi}\quad\text{or}\quad\frac1{2\pi}.
\tag{12}
\]
The limiting rank-two operator kills those coordinate columns. Consequently the lower limit of the operator-norm error is at least `1/(4 pi)`, for raw or augmented matrices. For the augmented entry use its magnitude `|csc(pi(a-b)/N)|/N`, which has the same limit.

In the antipodal embedding, the original unit residues `+1,-1` instead escape to infinity. Their mutual normalized entry tends to `1/(2 pi)`. Both possible local limits are compact, so their norms on these escaping coordinate vectors tend to zero. The operator-norm error therefore has lower limit at least `1/(2 pi)` along either parity subsequence. Thus the local limit misses persistent operator action in spatially escaping sectors; it does not provide a complete finite-spectrum limit.

There is no conflict with PC-458. Its empirical measure divides eigenvalue counts by `|Y_y|`; these local vector/spectral statements do not. A vanishing fraction of eigenvalues can retain fixed nonzero values while the empirical probability tends to `delta_0`.

## 6. Matched controls and prior-art boundary

The proof of §3 is a local-mask theorem: any subsets of the same `N`-gon with the same eventual centered membership at every fixed integer offset have the same strong limit. It requires no primality beyond determining that local membership.

For an explicit class of same-conductor, same-cardinality controls, take `m=1`. Choose radii `R_y -> infinity` with `R_y=o(varphi(d_y))` and `R_y=o(d_y)`. Keep the primitive support unchanged in the two windows of radius `R_y` about `0,d_y/2`; outside those windows, replace the remaining vertices arbitrarily, retaining the total cardinality `varphi(d_y)`. There is room to include nonprimitive vertices and change the support: the windows have `o(varphi(d_y))` points, whereas the available exterior has order `d_y`. These controls use exactly the same ambient circle, conductor, cotangent rule and dimension. They have both the anchor-pair and antipodal-dyadic strong limits by §3, even though their global supports differ. They retain the local sieve information deliberately; this is a boundary on what the local readout determines, not a claim that all arithmetic information has been removed or that their global spectra agree.

The neighboring primary literature is:

- W. Ejsmont and F. Lehner, *The Trace Method for Cotangent Sums*, **J. Combin. Theory Ser. A 177** (2021), 105324, [author manuscript](https://arxiv.org/abs/2002.06052): finite cotangent sums and self-adjoint matrix/trace methods. It does not supply this local primorial support calculation.
- Y. Belov, T. Y. Mengestie and K. Seip, *Discrete Hilbert transforms on sparse sequences*, **Proc. London Math. Soc. 103** (2011), 73--105, [DOI](https://doi.org/10.1112/plms/pdq053), [author manuscript, §1](https://arxiv.org/abs/0912.2899): classical discrete Cauchy transforms on exponentially separated sequences. Its general weighted-transform theorems are neighboring context; trace class and infinite rank here are proved directly by (9)--(10).

Directed searches covered cotangent reduced-residue/primorial local spectra, geometric Cauchy matrices and sparse discrete Hilbert transforms. These give no basis for historical novelty claims. The Cauchy expansion, strong-convergence argument, exponential Gram determinant and compact spectral consequences are classical. The local contribution is the **exact common-anchor/antipode and refinement-parity classification**, including the infinite-rank trace-class limit and the failure of norm convergence. PC-457 supplies a family norm scale and PC-458 a bulk-law criterion; neither identifies these common-space local operators. PC-099 and PC-443 hold the base fixed and use different limiting spaces/scales.

Changing coordinates is consequential here: the finite matrices in the two charts are unitarily equivalent, but their changing embeddings have inequivalent strong limits. Therefore a local compact spectrum alone cannot be promoted into an invariant global spectral law. No eigenvalue formula for the dyadic kernel, zeta determinant, zero exclusion, unbounded Hilbert--Polya operator, or completeness of the local spectral sectors is established.

## 7. Validation

The proof is analytic and is not Lean-verified. Standard-library Python checked the local membership classification exactly in **3,912** cases: primorial cutoffs `3,5,7,11,13,17,19,23,29,31`, refinements `1` through `6`, both centers, and every integer offset `|h|<=y`. Rational Gaussian elimination verified positive pivots in the Cauchy Gram blocks of sizes `1` through `8`; the all-size proof is (10).

Twelve direct antipodal column checks used cutoffs `5,7,11,13` and refinements `1,2,3`, with full finite columns through conductor `90090` and dyadic tails through exponent `50`. Residuals were below `0.084`; these finite floating-point values are consistency checks, not an estimate of the convergence rate. Sixteen checks also verified the opposite-center retained pairs and their cotangent entries. No numerical eigenvalue inference is used in (11).

The decisive audit points are the mesh-dependent embedding, the parity of `m d_y/2`, exclusion of `h=0`, the uniform circular-distance tail bound, the trace-norm rather than merely Hilbert--Schmidt sum in (9), and separating strong local convergence from norm or empirical spectral convergence. Scratch code remains outside Git.
