# PC-457 — Growing-base cotangent towers require conductor-scale normalization

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. For the unchanged complete cotangent tower over `P_d^*`, the Haar operator norm is between `d/(2 pi)` and `d`, uniformly in the base conductor. Haar minimizes the norm among all bounded probability-measure realizations retaining the cylinder action. Consequently a scalar base normalization `s(d)>0` admits uniformly bounded realizations over a family of conductors exactly when `sup d/s(d)<infinity`. Averaging by the number of primitive vertices fails along primorials at order `log y`. This is a normalization obstruction, not a growing-base operator limit, spectral-distribution theorem, new prime discriminator or RH implication.

## 1. Objects and uniform statement

For integers `d>=2`, `m>=1`, set
\[
Y_{d,m}=\{e^{2\pi i a/(dm)}:0\le a<dm,\ (a,d)=1\},
\qquad r_d=\varphi(d),\qquad |Y_{d,m}|=mr_d.
\]
These are the complete power-map preimages of `P_d^*`. On this set retain the Hermitian matrices
\[
(C_{d,m})_{ab}=
\begin{cases}i\cot\dfrac{\pi(a-b)}{dm},&a\ne b,\\0,&a=b,\end{cases}
\qquad C_{d,m}^+=C_{d,m}+J_{mr_d}.
\tag{1}
\]
The all-ones term includes the diagonal. The refinement-compatible actions are `B_{d,m}^{(+)}=C_{d,m}^{(+)}/m`, as proved in [[research/prime_circle/findings/PC-443-coherent-profinite-cotangent-tower-has-atomic-bands-and-universal-marked-moduli]]. Let `B_d^{(+)}` denote their bounded self-adjoint extensions on the inverse-limit space with uniform base measure and Haar fiber measure. All norms below are operator norms; uniform probability and counting measure give the same finite-matrix norm.

**Theorem.** For each convention separately,
\[
\boxed{\frac{d}{2\pi}\le\|B_d^{(+)}\|
       =\sup_{m\ge1}\frac{\|C_{d,m}^{(+)}\|}{m}\le d.}
\tag{2}
\]
If `T_d` is any bounded realization of the same pointwise cylinder prescription on `L^2(nu_d)` for a Borel probability `nu_d`, then
\[
\|T_d\|\ge\|B_d^{(+)}\|.
\tag{3}
\]
In particular Haar attains the minimum possible norm over such realizations.

For any nonempty conductor family `D` and positive scalars `s(d)`, the following are equivalent:

- `sup_{d in D} d/s(d)<infinity`;
- the Haar family `B_d^{(+)}/s(d)` is uniformly bounded;
- there exists a uniformly bounded family of probability-measure realizations of `C_{d,m}^{(+)}/(m s(d))`, containing every cylinder function and retaining the unchanged entries.

No identifications between different base-conductor Hilbert spaces are required or supplied by this statement.

## 2. Full-polygon compression supplies the uniform upper bound

Put `N=dm`. The full `N`-gon cotangent matrix `F_N`, with the same zero diagonal as (1), has Fourier eigenvalues
\[
0\quad(j=0),\qquad N-2j\quad(1\le j<N).
\tag{4}
\]
This is the finite cotangent Fourier identity used in [[research/prime_circle/findings/PC-053-composite-cotangent-preimage-tubes-are-affine-base-inflations]], §3. Adding `J_N` changes only the constant eigenvalue, from zero to `N`. Thus
\[
\|F_N\|\le N,\qquad \|F_N+J_N\|=N.
\]
Both matrices in (1) are principal Hermitian compressions of these full-polygon matrices. Therefore
\[
\|C_{d,m}^{(+)}\|\le dm.
\tag{5}
\]
For completeness, the compression inequality follows by extending a vector by zero: if `E` is the coordinate isometry then `C=E^*FE`, so `||C||<=||F||`. This argument improves the coarse `||H_d||+||J||+2` estimate without invoking a general irregular Hilbert inequality.

The power-map pullbacks are isometries and intertwine the matrices divided by `m`. Cylinder functions have dense union. Hence the norm of the bounded compatible extension equals the supremum of the finite norms. Dividing (5) by `m` proves the upper half of (2).

## 3. Two retained vertices force the conductor scale

Whenever `dm>4`, both residues `1` and `dm-1` belong to `Y_{d,m}` and are distinct. Their angular separation across the common anchor is `2/(dm)`. The corresponding off-diagonal entries have magnitudes
\[
|(C_{d,m})_{1,dm-1}|=
 \left|\cot\frac{2\pi}{dm}\right|,
\qquad
|(C_{d,m}^+)_{1,dm-1}|=
 \left|\csc\frac{2\pi}{dm}\right|.
\tag{6}
\]
Every matrix entry is bounded by the operator norm, by testing a coordinate vector. For each **fixed** `d`, let `m` tend to infinity in (6):
\[
\lim_{m\to\infty}\frac1m\cot\frac{2\pi}{dm}
=\lim_{m\to\infty}\frac1m\csc\frac{2\pi}{dm}
=\frac{d}{2\pi}.
\tag{7}
\]
Together with the supremum identity this proves the lower half of (2). It also handles the singleton base `d=2`, where the two vertices lie in different lifts of the same base point; no distinct-base-point assumption is needed. The lower constant is not claimed optimal.

The use of all refinement levels matters. Equation (2) is a tower bound and does not assert the same lower constant at every small `m`; the raw two-vertex antipodal matrix, for example, vanishes.

## 4. Changing the probability cannot remove the lower bound

[[research/prime_circle/findings/PC-446-raw-cotangent-tower-measures-cannot-remove-spectral-bands]], §§2--3, proves that well-definedness on all cylinder classes forces full support of `nu_d`, and that every finite cylinder eigenvector then remains a nonzero Hilbert-space vector. Multiplication by the nonzero scalar `1/s(d)` does not change that argument.

Every eigenvalue of `C_{d,m}^{(+)}/m` is therefore an eigenvalue of `T_d`. Since the finite matrices are Hermitian in uniform measure, their spectral radii equal their Euclidean operator norms. Boundedness of `T_d`, without any symmetry assumption in `L^2(nu_d)`, gives
\[
\|T_d\|\ge\max_{\lambda\in\sigma(C_{d,m}^{(+)}/m)}|\lambda|
=\frac{\|C_{d,m}^{(+)}\|}{m}.
\]
Taking the supremum proves (3). In particular an ill-conditioned change of Hilbert norm cannot shrink the required family scale. Conversely Haar and (5) supply uniformly bounded realizations whenever `sup d/s(d)` is finite, proving the equivalences.

This does not classify uniform resolvent bounds of unbounded realizations or closability for arbitrary probabilities. The fixed-base nonempty-resolvent classification in [[research/prime_circle/findings/PC-456-one-resolvent-point-forces-every-finite-base-cotangent-tower-bounded]] is consistent with the result but is not needed for this proof.

## 5. Cardinality averaging and matched controls

Dividing by the number `mr_d` of tube vertices corresponds exactly to `s(d)=varphi(d)`. Equation (2) gives
\[
\frac1{2\pi}\frac d{\varphi(d)}
\le\left\|\frac{B_d^{(+)}}{\varphi(d)}\right\|
\le\frac d{\varphi(d)}.
\tag{8}
\]
Thus cardinality averaging is uniformly bounded on a conductor family precisely when its reciprocal totient ratios are bounded. Repeated powers of a fixed prime satisfy this criterion. Primorials `d_y=prod_{p<=y}p` do not: Mertens's classical product theorem gives
\[
\frac{d_y}{\varphi(d_y)}
=\prod_{p\le y}(1-1/p)^{-1}\sim e^\gamma\log y,
\qquad
\left\|\frac{B_{d_y}^{(+)}}{\varphi(d_y)}\right\|\asymp\log y.
\tag{9}
\]
Only the ratio has the stated asymptotic constant; no norm asymptotic constant follows from these bounds. By contrast division by the conductor `dm` gives norm at most one for every base and every refinement.

The mechanism is not specific to primitive extraction. Take any base subset of the `d`-gon containing both `e^{2 pi i/d}` and `e^{-2 pi i/d}`, and form all its power preimages. Full-polygon compression and the same two retained vertices prove (2), with `d` unchanged and the base cardinality replacing `varphi(d)` in (8). When these points coincide at `d=2`, the singleton argument still applies. For example a nonprimitive subset of the `30`-gon of size `8`, containing residues `0,1,2,3,4,5,6,29`, has the same cardinality and the same bounds as `P_30^*`. The rest of the support affects the detailed spectrum, but is unnecessary for the norm inflation. A matched arbitrary subset of the same cardinality with the retained pair reproduces its order.

## 6. Prior art, mathematical delta and boundary

Finite cotangent Fourier diagonalization and Hermitian compression are classical; PC-053 already supplies the required exact transform. Montgomery--Vaughan, *Hilbert's Inequality*, **J. London Math. Soc. (2) 8** (1974), 73--82, [DOI](https://doi.org/10.1112/jlms/s2-8.1.73), and Preissmann--Lévêque, *On generalized weighted Hilbert matrices*, **Pacific J. Math. 265** (2013), 199--219, [§2](https://msp.org/pjm/2013/265-1/pjm-v265-n1-p09-p.pdf), locate separation-controlled cotangent/Cauchy estimates in the classical Hilbert-inequality setting. Their general estimates are neighboring prior art, not a necessary premise of (5)--(7).

Mertens's product theorem is recorded as Theorem 3.3.2 in Jeffrey C. Lagarias, *Euler's constant: Euler's work and modern developments*, **Bull. Amer. Math. Soc. 50** (2013), 527--628, [author manuscript](https://arxiv.org/pdf/1303.1856). This is the only external asymptotic input in (9).

The literature and local-corpus audit covered cotangent Fourier matrices, primitive-shell compressions, separation bounds and totient/Mertens normalization. No new general matrix or prime-product theorem, or historical priority, is claimed. The local delta is a **uniform growing-base normalization criterion**, including its measure-independent necessity, rather than another fixed-base classification: total-vertex averaging cannot make the complete primorial tower family uniformly bounded, already because of two retained anchor-neighbor vertices. The fixed-base limits of PC-099/PC-443 and the fixed-base weight theorem of PC-456 do not themselves state this family criterion.

This closes only the uniformly bounded, unchanged-action, scalar-normalization question. Unbounded common-space limits, resolvent convergence, additional source-forced couplings, modified kernels and incomplete fibers require their own constructions and estimates. In particular the uniform conductor-scaled bound does not construct a limit or erase the remaining base spectral data; the lack of a uniform cardinality-scaled bound does not rule out strong-resolvent limits of unbounded operators. No new zeta identity, zero exclusion or downstream proof-search utility is established.

## 7. Validation

The proof is analytic and has not been Lean-verified. Standard-library Python diagnostics checked all **629** full-polygon Fourier eigenvector identities for `2<=N<=35`, with maximum absolute residual below `8.7e-13`. Another **94** restricted raw/augmented matrix cases tested cardinalities, the two entries in (6), and the compression bound on deterministic vectors: primitive bases `d=2,3,4,5,6,8,10,12,15,30,210` at `m=1,2,3,7`, plus nonprimitive same-cardinality controls at `d=12,30,60`, `m=3`. The vector tests are finite diagnostics, not a proof of an operator-norm upper bound. Equation (5) supplies that proof. At `m=10000` and `d=2,3,6,30,210,2310,30030`, the raw expression in (7) divided by `d/(2 pi)` lay between `0.9999999671` and `1`.

The decisive audit points are the full augmented diagonal in (1), taking a supremum over refinement levels before applying the two-point limit, preserving finite eigenvectors under measure changes, and distinguishing the two-sided order estimate in (9) from a sharp norm asymptotic. Scratch computations are not canonical evidence beyond these normalization checks.
