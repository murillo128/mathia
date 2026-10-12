# RE-242 — Coupled conjugate Taylor predictors have a locally sharp arc-edge threshold

**Status:** EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-COUPLED-PREDICTION + SHARP-LOCAL-THRESHOLD + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDIT.

**Parent findings:** RE-218, RE-239, RE-240, RE-241.

RE-241 proves that a small symmetric phase split loses at first order if the two negative-binomial Taylor factors must separately pass a **strictly exponentially decaying absolute-tail certificate**. That condition was sufficient, not known to be necessary for the *coupled product*. Here the exact complex Taylor tail is controlled without discarding its phase. In a fixed neighborhood of the far-arc threshold, the product's actual uniform prediction error has the same exponential rate as its more exposed constituent and an additional sharp factor of \(m^{-1/2}\). Thus a coupled product cannot exploit cancellation to predict below the threshold **locally**, while the threshold itself already gives uniform prediction with algebraic error.

This sharpness is for fixed, distinct, sufficiently close conjugate phases and the specified equal-depth Taylor family; it is not a universal minimax lower bound for separated prediction.

## 1. Exact theorem

Fix \(0<\alpha<\pi/2\), \(\rho>0\), and a fixed split \(0<\beta<\alpha/2\), sufficiently small that

\[
r_f:=r(\alpha+\beta)<1,\qquad
r(\theta):=\frac{|\rho-e^{i\theta}|}{\rho}
=\left|1-\rho^{-1}e^{i\theta}\right|.
\]

The condition is equivalent to \(\rho>1/(2\cos(\alpha+\beta))\); if the RE-240 Wiener asymptotic is invoked, also keep \(\beta\) in its small-phase interval. Write

\[
h(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda,\qquad
\tau(\lambda,\theta)=-\log\rho+h(\lambda)+\lambda\log r(\theta).
\tag{1}
\]

Let \(\lambda_f\) be the unique **descending** root

\[
\tau(\lambda_f,\alpha+\beta)=0,\qquad
\lambda_f>\frac{r_f}{1-r_f}.
\tag{2}
\]

For \(m\ge1\), \(N=\lceil\lambda m\rceil\), and \(a_\pm=\rho e^{\pm i\beta}\), set

\[
Q_{\pm,m}(z)=
z^m a_\pm^{-m}
\sum_{k=0}^{N}\binom{m+k-1}{k}
\left(1-\frac z{a_\pm}\right)^k,
\qquad
G_m(z)=\frac{Q_{+,m}(z)Q_{-,m}(z)}
{Q_{+,m}(1)Q_{-,m}(1)}.
\tag{3}
\]

There exists \(\varepsilon>0\) such that, for every fixed \(\lambda\in(\lambda_f-\varepsilon,\lambda_f+\varepsilon)\), the denominator in (3) is nonzero for all sufficiently large \(m\), and constants \(0<c_\lambda<C_\lambda<\infty\) give

\[
\boxed{\quad
c_\lambda m^{-1/2} e^{m\tau(\lambda,\alpha+\beta)}
\le
\sup_{|\theta|\le\alpha}|G_m(e^{i\theta})-1|
\le
C_\lambda m^{-1/2} e^{m\tau(\lambda,\alpha+\beta)}.
\quad}
\tag{4}
\]

Consequently, **within this local interval**:

- \(\lambda>\lambda_f\): the coupled predictor error decays exponentially;
- \(\lambda=\lambda_f\): its uniform error is \(\asymp m^{-1/2}\), hence still tends to zero;
- \(\lambda<\lambda_f\): its uniform error grows exponentially and the coupled product fails to predict.

The strict-tail certificate of RE-241 is therefore locally necessary for *exponential decay* but **not** for convergence. The coupled-product threshold is sharp locally even though neither factor is assumed to pass its individual certificate when \(\lambda<\lambda_f\).

## 2. The complex negative-binomial tail keeps its first-term exponent

Put \(B_m(k)=\binom{m+k-1}{k}\) and \(u_a(z)=1-z/a\). Since \(r_f<1\), the binomial series converges on the entire observed arc, and its **exact** omitted remainder is

\[
E_{a,m}(z):=1-Q_{a,m}(z)
=z^m a^{-m}\sum_{k=N+1}^{\infty}B_m(k)u_a(z)^k.
\tag{5}
\]

With \(K=N+1\), factor out the first omitted term:

\[
E_{a,m}(z)=z^m a^{-m}B_m(K)u_a(z)^K S_m(u_a(z)),
\]

\[
S_m(u)=\sum_{j=0}^{\infty}
\frac{B_m(K+j)}{B_m(K)}u^j,\qquad
\frac{B_m(K+j)}{B_m(K)}
=\prod_{\ell=0}^{j-1}
\frac{m+K+\ell}{K+1+\ell}.
\tag{6}
\]

The ratios in the product decrease with \(\ell\), so their maximum is
\((m+K)/(K+1)\to(1+\lambda)/\lambda=:c_\lambda^\ast\).
Equation (2) gives \(c_{\lambda_f}^\ast r_f<1\). Thus, after shrinking the fixed neighborhood of \(\lambda_f\), there is a common \(\kappa<1\) such that every summand in (6) is dominated in modulus by \(\kappa^j\) for \(|u|\le r_f\). Termwise convergence plus the geometric majorant yields **uniformly** on that closed disk

\[
\boxed{\quad
S_m(u)\longrightarrow \frac{1}{1-c_\lambda^\ast u}.
\quad}
\tag{7}
\]

The limit is finite and nowhere zero on the disk. Thus \(S_m\) is bounded above and bounded away from zero there for large \(m\). There is no exponentially hidden cancellation within the complex Taylor tail: its first omitted term gives the exact exponential magnitude.

Stirling's formula with \(K=\lambda m+O(1)\) gives

\[
B_m(K)\asymp_\lambda m^{-1/2}e^{m h(\lambda)}.
\tag{8}
\]

The ceiling only changes a bounded prefactor. Using \(|z|=1\), (5)--(8) imply the uniform upper bound

\[
|E_{a_\pm,m}(e^{i\theta})|
\le C_\lambda m^{-1/2}
e^{m\tau(\lambda,|\theta\mp\beta|)}
\le C_\lambda m^{-1/2}
e^{m\tau(\lambda,\alpha+\beta)}.
\tag{9}
\]

At either far endpoint, where \(|\theta\mp\beta|=\alpha+\beta\), \(u\ne0\), and the nonzero limit (7) also gives the matching **lower** bound. These estimates remain valid when the last exponent is positive: they are asymptotics for the exact finite Taylor polynomial's error, not claims that it approximates in that regime.

## 3. Why coupling cannot cancel the exposed endpoint

The function \(r(\theta)\) is strictly increasing for \(0<\theta<\pi\). In particular, at \(\lambda=\lambda_f\),

\[
\tau(\lambda_f,\alpha-\beta)<0,\qquad
\tau(\lambda_f,\beta)<0.
\tag{10}
\]

By continuity these remain strictly negative throughout a sufficiently small fixed neighborhood of \(\lambda_f\). Moreover, for every \(\theta\in[-\alpha,\alpha]\), **at least one** of \(|\theta-\beta|\) and \(|\theta+\beta|\) is at most \(\alpha-\beta\), since \(0<\beta<\alpha/2\). Hence, uniformly on the arc,

\[
\min\bigl(|E_{a_+,m}|,|E_{a_-,m}|\bigr)
\le C m^{-1/2}e^{m\tau(\lambda,\alpha-\beta)}
=o(1),
\tag{11}
\]

and the other remainder has the far-arc upper bound (9). In particular, the product \(E_{a_+,m}E_{a_-,m}\) is
\(o(m^{-1/2}e^{m\tau(\lambda,\alpha+\beta)})\) uniformly. This **one-small-factor property** is essential when the far remainder itself grows: simply bounding the product by the square of the worst remainder would not prove (4).

At the DC point \(z=1\), both phase offsets have magnitude \(\beta\), so (9)--(10) give

\[
Q_{a_\pm,m}(1)=1-E_{a_\pm,m}(1)=1+o(1),
\qquad
|E_{a_\pm,m}(1)|
=o(m^{-1/2}e^{m\tau(\lambda,\alpha+\beta)}).
\tag{12}
\]

Expand the numerator of \(G_m-1\) using \(Q=1-E\). The two individual remainders satisfy the upper bound (9), their product is negligible by (11), and the DC-normalization correction is negligible by (12). This proves the **upper** bound in (4).

For the **lower** bound take the right or left arc endpoint, for example \(z=e^{-i\alpha}\). The \(a_+\) center is exposed to the full angle \(\alpha+\beta\), while \(a_-\) sees only \(\alpha-\beta\). Equations (7)--(9) show

\[
|E_{a_+,m}(e^{-i\alpha})|
\asymp m^{-1/2}e^{m\tau(\lambda,\alpha+\beta)},\qquad
\frac{E_{a_-,m}(e^{-i\alpha})}
{E_{a_+,m}(e^{-i\alpha})}\longrightarrow0.
\tag{13}
\]

The denominator corrections from (12) and the product term are also negligible **relative to the exposed remainder**. Therefore

\[
G_m(e^{-i\alpha})-1
=-E_{a_+,m}(e^{-i\alpha})(1+o(1)),
\tag{14}
\]

which proves the matching lower bound and the trichotomy. It also proves that the obstruction is not merely an absolute-value estimate: the leading complex coefficient of the exact remainder is nonzero.

## 4. Coefficient cost, numerical control, and the boundary that remains open

At \(\lambda=\lambda_f\), choose the RE-241 grid
\(\delta=\alpha/T\), \(m=\lceil H/(2\delta)\rceil\), \(z=e^{-i\delta t}\).
The coupled polynomial has real coefficients, exact DC normalization, \(O(T)\) support points, and delays in
\([H,(1+\lambda_f)H+o(1)]\). Equation (4) gives **actual uniform prediction error \(\asymp T^{-1/2}\)**, rather than merely an infimum of strictly exponentially certified rates. When the RE-240 small-phase hypotheses hold, its norm formula still supplies the leading coefficient-cost rate

\[
\frac{\nu(\lambda_f,\rho)+\tfrac{\lambda_f}{2}\log b(\rho,\beta)}{\alpha},
\quad
\nu=-\log\rho+h(\lambda)+\lambda\log(1+\rho^{-1}),
\quad
b=1-\frac{4\rho}{(1+\rho)^2}\sin^2(\beta/2).
\tag{15}
\]

For a diagnostic instance \(\rho=2.29\), \(\alpha=0.52\), and \(\beta=0.03\), the descending far threshold is \(\lambda_f\approx4.31476644416\), while the descending near-edge root is approximately \(3.69845117339\) and the DC exponent at \(\lambda_f\) is approximately \(-0.7322832969\). Direct high-precision finite-tail checks at \(m=40,80,160\), both sides of this root and at the root, agree with the \(m^{-1/2}e^{m\tau}\) scale; these checks are diagnostic only, not proof.

**Adversarial boundaries.** The theorem fixes \(\beta>0\) before \(m\to\infty\); the endpoint dominance need not be uniform when \(\beta\to0\) with \(m\), since then the two arc-edge errors can have comparable sizes. The theorem says nothing about large phase splitting, unequal factors, parameter drift, parallel/minimax synthesis, or a coupled product built from individually different approximation mechanisms. The \(m^{-1/2}\) boundary predictor also lacks the fixed exponential error margin used in the ordinary-prime transfer of RE-218; no new ordinary-prime realization or Robin inequality is inferred from it.

**Prior-art/novelty boundary.** Binomial-tail asymptotics and their incomplete-beta representations are classical; see NIST DLMF §8.18 and Nemes–Olde Daalhuis, *Uniform Asymptotic Expansion for the Incomplete Beta Function*, SIGMA **12** (2016), 101, DOI 10.3842/SIGMA.2016.101. Neither is imported as a theorem: (5)--(8) prove the precise complex-tail estimate directly by a geometric majorant. The line-specific delta is the endpoint dominance and local coupled-product impossibility from (10)--(14), alongside the admissible algebraic boundary excluded from RE-241's strict exponential certification. RE-241 alone did not assert either claim. No new load-bearing external input is required in SOURCES.md.

## Research consequence

The factorwise absolute-tail certificate from RE-241 is **locally exact at the exponential-rate level even for the coupled product**. At its sharp boundary the product nevertheless converges algebraically; immediately below it one exposed endpoint prevents all coupled cancellation. This closes the infinitesimal fixed-parameter conjugate-phase escape, not the broader multi-center prediction problem or the Robin/RH objective.
