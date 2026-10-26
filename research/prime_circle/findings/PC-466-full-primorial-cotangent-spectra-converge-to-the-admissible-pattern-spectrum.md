# PC-466 — Full primorial cotangent spectra converge to the admissible pattern spectrum

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE. The entire conductor-scaled primorial cotangent spectrum, including its interior and exceptional eigenvalues, has a uniform-in-refinement Hausdorff limit. That limit is exactly the closed union of finite admissible Cauchy-block spectra. A single admissible moving-center limit realizes the whole set as essential spectrum. This is a specialization of classical local-pattern spectral approximation, with the necessary sieve-dependent residual and isolation estimates proved below; it is not a new general spectral theorem or an RH mechanism. No historical priority is claimed.

## 1. Object and full spectral-set theorem

Let
\[
d_y=\prod_{p\le y}p,\qquad N=d_y m,\quad m\ge1,\qquad
Y=\{a\bmod N:(a,d_y)=1\},
\]
\[
(T_{y,m})_{ab}=\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T^+_{y,m}=T_{y,m}+J_{|Y|}/N.
\tag{1}
\]
These act on the **finite retained coordinate space**; no zero complement is added when taking their spectra. The augmentation includes its diagonal.

A finite nonempty set `F subset Z` is admissible if
`|F mod p|<p` for every prime `p`. Set
\[
(L_F)_{ab}=\begin{cases}i/[\pi(a-b)],&a\ne b,\\0,&a=b,
\end{cases}
\qquad
\Sigma_{\rm adm}=
\overline{\bigcup_{F\text{ finite nonempty admissible}}\sigma(L_F)}.
\tag{2}
\]
The closure is in the real line. Singletons supply `0`. Complex conjugation gives sign symmetry, and PC-464 gives
\[
\Sigma_{\rm adm}\subset[-\beta,\beta],\qquad
\{-\beta,0,\beta\}\subset\Sigma_{\rm adm},\qquad
\beta=\sup_F\|L_F\|<\frac{1+2/\sqrt3}{6}.
\tag{3}
\]
In particular this is a nonempty compact set. Define Hausdorff distance by
`d_H(A,B)=max(sup_(a in A) dist(a,B),sup_(b in B) dist(b,A))`.

**Theorem.** For both conventions,
\[
\boxed{\quad
\lim_{y\to\infty}\sup_{m\ge1}
d_H\bigl(\sigma(T^{(+)}_{y,m}),\Sigma_{\rm adm}\bigr)=0.
\quad}
\tag{4}
\]
Moreover, there exists an admissible `S subset Z` whose Cauchy operator, extended by zero to `ell^2(Z)`, satisfies
\[
\boxed{\quad
\sigma(L_S)=\sigma_{\rm ess}(L_S)=\Sigma_{\rm adm}.
\quad}
\tag{5}
\]
PC-465 makes this operator a strong limit of (1) under suitable moving centers along **any prescribed** `y_j -> infinity` and positive integer refinements `m_j`. It is an existence construction, not a canonical center selection.

Equation (4) excludes every compact spectral region disjoint from `Sigma_adm` eventually, uniformly over refinement. Conversely, every fixed neighborhood of every point of `Sigma_adm` contains a finite eigenvalue for all sufficiently large `y` and every refinement. The theorem does not determine whether `Sigma_adm` is an interval, its gaps, spectral multiplicities, or the spectral type in (5).

## 2. The inherited smoothing estimate and the missing residual step

We use the norm approximation from
[[research/prime_circle/findings/PC-464-primorial-cotangent-extreme-spectrum-converges-to-the-admissible-constellation-edge]], §§2--3.
For a fixed primorial `q=d_z`, put `eta=phi(q)/q`. Choose
`0<delta<1/(2q)` and `epsilon>0`. For sufficiently large Fejer degree `R`, the full-polygon sawtooth multiplier `h(x)=1-2x` on `0<x<1`, with `h(0)=0`, is approximated away from the jump by
\[
p_R(x)=\frac2\pi\sum_{r=1}^R
\left(1-\frac r{R+1}\right)\frac{\sin(2\pi rx)}r.
\]
Let `B=P_Y G_(N,R) P_Y`, where `G_(N,R)` has this Fourier multiplier. For `y>=z` and `N>2R`,
\[
\|T-B\|\le a:=\varepsilon+2\eta,
\qquad
B=\sum_{0<|r|\le R}b_r P_Y V^r P_Y,
\quad
b_r=\frac{i}{\pi r}\left(1-\frac{|r|}{R+1}\right).
\tag{6}
\]
Here `V` is cyclic coordinate shift on `Z/NZ`; the displayed sum is restricted to the retained space. The uniform bound uses periodic containment of `Y` in the unit residues modulo `q`, not just its cardinality density. Specifically, a Fourier arc of width less than `1/q` has compressed projection norm at most `eta`; on the rest of the circle the multiplier error is at most `epsilon`. No absolute summation of the untapered Cauchy tail is used.

Fix `R<L<N/2`. Let `Q_s` project onto the retained coordinates in the cyclic interval `{s,...,s+L-1}`. Then
\[
\sum_s\|Q_s v\|^2=L\|v\|^2.
\tag{7}
\]
For one displacement `r`, a coordinate and its translate belong to different windows at exactly `2|r|` starting positions. Since deleting coordinates only reduces the sum,
\[
\sum_s\|[P_YV^rP_Y,Q_s]v\|^2
\le2|r|\|v\|^2.
\]
The triangle inequality in the Hilbert direct sum over `s` therefore gives
\[
\left(\sum_s\|[B,Q_s]v\|^2\right)^{1/2}
\le C_R\|v\|,
\qquad
C_R=\frac{2\sqrt2}{\pi}\sum_{r=1}^R
\frac{1-r/(R+1)}{\sqrt r}
\le\frac{4\sqrt{2R}}\pi.
\tag{8}
\]

Now let `Tv=lambda v`, `||v||=1`. Equation (6) implies
`||(B-lambda)v||<=a`. Applying (7) to that residual and (8) to the commutator,
\[
\left(\sum_s\|(B-\lambda)Q_s v\|^2\right)^{1/2}
\le\sqrt L\,a+C_R.
\tag{9}
\]
Consequently some nonzero `Q_s v`, normalized to a unit vector `w`, obeys
`||(B-lambda)w||<=a+C_R/sqrt L`. Compress the output to that window and replace `B` by `T` once more:
\[
\|(Q_sTQ_s-\lambda)w\|
\le 2a+C_R/\sqrt L.
\tag{10}
\]
Self-adjointness converts (10) to distance from `lambda` to the local block spectrum. This is the residual estimate absent from a mere localization of extreme Rayleigh quotients. It controls an arbitrary eigenvalue, including one deep inside the global spectral interval.

## 3. Every finite eigenvalue approaches the admissible spectral set

When `y>=L`, the retained offsets `F_s subset {0,...,L-1}` in every cyclic window are admissible. For `p<=y` they miss the excluded offset residue modulo `p`; for `p>y` their cardinality is less than `p`. This includes windows crossing the cyclic cut.

The elementary cotangent-to-Cauchy estimate from PC-464, §5, gives
\[
\|Q_sTQ_s-L_{F_s}\|
\le\frac{\pi^2L^2}{6N^2}.
\tag{11}
\]
Thus (10), with the nonempty window it supplies, proves
\[
\boxed{\quad
\sup_{\lambda\in\sigma(T)}\operatorname{dist}
(\lambda,\Sigma_{\rm adm})
\le
2\varepsilon+4\frac{\varphi(q)}q+
\frac{4\sqrt{2R}}{\pi\sqrt L}+
\frac{\pi^2L^2}{6N^2}.
\quad}
\tag{12}
\]
For any desired accuracy choose, in order: a primorial `q` of small totient density; `delta<1/(2q)` and small `epsilon`; the Fejer degree `R`; and finally `L>R` large enough for the third term. Keep these parameters fixed as `y -> infinity`. The last term then vanishes uniformly in `m` because `N>=d_y`.

This proves the upper spectral inclusion in (4), including exclusion of isolated exceptional eigenvalues a fixed distance from the admissible set. It does not assert that a principal compression's eigenvalues must belong to the full spectrum. The reverse inclusion requires a separate argument.

## 4. Isolated exact patterns prevent loss of finite-block eigenvalues

Fix a nonempty finite admissible `F subset [-r_0,r_0]`, an eigenvalue `lambda` of `L_F`, and a corresponding unit vector `v`. Choose an integer `W>r_0`.

The exact-window CRT construction of
[[research/prime_circle/findings/PC-465-moving-center-cotangent-limits-fill-the-admissible-hull]], §2, realizes
\[
\{h\in[-W,W]:(c+h,d_y)=1\}=F
\tag{13}
\]
for every sufficiently large `y`, every refinement, and some center `c`. Briefly, assign each hole `b in [-W,W]\\F` a distinct prime `p_b>2W` and require `c=-b mod p_b`. These primes kill the holes without killing any point of `F`. At every other prime dividing `d_y`, admissibility supplies a residue of `c` preserving `F`. CRT solves all conditions. All assigned primes and the window are fixed before taking `y` large.

Embed `v` at the translated points of `F` in the finite retained space and put it zero elsewhere. In the centered coordinate interval `I_N={-N/2,...,N/2-1}`, assume `N>2(2r_0+1)` and `N>2W`. The output rows inside the protected window consist exactly of `F`; their residual is bounded by
`pi^2(2r_0+1)^2/(6N^2)`.

For each `k in F`, the uniform column-tail estimate of PC-465, §3, gives
\[
\sum_{\substack{h\in I_N\\|h|>W}}
\left|\frac1N\cot\frac{\pi(h-k)}N\right|^2
\le\frac2{\pi^2(W-r_0)}.
\tag{14}
\]
It remains valid after restricting rows to the retained support. The triangle inequality over input columns and `||v||_1<=sqrt(|F|)` therefore imply
\[
\boxed{\quad
\operatorname{dist}(\lambda,\sigma(T_{y,m}))
\le\|(T_{y,m}-\lambda)v\|
\le\frac{\pi^2(2r_0+1)^2}{6N^2}
+\sqrt{\frac{2|F|}{\pi^2(W-r_0)}}.
\quad}
\tag{15}
\]
First enlarge `W`, then take `y` large enough for (13) and the finite-block error. This proves uniform-in-refinement approximation of every eigenvalue of every fixed finite admissible block. It includes `lambda=0` from a singleton: the nearby eigenvalue belongs to the actual finite retained matrix, not an artificial zero complement.

Because (2) is a compact closure, a finite accuracy net can be selected from its defining union. Apply (15) to those finitely many witnesses and take the largest conductor threshold. This proves the reverse Hausdorff inclusion, and hence (4) for `T`. Finally,
\[
\|T^+-T\|=\varphi(d_y)/d_y\longrightarrow0
\tag{16}
\]
uniformly in refinement. The self-adjoint spectral perturbation bound proves the augmented assertion. Rank one without the vanishing norm in (16) would not suffice.

## 5. One admissible support realizes the entire limit as essential spectrum

For any admissible `S subset Z`, PC-465 defines a bounded self-adjoint `L_S`, with norm at most `beta`. On `ell^2(S)`, every spectral value admits unit approximate eigenvectors of finite support: start with a unit approximate eigenvector and use density of finitely supported vectors and boundedness. If such a vector is supported on `F subset S`, compression of its residual shows
\[
\operatorname{dist}(\lambda,\sigma(L_F))
\le\|(L_S-\lambda)v\|.
\]
It follows that `sigma(L_S) subset Sigma_adm`; extending by zero adds at most `0`, which is already in the set. The empty support is harmless.

Enumerate all finite nonempty admissible shapes modulo translation in a sequence `F_j` in which every shape occurs infinitely often. Put `k_j=|F_j|` and `R_j=j^2 k_j+2`.

PC-465's finite gluing lemma says that for finite admissible `U,F`, arbitrarily large translations `t` make `U union (t+F)` admissible. To recall its proof, for each prime `p<=|U|+|F|` choose a missing residue of `U` and translate `F` so that it also misses that residue. CRT chooses all translation residues simultaneously; larger primes cannot be covered by so few points. Adding multiples of the CRT modulus makes the translation arbitrarily large.

Use this lemma inductively to place disjoint copies `G_j=t_j+F_j` to the right of the preceding copies, with
\[
\operatorname{dist}(G_j,G_i)\ge\max(R_j,R_i)
\quad(i\ne j),
\tag{17}
\]
and with every finite partial union admissible. Their union `S` is admissible: a violation modulo any prime would have finitely many witnesses in one partial union.

For a unit eigenvector of `L_(F_j)`, translate it to `G_j` and extend by zero, calling it `v_j` and its eigenvalue `lambda_j`. Its residual vanishes on its own block. Summing the squared integer Cauchy tails outside distance `R_j` and then using `||v_j||_1<=sqrt(k_j)` gives
\[
\|(L_S-\lambda_j)v_j\|
\le\sqrt{\frac{2k_j}{\pi^2(R_j-1)}}
\le\frac{\sqrt2}{\pi j}.
\tag{18}
\]
This estimates all cross-copy interactions rather than discarding them.

Fix any eigenvalue of any finite admissible shape and restrict to its infinitely many occurrences in the enumeration. Choose its corresponding eigenvector each time. The resulting vectors have disjoint supports, are orthonormal, and satisfy (18) with residual tending to zero. The singular Weyl criterion places that eigenvalue in `sigma_ess(L_S)`. Closedness gives
\[
\Sigma_{\rm adm}\subset\sigma_{\rm ess}(L_S)
\subset\sigma(L_S)\subset\Sigma_{\rm adm},
\]
proving (5). Unlike the extremal Rayleigh argument in PC-465, the isolation bound works at **every** finite-block eigenvalue, not just the edge. The set `S` still has zero upper Banach density, by PC-465's admissibility argument.

## 6. Mathematical delta, controls and prior art

PC-463 classifies fixed-size high-level eigenvalue populations; PC-464 identifies the extreme norm; PC-465 classifies strong local operators and constructs an essential edge. Neither strong convergence nor an edge limit proves convergence of all spectral sets. Equations (8)--(15) close that particular gap: the limiting spectral set is exhausted by the finite admissible patterns, and a deliberate support realizes its whole closure in essential spectrum.

The kernel and the localization estimates are generic. Arithmetic supplies precisely the periodic sieve containment, local admissibility and realization of every exact pattern **including its holes**. Any other mask family satisfying these same approximation, local-pattern and occurrence conditions has the same spectral-set limit. This is a conditional matched-control statement; simply matching density or relabeling vertices does not ensure the hypotheses. It does not establish that the admissible set itself has forgotten arithmetic.

The theorem leaves spectral frequency, multiplicity, fine spacing, rates at moving thresholds, and eigenvector behavior undetermined. In particular, a vanishing empirical proportion can still carry the full nonzero spectral set. No actual prime-tuple occurrence theorem is used: CRT occurrences are among reduced residues of finite primorial sieves. There is no zeta-zero identification, critical-line selection, or RH implication. The new operator in (5) depends on choices and is not a geometry-forced replacement for the original family.

Closest primary prior art:

- F. Gabel, D. Gallaun, J. Grossmann, M. Lindner and R. Ukena, *Spectral Approximation of Generalized Schrödinger Operators via Approximation of Subwords*, **Complex Analysis and Operator Theory 18** (2024), article 7, [DOI and open text](https://doi.org/10.1007/s11785-023-01448-3). Lemma 3.1 and the spectral approximation framework identify localized lower norms and finite-pattern diversity as classical mechanisms. Here (8)--(10) prove the required residual estimate directly, and (6) justifies its use for a long-range cotangent kernel.
- R. Hagger, M. Lindner and M. Seidel, *Essential pseudospectra and essential norms of band-dominated operators*, **Journal of Mathematical Analysis and Applications 437** (2016), 255--291, [DOI](https://doi.org/10.1016/j.jmaa.2015.11.060), [author manuscript](https://arxiv.org/abs/1504.00540). This is the general limit-operator/essential-spectrum setting. Section 5 instead gives a direct isolated-block Weyl proof, so no unverified application of a general band-dominated theorem is needed.
- The admissible-hull and singular-Weyl sources recorded in PC-465 remain the anchors for the support language and the final essential-spectrum inference. The present proof explicitly supplies the stronger buffer construction.

The local duplication check covered PC-459, PC-463--PC-465 and the finite-patch edge theorem PC-264, whose operator and parameter regime differ. Structural literature searches found the mechanism to be established local-pattern spectral theory; narrow cotangent/sieved-Cauchy searches did not establish historical priority. The contribution here is the exact full-spectrum specialization and its uniformity in complete refinement, not a claim to a new spectral paradigm.

## 7. Validation and evidence boundary

The derivation is analytic, not Lean-verified or independently adversarially approved. A deterministic standard-library Python audit with system LAPACK `zheev` through `ctypes` checked **48** cyclic commutator bounds (8) and **48** localized-eigenvector bounds (9), including prime-derived masks, further randomly deleted controls, interior eigenvalues and cyclic wraparound. The maximum ratios to their respective bounds were below `0.021` and `0.487`.

It checked **162** finite isolated-window residual bounds (15) for primorial bases `30,210`, refinements one through three, multiple centers and windows, with maximum ratio below `0.519`; these include **12** singleton zero-eigenvalue tests. Separately, it verified **65** exact CRT windows and **35** consecutive admissibility-preserving gluings with the prescribed growing isolation buffers, producing 84 vertices with 33-digit offsets. These are finite sign, normalization, residual and congruence diagnostics, not numerical proof of the infinite limit or a computation of `Sigma_adm`. Scratch code and output stay outside Git.

The decisive audit points are localization of residuals rather than only quadratic forms, fixing every smoothing/window parameter before the sieve limit, preserving holes when passing from local to global spectra, controlling output beyond the protected window, using a finite net for uniform Hausdorff inclusion, and keeping later glued blocks outside every earlier buffer. A formalization handoff is not made: the substantive unresolved work was this analytic spectral passage, while formalizing it would require broad spectral and limiting infrastructure rather than an isolated finite certificate with a distinct fertility question.
