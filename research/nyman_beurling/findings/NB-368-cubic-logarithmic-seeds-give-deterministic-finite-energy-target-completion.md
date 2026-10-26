# NB-368 — Cubic logarithmic seeds give deterministic finite-energy target completion

- **Status:** proved (classical Diophantine mechanism plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 for real-orbit target membership and the bounded lattice lift; NB-360 for the full physical component-cost comparison; NB-362 for the completing Liouville control
- **Classification:** LITERATURE+DERIVED + EXACT-TARGET-MEMBERSHIP + DETERMINISTIC-CONTROL

## Claim and scope

There are explicitly specified triples of real Nyman seeds that assemble the projected target with finite physical component energy. No almost-everywhere selection of the third seed is needed. For every fixed real \(q>1\), put
\[
\theta=\sqrt[3]{2},\qquad p=q^\theta,\qquad r=q^{\theta^2}.
\tag{1}
\]
In \(H=L^2(0,1;dx)\), retain
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},
\quad\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},
\quad t=P_{\mathcal N}e.
\]
Then
\[
\boxed{t\in\mathcal C_q+\mathcal C_p+\mathcal C_r,\qquad
\inf_{\substack{u_v\in\mathcal C_v\\t=u_q+u_p+u_r}}\sum_{v=q,p,r}\|u_v\|^2<\infty.}
\tag{2}
\]
The sum is algebraic, with one vector in each **closed real-dilation orbit**. It is not a finite sum of dilation generators. The common zeta inner factor and the target projection are retained throughout.

A deterministic sufficient condition explains this example. For fixed positive real \(\alpha,\beta\), define
\[
R_n=\max(\|n\alpha\|_{\mathbb R/\mathbb Z},\|n\beta\|_{\mathbb R/\mathbb Z}),
\quad
S_{\ge N}(\alpha,\beta)=\sum_{n\ge N}
\frac1{n^2(\|n\alpha\|^2+\|n\beta\|^2)}.
\tag{3}
\]
If
\[
R_n\ge\gamma n^{-\nu}\quad(n\ge1),\qquad
\gamma>0,\quad\frac12\le\nu<1,
\tag{4}
\]
then \(S_{\ge1}<\infty\), and the seeds \(q,q^\alpha,q^\beta\) satisfy (2). More precisely, for integer \(N\ge1\),
\[
\boxed{
S_{\ge N}\le
\begin{cases}
16\gamma^{-2}\,[1+\log(2N)]/N,&\nu=1/2,\\[2mm]
\displaystyle\frac{4\,2^{2\nu}\zeta(2\nu)}{1-2^{2\nu-2}}
\gamma^{-2}N^{2\nu-2},&1/2<\nu<1.
\end{cases}}
\tag{5}
\]
The cubic pair in (1) satisfies (4) with \(\nu=1/2\) and the explicit constant in (11) below. The strict upper threshold \(\nu<1\) cannot be replaced by \(\nu\le1\): an explicit rank-two triple obeys the return inequality in (4) at \(\nu=1\) but fails completion. Conversely, (4) is not necessary for completion: a Liouville fixed ratio excludes this power certificate for **every** third phase, even when almost every third phase completes the target.

## 1. Count return times, including their first occurrence

For \(0<y\le1/2\), enumerate the positive indices with \(R_n\le y\) as \(n_1<n_2<\cdots\). Condition (4) and the triangle inequality on the two-dimensional torus give
\[
n_1\ge(\gamma/y)^{1/\nu},\qquad
n_{j+1}-n_j\ge D_y:=(\gamma/(2y))^{1/\nu}.
\tag{6}
\]
Indeed \(R_{n_{j+1}-n_j}\le2y\). Hence \(n_j\ge jD_y\), so at most \(2N/D_y\) such indices occur below \(2N\). The separate first-return bound is necessary: spacing alone would leave a possible exceptional first point arbitrarily close to the origin.

Order the \(N\) values \(R_n\), \(N\le n<2N\), as \(\rho_1\le\cdots\le\rho_N\). Applying the preceding count at \(y=\rho_j\) gives
\[
\rho_j\ge\frac\gamma2\left(\frac j{2N}\right)^\nu.
\]
Since the Euclidean squared denominator in (3) is at least \(R_n^2\),
\[
\sum_{N\le n<2N}
\frac1{n^2(\|n\alpha\|^2+\|n\beta\|^2)}
\le4\,2^{2\nu}\gamma^{-2}N^{2\nu-2}
\sum_{j=1}^N j^{-2\nu}.
\tag{7}
\]
At \(\nu=1/2\), use \(\sum_{j\le N}j^{-1}\le1+\log N\). Summing (7) over blocks beginning at \(2^kN\), and using \(\sum_{k\ge0}2^{-k}=\sum_{k\ge0}k2^{-k}=2\), gives the first line of (5). For \(\nu>1/2\), use \(\zeta(2\nu)\) and a geometric series to obtain the second.

This estimates the **entire positive series**, including accumulation of small summands. Neither equidistribution nor independence is used. In contrast, the pointwise estimate alone gives terms \(O(n^{2\nu-2})\), which is not summable even at \(\nu=1/2\). The gain comes from applying the same Diophantine lower bound to differences of return indices.

## 2. An elementary algebraic norm supplies a specified pair

Let \(m,\ell\) be the nearest integers to \(n\theta,n\theta^2\), and set
\[
\epsilon_1=m-n\theta,\quad\epsilon_2=\ell-n\theta^2,
\quad E=\max(|\epsilon_1|,|\epsilon_2|)\le1/2.
\]
The algebraic integer
\(Z=\ell+m\theta+n\theta^2\) is nonzero: \(1,\theta,\theta^2\) are rationally independent, by irreducibility of \(X^3-2\). Its field norm is a nonzero integer,
\[
\operatorname{Nm}(Z)=\ell^3+2m^3+4n^3-6\ell mn.
\tag{8}
\]
For a primitive cube root of unity \(\omega\), the two non-real conjugates satisfy
\[
Z_1=\ell+m\theta\omega+n\theta^2\omega^2
=\epsilon_2+\theta\omega\epsilon_1,\qquad Z_2=\overline{Z_1}.
\tag{9}
\]
Here the leading terms cancel because \(1+\omega+\omega^2=0\). The real conjugate obeys
\[
|Z|\le3n\theta^2+(1+\theta)/2
\le C_0 n,\qquad C_0=3\theta^2+(1+\theta)/2.
\]
Thus
\[
1\le|\operatorname{Nm}(Z)|=|Z|\,|Z_1|^2
\le C_0n(1+\theta)^2E^2,
\tag{10}
\]
and consequently
\[
\boxed{\max(\|n\theta\|,\|n\theta^2\|)
\ge\gamma_\theta n^{-1/2},\qquad
\gamma_\theta=[C_0(1+\theta)^2]^{-1/2}.}
\tag{11}
\]
This is the classical algebraic-number-field construction of a simultaneously badly approximable vector, specialized with a directly proved constant. No unproved assertion about bounded partial quotients of a cubic irrational is involved; each individual coordinate may have much closer returns. The two coordinates cannot have those returns simultaneously.

## 3. Transport the convergent series to all three physical components

Use the exact NB-356/NB-360 dictionary
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,
\quad\mathcal Mt=Bb/s,\quad b=B(1)>0,
\quad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})},
\tag{12}
\]
where \(H^2=H^2(\Re s>1/2)\) and \(\mathcal M\) is unitary. Multiplication by each inner factor is isometric; division by \(B\) is used only on its range. Set \(L=\log q\), \(\tau=2\pi/L\), \(z_k=1+i\tau k\), and \(f=b/s\). At the nonzero zeros of \(\Theta_q\), put
\[
a_k=|\Theta_p(z_k)|^2+|\Theta_r(z_k)|^2,
\qquad T=\sum_{k\ne0}\frac{|f(z_k)|^2}{a_k}.
\]
For \(p=q^\alpha,r=q^\beta\), the elementary factor bounds give
\[
a_k\ge c_*\big(\|k\alpha\|^2+\|k\beta\|^2\big),
\qquad c_*=\min_{v=p,r}\frac{16v}{(v+1)^2}>0,
\quad
T\le\frac{2b^2}{\tau^2c_*}S_{\ge1}(\alpha,\beta).
\tag{13}
\]
In particular (5) controls the complete data norm with constants depending only on the stated seeds and \(b\).

To exhibit the components, define, for \(v=p,r\),
\[
d_{v,k}=\frac{f(z_k)\overline{\Theta_v(z_k)}}{a_k}\ (k\ne0),
\qquad d_{v,0}=0,\qquad U_v=R_qd_v.
\]
The NB-356 lift is
\[
(R_qd)(s)=\int_0^L\left(\frac1L\sum_{k\in\mathbb Z}
d_ke^{i\tau kx}\right)e^{-(s-1)x}\,dx,
\qquad\|R_qd\|^2\le(q/L)\|d\|_{\ell^2}^2,
\tag{14}
\]
with the Fourier sum understood in \(L^2(0,L)\). It interpolates every \(z_k\). Therefore
\[
U_q=\frac{f-\Theta_pU_p-\Theta_rU_r}{\Theta_q}\in H^2.
\]
The numerator vanishes at every zero of the pure simple-zero Blaschke factor \(\Theta_q\); its removable point \(s=1\) imposes no zero condition. If \(H_*=\|U_p\|^2+\|U_r\|^2\), then
\[
H_*\le(q/L)T,\qquad
\|U_q\|\le b+\sqrt{2H_*},\qquad
\boxed{\sum_{v=q,p,r}\|U_v\|^2\le2b^2+5(q/L)T.}
\tag{15}
\]
Taking \(\mathcal Mu_v=B\Theta_vU_v\) proves (2) with the physical norms, including the anchor component.

There is also a certified meaning for truncating the **non-anchor interpolation data**. Put \(U_v^{<N}=R_q(d_v\mathbf1_{|k|<N})\), for \(v=p,r\). Equations (13)--(14) imply
\[
\sum_{v=p,r}\|U_v-U_v^{<N}\|^2
\le\frac{2qb^2}{L\tau^2c_*}S_{\ge N}(\alpha,\beta).
\tag{16}
\]
For (1) this is \(O_q(\log(2N)/N)\). Isometric multiplication transfers the same bound to the two physical orbit components. This does **not** define a truncated anchor by dividing a nonvanishing numerator: that operation would generally leave \(H^2\). Nor is a finite Fourier-data lift a finite Nyman-generator representation.

## 4. The exponent-one boundary can fail

Take \(\alpha=\sqrt2\), \(\beta=2\sqrt2-1\); both lie in \((1,2)\). If \(m\) is nearest to \(n\sqrt2\), then
\[
1\le|2n^2-m^2|\le(2\sqrt2+1/2)n\|n\sqrt2\|.
\]
Thus \(R_n\ge c/n\), satisfying the return inequality in (4) at the excluded endpoint \(\nu=1\). But
\(\|n\beta\|=\|2n\sqrt2\|\le2\|n\sqrt2\|\). Along the infinitely many continued-fraction convergent denominators of \(\sqrt2\),
\[
\frac1{n^2(\|n\alpha\|^2+\|n\beta\|^2)}\ge\frac15.
\tag{17}
\]
The series diverges, so NB-356 excludes exact target completion. This is a genuine distinct-seed control with logarithmic rank two, not a zero denominator or duplicate seed. It shows only that the universal sufficient exponent range cannot include its endpoint; it does not classify all rank-three pairs of joint exponent one.

More generally, if \(R_n\le n^{-1-\eta}\) for infinitely many \(n\) and some \(\eta>0\), the corresponding summands are at least \(n^{2\eta}/2\), again excluding completion. Thus the strict subunit and superunit joint-return regimes have opposite conclusions, while the borderline needs finer information.

## 5. A Liouville fixed ratio excludes the power certificate, not completion

The joint lower bound (4) imposes a finite-type restriction on each fixed coordinate. Specifically, if \(\alpha\) is irrational and (4) holds for some real \(\beta\), then
\[
\boxed{\|h\alpha\|\ge
\left(\frac{\gamma}{2^{1+\nu}}\right)^{2/(1-\nu)}
h^{-2\nu/(1-\nu)}\qquad(h\ge1).}
\tag{18}
\]
This is a classical Diophantine transference obstruction; a direct multiplier argument gives the constants required here.

Fix \(h\ge1\), put \(\eta=\|h\alpha\|\in(0,1/2]\), and choose
\(M=\lceil\eta^{-1/2}\rceil\le2\eta^{-1/2}\).
The one-dimensional Dirichlet pigeonhole principle supplies \(1\le m\le M\) such that
\(\|mh\beta\|\le1/M\le\sqrt\eta\). At \(n=hm\),
\[
\|n\alpha\|\le m\eta\le2\sqrt\eta,
\qquad R_n\le2\sqrt\eta,
\qquad n\le2h\eta^{-1/2}.
\]
Apply (4) at this actual positive integer \(n\), rather than treating the multiplier as a free real variable:
\[
\gamma\le n^\nu R_n
\le2^{1+\nu}h^\nu\eta^{(1-\nu)/2}.
\tag{19}
\]
Rearrangement proves (18). The argument permits rational \(\beta\) and requires no independence of the phases. The same implication holds for the other coordinate when it is irrational.

For a Liouville \(\alpha\), (18) is impossible for every fixed \(\nu<1\) and \(\gamma>0\). Equivalently, for every real \(\beta\),
\[
\inf_{n\ge1}n^\nu R_n=0\qquad(1/2\le\nu<1).
\tag{20}
\]
The small values occur at unbounded indices: \(\alpha\)'s irrationality makes \(R_n>0\) on every finite set. Equation (20) concerns a sufficient power certificate, not the convergence of (3).

To separate those questions within the actual Nyman construction, use NB-362's ratio
\[
\alpha_+=[1;2,a_2,a_3,\ldots],\qquad
a_{j+1}=\lceil\exp(\sqrt{Q_j})\rceil,
\tag{21}
\]
where \(Q_j\) are its successive convergent denominators. Then
\(\log Q_{j+1}=\sqrt{Q_j}+\log Q_j+O(1)\).
Thus \(Q_{j+1}/Q_j^A\to\infty\) for every fixed \(A\), making \(\alpha_+\) Liouville, while
\[
\sum_j\frac{\log Q_{j+1}}{Q_j}<\infty
\]
by at-least-Fibonacci growth. NB-362's clipped-moment argument therefore makes \(S_{\ge1}(\alpha_+,\beta)\) finite for almost every \(\beta\in(1,2)\), and its bounded Hardy lift supplies all three finite-norm physical components. Nevertheless **none** of those completing \(\beta\) satisfies (4) for any \(\nu<1\). Removing the countable set \(\mathbb Q+\mathbb Q\alpha_+\) retains this conclusion with rational rank three.

In particular, searching for a stronger constant or a subunit joint power exponent cannot settle exceptional completion for a 2-Brjuno but non-Brjuno fixed ratio: every non-Brjuno irrational is Liouville, since finite type forces \(Q_{j+1}\ll Q_j^A\) and hence Brjuno convergence. The exceptional-existence question remains open here. The available power certificate misses even the successful control (21), so its failure cannot be promoted to a target-membership obstruction.

## Prior art, mathematical delta, and limits

The algebraic construction is classical. Bugeaud, *On the multiples of a badly approximable vector*, Acta Arith. 168 (2015), 71–81, DOI `10.4064/aa168-1-4`, [author manuscript, abstract and Section 1](https://irma.math.unistra.fr/~bugeaud/travaux/multbad1.pdf), explicitly records simultaneous bad approximability of \((\theta,\ldots,\theta^d)\) for a real algebraic number of degree \(d+1\). Equations (8)--(11) prove the needed cubic specialization without importing a transference constant. Neither algebraic bad approximability nor the gap-counting principle is claimed new.

For the reciprocal-sum mechanism, Fregoli, *Sums of reciprocals of fractional parts*, [author manuscript, Section 1, gap argument preceding Theorem 1.2](https://pure.royalholloway.ac.uk/ws/files/34774891/1805.00865v1.pdf), gives a neighboring classical gap-principle bound for reciprocal linear-form distances. Its scalar linear-form sum differs from (3); the full joint-return estimate required here is proved in (6)--(7). The sampling and inner-factor machinery, including the Burnol target projection, is already proved and literature-anchored in NB-356/NB-360.

Ramírez, *Khintchine types of translated coordinate hyperplanes*, Acta Arith. 170 (2015), 243–273, DOI `10.4064/aa170-3-3`, [accepted manuscript, Section 2.1, remark on Khintchine's transference principle](https://eprints.whiterose.ac.uk/114053/1/hyperplanes.pdf), records the classical fixed-coordinate transference mechanism. Equations (18)--(19) prove the precise two-coordinate bound used here directly; no new transference theorem is claimed. The completing Liouville control is already proved in NB-362. Their combination identifies the limitation of (4), rather than establishing a new completion class.

The local addition is a deterministic, norm-certified **specified real-seed** completion family, together with a sufficient joint-return threshold and interpolation-data tail bound. NB-356 gives the exact test and a two-variable metric control; NB-360/NB-366 choose almost every third seed after fixing a pair. Those measure statements do not evaluate the specified point \((\theta,\theta^2)\). The present result does so by the algebraic norm. It is a derived application of classical tools, not a claim to bibliographic priority for a new approximation theorem.

- The seed logarithms in (1) have rational rank three. Their actual values are real; this does not settle the arithmetic triple \(2,3,5\), or construct a completing third seed for every fixed pair.
- The lower bound is for the **maximum** of two return distances, not their product. No multiplicative bad-approximation hypothesis or Littlewood-conjecture consequence is used.
- The exact component construction retains \(B\) and \(b\). The scalar series and its tail are explicitly controlled, but the construction does not provide source-only access to the unknown zeta-zero factor or to the projected target.
- Every orbit sum \(w\) still satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The Burnol floor and the RH question are unchanged.
- Closed real-dilation spaces allow infinitely many generators and unrestricted dilation range. Neither (5) nor (16) bounds a discrete Nyman-section distance, finite generator count, or absolute coefficient cost.

Evidence is the analytic proof and the inspected primary literature. An ephemeral exact polynomial determinant check verified (8). For \(1\le n\le10{,}000\), 20,000 integer cubic inequalities certified the two nearest integers and 10,000 integer norm checks were positive (minimum one). These finite checks audit the algebraic normalization only; they do not establish infinite-series convergence. An additional exact-rational check passed 53,136 multiplier controls in (19), including rational second phases, \(\eta=1/2\), and reciprocal-square ceiling boundaries. It checks the finite inequalities, not the Liouville or almost-everywhere assertions. The decisive analytic audits are the first-return bound as well as return-gap spacing, summation of the complete series, the conjugate cancellation in (9), inclusion of the anchor norm in (15), and the strict sign of \(1-\nu\) in (18)--(19). No Lean verification or independent adversarial approval is asserted.
