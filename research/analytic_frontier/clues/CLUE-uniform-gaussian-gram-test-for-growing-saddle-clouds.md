---
id: CLUE-analytic-frontier-uniform-gaussian-gram-test-for-growing-saddle-clouds
type: research-clue
status: resolved
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-115-binomial-packets-realize-exponential-source-unsaturation-at-an-interior-spectral-saddle.md
  - research/analytic_frontier/findings/ANF-117-sqrt-a-translation-clouds-defeat-every-fixed-saddle-phase-jet.md
  - research/analytic_frontier/findings/ANF-099-fixed-notch-ray-is-controlled-by-near-extremizer-exposure.md
---

# Can a uniform Gaussian Gram comparison decide growing-cloud source excision without truncating the phase jet?

## Observation

ANF-117 shows that every fixed saddle-phase jet can vanish while a positive physical translation cloud retains macroscopic source energy. Its Gaussian limit is proved for particular root clouds and fixed polynomial moments. Applying that limit to an arbitrary growing modulation is a different assertion: weak convergence against fixed tests does not justify integrating a scale-dependent, increasingly cancelling exponential sum.

There is a candidate replacement that keeps the entire modulation, rather than another finite jet. Compare the normalized source density with its Gaussian density multiplicatively on a widening saddle window, and charge the remaining tails against the total positive translation weight. Inside the window, the error is proportional to the already-cancelled quadratic energy, not to the square of the coefficient sum. Gaussian integration then makes the full observable an explicit positive-semidefinite Gram form.

## Research question

Freeze `gamma>0` and the exact ANF-115 packet `P_A`. Write
\[
a=\frac2\pi\arctan\frac1{\pi\gamma},\qquad
c=\frac{1+\pi^2\gamma^2}{2\gamma},\qquad
E_A=E_0(P_A),\qquad
F_\gamma(x)=x+2\gamma\log\cos(\pi x/2).
\]
Let a physical translation cloud have arbitrary real translations `tau_{j,A}` and positive integer weights `w_{j,A}`; repeated sites are retained as multiplicities. Put
\[
T_A=\bigsqcup_j w_{j,A}(P_A+\tau_{j,A}),\qquad
p_A(\alpha)=\sum_jw_{j,A}e^{-2\pi i\alpha\tau_{j,A}},\qquad
V_A=\sum_jw_{j,A}.
\tag{1}
\]
The notation `w(P+tau)` means a multiset of `w` copies, not dilation of coordinates. Define
\[
Z_A=\frac{E_0(T_A)}{E_A},\qquad
\mathcal G_A=\sum_{j,k}w_{j,A}w_{k,A}
 e^{-2\pi^2(\tau_{j,A}-\tau_{k,A})^2/(cA)}
 \cos\!\big(2\pi a(\tau_{j,A}-\tau_{k,A})\big).
\tag{2}
\]
Independently audit this proposed uniform comparison: for every fixed polynomial-weight budget `b>=0` and error exponent `d>0`, there is a constant depending only on `gamma,b,d` such that, for all sufficiently large `A` and **every** cloud with `V_A<=A^b`,
\[
\boxed{|Z_A-\mathcal G_A|
 \le C_{\gamma,b,d}\frac{(\log A)^{3/2}}{\sqrt A}\,\mathcal G_A
       +C_{\gamma,b,d}A^{-d}.}
\tag{3}
\]
No separation, bounded translation range, fixed number of distinct translates, or nonzero finite phase jet is assumed. Constants are not yet numerically certified. The proposed theorem is uniform in the cloud, with `gamma` fixed, not uniform as its saddle merges with zero or the spectral endpoint.

## Why it may matter

If (3) survives, `Z_A->0` is equivalent to `mathcal G_A->0` for every admitted sequence. If the Gaussian form remains bounded below, its relative error tends to zero. This gives a finite quadratic test for the full mesoscopic source profile, including ANF-117's cancellations, without guessing which finite jet will be sufficient.

The normalization remains important: this tests excision at scale `E_A`. It tests an ambient affine scale `L_A` directly when `E_A/L_A` is bounded above and below by positive constants; otherwise that ratio must be retained. It does not establish global near-extremality of a completion or the exposure inequality `beta_eta<B_eta`.

## Decisive test

**Reconstruct a quantitative density estimate before using the Gaussian matrix.** Let
\[
d\nu_A(\alpha)=\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{E_A}\,d\alpha.
\]
It is even. Condition on `alpha>0`, set `u=sqrt(A)(alpha-a)`, and call the resulting probability density `f_A(u)`, extended by zero outside its physical interval. Let
\[
\varphi_c(u)=\sqrt{\frac c{2\pi}}e^{-cu^2/2}.
\]
The needed strengthening of ANF-117 is the existence of constants `C,c_*,kappa>0`, depending only on `gamma`, such that for `1<=U<=kappa A^(1/6)`,
\[
\sup_{|u|\le U}\left|\frac{f_A(u)}{\varphi_c(u)}-1\right|
 \le C\frac{1+U^3}{\sqrt A}=:\epsilon_A(U),
\qquad
\int_{|u|>U}(f_A+\varphi_c)\,du\le Ce^{-c_*U^2}.
\tag{4}
\]
Choose `kappa` small enough that the local error is bounded, and use `U=o(A^(1/6))` for vanishing error.

Here is a direct route using the exact physical product, including its floor and distinctness perturbations. Set `n=floor(gamma A)` and `t_{k,A}=1/2+A^(-2)3^(-k)`. On a fixed neighborhood of `a` contained in `(0,1)`, ANF-115 gives
\[
\log\left(\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{|P_A|^2}\right)
 =A F_\gamma(\alpha)+B_A(\alpha),
\tag{5}
\]
where exactly
\[
\begin{split}
B_A(\alpha)={}&\log J_0(\alpha)-\log4
 +2\log(1+e^{-A\alpha})\\
&+2(n-\gamma A)\log\cos(\pi\alpha/2)\\
&+2\sum_{k=1}^{n}\left[
 \log\cos(\pi\alpha t_{k,A})-\log\cos(\pi\alpha/2)\right].
\end{split}
\tag{6}
\]
All cosines in (6) are positive on that fixed neighborhood for large `A`. The functions `B_A` and their first two derivatives are uniformly bounded there; `exp(B_A)` is bounded above and away from zero. The floor error is bounded and the sum of the perturbations is `O(A^-2)`. The exact convolution also supplies, for `0<=x<1`,
\[
J_0(x)=\frac{\sin(\sqrt2(1-x))/\sqrt2+(1-x)\cos(\sqrt2x)}
                 {4\sin^2(1/\sqrt2)},
\tag{7}
\]
so no unproved smoothness of `J_0` at the interior saddle is needed.

Taylor expansion of (5), using `F_gamma'(a)=0` and `F_gamma''(a)=-c`, gives local log-density error `O_gamma((|u|+|u|^3)/sqrt(A))`. Normalizing the integral adds `O_gamma(A^-1/2)`. Establish this last rate by integrating the Taylor remainder against a Gaussian majorant, not by using qualitative weak convergence.

For the tail, strict concavity controls a fixed saddle neighborhood. Away from it and before `alpha=1-A^-1`, the perturbed positive cosines are at most the unperturbed ones; the floor loses at most a polynomial factor. The fixed spectral gap absorbs that factor. In the remaining endpoint layer, every cosine has modulus `O(A^-1)`, giving `exp(-2 gamma A log A+O(A))` before normalization. Near `alpha=0`, use `cosh^2(A alpha/2)<=e^(A alpha)` and the strict gap `F_gamma(a)>F_gamma(0)`. These estimates supply the second part of (4); tiny endpoint zero crossings must not be fed into (6)'s logarithm. Recheck these uniform bounds as the main analytical acceptance gate.

**Compare nonnegative integrands before expanding any cancelling sum.** Real weights give `|p_A(-alpha)|=|p_A(alpha)|`, so conditioning on the positive saddle loses no factor of two:
\[
Z_A=\int_{\mathbb R}|p_A(a+u/\sqrt A)|^2f_A(u)\,du.
\tag{8}
\]
Gaussian Fourier integration gives exactly
\[
\int_{\mathbb R}|p_A(a+u/\sqrt A)|^2\varphi_c(u)\,du
 =\mathcal G_A\ge0.
\tag{9}
\]
This proves positive semidefiniteness of the matrix in (2), despite its potentially negative off-diagonal entries.

Use (4) on `|u|<=U` and `|p_A|<=V_A` outside. The proposed deterministic comparison is
\[
\boxed{|Z_A-\mathcal G_A|
 \le\epsilon_A(U)\mathcal G_A+CV_A^2e^{-c_*U^2}.}
\tag{10}
\]
For `V_A<=A^b`, choose `U^2=K log A` with `c_*K>2b+d`. This proves (3). The decisive order of operations is density comparison, integration of the squared **complete** modulation, and only then Gaussian expansion. Entrywise kernel error followed by a triangle inequality would instead cost `V_A^2` throughout and can fail exactly in ANF-117's cancellation regime.

The same argument has a useful larger envelope. If
\[
\log(e+V_A)=o(A^{1/3}),
\tag{11}
\]
choose `U_A^2` strictly between the scales `log(e+V_A)` and `A^(1/3)`, with its ratio to the first tending to infinity. Equation (10) then yields
\[
|Z_A-\mathcal G_A|\le o(1)\mathcal G_A+o(1).
\tag{12}
\]
This again decides vanishing versus a positive order-one source remainder. It does not give relative precision for energies smaller than the additive error. The exponent `1/3` is a sufficient Gaussian-window regime from the cubic remainder, not a claim of an optimal growth threshold.

**Keep the destination and the remaining completion problem separate.** For any fixed `0<eta<a`, let `E_eta` use the same fixed notch as ANF-099. ANF-115 supplies `d_(eta,gamma)=F_gamma(a)-F_gamma(eta)>0` and
\[
\frac{E_\eta(P_A)}{E_A}
 =\exp[-d_{\eta,\gamma}A+o(A)].
\]
Consequently every cloud obeys the elementary bound
\[
\boxed{\frac{E_\eta(T_A)}{E_A}
 \le V_A^2\exp[-d_{\eta,\gamma}A+o(A)].}
\tag{13}
\]
Under (11), a source-heavy cloud detected by (12) remains notch-negligible. This extends the fixed-jet examples to all admitted translation clouds, with no need to identify their limiting modulation. It does **not** make a source-heavy cloud removable from the source norm: cancellation with an external remainder can still matter. A fatal completion must therefore be tested jointly with that remainder; notch invisibility alone is not an excision theorem.

**Use two sharp controls, not just randomly chosen clouds.** First, substitute ANF-117's
\[
p_A(\alpha)=\left[\sum_{j=0}^{r_A-1}
 e^{-2\pi i\alpha j/(r_Aa)}\right]^s,
\qquad r_A/\sqrt A\to\rho,
\]
for any fixed `s`. All jets below order `s` vanish, but (9) must recover
\[
\mathcal G_A\longrightarrow
\frac{\rho^{2s}(2s-1)!!}{a^{2s}c^s}>0.
\tag{14}
\]
This is a calibration, not a new derivation of ANF-117's obstruction. Also test translations of size `sqrt(A)` or larger, where replacing the Gaussian damping in (2) by one is wrong.

Second, do not extend the comparison to arbitrary exponential weight growth. The positive physical cloud
\[
p_A(\alpha)=(1+e^{-\pi i\alpha})^{\lfloor\lambda A\rfloor},
\qquad V_A=2^{\lfloor\lambda A\rfloor},\quad\lambda>0,
\tag{15}
\]
changes the exact spectral rate to `F_(gamma+lambda)`, with saddle `a_(gamma+lambda)`, rather than `a_gamma`. Its true logarithmic source ratio tends to
\[
2\lambda\log2+f_{\gamma+\lambda}-f_\gamma,
\qquad f_g=F_g(a_g),
\tag{16}
\]
whereas the Gaussian proxy rate is
\[
\sup_{x\in\mathbb R}\left\{
2\lambda\log2+2\lambda\log|\cos(\pi x/2)|
 -\frac c2(x-a)^2\right\}.
\tag{17}
\]
These rates are genuinely different. By evenness and period-two reflection, the maximizer in (17) lies in `[0,1]`; strict concavity puts it in `(0,a)`. On that interval `F_gamma(x)-f_gamma> -c(x-a)^2/2`, since `|F_gamma''(x)|<|F_gamma''(a)|`. Evaluating the exact rate function at the proxy maximizer makes (16) strictly larger than (17). Thus the unrestricted extension has an exponential relative error, even with positive physical weights. This is a control against removing the growth hypothesis, not a counterexample to (3).

After validating (4) and (10), the actionable output is a uniform source-excision test for these clouds and the exact scope of (13). Do not turn a Gaussian matrix eigenvalue into a global certificate without an actual completion and the unchanged affine denominator.

## Evidence boundary

Research Watch independently reconstructed the exact packet product, proved the widening-window multiplicative density estimate and Gaussian tail bound, and derived the cancellation-safe comparison (10); the durable result is `ANF-118`. No numerically certified finite-`A` constants are claimed. No physical near-extremizer attaining fatal exposure, bound on `beta_eta`, improved unconditional zero proportion, or RH conclusion is established. Different packet shapes, mixed values of `gamma`, a moving saddle, exponentially large translation weights, and an uncontrolled ratio `E_A/L_A` require separate estimates.

The ingredients are classical Laplace asymptotics and the Gaussian Fourier transform. NIST DLMF, sections [2.3(iii)](https://dlmf.nist.gov/2.3.iii) and [2.4(iv)](https://dlmf.nist.gov/2.4.iv), provide the prior-art boundary for nondegenerate saddle expansions and their error discipline. They are not cited as proving (3) for this growing class. The Mathia-specific delta is the multiplicative density comparison that survives cancellation, yielding a uniform complete-profile Gram test where weak convergence and every fixed jet are inadequate.

Exploratory floating-point quadrature of the ANF-115 product at `gamma=1/2`, `A=200,800,3200`, for root clouds of orders `s=1,2,3` and a twelve-site spread cloud at each scale, supported the comparison's asymptotic behavior. For the third-order root cloud, `|Z_A/mathcal G_A-1|` was approximately `0.5014,0.1792,0.05095`: the finite-scale discrepancy is not automatically small. These are twelve numerical comparisons, not outward-rounded bounds or evidence for uniformity. The product was evaluated in logarithmic form; ternary perturbations through index 24 were retained and the remaining increments replaced by `1/2`, so this diagnostic is itself a numerical approximation. Analytical acceptance comes from the proof of (4)--(10), not from these samples.

The matrix in (2) may be ill-conditioned. Its mathematical positivity does not guarantee stable floating-point summation after large cancellations. Use the nonnegative integral (9), factorized modulation where available, or controlled-precision matrix evaluation; an apparent negative numerical quadratic value is not a physical counterexample.

## Research disposition
Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-118-uniform-gaussian-gram-comparison-controls-growing-interior-saddle-translation-clouds.md]]
