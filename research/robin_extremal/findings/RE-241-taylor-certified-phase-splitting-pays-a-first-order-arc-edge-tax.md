# RE-241 — Taylor-certified phase splitting pays a first-order arc-edge tax

**Status:** EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-SERIAL-COMPOSITION + TAYLOR-CERTIFIED-LOCAL-OBSTRUCTION + RATIONAL-INTERVAL-CERTIFICATE + PRIOR-ART-AUDIT.

**Parent findings:** RE-218, RE-237, RE-239, RE-240.

RE-240 gives a genuine exponential Wiener-norm discount for two off-center negative-binomial factors with conjugate center phases. This does not automatically help separated prediction: moving the centers apart also enlarges the worst Taylor remainder on the observed arc. Here those effects are compared *within the family whose two factors are individually certified by the absolute Taylor-tail test used in RE-218*. At fixed radius and fixed arc width, the cost of splitting the phases is first order in the angular separation parameter, while the coefficient cancellation is second order. The certificate-optimal Wiener exponent therefore **increases** for every sufficiently small nonzero symmetric split.

The same calculation isolates a slightly sharper rational *unsplit* witness, improving the explicitly proved upper bound for the separated-prediction constant from 5.996390 to **strictly below 5.9960**. Neither statement is a global lower bound for all coupled predictors.

## 1. Precise certified family and its asymptotic rate

Fix

\[
0<\alpha<\frac{\pi}{2},
\qquad
\rho>\frac1{2\cos\alpha}.
\]

This ensures

\[
r(\theta):=
\frac{\sqrt{\rho^2+1-2\rho\cos\theta}}{\rho}
<1
\quad\text{at }\theta=\alpha,
\]

and also at \(\theta=\alpha+\beta\) for sufficiently small \(\beta\ge0\). Write

\[
h(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda,
\]

\[
\tau(\lambda,\theta)
=-\log\rho+h(\lambda)+\lambda\log r(\theta),
\qquad
\nu(\lambda,\rho)
=-\log\rho+h(\lambda)
+\lambda\log(1+\rho^{-1}).
\tag{1}
\]

These are respectively the absolute Taylor-tail exponent and the Wiener coefficient exponent in RE-218, both per Taylor order \(m\). Define \(\lambda_*(\beta)\) to be the root of

\[
\tau(\lambda_*(\beta),\alpha+\beta)=0,
\qquad
\lambda_*(\beta)>
\frac{r(\alpha+\beta)}{1-r(\alpha+\beta)}.
\tag{2}
\]

This *descending* root exists and is unique. Indeed

\[
\partial_\lambda\tau
=\log\!\left(r(\theta)(1+\lambda^{-1})\right),
\qquad
\partial_{\lambda\lambda}\tau
=-\frac1{\lambda(1+\lambda)}<0,
\]

and at the ratio threshold \(\lambda=r/(1-r)\),

\[
\tau=-\log\bigl(\rho(1-r)\bigr)>0,
\]

because \(\rho-|\,\rho-e^{i\theta}\,|<1\) for \(0<\theta<\pi\). As \(\lambda\to\infty\), \(\tau\to-\infty\) since \(r<1\). Consequently \(\tau<0\), with a uniformly subunit consecutive-tail ratio, holds for every fixed \(\lambda>\lambda_*(\beta)\).

Take centers

\[
a_\pm=\rho e^{\pm i\beta}
\]

and the normalized RE-237 polynomials \(F_\pm\) with the same order \(m\) and truncation \(N=\lceil\lambda m\rceil\). Choose a grid step \(\delta=\alpha/T\) and \(m=\lceil H/(2\delta)\rceil\). Then the product \(G=F_+F_-\) has real coefficients, exact DC value \(G(1)=1\), and support delays in

\[
[\,2m\delta,\;2(m+N)\delta\,]
\subseteq [\,H,\;(1+\lambda)H+o(1)\,].
\tag{3}
\]

For every fixed \(\lambda>\lambda_*(\beta)\), the absolute Taylor remainder of *each* factor tends uniformly to zero on \(|t|\le T\), with exponential rate \(\tau(\lambda,\alpha+\beta)<0\). Thus \(G\) is a valid factorwise-certified separated predictor, with \(O(T)\) real coefficients and a fixed delay corridor. The behavior at the boundary \(\lambda=\lambda_*(\beta)\) is only an **infimum of certified rates**; vanishing error is asserted at fixed strictly greater \(\lambda\), not at equality.

RE-218 and the exact RE-240 two-center norm law imply, uniformly for every sufficiently small fixed \(\beta\),

\[
\log\|F_\pm\|_A
=m\nu(\lambda,\rho)+o(m),
\]

\[
\log
\frac{\|F_+F_-\|_A}
{\|F_+\|_A\|F_-\|_A}
=N\log b(\rho,\beta)+O_\rho(\beta^2),
\]

where

\[
b(\rho,\beta)
=1-\frac{4\rho}{(1+\rho)^2}\sin^2(\beta/2).
\tag{4}
\]

Since \(2m\alpha=HT+O(1)\), the normalized asymptotic Wiener rate is exactly

\[
\boxed{
C_{\rm pair}^{\rm cert}(\lambda,\beta;\rho,\alpha)
=
\frac{\nu(\lambda,\rho)
+\frac{\lambda}{2}\log b(\rho,\beta)}{\alpha}
}
\qquad(\lambda>\lambda_*(\beta)).
\tag{5}
\]

The superscript denotes this specified **Taylor-tail-certified construction** and must not be confused with the universal constant \(C_{\rm sep}\).

## 2. The certificate-optimal rate has a positive one-sided derivative

Differentiating the numerator of (5) with respect to \(\lambda\) gives

\[
\partial_\lambda\left(\nu+\frac{\lambda}{2}\log b\right)
=
\log\!\left((1+\lambda^{-1})(1+\rho^{-1})\right)
+\frac12\log b.
\tag{6}
\]

This is positive for all \(\lambda>0\) whenever \(\beta\) is sufficiently small, since the first term is at least \(\log(1+\rho^{-1})>0\) and \(\log b=O(\beta^2)\). Hence the **infimum** of the certified rates (5) occurs as \(\lambda\downarrow\lambda_*(\beta)\):

\[
\mathcal C_{\rho,\alpha}^{\rm cert}(\beta)
:=
\frac{\nu(\lambda_*(\beta),\rho)
+\frac{\lambda_*(\beta)}2\log b(\rho,\beta)}{\alpha}.
\tag{7}
\]

Set \(r_0=r(\alpha)\), \(\lambda_0=\lambda_*(0)\). Implicit differentiation of (2), using

\[
\partial_\theta\log r(\theta)
=\frac{\sin\theta}{\rho r(\theta)^2},
\]

yields

\[
\lambda_*'(0+)
=
\frac{\lambda_0\sin\alpha}
{\rho r_0^2[-\log(r_0(1+\lambda_0^{-1}))]}
>0.
\tag{8}
\]

The cancellation factor in (4) obeys \(\log b(\rho,\beta)=O(\beta^2)\), so it contributes **no first-order term**. By contrast \(\partial_\lambda\nu=\log((1+\lambda^{-1})(1+\rho^{-1}))>0\). Therefore

\[
\boxed{
\mathcal C_{\rho,\alpha}^{\rm cert}(\beta)
=
\mathcal C_{\rho,\alpha}^{\rm cert}(0)
+K_{\rho,\alpha}\beta+O_{\rho,\alpha}(\beta^2),
\qquad \beta\downarrow0,
}
\tag{9}
\]

with the explicit positive coefficient

\[
\boxed{
K_{\rho,\alpha}
=
\frac{\lambda_0\sin\alpha}
{\alpha\rho r_0^2}
\frac{
\log[(1+\lambda_0^{-1})(1+\rho^{-1})]
}{
-\log[r_0(1+\lambda_0^{-1})]
}>0.
}
\tag{10}
\]

Swapping the two conjugate centers exchanges \(\beta\) and \(-\beta\), so the same expansion for a signed split has \(K_{\rho,\alpha}|\beta|\), not a nonzero signed derivative at the origin. This cusp is the *arc-edge tax*: one center must face the right-hand arc endpoint and the other the left-hand endpoint. Their worst contraction radii increase to first order in \(|\beta|\), while their coefficient-norm interference begins only at quadratic order.

Thus for **each fixed admissible** \((\rho,\alpha)\), a sufficiently small nonzero conjugate phase split cannot reduce the best achievable leading Wiener exponent *within this certification rule*. This does not assert a uniform neighborhood when \(\rho\) or \(\alpha\) varies with \(\beta\), and it does not assert that the absolute Taylor-tail test is necessary for actual predictor convergence.

For \(\rho=229/100,\;\alpha=13/25\), solving the descending root gives

\[
\lambda_0=3.9916164648\ldots,
\quad
\mathcal C_{\rho,\alpha}^{\rm cert}(0)
=5.9959483526\ldots,
\quad
K_{\rho,\alpha}=11.5510916\ldots .
\tag{11}
\]

These are diagnostics of the symbolic formula, not substituted numerical proof of the sign in (10).

## 3. A rational witness improves the live constructive bound

The exact boundary in (11) is an infimum and is not itself a certified decaying-tail construction. Instead choose the fixed rational depth

\[
\boxed{
\rho=\frac{229}{100},
\qquad
\alpha=\frac{13}{25},
\qquad
\lambda=\frac{79833}{20000}=3.99165.
}
\tag{12}
\]

For a **single unsplit stage**, choose \(m=\lceil HT/\alpha\rceil\), \(N=\lceil\lambda m\rceil\) as in RE-218. All numerical inequalities needed for this witness can be enclosed by rational arithmetic:

\[
0.65785242214654
<r(\alpha)
<0.65785242214655,
\]

\[
0.82265956258884
<r(\alpha)(1+\lambda^{-1})
<0.82265956258887<1,
\]

\[
-6.547\cdot10^{-6}
<\tau(\lambda,\alpha)
<-6.545\cdot10^{-6}<0,
\]

\[
\boxed{
5.99598613
<
\frac{\nu(\lambda,\rho)}{\alpha}
<
5.99598615
<5.9960.
}
\tag{13}
\]

For reproducibility, one exact rational enclosure method is to use the alternating cosine series at the rational \(\alpha\), including the sign and magnitude of the first omitted term, to bound \(r(\alpha)^2\); bracket its square root by the two displayed rational decimals. For every positive rational argument \(x\), use \(u=(x-1)/(x+1)\) and

\[
\log x
=
2\sum_{j=0}^{n-1}\frac{u^{2j+1}}{2j+1}
+E_n,
\qquad
|E_n|\le
\frac{2|u|^{2n+1}}{(2n+1)(1-u^2)}.
\tag{14}
\]

Taking \(n=70\), applying (14) at the rational endpoints for \(r\) and to \(\rho,\lambda,1+\lambda,1+\rho^{-1}\), and propagating rational intervals gives the bounds (13). This is a strict arithmetic certificate rather than floating-point optimization. The fixed negative margin of \(\tau\) and the subunit tail ratio imply exponentially vanishing uniform prediction error for sufficiently large \(m\). The support lies inside \([H,4.99165H+o(1)]\), preserving the fixed corridor and the regular spacing/real-coefficient interface of RE-218.

Consequently the existing RE-208 ordinary-prime realization applies with the same hypotheses as in RE-218, and the spectral bound sharpens to

\[
\boxed{
C_{\rm sep}<5.9960
}
\tag{15}
\]

(in contrast to RE-218's \(C_{\rm sep}\le5.996390\)). For \(H=\log 8\) its corresponding sufficient logarithmic height interval includes every

\[
c<
\frac{1}{2(5.9960)\log 8}
=0.0401015\ldots .
\tag{16}
\]

The result does not claim that the irrational infimum \(5.99594835\ldots\) is itself realized with a fixed exponential tail margin, though rational witnesses can approach it arbitrarily closely from above.

## 4. Adversarial boundaries and prior art

**Certification versus optimal prediction.** The test \(\tau<0\) with the descending tail ratio is a *sufficient absolute-value bound* for the individual Taylor remainders. Failure of that test does not prove a factor fails to approximate, and nothing here rules out cancellation inside a Taylor remainder or across the two remainders of a coupled product. A pair could conceivably work only jointly, below the individual threshold.

**Fixed parameter scope.** The positive derivative is proven at each fixed finite \(\rho\) and fixed arc \(\alpha\), not under all simultaneous radius/arc/phase retunings. The small-angle RE-240 norm formula is load-bearing; large phase separations lie outside (9).

**Scale and endpoints.** The asymptotic definition first fixes \(\rho,\alpha,\beta,\lambda\) and lets \(m\to\infty\), then approaches the certificate boundary in the rate infimum and examines \(\beta\downarrow0\). Rounding \(m,N\) changes the leading rates only by \(o(1)\). At \(\beta=0\), RE-237 gives zero Wiener discount exactly and (9) returns the unsplit rate. At \(\beta\ne0\), the two factors face opposite arc edges, explaining the \(|\beta|\) cusp. Choosing \(m\) so the *product* has minimum delay \(H\) prevents counting the double delay as a hidden benefit.

**Literature boundary.** Off-center Taylor approximation, Stirling entropy rates, conditioning of analytic continuation, the implicit-function theorem, and submultiplicativity in the Wiener algebra are standard. For related but different prediction/approximation objectives compare Geddes–Mason, *Polynomial Approximation by Projections on the Unit Circle*, SIAM J. Numer. Anal. **12** (1975), DOI 10.1137/0712011, and Xia–Nashed, *A method with error estimates for band-limited signal extrapolation from inaccurate data*, Inverse Problems **13** (1997), DOI 10.1088/0266-5611/13/6/015. Neither theorem is imported into the argument and neither controls this exact Wiener-cost/arc-edge trade-off. The mathematical contribution here is the explicit combination of RE-218's individual tail certificate with RE-240's sharp phase-interference rate and the independent strict rational improvement (12)--(15); no new external load-bearing theorem requires a SOURCES.md change.

## Research consequence

Within the symmetric, fixed-radius, **factorwise Taylor-certified** serial architecture, infinitesimal phase splitting is a rigorously losing move: the first-order enlargement of the worst observed-arc remainder dominates the second-order exponential coefficient cancellation. The quantitative example shows that a small improvement to the unsplit construction remains available without invoking phase interference.

What remains open is exactly what the two-center result does **not** control: genuinely nonperturbative phase splitting, optimizing with parameters that themselves vary, parallel/minimax coefficient synthesis, or a coupled predictor whose product—not its individual factors—satisfies the uniform approximation test. No new Robin inequality or RH implication follows from the certified obstruction alone.
