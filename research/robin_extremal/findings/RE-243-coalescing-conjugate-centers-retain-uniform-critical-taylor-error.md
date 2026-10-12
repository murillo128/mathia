# RE-243 — Coalescing conjugate centers retain uniform critical Taylor error

**Status:** EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-COUPLED-PREDICTION + UNIFORM-COALESCING-PHASE-BOUNDARY + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDIT.

**Parent findings:** RE-218, RE-239, RE-240, RE-241, RE-242.

RE-242 proves that two fixed, distinct conjugate Taylor centers have a sharp arc-edge truncation threshold and an actual coupled prediction error of order \(m^{-1/2}\) at that threshold. Its endpoint-dominance proof is not uniform when the phase split approaches zero with \(m\), because the two omitted tails then have comparable magnitudes. The remaining question is whether a coalescing split can tune their complex phases to cancel the leading endpoint error. It cannot **at the moving critical truncation threshold**, uniformly over all splitting speeds. The precise interference limit below replaces a fixed-split dominance argument.

## 1. The uniform critical-boundary theorem

Fix \(0<\alpha<\pi/2\), \(\rho>0\), and assume

\[
r(\alpha)<1,\qquad
r(\theta):=\left|1-\rho^{-1}e^{i\theta}\right|.
\]

Equivalently, \(\rho>1/(2\cos\alpha)\). Define

\[
h(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda,
\quad
\tau(\lambda,\theta)=-\log\rho+h(\lambda)+\lambda\log r(\theta).
\]

For every sufficiently small \(0\le\beta\le\beta_0\), let \(\lambda_\beta\) be the descending root

\[
\tau(\lambda_\beta,\alpha+\beta)=0,
\qquad
\lambda_\beta>
\frac{r(\alpha+\beta)}{1-r(\alpha+\beta)}.
\tag{1}
\]

The existence, uniqueness, positivity, and continuity of this root follow from RE-241. Shrink the fixed \(\beta_0>0\) if needed so that \(\alpha+\beta_0<\pi\) and the root lies in a compact positive interval. For integers \(m\ge1\), set \(N=\lceil m\lambda_\beta\rceil\), \(a_\pm=\rho e^{\pm i\beta}\), and

\[
Q_{\pm,m}(z)
=z^m a_\pm^{-m}
\sum_{k=0}^{N}\binom{m+k-1}{k}
(1-z/a_\pm)^k,
\qquad
G_{m,\beta}(z)=
\frac{Q_{+,m}(z)Q_{-,m}(z)}
{Q_{+,m}(1)Q_{-,m}(1)}.
\tag{2}
\]

**Theorem.** There are constants \(0<c<C<\infty\) and \(m_0\), depending only on \(\rho,\alpha\) and the chosen sufficiently small \(\beta_0\), such that for *every* \(m\ge m_0\) and *every* \(\beta\in[0,\beta_0]\) the denominator in (2) is nonzero and

\[
\boxed{
c\,m^{-1/2}
\le
\sup_{|\theta|\le\alpha}
|G_{m,\beta}(e^{i\theta})-1|
\le
C\,m^{-1/2}.
}
\tag{3}
\]

In particular (3) holds for any triangular array \(\beta=\beta_m\), including \(\beta_m=0\), \(\beta_m\asymp m^{-1}\), \(m\beta_m\to\infty\) with \(\beta_m\to0\), and fixed nonzero splits. No uniformity in \(\rho\) or in \(\alpha\) is asserted.

## 2. Uniform complex-tail estimates and the upper bound

Write \(K=N+1\), \(B_m(k)=\binom{m+k-1}{k}\), and \(u_\pm(z)=1-z/a_\pm\). The exact omitted tails are

\[
E_\pm(z):=1-Q_{\pm,m}(z)
=z^m a_\pm^{-m}B_m(K)u_\pm(z)^K
S_{m,\beta}(u_\pm(z)),
\]

\[
S_{m,\beta}(u)=\sum_{j\ge0}
\frac{B_m(K+j)}{B_m(K)}u^j.
\tag{4}
\]

The consecutive coefficient ratios decrease in \(j\) and are at most
\((m+K)/(K+1)\). By (1), the product of its limit \((1+\lambda_\beta)/\lambda_\beta\) with the far-edge radius \(r(\alpha+\beta)\) is strictly less than one. Continuity and a sufficiently small fixed \(\beta_0\) give a *common* geometric ratio less than one on a slightly enlarged disk covering all \(u_\pm(e^{i\theta})\), \(|\theta|\le\alpha\), and the DC values \(u_\pm(1)\).

Uniform dominated convergence then gives

\[
S_{m,\beta}(u)
=\left(1-\frac{1+\lambda_\beta}{\lambda_\beta}u\right)^{-1}
+o(1)
\tag{5}
\]

uniformly over those compact parameter/disk sets. The limiting function is nonzero, so \(S_{m,\beta}\), its reciprocal, and its first derivative on the observed disk are uniformly bounded for large \(m\). Uniform Stirling estimates and \(K=m\lambda_\beta+O(1)\) imply

\[
|E_\pm(e^{i\theta})|
\le
C_1m^{-1/2}
\exp\{m\tau(\lambda_\beta,|\theta\mp\beta|)\}
\le C_1m^{-1/2}.
\tag{6}
\]

At the exposed endpoint \(z_*=e^{-i\alpha}\), the \(+\) tail reaches \(\alpha+\beta\) and satisfies the two-sided estimate

\[
c_1m^{-1/2}\le |E_+(z_*)|\le C_1m^{-1/2}
\tag{7}
\]

with constants independent of \(\beta\). Because the DC angle \(\beta\) stays strictly inside the far edge, (1) also gives
\(\sup_{\beta\le\beta_0}\tau(\lambda_\beta,\beta)<0\), with the value \(-\infty\) interpreted harmlessly if \(r(\beta)=0\). Hence \(E_\pm(1)=O(e^{-dm})\) uniformly for some \(d>0\). Expanding
\((1-E_+)(1-E_-)\), using the \(O(m^{-1})\) product and the exponentially small DC correction, proves the upper bound in (3).

## 3. Endpoint crossover prevents cancellation at every coalescence speed

At \(z_*=e^{-i\alpha}\), let

\[
w=\rho^{-1}e^{-i\alpha},\qquad
u_+(\beta)=1-we^{-i\beta},\qquad
u_-(\beta)=1-we^{i\beta}.
\]

The exact ratio of the two *nonzero* endpoint tails is

\[
R_m(\beta):=\frac{E_-(z_*)}{E_+(z_*)}
=e^{2im\beta}
\left(\frac{u_-(\beta)}{u_+(\beta)}\right)^K
\frac{S_{m,\beta}(u_-(\beta))}
{S_{m,\beta}(u_+(\beta))}.
\tag{8}
\]

First, since \(\partial_\theta\log r(\theta)
=\sin\theta/(\rho r(\theta)^2)>0\) on a fixed neighborhood of \(\alpha\), (5) and (8) imply

\[
|R_m(\beta)|
\le C_2
\left(\frac{r(\alpha-\beta)}{r(\alpha+\beta)}\right)^K
\le C_2e^{-d_2m\beta}.
\tag{9}
\]

Thus whenever \(m\beta\to\infty\), the near tail is negligible relative to the far tail, *even if* \(\beta\to0\).

The only other subsequential regime is \(m\beta\to s\in[0,\infty)\), which forces \(\beta\to0\). Put \(\lambda_0=\lambda_{\beta=0}\) and

\[
A=1-\lambda_0\frac{w}{1-w}.
\tag{10}
\]

The expansions
\(\log(u_-/u_+)=-2i\beta w/(1-w)+O(\beta^2)\),
\(K/m\to\lambda_0\), and
\(S_{m,\beta}(u_-)/S_{m,\beta}(u_+)\to1\)
give the exact crossover limit

\[
\boxed{
R_m(\beta)\longrightarrow e^{2isA}
\qquad\text{if }m\beta\to s<\infty.
}
\tag{11}
\]

Its crucial non-cancellation feature is

\[
\Im A
=
\frac{\lambda_0\sin\alpha}
{\rho\,|1-w|^2}>0.
\tag{12}
\]

For \(s>0\), \(|e^{2isA}|=e^{-2s\Im A}<1\), so
\(1+e^{2isA}\ne0\). For \(s=0\) the ratio tends to \(1\), and the sum instead tends to \(2\). Together with the \(m\beta\to\infty\) limit from (9), this proves by subsequence contradiction that there exists \(\eta>0\) with

\[
|1+R_m(\beta)|\ge\eta
\quad
\text{for all large \(m\) and \(0\le\beta\le\beta_0\)}.
\tag{13}
\]

Consequently \(|E_+(z_*)+E_-(z_*)|\ge\eta|E_+(z_*)|
\ge \eta c_1m^{-1/2}\). The product \(E_+E_-\) is \(O(m^{-1})\) there, while the DC correction is exponentially small. No lower-order term can erase the leading endpoint sum, proving the lower bound in (3). The argument does not assume separate factorwise certificates below the threshold.

## 4. Checks, prior art, and limitations

At \(\beta=0\) the two factors coincide, \(R_m(0)=1\), and their leading errors add rather than cancel. At any fixed \(\beta>0\), (9) recovers RE-242 endpoint dominance. At the intermediate scale \(\beta=s/m\), (11)--(12) show that the phase rotation comes with an inseparable strict amplitude loss, so tuning \(s\) cannot produce leading cancellation. This controls precisely the nonuniformity left open by the fixed-split proof.

As a diagnostic only, for \(\rho=2.29,\alpha=0.52,m=160\) and \(N=\lceil m\lambda_\beta\rceil\), direct high-precision negative-binomial tail evaluation gives
\(\sqrt m\,|G(e^{-i\alpha})-1|\) approximately \(0.38825\), \(0.16846\), and \(0.16699\) at \(\beta=0\), \(1/m\), and \(0.03\), respectively. The proof uses (4)--(13), not those evaluations.

Uniform asymptotic analysis of incomplete beta functions and negative-binomial tails is classical (NIST DLMF §8.18; Nemes--Olde Daalhuis, SIGMA 12 (2016), 101, DOI 10.3842/SIGMA.2016.101, already noted in RE-242). No novelty is claimed for Stirling, first-term geometric tail asymptotics, or the general asymptotic methods. The local mathematical delta is the exact *two-tail complex crossover* (11) with the sign (12), which closes the \(\beta_m\to0\) cancellation loophole for the particular coupled Taylor family. No external theorem is load-bearing, so SOURCES.md is unchanged.

The theorem asserts **critical-boundary error**, not a full below-threshold trichotomy uniform in coalescing \(\beta_m\). Below threshold, both tails can grow and their product may become leading as \(\beta_m\to0\), so RE-242's fixed-split \(m^{-1/2}e^{m\tau}\) asymptotic must not be extrapolated there. Nor does (3) lower the global separated-prediction Wiener constant, supply ordinary-prime realization with a fixed exponential error margin, bound the extremal divisor-sum functional, or establish Robin's inequality/RH.

## Research consequence

The coalescing center phase is not an escape at the moving critical Taylor depth: no choice of \(\beta_m\), however rapidly or slowly vanishing, reduces the uniform predictor error below order \(m^{-1/2}\) by cancellation of the two conjugate edge tails. The remaining mechanisms must change the truncation/prediction architecture, use sufficiently separated phases with different error geometry, or supply new prime-specific input.