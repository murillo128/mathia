---
type: theorem
research_line: xi_flow
finding_id: XF-198
status: canonical
---

# XF-198 — Anti-phase Jacobi pairs preserve the linear support tariff modulo a common complex baseline

**Evidence:** EXACT-DERIVED + SOURCE-SPECIFIC-ANTI-PHASE-BANK + CLASSICAL-QUOTIENT-DECODING. A single unrestricted complex offset shared by all gain-normalized rows does **not** change XF-197's sharp linear acquisition cost for a separated, unknown-radius one-pair Jacobi edit. Unlike an uncentered rowwise witness, this requires a genuine within-block nonconstant direction. An explicit half-period phase partner supplies it, including the full reciprocal Jacobi term.

## Observation model and theorem

Fix \(\alpha>0\), \(0<\tau_0\le1/4\), and a fixed total deterministic noise budget \(\sigma>0\). For \(p\in\mathbb Z_{\ge1}\), \(\tau\in I=[-1/4,1/4]\), and \(r>0\), define the complete one-pair defect and normalized observation
\[
\begin{aligned}
x_r&=\pi^{-1}(\alpha r^{-2}+ir^{-1}),\qquad
G_r=\max\{1,|x_r|^{-1/2}\},\\
J_{p,\tau}(x)&=2(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x})
-2x^{-1/2}(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}),\\
F_{p,\tau}(r)&=J_{p,\tau}(x_r)/G_r,\qquad F_{\varnothing}(r)=0.
\end{aligned}
\tag{1}
\]
The square root is principal. Alternatives have exactly one displaced symmetric unit-weight pair, with unknown \(p\) in a **known finite** integer candidate set \(S\) and unknown \(\tau\in I_{\tau_0}=[-1/4,-\tau_0]\cup[\tau_0,1/4]\). The null is the unchanged reference. Every other source atom stays fixed.

At a prechosen distinct-scale bank \(\mathcal R=(r_1,\ldots,r_M)\), allow the same unknown unrestricted \(b\in\mathbb C\) in every normalized row:
\[
y_j=F_{p,\tau}(r_j)+b+e_j,\qquad
\sum_{j=1}^M|e_j|^2\le\sigma^2.
\tag{2}
\]
The null also permits arbitrary \(b\). Different competing model fits may use different baselines. The exact nuisance quotient is
\[
\Pi_{\mathcal R}=I_M-\mathbf1\mathbf1^*/M,\qquad
\inf_{c\in\mathbb C}\|v-c\mathbf1\|_2=\|\Pi_{\mathcal R}v\|_2 .
\tag{3}
\]

There are \(P_0=P_0(\alpha,\tau_0)\), \(\rho=\rho(\alpha,\tau_0)>2\), and positive \(c,C\) depending on \(\alpha,\tau_0,\sigma\), such that for every nonempty finite \(S\subset\mathbb Z\), with \(P=\min S\ge P_0\), \(Q=\max S\), and consecutive candidates satisfying \(q\ge\rho p\), a bank of at most \(CQ\) distinct scales separates **the null and all distinct supports in the quotient by at least \(8\sigma\)**. It also has a uniform finite-chord lower bound for displacement fitting at each identified radius. Conversely every always-correct deterministic adaptive detection/identification procedure requires at least \(cQ\) rows in the worst case. In particular,
\[
\boxed{M_{\mathrm{support,offset}}(\sigma;S)=
\Theta_{\alpha,\tau_0,\sigma}(Q)}
\tag{4}
\]
with no bound on \(Q/P\). The baseline is an additive offset **after** the specified gain normalization, not an unknown unnormalized intercept subsequently divided by a row-dependent \(G_r\).

## Half-period pairs and a uniform finite-chord antisymmetric margin

For large \(p\), choose any \(r\in(p,p+1)\) and its partner
\[
T_p(r)=\left(\frac1r-\frac{\pi}{p^2}\right)^{-1}
=\frac{p^2r}{p^2-\pi r}.
\tag{5}
\]
Then \(T_p(r)-r=\pi r^2/(p^2-\pi r)=\pi+O(p^{-1})\), uniformly over this unit interval. For \(p\) sufficiently large, \(r,T_p(r)\in[p,2p]\), their two unit-width clusters are disjoint, and
\[
e^{-ip^2/T_p(r)}=-e^{-ip^2/r}.
\tag{6}
\]
This identity uses the **base radius** \(p\) only to design the bank for the known candidate set, not as an oracle revealing the active radius.

Split \(F_{p,\tau}=D_{p,\tau}/G_r+R_{p,\tau}\), where \(D\) is the direct Gaussian difference and \(R\) the full reciprocal difference after normalization. Factor the direct term exactly:
\[
\frac{D_{p,\tau}(x_r)}{G_r}
=e^{-ip^2/r}H_{p,\tau}(r),\qquad
H_{p,\tau}(r)=
\frac{2e^{-\alpha p^2/r^2}}{G_r}
\left(e^{-(2p\tau+\tau^2)(\alpha/r^2+i/r)}-1\right).
\tag{7}
\]
For \(p\le r\le2p\), once \(p\) is large, \(G_r^{-1}=(\pi r)^{-1/2}(1+\alpha^2/r^2)^{1/4}\). Differentiating the explicit expression (7) gives, uniformly over \(\tau\in I\),
\[
|\partial_r\partial_\tau H_{p,\tau}(r)|
\le C_\alpha p^{-3/2}.
\tag{8}
\]
Indeed \(2p\tau+\tau^2=O(p)\), its product with \(\alpha/r^2+i/r\) is \(O_\alpha(1)\), the \(r\)-derivative of this product is \(O_\alpha(p^{-1})\), and the logarithmic \(r\)-derivative of the smooth prefactor is \(O_\alpha(p^{-1})\). The same estimates hold after one \(\tau\)-derivative. Thus integration first in \(\tau\) and then over the bounded distance \(T_p(r)-r\) yields
\[
|(H_{p,\eta}-H_{p,\zeta})(T_p(r))
 -(H_{p,\eta}-H_{p,\zeta})(r)|
\le C_\alpha|\eta-\zeta|p^{-3/2}.
\tag{9}
\]
XF-193, equation (9), bounds the *full* reciprocal derivative, uniformly on these matched rows:
\[
|\partial_\tau R_{p,\tau}(r)|
\le C_\alpha p^{5/2}e^{-\kappa p^2},\qquad
\kappa=9\pi^2\alpha/32.
\tag{10}
\]
The normalization \(G_r\ge1\) can only improve this estimate. Combining (6)--(10), for every \(\eta,\zeta\in I\),
\[
\left|
  [F_{p,\eta}(r)+F_{p,\eta}(T_p(r))]
 -[F_{p,\zeta}(r)+F_{p,\zeta}(T_p(r))]
\right|
\le |\eta-\zeta|
 \left(C_\alpha p^{-3/2}+C_\alpha p^{5/2}e^{-\kappa p^2}\right).
\tag{11}
\]
Let \(a_\alpha=3e^{-2\alpha}/[2\pi(1+\sqrt{2\pi})]\), the matched-row constant of XF-193. Enlarge \(P_0\) so that the right-hand coefficient of (11) is at most \(a_\alpha/(2\sqrt p)\). XF-193's full finite-chord estimate gives
\(|F_{p,\eta}(r)-F_{p,\zeta}(r)|\ge
a_\alpha|\eta-\zeta|/\sqrt p\). Subtracting the small *sum* in (11) from twice the first chord proves the **paired difference** lower bound
\[
\boxed{
\left|
 [F_{p,\eta}(r)-F_{p,\eta}(T_p(r))]
 -[F_{p,\zeta}(r)-F_{p,\zeta}(T_p(r))]
\right|
\ge\frac{3a_\alpha}{2\sqrt p}|\eta-\zeta| .
}
\tag{12}
\]
This is a nonlinear, finite-chord estimate for all signs and all displacements in \(I\), not a derivative-only or direct-Gaussian-only approximation.

## One-sided support separation survives the quotient

Take the same \(\rho>2\) as in XF-197, enlarged if needed. Its complete-Jacobi off-target lemma (equation (12) there) ensures that for every \(q\ge\rho p\), \(\zeta\in I_{\tau_0}\), and \(s\in[p,2p]\),
\[
|F_{q,\zeta}(s)|\le\frac{a_\alpha\tau_0}{2\sqrt p}.
\tag{13}
\]
In particular, the off-target paired difference is bounded by \(a_\alpha\tau_0/\sqrt p\). On the \(p\)-pair, (12) with the other displacement zero bounds the active paired difference from below by \(3a_\alpha|\tau|/(2\sqrt p)\). Therefore, for \(q\ge\rho p\) and admissible \(\tau,\zeta\),
\[
\left|
 [F_{p,\tau}(r)-F_{p,\tau}(T_p(r))]
 -[F_{q,\zeta}(r)-F_{q,\zeta}(T_p(r))]
\right|
\ge\frac{a_\alpha\tau_0}{2\sqrt p}.
\tag{14}
\]
The analogous active-versus-null paired difference has the stronger \(3a_\alpha\tau_0/(2\sqrt p)\) bound. For any two distinct supports, always use the block of the **smaller** radius, so (13)--(14) never require an upper bound on \(Q/P\).

For each \(p\in S\), choose
\[
K=\left(\frac{16\sqrt2\,\sigma}{a_\alpha\tau_0}\right)^2,\quad
n_p=\lceil Kp\rceil,\quad
r_{p,\ell}=p+\frac{\ell}{n_p+1},\quad
r'_{p,\ell}=T_p(r_{p,\ell}),\quad1\le\ell\le n_p.
\tag{15}
\]
All \(2\sum_{p\in S}n_p\) scales are distinct: the base and partner clusters within each block are disjoint for large \(p\); different candidate blocks lie in \([p,2p]\) and are disjoint because \(\rho>2\).

For an arbitrary vector \(v\) on this bank and for *any* subcollection of disjoint base/partner pairs,
\[
\|\Pi_{\mathcal R}v\|_2^2
=\inf_{c\in\mathbb C}\sum_{s\in\mathcal R}|v(s)-c|^2
\ge\frac12\sum_{\mathrm{selected\ pairs}}
     |v(r)-v(T_p(r))|^2 .
\tag{16}
\]
This is the exact common-baseline cancellation; no assumption that the mean of a sampled oscillatory profile is small is needed. By (14)--(16), every two competing supports, and each support versus the null, have quotient distance at least
\[
\frac{a_\alpha\tau_0}{2}
   \sqrt{\frac{n_p}{2p}}
\ge\frac{a_\alpha\tau_0}{2}\sqrt{\frac K2}
=8\sigma
\tag{17}
\]
using the smaller active radius's block (the null case has an even larger margin). Thus nearest-curve fitting of the *projected* data identifies the active radius or the null correctly despite arbitrary \(b\) and total \(\ell^2\) errors \(\sigma\). For equal-radius displacement chords, (12) and (16) give
\[
\|\Pi_{\mathcal R}(F_{p,\eta}-F_{p,\zeta})\|_2
\ge\frac{3a_\alpha}{2}
       \sqrt{\frac{n_p}{2p}}|\eta-\zeta|,
\tag{18}
\]
so a feasible fit at the recovered radius has displacement error at most
\(4\sigma\sqrt{2p/n_p}/(3a_\alpha)\le\tau_0/12\).
The total number of distinct rows satisfies
\[
M=2\sum_{p\in S}n_p
\le2(K+1)\sum_{p\in S}p
\le2(K+1)\frac{\rho}{\rho-1}Q .
\tag{19}
\]

## Lower bound, prior art, and boundary

XF-192's uniform single-row ceiling is
\(\sup_{r>0,|\tau|\le1/4}|F_{Q,\tau}(r)|
\le A_\alpha Q^{-1/2}\).
An adaptive algorithm run on the null with \(b=0\), \(e=0\) produces a zero transcript. Under the alternative \((Q,\tau_0)\) with the *same* \(b=0\), the causal errors \(e_j=-F_{Q,\tau_0}(r_j)\) reproduce that transcript at total squared cost at most \(A_\alpha^2k/Q\) for \(k\) queried rows. Thus \(k\le\sigma^2Q/A_\alpha^2\) cannot permit worst-case detection, a fortiori cannot permit support identification. Allowing an unknown baseline cannot remove this hard instance. This proves the lower half of (4) even for sequential scales.

Orthogonal projection against a common intercept, difference measurements, and half-cycle cancellation are classical signal-processing and linear-algebra devices, not claimed as general discoveries. The source-specific increment beyond XF-197 is the exact Jacobi phase partner (5), its slowly varying nonlinear finite-chord envelope (8)--(12), and the one-sided full-reciprocal quotient witness (14). No result in a different sparse sensing or stochastic noise model is imported as a theorem here.

The guarantee depends on a known finite multiplicatively separated set, one edited *unit-weight symmetric* pair, the precise holomorphic scales and source-independent \(G_r\), an offset constant **across normalized rows**, and a fixed *total* adversarial \(\ell^2\) noise budget. Pair clusters contain \(O(p)\) distinct scales in a bounded interval, with spacings of order \(1/p\); this theorem does not address instrumental resolution, independent per-row noise, drifting or scale-dependent baselines, arbitrary close supports, multiple edits, or unknown weights. Nor has physical access to these complex Jacobi defects been derived from the real Xi heat flow. It supplies neither an upper bound on the de Bruijn--Newman constant nor an RH implication.
