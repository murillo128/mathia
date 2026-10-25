# PC-458 — Conductor-scaled cotangent bulk collapses exactly at vanishing primitive density

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. For the complete cotangent preimage tubes, division by the ambient conductor gives an empirical eigenvalue law tending to a point mass at zero **if and only if** the primitive-base density tends to zero, provided the ambient conductor tends to infinity. This criterion holds for arbitrary simultaneous base/refinement sequences, for both raw and augmented kernels. On primorial bases the squared Wasserstein-2 distance to zero is asymptotic to `A exp(-gamma)/(3 log y)`, uniformly in refinement depth, where `A` is Artin's classical constant. The operator norms nevertheless stay bounded away from zero. The result closes this growing-base **bulk-law** question; it does not construct a common-space operator limit or eliminate exceptional spectral information.

## 1. Exact finite statement

For integers `d>=2`, `m>=1`, put
\[
N=dm,\qquad r=\varphi(d),\qquad M=mr,\qquad
Y_{d,m}=\{e^{2\pi i a/N}:0\le a<N,\ (a,d)=1\}.
\]
On these `M` vertices let
\[
C_{ab}=\begin{cases}
i\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T=\frac CN,\qquad T^+=\frac{C+J_M}N.
\tag{1}
\]
Here `J_M` has every entry equal to one, including its diagonal. Both matrices are Hermitian. Their empirical spectral measures assign mass `1/M` to each eigenvalue, with multiplicity; denote them by `nu_(d,m)` and `nu^+_(d,m)`.

Define
\[
\eta(d)=\frac{\varphi(d)}d,\qquad
Q(d)=\prod_{p\mid d}\left(1-\frac1p-\frac1{p^2}\right),\qquad
A(d)=\prod_{p\mid d}\left(1-\frac1{p(p-1)}\right).
\tag{2}
\]
There are exact identities
\[
Q(d)=\eta(d)A(d),
\tag{3}
\]
\[
\boxed{\begin{aligned}
\int t^2\,d\nu_{d,m}(t)
 &=\frac{Q(d)}3-\frac{M}{N^2}+\frac2{3N^2},\\
\int t^2\,d\nu^+_{d,m}(t)
 &=\frac{Q(d)}3+\frac2{3N^2}.
\end{aligned}}
\tag{4}
\]
In particular these are the exact squared Wasserstein-2 distances to `delta_0`: transporting any probability measure to one point has cost equal to its second moment.

For **any** sequence `(d_j,m_j)` with `N_j=d_j m_j -> infinity`, and for each kernel convention separately,
\[
\boxed{\quad
\nu^{(+)}_{d_j,m_j}\Longrightarrow\delta_0
\quad\Longleftrightarrow\quad
\frac{\varphi(d_j)}{d_j}\longrightarrow0.
\quad}
\tag{5}
\]
No nesting of the bases and no ordering between the two growing parameters is assumed.

## 2. Pair counting and the second moment

For a residue `h mod N`, the number of ordered retained pairs of difference `h` is
\[
R_{d,m}(h)
=\#\{a\bmod N:(a,d)=(a-h,d)=1\}
=M b_d(h),
\]
where CRT at every prime power dividing `d` gives
\[
b_d(h)=\prod_{p\mid d}
\left(\frac{p-2}{p-1}+\frac{\mathbf1_{p\mid h}}{p-1}\right).
\tag{6}
\]
This is the same elementary residue-pair count as in [[research/prime_circle/findings/PC-136-cross-shell-only-primorial-hessian-has-universal-bulk-spectrum-with-mertens-squared-defect]], now repeated over the `m` lifts. It remains valid when `m` shares prime factors with `d`; no coprimality is required. Also `b_d(0)=1` and
\[
\sum_{h=1}^{N-1}b_d(h)=M-1.
\tag{7}
\]
Indeed the sum including zero counts all `M^2` ordered pairs, divided by `M`.

Write `R=rad(d)` and expand
\[
b_d(h)=\sum_{q\mid R}c_q\mathbf1_{q\mid h},\qquad
c_q=\prod_{p\mid q}\frac1{p-1}
     \prod_{p\mid R/q}\frac{p-2}{p-1}.
\tag{8}
\]
All coefficients are nonnegative, including when `p=2` makes some vanish. Since every `q|R` divides `N`, the classical finite cosecant identity gives
\[
\sum_{\substack{1\le h<N\\q\mid h}}
\csc^2\frac{\pi h}N
=\frac{(N/q)^2-1}{3}.
\tag{9}
\]
For completeness, differentiate the logarithm of the finite sine-product formula to obtain
`sum_(k=0)^(L-1) csc^2(x+k pi/L)=L^2 csc^2(Lx)`.
Subtract `csc^2(x)` and let `x -> 0`; the constant term of `csc^2(x)` is `1/3`. This proves (9), also for `L=N/q=1`, when the sum is empty.

Now `sum c_q=1` and
\[
\sum_{q\mid R}\frac{c_q}{q^2}
=\prod_{p\mid d}\frac{p-2+p^{-2}}{p-1}
=Q(d).
\]
Thus (8)--(9) imply
\[
\sum_{h=1}^{N-1}b_d(h)\csc^2\frac{\pi h}N
=\frac{N^2Q(d)-1}{3}.
\tag{10}
\]
Hermiticity and `cot^2=csc^2-1` give
\[
\frac{\operatorname{tr}C^2}{M}
=\sum_{h=1}^{N-1}b_d(h)\cot^2\frac{\pi h}N
=\frac{N^2Q(d)}3-M+\frac23.
\tag{11}
\]
Finally `tr(C J_M)=0`, since the off-diagonal entries cancel in opposite ordered pairs, and `tr(J_M^2)=M^2`. Dividing (11) and its augmented version by `N^2` proves (4). The factorization in (3) holds prime by prime.

At `m=1`, (11) is also obtained from PC-136's primitive-shell chord energy using `cot^2=4/(4 sin^2)-1`. Its Artin factor is already recognized in [[research/prime_circle/findings/PC-140-primitive-shell-hessian-trace-classicalizes-to-artin-nicolas]]. Neither the underlying pair count nor the appearance of Artin's constant is a new arithmetic discovery.

## 3. Why the criterion is necessary as well as sufficient

The full `N`-gon cotangent matrix has eigenvalues `0` and `N-2k`, `1<=k<N`; its augmentation replaces the constant eigenvalue by `N`. The matrices in (1) are principal compressions divided by `N`, so
\[
\|T\|\le1,\qquad\|T^+\|\le1.
\tag{12}
\]
This is the full-polygon compression argument of [[research/prime_circle/findings/PC-457-growing-base-cotangent-towers-require-conductor-scale-normalization]]. Consequently all empirical laws are supported in the fixed interval `[-1,1]`. On this interval weak convergence to `delta_0` is equivalent to the second moment tending to zero: necessity follows by testing the bounded continuous restriction of `t^2`, and sufficiency follows from
\[
\nu^{(+)}_{d,m}(\{|t|\ge\varepsilon\})
\le\varepsilon^{-2}\int t^2\,d\nu^{(+)}_{d,m}(t).
\tag{13}
\]

The absolutely convergent product
\[
A=\prod_p\left(1-\frac1{p(p-1)}\right)>0
\]
provides uniform bounds
\[
A\le A(d)\le1,\qquad A\eta(d)\le Q(d)\le\eta(d).
\tag{14}
\]
Positivity of `A` follows because the factor at `2` is positive and the remaining logarithmic deficits are summable. Since `M<=N`, the correction terms in (4) vanish as `N -> infinity`; (3), (4) and (14) prove (5).

This excludes collapse for fixed bases with `m -> infinity`, and for growing powers of a fixed prime, since their primitive densities stay positive. It is consistent with [[research/prime_circle/findings/PC-099-growing-complete-cotangent-tube-spectrum-converges-to-uniform-bands]], which takes a fixed base and uses the different scaling `1/m`. The condition `N -> infinity` is necessary: the raw singleton `(d,m)=(2,1)` is already the zero matrix while `eta(2)=1/2`.

## 4. Primorial rate, surviving extremes, and a control

Let `d_y=prod_(p<=y) p`, with `y -> infinity`, and allow **any** `m=m(y)>=1`. By Mertens's product theorem and the convergence of `A(d_y)` to `A`,
\[
Q(d_y)\sim\frac{A e^{-\gamma}}{\log y}.
\]
The relative correction in (4) is uniformly negligible: `M/N^2=eta(d_y)/N`, while `1/(N^2 eta(d_y))=1/(NM)<=1/N`. Therefore
\[
\boxed{\quad
W_2(\nu^{(+)}_{d_y,m(y)},\delta_0)^2
\sim\frac{A e^{-\gamma}}{3\log y},
\quad}
\tag{15}
\]
uniformly over all refinement choices. In particular the fraction of eigenvalues outside any fixed neighborhood of zero is `O(1/log y)` by (13); (15) is not an asymptotic formula for that fraction.

Bulk collapse does **not** imply norm collapse. For `N>4`, residues `1` and `N-1` are both retained, and their off-diagonal entries give
\[
\|T\|\ge\frac1N\cot\frac{2\pi}N,\qquad
\|T^+\|\ge\frac1N\csc\frac{2\pi}N.
\tag{16}
\]
Thus along every sequence with `N -> infinity`, both norms have lower limit at least `1/(2 pi)`. In the collapsing regime some extreme eigenvalues persist inside a vanishing fraction of the total eigenvalue count. No bound on their exact count, limiting locations, or eigenvectors follows here.

A control separates the weak bulk conclusion from the finer information. Replace the primitive base by the equally spaced `r`-gon and take its complete `m`-fold preimages, the regular `M`-gon. Use the same circle, the same cotangent kernel, the same number `M` of vertices and the same numerical scaling `1/N`. Its two normalized operator norms are at most `M/N=eta(d)`, so its entire spectrum tends to zero when `eta(d)->0`. This control reproduces the limiting point mass without the primitive sieve. It does **not** match the primitive pair correlations or the fixed ambient `N`-gon embedding in general, and (16) shows that it does not match the extreme spectrum. Therefore only the weak bulk readout is control-blind; the surviving spectral data have not been proved irrelevant or universal.

## 5. Prior art, delta, and evidence boundary

The proof combines classical finite trigonometric sums, CRT and a second-moment concentration argument. N. Gauthier and P. S. Bruckman, *Sums of the even integral powers of the cosecant and secant*, **Fibonacci Quarterly 44** (2006), DOI [10.1080/00150517.2006.12428317](https://doi.org/10.1080/00150517.2006.12428317), supplies the neighboring trigonometric power-sum literature; (9) was derived directly above. W. Ejsmont and F. Lehner, *The Trace Method for Cotangent Sums*, **J. Combin. Theory Ser. A 177** (2021), 105324, [author manuscript](https://arxiv.org/abs/2002.06052), treats finite cotangent matrices and trace methods, without supplying this primitive-tube growing-base theorem.

P. Moree, *Artin's Primitive Root Conjecture — A Survey*, **Integers 12** (2012), [§1, author manuscript](https://arxiv.org/pdf/math/0412262), identifies the standard constant `A`. J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, **Bull. Amer. Math. Soc. 50** (2013), 527--628, [Theorem 3.3.2](https://arxiv.org/pdf/1303.1856), records Mertens's product theorem, the only external asymptotic input to (15). No primitive-root conjecture or RH assumption is used.

The local audit distinguishes PC-136/PC-140's existing chord-energy identity, PC-099's fixed-base band limit, PC-443's fixed-base profinite spectral type, and PC-457's uniform norm scale. The additional conclusion is the **necessary-and-sufficient growing-base empirical collapse criterion, uniform in refinement**, with an exact rate and an explicit nonvanishing-norm boundary. The trace identity is a classical specialization used to settle that previously unspecified topology, not a new Euler product or an independent RH mechanism. Searches by cotangent/reduced-residue spectra, finite cosecant energies and discrete Hilbert-transform spectral distributions gave no basis for a historical novelty claim.

These empirical probabilities use normalized finite matrix traces. They do not identify the spectral type of a common-space limit, a normal-state distribution of a profinite tower, or strong/resolvent convergence across bases. PC-443 already warns that empirical and vector spectral measures can differ. An amplified residual statistic, a statistic selecting exceptional modes, incomplete fibers or a genuinely different source-forced coupling is outside (5). Neither the limit law nor its classical rate gives zero exclusion or a new route to RH.

## 6. Validation and audit surface

The argument is analytic and has not been Lean-verified. Independent standard-library Python diagnostics explicitly summed matrix-entry squares for all `2<=d<=60`, `m in {1,2,3,5}`: **236** matrices, **472** raw/augmented trace checks. The largest absolute error in the normalized raw trace was below `3.1e-14`. Every ordered-pair count in those cases agreed exactly with (6), using rational arithmetic; (3) also held exactly. This includes singleton and antipodal degeneracies, repeated prime powers and refinements sharing prime divisors with the base. Numerical eigenvalue tests were not run because NumPy was unavailable; they are unnecessary for the analytic compression and trace proofs.

The decisive audit points are the ordered-pair normalization by `M`, excluding `h=0` before applying the singular kernel, the augmented diagonal and its `M^2` trace contribution, uniformity in arbitrary `m(y)`, the necessity of `N -> infinity`, and the distinction between vanishing empirical mass and a vanishing norm. Scratch diagnostics are not a substitute for these proofs.
