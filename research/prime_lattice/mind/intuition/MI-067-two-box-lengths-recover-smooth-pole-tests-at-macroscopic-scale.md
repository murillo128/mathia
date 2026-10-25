# MI-067 — Two box lengths recover a smooth pole test at macroscopic scale

**Evidence level:** supported conditional synthesis of [PL-475](../../findings/PL-475-two-box-lengths-force-paired-macroscopic-prime-variance.md), with the single-box boundary in [PL-474](../../findings/PL-474-nonquasianalytic-tests-close-the-iterated-log-window-boundary.md). Compact-distribution multichannel deconvolution is classical. No arithmetic variance ceiling or new general inversion theorem is asserted.

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
