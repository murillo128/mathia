# PC-465 — Moving-center cotangent limits fill the admissible hull

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE. Allowing the observation center to move gives an exact classification of all strong local limits of the conductor-scaled primorial cotangent matrices: the discrete Cauchy operators on all prime-admissible integer supports. One such limit attains the full PC-464 edge in its **essential** spectrum; uniformly random centers instead converge strongly to zero in mean square. The ingredients are CRT, classical admissible-set dynamics and elementary self-adjoint spectral theory. This is neither a canonical choice of limit nor a zeta-zero/RH mechanism, and no historical priority is claimed.

## 1. The center is part of the limiting operation

Let
\[
d_y=\prod_{p\le y}p,\qquad N=d_y m,\quad m\ge1,
\qquad I_N=\{-N/2,\ldots,N/2-1\}.
\]
We take `y>=2`, so `N` is even. For an arbitrary integer center `c mod N`, put
\[
\chi_{y,m,c}(h)=\mathbf1_{h\in I_N}\mathbf1_{(c+h,d_y)=1}.
\]
On `ell^2(Z)`, embed the primitive complete-tube matrix by
\[
(K_{y,m,c})_{hk}=
\begin{cases}
\chi_{y,m,c}(h)\chi_{y,m,c}(k)
\dfrac{i}{N}\cot\dfrac{\pi(h-k)}N,&h,k\in I_N,\ h\ne k,\\
0,&\text{otherwise},
\end{cases}
\tag{1}
\]
and write `K^+` for the augmentation by the matrix
`chi(h)chi(k)/N`, including its diagonal. These are finite-rank operators. The center need not be a retained vertex. All centers give unitarily equivalent finite nonzero blocks, with identical finite spectra.

For `S subset Z`, call `S` admissible when
\[
|S\bmod p|<p\qquad\text{for every prime }p.
\tag{2}
\]
Equivalently, every finite subset of `S` is admissible. Write `mathcal A` for this family and define
\[
(L_S)_{hk}=\begin{cases}
i/[\pi(h-k)],&h,k\in S,\ h\ne k,\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
\]
For admissible `S` this is a bounded self-adjoint operator, as proved below. Set
\[
\beta=\sup_{F\subset\mathbb Z\text{ finite admissible}}\|L_F\|.
\]
This is `beta_infinity` in [[research/prime_circle/findings/PC-464-primorial-cotangent-extreme-spectrum-converges-to-the-admissible-constellation-edge]]. In particular,
\[
0<\beta<\frac{1+2/\sqrt3}{6}.
\]

**Classification.** Fix any sequence `y_j -> infinity` and any positive integer refinements `m_j`. As centers are allowed to vary, the set of strong subsequential limits of either family (1) is exactly
\[
\boxed{\quad\{L_S:S\in\mathcal A\}.\quad}
\tag{4}
\]
Every member can in fact be realized along the entire prescribed sequence by choosing its centers. This is an equality of operator sets, not an injective parametrization: all empty/singleton supports give the zero operator.

Moreover, there exists an admissible `S_*` such that
\[
\boxed{\quad
\|L_{S_*}\|=\|L_{S_*}\|_{\rm ess}=\beta,
\qquad \{-\beta,\beta\}\subset\sigma_{\rm ess}(L_{S_*}).
\quad}
\tag{5}
\]
Here the essential norm is distance to the compact operators. Thus compactness of the anchor and antipodal limits in PC-459 does not extend to arbitrary moving centers.

For the different choice of a uniformly random center `C mod N`, every fixed `v in ell^2(Z)` satisfies
\[
\boxed{\quad
\lim_{y\to\infty}\sup_{m\ge1}
\mathbb E_C\|K_{y,m,C}^{(+)}v\|^2=0.
\quad}
\tag{6}
\]
These contrasting local limits coexist with `||K_(y,m,c)^(+)|| -> beta`, uniformly in refinement and center, by PC-464.

## 2. CRT realizes exact windows, including their holes

Fix a finite integer window `W=[-R,R]` and an admissible `F subset W`. Assign to each unwanted offset `b in W\F` a **different** prime `p_b>2R`. Impose
\[
c\equiv-b\pmod{p_b}.
\tag{7}
\]
This excludes `b` and excludes no member of `F`: for `f in F`, the nonzero difference `f-b` has absolute value at most `2R<p_b`.

For any other prime `p<=y`, choose `c mod p` outside `-F mod p`; admissibility makes this possible. Once `y` includes all the assigned primes, CRT solves these simultaneous conditions modulo `d_y`. For every refinement `m`, take any corresponding center modulo `N=d_y m`. Once `N>2R`,
\[
\{h\in W:(c+h,d_y)=1\}=F.
\tag{8}
\]
The empty `F` is allowed. The distinct auxiliary primes are essential to this proof: using a small prime to remove a hole can remove a desired point as well.

For an arbitrary admissible `S`, apply (8) to `F=S intersect [-R,R]`. For each fixed `R` there is a finite threshold `y_R` after which the exact window is realizable for every refinement. Increase these thresholds if necessary to make them monotone. Along any prescribed `y_j -> infinity`, choose radii `R_j -> infinity` slowly enough that `y_j>=y_(R_j)`, then select the corresponding centers. The masks converge pointwise to `1_S`. No compatibility of the centers at different conductors is asserted or needed.

Conversely, suppose some masks converge pointwise to `1_S`. If `S` occupied every residue modulo a prime `p`, finitely many of its offsets would witness this. For all sufficiently large indices they would all survive while `p|d_y`, which is impossible because the offset residue `-c mod p` is excluded. Thus `S` is admissible. Every sequence of masks has a pointwise convergent subsequence by a diagonal extraction over the integer coordinates.

This classifies the local supports. It does not assert that the same patterns recur among actual primes: all occurrence assertions concern finite sieves.

## 3. Pointwise masks give strong operator convergence

Every finite admissible compression in (3) has norm at most `beta`. Hence its finitely supported sesquilinear form has bound `beta ||u|| ||v||`, by applying the bound on the union of the two finite supports. It extends uniquely to a bounded self-adjoint operator with the stated matrix entries. Finite-support Rayleigh quotients give the exact identity
\[
\|L_S\|=\sup_{F\subset S\text{ finite}}\|L_F\|\le\beta.
\tag{9}
\]

The column-tail estimate from [[research/prime_circle/findings/PC-459-primorial-cotangent-local-limits-split-into-anchor-pair-and-antipodal-dyadic-kernel]], §3, is uniform in the center. To make the topology explicit, let `delta_N(h-k)` be circular distance. For distinct `h,k in I_N`,
\[
\left|N^{-1}\cot\frac{\pi(h-k)}N\right|
\le\frac1{\pi\delta_N(h-k)},
\qquad
\delta_N(h-k)\ge |h|-|k|.
\]
For fixed `k` and integer `R>|k|`, therefore,
\[
\sum_{|h|>R}|(K_{y,m,c})_{hk}|^2
\le\frac2{\pi^2(R-|k|)}.
\tag{10}
\]
If `k` is unused the left side is zero. The same bound holds for `L_S`. For a fixed finite window, pointwise convergence of the binary masks makes membership eventually exact, and the cotangent entries converge to (3). Combining this with (10) proves convergence of each column in `ell^2`.

The full-polygon Fourier multiplier has absolute value at most one, so the raw and augmented finite compressions have norms at most one. Convergence on finitely supported vectors thus extends to strong convergence on `ell^2(Z)`. The augmentation has norm
\[
\|K^+-K\|=\varphi(d_y)/d_y\longrightarrow0,
\tag{11}
\]
uniformly in refinement and center, so it has the same limits.

These facts prove realizability in (4). For exhaustiveness, start with any strongly convergent operator subsequence and extract a further pointwise-convergent mask subsequence. Its admissible limit `S` gives strong limit `L_S`; uniqueness of the original strong limit finishes the argument. Operator convergence does not require assuming that the original masks themselves converge.

## 4. One admissible limit has the entire edge in essential spectrum

The necessary gluing lemma is finite and exact:

> Given finite admissible `U,F`, arbitrarily large translations `t` make `U union (t+F)` admissible.

Put `n=|U|+|F|`. For every prime `p<=n`, choose a missing residue `r_p` of `U`. Since `F` is admissible, there is a residue `t_p` such that `r_p` is absent from `t_p+F mod p`. Solve `t=t_p mod p` by CRT. The union omits `r_p` for all these primes; primes larger than `n` cannot be covered by a set of at most `n` points. Adding arbitrarily large multiples of the CRT modulus puts the new copy beyond any specified finite interval.

By [[research/prime_circle/findings/PC-463-every-fixed-cotangent-population-level-is-a-finite-constellation-law]], choose an admissible `j`-point maximizer `F_j`, with top eigenvalue `beta_j`, where `beta_j` increases to `beta`. Repeatedly apply the lemma so that the translated copies `G_j=t_j+F_j` are disjoint and move to positive infinity, and every partial union is admissible. Then
\[
S_*:=\bigcup_{j\ge1}G_j
\]
is admissible: a violation modulo any prime would already have finitely many witnesses in one partial union.

Let `v_j` be a unit top eigenvector of `L_(F_j)`, translated to `G_j` and extended by zero. The `v_j` are orthonormal, and
\[
\langle v_j,L_{S_*}v_j\rangle=\beta_j.
\tag{12}
\]
Cross-copy entries do not enter this quadratic form; they are **not** discarded from the full operator. Its spectrum lies in `[-beta,beta]` by (9). On that interval,
\[
(\beta-t)^2\le2\beta(\beta-t).
\]
The spectral theorem and (12) yield
\[
\|(L_{S_*}-\beta)v_j\|^2
\le2\beta(\beta-\beta_j)\longrightarrow0.
\tag{13}
\]
Thus the escaping vectors form a singular Weyl sequence at `beta`. Complex conjugation sends `L_(S_*)` to `-L_(S_*)`, giving another at `-beta`. Weyl's criterion proves the essential-spectrum assertion.

For any compact `A`, `Av_j -> 0`, so (13) also gives `||L_(S_*)-A||>=beta`. Together with (9), this proves both norm equalities in (5) directly. No absolute summation of all cross-copy Cauchy interactions, and no assertion that finite-block eigenvectors remain exact global eigenvectors, is used.

This constructs an edge-attaining **operator**, not a normalized eigenvector at the edge. Neither pure point, absolutely continuous nor singular continuous spectral type is determined. By (4), it is a strong limit of the original matrices under chosen moving centers. Since those matrices are finite rank,
\[
\|K_{y,m,c}^{(+)}-L_{S_*}\|\ge\beta
\tag{14}
\]
for every index and center. In this realization the failure of norm convergence follows from the nonzero essential norm itself.

## 5. Typical centers and zero-density supports

Let `eta_y=phi(d_y)/d_y`. For a uniform center modulo `N`, every fixed offset in `I_N` survives with probability exactly `eta_y`, independently of refinement. If `v` has finite support `F`, a union bound shows
\[
\mathbb P_C\bigl(\chi_{y,m,C}(k)=1
\text{ for some }k\in F\bigr)\le |F|\eta_y.
\]
Outside this event all input columns vanish, for both conventions. Their norm bound by one therefore gives
\[
\mathbb E_C\|K_{y,m,C}^{(+)}v\|^2
\le |F|\eta_y\|v\|^2.
\tag{15}
\]
Approximate any `ell^2` vector by finite-support vectors and use the same uniform norm bound to obtain (6). This also gives convergence to zero in probability for each fixed input vector. It does not assert almost-sure convergence for an arbitrary coupling of the random centers.

All admissible supports, including `S_*`, have zero upper Banach density. Indeed, for any fixed primorial `q`, choose one omitted residue modulo each prime dividing `q`. Their complement has exactly `phi(q)` allowed classes modulo `q` and contains `S`. In any integer interval of length `H`,
\[
|S\cap[a,a+H)|\le\bigl(H/q+1\bigr)\varphi(q).
\tag{16}
\]
First let `H -> infinity` uniformly in `a`, then let `q` run through primorials. The upper Banach density is zero. This sparsity is fully consistent with (5): essential norm can be carried by increasingly rare, spatially escaping finite constellations.

## 6. Consequence, controls and prior art

PC-459 identifies the fixed-anchor rank-two and antipodal trace-class limits. PC-464 identifies the common finite spectral edge. Equation (4) classifies **every moving integer-mesh chart**, while (5) realizes that edge in a noncompact local limit. Hence neither a compact local spectrum nor the recovery of the global edge selects a unique limiting operator from the intrinsic finite matrices. A proposed spectral mechanism must justify its choice of chart or another source-forced limiting operation. The gluing choices above provide existence, not such a canonical selection.

The local operator depends only on the limiting support and the unchanged Cauchy kernel. Any other polygon masks with the same pointwise limit and the same uniform norm/tail bounds reproduce it. This control retains the local admissibility data deliberately; it is not evidence that every arithmetic invariant or full finite spectrum is prime-blind. The statement is restricted to this kernel, conductor normalization and integer-mesh embedding. It gives no full spectral-set convergence, eigenvector localization, value of `beta`, prime-tuple theorem, zeta-zero identification or RH implication.

The closest prior-art anchors are:

- A. Dymek (A. Bartnicka in the preprint), S. Kasjan, J. Kułaga-Przymus and M. Lemańczyk, *B-free sets and dynamics*, **Trans. Amer. Math. Soc. 370** (2018), 5425–5489, [author manuscript, Definition 2.28 and Example 2.45](https://arxiv.org/pdf/1509.08010). The admissible hull is classical. Their example with all primes distinguishes it from the much smaller orbit closure of `{−1,1}`. Accordingly, (4) takes moving centers **before** the sieve limit; it does not claim that translating the already-limited anchor pair generates the hull. Their discussion of prime tuples also separates finite-sieve realization from conjectural realization among primes.
- G. Teschl, *Mathematical Methods in Quantum Mechanics*, 2nd ed., AMS GSM **157** (2014), [author edition, Lemma 6.17](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf): the classical singular-Weyl-sequence criterion used after the direct residual estimate (13).

CRT pattern realization, bounded Cauchy compression and Weyl's criterion are classical ingredients, not new general theorems. The local contribution is their exact joint use to classify the cotangent limits and contrast an essential edge with typical strong collapse. Local duplication checks covered PC-388, PC-459, PC-463 and PC-464, plus targeted searches for admissible configurations and moving local limits. External searches through admissible/B-free dynamics and discrete Hilbert-transform spectral theory did not establish historical priority. In particular, no theorem identifying the prime-admissible hull with the orbit closure of the infinite prime-free set is used.

## 7. Validation and evidence boundary

The proof is analytic, not Lean-verified or independently adversarially approved. A fresh deterministic standard-library Python audit checked all **128** admissible patterns in symmetric windows of radii one through five, including empty and singleton patterns, and verified their exact CRT realizations in **768** refined/lifted windows. It rejected **2,600** inadmissible patterns by the finite modular criterion. It also checked **75** consecutive admissibility-preserving gluings, producing a 154-point admissible union with 60-digit offsets.

For primorial bases `6,30,210` and refinements one through four, **240** finite column-tail tests satisfied (10), with maximum ratio below `0.274`, and **48** exact uniform-center counts satisfied the union bound in (15). These checks test congruences, signs, wraparound, tails and quantifiers; they do not prove the infinite classification, compute maximizing `F_j`, or certify `beta` numerically. Scratch code and output remain outside Git.

The decisive audit points are simultaneous retention and exclusion in (8), using new primes larger than the whole window, pointwise-mask compactness before classifying arbitrary strong limits, the column-tail step beyond entrywise convergence, admissibility of the increasing union, and the extremal spectral inequality in (13), which controls the full operator without suppressing cross-copy interactions.
