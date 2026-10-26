# MI-067 — Two box lengths recover a smooth pole test at macroscopic scale

**Evidence level:** supported conditional synthesis of [PL-475](../../findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md) and [PL-476](../../findings/PL-476-trimmed-paired-prime-variance-retains-the-grh-obstruction.md), with the single-box boundary in [PL-474](../../findings/PL-474-nonquasianalytic-tests-close-the-iterated-log-window-boundary.md). Compact-distribution multichannel deconvolution is classical. No arithmetic variance ceiling or new general inversion theorem is asserted.

Let \(b_a=a^{-1}\mathbf1_{[0,a]}\), \(A_af=b_a*f\), and use
\(\widehat f(\xi)=\int f(u)e^{-iu\xi}\,du\). A single box has zeros
\(\widehat b_a(2\pi n/a)=0\), \(n\ne0\). Two lengths with
\(\alpha=\sqrt2\) admit compact finite-order distributions satisfying
\[
b_1*T_1+b_\alpha*T_2=\delta_0,\qquad
\operatorname{supp}T_1\subset[-1,1+\alpha],\quad
\operatorname{supp}T_2\subset[-1,1].
\]
The key arithmetic of the **length ratio**, independent of the prime
source, is \(\|\alpha n\|_{\mathbb Z}\gg1/|n|\). Thus
\(v_n=\widehat b_\alpha(2\pi n)^{-1}=O(n^2)\) for \(n\ne0\),
with \(v_0=0\), defines a periodic distribution \(V\). Multiplying by
a smooth window \(w\in C_c^\infty((-1,1))\) with
\(\sum_{j\in\mathbb Z}w(u+j)=1\) yields \(T_2=wV\)
with these Fourier samples. For \(D=\delta_0-b_\alpha*T_2\),
the periodization of \(D'\) vanishes. With \(\tau_jF(u)=F(u-j)\),
\(T_1=\sum_{j\ge0}\tau_jD'\) is compactly supported and
\((I-\tau_1)T_1=D'\), giving the identity including zero frequency.

For any fixed mean-zero \(\phi\in C_c^\infty((4/3,5/3))\), dilate
the distributions by \(h\), preserving mass, and set
\(f_{j,h}=T_{j,h}*\phi\). For \(0<h\le1/20\),
\[
A_hf_{1,h}+A_{\alpha h}f_{2,h}=\phi,\qquad
\int f_{j,h}=0,\qquad
\sup_h(\|f_{j,h}\|_\infty+\|f'_{j,h}\|_\infty)<\infty.
\]
Their supports stay inside one compact subinterval of \((1,2)\).
Finite distributional order costs finitely many derivatives of the
fixed target; differentiation under dilation produces factors \(h^r\),
so the norm does not blow up as \(h\to0\). This recovers smooth target
tests, not arbitrary signals by a bounded \(L^2\) inverse.

For integer \(H\), put \(h=H/X\), \(K=\lfloor\sqrt2H\rfloor\),
\(k=K/X\). Even though the integer lengths are commensurable,
\[
\|A_hf_{1,h}+A_kf_{2,h}-\phi\|_\infty
\le\tfrac12|k-\alpha h|\|f'_{2,h}\|_\infty=O_\phi(X^{-1}).
\]
No exact inverse for the rounded pair is claimed. This error contributes
only \(O(\log X)\) against \(a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)}\)
on the common \(O(X)\)-sized support.

If \(\rho_0\) is a nontrivial zero of zeta or one of the three primitive
nonprincipal Dirichlet functions modulo 5 with \(\Re\rho_0>1/2\), the
independent arithmetic input is PL-471's fixed complex target,
which may be supported in \((4/3,5/3)\) and satisfies
\[
\sum_na_n\phi(n/X)=-w_{\rho_0}X^{\rho_0}+O(X^{\sigma_0}),
\qquad w_{\rho_0}>0,\quad 1/2<\sigma_0<\beta=\Re\rho_0.
\]
Its sparse-zero annihilator and noncancelling identity-residue weights
are not supplied by deconvolution. For
\(S_L(y)=\sum_{y<n\le y+L}a_n\), own empirical mean \(m_L\), and
\(V_1(X,L)=\int_X^{2X}|S_L-m_L|^2\), the exact pairing is
\[
L^{-1}\int_X^{2X}(S_L(y)-m_L)f(y/X)\,dy
=\sum_na_n(A_{L/X}f)(n/X).
\]
Adding the two pairings and using direct-sum Cauchy–Schwarz gives,
for every sufficiently large real \(X\) and integer \(1\le H\le X/20\),
\[
\boxed{V_1(X,H)/H^2+V_1(X,K)/K^2\gg X^{2\beta-1}.}
\]
At least one normalized variance is large; no independence or choice
of which length is large is available. Bounds
\(V_1(X,L)\ll XL(\log X)^A\) for **both** \(L=H,K\), on one
unbounded scale set with \(H=\lfloor X/20\rfloor\) and fixed finite
\(A\ge0\), imply joint GRH
modulo 5. A ceiling at just one member does not suffice.

For integer base scales, PL-476 also recovers the complete pairings
after deleting whole starts. Put \(I_X=\{X,\ldots,2X-1\}\),
\(L_1=H,L_2=K\), and independently choose \(E_i\subset I_X\),
\(B_i=|E_i|<X/2\), and constants \(c_i\in\mathbb C\). Define
\[
W_i=\sum_{j\in I_X\setminus E_i}|S_{L_i}(j)-c_i|^2.
\]
The exact endpoint difference is
\(S_L(j+1)-S_L(j)=a_{j+L+1}-a_{j+1}\). Since both coefficients
lie in \([0,\log(3X)]\), its modulus is at most \(\log(3X)\).
The finite recovery lemma for a sequence with jumps bounded by \(J\)
gives \(\sum_j|r_j|\le2\sqrt{XW}+2JB^2\) when \(B<X/2\).
Applying it separately to the centered windows yields
\[
\boxed{\sum_{i=1}^2
 \frac{\sqrt{XW_i}+B_i^2\log(3X)}{L_i}\gg X^\beta.}
\]
The complete mean-zero pairings still recover the pole-isolating target
with the same \(O(\log X)\) rounding error; no test is multiplied by a
mask. Different masks and retained empirical means are allowed. A
start-dependent fitted profile need not preserve either cancellation
of the center or the jump bound.

At \(H=\lfloor X/20\rfloor\), joint GRH for the four functions is
equivalent to the existence of one unbounded integer scale set and
mask/center families, fixed before epsilon, for which both channels obey
\[
B_i\ll_\varepsilon X^{3/4+\varepsilon},\qquad
W_i\ll_\varepsilon X^{1+\varepsilon}L_i
\quad\text{for every }\varepsilon>0.
\]
The resulting upper bound is
\(O_\varepsilon(X^{1/2+\varepsilon/2}
+X^{1/2+2\varepsilon}\log(3X))\), contradicting any \(\beta>1/2\)
for sufficiently small epsilon. The converse uses the separate prime
estimate \(\psi(x;5,1)=x/4+O(\sqrt{x}\log^2(3x))\) under joint
GRH: empty masks and \(c_i=L_i/4\) give
\(W_i\ll X^2\log^4(3X)\). This suffices because \(L_i\asymp X\);
it does not give the same ceiling at arbitrary short lengths.
The \(3/4\) deletion exponent is sufficient, not proved optimal for
primes; qualitative \(B_i=o(X)\) is insufficient for this recovery bound.

[PL-477](../../findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity.md)
closes the generic signed-test escape even with shared-source and
common-mask constraints. Fix any nonzero mean-zero
\(\varphi\in C_c^\infty((4/3,5/3);\mathbb C)\) and
\(1/2<\gamma<1\). Choose \(u_0\) with \(\varphi'(u_0)\ne0\).
On sufficiently separated scales \(X=10^k\), let
\(m=\lfloor X^\gamma\rfloor\), take \(N\equiv1\pmod5\) within
five of \(u_0X\), and put a balanced packet on that residue:
\[
d_{N+5\ell}=\begin{cases}1/4&0\le\ell<m,\\-1/4&m\le\ell<2m.\end{cases}
\]
All packets together define one fixed sequence \(d\). The two fixed
positive completions
\(b_n^\pm=(5/4)\mathbf1_{n\equiv1\ (5),\ n\ge6}\pm d_n\)
have coefficients at most \(3/2\), the logarithmic envelope
\(b_n^\pm\le\log n\), and sums \(x/4+O(x^\gamma)\).
The current packet's primitive vanishes outside
\(Q=\{N,\ldots,N+10m-1\}\); no other packet contributes on
\([X,3X]\). At \(H=\lfloor X/20\rfloor\), \(K=\lfloor\sqrt2H\rfloor\),
the common mask
\[
E_X=Q\cup(Q-H)\cup(Q-K),\qquad B_X=30m,
\]
hides both endpoint differences. Every retained window value agrees
for the two completions and the periodic background, and each energy
about \(L/4\) is at most \(25X/16\). Nevertheless
\[
\sum_n(b_n^+-b_n^-)\varphi(n/X)
=-\tfrac52\varphi'(u_0)m^2/X+O_\varphi(m^3/X^2).
\]
The packet has zero mass but first moment \(-5m^2/4\), so the signed
test detects it. Identical observed vectors force any estimator of
this target to incur error \(\gg_\varphi B_X^2/X\) on one completion.
For \(\gamma>3/4\) the hidden response exceeds square-root size while
the retained energies are \(O(X)\). Thus positivity, correct leading
residue density, bounded jumps, common masks and two consistent windows
cannot alone save a power of the quadratic deletion cost, even for a
target known in advance. This is an exact non-prime control: it proves
neither necessity of the prime logarithm nor optimality for von Mangoldt
coefficients, and supplies no arithmetic pole formula for these sources.

[PL-478](../../findings/PL-478-geometric-coverage-retains-sparsely-sampled-prime-variance.md)
replaces the deleted count by coverage geometry, permitting any nonempty
retained set \(R_i\subset I_X\). For the nearest-sample map
\(\pi_i\), define
\[
w_{i,r}=|\pi_i^{-1}(r)|,\qquad D_i=\sum_{j\in I_X}|j-\pi_i(j)|,
\qquad \widetilde W_i(c_i)=\sum_{r\in R_i}w_{i,r}|S_{L_i}(r)-c_i|^2.
\]
Telescoping the prime jump bound and weighted Cauchy–Schwarz give
\(\sum_j|S_{L_i}(j)-c_i|\le\sqrt{X\widetilde W_i}+\log(3X)D_i\).
Applying this to the same complete tests yields
\[
\boxed{\sum_{i=1}^2
\frac{\sqrt{X\widetilde W_i(c_i)}+\log(3X)D_i}{L_i}
\gg X^\beta.}
\]
This keeps the non-effective zero-dependent constants and the uniformity
in lengths, separate masks and constant centers. No positive retained
fraction is needed; inserting a mask into the smooth test is still invalid.

At the macroscopic pair, fix \(g_X=\lfloor\sqrt X\rfloor\),
\(R_X=\{X+kg_X:0\le k\le\lfloor(X-1)/g_X\rfloor\}\), and
\(q_X=|R_X|\asymp\sqrt X\). Let
\(Q_i(X)=\min_c\sum_{r\in R_X}|S_{L_i}(r)-c|^2\).
The grid satisfies \(D_i\le Xg_X\), \(w_{i,\max}\le2g_X\),
and \(g_Xq_X\le2X\). Using the ordinary sample mean in both
energies, \(\widetilde W_i\le2g_XQ_i\). Therefore
\[
\exists\mathcal X\text{ unbounded, fixed before }\varepsilon,
\quad Q_i(X)/q_X\ll_\varepsilon X^{1+\varepsilon}
\quad(i=1,2;\ \forall\varepsilon>0;\ X\in\mathcal X)
\]
is equivalent to joint GRH for the four mod-5 functions. Both channels
must obey the bound on the same scale set. The forward cost is
\(O_\varepsilon(X^{1/2+\varepsilon/2}+X^{1/2}\log(3X))\),
which cannot accommodate any \(\beta>1/2\). The converse uses
the GRH pointwise bound for \(\psi(x;5,1)\), giving
\(Q_i/q_X\ll X\log^4(3X)\) with the trial center \(L_i/4\).
It does not deduce sparse energy from complete mean square.
PL-477's clustered gaps instead have \(D_i\asymp B^2\), so its
hidden signed response and this sparse-grid criterion are consistent.
The finite recovery is classical; neither the required arithmetic ceiling
nor an optimal prime sample count or logarithmic loss is established.

PL-474's single-box certificate stops at
\(H=X/[\log X(\log\log X)^r]\), \(r>1\), within that family of
uniform fixed-target approximations. The second channel changes the
operator and reaches macroscopic lengths without disproving that
single-channel obstruction. Rational ratios have common Fourier zeros;
Liouville ratios force superpolynomial reciprocal samples and cannot
have this compact finite-order inverse. Mere irrationality is insufficient.
Constants still depend on the full hypothetical arithmetic zero set;
there is no effective certificate, absolute variance estimate or
relative covariance lower frame from these inverse tests alone.
