# WI-458 — Euler Hankel peaks have exponentially small height density

**Status:** EXACT-DERIVED + CLASSICAL-CONCENTRATION + SOURCE-FAMILY-BOUNDARY + NO-NOVELTY-CLAIM + NON-RH

**Local dependency:** WI-457, for the normalized Euler symbol, the exact Hardy response, and the recurrent pole-scale maximum.

## Claim and quantifiers

Retain the WI-457 conventions
\[
L(s)=-\zeta'(s)/\zeta(s),\quad A_\varepsilon=L(1+\varepsilon),\quad
\varphi_\varepsilon(t)=L(1+\varepsilon+it)/A_\varepsilon,
\]
\[
k_{r,\gamma}(t)=\frac{\sqrt{r/\pi}}{r-i(t-\gamma)},\qquad
Q_\varepsilon(r,\gamma)
=\|P_-(\varphi_\varepsilon k_{r,\gamma})\|_2^2.
\tag{1}
\]
Here \(\varepsilon,r>0\), the Fourier phase is \(e^{-it\xi}\), and \(P_-\) projects onto negative frequencies. All the symbols are bounded by one. For a measurable set of real heights define
\[
d^*(E)=\limsup_{H\to\infty}\sup_{T\in\mathbb R}
\frac{|E\cap[T,T+H]|}{H}.
\tag{2}
\]
The finite absolute constant
\[
B=2\sum_{p\ \mathrm{prime}}(\log p)^3\frac{p^2}{(p-1)^4}
\tag{3}
\]
gives, for every \(\tau>0\),
\[
\boxed{
d^*\{\gamma:Q_\varepsilon(r,\gamma)\ge\tau\}
\le \exp\!\left[-\frac{(A_\varepsilon\sqrt\tau-\sqrt{rB})_+^2}{2rB}\right].}
\tag{4}
\]
In particular, for fixed \(q,\tau>0\), there is \(c_{q,\tau}>0\) such that, for sufficiently small \(\varepsilon>0\),
\[
\boxed{d^*\{\gamma:Q_\varepsilon(q\varepsilon,\gamma)\ge\tau\}
\le \exp(-c_{q,\tau}/\varepsilon^3).}
\tag{5}
\]
This upper bound is not claimed sharp. If \(0<\tau<q/(1+q)^2\), the same set has **positive** lower uniform density at every sufficiently small fixed \(\varepsilon\). Thus recurrent order-one peaks coexist with exponentially small height density.

The order of limits in (4)--(5) is essential: the infinite-height density is taken at each fixed \(\varepsilon,r\), then \(\varepsilon\) tends to zero. A separate quantitative finite-window estimate, uniform in the window's starting height, is
\[
\frac1H\int_T^{T+H}Q_\varepsilon(r,\gamma)\,d\gamma
=\mu_\varepsilon(r)+O(H^{-1}),\qquad 0<\varepsilon\le1,
\tag{6}
\]
with an absolute implied constant, all \(r,H>0\), and
\[
\mu_\varepsilon(r)=A_\varepsilon^{-2}
\sum_{n\ge2}\frac{\Lambda(n)^2}{n^{2+2\varepsilon}}(1-n^{-2r}).
\tag{7}
\]
For fixed \(q>0\),
\[
\mu_\varepsilon(q\varepsilon)
=2qC\varepsilon^3+O_q(\varepsilon^4),\qquad
C=\sum_{n\ge2}\frac{\Lambda(n)^2\log n}{n^2}>0.
\tag{8}
\]
Consequently the finite-window superlevel fraction is at most
\((\mu_\varepsilon(r)+C_0/H)/\tau\) for an absolute \(C_0\). The exponential bound (5) has no asserted uniform finite-height convergence rate.

## Prime blocks, rather than independent prime powers

Translation reduces the unnormalized response to a vector in the fixed Hilbert space \(\mathcal H_-\):
\[
W_\gamma=P_-\big(L(1+\varepsilon+i(t+\gamma))k_{r,0}(t)\big),
\qquad \|W_\gamma\|^2=A_\varepsilon^2Q_\varepsilon(r,\gamma).
\tag{9}
\]
Set \(h_\omega=P_-(e^{-i\omega t}k_{r,0})\). The single-tone Fourier shift gives
\[
\|h_\omega\|^2=1-e^{-2r\omega}.
\tag{10}
\]
Grouping the absolutely convergent Euler series by primes gives
\[
W(z)=\sum_p X_p(z_p),\qquad
X_p(z)=\sum_{k\ge1}\frac{\log p}{p^{k(1+\varepsilon)}}z^k h_{k\log p},
\quad z_p=e^{-i\gamma\log p}.
\tag{11}
\]
Under product Haar measure, the variables \(z_p\) are independent uniform circle variables and \(\mathbb E X_p=0\). The powers \(z_p^k\) of one prime are **not** independent; they are retained in the same block throughout.

The norm of one block is at most
\[
b_p=\sum_{k\ge1}\frac{\log p}{p^{k(1+\varepsilon)}}
\sqrt{1-p^{-2rk}}
\le \sqrt{2r}(\log p)^{3/2}\sum_{k\ge1}\frac{k}{p^k}
=\sqrt{2r}(\log p)^{3/2}\frac{p}{(p-1)^2}.
\tag{12}
\]
We used \(1-e^{-x}\le x\), \(\sqrt{k}\le k\), and \(\varepsilon>0\). In particular \(\sum_p b_p^2\le rB\), and (3) converges even when the prime sum is enlarged to all integers. Orthogonality of distinct positive powers on each circle gives the stronger exact identity
\[
\mathbb E\|W\|^2
=D_\varepsilon(r):=\sum_{n\ge2}\frac{\Lambda(n)^2}{n^{2+2\varepsilon}}(1-n^{-2r})
\le rB.
\tag{13}
\]
No random model for the zero set enters this calculation.

## Bounded differences and the deterministic height transfer

First use finitely many prime blocks. Changing \(z_p\) changes the real function \(F(z)=\|W(z)\|\) by at most \(2b_p\). The bounded-differences inequality gives
\[
\Pr(F-\mathbb EF\ge u)
\le\exp\!\left(-\frac{u^2}{2\sum_p b_p^2}\right),\qquad u>0.
\tag{14}
\]
For completeness, expose the independent coordinates successively. Each Doob martingale increment has conditional range length at most \(2b_p\). The conditional Hoeffding bound multiplies to
\(\mathbb E e^{\lambda(F-\mathbb EF)}\le
\exp(\lambda^2\sum_p b_p^2/2)\).
Markov's inequality optimized at \(\lambda=u/\sum_p b_p^2\) proves (14). Cauchy--Schwarz and (13) give \(\mathbb EF\le\sqrt{rB}\).

At each fixed \(\varepsilon>0\), (11) converges uniformly in all phase coordinates in Hilbert norm: its tail is bounded by the tail of the absolutely convergent positive Euler series. Therefore both the norm expectations and the finite-block concentration bounds pass to the infinite product. This proves
\[
\Pr(\|W\|\ge A_\varepsilon\sqrt\tau)
\le\exp\!\left[-\frac{(A_\varepsilon\sqrt\tau-\sqrt{rB})_+^2}{2rB}\right].
\tag{15}
\]

The transfer to heights is exact in this half-plane. The logarithms of distinct primes are rationally independent by unique factorization. Every nonconstant finite torus character therefore has average over \([T,T+H]\) bounded by a constant times \(H^{-1}\), independently of \(T\). Finite trigonometric approximation gives uniform-in-\(T\) equidistribution for continuous functions of finitely many prime phases. Uniform convergence of (11) then gives the same assertion for continuous functions of \(\|W\|\).

To handle a superlevel indicator, majorize \(1_{[v,\infty)}\) by continuous functions that vanish on \(( -\infty,v-\delta]\), apply this uniform averaging statement, then let \(\delta\downarrow0\). The resulting upper density is at most \(\Pr(\|W\|\ge v)\); no assumption that the limiting law has a density is needed. This proves (4). Finally \(A_\varepsilon=\varepsilon^{-1}+O(1)\) makes the exponent in (4), at \(r=q\varepsilon\), asymptotic to \(\tau/(2qB\varepsilon^3)\), proving (5).

## Finite-window mean and the cubic scale

Write \(a_n=\Lambda(n)n^{-1-\varepsilon}/A_\varepsilon\). The exact WI-457 identity is
\[
Q_\varepsilon(r,\gamma)
=(P_r*|\varphi_\varepsilon|^2)(\gamma)
-\left|\sum_{n\ge2}a_n n^{-r-i\gamma}\right|^2,
\tag{16}
\]
where \(P_r(t)=r/[\pi(r^2+t^2)]\). For coefficients satisfying \(\sum n|c_n|^2<\infty\), Montgomery--Vaughan's mean-value theorem gives, on every interval \(I\) of length \(H\),
\[
\int_I\left|\sum c_n n^{-it}\right|^2dt
=H\sum|c_n|^2+O\!\left(\sum n|c_n|^2\right).
\tag{17}
\]
The error is independent of the interval's starting point, which only changes coefficient phases. It therefore remains valid after averaging translates against the probability kernel \(P_r\). Apply (17) to the two terms of (16); the combined error is bounded by a constant times \(\sum n a_n^2\).

This last sum is uniformly bounded for \(0<\varepsilon\le1\). Indeed \(\Lambda(n)^2\le\Lambda(n)\log n\) gives
\[
\sum n a_n^2\le A_\varepsilon^{-2}[-L'(1+2\varepsilon)]=O(1),
\tag{18}
\]
using the ordinary pole expansions \(A_\varepsilon=\varepsilon^{-1}+O(1)\) and \(-L'(1+2\varepsilon)=(4\varepsilon^2)^{-1}+O(1)\) near zero, and continuity on the remaining compact parameter interval. Equations (16)--(18) prove (6)--(7). All infinite-series passages satisfy the weighted square-summability hypothesis in (17); no global real-line square-integrability of \(L\) is assumed.

For (8), expand \(1-n^{-2q\varepsilon}=2q\varepsilon\log n+O_q(\varepsilon^2(\log n)^2)\) and \(n^{-2\varepsilon}=1+O(\varepsilon\log n)\), with bounds valid for \(\log n\ge0\). The remainders are summable against \(\Lambda(n)^2/n^2\). Combining with \(A_\varepsilon^{-2}=\varepsilon^2(1+O(\varepsilon))\) proves the assertion. The height mean is carried by the diagonal prime-power terms, while persistent peaks require coherent off-diagonal phases.

## Recurrence, controls, and the remaining arithmetic gap

For fixed \(\varepsilon,r\), (11) makes \(Q_\varepsilon(r,\cdot)\) uniformly almost periodic. If \(Q_\varepsilon(r,0)>\tau\), continuity supplies an interval above threshold and relative density of sufficiently accurate almost periods supplies translated intervals of the same positive width with bounded gaps. This gives positive lower uniform density, with no uniform lower bound as the parameters shrink. WI-457's exact pole-scale limit \(Q_\varepsilon(q\varepsilon,0)\to q/(1+q)^2\) proves the assertion following (5). The exponentially small upper density and positive fixed-parameter lower density are compatible; the gap bound for almost periods may grow arbitrarily rapidly.

This test changes the information available about the explicit source family: recurrent maxima are exponentially rare at the shallow packet scale, even though the exact mean is only cubic. It does not reopen WI-457's failure of uniform shallow detection. In the Kunik correspondence \(r=(1-\theta)d\), \(d\) is horizontal defect depth; neither Haar averaging nor Lebesgue averaging makes actual zero ordinates independent prime phases. Even a set of zero height density can contain every member of a prescribed discrete exceptional zero set. Thus (4) cannot upper-bound the number of off-line zeros, certify simplicity, or exclude one exceptional block.

The estimates apply to the fixed symbol and fixed \(\varepsilon,r\) while averaging height. They do not bound a height-adaptive supremum over all \(\varepsilon\), arbitrary translations aligning each symbol's pole with a chosen ordinate, or signed coefficient redesign. The finite-window bound (6) gives a cubic-scale mean with error \(O(H^{-1})\); substituting a growing-height/decreasing-\(\varepsilon\) diagonal into (5) without a convergence-rate theorem is invalid. The concentration estimate is deliberately not an optimal large-deviation law.

The decisive audit checks are the \(\sqrt r\) factor in each prime block (12), retention of all dependent prime powers within that block, the squared coordinate costs in (14), uniform phase approximation at fixed \(\varepsilon\), and the finite-interval error (18). These are analytic identities and inequalities, not numerical or formalized evidence.

## Prior art and mathematical delta

The probability mechanism is classical bounded differences: Colin McDiarmid, *On the method of bounded differences*, in **Surveys in Combinatorics, 1989**, London Mathematical Society Lecture Note Series 141, pp. 148--188, [DOI 10.1017/CBO9781107359949.008](https://doi.org/10.1017/CBO9781107359949.008). The martingale argument needed here is given above. The additional source-specific step is the Hilbert-valued Hankel block budget \(\sum b_p^2\le rB\); a scalar bound on the unprojected logarithmic derivative would lose this packet-scale factor.

Prime-torus value distributions of logarithmic derivatives are established prior art. Yasutaka Ihara, *On “M-Functions” Closely Related to the Distribution of L'/L-Values*, **Publications of RIMS 44** (2008), 893--954, [DOI 10.2977/PRIMS/1216238306](https://doi.org/10.2977/PRIMS/1216238306), especially §1.5 and its discussion of the vertical family, explicitly constructs the prime torus and relates logarithmic-derivative values to Bohr--Jessen theory. No new random Euler-product principle is claimed. Only the elementary absolutely convergent regime \(\Re s>1\) is used here.

The quantitative finite-window ingredient is H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **Journal of the London Mathematical Society** (2) 8 (1974), 73--82, Corollary 3, equation (1.11), [author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf). The pole input is the same classical input already anchored in WI-457.

The delta from WI-457 is a bound on the frequency of its recurrent peaks, with a separate finite-window interface and explicit noncommuting parameter limits. It is a derived specialization of classical concentration, torus averaging, and mean-value theory, not a new general theorem or a claim of literature priority. The missing zero-ordinate alignment estimate remains missing; no RH implication follows.
