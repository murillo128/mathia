---
type: theorem
research_line: xi_flow
finding_id: XF-192
status: canonical
---

# XF-192 — Unknown-radius Jacobi probing has an exponential scale/gain loophole

**Evidence:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-GAUSSIAN-SEPARATION. The one-known-atom result XF-191 does not imply that a natural bounded-scale, single holomorphic Jacobi probe can locate an unknown atom. In the *unnormalized absolute complex-noise* model, however, allowing arbitrarily large probe scales yields one-sample identification for every known finite candidate set. The positive part uses an exponentially amplified reciprocal Jacobi channel, and hence does **not** establish physically well-conditioned acquisition.

## Model and two theorems

Fix \(\alpha>0\). For a single symmetric unit-weight pair displaced from the known reference radius \(p\ge1\) by \(\tau\in[-1/4,1/4]\), with every other source atom unchanged, define its complete Jacobi defect
\[
J_{p,\tau}(x)
=2\big(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x}\big)
 -2x^{-1/2}\big(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}\big),
\quad \Re x>0,
\tag{1}
\]
using the principal square root. The only admissible probes in these statements are
\[
x_r=\frac1\pi\left(\frac{\alpha}{r^2}+\frac{i}{r}\right),\quad r>0,\qquad
k_r:=\pi\Re(1/x_r)=\frac{\pi^2\alpha r^2}{\alpha^2+r^2},\qquad
t_r:=|x_r|^{-1/2}=\frac{\sqrt\pi\,r}{(\alpha^2+r^2)^{1/4}}.
\tag{2}
\]
These are *exact* source differences, not a truncated approximate theta series.

**Bounded-scale obstruction.** Put
\(\kappa=9\pi^2\alpha/32\) and \(\delta=\kappa/3=3\pi^2\alpha/32\).
For all sufficiently large integers \(n\), uniformly over every scale
\(0<r\le\exp(\delta n^4)\), at least one of the two candidate radii
\(p\in\{n,n^2\}\) obeys
\[
\boxed{\quad
\sup_{|\tau|\le1/4}|\partial_\tau J_{p,\tau}(x_r)|
\le C_\alpha n^{-1/2}.
\quad}
\tag{3}
\]
Consequently, for that candidate radius all displacement chords satisfy
\[
|J_{p,\eta}(x_r)-J_{p,\zeta}(x_r)|
\le C_\alpha n^{-1/2}|\eta-\zeta|.
\tag{4}
\]
Even restricting nonzero displacements to
\(I_{\tau_0}=[-1/4,-\tau_0]\cup[\tau_0,1/4]\),
\(0<\tau_0\le1/4\), cannot yield a uniform positive same-radius inverse margin for this single probe over both candidates. This is an obstruction **within** (2), with the explicit upper scale restriction, not for unrestricted holomorphic observations.

**Unbounded-gain positive theorem.** For every \(\alpha>0\) and \(0<\tau_0\le1/4\), there is \(P_0(\alpha,\tau_0)\) such that any nonempty *known finite* set \(S\subset\mathbb Z\cap[P_0,\infty)\) admits one choice \(r=r(S,\alpha,\tau_0)>0\), **independent of the unknown active radius**, for which, for all \(p,q\in S\) and \(\eta,\zeta\in I_{\tau_0}\),
\[
\boxed{\quad
|J_{p,\eta}(x_r)-J_{q,\zeta}(x_r)|
\ge
\begin{cases}
|\eta-\zeta|,& p=q,\\[2pt]
1,&p\ne q.
\end{cases}
\quad}
\tag{5}
\]
Writing \(Q=\max S\), one can arrange
\(\log r=O_{\alpha,\tau_0}(Q^2)\).
The lower bound for distinct radii requires \(|\tau|\ge\tau_0\): at \(\tau=0\), \(J_{p,0}\equiv0\) for every \(p\), so exact radius identification is impossible even with arbitrarily many noiseless samples.

## Proof of the bounded-scale obstruction

Decompose \(J=D+B\), with \(D\) the first (direct) difference in (1) and \(B\) the reciprocal difference. Exact differentiation gives
\[
D'_{p,\tau}(x_r)
=-4\pi(p+\tau)x_r\,e^{-\pi(p+\tau)^2x_r},\qquad
B'_{p,\tau}(x_r)
=4\pi(p+\tau)x_r^{-3/2}e^{-\pi(p+\tau)^2/x_r}.
\tag{6}
\]
For \(r\ge\alpha\), one has
\(|x_r|\le\sqrt2/(\pi r)\),
\(|x_r|^{-3/2}\le(\pi r)^{3/2}\), and
\(k_r\ge\pi^2\alpha/2\).
Since \(3p/4\le p+\tau\le5p/4\),
\[
|D'_{p,\tau}(x_r)|
 \le 5\sqrt2\frac{p}{r}
 \exp\!\left[-\frac{9\alpha}{16}(p/r)^2\right],
\qquad
|B'_{p,\tau}(x_r)|
 \le 5\pi^{5/2}p\,r^{3/2}e^{-\kappa p^2}.
\tag{7}
\]
For \(0<r\le\alpha\), using
\(|x_r|\le\sqrt2\alpha/(\pi r^2)\),
\(|x_r|^{-3/2}\le C_\alpha r^3\), and
\(k_r\ge(\pi^2/2\alpha)r^2\), maximize
\(u^2e^{-cu^2}\) with \(u=p/r\) and
\(v^3e^{-cv^2}\) with \(v=pr\), respectively, to obtain
\[
|D'_{p,\tau}(x_r)|\le C_\alpha/p,\qquad
|B'_{p,\tau}(x_r)|\le C_\alpha/p^2 .
\tag{8}
\]
All constants in (7)--(8) are uniform over the full displacement interval.

Split the possible \(r\) into three ranges; for \(n\) sufficiently large:
\[
\begin{array}{c|c|c}
\text{scale}&\text{blind radius}&\text{reason}\\ \hline
0<r\le n^{3/2} &p=n^2&
  p/r\ge n^{1/2}\text{ when }r\ge\alpha,\text{ while (8) covers }r\le\alpha\\
n^{3/2}<r\le n^3 &p=n&
  p/r\le n^{-1/2},\quad
  p r^{3/2}e^{-\kappa p^2}\le n^{11/2}e^{-\kappa n^2}\\
n^3<r\le e^{\delta n^4} &p=n^2&
  p/r\le n^{-1},\quad
  p r^{3/2}e^{-\kappa p^2}
    \le n^2 e^{-\kappa n^4/2}.
\end{array}
\tag{9}
\]
In the first range the direct bound decays at least like a polynomial times \(e^{-c_\alpha n}\), and the reciprocal bound is \(O_\alpha(n^{-4})\) for \(r\le\alpha\) or Gaussian-small for \(r>\alpha\). In the other two ranges (7) is at most \(C_\alpha n^{-1/2}\) for the designated radius. This proves (3). Integrating (6) along the real interval between \(\zeta\) and \(\eta\) proves (4); no assumption of nonzero displacement was used.

## Proof of the one-sample positive theorem

Write \(k_0=\pi^2\alpha/2\), \(k_\infty=\pi^2\alpha\), \(P=\min S\), \(Q=\max S\). Choose \(P_0\) large enough that
\[
e^{-2k_0P\tau_0}\le\tfrac14,\quad
e^{-k_0(2P\tau_0-\tau_0^2)}\le\tfrac14,\quad
e^{-k_0[(P+3/4)^2-P^2]}\le\tfrac18
\tag{10}
\]
for \(P\ge P_0\); also take \(P_0\ge1\).
Set
\[
T=\max\!\left\{9,\,[2k_0(P-1/4)]^{-1}\right\},\qquad
R=\max\!\left\{\alpha,\ 5\sqrt2(Q+1/4),\
 \frac{\sqrt2}{\pi}T^2e^{2k_\infty(Q+1/4)^2}\right\},
\tag{11}
\]
and take \(r=R\). From (2), \(r\ge\alpha\) implies
\(k_0\le k_r\le k_\infty\) and
\(t_r\ge \sqrt{\pi r}/2^{1/4}\). Thus
\[
t_r e^{-k_\infty(Q+1/4)^2}\ge T
\quad\text{and}\quad
\sup_{p\in S,\ |\tau|\le1/4}|D'_{p,\tau}(x_r)|
\le 4\sqrt2(Q+1/4)/r\le4/5<1.
\tag{12}
\]

For same-radius chords define \(A(s)=e^{-\pi s^2/x_r}\) and
\(E(s)=|A(s)|=e^{-k_rs^2}\). The reverse triangle inequality and the mean-value theorem for the positive decreasing function \(E\) give
\[
\begin{aligned}
|B_{p,\eta}(x_r)-B_{p,\zeta}(x_r)|
 &=2t_r|A(p+\eta)-A(p+\zeta)|\\
 &\ge2t_r|E(p+\eta)-E(p+\zeta)|\\
 &\ge4k_0(P-1/4)t_re^{-k_\infty(Q+1/4)^2}
    |\eta-\zeta|
 \ge 2|\eta-\zeta|.
\end{aligned}
\tag{13}
\]
The direct chord costs less than \(|\eta-\zeta|\) by (12); this proves the first inequality of (5), including opposite-sign displacements.

For \(p<q\) in \(S\) and \(\eta,\zeta\in I_{\tau_0}\), both signs of \(\eta\) satisfy
\[
|B_{p,\eta}(x_r)|
=2t_r|A(p+\eta)-A(p)|
\ge \tfrac32t_rE(p)
\tag{14}
\]
by the first two inequalities in (10). Since \(q\ge p+1\), the last inequality in (10) implies
\[
|B_{q,\zeta}(x_r)|
\le4t_rE(q-1/4)
\le\tfrac12t_rE(p).
\tag{15}
\]
Hence \(|B_{p,\eta}-B_{q,\zeta}|\ge t_rE(p)\ge T\ge9\).
Every complete direct defect has modulus at most \(4\), so the direct difference between two candidate radii has modulus at most \(8\). Subtraction yields the second inequality in (5). Finally (11), with \(T=9\) once \(P\) is large, gives \(\log r=O_{\alpha,\tau_0}(Q^2)\).

For a feasible fit in the declared model under absolute complex noise \(|e|\le\sigma<1/2\), distinct candidate radii cannot both have residual \(\le\sigma\). Conditional on the identified radius, the first bound of (5) yields displacement error \(\le2\sigma\). This is an **existence/identifiability** statement, not an efficient algorithm or floating-point stability result.

## Gain-normalized boundary and prior-art audit

The positive result is purchased by the factor
\(t_r=|x_r|^{-1/2}\asymp\sqrt r\), which grows like
\(\exp[O_\alpha(Q^2)]\) under (11). In particular, the reciprocal Gaussian amplitude at the largest candidate \(Q\) is exponentially tiny *before* multiplication by this gain. For \(r\ge\alpha\),
\[
\sup_{|\tau|\le1/4}\frac{|J_{Q,\tau}(x_r)|}{t_r}
\le \frac4{t_r}+4e^{-k_0(Q-1/4)^2}
\longrightarrow0
\quad(Q\to\infty).
\tag{16}
\]
Thus the raw absolute-noise success does not persist as a uniform gain-normalized noise modulus. It also does not prove scale optimality, an impossibility result for arbitrary \(\Re x>0\) probes, or a matching lower/upper bound for a scale grid under a meaningful gain/precision budget.

The source-dependent contrast is exact: XF-191's direct phase at \(r=p\) recovers one **known** radius with order-one displacement sensitivity, whereas an unknown radius in a dispersed candidate set can be blind at every scale below the explicit exponential threshold of (3); if raw amplification is unlimited, the reciprocal channel instead identifies all candidates at one artificially large scale. The proposed local clue CLUE-known-candidate-holomorphic-scale-grid is thereby narrowed rather than establishing a universal information-theoretic grid lower bound.

Related general background includes Ankur Moitra, *Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices* (STOC 2015, DOI 10.1145/2746539.2746561), and Mathias Hockmann and Stefan Kunis, *Weak Sparse Superresolution is Well-Conditioned* (SIAM J. Imaging Sci. 16, 2023, DOI 10.1137/22M1521353). Those theorems concern separated Fourier-measure acquisition and its metrics; no implication from either is used here, and no broad Gaussian-separation or information-theoretic novelty is claimed. AF-563's one-sample prime-edit equalizer gives a *relative*, generally vanishing absolute margin for a different inverse-prime response. Its discrete spacing argument does not justify a positive absolute Gaussian-Jacobi margin without the reciprocal gain and exact scale accounting proved above.

**Scientific exclusion:** all source atoms other than one known-weight symmetric candidate remain fixed, the finite candidate set is known, the scale can depend on that set, the complex Jacobi defect is assumed observable with *raw absolute noise*, and no Xi-specific measurement budget is established. Source reconstruction does not by itself control H_t zeros. This finding gives neither a bound on the de Bruijn--Newman constant \(\Lambda\) nor a conclusion about RH.
