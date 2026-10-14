---
type: theorem
research_line: xi_flow
finding_id: XF-199
status: canonical
---

# XF-199 — Fixed-degree polynomial baselines preserve the sharp Jacobi support tariff

**Evidence:** EXACT-DERIVED + CLASSICAL-FINITE-DIFFERENCE-QUOTIENT + SOURCE-SPECIFIC-JACOBI-PHASE. An unrestricted unknown complex polynomial drift of fixed degree, additive after gain normalization, does not change the sharp linear support-identification cost in the synthetic complete-Jacobi one-pair model. The filter uses a fixed-order finite difference on near-anti-phase Jacobi samples; no Xi-zero or de Bruijn–Newman conclusion is asserted.

## Exact model and theorem

Fix \(\alpha>0\), \(0<\tau_0\le 1/4\), \(\sigma>0\), and a fixed integer \(d\ge0\); put \(m=d+1\). For \(p\in\mathbb Z_{\ge1}\), \(\tau\in[-1/4,1/4]\), and \(r>0\), define the complete, gain-normalized one-pair Jacobi defect
\[
\begin{aligned}
J_{p,\tau}(x)&=2(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x})
 -2x^{-1/2}(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}),\\
x_r&=\pi^{-1}(\alpha r^{-2}+ir^{-1}),\qquad
G_r=\max\{1,|x_r|^{-1/2}\},\qquad
F_{p,\tau}(r)=J_{p,\tau}(x_r)/G_r,\quad F_\varnothing=0.
\end{aligned}
\tag{1}
\]
The square root is principal. Alternatives move exactly one symmetric unit-weight pair at unknown radius \(p\) in a **known finite** set \(S\), by a displacement \(\tau\in I_{\tau_0}=[-1/4,-\tau_0]\cup[\tau_0,1/4]\). All other source atoms stay fixed. At prechosen distinct scales \(\mathcal R=(r_j)_{j=1}^M\), observations obey
\[
y_j=F_{p,\tau}(r_j)+B(r_j)+e_j,
\qquad B\in\mathbb C[r],\ \deg B\le d,
\qquad \sum_j|e_j|^2\le\sigma^2.
\tag{2}
\]
The null also allows an arbitrary polynomial \(B\), and competing model fits may choose different polynomials. Let \(V_d(\mathcal R)=\{(B(r_j))_j:\deg B\le d\}\) and let \(\Pi_d\) be orthogonal projection onto \(V_d(\mathcal R)^\perp\).

**Theorem.** There exist \(P_0=P_0(\alpha,\tau_0,d)\), \(\rho=\rho(\alpha,\tau_0)>2\), and constants \(c,C>0\) depending on \(\alpha,\tau_0,\sigma,d\), such that every nonempty finite \(S\subset\mathbb Z_{\ge P_0}\) with \(Q=\max S\) and consecutive elements at least a factor \(\rho\) apart admits a bank of at most \(CQ\) distinct scales for which projected predictions of the null and distinct active supports have pairwise distance at least \(8\sigma\). A fixed-radius displacement also has a uniform finite-chord inverse modulus. Conversely, any always-correct deterministic adaptive detector or support identifier requires at least \(cQ\) rows in the worst case. Thus
\[
\boxed{M_{\mathrm{support,poly}(d)}(\sigma;S)
=\Theta_{\alpha,\tau_0,\sigma,d}(Q).}
\tag{3}
\]
No upper restriction on \(Q/\min S\) is imposed.

## Full-Jacobi finite-difference lemma

Put \(a_\alpha=3e^{-2\alpha}/[2\pi(1+\sqrt{2\pi})]\) and \(\kappa=9\pi^2\alpha/32\), as in XF-193. For integer \(m\ge1\), set
\[
\Delta_\pi^m f(r)=\sum_{j=0}^m(-1)^{m-j}\binom mj f(r+j\pi).
\tag{4}
\]
For every polynomial \(B\) of degree at most \(m-1\), \(\Delta_\pi^m B\equiv0\). The load-bearing finite-chord lemma is: for all sufficiently large \(p\), every \(r\in(p,p+1)\), and all \(\eta,\zeta\in[-1/4,1/4]\),
\[
\boxed{|\Delta_\pi^m(F_{p,\eta}-F_{p,\zeta})(r)|
\ge 2^{m-1}a_\alpha|\eta-\zeta|/\sqrt p.}
\tag{5}
\]

**Proof.** On \(s\in[p,2p]\), XF-198's exact decomposition is
\[
F_{p,\tau}(s)=e^{-ip^2/s}H_{p,\tau}(s)+R_{p,\tau}(s),\quad
H_{p,\tau}(s)=\frac{2e^{-\alpha p^2/s^2}}{G_s}
\left(e^{-(2p\tau+\tau^2)(\alpha/s^2+i/s)}-1\right).
\tag{6}
\]
Here \(R\) is the entire normalized reciprocal term, not a direct-Gaussian approximation. Differentiating this explicit envelope, as in XF-198, gives uniformly in the indicated intervals
\[
|\partial_\tau H_{p,\tau}(s)|\le C_\alpha p^{-1/2},\qquad
|\partial_s\partial_\tau H_{p,\tau}(s)|\le C_\alpha p^{-3/2}.
\tag{7}
\]
For fixed \(m\), \(r\in(p,p+1)\), and \(0\le j\le m\), all \(r+j\pi\) lie in \([p,2p]\) once \(p>m\pi+1\), and uniformly
\[
\frac{p^2}{r+j\pi}=\frac{p^2}{r}-j\pi+O_m(p^{-1}),\qquad
e^{-ip^2/(r+j\pi)}=(-1)^j e^{-ip^2/r}(1+O_m(p^{-1})).
\tag{8}
\]
Integrating (7) along the displacement chord and the bounded shifts \(j\pi\) shows that the forward difference of the **direct** chord equals
\[
(-1)^m2^m e^{-ip^2/r}[H_{p,\eta}(r)-H_{p,\zeta}(r)]
+O_{\alpha,m}(|\eta-\zeta|p^{-3/2}),
\tag{9}
\]
since \(\sum_j(-1)^{m-j}\binom mj(-1)^j=(-1)^m2^m\). XF-193's full matched-Jacobi finite-chord estimate says
\[
|F_{p,\eta}(r)-F_{p,\zeta}(r)|
\ge a_\alpha|\eta-\zeta|p^{-1/2},
\tag{10}
\]
and its reciprocal derivative obeys
\[
|\partial_\tau R_{p,\tau}(s)|\le C_\alpha p^{5/2}e^{-\kappa p^2}
\qquad(s\in[p,2p]).
\tag{11}
\]
Replacing the direct chord at \(r\) by the full chord and restoring all reciprocal differences in (9) therefore costs only \(O_{\alpha,m}(|\eta-\zeta|p^{5/2}e^{-\kappa p^2})\). For sufficiently large \(p\), the errors in (9) and (11) consume less than half of the leading \(2^m a_\alpha|\eta-\zeta|p^{-1/2}\) margin, proving (5), including chords between opposite-sign displacements.

## One-sided separation and polynomial quotient

The off-target full-reciprocal estimate of XF-197 can be made arbitrarily small by increasing the separation factor. In particular, choose \(\rho>2\) and then \(P_0\) such that whenever \(q\ge\rho p\), \(p\ge P_0\), \(s\in[p,2p]\), and \(\zeta\in I_{\tau_0}\),
\[
|F_{q,\zeta}(s)|\le a_\alpha\tau_0/(8\sqrt p).
\tag{12}
\]
Then \(|\Delta_\pi^m F_{q,\zeta}|\le 2^{m-3}a_\alpha\tau_0/\sqrt p\) on a \(p\)-tuple, whereas the active difference to the null has modulus at least \(2^{m-1}a_\alpha\tau_0/\sqrt p\). Thus, for any distinct active radii \(p<q\) and allowed displacements, the smaller radius's tuples give
\[
|\Delta_\pi^m(F_{p,\tau}-F_{q,\zeta})(r)|
\ge c_m/\sqrt p,\qquad c_m=3\cdot2^{m-3}a_\alpha\tau_0.
\tag{13}
\]
Active versus null has an even larger gap. No comparison is made at the larger radius's adapted scales, so (13) does not constrain \(Q/P\).

Set \(L_m=\sum_{j=0}^m\binom mj^2=\binom{2m}m\) and
\[
K=(8\sigma\sqrt{L_m}/c_m)^2,\qquad
n_p=\lceil Kp\rceil,\qquad
r_{p,\ell}=p+\ell/(n_p+1),\quad1\le\ell\le n_p.
\tag{14}
\]
For each \(p\in S\), use the \((m+1)n_p\) scales \(r_{p,\ell}+j\pi\), \(0\le j\le m\). Their unit-width clusters do not overlap since \(\pi>1\); for sufficiently large \(P_0\), each block is contained in \([p,2p]\), and blocks for different candidate radii are disjoint because \(\rho>2\).

On any \((m+1)\)-tuple, the weight vector \(w_j=(-1)^{m-j}\binom mj\) is orthogonal to all degree-at-most-\(d\) polynomial evaluation vectors and has squared norm \(L_m\). The corresponding normalized vectors on disjoint tuples are orthonormal. Hence Bessel's inequality gives, for every contrast \(v\),
\[
\|\Pi_d v\|_2^2\ge\frac1{L_m}
\sum_{\text{selected disjoint tuples}}
|\Delta_\pi^m v(r_{p,\ell})|^2.
\tag{15}
\]
By (13), each pair of distinct supports, and each support versus the null, has nuisance-quotient separation at least
\[
c_m\sqrt{n_p/(L_mp)}\ge8\sigma
\tag{16}
\]
using the smaller active radius's block. Projected true noisy data are within \(\sigma\) of their true curve while wrong supports have residual at least \(7\sigma\), proving uniform identification. For equal-radius displacement chords, (5) and (15) yield
\[
\|\Pi_d(F_{p,\eta}-F_{p,\zeta})\|_2
\ge2^{m-1}a_\alpha\sqrt{n_p/(L_mp)}|\eta-\zeta|.
\tag{17}
\]
A feasible fit at the recovered radius therefore satisfies \(|\widehat\tau-\tau|\le3\tau_0/16\). Geometric separation gives
\[
M=(m+1)\sum_{p\in S} n_p
\le(m+1)(K+1)\frac{\rho}{\rho-1}Q.
\tag{18}
\]

## Adaptive lower bound

XF-192 proves the all-scale ceiling \(\sup_{r>0,|\tau|\le1/4}|F_{Q,\tau}(r)|\le A_\alpha/\sqrt Q\). Feed any deterministic adaptive algorithm the zero transcript under the null with \(B=0,e=0\). The alternative \((Q,\tau_0)\), also with \(B=0\), reproduces that transcript through causal errors \(e_j=-F_{Q,\tau_0}(r_j)\), whose total squared norm after \(M\) rows is at most \(A_\alpha^2M/Q\). If \(M\le\sigma^2Q/A_\alpha^2\), both cases have identical observations, so detection is impossible. This proves the \(\Omega(Q)\) bound even for adaptive scales.

## Prior art, falsification controls, and Xi boundary

Polynomial annihilation by finite differences, binomial identities, and orthogonal nuisance projection are classical, not claimed as generic discoveries. The source-specific calculation beyond XF-198 is fixed-order full-Jacobi nonlinear finite-chord amplification by an approximate alternating phase filter, retaining one-sided support separation after quotienting by a polynomial trend. Generalized Prony/annihilating-filter work and the separated Fourier inverse-problem literature (including Moitra 2015 and Hockmann–Kunis 2023, already anchored in SOURCES.md) are neighboring techniques, not assumed to imply this exact Jacobi theorem.

The degree \(d\) must be fixed independently of \(Q\): if \(d\ge M-1\), a polynomial can interpolate all rows and the quotient vanishes. The theorem assumes known multiplicatively separated candidate radii, one symmetric unit-weight pair edit, the stated source-independent gain, a polynomial nuisance **after** gain normalization, and a fixed deterministic **total** \(\ell^2\) noise budget. It does not handle arbitrary scale-dependent backgrounds, pre-gain polynomial nuisances, limited scale precision, independent per-row noise, multiple edits, or close candidate supports. Its \(O(p)\) measurements per block occupy bounded intervals with \(O(1/p)\) spacing. Access to these complex normalized defects from the actual Xi heat flow has not been derived, nor has any Xi-zero exclusion, upper bound on the de Bruijn–Newman constant, or RH implication.
