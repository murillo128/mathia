# NB-361 — Non-2-Brjuno seed pairs admit no third-orbit completion

- **Status:** proved (classical tools plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the real-orbit factors and projected target; NB-356 for the phase-series membership test; NB-355 for the dyadic return-charging mechanism
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-OBSTRUCTION

## Claim and scope

NB-360 completes any fixed finite-Diophantine-type seed pair with almost every real third seed. That conclusion cannot be extended to every irrational seed ratio: failure of the classical **2-Brjuno condition** excludes every third seed, including choices giving rational rank three.

Fix real seeds \(p,q>1\), with irrational \(\alpha=\log p/\log q\). Write \(P_j/Q_j=[a_0;a_1,\ldots,a_j]\) for its regular continued-fraction convergents, with \(Q_{-1}=0,Q_0=1\), and define
\[
\mathcal B_2(\alpha)=\sum_{j=1}^{\infty}
\frac{\log Q_{j+1}}{Q_j^2}.
\tag{1}
\]
The omitted initial term is finite and does not affect the classical condition. In \(H=L^2(0,1;dx)\), put
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\}.
\]
Let \(\mathcal N\) be the full continuous Nyman space and \(t=P_{\mathcal N}e\). Then
\[
\boxed{\mathcal B_2(\alpha)=\infty
\quad\Longrightarrow\quad
t\notin\mathcal C_q+\mathcal C_p+\mathcal C_r
\quad\text{for every real }r>1.}
\tag{2}
\]
The sum in (2) is algebraic, with one finite-norm vector from each closed orbit space. Its closure is nevertheless \(\mathcal N\), because the original pair already has irrational log ratio. Thus approximation remains possible, but the total squared norm of the three physical components must diverge as their sum approaches \(t\).

This is a necessary-condition theorem, not a classification of all fixed pairs: no converse under \(\mathcal B_2(\alpha)<\infty\) is claimed. It concerns real seeds and gives no new obstruction for specified multiplicatively independent integer seeds, whose ratios have finite Diophantine type and satisfy (1).

## 1. The physical target imposes the Euclidean phase series

For \(\beta=\log r/\log q>0\), define
\[
S_\alpha(\beta)=\sum_{n\ge1}
\frac1{n^2\bigl(\|n\alpha\|_{\mathbb R/\mathbb Z}^2+
\|n\beta\|_{\mathbb R/\mathbb Z}^2\bigr)}.
\tag{3}
\]
NB-356's real-seed extension gives
\[
t\in\mathcal C_q+\mathcal C_p+\mathcal C_r
\quad\Longleftrightarrow\quad S_\alpha(\beta)<\infty.
\tag{4}
\]
Here the needed implication can be checked directly. In the unitary Mellin model,
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad
\mathcal Mt=Bb/s,\qquad b=B(1)>0,
\]
\[
\Theta_v(s)=\frac{s}{s-1}\frac1{\sqrt v}
\frac{1-v^{1-s}}{1-v^{-s}},\qquad H^2=H^2(\Re s>1/2).
\tag{5}
\]
The zeros of \(\Theta_q\) are precisely \(z_\ell=1+2\pi i\ell/\log q\), \(\ell\ne0\). Remove the common inner factor \(B\) isometrically. An exact decomposition gives
\[
b/s=\Theta_q U_q+\Theta_p U_p+\Theta_r U_r,
\qquad U_v\in H^2,\quad \|U_v\|=\|u_v\|.
\]
At the nonzero lattice points,
\[
|b/z_\ell|\asymp_{q,b}|\ell|^{-1},\qquad
|\Theta_p(z_\ell)|^2+|\Theta_r(z_\ell)|^2
\asymp_{p,q,r}\|\ell\alpha\|^2+\|\ell\beta\|^2.
\]
Cauchy--Schwarz and the bounded lattice sampler
\[
\sum_{\ell\in\mathbb Z}|U(z_\ell)|^2
\le\frac{\log q}{1-q^{-1}}\|U\|^2
\]
therefore imply
\[
S_\alpha(\beta)\le C_{p,q,r,b}
(\|u_p\|^2+\|u_r\|^2)<\infty.
\tag{6}
\]
No lower bound for \(|B(z_\ell)|\) is used. The removable point \(s=1\) is not treated as a zero. Repeated seed spaces cause no problem for this necessary inequality.

## 2. A regularized return bound, uniform in the free phase

For every real \(\theta\), \(\eta>0\), and integer \(L\ge1\) satisfying \(\eta L^2\le1\),
\[
\boxed{\sum_{m=1}^L
\frac1{m^2\bigl((m\eta)^2+\|m\theta\|^2\bigr)}
\ge\frac{1+\lfloor\log_2 L\rfloor}{2}.}
\tag{7}
\]
The positive regularizer makes the assertion valid even when \(\theta\) is rational.

Set \(K=\lfloor\log_2 L\rfloor\). For every \(0\le k\le K\), Dirichlet's pigeonhole argument selects \(1\le m_k\le2^k\) with \(\|m_k\theta\|\le2^{-k}\). At that index,
\[
m_k\eta\le2^k\eta\le2^{-k},
\]
since \(\eta4^k\le\eta L^2\le1\). Thus its summand in (7) is at least \(4^k/(2m_k^2)\).

If the same integer \(m\) is selected at \(h\) scales \(k_1<\cdots<k_h\), use the largest scale for the denominator and \(m\le2^{k_1}\) for its size:
\[
\frac1{m^2((m\eta)^2+\|m\theta\|^2)}
\ge\frac{4^{k_h-k_1}}2
\ge\frac{4^{h-1}}2\ge\frac h2.
\tag{8}
\]
The distinct selected indices therefore pay for all \(K+1\) scales without being counted twice. This proves (7); it assumes no equidistribution, independence, irrationality, or spacing of the selected returns.

## 3. Disjoint convergent blocks force the 2-Brjuno condition

Write \(\eta_j=\|Q_j\alpha\|\). The classical convergent estimate gives \(0<\eta_j<1/Q_{j+1}\). Restrict to
\[
\mathcal J=\{j\ge1:Q_{j+1}\ge\max(16,4Q_j^2)\},\qquad
L_j=\lfloor\sqrt{Q_{j+1}}\rfloor.
\]
For \(j\in\mathcal J\),
\[
\eta_j L_j^2<1,\qquad
Q_jL_j\le Q_j\sqrt{Q_{j+1}}\le Q_{j+1}/2.
\tag{9}
\]
On the indices \(n=Q_jm\), \(1\le m\le L_j\), the circle triangle inequality yields
\[
\|Q_jm\alpha\|\le m\eta_j,\qquad
\|Q_jm\beta\|=\|m(Q_j\beta)\|.
\]
Use (7) with \(\theta=Q_j\beta\):
\[
\sum_{m=1}^{L_j}
\frac1{(Q_jm)^2(\|Q_jm\alpha\|^2+\|Q_jm\beta\|^2)}
\ge\frac{1+\lfloor\log_2 L_j\rfloor}{2Q_j^2}
\ge\frac{\log Q_{j+1}}{8(\log2)Q_j^2}.
\tag{10}
\]
For the last inequality, \(L_j\ge\sqrt{Q_{j+1}}/2\) and \(Q_{j+1}\ge16\) give \(\log L_j\ge\tfrac14\log Q_{j+1}\).

Crucially, every index used in (10) lies in \([Q_j,Q_{j+1})\). The denominators \(Q_1,Q_2,\ldots\) are strictly increasing, even when the omitted initial denominator \(Q_0\) equals \(Q_1\). Hence blocks for distinct \(j\) are disjoint. Positivity now permits summation:
\[
\boxed{S_\alpha(\beta)\ge
\frac1{8\log2}\sum_{j\in\mathcal J}
\frac{\log Q_{j+1}}{Q_j^2}
\quad\text{for every real }\beta.}
\tag{11}
\]

The discarded indices cannot carry a divergent part of (1). Apart from finitely many with \(Q_{j+1}<16\), they satisfy \(Q_{j+1}<4Q_j^2\), so
\[
\sum_{j\notin\mathcal J}\frac{\log Q_{j+1}}{Q_j^2}
\le C_\alpha+\sum_{j\ge1}\frac{\log4+2\log Q_j}{Q_j^2}<\infty.
\tag{12}
\]
The last series converges because \(Q_j\) grows at least at Fibonacci rate and \((\log4+2\log x)/x^2\) is decreasing for \(x\ge1\). Equations (11)--(12) prove
\[
S_\alpha(\beta)<\infty\quad\Longrightarrow\quad
\mathcal B_2(\alpha)<\infty,
\tag{13}
\]
which, with (6), proves (2). This uses the entire divergent sum, not merely a nonzero limsup of its summands.

## 4. An explicit empty completion family and its norm boundary

Define a real irrational ratio recursively by
\[
\alpha_*=[1;2,a_2,a_3,\ldots],\qquad
a_{j+1}=\left\lceil\exp(Q_j^2/j)\right\rceil\quad(j\ge1).
\tag{14}
\]
The denominators are determined successively, so this defines one ordinary infinite continued fraction. Since
\(a_{j+1}Q_j\le Q_{j+1}\le(a_{j+1}+1)Q_j\),
\[
\frac1j+\frac{\log Q_j}{Q_j^2}
\le\frac{\log Q_{j+1}}{Q_j^2}
\le\frac1j+\frac{\log Q_j+\log3}{Q_j^2}.
\tag{15}
\]
Thus \(\mathcal B_2(\alpha_*)=\infty\), although its individual summands tend to zero. This control rules out replacing the summability obstruction by only a test that individual terms fail to vanish. The ratio is Liouville, since \(Q_j^2/(j\log Q_j)\to\infty\).

For any fixed \(q>1\), choose \(p=q^{\alpha_*}\). No real \(r>1\) completes these two orbit spaces to an algebraic representation of \(t\). In particular choose \(r=q^\beta\) with positive \(\beta\notin\mathbb Q+\mathbb Q\alpha_*\); then the three seed logarithms have rational rank three, yet (2) still applies. NB-356's rank-two obstruction alone cannot explain this example.

For fixed such \(p,q,r\), set
\[
E_3(\varepsilon)=\inf\left\{\sum_{v=q,p,r}\|u_v\|^2:
u_v\in\mathcal C_v,\ \left\|t-\sum_vu_v\right\|\le\varepsilon\right\}.
\]
Then \(E_3(\varepsilon)<\infty\) for every \(\varepsilon>0\), by the two-orbit closure theorem, but \(E_3(\varepsilon)\to\infty\) as \(\varepsilon\downarrow0\). Otherwise a bounded sequence of triples would have a weakly convergent subsequence in the Hilbert direct sum. Each closed orbit space is weakly closed, and the sums converge strongly to \(t\), producing the excluded exact decomposition. No quantitative rate for this divergence is asserted.

## Prior art, mathematical delta, and limitations

Lee, Marmi, Petrykiewicz and Schindler, *Regularity properties of k-Brjuno and Wilton functions*, Aequationes Math. 98 (2024), 13--85, [Section 1.2, equation (1.4)](https://link.springer.com/article/10.1007/s00010-023-00967-w), explicitly defines the classical k-Brjuno series used in (1). Their [correction](https://link.springer.com/article/10.1007/s00010-023-01028-y) concerns formulas (1.10)--(1.11), not that definition. The condition and continued-fraction construction are not new.

Borda, *On the theorem of Davenport and generalized Dedekind sums*, [Section 4 and Theorem 3](https://arxiv.org/pdf/1606.07946), studies reciprocal-power sums by separating multiples of convergent denominators. This is the classical arithmetic mechanism behind (9)--(12). Beresnevich, Haynes and Velani, *Sums of reciprocals of fractional parts and multiplicative Diophantine approximation*, [Section 2.2, Theorem 2.2](https://arxiv.org/pdf/1511.06862), supplies the neighboring fixed-coordinate metric framework; its multiplicative almost-everywhere theorem is not used to infer the universal Euclidean-series obstruction proved here.

Burnol's [Section 2 and Lemma 2.4](https://arxiv.org/pdf/math/9910055) supply the common inner factor and target projection. The orbit realization and lattice sampling are already reconstructed in NB-354--NB-356. The local delta is the disjoint-block implication (13) and its transfer to **every** third real seed for a fixed non-2-Brjuno pair. It is a derived application of classical tools, with no claim to a new general Diophantine theory.

- Finite Diophantine type implies \(Q_{j+1}\ll Q_j^\nu\), hence (1) converges. This is compatible with NB-360 and does not weaken its fixed-integer-pair conclusion. Ordinary Liouville behavior alone is not shown sufficient for the obstruction.
- Convergence of (1) is only necessary. Even a finite-type ratio still has exceptional third seeds with infinite (3), as NB-360 shows. No all-seed or almost-everywhere converse under just the 2-Brjuno condition is established.
- This is a three-space obstruction. Adding two freely varying real seeds can instead use NB-356's joint almost-everywhere finite two-phase series; including the fixed \(\alpha\) in its denominator only decreases it. No no-go for every finite number of additional seeds follows.
- For every sum \(w\) of these orbit vectors, \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The Burnol floor is unchanged. There is no RH conclusion, discrete-section rate, finite generator count, or effective computation of \(B\).

Evidence is the analytic proof and the inspected primary sources. An ephemeral exact-rational stress check of (8) used all 325 distinct phases in \([0,1]\) of denominator at most 32 and \(K=0,\ldots,8\), with \(\eta=4^{-K},L=2^K\): all 2,925 cases passed, including a return reused at nine scales. That bounded check is not evidence for the infinite limit. The decisive proof audits are the regularizer inequality at every selected scale, charging repeated returns only once, disjointness in (9), and convergence of the discarded contribution (12). No Lean verification or independent adversarial approval is asserted.
