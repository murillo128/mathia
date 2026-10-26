# PC-460 — Primorial cotangent rare spectrum has a prime-pair counting law

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-CLASSICALIZATION. For the full conductor-scaled cotangent matrix on a primorial complete tube, the eigenvalue counts outside any fixed nonzero threshold have an exact first-order limit, except at the explicitly identified atomic thresholds. Both signs have the same limit, uniformly in arbitrary refinement depth, and the all-ones augmentation leaves it unchanged. The coefficients are the classical Hardy--Littlewood prime-pair singular series. This determines the leading population of exceptional eigenvalues left open by PC-458; it does not classify individual outliers, eigenspaces, or the smaller spectral populations visible in PC-459, and supplies no new zeta-zero implication.

## 1. The full operator and its rare-count scale

Let
\[
d_y=\prod_{p\le y}p,\quad m\ge1,\quad N=d_y m,\quad
Y=\{a\bmod N:(a,d_y)=1\},\quad M=|Y|=m\varphi(d_y).
\]
On the coordinate space of `Y`, retain the full matrices
\[
T_{ab}=\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T^+=T+J_M/N.
\tag{1}
\]
The augmentation includes its diagonal. These are exactly the matrices of [[research/prime_circle/findings/PC-458-conductor-scaled-cotangent-bulk-collapses-exactly-at-vanishing-primitive-density]]. Their norms are at most one. For a Hermitian matrix `A` and `t>0`, write
\[
n_+(A,t)=\#\{\lambda(A)>t\},\qquad
n_-(A,t)=\#\{\lambda(A)<-t\},
\]
counting multiplicity. Put
\[
\alpha_y=\frac{\log y}{M},\qquad
C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right),
\]
\[
\mathfrak S_2(h)=\begin{cases}
2C_2\displaystyle\prod_{\substack{p\mid h\\p>2}}\frac{p-1}{p-2},&h\text{ even},\\
0,&h\text{ odd}.
\end{cases}
\tag{2}
\]
For every fixed `t>0` outside
\[
\mathcal A=\{1/(2\pi k):k=1,2,\ldots\},
\]
the theorem is
\[
\boxed{\quad
\alpha_y n_\pm(T^{(+)},t)
\longrightarrow
 e^{-\gamma}\sum_{\substack{h\ge1\\1/(\pi h)>t}}\mathfrak S_2(h).
\quad}
\tag{3}
\]
Here either sign and either matrix convention are allowed. Convergence is uniform over all integers `m>=1`; in particular no ordering or coprimality restriction on `m=m(y)` is needed. The sum is finite.

Equivalently, the measures `alpha_y sum_lambda delta_lambda`, restricted to `R\{0}`, converge vaguely to
\[
e^{-\gamma}\sum_{\substack{h\ge1\\2\mid h}}\mathfrak S_2(h)
 \left(\delta_{1/(\pi h)}+\delta_{-1/(\pi h)}\right).
\tag{4}
\]
This is a locally finite measure away from zero, not a probability measure on the whole line. It is distinct from PC-458's empirical probability, whose limit is `delta_0`.

For example, whenever `1/(4 pi)<t<1/(2 pi)`, only `h=2` contributes, so
\[
\boxed{\quad
n_\pm(T^{(+)},t)
\sim 2C_2e^{-\gamma}\frac{M}{\log y}
\sim 2C_2e^{-2\gamma}\frac{N}{(\log y)^2}.
\quad}
\tag{5}
\]
Thus each signed population has the same leading size as the exact number of retained gap-two edges. The arithmetic here counts units modulo a primorial, not pairs of actual primes; no prime-pair conjecture is used.

## 2. Exact local counts, including refinement

For any fixed finite offset set `F`, CRT gives
\[
\#\{a\bmod N:a+f\in Y\ (f\in F)\}
=N\prod_{p\le y}\left(1-\frac{\nu_p(F)}p\right),
\quad \nu_p(F)=|F\bmod p|.
\tag{6}
\]
Every allowed residue modulo `d_y` has exactly `m` lifts, even if `m` shares primes with `d_y`.

For `0<h<N/2`, let `J_y(h)` count the retained unordered positive-offset-`h` edges. Each such edge has one start, so (6) gives, for even `h`,
\[
\frac{J_y(h)}M=B_yG_y(h),\qquad
B_y=\prod_{3\le p\le y}\frac{p-2}{p-1},\quad
G_y(h)=\prod_{\substack{3\le p\le y\\p\mid h}}\frac{p-1}{p-2}.
\tag{7}
\]
For odd `h` the count is zero. Mertens's product theorem and
\[
B_y=2\prod_{p\le y}(1-1/p)
       \prod_{3\le p\le y}\left(1-\frac1{(p-1)^2}\right)
\]
imply
\[
\alpha_yJ_y(h)\longrightarrow e^{-\gamma}\mathfrak S_2(h)
\tag{8}
\]
for every fixed `h`, uniformly in refinement.

For fixed distinct nonzero shifts `s,t`, the count of `a,a+s,a+t` is either zero by a local obstruction or
\[
O_{s,t}\!\left(\frac{M}{(\log y)^2}\right).
\tag{9}
\]
Indeed, outside the finitely many prime divisors of `st(s-t)`, the local numerator in (6) is `1-3/p`. Its ratio to `(1-1/p)^3` is `1+O(p^-2)`. The convergent product and Mertens give `O(N/(log y)^3)`, equivalent to (9). All dependence on `m` is the exact factor `m`.

These are the pair/triple counts behind [[research/prime_circle/findings/PC-150-fixed-radius-spectral-functions-collapse-to-atomic-pair-singular-series]] and [[research/prime_circle/findings/PC-151-full-chord-first-mertens-spectral-displacement-is-prime-pair-singular-series]], applied here to cotangent matrices. The formulas above give the needed argument independently of those inverse-square operators.

## 3. Fixed windows reduce to isolated signed edges

Fix an integer `H`. For `N>2H`, truncate (1) to circular distances at most `H`, obtaining `T_H`. Let `B_H` be the vertices incident to at least two retained short edges. Such a vertex belongs to one of the finitely many triples in (9), with `s,t in {-H,...,-1,1,...,H}`. Hence
\[
|B_H|=O_H\!\left(\frac{M}{(\log y)^2}\right).
\tag{10}
\]
Set to zero every row and column of `T_H` indexed by `B_H`. The result `D_H` is a direct sum of isolated edge blocks and zeros. The removed matrix is supported on those rows or columns, so
\[
\operatorname{rank}(T_H-D_H)\le2|B_H|.
\tag{11}
\]
Each vertex has degree at most `2H`; consequently the number of surviving edges of type `h` differs from `J_y(h)` by at most `2H|B_H|`.

A surviving edge of length `h` has eigenvalues
\[
\pm w_N(h),\qquad w_N(h)=\frac1N\cot\frac{\pi h}N
\longrightarrow\frac1{\pi h}.
\tag{12}
\]
The convergence is uniform over `m>=1` because `N>=d_y->infinity`. Finite-rank interlacing changes either threshold count by at most the rank in (11). Multiplying by `alpha_y`, (8)--(12) therefore prove, for non-atomic thresholds,
\[
\alpha_y n_\pm(T_H,t)\longrightarrow
 e^{-\gamma}\sum_{\substack{1\le h\le H\\1/(\pi h)>t}}\mathfrak S_2(h).
\tag{13}
\]
The signed edge eigenvalues in (12) differ from the single nonzero inverse-square Laplacian eigenvalue in PC-150. Positivity of a deleted-edge Laplacian cannot be used for the next step.

## 4. The full cotangent tail is small in squared Hilbert--Schmidt mass

For `0<h<N/2`, `0<=cot(pi h/N)/N<=1/(pi h)`. The antipodal cotangent entry is zero. Thus the full discarded tail `R_H=T-T_H` satisfies
\[
\|R_H\|_{\rm HS}^2
=2\sum_{H<h<N/2}J_y(h)w_N(h)^2
\le\frac2{\pi^2}\sum_{H<h<N/2}\frac{J_y(h)}{h^2}.
\tag{14}
\]
The factor two counts both matrix orientations of each unordered edge. Define
\[
G(h)=\prod_{\substack{p\mid h\\p>2}}\left(1+\frac1{p-2}\right).
\]
Since `G_y(h)<=G(h)` and `(log y)B_y` is bounded, (7) implies
\[
\alpha_y\|R_H\|_{\rm HS}^2
\le C\sum_{h>H}\frac{G(h)}{h^2}=:\varepsilon_H,
\qquad \varepsilon_H\longrightarrow0,
\tag{15}
\]
uniformly in `m` and in sufficiently large `y`. No uniform estimate for prime gaps is hidden here. Absolute summability follows directly by expanding over odd squarefree divisors:
\[
\sum_{h\ge1}\frac{G(h)}{h^2}
=\zeta(2)\prod_{p>2}\left(1+\frac1{p^2(p-2)}\right)<\infty.
\tag{16}
\]
Tonelli applies because all terms are nonnegative, and the product converges since its deviations from one are summable.

Unlike the inverse-square trace-norm tail of PC-151, (15) is a **squared Hilbert--Schmidt estimate for an indefinite kernel**. It does not assert that the tail tends to zero in operator norm, nor that every Lipschitz trace functional has a limit at this scale.

## 5. Threshold perturbation closes the all-radius passage

For Hermitian `A,B`, put `E=A-B`. For `delta>0`, spectral truncation writes `E=E_small+E_large`, with
\[
\|E_{\rm small}\|\le\delta,\qquad
\operatorname{rank}E_{\rm large}\le\delta^{-2}\|E\|_{\rm HS}^2.
\]
The min--max principle and finite-rank interlacing give
\[
n_+(B,t+\delta)-\delta^{-2}\|E\|_{\rm HS}^2
\le n_+(A,t)
\le n_+(B,t-\delta)+\delta^{-2}\|E\|_{\rm HS}^2.
\tag{17}
\]
Applying the same argument to `-A,-B` gives the negative-count version.

Choose `t>0` outside `mathcal A`, and then `0<delta<t/2` so that `[t-delta,t+delta]` contains no atomic point. For every sufficiently large fixed `H`, both finite sums in (13) at thresholds `t-delta` and `t+delta` equal the full finite sum in (3). Apply (17) to `A=T,B=T_H`, multiply by `alpha_y`, take `y->infinity`, and then `H->infinity`. Equations (13) and (15) squeeze both limits to (3). All estimates were uniform in `m`, so this proves the asserted uniformity as well.

Finally, `T^+-T=J_M/N` has rank one. Each threshold count differs by at most one; `alpha_y<=log y/varphi(d_y)->0`. This proves the augmented case without estimating its operator norm at the rare-count scale. For the raw matrix the two signed counts are also exactly equal, since complex conjugation sends `T` to `-T`. The augmentation need not preserve this exact finite symmetry.

## 6. Consequences, controls, and the remaining information

The theorem upgrades PC-458's `O(1/log y)` bound on the empirical mass outside a fixed neighborhood of zero to an exact step-function coefficient. It also shows why a finite number of local eigenvalues cannot determine the leading rare-count population. The common-space limits in [[research/prime_circle/findings/PC-459-primorial-cotangent-local-limits-split-into-anchor-pair-and-antipodal-dyadic-kernel]] concern particular vectors and spectral locations, whereas (3) resolves populations of order `M/log y` when its coefficient is nonzero.

There is an exact normalization check against PC-458. If
\[
A=\prod_p\left(1-\frac1{p(p-1)}\right),
\]
then the absolutely convergent Euler products give
\[
\sum_{\substack{h\ge1\\2\mid h}}\frac{\mathfrak S_2(h)}{h^2}
=\frac{\pi^2A}{6}.
\tag{18}
\]
To see the constants, the left side is `(C_2/2) zeta(2)` times the product in (16). Multiplying its odd-prime factors by those of `C_2` gives the odd-prime factors of `A`, whose omitted factor at `2` is `1/2`. The second moment of (4) is consequently `A e^-gamma/3`, exactly the limit of `alpha_y tr(T^2)` from PC-458. This is a check, not an inference of the counting law from a second moment.

The proof identifies a precise information-loss control: at this scale, the full matrix has the same nonzero counting limit as its isolated-edge models `D_H`, with `y->infinity` before `H->infinity`. The models deliberately retain the pair counts and edge weights while deleting higher local couplings. They are comparison matrices, not another full cotangent support, and they do not remove the arithmetic in `mathfrak S_2`. Thus the conclusion is classicalization of the **leading rare-count readout**, not blindness to all arithmetic.

In particular:

- At `t in mathcal A`, the theorem does not decide how the spectral cluster splits across the exact threshold.
- Above `1/(2 pi)`, the count is `o(M/log y)`; it need not be zero or bounded. There is no operator-norm upper bound of `1/(2 pi)` here.
- No assertion is made for `t=t(y)->0`, for individual eigenvalues/eigenvectors, or for the next `M/(log y)^2` population.
- The result does not identify a Fredholm determinant, a zeta-zero spectrum, or a critical-line selector. Applying further scalar transforms to these coefficients begins with the classical singular series already identified in PC-151.

## 7. Prior art and validation

The closest local results are PC-150's fixed-radius matching law and PC-151's full inverse-square trace law. Neither is a cotangent threshold-count theorem: the signed `1/h` edge kernel lacks their positive trace-norm comparison. The additional bridge here is (14)--(17), which closes the **full cotangent** problem at its first rare-count scale, for arbitrary complete refinements.

The external ingredients are classical:

- J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, **Bull. Amer. Math. Soc. 50** (2013), 527--628, [Theorem 3.3.2](https://arxiv.org/pdf/1303.1856), records the Mertens product theorem used in (8)--(9).
- D. A. Goldston and A. I. Suriajaya, *A singular series average and the zeros of the Riemann zeta-function*, **Acta Arith. 200** (2021), 71--90, [equations (1.1)--(1.2), author manuscript](https://arxiv.org/pdf/2007.16099), gives exactly the coefficient (2). Its later analytic continuation is a classical zero-sensitive channel, not a new consequence of these matrices.
- W. Ejsmont and F. Lehner, *The Trace Method for Cotangent Sums*, **J. Combin. Theory Ser. A 177** (2021), 105324, [author manuscript](https://arxiv.org/abs/2002.06052), supplies neighboring finite cotangent-matrix and trace theory, not this primorial rare-count limit.

Directed searches covered reduced-residue cotangent spectra, sieved Hilbert matrices, rare spectral counts and singular-series laws. They supply no basis for a historical priority claim. CRT, isolated-edge reduction, spectral truncation and interlacing are standard; the durable contribution is the stated analytic closure and its exact boundary in this line.

The proof is analytic, not Lean-verified. Standard-library Python checked **213 exact pair counts** and **180 exact triple counts** for primorial cutoffs `3,5,7,11`, refinements `1,2,3`, pair offsets through `20` where available, and distinct signed shifts from `{-6,-4,-2,2,4,6}`. Existing system LAPACK `zheev`, called through `ctypes`, checked **47** raw, augmented and short-window matrices of dimensions up to `480`: **162** rank-count inequalities and **324** tail perturbation inequalities passed. The largest absolute discrepancy in the directly summed Hilbert--Schmidt tail identity was below `2.3e-16`; the normalized second-moment and raw spectral-symmetry discrepancies were below `2.8e-17` and `3.9e-16`. These finite checks validate constants and conventions, not the asymptotic theorem. Scratch code remains outside Git.

The decisive audit points are unordered-edge versus matrix-entry factors, uniformity in the complete refinement, deleting collision rows without a positivity assumption, squared Hilbert--Schmidt rather than trace-norm control, threshold separation from atoms, the order of the two limits, and the rank-one augmented diagonal.
