# PL-176 — Canonical additive-cube degree-four averaging is already Gowers-flat

## Claim

The first fixed logarithmic Walsh degree left uncontrolled by the theorem inputs in `PL-175` is even degree four, but the most canonical way to aggregate such a four-sign term over additive directions is already unconditionally flat.

Let

\[
\lambda(n)=(-1)^{\Omega(n)}=(-1)^{\sum_p v_p(n)}
\]

and define the positive additive-parallelogram sum

\[
P_N=\sum_{\substack{x,h,k\ge1\\x+h+k\le N}}
\lambda(x)\lambda(x+h)\lambda(x+k)\lambda(x+h+k).
\]

Then

\[
P_N=o(N^3),
\]

indeed for every fixed `A>0`,

\[
P_N\ll_A \frac{N^3}{(\log N)^A}+N^2.
\]

Since the number of positive triples `(x,h,k)` with `x+h+k<=N` is `binom(N,3)`, the normalized complete two-direction additive-cube average tends to zero.

The proof is not a new four-point Chowla theorem. It uses the classical uniform Davenport exponential-sum estimate and the exact Fourier identity

\[
\int_0^1\left|\sum_{n\le N}\lambda(n)e(n\theta)\right|^4d\theta
=4P_N+2N^2-N.
\]

Thus complete averaging over both additive directions turns the first apparently surviving degree-four affine channel into ordinary `U^2`/Fourier uniformity. Modern higher-uniformity theorems go much further: Liouville, and more generally nonpretentious bounded multiplicative functions, have asymptotically small higher Gowers norms on average in mesoscopic intervals. Consequently the standard additive-cube hierarchy is a generic pseudorandomness phenomenon, not a rational-prime or zeta-zero selector.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`. This is decisive only against **complete/diffuse additive-cube averaging** as the degree-four escape from `PL-175`. It does not control a fixed prescribed four-point correlation, a sparse/source-forced family of shifts, or a completed/target-relative coupling formed before the averaging.

## Exact Fourier identity

Extend the finite Liouville sequence by zero:

\[
f_N(n)=\lambda(n)\mathbf 1_{1\le n\le N},
\qquad
F_N(\theta)=\sum_{n\in\mathbf Z}f_N(n)e(n\theta)
=\sum_{n=1}^N\lambda(n)e(n\theta).
\]

Fourier orthogonality gives the standard additive-energy identity

\[
\int_0^1|F_N(\theta)|^4d\theta
=
\sum_{x,h,k\in\mathbf Z}
 f_N(x)f_N(x+h)f_N(x+k)f_N(x+h+k).
\]

For `h` and `k` both nonzero, the four sign quadrants are related by changes of base point and each contributes exactly the positive-parallelogram sum `P_N`. On the degenerate line `h=0`, every ordered pair of points of `[1,N]` contributes `1`, hence the contribution is `N^2`; the same is true for `k=0`; and the intersection `(h,k)=(0,0)` has been counted twice and contributes `N`. Therefore

\[
\boxed{
\int_0^1|F_N(\theta)|^4d\theta
=4P_N+2N^2-N.
}
\]

This identity is exact for every `N`. It is the finite `U^2` cube identity written so that the positive-direction degree-four Liouville statistic is visible separately from the degenerate faces.

## Davenport input and unconditional collapse

The required analytic input is the classical Davenport estimate for linear exponential sums with the Möbius function:

\[
\sup_{\theta\in\mathbf R}
\left|\sum_{m\le M}\mu(m)e(m\theta)\right|
\ll_A \frac{M}{(\log M)^A}
\]

for every fixed `A>0`.

The corresponding Liouville estimate follows directly from

\[
\lambda(n)=\sum_{d^2\mid n}\mu(n/d^2).
\]

Indeed,

\[
F_N(\theta)
=
\sum_{d\le\sqrt N}
\sum_{m\le N/d^2}\mu(m)e(md^2\theta).
\]

Split the outer sum at `d=N^{1/4}`. For `d<=N^{1/4}`, the inner length is at least `N^{1/2}`, so Davenport, uniformly in the phase `d^2 theta`, gives after summing `d^{-2}`

\[
\sum_{d\le N^{1/4}}
\left|\sum_{m\le N/d^2}\mu(m)e(md^2\theta)\right|
\ll_A \frac{N}{(\log N)^A}.
\]

For `d>N^{1/4}`, the trivial estimate gives

\[
\sum_{d>N^{1/4}}\frac{N}{d^2}
=O(N^{3/4}),
\]

which is smaller than `N/(log N)^A` for every fixed `A`. Hence

\[
\boxed{
\|F_N\|_{\infty}
\ll_A \frac{N}{(\log N)^A}.
}
\]

Parseval gives

\[
\int_0^1|F_N(\theta)|^2d\theta=N.
\]

Therefore

\[
\int_0^1|F_N(\theta)|^4d\theta
\le
\|F_N\|_\infty^2
\int_0^1|F_N(\theta)|^2d\theta
\ll_A \frac{N^3}{(\log N)^A},
\]

where the arbitrary logarithmic exponent has been renamed. Substitution into the exact identity yields

\[
P_N
=
\frac14\left(\int_0^1|F_N|^4-2N^2+N\right)
\ll_A \frac{N^3}{(\log N)^A}+N^2
=o(N^3).
\]

No unproved four-point Chowla estimate is used.

## Relation to the prime-exponent lattice

The sign `lambda(n)` is intrinsic to exponent coordinates:

\[
\lambda(n)=(-1)^{\langle v(n),\mathbf 1\rangle}.
\]

The extra operation in `P_N` is ordinary addition, already isolated in `PL-169` as genuinely external to multiplication/exponent-vector addition. The four vertices

\[
x,\quad x+h,\quad x+k,\quad x+h+k
\]

form the canonical two-dimensional additive cube. Thus `P_N` is a precise mixed object: exponent-lattice parity is sampled on an additive parallelogram and then averaged over every positive base point and every positive pair of directions allowed by the cutoff.

After `PL-175`, this is the most symmetric way to turn the first uncontrolled even Walsh degree into a global statistic. The exact fourth-moment identity shows why that symmetry is fatal: averaging over all directions diagonalizes the object by ordinary additive Fourier analysis. Davenport then supplies enough Fourier cancellation to make the entire normalized cube statistic vanish.

In operator notation, if

\[
J_h e_n=\lambda(n+h)e_n,
\]

then `P_N` is the complete positive-direction sum of finite traces of `J_0J_hJ_kJ_{h+k}` over the admissible base interval. The operator packaging does not add information; after summing all `(h,k)` it is exactly the same Fourier fourth moment.

## Modern higher-uniformity control

The negative is not special to this single fourth-moment calculation. Matomäki, Radziwiłł, Tao, Teräväinen, and Ziegler prove that for every fixed `k` and every fixed `theta>0`, Liouville has asymptotically vanishing local `U^{k+1}` norm on average over intervals `[x,x+H]` with `X^theta <= H <= X`. Their theorem is obtained in the more general setting of nonpretentious `1`-bounded multiplicative functions.

This supplies a matched-control obstruction stronger than merely saying that `P_N` is small. Standard fixed-dimensional additive cubes, when averaged in the usual Gowers fashion, are already part of a broad multiplicative pseudorandomness theory. They therefore fail the `prime_lattice` contract's discrimination test: the same flattening mechanism is not specific to the rational-prime source, the zeta functional equation, analytic continuation, or the critical line.

The theorem is local-on-average rather than a statement that every fixed shift tuple has zero correlation. That distinction is essential: Gowers uniformity controls averages over cube directions and does not prove the fixed even-order Chowla conjecture.

## Prior-art / novelty audit

This finding is deliberately a redirect, not a novelty claim.

- H. Davenport, “On some infinite series involving arithmetical functions (II),” *The Quarterly Journal of Mathematics* **os-8**(1) (1937), 313--320. DOI: https://doi.org/10.1093/qmath/os-8.1.313. This is the classical source of the uniform logarithmic-power exponential-sum estimate used above; the Liouville form is also obtained from the displayed square-divisor identity.
- Kaisa Matomäki, Maksym Radziwiłł, Terence Tao, Joni Teräväinen, Tamar Ziegler, “Higher uniformity of bounded multiplicative functions in short intervals on average,” *Annals of Mathematics* **197**(2) (2023), 739--857. DOI: https://doi.org/10.4007/annals.2023.197.2.3. This is the modern prior-art anchor showing that higher additive-cube/Gowers flattening holds on average for Liouville and, more generally, nonpretentious bounded multiplicative functions.
- Krishnarjun Krishnamoorthy, “On a conjecture of Corradi and Katai,” arXiv:2608.13266v1 [math.NT] (13 August 2026), https://arxiv.org/abs/2608.13266. This very recent preprint uses the Davenport bound and a fourth-moment Fourier method in a closely related Liouville additive-convolution problem. It is used only as a current-literature audit signal; the exact parallelogram identity and bound above are independently derived and do not rely on any unreviewed claim in the preprint.

The identity `int |F_N|^4 = additive energy` is standard Fourier/Gowers algebra, and the line-local reparameterization into `P_N` is elementary. The durable contribution here is therefore the **research exclusion**: the canonical complete degree-four additive-cube escape suggested by the information boundary in `PL-175` is already theoremically flat and is not a new route to RH.

## Adversarial checks and limitations

- **Not fixed four-point Chowla.** Nothing here proves that `lambda(n)lambda(n+h_1)lambda(n+h_2)lambda(n+h_3)` has zero Cesaro or logarithmic mean for an arbitrary fixed four-tuple of shifts.
- **Direction averaging is essential.** The collapse uses complete summation over both additive directions. A sparse, fixed, source-forced, or otherwise non-diffuse family can evade this exact fourth-moment reduction and needs its own theorem.
- **No analytic continuation.** The estimate is a finite additive Fourier statement. It does not continue a Dirichlet series through `Re(s)=1`, create a functional equation, or single out `Re(s)=1/2`.
- **No zeta-zero spectral claim.** `U^2` flatness is a pseudorandomness statement about Liouville signs, not a spectrum whose eigenvalues or resonances are zeta zeros.
- **Genericity is a negative control.** The modern higher-uniformity theorem applies beyond Liouville to nonpretentious bounded multiplicative functions, so the additive-cube carrier is not specific to rational primes.
- **Higher Gowers uniformity does not solve Chowla pointwise in the shifts.** The distinction between averaged cube directions and fixed configurations is exactly the residual boundary that must be preserved.
- **The `N^2` degeneracies matter.** They are retained explicitly in the exact identity rather than silently discarded; after normalization by `N^3` they are lower order.

## Consequence for the research line

`PL-175` should not be read as a recommendation to escalate blindly from degree three to degree four. Even though degree four is the first fixed logarithmic Walsh sector not killed by the cited Chowla theorems, the **canonical complete additive-parallelogram aggregation** of that sector is already unconditionally zero after normalization, and the broader Gowers hierarchy is known to flatten on average.

The active affine clue should therefore keep only degree-four/higher-even candidates whose configuration is independently source-forced **before** averaging: a fixed or sparse pattern, a justified non-diffuse/growing family outside the standard uniformity theorem, or a completed/target-relative coupling whose arithmetic information is not converted into ordinary Gowers averaging. Any proposal that merely sums the four-sign cube over all additive directions can now be rejected immediately by this finding.