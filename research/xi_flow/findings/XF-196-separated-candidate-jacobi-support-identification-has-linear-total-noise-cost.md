---
type: theorem
research_line: xi_flow
finding_id: XF-196
status: canonical
---

# XF-196 — Separated unknown Jacobi radii can be identified at the sharp linear fixed-total-noise cost

**Evidence:** EXACT-DERIVED + SEPARATED-SUPPORT-RECOVERY + CLASSICAL-NOISE-SEPARATION. Unlike XF-194's fixed-radius fitting or XF-195's unknown-radius binary detection, this theorem identifies **which** known candidate radius carries a nonzero single-atom displacement, while retaining the sharp \(\Theta(Q)\) fixed-total Euclidean-noise row count. The theorem is limited to multiplicatively separated candidates below an explicit reciprocal-image leakage horizon. It asserts no Xi-zero-flow consequence.

## Exact experiment and theorem

Fix \(\alpha>0\), \(0<\tau_0\le1/4\), and \(\sigma>0\). Let \(I_{\tau_0}=[-1/4,-\tau_0]\cup[\tau_0,1/4]\). Keep precisely the complete one-pair Jacobi defect and the *source-independent* row normalization of XF-192--XF-195:
\[
J_{p,\tau}(x)=2(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x})
 -2x^{-1/2}(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}),\qquad \Re x>0,
\tag{1}
\]
\[
x_r=\pi^{-1}(\alpha r^{-2}+ir^{-1}),\qquad
G_r=\max(1,|x_r|^{-1/2}),\qquad F_{p,\tau}(r)=J_{p,\tau}(x_r)/G_r.
\tag{2}
\]
The square root is principal. The null is the unchanged source \(F_\varnothing=0\); every alternative moves exactly one symmetric unit-weight pair from an *unknown* integer \(p\) by an *unknown* \(\tau\in I_{\tau_0}\), leaving the other atoms unchanged. The complete observation vector at prechosen distinct positive scales \(\mathcal R\) is \(F|_{\mathcal R}+e\), with one adversarial budget \(\|e\|_{\ell^2(\mathcal R)}\le\sigma\).

Write
\[
\kappa=\frac{9\pi^2\alpha}{32},\quad c=\frac{9\alpha}{16},\quad
A=\frac{5\,2^{3/4}}{\sqrt\pi},\quad
a_\alpha=\frac{3e^{-2\alpha}}{2\pi(1+\sqrt{2\pi})}>0.
\tag{3}
\]
There are \(P_0=P_0(\alpha,\tau_0)\) and a separation factor \(\rho=\rho(\alpha,\tau_0)>2\) such that the following holds. Let \(S\) be any nonempty finite set of integer radii, \(P=\min S\ge P_0\), \(Q=\max S\), with successive radii separated by at least a factor \(\rho\), and suppose
\[
Q\le \exp(\kappa P^2).
\tag{4}
\]
There is a prechosen bank of \(M\le C_{\alpha,\tau_0,\sigma}Q\) **distinct** scales, independent of the active \(p,\tau\), whose complete normalized signal vectors obey
\[
\begin{split}
\|F_{p,\tau}|_{\mathcal R}\|_2&\ge8\sigma,\\
\|F_{p,\tau}|_{\mathcal R}-F_{q,\zeta}|_{\mathcal R}\|_2&\ge4\sigma
\quad(p\ne q;\ p,q\in S;\ \tau,\zeta\in I_{\tau_0}),\\
\|F_{p,\eta}|_{\mathcal R}-F_{p,\zeta}|_{\mathcal R}\|_2
&\ge a_\alpha\sqrt{n_p/p}\,|\eta-\zeta|
\quad(\eta,\zeta\in[-1/4,1/4]).
\end{split}
\tag{5}
\]
Here \(n_p\) is the explicit number of rows in the block allocated to candidate \(p\) below. Thus nearest-model fitting under the stated total noise bound identifies **the active radius versus every other candidate and versus the null**, and yields a stable displacement fit at that radius. Conversely, any deterministic adaptive method that uniformly identifies the radius and distinguishes the null under the same fixed-total \(\ell^2\) budget needs \(\Omega_{\alpha,\sigma}(Q)\) observations, even if it may repeat scales. The optimal worst-case count in this separated-candidate, leakage-controlled model is therefore
\[
\boxed{M_{\mathrm{support}}(\sigma;S)=\Theta_{\alpha,\tau_0,\sigma}(Q).}
\tag{6}
\]
The statement concerns identification of a single moved radius from a *known* separated candidate set; it does not identify multiple simultaneous edits or arbitrary densely packed candidate radii.

## Matched-radius row and cross-radius leakage estimate

XF-193, equation (10), gives the complete-Jacobi **finite-chord** bound, valid for all sufficiently large \(p\) and all \(r\in[p,2p]\):
\[
|F_{p,\eta}(r)-F_{p,\zeta}(r)|
 \ge a_\alpha|\eta-\zeta|/\sqrt p.
\tag{7}
\]
In particular \(|F_{p,\tau}(r)|\ge a_\alpha\tau_0/\sqrt p\) for every allowed nonzero displacement. This already includes the reciprocal Jacobi correction.

The cross-radius estimate must instead bound an *off-target* \(q\) at a row matched to \(p\). Split its complete defect into direct and reciprocal pieces \(F_{q,\zeta}=D_{q,\zeta}/G_r+B_{q,\zeta}/G_r\). Differentiating the direct Gaussian exactly and using \(r\ge p\ge\alpha\), \(|\zeta|\le1/4\), yields
\[
|D_{q,\zeta}(x_r)|/G_r
 \le A|\zeta|\,q\,r^{-3/2}
    \exp[-c(q/r)^2].
\tag{8}
\]
Indeed \(|\partial_\zeta D|\le5\sqrt2(q/r)\exp[-c(q/r)^2]\), while
\(G_r\ge2^{-1/4}\sqrt{\pi r}\). For the reciprocal term, use its finite **amplitudes**, not its possibly rapidly oscillating derivative:
\[
|B_{q,\zeta}(x_r)|/G_r
 \le4e^{-\kappa q^2},
\tag{9}
\]
because \(\pi\Re(1/x_r)\ge\pi^2\alpha/2\) and both \(q^2,(q+\zeta)^2\ge9q^2/16\).

Put \(s=q/p\). For every \(r\in[p,2p]\), (8)--(9) imply the uniform off-target inequality
\[
\sqrt p\,|F_{q,\zeta}(r)|
\le\frac A4\,s\,e^{-cs^2/4}
       +4\sqrt Q\,e^{-\kappa P^2}.
\tag{10}
\]
The scalar function \(s\mapsto s e^{-cs^2/4}\) tends to zero both at zero and at infinity. Choose \(\rho>2\) large enough that
\[
\frac A4\sup_{s\in(0,1/\rho]\cup[\rho,\infty)}
s e^{-cs^2/4}\le a_\alpha\tau_0/4.
\tag{11}
\]
By (4), the remaining reciprocal leakage in (10) is at most \(4e^{-\kappa P^2/2}\); enlarge \(P_0\) so this is at most \(a_\alpha\tau_0/4\), and so (7) holds. For distinct \(p,q\in S\), their multiplicative separation makes \(s\) fall in the set of (11), hence
\[
\sqrt p\,|F_{q,\zeta}(r)|\le a_\alpha\tau_0/2
\quad\text{for all }r\in[p,2p].
\tag{12}
\]
Combining (7) for the true candidate with (12) for the wrong candidate gives the **complete finite-chord cross-radius separation**
\[
|F_{p,\tau}(r)-F_{q,\zeta}(r)|
\ge a_\alpha\tau_0/(2\sqrt p)
\quad(r\in[p,2p],\ p\ne q).
\tag{13}
\]
There is no unknown-radius prewhitening in the observations: \(\sqrt p\) appears only in the proof and all actual rows use the common \(G_r\).

## Fixed-total noise decoding and the linear count

For every \(p\in S\), choose
\[
n_p=\Big\lceil(8\sigma/(a_\alpha\tau_0))^2p\Big\rceil,\qquad
r_{p,\ell}=p\Big(1+\frac{\ell}{3(n_p+1)}\Big)
\quad(1\le\ell\le n_p).
\tag{14}
\]
The rows lie strictly in \((p,4p/3)\subset[p,2p]\) and are distinct within and across candidate blocks because \(\rho>2\). Let \(\mathcal R\) be their union. Apply (7) and (13) just on the block belonging to \(p\): the squared norms sum over its \(n_p\) rows and give all three inequalities of (5). Every alternative therefore lies at least \(4\sigma\) from the curves of all *other* radii and at least \(8\sigma\) from the null. A measurement within \(\sigma\) of a true alternative has residual at most \(\sigma\) there and at least \(3\sigma\) against any wrong-radius curve. A feasible fit on the correct radius satisfies
\[
|\widehat\tau-\tau|
\le2\sigma/[a_\alpha\sqrt{n_p/p}]
\le\tau_0/4.
\tag{15}
\]
This is a source-independent fitting rule; neither the chosen rows nor the raw data assume the unknown support.

Because successive radii grow by at least \(\rho\),
\[
M=\sum_{p\in S}n_p
\le\Big((8\sigma/(a_\alpha\tau_0))^2+1\Big)
       \sum_{p\in S}p
\le\Big((8\sigma/(a_\alpha\tau_0))^2+1\Big)
       \frac{\rho}{\rho-1}Q.
\tag{16}
\]
The upper bound uses distinct prechosen observations, not duplicated rows or an unbounded reciprocal gain.

For the lower bound, XF-192's all-scale gain-normalized response ceiling gives a constant \(A_\alpha<\infty\) with \(|F_{Q,\tau_0}(r)|\le A_\alpha/\sqrt Q\) for every positive scale. Run any \(k\)-query adaptive decision policy on the null with zero errors; the queries on the all-zero transcript are fixed. On the alternative \(p=Q,\tau=\tau_0\), choose the causal noise \(e_j=-F_{Q,\tau_0}(r_j)\). If \(k\le \sigma^2Q/A_\alpha^2\), then \(\sum_j|e_j|^2\le\sigma^2\), reproducing exactly the same transcript and decision as the null. Thus even binary detection, and a fortiori support identification, requires more than \(\sigma^2Q/A_\alpha^2\) worst-case queries. This proves (6) without using separation to weaken the lower bound.

## Novelty, controls, and Xi boundary

The geometric candidate separation, total-\(\ell^2\) robust decoding, and zero-transcript adaptive lower-bound principles are classical. See Hockmann--Kunis, *Weak Sparse Superresolution is Well-Conditioned* (SIAM J. Imaging Sci. 2023, DOI 10.1137/22M1521353) for a **different Fourier sparse-measure and Wasserstein metric**, and Castro, *Adaptive sensing performance lower bounds for sparse signal detection and support estimation* (Bernoulli 2014, DOI 10.3150/13-BEJ555), for a **different stochastic adaptive sensing model**. Both are already anchored in this line's SOURCES.md. The local derived increment is (10)--(13): a **complete normalized Jacobi** off-radius estimate that lets XF-194's linear observation budget perform robust unknown-support identification when candidates are well separated and reciprocal-image leakage is controlled. Neither source is claimed to prove that specialized statement.

The restriction \(\log Q\le\kappa P^2\) is **load-bearing** for this proof. When an off-target candidate \(q=P\) is far smaller than \(p\), its reciprocal channel at \(r\asymp p\) has an absolute floor of order \(e^{-\kappa P^2}\), which cannot simply be compared to \(p^{-1/2}\) over unbounded \(Q\). Failure of this one-block domination beyond (4) is **not** a counterexample to all possible support-recovery algorithms: cancellation, alternative row combinations, or finer phase analysis may work. Likewise (11) requires a potentially large \(\rho(\alpha,\tau_0)\); close/adjacent candidate radii and unrestricted multiplicative range remain open.

This is a theorem only for the exact synthetic single-pair Jacobi edit, the specific holomorphic scale family (2), and fixed *total deterministic* normalized noise. It is not a theorem for independent fixed-variance errors at every row, does not construct source-faithful access to these complex defects from the actual Xi heat flow, and does not exclude a Xi-zero collision or bound the de Bruijn--Newman constant.