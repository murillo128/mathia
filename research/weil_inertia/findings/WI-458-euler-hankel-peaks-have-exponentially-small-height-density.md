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

The density statements (4)--(5b) take the infinite-height limit at each fixed \(\varepsilon,r\). A quantitative finite-height replacement is available on a doubly exponential window scale. For fixed \(q>0\) and \(0<\tau<1\), put
\[
\mathcal F_\varepsilon(H)=\sup_{T\in\mathbb R}
\frac{|\{\gamma\in[T,T+H]:Q_\varepsilon(q\varepsilon,\gamma)\ge\tau\}|}{H}.
\]
There are constants \(c_{\rm fin},C_{\rm fin}>0\), depending only on \(q,\tau\), such that for sufficiently small \(\varepsilon>0\),
\[
\boxed{H\ge\exp[\exp(C_{\rm fin}/\varepsilon)]
\quad\Longrightarrow\quad
\mathcal F_\varepsilon(H)\le\exp[-\exp(c_{\rm fin}/\varepsilon)].}
\tag{5c}
\]
For a submaximum threshold \(0<\tau<q/(1+q)^2\), a constant \(b=b(q,\tau)>0\) also gives, for every \(H>0\),
\[
\boxed{\mathcal F_\varepsilon(H)\ge\min\{1,b\varepsilon/H\}.}
\tag{5d}
\]
Thus a proposed bound \(\mathcal F_\varepsilon(H)\le\exp[-\exp(c_0/\varepsilon)]\), with fixed \(c_0>0\), necessarily requires
\(H\ge b\varepsilon\exp[\exp(c_0/\varepsilon)]\).
The broad doubly exponential window scale is therefore sufficient and necessary for a uniform-in-starting-height upper bound of this strength. No matching constants, finite-window lower density law, or maximum recurrence-gap estimate is asserted.

A separate quantitative mean estimate, valid on every window and uniform in its starting height, is
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
\((\mu_\varepsilon(r)+C_0/H)/\tau\) for an absolute \(C_0\). Unlike (5c), this mean estimate needs no lower bound on the window length. Equation (5c) is an upper tail estimate, not a rate of convergence of the full height distribution to its torus law.

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

## Finite windows through tensor moments

Fix \(q>0\), \(0<\tau<1\), and \(r=q\varepsilon\). Choose the small constant \(a>0\) in (24) so \(S_y\le\sqrt\tau/4\) for \(y=e^{a/\varepsilon}\). There is then a fixed \(D>0\) such that
\[
V_y\le \overline V:=D e^{-a/\varepsilon}
\tag{29}
\]
for all sufficiently small \(\varepsilon\). Next choose a fixed \(K>a\) large enough, and put \(X=e^{K/\varepsilon}\). The coefficient tail over **all integers** \(n>X\) has the same tilt estimate as (25):
\[
A_\varepsilon^{-1}\sum_{n>X}\frac{\Lambda(n)}{n^{1+\varepsilon}}
\le X^{-\varepsilon/2}\frac{A_{\varepsilon/2}}{A_\varepsilon}
\le3e^{-K/2}\le\sqrt\tau/4.
\tag{30}
\]
This estimate is uniform in every phase and ordinate. Remove the small-prime blocks and this far coefficient tail, retaining the finite Hilbert-valued Dirichlet polynomial
\[
Z(\gamma)=\sum_{\substack{p>y,\ j\ge1\\p^j\le X}}
\frac{\log p}{A_\varepsilon p^{j(1+\varepsilon)}}
 h_{j\log p}e^{-ij\gamma\log p}.
\tag{31}
\]
The two discarded portions have total norm at most \(\sqrt\tau/2\). Therefore
\[
Q_\varepsilon(q\varepsilon,\gamma)\ge\tau
\quad\Longrightarrow\quad \|Z(\gamma)\|\ge v:=\sqrt\tau/2.
\tag{32}
\]
No truncation of the Hardy variable \(t\) is made: each \(h_{j\log p}\) remains its exact \(L^2\) vector.

Under prime-torus Haar measure, the truncated blocks are still independent across primes, with zero mean and coordinate sensitivity at most \(2b_p/A_\varepsilon\). If \(F=\|Z\|\), (13)--(14) imply
\[
\mathbb EF\le\sqrt{\overline V},\qquad
\Pr(F-\mathbb EF\ge u)\le e^{-u^2/(2\overline V)}.
\]
For each integer \(m\ge1\), integration of the latter tail gives
\(\mathbb E[(F-\mathbb EF)_+^{2m}]\le(2\overline V)^m m!\).
Minkowski and \(m!\le m^m\) consequently give
\[
\mathbb E\|Z\|^{2m}\le(9m\overline V)^m.
\tag{33}
\]
Dependent powers of a prime have never been randomized separately.

The finite-height transfer is quantitative because tensor powers retain integer Dirichlet frequencies. Write \(Z(\gamma)=\sum_{n\le X}u_n n^{-i\gamma}\), with Hilbert-space coefficients \(u_n\). In the Hilbert tensor product,
\[
Z(\gamma)^{\otimes m}=\sum_{n\le X^m}U_n n^{-i\gamma},
\qquad \|Z(\gamma)^{\otimes m}\|^2=\|Z(\gamma)\|^{2m}.
\tag{34}
\]
Unique factorization makes different integers different torus characters, so
\(\sum_n\|U_n\|^2=\mathbb E\|Z\|^{2m}\).
Apply the scalar Montgomery--Vaughan estimate (17) in an orthonormal basis of the finite span of the \(U_n\), and sum. Its absolute constant is independent of the dimension, \(m\), and coefficient phases. Hence, for an absolute \(C_{\rm MV}\),
\[
\frac1H\int_T^{T+H}\|Z(\gamma)\|^{2m}\,d\gamma
\le\left(1+\frac{C_{\rm MV}X^m}{H}\right)
\mathbb E\|Z\|^{2m}.
\tag{35}
\]
This step replaces qualitative equidistribution; it does not claim probabilistic independence on a finite height interval. Equations (32)--(35) yield the explicit interface
\[
\boxed{\mathcal F_\varepsilon(H)
\le\left(1+\frac{C_{\rm MV}X^m}{H}\right)
\left(\frac{9m\overline V}{v^2}\right)^m.}
\tag{36}
\]
Take
\[
m=\left\lfloor\frac{v^2}{36D}e^{a/\varepsilon}\right\rfloor.
\]
For sufficiently small \(\varepsilon\), \(m\ge2\), the last parenthesis in (36) is at most \(1/4\), and \(H\ge C_{\rm MV}X^m\) gives an upper bound \(2\cdot4^{-m}\le e^{-m}\). For example, after reducing \(\varepsilon\) further,
\[
m\ge e^{a/(2\varepsilon)},\qquad
\log(C_{\rm MV}X^m)\le e^{2a/\varepsilon}.
\]
Thus \(c_{\rm fin}=a/2\) and \(C_{\rm fin}=2a\) suffice in (5c). These constants are deliberately coarse and depend on the earlier fixed threshold choices.

## Why a uniform rare-peak bound needs long windows

Suppose \(\tau<q/(1+q)^2\), and let \(\Delta=\sqrt q/(1+q)-\sqrt\tau>0\). The pole-scale limit gives
\(\sqrt{Q_\varepsilon(q\varepsilon,0)}\ge\sqrt\tau+3\Delta/4\)
for sufficiently small \(\varepsilon\). From the translated vector representation (9) and the positive Euler coefficients,
\[
\left|\sqrt{Q_\varepsilon(r,\gamma)}-
\sqrt{Q_\varepsilon(r,\gamma')}\right|
\le |\gamma-\gamma'|\,
\frac{-L'(1+\varepsilon)}{A_\varepsilon}
\le\frac{2|\gamma-\gamma'|}{\varepsilon}.
\tag{37}
\]
The last inequality uses the simple pole expansion and is valid for sufficiently small \(\varepsilon\), uniformly in \(r\). Taking \(b=\Delta/8\) shows that the interval \([0,b\varepsilon]\) lies strictly above threshold, with a fixed positive gap. The fraction in the interval \([0,H]\) is consequently at least \(\min\{1,b\varepsilon/H\}\), proving (5d).

This lower obstruction also survives restriction to arbitrarily large starting heights at each fixed \(\varepsilon\): the almost periods in WI-457 transfer the whole above-threshold interval with its strict gap. It is not eliminated by discarding the neighborhood of height zero. It does not specify where those high intervals occur, bound their gaps, or associate them with zeta zeros. The necessary window scale concerns a supremum over interval placements, not a typical starting height.

## Recurrence, controls, and the remaining arithmetic gap

For fixed \(\varepsilon,r\), (11) makes \(Q_\varepsilon(r,\cdot)\) uniformly almost periodic. If \(Q_\varepsilon(r,0)>\tau\), continuity supplies an interval above threshold and relative density of sufficiently accurate almost periods supplies translated intervals of the same positive width with bounded gaps. This gives positive lower uniform density. The phase-box argument quantifies an infinite-height lower density at the pole scale. The tensor-moment estimate (5c) supplies a uniform finite-window upper bound, but neither argument gives a quantitative finite-window lower density or a bound on the largest gap between successive peaks. Its lower density tends to zero as \(\varepsilon\downarrow0\), consistently with (5a).

This test changes the information available about the explicit source family: recurrent maxima have doubly exponential rarity at the shallow packet scale, even though the exact mean is only cubic. It does not reopen WI-457's failure of uniform shallow detection. In the Kunik correspondence \(r=(1-\theta)d\), \(d\) is horizontal defect depth; neither Haar averaging nor Lebesgue averaging makes actual zero ordinates independent prime phases. Even a set of zero height density can contain every member of a prescribed discrete exceptional zero set. None of the density bounds can upper-bound the number of off-line zeros, certify simplicity, or exclude one exceptional block.

The estimates apply to the fixed symbol and fixed \(\varepsilon,r\) while averaging height. They do not bound a height-adaptive supremum over all \(\varepsilon\), arbitrary translations aligning each symbol's pole with a chosen ordinate, or signed coefficient redesign. The finite-window bound (6) gives a cubic-scale mean with error \(O(H^{-1})\); (5c) permits a simultaneous shrinking-scale/long-window limit only in its stated range. Substituting an unrestricted diagonal into (5a)--(5b) remains invalid. The general finite-window interface (36) keeps the length cost explicit. The lower bound requires a fixed strict gap below the limiting maximum; it asserts nothing at equality or for a threshold approaching that maximum with \(\varepsilon\). The concentration estimate is not an optimal large-deviation law.

The decisive audit checks are the \(\sqrt r\) factor in each prime block (12), retention of all dependent prime powers within that block, the squared coordinate costs in (14), the distinct deterministic and quadratic tail costs (22)--(24), the tail-uniform phase-box inclusion (25)--(27), uniform phase approximation at fixed \(\varepsilon\), the finite-interval error (18), the tensor-frequency length \(X^m\) in (34)--(36), and the peak-width lower bound (37). A single prime cannot create a fixed-threshold peak as \(\varepsilon\downarrow0\); charging its sensitivity to the whole large deviation is exactly the loss avoided by (20). These are analytic identities and inequalities, not numerical or formalized evidence.

## Prior art and mathematical delta

The probability mechanism is classical bounded differences: Colin McDiarmid, *On the method of bounded differences*, in **Surveys in Combinatorics, 1989**, London Mathematical Society Lecture Note Series 141, pp. 148--188, [DOI 10.1017/CBO9781107359949.008](https://doi.org/10.1017/CBO9781107359949.008). The martingale argument needed here is given above. The additional source-specific step is the Hilbert-valued Hankel block budget \(\sum b_p^2\le rB\); a scalar bound on the unprojected logarithmic derivative would lose this packet-scale factor.

Prime-torus value distributions of logarithmic derivatives are established prior art. Yasutaka Ihara, *On “M-Functions” Closely Related to the Distribution of L'/L-Values*, **Publications of RIMS 44** (2008), 893--954, [DOI 10.2977/PRIMS/1216238306](https://doi.org/10.2977/PRIMS/1216238306), especially §1.5 and its discussion of the vertical family, explicitly constructs the prime torus and relates logarithmic-derivative values to Bohr--Jessen theory. No new random Euler-product principle is claimed. Only the elementary absolutely convergent regime \(\Re s>1\) is used here.

The quantitative finite-window ingredient is H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **Journal of the London Mathematical Society** (2) 8 (1974), 73--82, Corollary 3, equation (1.11), [author-hosted paper](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf). Summing that scalar estimate over a finite orthonormal basis gives (35); the moment order enters through the polynomial length \(X^m\), without a dimension-dependent constant. The pole input is the same classical input already anchored in WI-457.

Doubly exponential tails of logarithmic-derivative Euler models are also established neighboring prior art. Youness Lamzouri, *The distribution of Euler-Kronecker constants of quadratic fields*, [arXiv:1410.1603](https://arxiv.org/abs/1410.1603), Theorem 1.2, proves sharp doubly exponential tails for a scalar quadratic-character model at \(s=1\); the discussion immediately preceding it also identifies the unit-circle model for vertical zeta logarithmic derivatives. That scalar theorem is not imported as a theorem about this Hilbert-valued, \(r=q\varepsilon\), normalized Hankel response. Equations (19)--(28) supply the needed specialization directly. No new double-exponential Euler-product phenomenon is claimed.

Effective random-model comparison by truncating Euler series and comparing high moments is established prior art too. Clayton James Lungstrum, *Discrepancy Bounds of the Logarithmic Derivative of the Riemann Zeta Function*, Ph.D. thesis, University of Rochester (2019), [institutional copy](https://hdl.handle.net/1802/35234), §2.3, studies scalar prime-polynomial moments for this purpose. The proof here retains the Hilbert-valued Hankel coefficients, groups all powers of a prime, and obtains a dimension-independent finite-window estimate by tensorization. It is a direct specialization of classical methods, not a new discrepancy principle or an imported scalar theorem about this response.

The delta from WI-457 is a bound on the frequency of its recurrent peaks, determining the doubly exponential density scale above and below for fixed submaximum thresholds. The finite-window strengthening (5c), (36), and (37) additionally identifies a sufficient and necessary broad window scale for a uniform rare-peak upper bound, with explicit control of the simultaneous parameter limit. This is stronger than the unsplit concentration estimate (5), while preserving the same claim identity. It is a derived specialization of classical concentration, torus averaging, and mean-value theory, not a new general theorem or a claim of literature priority. The missing zero-ordinate alignment estimate remains missing; no RH implication follows.
