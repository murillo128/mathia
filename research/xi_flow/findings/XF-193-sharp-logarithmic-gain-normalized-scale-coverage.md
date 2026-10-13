---
type: theorem
research_line: xi_flow
finding_id: XF-193
status: canonical
---

# XF-193 — Gain-normalized Jacobi finite-chord visibility has sharp logarithmic scale coverage

**Evidence:** EXACT-DERIVED + CLASSICAL-MULTISCALE-COVERING + SOURCE-SPECIFIC-RECIPROCAL-CONTROL. For prechosen probes in XF-192's holomorphic family and its row gain, a bank with \(\Theta(1+\log(Q/P))\) distinct scales is necessary and sufficient for uniform radius-compensated *same-radius* physical-displacement sensitivity on every radius \(p\in[P,Q]\). This is an exact conditional-recovery/coverage result, not an unknown-support identification theorem.

## Exact model and statement

Fix \(\alpha>0\), \(I=[-1/4,1/4]\), and the complete one-pair Jacobi difference
\[
J_{p,\tau}(x)=2\left(e^{-\pi(p+\tau)^2x}-e^{-\pi p^2x}\right)
-2x^{-1/2}\left(e^{-\pi(p+\tau)^2/x}-e^{-\pi p^2/x}\right),
\quad \Re x>0,
\tag{1}
\]
using the principal square root. All other source atoms are unchanged. Restrict observations to
\[
x_r=\frac1\pi\left(\frac\alpha{r^2}+\frac{i}{r}\right),\quad
t_r=|x_r|^{-1/2}=\frac{\sqrt\pi\,r}{(\alpha^2+r^2)^{1/4}},\quad
G_r=\max\{1,t_r\},\quad r>0,
\tag{2}
\]
exactly as in XF-192. For a finite nonempty *prechosen* bank \(\mathcal R\), define
\[
\mathcal C(p;\mathcal R)=
\inf_{\eta,\zeta\in I,\;\eta\ne\zeta}\ 
\max_{r\in\mathcal R}
\frac{\sqrt p\,|J_{p,\eta}(x_r)-J_{p,\zeta}(x_r)|}
{G_r|\eta-\zeta|}.
\tag{3}
\]
Here \(\sqrt p\) is **only a comparison normalization** for the optimal \(p^{-1/2}\) row response in XF-192, not physically accessible gain when \(p\) is unknown.

Set \(K=1+\sqrt{2\pi}\) and \(c_\alpha=3e^{-2\alpha}/(2\pi K)\). For every sufficiently large integer \(P\) depending on \(\alpha\), every integer \(Q\ge P\), and every integer \(p\in[P,Q]\), the dyadic bank
\[
\mathcal R_{P,Q}=\{P\,2^j:0\le j\le\lceil\log_2(Q/P)\rceil\}
\]
satisfies
\[
\boxed{\quad\mathcal C(p;\mathcal R_{P,Q})\ge c_\alpha.\quad}
\tag{4}
\]
Conversely, for any fixed \(0<\gamma\le c_\alpha\) there are \(P_1(\alpha,\gamma)\) and an integer \(h(\alpha,\gamma)\ge1\) such that **any** bank of positive scales with \(\mathcal C(p;\mathcal R)\ge\gamma\) for every integer \(p\in[P,Q]\), \(P\ge P_1\), must have
\[
\boxed{\quad |\mathcal R|\ge
1+\left\lfloor\frac{\log_2(Q/P)}{h(\alpha,\gamma)}\right\rfloor.\quad}
\tag{5}
\]
Thus the scale-count order is \(\Theta_{\alpha,\gamma}(1+\log(Q/P))\) for exactly this rowwise-max, gain-normalized, radius-compensated finite-chord problem.

## Upper bound: a matched row controls every nonlinear chord

For \(p\le r\le2p\) write the direct nonconstant contribution as \(A_\tau=2q_\tau e^{-i\theta_\tau}\), with
\(q_\tau=e^{-\alpha(p+\tau)^2/r^2}\ge e^{-2\alpha}\) and \(\theta_\tau=(p+\tau)^2/r\).
For \(d=|\eta-\zeta|\le1/2\), the half-phase difference is exactly
\[
v=(\eta-\zeta)\frac{2p+\eta+\zeta}{2r},\qquad
\frac38d\le|v|\le\frac54d\le\frac58<\frac\pi2.
\tag{6}
\]
The two-amplitude identity and \(|\sin v|\ge2|v|/\pi\) yield
\[
|A_\eta-A_\zeta|^2
=4[(q_\eta-q_\zeta)^2+4q_\eta q_\zeta\sin^2v],\qquad
|A_\eta-A_\zeta|\ge\frac{3e^{-2\alpha}}\pi d.
\tag{7}
\]

The reciprocal nonconstant term
\(B_\tau=-2x_r^{-1/2}e^{-\pi(p+\tau)^2/x_r}\) has exact derivative
\[
B'_\tau=4\pi(p+\tau)x_r^{-3/2}e^{-\pi(p+\tau)^2/x_r}.
\tag{8}
\]
For \(p\ge\max(1,\alpha)\), \(p\le r\le2p\), put \(\kappa=9\pi^2\alpha/32\).
Since
\[
\pi\Re(1/x_r)=\frac{\pi^2\alpha r^2}{r^2+\alpha^2}
\ge\frac{\pi^2\alpha}{2},\qquad
|x_r|^{-3/2}\le(2\pi p)^{3/2},
\]
we have for every \(\tau\in I\)
\[
|B'_\tau|\le5\pi(2\pi)^{3/2}p^{5/2}e^{-\kappa p^2}.
\tag{9}
\]
For \(p\) sufficiently large, this is at most \(3e^{-2\alpha}/(2\pi)\). Integrating over each *finite* chord and subtracting (7) gives
\[
|J_{p,\eta}(x_r)-J_{p,\zeta}(x_r)|
\ge\frac{3e^{-2\alpha}}{2\pi}d.
\tag{10}
\]
Because \(G_r\le1+\sqrt{\pi r}\le K\sqrt p\), this proves the \(c_\alpha\) margin for every \(r\in[p,2p]\). Given \(p\in[P,Q]\), \(j=\lceil\log_2(p/P)\rceil\) selects such a row from the dyadic bank, proving (4).

## Lower bound: a row can witness only a bounded multiplicative interval

It suffices to test the **two nonzero** displacements \(\eta=1/4\), \(\zeta=-1/4\), \(d=1/2\). These also belong to any displacement-floor model \(0<\tau_0\le1/4\). Decompose \(J=D+B\). For \(r\ge\alpha\),
\[
|x_r|\le\frac{\sqrt2}{\pi r},\qquad
G_r\ge t_r\ge2^{-1/4}\sqrt{\pi r}.
\tag{11}
\]
The exact derivative
\(D'_{p,\tau}=-4\pi(p+\tau)x_r e^{-\pi(p+\tau)^2x_r}\)
therefore gives, after integrating along the test chord,
\[
\frac{\sqrt p\,|\Delta D|}{G_r}\le A\,d\,f(p/r),
\qquad A=\frac{5\,2^{3/4}}{\sqrt\pi},
\quad f(s)=s^{3/2}e^{-9\alpha s^2/16}.
\tag{12}
\]
Use **finite amplitudes**, not the reciprocal phase derivative: for every \(r\ge\alpha\), even arbitrarily large scales,
\[
\frac{\sqrt p\,|\Delta B|}{G_r}\le4\sqrt p\,e^{-\kappa p^2}.
\tag{13}
\]
This eliminates XF-192's raw-gain loophole after row normalization.

For \(0<r\le\alpha\), \(G_r\ge1\),
\(t_r\le\sqrt{\pi/\alpha}\,r\),
\(\pi\Re x_r=\alpha/r^2\), and
\(\pi\Re(1/x_r)\ge\pi^2r^2/(2\alpha)\). Consequently
\[
\frac{\sqrt p\,|\Delta D|}{G_r}
\le4\sqrt p\,e^{-9p^2/(16\alpha)},\qquad
\frac{\sqrt p\,|\Delta B|}{G_r}
\le4\sqrt{\pi/\alpha}\,\sqrt p\,r
e^{-9\pi^2p^2r^2/(32\alpha)}
\le C_\alpha p^{-1/2}.
\tag{14}
\]
Thus there is \(E_\alpha(P)\to0\) such that uniformly for \(p\ge P\),
\[
\frac{\sqrt p\,|\Delta J|}{G_r}
\le\begin{cases}
A\,d\,f(p/r)+E_\alpha(P),&r\ge\alpha,\\
E_\alpha(P),&0<r<\alpha.
\end{cases}
\tag{15}
\]
Choose \(P_1\) with \(E_\alpha(P_1)<\gamma d/2\). If \(\mathcal C(p;\mathcal R)\ge\gamma\), some row satisfies \(r\ge\alpha\) and \(f(p/r)\ge\gamma/(2A)\). Since \(f(s)\to0\) both as \(s\downarrow0\) and \(s\to\infty\), this superlevel set lies in a compact interval \([a,b]\subset(0,\infty)\) depending only on \(\alpha,\gamma\). Such a row can witness only radii \(p\in[ar,br]\).

Choose integer \(h\ge1\) with \(2^h>b/a\). The integer candidate radii
\(p_j=P2^{hj}\), \(0\le j\le\lfloor\log_2(Q/P)/h\rfloor\), are pairwise more widely separated than \(b/a\). No one row witnesses two, so counting the required rows proves (5).

## Prior art, scope, and Xi-flow boundary

Dyadic scale covering is a classical multiscale principle, and one-tone phase sensitivity is elementary Fourier analysis; no generic novelty is claimed. Moitra (STOC 2015, DOI 10.1145/2746539.2746561) and Aubel--Bölcskei (ACHA 2019, DOI 10.1016/j.acha.2017.07.006), already indexed in SOURCES.md, calibrate the neighboring Fourier-conditioning literature. The specific additional calculation here is complete-Jacobi finite-chord stability at matched holomorphic scales together with *uniform all-scale* gain-normalized reciprocal suppression.

This does **not** prove distinct-radius identification, optimality under a fixed-total \(\ell^2\) noise budget or independent stochastic row noise, or anything about arbitrary right-half-plane probes or adaptive selection. The factor \(\sqrt p\) is not an available support-independent prewhitening operation. The theorem assumes source differences can be sampled holomorphically and does not derive this access from the actual Xi heat flow. No Xi-zero exclusion, upper bound on the de Bruijn--Newman constant \(\Lambda\), or RH consequence follows.
