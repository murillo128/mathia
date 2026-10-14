# WI-452 — Cyclotomic positivity can enlarge the sharp support budget for commensurate reciprocal Fourier grids

**Status:** EXACT-DERIVED + CLASSICAL-CYCLOTOMIC-REDUCTION + EXACT-POSITIVITY-OBSTRUCTION + WANG-CLASS-SPECIALIZATION + NON-RH + NO-PRIORITY-CLAIM

**Local dependencies:** WI-450 (multi-grid support and superflat smoothing), WI-451 (sharp two-commensurate-grid overlap formula).

**Prior-art anchors:** Etkind--Lev (2023), DOI 10.1112/plms.12570, simultaneous tiling by two progressions; J. P. Steinberger (2012), DOI 10.37236/2755, nonnegative cyclotomic multiples; H. Tan and Y. Zhang (2026), arXiv:2609.07646, sharp diameter bounds for nonnegative cyclotomic multiples; T. Kepka and M. Korbelar (2012), arXiv:1210.6868, general minimum-degree nonnegative multiples. The finite polynomial reduction uses elementary root-of-unity Fourier analysis; no general novelty or priority is claimed.

## Sharp criterion for finite commensurate families

Fix the convention \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt\), with \(\int f=1\). Let \(M=\{m_1,\ldots,m_s\}\subset\mathbb N\), \(h>0\), and prescribe all zeros
\[
\widehat f(k/(m_i h))=0\quad (1\le i\le s,\ k\in\mathbb Z\setminus\{0\}). \tag{1}
\]
Put
\[
Q_M(z)=\operatorname{lcm}_{m\in M}(1+z+\cdots+z^{m-1})
      =\prod_{\substack{d>1\\d\mid m\text{ for some }m\in M}}\Phi_d(z),
\qquad D=\deg Q_M.
\tag{2}
\]
Define the **nonnegative-multiple degree**
\[
d_+(Q_M)=\min\{\deg P:\;0\ne P\in\mathbb R[z],\ Q_M\mid P,
\ P\text{ has all coefficients }\ge0\}.\tag{3}
\]
It is finite because \(\prod_{m\in M}(1+\cdots+z^{m-1})\) is a nonnegative multiple; necessarily \(d_+\ge D\).

**Theorem.** The least length of an enclosing interval supporting an integrable normalized **signed real** solution of (1) is exactly \(h(D+1)\). The least such length for a **nonnegative** normalized integrable solution is exactly \(h(d_+(Q_M)+1)\). Both endpoints are attained by compactly supported piecewise-constant densities (signed in the first case).

For Wang's even smooth-square admissible class
\[
\mathcal F_\lambda=\{\eta^2:\eta\in C_c^\infty((-\lambda/2,\lambda/2);\mathbb R),\;
\eta\text{ even},\;\int\eta^2=1\},
\]
there exists an \(f\in\mathcal F_\lambda\) obeying every prescribed zero in (1) **if and only if**
\[
\boxed{h(d_+(Q_M)+1)<\lambda}. \tag{4}
\]
This is an enclosing-interval threshold, not a claim about least Lebesgue measure of the possibly disconnected support.

## Proof: periodization reduces each fiber to one polynomial

Fourier uniqueness on the circle converts the complete reciprocal-zero grid for \(m h\) into the exact tiling equation
\[
\sum_{n\in\mathbb Z}f(t+n m h)=\frac1{m h}\qquad\text{a.e. }t. \tag{5}
\]
Translate an enclosing support interval to \([0,L]\). For almost every \(x\in(0,h)\), the finite polynomial
\(A_x(z)=\sum_{j\ge0}f(x+jh)z^j\)
has residue sums equal to \(1/(m h)\) modulo every \(m\in M\). Consequently \(A_x(1)=1/h\), and \(A_x(\zeta)=0\) for every nonidentity \(m\)-th root of unity, so \(Q_M\mid A_x\) in \(\mathbb C[z]\). Since the coefficients are real, divisibility holds in \(\mathbb R[z]\). If \(f\ge0\), all coefficients of \(A_x\) are nonnegative. Hence its degree is at least \(D\) or \(d_+\), respectively. In any enclosing interval of length \(L<(d+1)h\), there is a positive-measure set of residues \(x\in(0,h)\) for which at most \(d\) consecutive \(h\)-cells meet the interval, so \(\deg A_x<d\). This contradicts the relevant degree bound and proves both lower bounds.

Conversely choose any polynomial \(P(z)=\sum_{j=0}^d a_jz^j\) divisible by \(Q_M\), with \(P(1)\ne0\). Then the normalized step density
\[
\rho_P(t)=\frac{1}{hP(1)}\sum_{j=0}^d a_j\,\mathbf1_{[jh,(j+1)h)}(t)
\tag{6}
\]
has unit integral and support within \([0,(d+1)h]\). Its Fourier transform is the length-\(h\) uniform sinc factor multiplied by \(P(e^{-2\pi i h\xi})/P(1)\) (up to a zero-free phase): at \(\xi=k/(m h)\), the sinc vanishes if \(m\mid k\), and otherwise \(Q_M\) vanishes at the nontrivial \(m\)-th root. Thus (1) is exact. Taking \(P=Q_M\) gives signed equality with degree \(D\); taking a minimizing nonnegative \(P\) gives positive equality with degree \(d_+\). A minimizing nonnegative \(P\) necessarily has positive constant and leading coefficient: otherwise its monomial factor could be removed because \(Q_M(0)=1\).

Every cyclotomic \(\Phi_d\) with \(d>1\) is reciprocal, hence \(Q_M\) is reciprocal. If the minimizing positive polynomial is not palindromic, replace it with \(P(z)+z^dP(1/z)\): divisibility, nonnegative coefficients and degree \(d\) persist. Center (6) to obtain an even probability density. Convolve it with an even normalized superflat bump of support width \(\delta>0\), chosen so \((d+1)h+\delta<\lambda\). The Fourier zeros survive exactly. The derivative-power bounds \(|g^{(n)}|\le C_{n,\alpha}g^\alpha\) for every \(n\) and \(0<\alpha<1\) pass to \(f=\rho_P*g\) by Jensen's inequality; as in WI-450, the chain rule with \(\alpha>1-1/(2n)\) extends each derivative of \(\sqrt f\) by zero at the zero set. Thus \(\sqrt f\in C_c^\infty\), proving sufficiency in (4). Necessity is strict since a Wang function is supported in a closed interval of length strictly less than \(\lambda\).

## Exact five-period positivity gap

Take \(M=\{12,15,20,22,33\}\). Its nontrivial root orders are
\(\mathcal D=\{2,3,4,5,6,10,11,12,15,20,22,33\}\), and the exact cyclotomic product \(Q=\prod_{d\in\mathcal D}\Phi_d\) has degree \(D=75\), \(Q(1)=660\), and **the only negative coefficients of \(Q\) are** \([z]Q=[z^{74}]Q=-1\); both endpoint coefficients are \(1\). It follows that no nonnegative polynomial of degree \(75\) is divisible by \(Q\) (every such multiple is a scalar multiple of \(Q\)). On the other hand, exact coefficient multiplication shows that \((1+z)Q(z)\) has entirely nonnegative coefficients, degree \(76\), and value \(1320\) at \(z=1\). Therefore
\[
\boxed{d_+(Q)=76,\qquad L_{\rm signed}=76h,\qquad
 L_{\rm nonnegative}=77h,\qquad
 \mathcal F_\lambda\text{ feasible}\iff 77h<\lambda.}\tag{7}
\]
An exact reproducibility certificate (no floating-point inference) is:

    import sympy as s
    z = s.Symbol('z')
    M = (12, 15, 20, 22, 33)
    orders = sorted({d for m in M for d in s.divisors(m) if d > 1})
    Q = s.Poly(s.prod(s.cyclotomic_poly(d, z) for d in orders), z)
    P = s.Poly((1 + z) * Q.as_expr(), z)
    assert Q.degree() == 75 and Q.eval(1) == 660
    assert [(j, Q.nth(j)) for j in range(76) if Q.nth(j) < 0] == [(1, -1), (74, -1)]
    assert P.degree() == 76 and P.eval(1) == 1320
    assert all(P.nth(j) >= 0 for j in range(77))

For two commensurate periods, \(Q_M\) has degree \(m+n-\gcd(m,n)-1\), and the WI-451 nonnegative construction realizes degree \(D\); hence (4) reduces exactly to WI-451's threshold \(p+q-\gcd(p,q)<\lambda\). The five-period example proves that this no-extra-positivity-charge property does not extend to all finite families.


## Three grids have no extra positivity cost; four are necessary and sufficient

For any three positive integer periods \(a,b,c\) (repetitions allowed), write
\(S_m(z)=1+z+\cdots+z^{m-1}\),
\(g_{ab}=\gcd(a,b)\), \(g_{bc}=\gcd(b,c)\),
\(g_{ac}=\gcd(a,c)\), and \(g=\gcd(a,b,c)\).
Inclusion--exclusion for each cyclotomic factor \(\Phi_d\), \(d>1\), gives the exact polynomial identity
\[
Q_{\{a,b,c\}}(z)
=\frac{S_a(z)S_b(z)S_c(z)S_g(z)}
       {S_{g_{ab}}(z)S_{g_{bc}}(z)S_{g_{ac}}(z)}
=S_g(z)\frac{S_a(z)}{S_{g_{ab}}(z)}
       \frac{S_b(z)}{S_{g_{bc}}(z)}
       \frac{S_c(z)}{S_{g_{ac}}(z)}. \tag{8}
\]
Whenever \(v\mid u\),
\(S_u(z)/S_v(z)=\sum_{r=0}^{u/v-1}z^{rv}\), a polynomial with
nonnegative integer coefficients. Hence \(Q_M\) itself is coefficientwise
nonnegative for every family of **at most three** commensurate periods.
In particular, \(d_+(Q_M)=\deg Q_M\): the sharp signed and nonnegative
enclosing-interval thresholds coincide, and Wang's smooth-square criterion
remains \(h(\deg Q_M+1)<\lambda\). This is an exact identity, not an
extrapolation from a bounded search.

The threshold can already separate at **four periods**. Set
\[
M_4=\{14,21,30,35\},\qquad
\mathcal D_4=\{2,3,5,6,7,10,14,15,21,30,35\},\quad
Q_4=\prod_{d\in\mathcal D_4}\Phi_d. \tag{9}
\]
Exact integer coefficient arithmetic gives \(\deg Q_4=77\),
\(Q_4(1)=210\), and precisely four negative coefficients:
\([z]Q_4=[z^8]Q_4=[z^{69}]Q_4=[z^{76}]Q_4=-1\).
Since every degree-77 multiple of the monic \(Q_4\) is scalar,
there is no coefficientwise-nonnegative nonzero multiple of degree 77.
Conversely \((1+z)Q_4\) has **all** coefficients nonnegative, degree 78,
and value 420 at 1. Thus
\[
\boxed{d_+(Q_4)=78,\quad
L_{\rm signed}=78h,\quad L_{\rm nonnegative}=79h,\quad
\mathcal F_\lambda\text{ feasible}\iff79h<\lambda.} \tag{10}
\]
An exact, self-contained verification certificate is:

    import sympy as s
    z = s.Symbol('z')
    M4 = (14, 21, 30, 35)
    orders4 = sorted({d for m in M4 for d in s.divisors(m) if d > 1})
    Q4 = s.Poly(s.prod(s.cyclotomic_poly(d, z) for d in orders4), z)
    R4 = s.Poly((1 + z) * Q4.as_expr(), z)
    assert Q4.degree() == 77 and Q4.eval(1) == 210
    assert [(j, Q4.nth(j)) for j in range(78) if Q4.nth(j) < 0] == [
        (1, -1), (8, -1), (69, -1), (76, -1)
    ]
    assert R4.degree() == 78 and R4.eval(1) == 420
    assert all(R4.nth(j) >= 0 for j in range(79))

Therefore **four is the smallest possible number of commensurate periods**
for a positive-coefficient support surcharge. The existing five-period
example has a smaller absolute degree but does not establish this
cardinality threshold. The inclusion--exclusion construction is elementary
cyclotomic algebra, not a claim of a new general tiling theorem; the
Fourier/source-admissibility and RH limitations above remain unchanged.

## Prior art, falsification controls, and Weil-inertia boundary

The correspondence between (5), roots of unity and nonnegative cyclotomic multiples is classical. Etkind--Lev settle the sharper support-**measure** theorem for **two** progressions. Steinberger and Tan--Zhang analyze nonnegative multiples of cyclotomic factors, so neither the degree formulation nor the possibility of positivity-induced obstructions should be presented as a new general theory. Kepka--Korbelar address general nonnegative polynomial multiples. The source-specific content here is the exact arbitrary finite commensurate-grid criterion coupled to Wang's even smooth-square admissibility, and the explicit five-period gap. No exhaustive novelty claim is made.

Check that no grid is double-counted: repeated or dividing periods merely remove redundant cyclotomic factors in (2). Check that the signed \(Q\) construction is **not** claimed to produce Wang-admissible \(\eta^2\) when its coefficients are negative. Check that the \(h\)-cell polynomial argument controls enclosing-interval length, not disconnected support measure. At equality in (4) the positive step density exists on a closed window but its smooth-square perturbation cannot fit compactly inside the same open window.

These constraints apply to a **prescribed finite family of artificial real-frequency grids**. They do not force actual zeta ordinates onto those grids, supply a zeta-derived test function, control the off-critical indefinite Weil blocks, or improve an unconditional certified simple-critical proportion. An RH-facing implication would require independent arithmetic data tying an individual off-line block to such source-fixed Fourier constraints; none is proved here.
