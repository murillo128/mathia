# PC-463 — Every fixed cotangent population level is a finite constellation law

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-SIEVE-BOUNDARY. The pair and triplet population laws extend to every fixed constellation size. The maximal finite-constellation spectral values are attained and strictly increase with size; above the preceding maximum, only finitely many shapes contribute. Their classical singular series give the exact full-matrix counting coefficient. This is a fixed-size theorem, not a uniform resummation in size, a global spectral-edge theorem, a prime-tuple conjecture, or an RH implication. No historical priority is claimed.

## 1. Objects and the finite-shape counting theorem

Keep the complete primorial tube and conductor normalization:
\[
d_y=\prod_{p\le y}p,\qquad N=d_y m,\quad m\ge1,\qquad
Y=\{a\bmod N:(a,d_y)=1\},
\]
\[
T_{ab}=\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T^+=T+J_{|Y|}/N.
\tag{1}
\]
The augmentation includes its diagonal. Write
`n_+(A,t)=#{lambda(A)>t}` and `n_-(A,t)=#{lambda(A)<-t}`,
with multiplicities.

Let `mathcal F_k` be the finite integer sets of cardinality `k`, normalized by `min F=0`, that are **admissible**:
\[
\nu_p(F):=|F\bmod p|<p\quad\hbox{for every prime }p.
\]
For a fixed `k`, only primes `p<=k` need checking. Define the Hermitian Cauchy block
\[
(L_F)_{ab}=\begin{cases}i/[\pi(a-b)],&a\ne b,\\0,&a=b,\end{cases}
\qquad \ell(F)=\lambda_{\max}(L_F)=\|L_F\|,
\]
\[
\beta_k=\sup_{F\in\mathcal F_k}\ell(F),\qquad \beta_1=0,
\qquad
\mathfrak S(F)=\prod_p
\frac{1-\nu_p(F)/p}{(1-1/p)^k}.
\tag{2}
\]
Complex conjugation sends `L_F` to `-L_F`, explaining the norm equality and sign symmetry. The singular series is positive and absolutely convergent: outside the finitely many prime divisors of the nonzero differences, its factors are `(1-k/p)/(1-1/p)^k=1+O_k(p^-2)`.

The first structural conclusions are
\[
\boxed{\quad
0=\beta_1<\beta_2<\beta_3<\cdots<\tfrac12,
\qquad\text{every }\beta_k\text{ is attained.}
\quad}
\tag{3}
\]
Moreover, for each `epsilon>0`, only finitely many normalized `F in mathcal F_k` satisfy `ell(F)>=beta_(k-1)+epsilon`.

For every **fixed** integer `k>=2` and fixed threshold
\[
t>\beta_{k-1},\qquad
t\notin\{\ell(F):F\in\mathcal F_k\},
\tag{4}
\]
the full matrices obey, for either sign and either convention,
\[
\boxed{\quad
\lim_{y\to\infty}\sup_{m\ge1}
\left|
\frac{(\log y)^k}{d_y m}n_\pm(T^{(+)},t)
-e^{-k\gamma}
\sum_{\substack{F\in\mathcal F_k\\\ell(F)>t}}
\mathfrak S(F)
\right|=0.
\quad}
\tag{5}
\]
The sum is finite. Each normalized shape is counted once. Reflection is included as a different shape when `max F-F` differs from `F`; no universal factor of two or factorial is inserted.

For `t>beta_k`, a stronger zero-coefficient bound holds:
\[
n_\pm(T^{(+)},t)
=O_{k,t}\!\left(\frac{N}{(\log y)^{k+1}}\right),
\tag{6}
\]
uniformly in refinement. Neither (5) nor (6) says that every eigenvalue is below `beta_k`.

## 2. Large gaps force reduction to a smaller block

For an admissible set with at least two points, all differences are even. The classical uniform-separation Hilbert inequality on the real line gives `||L_F||<=1/2`. This is the uniform-gap theorem, not a proposed sharp constant for variable nearest-neighbor weights.

Order `F={0=f_1<...<f_k}` and split at any consecutive gap `G=f_(j+1)-f_j`. Both parts are admissible. The matrix retaining the two diagonal blocks has norm at most `beta_(k-1)`, once monotonicity through that index is known. Every cross entry has magnitude at most `1/(pi G)`; the maximum absolute row sum of the cross-block matrix is at most `k/(pi G)`. Consequently
\[
\ell(F)\le\beta_{k-1}+\frac{k}{\pi G}.
\tag{7}
\]
In particular,
\[
\ell(F)\ge\beta_{k-1}+\varepsilon
\quad\Longrightarrow\quad
\max F\le\frac{k(k-1)}{\pi\varepsilon}.
\tag{8}
\]
The bound is deliberately coarse. Its consequence is discrete compactness modulo translation: above the smaller-block ceiling, a constellation cannot send a point or a subcluster arbitrarily far away. Equation (8) supplies an explicit finite enumeration region once a strict spectral margin is available.

## 3. Admissible extension strictly raises the maximum

Here is an induction that justifies both the monotonicity used in (7) and attainment. The singleton maximum is attained. Suppose `beta_(k-1)` is attained at `F={f_1,...,f_(k-1)}`, and let `v` be a unit eigenvector for that value. Take
\[
Q=\prod_{p\le k}p,\qquad b=f_1+nQ>\max F.
\]
For every `p<=k`, the added point repeats the residue of `f_1`; no previously missing residue is filled. For `p>k`, a `k`-point set cannot occupy all residues. Thus `F union {b}` is admissible.

The coupling of the old top vector to the new coordinate is
\[
g(b)=\sum_{j=1}^{k-1}
\overline{v_j}\frac{i}{\pi(f_j-b)}.
\tag{9}
\]
This rational function is not identically zero: its distinct simple poles have residues proportional to the coordinates of the nonzero vector `v`. It has only finitely many zeros, so some arbitrarily large allowed `b` has `g(b)!=0`. On the span of `(v,0)` and the new coordinate, the Rayleigh compression is
\[
\begin{pmatrix}\beta_{k-1}&g(b)\\\overline{g(b)}&0\end{pmatrix}.
\]
Its top eigenvalue is
\[
\frac{\beta_{k-1}+\sqrt{\beta_{k-1}^2+4|g(b)|^2}}2
>\beta_{k-1}.
\tag{10}
\]
Hence some admissible `k`-set has value `c>beta_(k-1)`. Equation (8), whose smaller-cardinality bounds are already available by induction, confines **all** sets with value at least `c` to a finite region. Their finite maximum is the supremum in (2); sets outside that region have value less than `c` and cannot change it. This proves attainment and strict increase. The common bound `1/2` then implies `beta_k<1/2` for every finite `k`, since `beta_(k+1)>beta_k`.

There is also exactly one possible eigenvalue of either sign above the smaller-block ceiling. Removing any coordinate gives an admissible `(k-1)`-point principal block. Cauchy interlacing yields
\[
\lambda_2^{\downarrow}(L_F)\le\beta_{k-1}.
\tag{11}
\]
By sign symmetry the same holds at the negative edge. Thus, whenever `t>beta_(k-1)`, a shape with `ell(F)>t` contributes one eigenvalue per sign, not an unspecified multiplicity.

## 4. Fixed-size components retain the entire cotangent interaction

Fix an integer cutoff `H` before sending `y` to infinity. On `Y`, join points of circular distance at most `H`. Delete every vertex in a component of size at least `k+1`, leaving a principal matrix `B_H`. Let `R_(y,H,k)` count the deleted vertices.

For any fixed distinct offset set `E`, exact CRT gives
\[
A_y(E):=\#\{a\bmod N:a+E\subset Y\}
=N\prod_{p\le y}\left(1-\frac{\nu_p(E)}p\right).
\tag{12}
\]
If `E` is admissible of size `r`, Mertens's product theorem gives
\[
A_y(E)\sim
\frac{Ne^{-r\gamma}\mathfrak S(E)}{(\log y)^r}.
\tag{13}
\]
Otherwise `A_y(E)` is eventually zero. The dependence on `m` in (12) is exactly linear even when it shares primes with `d_y`, so these fixed-pattern limits are uniform over every `m>=1`.

Every deleted vertex belongs to a connected `(k+1)`-vertex subset containing it: grow a connected set one vertex at a time. Its vertices have graph distance at most `k` from the chosen root. For `N>2kH`, they lift to distinct offsets in `[-kH,kH]`. A finite union bound over these patterns using (12)--(13) proves
\[
R_{y,H,k}=O_{k,H}\!\left(\frac{N}{(\log y)^{k+1}}\right).
\tag{14}
\]
This deletes every vertex of a large component, including components of unbounded size; it is not a count of selected representatives only.

The remaining components have sizes at most `k` and are pairwise separated by more than `H`. Let `D_H` retain their complete diagonal blocks. The separated-cluster inequality of [[research/prime_circle/findings/PC-462-separated-cluster-hilbert-bound-closes-the-cotangent-triplet-counting-law]], applied with maximum cluster size `k`, gives
\[
\|B_H-D_H\|\le k/H.
\tag{15}
\]
For completeness, select one uniform point `X_j` in each component `C_j`, independently, and give it coefficient `u_j=|C_j|v_(X_j)`. The selected support is `H`-separated. The circular Hilbert inequality bounds its normalized cotangent quadratic form by `H^-1 sum_j |u_j|^2`. Taking expectation recovers exactly the full off-block quadratic form, while
`E sum_j |u_j|^2=sum_j |C_j| sum_(a in C_j)|v_a|^2<=k||v||^2`.
Thus (15) keeps the cancellation of all long-distance entries; an absolute row sum of the full `1/h` tail would not give this conclusion.

Norm perturbation and principal-submatrix interlacing now give
\[
n_\pm(D_H,t+k/H)
\le n_\pm(T,t)
\le n_\pm(D_H,t-k/H)+R_{y,H,k}.
\tag{16}
\]
This is the all-radius bridge. The deleted population is one sieve order smaller than the desired `k`-point population.

## 5. Component frequencies and the threshold squeeze

For `N>2kH`, each surviving component has a unique long exterior arc. Starting immediately after that arc gives one normalized shape `F`, with successive gaps at most `H` and diameter at most `(k-1)H`. In particular, no division by its cardinality is required. Once `y>=k`, every shape occurring in a component of size at most `k` is admissible: its membership avoids a residue modulo each prime at most its size, and larger primes cannot be fully covered.

For a fixed admissible `k`-shape whose successive gaps are at most `H`, a translated copy fails to be an entire component only if an extra retained vertex lies within `H` of one of its vertices. The additional offset lies in the fixed interval `[-H,max F+H]`; adjoining it produces a distinct `(k+1)`-set. Equations (12)--(14) therefore show that the number of components of this shape is
\[
\frac{Ne^{-k\gamma}\mathfrak S(F)}{(\log y)^k}
+o_{k,H,F}\!\left(\frac{N}{(\log y)^k}\right),
\tag{17}
\]
uniformly in `m`. This includes components crossing the coordinate cut.

There are finitely many component shapes at fixed `k,H`. Each finite cotangent block converges in norm to `L_F` as `N->infinity`, uniformly in refinement. No entrywise monotonicity of indefinite-matrix eigenvalues is assumed. Thus blocks of sizes less than `k` eventually contribute nothing at any fixed threshold above `beta_(k-1)`, and (11) determines the contribution of each `k`-block away from its top atom.

For a threshold (4), (8) makes the atom set locally finite in `(beta_(k-1),infinity)`. Choose `delta>0` so that
\[
t-\delta>\beta_{k-1},\qquad
[t-\delta,t+\delta]\cap\{\ell(F):F\in\mathcal F_k\}=\varnothing.
\]
Choose one fixed `H` with `k/H<delta` and larger than the diameter of every shape with `ell(F)>t-delta`. Both thresholds in (16) then have exactly the same finite set of contributing shapes. Equations (14), (17) and the finite-block convergence squeeze the normalized counts to (5).

If `t>beta_k`, instead choose fixed `H` with `k/H<(t-beta_k)/2`. Every surviving block is eventually below `t-k/H`, and (14)--(16) give (6). Finally, `T^+-T` has rank one, so either signed count changes by at most one. Since `(log y)^r/d_y->0` for each fixed `r`, this does not affect (5) or (6), uniformly in `m`. Exact finite sign symmetry is asserted for `T`, not for its augmentation.

## 6. What the hierarchy settles and what remains outside it

The initial values are `beta_2=1/(2 pi)` and `beta_3=7/(12 pi)`. The first follows from the smallest admissible pair gap. The second and its two maximizing shapes `{0,2,6}`, `{0,4,6}` are established in PC-462. Thus (5) recovers [[research/prime_circle/findings/PC-460-primorial-cotangent-rare-spectrum-has-a-prime-pair-counting-law]] and PC-462 with their original normalizations and reflection multiplicities.

Equation (3) shows that the hierarchy does not terminate at pairs, triplets, or any finite constellation size. Every interval `(beta_(k-1),beta_k)` contains non-atomic thresholds with a strictly positive coefficient in (5), hence populations of exact order `N/(log y)^k`. This is stronger than repeatedly producing one more local eigenvalue lower bound: each fixed order has a complete finite-shape counting law in its own upper spectral region.

Define `beta_infinity=lim_k beta_k<=1/2`. For every fixed `t>beta_infinity` and every fixed positive integer `A`, (6) implies
\[
n_\pm(T^{(+)},t)=O_{A,t}\!\left(N/(\log y)^A\right).
\tag{18}
\]
This does **not** exclude individual eigenvalues there: `N/(log y)^A` still diverges for every fixed `A`. The constants and cutoffs are not uniform in `k`. Neither the value of `beta_infinity` nor a norm limit of the full matrices follows. Similarly, (5) is not a higher-order expansion at a threshold already below `beta_(k-1)`, where larger leading populations are present.

The deterministic comparison works for arbitrary supports with matching local constellation frequencies and negligible connected `(k+1)`-point populations. Its operator mechanism is not prime-specific. In the present support the arithmetic coefficients are precisely the classical singular series. The comparison preserves those coefficients deliberately; it is not a matched support with all arithmetic information removed.

The theorem leaves atomic thresholds, thresholds approaching a preceding ceiling, constellation size growing with `y`, eigenvector localization, and a uniform infinite-size resummation outside its scope. It counts sieved residues, not actual prime tuples. There is no spectral identification with zeta zeros, zero-exclusion result, or RH-strength estimate.

## 7. Prior art and validation

The external ingredients are classical:

- H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **J. London Math. Soc. (2) 8** (1974), 73--82, [original, p. 74](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf): Corollary 1, equation (1.4), supplies the circular uniform-separation bound, and Theorem 2, equation (1.6), the real-line bound. The cluster averaging argument is already in PC-462.
- J. C. Lagarias, [*Euler's constant: Euler's work and modern developments*, Theorem 3.3.2](https://arxiv.org/pdf/1303.1856): Mertens's product theorem used in (13).
- K. S. Kedlaya, [*Notes on analytic number theory*, Definition 19.1](https://kskedlaya.org/ant/chap-k-tuples.html): the standard singular-series normalization. No conjectural prime-tuple asymptotic is used.

Local duplication checks included PC-460--PC-462 and the fixed-support inverse-square moment/log-determinant classifications PC-153--PC-154. The latter concern different kernels and scalar functionals; they do not give the full indefinite cotangent threshold counts or the attained strictly increasing maxima (3). The new local steps are the large-gap finite-search bound, admissibility-preserving strict extension, and their use to close every fixed population order at once. This is a consequence of classical finite spectral theory and the existing cluster estimate, not a new general Hilbert inequality or new sieve principle. Directed literature searches for sieved discrete Hilbert/cotangent spectra, admissible-tuple spectral maxima and singular-series cluster laws did not establish historical priority.

The proof is analytic, not Lean-verified. A fresh standard-library Python audit, using system LAPACK `zheev` through `ctypes`, checked **560** admissible shapes of sizes `2` through `8`, **2,240** gap-splitting bounds, **2,800** principal-block interlacings and **560** admissibility-preserving strict-extension Rayleigh bounds. The smallest checked positive extension gain was above `1.26e-5`. Independently enumerating reduced residues checked **1,440** exact CRT counts for patterns of sizes `2` through `6`, primorial cutoffs through `11`, and refinements `1,2,3`.

Full-matrix audits through dimension `480` checked **83** cluster norm bounds, **1,162** signed count sandwiches, **1,162** rank-one count comparisons, **6,562** rooted connected deletion witnesses and **64** exact component-count/extra-vertex bounds. The largest ratio to the cluster bound was below `0.302`. These finite tests check conventions, deletion coverage, extension and perturbation arguments; they do not prove the asymptotic theorem or globally maximize any unclassified `beta_k`. Scratch code and output remain outside Git.

The decisive audit points are the induction order in (3), the nonzero rational coupling in (9), local finiteness only above `beta_(k-1)`, the unique cyclic start, removal of all vertices of large components, uniformity in complete refinement, and keeping `k,H,t` fixed before the conductor limit.
