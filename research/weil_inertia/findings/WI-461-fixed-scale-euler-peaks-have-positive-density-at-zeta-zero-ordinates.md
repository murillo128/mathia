# WI-461 — Euler peaks meet zeta-zero ordinates at fixed and controlled shrinking scales

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-EQUIDISTRIBUTION + SOURCE-FAMILY-BOUNDARY + NO-NOVELTY-CLAIM + NON-RH

**Local dependencies:** [WI-457](WI-457-normalized-euler-hankel-symbols-have-local-blindness-and-recurrent-peaks.md), for the response, its global maximum and pole limit; [WI-458](WI-458-euler-hankel-peaks-have-exponentially-small-height-density.md), for the tail-uniform prime phase box; [WI-459](WI-459-safe-line-optimization-preserves-double-exponential-euler-peak-rarity.md), for the optimized maximum; [WI-460](WI-460-adaptive-euler-peaks-remain-rare-at-zeta-zero-ordinates.md), for the upper bound after simultaneous safe-line and width selection.

## Claim: rarity does not imply avoidance by the divisor

Use the normalized Euler symbols and Hardy kernels
\[
L(s)=-\zeta'(s)/\zeta(s),\quad A_\varepsilon=L(1+\varepsilon),\quad
\varphi_\varepsilon(t)=L(1+\varepsilon+it)/A_\varepsilon,
\]
\[
k_{r,\gamma}(t)=\frac{\sqrt{r/\pi}}{r-i(t-\gamma)},\qquad
Q_\varepsilon(r,\gamma)=\|P_-(\varphi_\varepsilon k_{r,\gamma})\|_2^2,
\quad \varepsilon,r>0.
\tag{1}
\]
The Fourier phase is \(e^{-it\xi}\). Let \(\Gamma\) be the positive ordinates of **all** nontrivial zeta zeros, and let \(N(T)\) count those with ordinate at most \(T\). Count each zero with its multiplicity in \(N\) and every sum. Different real parts at the same ordinate contribute separately. Define
\[
D_T=N(2T)-N(T),\qquad
M_r(t)=\sup_{\varepsilon>0}Q_\varepsilon(r,t),\qquad
\mathcal M_R(t)=\sup_{0<r\le R}M_r(t).
\]

For each fixed \(0<\tau<1/4\), there are \(0<c_\tau<C_\tau\) and \(R_\tau>0\) such that, for every **fixed** \(0<R<R_\tau\),
\[
\boxed{
\begin{aligned}
\exp[-\exp(C_\tau/R)]
&\le \liminf_{T\to\infty}\frac1{D_T}
 \sum_{T<\gamma\le2T}\mathbf1_{\{Q_R(R,\gamma)>\tau\}}\\
&\le \liminf_{T\to\infty}\frac1{D_T}
 \sum_{T<\gamma\le2T}\mathbf1_{\{\mathcal M_R(\gamma)\ge\tau\}}\\
&\le \limsup_{T\to\infty}\frac1{D_T}
 \sum_{T<\gamma\le2T}\mathbf1_{\{\mathcal M_R(\gamma)\ge\tau\}}
\le \exp[-\exp(c_\tau/R)].
\end{aligned}}
\tag{2}
\]
Thus at any fixed sufficiently small scale, peaks occur at a positive, very small asymptotic lower fraction of actual zero ordinates. Safe-line or width adaptation is unnecessary for the lower bound.

There is also an exact range statement: for every fixed \(\varepsilon,r>0\) and every finite \(B\ge0\),
\[
\boxed{\sup_{\gamma\in\Gamma,\ \gamma>B}Q_\varepsilon(r,\gamma)
=Q_\varepsilon(r,0).}
\tag{3}
\]
Consequently
\[
\sup_{\gamma\in\Gamma,\ \gamma>B}M_r(\gamma)=M_r(0),
\qquad
\lim_{r\downarrow0}\sup_{\gamma\in\Gamma,\ \gamma>B(r)}M_r(\gamma)=\frac14
\tag{4}
\]
for any finite nonnegative cutoff \(B(r)\). These are suprema, not assertions that a maximum is attained at a zero.

There is a quantitative replacement for the fixed-scale lower limit. After enlarging \(C_\tau\) and decreasing \(R_\tau\), there is \(H_\tau>C_\tau\) such that, uniformly in \(R,T\),
\[
\boxed{\begin{gathered}
0<R<R_\tau,\qquad
T\ge\exp\!\big(\exp(\exp(H_\tau/R))\big)
\\[2pt]\Longrightarrow\qquad
\frac1{D_T}\sum_{T<\gamma\le2T}
\mathbf1_{\{Q_R(R,\gamma)>\tau\}}
\ge\exp[-\exp(C_\tau/R)].
\end{gathered}}
\tag{4a}
\]
In particular this applies to every shrinking function \(R(T)\) with
\(R(T)\ge H_\tau/\log\log\log T\) eventually. The triple-exponential height is a sufficient cost, not a sharp recurrence scale; the constants are not numerically evaluated.

None of (2)--(4a) restricts the real parts of the responsive zeros. They do not show that any off-line zero exists or responds, nor that any responsive zero is simple. They are fully compatible with RH. The lower bound in (2) does **not** apply with an arbitrary shrinking \(R=R(T)\); (4a) supplies a specific sufficient range instead of exchanging limits.

For every fixed \(\varepsilon,r>0\), the prime-torus response law
\(\mu_{\varepsilon,r}=(\mathscr Q_{\varepsilon,r})_*m\), defined by (7), is
**absolutely continuous with respect to Lebesgue measure**. In particular its
distribution function \(F_{\varepsilon,r}(x)=\mu_{\varepsilon,r}((-\infty,x])\)
is continuous, and the zero-sampled distribution satisfies
\[
\boxed{\sup_{x\in\mathbb R}\left|
\frac1{D_T}\sum_{T<\gamma\le2T}
\mathbf1_{\{Q_\varepsilon(r,\gamma)\le x\}}
-F_{\varepsilon,r}(x)\right|\longrightarrow0.}
\tag{4b}
\]
Thus every fixed threshold has an exact limiting frequency, with the same
limit for strict and non-strict inequalities. The uniformity in (4b) is over
thresholds, not over the two fixed response parameters, and supplies no rate.

## Classical arithmetic input and the finite-prime sampling law

The input is the unconditional equidistribution of \(\alpha\gamma\) modulo one for every fixed real \(\alpha\ne0\), with all zeros counted with multiplicity. In character form,
\[
\frac1{N(T)}\sum_{0<\gamma\le T}e^{i\omega\gamma}\longrightarrow0
\quad\text{for every fixed }\omega\ne0.
\tag{5}
\]
This is the classical Elliott--Hlawka conclusion discussed in Ford--Zaharescu, §1, and stated in Ford--Soundararajan--Zaharescu, equation (1.1). The unconditional assertion must not be confused with the sharper RH-conditional discrepancy bounds or conjectured lower-order formulas in those papers.

For a fixed finite set of primes \(P\), put
\[
z_P(t)=(e^{-it\log p})_{p\in P}\in\mathbb T^P,
\qquad \mathbb T=\{z\in\mathbb C:|z|=1\}.
\]
If \((j_p)_{p\in P}\) is a nonzero integer vector, unique prime factorization gives
\(\sum_{p\in P}j_p\log p\ne0\). Applying (5) to this frequency shows that every nontrivial character of \(z_P(\gamma)\) has limiting mean zero. Finite Fourier approximation therefore proves convergence to product Haar measure for all continuous functions on \(\mathbb T^P\), and for finite phase boxes whose boundaries have Haar measure zero.

The same conclusion holds on \((T,2T]\): subtract the two cumulative sums and use \(N(2T)/D_T\to2\), \(N(T)/D_T\to1\). In particular, for fixed \(0<\eta<\pi\),
\[
\frac1{D_T}\sum_{T<\gamma\le2T}
\mathbf1_{\{|\arg z_p(\gamma)|<\eta\ \forall p\in P\}}
\longrightarrow (\eta/\pi)^{|P|}.
\tag{6}
\]
This is joint equidistribution deduced using every mixed character. Separate equidistribution of the individual prime phases alone would not establish (6). Powers of the same prime remain powers of one coordinate, never independent coordinates.

## The fixed-parameter response has its prime-torus law at zeros

For \(\omega>0\) define \(h_\omega=P_-(e^{-i\omega t}k_{r,0})\), so \(\|h_\omega\|_2\le1\). On the infinite product prime torus, with product Haar probability \(m\), set
\[
V_{\varepsilon,r}(z)=A_\varepsilon^{-1}
\sum_p\sum_{k\ge1}\frac{\log p}{p^{k(1+\varepsilon)}}z_p^k h_{k\log p},
\qquad \mathscr Q_{\varepsilon,r}(z)=\|V_{\varepsilon,r}(z)\|_2^2.
\tag{7}
\]
The sum of coefficient norms is at most one. Hence finite truncations converge uniformly in every phase choice, and \(\mathscr Q_{\varepsilon,r}\) is continuous with values in \([0,1]\). Translation of (1) gives
\(Q_\varepsilon(r,t)=\mathscr Q_{\varepsilon,r}(z(t))\).

For every continuous \(F:[0,1]\to\mathbb R\), finite truncation, (6)'s continuous-function version, and uniform continuity of \(F\) prove
\[
\boxed{\lim_{T\to\infty}\frac1{D_T}
\sum_{T<\gamma\le2T}F(Q_\varepsilon(r,\gamma))
=\int F(\mathscr Q_{\varepsilon,r}(z))\,dm(z).}
\tag{8}
\]
The truncation is fixed before taking \(T\to\infty\), then removed. The same torus law governs continuous-height averages, by finite-prime Kronecker equidistribution and the identical uniform truncation. Thus (8) is a leading-order sampling law for this fixed observable, not a postulate of random prime phases at selected zeros.

Weak convergence alone would not give equality for every threshold indicator.
For this coherent response the following two-prime argument removes that
obstruction. The quantitative phase-box argument later in the finding still
uses its own explicit errors; qualitative absolute continuity cannot replace
them.

## Two prime phases give an absolutely continuous response law

Fix \(\varepsilon,r>0\) throughout. For a prime \(p\) and integer \(k\ge1\), put
\[
a_{p,k}=\frac{\log p}{A_\varepsilon p^{k(1+\varepsilon)}},
\qquad
X_p(\theta)=\sum_{k\ge1}a_{p,k}e^{ik\theta}h_{k\log p}.
\tag{8a}
\]
Freeze all prime phases except those of two distinct primes \(p,q\), and
denote their remaining, uniformly convergent vector sum by \(W\). The
conditional response is the real-valued function
\[
G_W(\theta,\psi)=\|W+X_p(\theta)+X_q(\psi)\|_2^2.
\tag{8b}
\]
It is real analytic on the two-dimensional torus for **every** frozen tail.
Indeed, the two vector series have geometrically decreasing coefficients;
their norm-square Fourier expansions converge on each smaller complex strip
\[
|\Im\theta|<(1+\varepsilon)\log p,\qquad
|\Im\psi|<(1+\varepsilon)\log q.
\]
Here the norm-square expansion is extended using both positive and negative
Fourier powers, rather than treating a squared norm as a holomorphic norm.
The tail \(W\) is a fixed bounded vector and does not affect this convergence.

The Hardy-tone Gram matrix, obtained by the same projection calculation as
WI-457 (7)--(8), is
\[
\langle h_\omega,h_\nu\rangle
=e^{-r|\omega-\nu|}-e^{-r(\omega+\nu)}
\qquad(\omega,\nu>0).
\tag{8c}
\]
Consequently the coefficient of \(e^{i(\theta-\psi)}\) in (8b) is exactly
\[
c_{p,q}=a_{p,1}a_{q,1}
\left(e^{-r|\log(p/q)|}-(pq)^{-r}\right)>0.
\tag{8d}
\]
Only the \(p^1,q^1\) cross term contributes to that coefficient. Terms involving
\(W\) depend on at most one of the two phases, and higher prime powers have
different mixed exponents. Thus no choice of the other prime phases can cancel
(8d). In particular, \(\partial_\theta G_W\) is a nonzero real-analytic
function for every \(W\).

The classical real-analytic zero-set theorem implies that
\(\{\partial_\theta G_W=0\}\) has two-dimensional Haar measure zero.
On its complement the map
\[
(\theta,\psi)\longmapsto(G_W(\theta,\psi),\psi)
\]
has nonzero Jacobian. The inverse function theorem covers this complement by
countably many coordinate neighborhoods on which this map is a \(C^1\)
diffeomorphism. For any Lebesgue-null Borel set \(E\subset\mathbb R\), the set
\(E\times\mathbb R\) has planar measure zero. Change of variables on these
neighborhoods, together with the null critical set, therefore gives
\[
m_{\mathbb T^2}\{G_W\in E\}=0.
\tag{8e}
\]
Local coordinate charts handle the torus endpoints. Integrating (8e) over
all remaining prime phases by Fubini proves
\(\mu_{\varepsilon,r}(E)=0\). This is absolute continuity, not merely absence
of an atom at a chosen threshold; no probability law for selected zeros has
been assumed.

Equation (8) now implies convergence of the zero-sampled distribution function
at every real \(x\). Monotonicity upgrades it to (4b): on the compact response
range \([0,1]\), choose a finite mesh on which increments of the continuous
limit distribution function are arbitrarily small, apply pointwise
convergence at mesh points, and bracket every intermediate threshold.
The identical argument applies to continuous-height averages, so for every
fixed real \(\tau\),
\[
\begin{aligned}
\lim_{T\to\infty}\frac1{D_T}\sum_{T<\gamma\le2T}
 \mathbf1_{\{Q_\varepsilon(r,\gamma)>\tau\}}
&=\mu_{\varepsilon,r}((\tau,\infty))\\
&=\lim_{T\to\infty}\frac1T\int_T^{2T}
 \mathbf1_{\{Q_\varepsilon(r,t)>\tau\}}\,dt .
\end{aligned}
\tag{8f}
\]
Both strict inequalities may be replaced by non-strict ones.

Coherence is essential to this proof. A single tone has phase-independent
squared norm; replacing the full response by its diagonal prime-power energy
also gives a constant and hence an atomic law. The actual cross coefficient
(8d) prevents that degeneration for fixed positive parameters. It does not
provide uniform smoothing as parameters shrink: for each fixed \(\kappa>0\),
WI-458 (8) gives
\(\int x\,d\mu_{\varepsilon,\kappa\varepsilon}(x)=O_\kappa(\varepsilon^3)\).
Since the responses are nonnegative, these absolutely continuous laws
converge weakly to the point mass at zero as \(\varepsilon\downarrow0\).
There is no contradiction and no parameter-uniform density bound here.

## A phase box forces responsive zeros

Fix \(\tau\in(0,1/4)\), put \(\Delta=1/2-\sqrt\tau>0\), and take \(\varepsilon=r=R\). The pole limit in WI-457 gives
\[
\|V_{R,R}(1)\|_2\ge\sqrt\tau+3\Delta/4
\tag{9}
\]
for sufficiently small \(R\). Retain primes \(p\le y=\exp(K/R)\), with \(K\) a large fixed constant depending on \(\tau\). The normalized coefficient tail satisfies
\[
A_R^{-1}\sum_{p>y,k\ge1}\frac{\log p}{p^{k(1+R)}}
\le y^{-R/2}\frac{A_{R/2}}{A_R}\le3e^{-K/2}.
\tag{10}
\]
Here \(p^k>y\), and \(A_{R/2}/A_R\to2\). Also
\[
\sum_{p,k\ge1}\frac{k\log p}{p^{k(1+R)}}
\le A_R+D,\qquad
D=\sum_p\frac{\log p}{(p-1)^2}<\infty.
\tag{11}
\]
If \(|\arg z_p|<\eta\) for all \(p\le y\), then \(|z_p^k-1|\le k\eta\). Equations (10)--(11) and \(\|h_\omega\|_2\le1\) give, for small \(R\),
\[
\|V_{R,R}(z)-V_{R,R}(1)\|_2\le2\eta+6e^{-K/2}.
\tag{12}
\]
Choose \(\eta>0\) small and \(K\) large so this is at most \(\Delta/2\). The finite phase box lies in \(\mathscr Q_{R,R}>\tau\) for **every** choice of tail phases. This reconstructs the WI-458 box without assuming that the tail is typical.

At each fixed \(R\), equation (6) now gives a zero-sampled lower proportion at least
\[
(\eta/\pi)^{\pi(y)}
\ge\exp[-\log(\pi/\eta)e^{K/R}]
\ge\exp[-\exp(C_\tau/R)]
\tag{13}
\]
for a larger \(C_\tau\). Only \(\pi(y)\le y\) is used. The upper bound in (2) is WI-460's simultaneous-selection upper bound at the same fixed threshold; taking \(C_\tau>c_\tau\) is harmless.

For (3), use arbitrary fixed \(\varepsilon,r>0\). Uniform convergence in (7) lets a sufficiently large finite phase box make \(V_{\varepsilon,r}(z)\) arbitrarily close to \(V_{\varepsilon,r}(1)\), regardless of the tail. Equation (6) puts a positive limiting fraction of zeros in each such box, hence infinitely many beyond any finite \(B\). This gives the lower bound for the supremum in (3). The reverse bound is WI-457's pointwise inequality \(Q_\varepsilon(r,t)\le Q_\varepsilon(r,0)\). Interchanging two suprema proves the first equality in (4); WI-459's \(M_r(0)\to1/4\) proves its limit, including a finite cutoff depending on \(r\).

## A dimension-explicit phase-box estimate

The quantitative input is Ford--Zaharescu's uniform Landau formula and Selberg density bound (their Lemmas 1--2). Write \(\ell=\log T\). For every \(B\ge1\) with \(B\le\ell/8\), and every nonzero real \(\omega\) satisfying
\[
e^{-B}\le|\omega|\le B,
\]
they imply the uniform dyadic character estimate
\[
\left|\frac1{D_T}\sum_{T<\gamma\le2T}e^{i\omega\gamma}\right|
\le C\left(\frac1\ell+\frac{B^2}{\ell^2}
                  +\frac{e^B\ell}{T}\right)=:\mathcal E(T,B).
\tag{14}
\]
Here and below absolute constants do not depend on the number of primes or the mixed character. Negative frequencies follow by conjugation. The very small lower frequency cutoff is essential.

To verify (14) without a hidden fixed-frequency constant, take \(x=e^\omega>1\). The Landau formula at height \(U\) has main term of modulus at most \(C U\Lambda(n_x)\), where \(n_x\) is the nearest prime power to \(x\), and error
\(O(x\log^2(2xU)+\log(2U)/\log x)\).
After multiplication by \(x^{-1/2}\), the main term is \(O(U)\): one has \(n_x\le2x\), so \(\Lambda(n_x)/\sqrt x\) is bounded. This also covers exact prime-power resonance; no separation from prime powers is assumed.

The conversion from \(x^{\rho-1/2}\) to \(x^{i\gamma}\) must be unconditional and uniform near \(x=1\). Pair \(\beta+i\gamma\) with \(1-\beta+i\gamma\), preserving multiplicities. If \(u=\beta-1/2>0\), their difference in modulus is bounded by \(2(\cosh(\omega u)-1)\). Selberg's bound gives
\[
N_+(u,U):=\#\{\rho:0<\gamma\le U,\ \beta>1/2+u\}
\ll U\log U\,e^{-u\log U/4}.
\]
Layer-cake integration, \(\sinh v\le ve^v\), and \(\omega\le\log U/8\) therefore yield
\[
\begin{aligned}
\left|\sum_{0<\gamma\le U}
       (x^{i\gamma}-x^{\rho-1/2})\right|
&\le 2\int_0^{1/2}\omega\sinh(\omega u)N_+(u,U)\,du\\
&\ll U\log U\,\omega^2
       \int_0^\infty u e^{-u\log U/8}\,du
\ll\frac{U\omega^2}{\log U}.
\end{aligned}
\tag{15}
\]
Critical-line zeros contribute zero to this difference. This direct integration retains the factor \(\omega^2\) even for an exponentially small frequency.
Apply these bounds at \(U=2T,T\), subtract, and divide by \(D_T\asymp T\ell\). Since \(x^{1/2}\le e^{B/2}\), \(1/\omega\le e^B\), and \(\log(2xU)\ll\ell\), the resulting errors are bounded by (14).

Now fix the phase aperture \(\eta\) from (12). On \([-\pi,\pi]\), periodically extended, use the tent
\[
f(\theta)=(1-|\theta|/\eta)_+,
\qquad b=\widehat f(0)=\frac{\eta}{2\pi}\in(0,1).
\]
Its Fourier coefficients, normalized by \(d\theta/(2\pi)\), are
\[
\widehat f(j)=\frac{1-\cos(j\eta)}{\pi\eta j^2}\ge0
\quad(j\ne0),\qquad
\sum_{j\in\mathbb Z}\widehat f(j)=f(0)=1.
\tag{16}
\]
For \(f_J=\sum_{|j|\le J}\widehat f(j)e^{ij\theta}\),
\[
\|f-f_J\|_\infty\le\frac{C_\eta}{J},\qquad
|f_J|\le1,\qquad C_\eta=\frac4{\pi\eta}.
\tag{17}
\]
Although \(f_J\) need not be nonnegative, its absolute value and coefficient sum have the displayed bounds; no positivity of the truncated function is used.

For primes \(p\le y\), let \(d=\pi(y)\) and
\[
g(z)=\prod_{p\le y}f(\arg z_p),\qquad
g_J(z)=\prod_{p\le y}f_J(\arg z_p).
\]
Then \(0\le g\le\mathbf1_{\{|\arg z_p|<\eta\ \forall p\le y\}}\),
\(\|g-g_J\|_\infty\le C_\eta d/J\), and the constant coefficient of \(g_J\) is \(b^d\). Its nonnegative Fourier coefficients have total sum at most one. Every nonconstant character evaluated at \(z_p(t)=e^{-it\log p}\) has frequency
\(\omega=-\sum_{p\le y}j_p\log p\), with \(|j_p|\le J\).
Put
\[
B=\max\left\{1,J\sum_{p\le y}\log p\right\}.
\]
Unique factorization gives \(\omega\ne0\). More quantitatively, \(e^{|\omega|}=a/c>1\) for unequal positive integers \(a,c\le e^B\); hence
\[
|\omega|=\log(a/c)\ge(a-c)/a\ge e^{-B}.
\tag{18}
\]
This elementary rational separation handles all mixed frequencies, including near cancellation between large numerator and denominator.

Applying (14) to the finite Fourier expansion gives the explicit box lower bound
\[
\frac1{D_T}\sum_{T<\gamma\le2T}
\mathbf1_{\{|\arg z_p(\gamma)|<\eta\ \forall p\le y\}}
\ge b^d-\frac{C_\eta d}{J}-\mathcal E(T,B),
\qquad B\le\tfrac18\log T.
\tag{19}
\]
There is no factor counting the number of characters: their coefficient mass is at most one. Equation (19), rather than a fixed-dimensional asymptotic with unspecified constants, is the interface used below.

## Paying for a growing prime box

Take \(y=\exp(K/R)\), with the fixed \(K=K(\tau)\) from (12), and choose
\[
J=\left\lceil4C_\eta d\,b^{-d}\right\rceil.
\tag{20}
\]
Then \(C_\eta d/J\le b^d/4\). The elementary bounds \(d\le y\) and \(\sum_{p\le y}\log p\le y\log y\) show that, for a constant \(C_1=C_1(\eta)\) and large \(y\),
\[
B\le\exp(C_1y),\qquad b^d\ge\exp[-y\log(1/b)].
\tag{21}
\]
Choose \(C_2\) large enough depending only on \(\eta\). If
\[
\ell=\log T\ge\exp(C_2y),
\tag{22}
\]
then \(B\le\ell/8\) and \(\mathcal E(T,B)\le b^d/4\). Indeed the first two errors in (14) are at most constants times \(e^{-C_2y}\) and \(e^{-2(C_2-C_1)y}\); taking \(C_2>C_1+\log(1/b)+2\) makes both negligible compared with \(b^d\). The remaining term is \(e^B\ell e^{-\ell}\), smaller still throughout (22). Fixed multiplicative constants are absorbed by taking \(R\) sufficiently small.

Thus (19) is at least \(b^d/2\). Every counted ordinate is responsive by the tail-uniform inclusion (9)--(12), independently of all prime phases beyond \(y\). Enlarging \(C_\tau>K\) gives
\[
b^d/2\ge\exp[-\exp(C_\tau/R)].
\]
Finally choose \(H_\tau>C_\tau\). For all sufficiently small \(R\), the height assumption in (4a) implies (22), since
\(\exp(H_\tau/R)\ge C_2\exp(K/R)\).
This proves (4a) with every dimension, truncation and small-frequency cost retained. The method uses neither independent phases at zeros nor an RH-conditional discrepancy theorem.

## Consequence and limits of the conclusion

WI-460 proves upper rarity and explicitly leaves peak occurrence at zeros undecided. Classical fixed-frequency equidistribution supplies that missing qualitative arithmetic input: actual zero ordinates sample the full fixed-parameter response range and meet every robust near-maximum phase box. Their positive lower fraction has the same broad double-exponential scale as the established upper bound.

This resolves **fixed-scale overlap with the full divisor** and gives a sufficient quantitative range for shrinking-scale overlap. It does not resolve alignment with a hypothetical exceptional subpopulation. The relevant distinctions are:

- All zeros and multiplicities enter (5)--(8). Restricting to off-line zeros, simple zeros, or any other selected subpopulation requires a new sampling theorem. In particular, the result supplies no lower bound for the response at every off-line zero.
- At scale \(R\), the number of constrained primes can be as large as \(\exp(K/R)\). Equation (4a) pays a triple-exponential sufficient height for this growing box. It does not justify arbitrary shrinking diagonals or optimal convergence heights. Its lower fraction tends to zero, consistently with WI-460's vanishing fraction for **every** \(R(T)\to0\).
- A slowly chosen diagonal can retain some responsive zeros at widths tending to zero, by (3)--(4). This is existence with freely chosen heights and widths; it identifies neither a zero's horizontal depth nor the physical relation \(r=(1-\vartheta)d\) for a Kunik defect.
- The leading Haar law loses lower-order arithmetic biases. Ford--Zaharescu's nonzero prime-resonant correction occurs at order \(T\), whereas the normalization here is \(T\log T\). It is not contradicted or eliminated by (8).
- Absolute continuity and (4b) concern each fixed \(Q_\varepsilon(r,\cdot)\). They assert no bounded or smooth density, rate uniform in \(\varepsilon,r\), or absolute continuity for the optimized observables \(M_r,\mathcal M_R\). No maximum attainment, sharp rare-peak constant, or optimal recurrence gap is asserted. The growing-frequency estimate is only (14)--(19) with its stated size and separation costs; it is not an unrestricted growing-dimensional equidistribution law.

The analytical audit points are the unconditional quantifier in (5), dyadic normalization, uniform Hilbert-valued truncation, the tail-independent mixed coefficient (8d), the null-critical-set/change-of-variables step (8e), the tail-uniform box inclusion, the mirror-paired density estimate (15), rational frequency separation (18), and the complete dimension/truncation budget in (19)--(22). No numerical evidence, Lean proof, new critical-line or simplicity proportion, or RH conclusion is claimed. The auxiliary Fourier, real-analytic and sampling lemmas are classical and do not present a separate formalization-fertility question.

## Prior art and novelty assessment

Kevin Ford and Alexandru Zaharescu, *On the distribution of imaginary parts of zeros of the Riemann zeta function*, **Journal für die reine und angewandte Mathematik 579** (2005), 145--158, [arXiv:math/0405459](https://arxiv.org/abs/math/0405459), §1 and equation (3.8), describe unconditional fixed-frequency equidistribution and its zero-density/Landau bridge; §1 specifies multiplicity counting. Their investigation of lower-order prime-resonant bias is stronger information than the leading Haar law used here.

Kevin Ford, K. Soundararajan and Alexandru Zaharescu, *On the distribution of imaginary parts of zeros of the Riemann zeta function, II*, **Mathematische Annalen 343** (2009), 487--505, [DOI 10.1007/s00208-008-0280-x](https://doi.org/10.1007/s00208-008-0280-x), [arXiv:0805.2745](https://arxiv.org/abs/0805.2745), equation (1.1), explicitly states the fixed-frequency continuous-test law. Its later conjectures and RH-conditional refinements are not inputs here. The original Hlawka reference is *Über die Gleichverteilung gewisser Folgen, welche mit den Nullstellen der Zetafunktionen zusammenhängen*, **Sitzungsberichte der Österreichischen Akademie der Wissenschaften, Math.-Naturw. Klasse, Abteilung II 184** (1975), 459--471; the theorem was checked here through the two primary research papers above.

Ford--Zaharescu's Lemmas 1--2 also provide the uniform Landau and Selberg-density inputs for (14)--(15). The layer-cake proof here makes their use uniform even at very small mixed frequencies. Kevin Ford, Xianchang Meng and Alexandru Zaharescu, *Simultaneous distribution of the fractional parts of Riemann zeta zeros*, **Bull. London Math. Soc. 49** (2017), 1--9, [DOI 10.1112/blms.12001](https://doi.org/10.1112/blms.12001), [arXiv:1511.06814v2](https://arxiv.org/abs/1511.06814), Theorem 1, Corollary 1.1 and §2, are closer multidimensional prior art: they treat fixed dimension with Diophantine frequency control and retain lower-order prime bias. Their fixed-dimensional theorem is not used with growing dimension. Equations (16)--(22) instead keep all costs explicitly.

Boris S. Mityagin, *The Zero Set of a Real Analytic Function*,
[arXiv:1512.07276v1](https://arxiv.org/abs/1512.07276), Proposition 0, supplies
the classical null-zero-set fact used for \(\partial_\theta G_W\). The
inverse-function/change-of-variables argument above proves the required
absolute-continuity consequence directly. Yasutaka Ihara, *On
“M-Functions” Closely Related to the Distribution of \(L'/L\)-Values*,
**Publ. RIMS 44** (2008), 893--954,
[DOI 10.2977/PRIMS/1216238306](https://ems.press/journals/prims/articles/2161),
provides neighboring prime-torus density theory for scalar logarithmic
derivatives. That scalar density is not the distribution of this coherent
Hilbert-norm-square observable and is not imported as such.

Finite-dimensional character testing, uniform almost-periodic approximation,
analytic pushforwards, tent Fourier coefficients and phase-box sampling are
standard. The local delta is the proved transfer for the normalized
Euler--Hankel family: an absolutely continuous fixed-parameter response law
and exact frequency at every threshold, positive rare-peak fraction, exact
sampled supremum, and a quantitative lower bound along a stated shrinking-scale
regime. The last conclusion is stronger than fixed-scale convergence because
it retains an error smaller than the shrinking box mass. Qualitative density
regularity does not improve that error budget. This is a classical-method
specialization, with no claim of literature priority, a new general
equidistribution theorem, or an optimal triple-logarithmic scale.
