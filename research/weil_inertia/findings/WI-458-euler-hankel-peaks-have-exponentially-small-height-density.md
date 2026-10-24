# WI-458 — Euler Hankel peaks have doubly exponentially small height density

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
Splitting off the small primes gives the stronger scale. Define
\[
d_*(E)=\liminf_{H\to\infty}\inf_{T\in\mathbb R}
\frac{|E\cap[T,T+H]|}{H}.
\]
For every fixed \(q,\tau>0\) there is \(c=c(q,\tau)>0\) such that, for all sufficiently small \(\varepsilon>0\),
\[
\boxed{d^*\{\gamma:Q_\varepsilon(q\varepsilon,\gamma)\ge\tau\}
\le \exp[-\exp(c/\varepsilon)].}
\tag{5a}
\]
If additionally \(0<\tau<q/(1+q)^2\), there is \(C=C(q,\tau)>c\) such that
\[
\boxed{\exp[-\exp(C/\varepsilon)]
\le d_*\{\gamma:Q_\varepsilon(q\varepsilon,\gamma)>\tau\}
\le d^*\{\gamma:Q_\varepsilon(q\varepsilon,\gamma)\ge\tau\}.}
\tag{5b}
\]
Thus the recurrent order-one peaks have doubly exponential rarity in \(1/\varepsilon\), with no claim of a sharp constant or an exact density asymptotic. This strengthens the same peak-frequency claim; (4) remains a useful bound at arbitrary fixed \(\varepsilon,r\).

The order of limits in (4)--(5b) is essential: the infinite-height density is taken at each fixed \(\varepsilon,r\), then \(\varepsilon\) tends to zero. A separate quantitative finite-window estimate, uniform in the window's starting height, is
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
\((\mu_\varepsilon(r)+C_0/H)/\tau\) for an absolute \(C_0\). The exponential and doubly exponential bounds have no asserted uniform finite-height convergence rate.

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

## Small-prime splitting and the doubly exponential upper bound

Keep all powers of each prime in its block. At a cutoff \(y\ge2\), write
\[
W=W_{\le y}+W_{>y},\qquad
S_y=A_\varepsilon^{-1}\sum_{p\le y}b_p,\qquad
V_y=A_\varepsilon^{-2}\sum_{p>y}b_p^2.
\tag{19}
\]
Then \(\|W_{\le y}\|/A_\varepsilon\le S_y\) deterministically, while
\(\mathbb E\|W_{>y}\|/A_\varepsilon\le\sqrt{V_y}\). Applying (14) only to the tail gives
\[
\Pr\{\|W\|/A_\varepsilon\ge\sqrt\tau\}
\le\exp\!\left[-\frac{(\sqrt\tau-S_y-\sqrt{V_y})_+^2}{2V_y}\right].
\tag{20}
\]
In particular the cost of changing a small-prime phase is no longer charged to a tail deviation that it cannot produce on its own.

Only the real pole estimate \(A_u\asymp u^{-1}\) as \(u\downarrow0\) is needed to bound the deterministic part. For \(y\) sufficiently large,
\[
\sum_{p\le y}\frac{\log p}{p}
\le e\sum_{p\le y}\frac{\log p}{p^{1+1/\log y}}
\le e A_{1/\log y}\ll\log y.
\tag{21}
\]
Using \(p/(p-1)^2\le4/p\) in (12) consequently yields
\[
S_y\ll A_\varepsilon^{-1}\sqrt r\,(\log y)^{3/2}.
\tag{22}
\]
For the quadratic tail budget, enlarging the prime sum to all integers is sufficient:
\[
V_y\ll A_\varepsilon^{-2}r
\sum_{n>y}\frac{(\log n)^3}{n^2}
\ll A_\varepsilon^{-2}r\frac{(1+\log y)^3}{y}.
\tag{23}
\]
The last bound follows by integral comparison, with the finitely many small values absorbed into an absolute constant.

Now set \(r=q\varepsilon\) and \(y=\exp(a/\varepsilon)\), where \(a>0\) is fixed and small. Equations (22)--(23) imply
\[
S_y\ll\sqrt q\,a^{3/2},\qquad
V_y\ll q(a+\varepsilon)^3\exp(-a/\varepsilon).
\tag{24}
\]
Choose \(a=a(q,\tau)\) so the first bound is at most \(\sqrt\tau/4\). For sufficiently small \(\varepsilon\), \(\sqrt{V_y}\le\sqrt\tau/4\) as well. Equation (20) is then at most
\(\exp[-\tau/(8V_y)]\), which is at most
\(\exp[-\exp(a/(2\varepsilon))]\) after reducing \(\varepsilon\) further. The deterministic height-transfer argument following (15) proves (5a), with \(c=a/2\). No prime number theorem or estimate at zero ordinates is used.

## A matching broad lower scale from finite phase boxes

Suppose \(\tau<q/(1+q)^2\), and put
\[
m_q=\frac{\sqrt q}{1+q},\qquad \Delta=m_q-\sqrt\tau>0.
\]
The WI-457 pole limit gives
\(\|W(1)\|/A_\varepsilon\ge\sqrt\tau+3\Delta/4\) for sufficiently small \(\varepsilon\), where \(1\) means all prime phases are one. Choose a large fixed \(K>0\) and a small fixed \(0<\eta<1\), and now use the different cutoff \(y=\exp(K/\varepsilon)\).

The normalized coefficient mass beyond this cutoff obeys the exact tilt bound
\[
R_y:=A_\varepsilon^{-1}
\sum_{p>y}\sum_{k\ge1}\frac{\log p}{p^{k(1+\varepsilon)}}
\le y^{-\varepsilon/2}\frac{A_{\varepsilon/2}}{A_\varepsilon}
\le3e^{-K/2}
\tag{25}
\]
for sufficiently small \(\varepsilon\). Here \(p^k>y\), and the ratio of the two pole normalizations tends to two. This bounds every possible tail phase choice, not just its average.

The phase sensitivity of the retained blocks is uniformly bounded too. Indeed,
\[
\sum_{p,k\ge1}\frac{k\log p}{p^{k(1+\varepsilon)}}
\le A_\varepsilon+D,\qquad
D=\sum_p\frac{\log p}{(p-1)^2}<\infty,
\tag{26}
\]
because \(\sum_{k\ge2}(k-1)p^{-k}=1/(p-1)^2\). If \(|\arg z_p|<\eta\) for every \(p\le y\), then \(|z_p^k-1|\le k\eta\); using \(\|h_\omega\|\le1\), (25)--(26) give
\[
\frac{\|W(z)-W(1)\|}{A_\varepsilon}
\le2\eta+6e^{-K/2}.
\tag{27}
\]
Choose \(\eta,K\) so the right side is at most \(\Delta/2\). The whole finite phase box then lies in \(Q_\varepsilon(q\varepsilon,\gamma)>\tau\), regardless of the remaining prime phases.

If \(\pi(y)\) denotes the number of primes at most \(y\), the box has Haar measure
\[
(\eta/\pi)^{\pi(y)}
\ge\exp[-\log(\pi/\eta)e^{K/\varepsilon}]
\ge\exp[-\exp((K+1)/\varepsilon)]
\tag{28}
\]
for sufficiently small \(\varepsilon\); only \(\pi(y)\le y\) was used. At each fixed \(\varepsilon\) this is a finite-dimensional box with Haar-null boundary. Uniform-in-starting-height equidistribution, obtained by continuous upper and lower approximation of its indicator, makes its lower uniform height density equal to its Haar measure. Its pointwise containment in the strict superlevel set proves (5b). Enlarging \(C\) if necessary ensures \(C>c\).

The two cutoffs serve different purposes: \(a\) is small for the upper bound so the retained part cannot reach threshold; \(K\) is large for the lower bound so arbitrary tail phases cannot destroy a near-maximum. No equality of the inner exponential constants follows.

## Recurrence, controls, and the remaining arithmetic gap

For fixed \(\varepsilon,r\), (11) makes \(Q_\varepsilon(r,\cdot)\) uniformly almost periodic. If \(Q_\varepsilon(r,0)>\tau\), continuity supplies an interval above threshold and relative density of sufficiently accurate almost periods supplies translated intervals of the same positive width with bounded gaps. This gives positive lower uniform density. The phase-box argument quantifies a lower density at the pole scale, but supplies neither a useful finite-height convergence rate nor a bound on the largest gap between successive peaks. Its lower density tends to zero as \(\varepsilon\downarrow0\), consistently with (5a).

This test changes the information available about the explicit source family: recurrent maxima have doubly exponential rarity at the shallow packet scale, even though the exact mean is only cubic. It does not reopen WI-457's failure of uniform shallow detection. In the Kunik correspondence \(r=(1-\theta)d\), \(d\) is horizontal defect depth; neither Haar averaging nor Lebesgue averaging makes actual zero ordinates independent prime phases. Even a set of zero height density can contain every member of a prescribed discrete exceptional zero set. None of the density bounds can upper-bound the number of off-line zeros, certify simplicity, or exclude one exceptional block.

The estimates apply to the fixed symbol and fixed \(\varepsilon,r\) while averaging height. They do not bound a height-adaptive supremum over all \(\varepsilon\), arbitrary translations aligning each symbol's pole with a chosen ordinate, or signed coefficient redesign. The finite-window bound (6) gives a cubic-scale mean with error \(O(H^{-1})\); substituting a growing-height/decreasing-\(\varepsilon\) diagonal into (5a)--(5b) without a convergence-rate theorem is invalid. The lower bound requires a fixed strict gap below the limiting maximum; it asserts nothing at equality or for a threshold approaching that maximum with \(\varepsilon\). The concentration estimate is not an optimal large-deviation law.

The decisive audit checks are the \(\sqrt r\) factor in each prime block (12), retention of all dependent prime powers within that block, the squared coordinate costs in (14), the distinct deterministic and quadratic tail costs (22)--(24), the tail-uniform phase-box inclusion (25)--(27), uniform phase approximation at fixed \(\varepsilon\), and the finite-interval error (18). A single prime cannot create a fixed-threshold peak as \(\varepsilon\downarrow0\); charging its sensitivity to the whole large deviation is exactly the loss avoided by (20). These are analytic identities and inequalities, not numerical or formalized evidence.

## Prior art and mathematical delta

The probability mechanism is classical bounded differences: Colin McDiarmid, *On the method of bounded differences*, in **Surveys in Combinatorics, 1989**, London Mathematical Society Lecture Note Series 141, pp. 148--188, [DOI 10.1017/CBO9781107359949.008](https://doi.org/10.1017/CBO9781107359949.008). The martingale argument needed here is given above. The additional source-specific step is the Hilbert-valued Hankel block budget \(\sum b_p^2\le rB\); a scalar bound on the unprojected logarithmic derivative would lose this packet-scale factor.

Prime-torus value distributions of logarithmic derivatives are established prior art. Yasutaka Ihara, *On “M-Functions” Closely Related to the Distribution of L'/L-Values*, **Publications of RIMS 44** (2008), 893--954, [DOI 10.2977/PRIMS/1216238306](https://doi.org/10.2977/PRIMS/1216238306), especially §1.5 and its discussion of the vertical family, explicitly constructs the prime torus and relates logarithmic-derivative values to Bohr--Jessen theory. No new random Euler-product principle is claimed. Only the elementary absolutely convergent regime \(\Re s>1\) is used here.

The quantitative finite-window ingredient is H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **Journal of the London Mathematical Society** (2) 8 (1974), 73--82, Corollary 3, equation (1.11), [author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf). The pole input is the same classical input already anchored in WI-457.

Doubly exponential tails of logarithmic-derivative Euler models are also established neighboring prior art. Youness Lamzouri, *The distribution of Euler-Kronecker constants of quadratic fields*, [arXiv:1410.1603](https://arxiv.org/abs/1410.1603), Theorem 1.2, proves sharp doubly exponential tails for a scalar quadratic-character model at \(s=1\); the discussion immediately preceding it also identifies the unit-circle model for vertical zeta logarithmic derivatives. That scalar theorem is not imported as a theorem about this Hilbert-valued, \(r=q\varepsilon\), normalized Hankel response. Equations (19)--(28) supply the needed specialization directly. No new double-exponential Euler-product phenomenon is claimed.

The delta from WI-457 is a bound on the frequency of its recurrent peaks, now determining the doubly exponential scale above and below for fixed submaximum thresholds, with a separate finite-window interface and explicit noncommuting parameter limits. This is stronger than the unsplit concentration estimate (5), while preserving the same claim identity. It is a derived specialization of classical concentration, torus averaging, and mean-value theory, not a new general theorem or a claim of literature priority. The missing zero-ordinate alignment estimate remains missing; no RH implication follows.
