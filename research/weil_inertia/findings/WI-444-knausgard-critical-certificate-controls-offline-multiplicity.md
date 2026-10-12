# WI-444 — Critical-line certificate couples off-line multiple-zero mass to simple-critical surplus

**Status:** LITERATURE+DERIVED + EXACT-COUNT-COROLLARY + COMPUTATIONAL-CERTIFICATE-DEPENDENT + INDEPENDENT-REPLAY-PENDING + NON-RH + NO-NOVELTY-CLAIM

**Primary source:** Kristian Muri Knausgård, *More than 83.9% of the zeros of the Riemann zeta function are distinct and more than 67.35% are simple and on the critical line*, arXiv:2610.08965v1 (6 October 2026), https://arxiv.org/html/2610.08965v1, especially Theorem 6.2(a), its proof, Theorem 5.1 and Proposition 5.3. Source/certificate revision: https://github.com/kristianmk/839/tree/b280d51bef5ab32b3280b0955d040085ed522d59.

**Related local finding:** WI-443 audits the three reported headline proportions, the finite certificates and their ceilings. The present result extracts a *joint* inequality from the intermediate count/energy estimate, not a fourth independent source certificate.

## Joint certificate inequality

Write $N=N(T)$ for the number of nontrivial zeta zeros with $0<\operatorname{Im}\rho\le T$, **with multiplicity**; $n=N_0^s(T)$ for the simple zeros on $\operatorname{Re}\rho=1/2$; and

\[
E_{\mathrm{off},\,m\ge2}(T)
=\sum_{\substack{0<\operatorname{Im}\rho\le T\\
\operatorname{Re}\rho\ne1/2,\;m_\rho\ge2}}m_\rho
\]

for the **multiplicity-weighted** mass of off-critical *multiple* zeros. Under the source's certified second-window critical-line inequality, with

\[
x=\frac{8722}{10^6},\qquad
s=\frac{1669159}{2478195},\qquad
1-x=0.991278,
\]

the actual zeta counting functions satisfy

\[
\boxed{\;
\frac{E_{\mathrm{off},\,m\ge2}(T)}{N(T)}
\le $1-x$\left(
\frac{N_0^s(T)}{N(T)}-s\right)+o(1)
\;}\qquad$T\to\infty$.
\tag{1}
\]

The asymptotic error arises from the same smoothing/height limits as the source; (1) is **not** asserted as a uniform finite-height inequality. In particular, if the simple-critical proportion is at most $s+\delta+o(1)$ for a fixed $\delta\ge0$, the off-critical *multiple* mass is at most $$1-x$\delta+o(1)$. Saturation $N_0^s(T)/N(T)\to s$ forces $E_{\mathrm{off},\,m\ge2}(T)/N(T)\to0$.

## Derivation from the source's actual inequality

Use the notation of Theorem 6.2(a): $D$ is the total multiplicity of the on-line multiple zeros, $r$ their distinct-point count; $k_1$ counts off-line *simple* conjugate pairs; $k_2$ counts off-line *multiple* conjugate pairs; $M_2$ sums the multiplicities of one representative from each such pair. Thus

\[
N=n+D+2k_1+2M_2,\qquad
D\ge2r,\qquad M_2\ge2k_2,\qquad
E_{\mathrm{off},\,m\ge2}=2M_2.
\tag{2}
\]

The source's critical-line Gram estimate and two-level trace inequality (its proof of Theorem 6.2(a)) give, after $T\to\infty$ and removal of the smoothing parameter,

\[
(C(f)+b+o(1))N
\ge4(N-n)-4(r+k_1+k_2)+(1+x)n,
\tag{3}
\]

where the same window has $b=4389/10^6$. Using the two multiplicity inequalities in (2), the right side of (3) is bounded below by

\[
4(N-n)-(2D+4k_1+2M_2)+(1+x)n
=2N-$1-x$n+2M_2.
\tag{4}
\]

For the abstract theorem, the certificate defines
\(s_f=(2-C(f)-b)/(1-x)\); the displayed rational \(s=1669159/2478195\)
is a certified **lower bound** for \(s_f\), obtained from an upper enclosure for
\(C(f)\), not an assertion that the exact window energy is rational.
Rearranging (3)–(4) therefore proves (1). The argument neither assumes
positive semidefiniteness of the full Weil form nor drops off-line multiplicities.

### Exact excess-multiplicity refinement

The bound (4) discards two nonnegative multiplicity surpluses. Define
\[
H_0(T):=D-2r
 =\sum_{\substack{\operatorname{Re}\rho=1/2\\m_\rho\ge3}}(m_\rho-2),
\qquad
H_{\mathrm{off}}(T):=2(M_2-2k_2)
 =\sum_{\substack{\operatorname{Re}\rho\ne1/2\\m_\rho\ge3}}(m_\rho-2),
\tag{5}
\]
with \(0<\operatorname{Im}\rho\le T\) in both sums. Off-line conjugate
partners are **both** counted in \(H_{\mathrm{off}}\). Substitution of (2)
gives the exact finite-count identity
\[
\begin{aligned}
&4(N-n)-4(r+k_1+k_2)+(1+x)n\\
&\qquad=2N-(1-x)n+
 E_{\mathrm{off},\,m\ge2}+2H_0+H_{\mathrm{off}}.
\end{aligned}
\tag{6}
\]
Keeping these nonnegative terms through the same source estimate (3),
the \(T\to\infty\) and smoothing limits, and the enclosure
\(s\le s_f\), strengthens (1) to
\[
\boxed{\;
\frac{E_{\mathrm{off},\,m\ge2}(T)+2H_0(T)+H_{\mathrm{off}}(T)}{N(T)}
\le(1-x)\left(\frac{N_0^s(T)}{N(T)}-s\right)+o(1).
\;}
\tag{7}
\]
Thus near saturation of the simple-critical lower bound excludes not
only a positive *density* of off-line multiple-zero mass, as (1) does,
but also a positive *density* of multiplicity **excess above two**
on the critical line. The original (1) by itself cannot control \(H_0\).
For a critical-line zero of multiplicity \(m\ge3\), the retained
additional cost is \(2(m-2)\); for an off-line pair of multiplicity \(m\ge3\)
it is \(2(m-2)\) in addition to the \(2m\) already charged by
\(E_{\mathrm{off},\,m\ge2}\). Equality in the counting relaxations used
for (1) requires every multiple zero to be exactly double.

This is an exact consequence of the published intermediate count
inequality in Theorem 6.2(a), **not** an independent new zeta theorem or
an independently replayed numerical certificate. Every term is global
and asymptotic; a fixed exceptional zero or a zero-density exceptional
family still contributes \(o(N)\), and simple off-line zeros remain
uncontrolled.

The source also proves
$\liminf(N_s+N_0)/(2N)\ge(1+s)/2$. Since
$N_s+N_0=N+n-E_{\mathrm{off},\,m\ge2}$, that displayed average bound alone gives only the weaker slope-one inequality
$E/N\le n/N-s+o(1)$. The stronger factor $1-x<1$ survives **only** by retaining the certificate's positive interaction term $xn$ in (3).

## Independent information and sharp evidence boundary

The slope $1-x$ is not an algebraic consequence of the headline scalar lower bounds in WI-443, even when the source's average bound is included. To see this at the level of formal zero-count budgets, fix $\delta=0.02$, take $n/N=s+\delta$, $E/N=(1-x/2)\delta$, suppose every multiple off-line zero is double and all remaining zeros are simple. Then $N_d/N=1-E/(2N)>q=1645064/1960733$, $N_{s\cup0}/N=1-E/N>u=50652159/56956375$, and $(N_s+N_0)/(2N)=(1+n/N-E/N)/2>(1+s)/2$; yet $E/N>$1-x$\delta$, violating (1). This is a **logical count control**, not an assertion that such a configuration is realised by zeta zeros or satisfies the source's full energy inequality.

The joint bound is still about *global asymptotic proportions*. It says nothing about off-line **simple** zeros, and it cannot exclude even a single off-line multiple zero: finite or zero-density exceptional sets contribute $o(N)$. It gives no RH proof or strict defect bootstrap. Its coefficient and asymptotic bridge inherit Knausgård's analytic proof and the unrefereed finite-search certificate; the cited source's large numerical search has **not** been independently replayed here. Mathematical novelty is not claimed: (1) is an explicit, reusable rearrangement of the published Theorem 6.2(a) proof rather than a new zeta theorem.

## Audit test

Independently replay the second-window finite certificate and check its exact $x,b,C(f)$ interface against the analytic inequality (3); then verify that the on-line/off-line pair decomposition yields (2) and the trace estimate retains $xn$ before substituting the scalar lower bound $n\ge(s-o(1))N$. A mismatch in the certificate, zero-count normalisation, or order of limits invalidates the corresponding numerical coefficient. A better RHS estimate in (4), or an arithmetic bridge controlling *individual simple off-line zeros*, would be genuinely new information beyond this rearrangement.
