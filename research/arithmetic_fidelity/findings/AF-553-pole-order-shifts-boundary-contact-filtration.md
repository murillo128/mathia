# AF-553 — Pole order shifts the finite-prefix boundary-contact filtration

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · BOUNDARY-CONTACT · POLE-ORDER · DIRICHLET-TAIL · MATCHED-CONTROL · NO-NOVELTY-CLAIM

## Claim

Let \(m\ge1\) be an integer. Suppose that a real meromorphic source has an exact order-\(m\) pole at \(\sigma\):
\[
F(\sigma+x)=x^{-m}G(x),\qquad G(0)=C>0,
\]
where \(G\) is analytic near zero. For sufficiently small positive \(x\), \(F\) is strictly decreasing. Given a real-analytic finite-prefix perturbation \(A\) near \(\sigma\), use the decreasing inverse branch to define
\[
F(H_A(s))=F(s)-A(s),\qquad H_A(s)\to\sigma\quad(s\downarrow\sigma).
\tag{1}
\]

The transition extends analytically across \(\sigma\) and obeys
\[
\boxed{H_A(\sigma+x)=\sigma+x+\frac{A(\sigma)}{mC}x^{m+1}+O_A(x^{m+2}).}
\tag{2}
\]
Consequently every boundary jet through order \(m\) is identical to the corresponding jet of the identity, regardless of \(A\), and
\[
\boxed{H_A^{(m+1)}(\sigma)=\frac{(m+1)!}{mC}A(\sigma).}
\tag{3}
\]
If \(A(\sigma)\ne0\), order \(m+1\) is the **minimal** jet at which this prefix can be detected.

The more precise filtration statement is as follows. If two perturbations differ first in order \(r\),
\[
(A-B)(\sigma+x)=a_rx^r+O(x^{r+1}),\qquad a_r\ne0,\quad r\ge0,
\tag{4}
\]
then
\[
\boxed{H_A(\sigma+x)-H_B(\sigma+x)
=\frac{a_r}{mC}x^{m+r+1}+O(x^{m+r+2}).}
\tag{5}
\]
Thus prefix agreement through order \(r-1\) implies transition agreement through order \(m+r\); the first surviving derivative is \(m+r+1\). This exponent is exact, not just a sufficient upper bound.

## Analytic existence and contact coefficient

Set \(x=s-\sigma\) and \(H_A(s)-\sigma=xv(x)\). Multiplying (1) by \(x^mv^m\) yields
\[
G(xv)-v^mG(x)+x^mv^mA(\sigma+x)=0.
\tag{6}
\]
At \(x=0,v=1\), the left side is zero and its derivative with respect to \(v\) is \(-mC\ne0\). The analytic implicit-function theorem gives a unique analytic \(v(x)\) with \(v(0)=1\), corresponding to the positive real inverse branch.

Equation (6) gives \(v-1=O(x^m)\), and its first nonzero balance is
\[
-mC(v-1)+x^mA(\sigma)+O(x^{m+1})=0.
\]
Hence \(v-1=A(\sigma)x^m/(mC)+O(x^{m+1})\). Multiplying by \(x\) proves (2), and analyticity proves the boundary derivative formula (3).

For the sharp model \(F(\sigma+x)=Cx^{-m}\), the transition is explicitly
\[
H_A(\sigma+x)-\sigma=x\left(1-\frac{x^mA(\sigma+x)}{C}\right)^{-1/m}.
\tag{7}
\]
This model has no prefactor corrections and still suppresses every prefix perturbation until order \(m+1\).

## Proof of the filtration shift and sharp controls

For two analytic perturbations let \(y_A=H_A(\sigma+x)-\sigma\), \(y_B=H_B(\sigma+x)-\sigma\). By (2) each is \(x(1+O(x^m))\). Subtracting their exact defining identities,
\[
F(\sigma+y_A)-F(\sigma+y_B)=-(A-B)(\sigma+x).
\tag{8}
\]
The divided difference of \(F\) is
\[
\frac{F(\sigma+y_A)-F(\sigma+y_B)}{y_A-y_B}
=-mCx^{-m-1}(1+O(x)),
\tag{9}
\]
because \(F'(\sigma+u)=-mCu^{-m-1}(1+O(u))\) and \(y_A,y_B=x(1+O(x^m))\). Substitution of (4) into (8)--(9) gives exactly (5).

The controls \(A(\sigma+x)=a\) and \(B(\sigma+x)=a+bx^r\), where \(a>0\), \(b\ne0\), \(r\ge1\), are analytic and both positive on a sufficiently small positive interval. They have identical source jets below order \(r\), identical transition jets through order \(m+r\), and a nonzero difference in order \(m+r+1\). For \(r=0\), simply take different positive constants. This demonstrates sharpness for all \(r\) without invoking pathological or sign-changing source data.

The theorem is about **finite analytic prefix information**. If two prefixes agree at the boundary but not in higher derivatives, one low-order transition jet cannot identify them; no finite jet classifies all analytic perturbations.

## Specialization to zeta-power Dirichlet tails

Let \(d_m(n)\) denote the ordinary \(m\)-fold divisor coefficients. Absolute convergence on \(\Re s>1\) gives
\[
\zeta(s)^m=\sum_{n\ge1}d_m(n)n^{-s},\qquad d_m(1)=1.
\tag{10}
\]
Define a positive source and its finite deleted prefix by
\[
F_m(s)=\zeta(s)^m-1=\sum_{n\ge2}d_m(n)n^{-s},
\qquad A_{m,N}(s)=\sum_{2\le n<N}d_m(n)n^{-s},
\tag{11}
\]
and its relative tail transition by
\[
H_{m,N}=F_m^{-1}\circ(F_m-A_{m,N}),\qquad s>1,\quad N\ge2.
\tag{12}
\]
For fixed \(N\), the source and remaining tail decrease continuously from \(+\infty\) to \(0\), so (12) is well-defined on the entire real interval \((1,\infty)\). The common-output-calibration invariance of these full relative transitions is the same elementary cancellation established in AF-550.

The classical Laurent expansion (DLMF §25.2.4)
\[
\zeta(1+x)=x^{-1}+\gamma+O(x)
\]
shows that \(F_m(1+x)=x^{-m}G_m(x)\) with \(G_m(0)=1\). Therefore
\[
H_{m,N}(1+)=1,\qquad
H_{m,N}'(1+)=1,\qquad
H_{m,N}^{(j)}(1+)=0\quad (2\le j\le m),
\tag{13}
\]
and
\[
\boxed{H_{m,N}^{(m+1)}(1+)
=\frac{(m+1)!}{m}\sum_{2\le n<N}\frac{d_m(n)}n.}
\tag{14}
\]
Since \(A_{m,N+1}-A_{m,N}=d_m(N)N^{-s}\),
\[
\boxed{H_{m,N+1}^{(m+1)}(1+)-H_{m,N}^{(m+1)}(1+)
=\frac{(m+1)!}{m}\frac{d_m(N)}N.}
\tag{15}
\]
For \(m=1\), the first informative jet is the second derivative: \(H_{1,N}''(1+)=2\sum_{2\le n<N}n^{-1}\), with adjacent increment \(2/N\). For \(m=2\), the first informative jet is the third derivative and the increment is \(3d_2(N)/N\).

The marked family of these jets recovers standard positive divisor coefficients; neither (14) nor (15) supplies a criterion for zeros or RH. The result is the exact threshold at which a compressed boundary-jet representation begins to see its finite source prefixes.

## Conditioning and the logarithmic contrast

At a fixed positive boundary offset \(x\), (5) says that two prefixes which first differ in order \(r\) produce horizontal transition separation of scale \(x^{m+r+1}\). In particular,
\[
mC\,\frac{H_A(\sigma+x)-(\sigma+x)}{x^{m+1}}
=A(\sigma)+O_A(x).
\tag{16}
\]
An additive observation error \(\delta\) in the horizontal transition is magnified by \(mC|\delta|x^{-(m+1)}\). This is a local deterministic error budget for fixed source germs, not a uniform large-\(N\) recovery theorem. The coefficient \(d_m(N)/N\) in (15) may itself become small.

AF-552 concerns a different singularity class. For a logarithmic source \(P(1+x)=-\log x+R(x)\) with analytic regular part, the same relative transition construction gives \(H_A'(1+)=\exp(A(1))\). Thus **logarithmic divergence exposes a finite prime prefix in first-order dilation**, while a pole of order \(m\) forces identity contact through order \(m\), and only the \((m+1)\)-st derivative is prefix-sensitive. This does not contradict AF-548's finite-separated-jet no-go: the common source boundary and entire reference profile are already retained before taking the relative transition.

A downstream arithmetic representation that keeps only jets through order \(m\) cannot reconstruct a finite analytic prefix by subsequent deterministic processing of those jets alone. Keeping deeper derivatives still requires adequate precision in the destination seminorm.

## Prior-art and novelty audit

- The Laurent series of \(\zeta\) and Dirichlet convolution identity (10) are classical, documented by NIST DLMF §25.2.
- The proof by (6) is an elementary analytic implicit-function argument; the filtration identity (5) follows from a standard divided-difference estimate.
- For constant \(A\equiv a\), the equation \(F\circ H_a=F-a\) is an Abel/Fatou translation coordinate. The leading \(x^{m+1}\) term is the familiar contact order of a parabolic germ. See Marco Abate, *Discrete holomorphic local dynamical systems*, arXiv:0903.3289, for the classical setting. A nonconstant \(A(s)\) generally does not define a one-parameter translation action.

No novelty is claimed for complex-analytic inversion, parabolic germs, zeta expansions, or divisor coefficients. The durable Mathia-specific result is the **source-to-transition filtration law** in (5) and its exact compression/recovery boundary for the zeta-power tails. This is a local structural theorem with a clear no-go for shallow boundary representations, not evidence for RH.

## Boundaries and audit tests

1. The pole order is an integer \(m\ge1\), \(C>0\), and \(G,A,B\) are analytic at the retained boundary. Essential, fractional, logarithmic, and nonanalytic singularities require separate hypotheses.
2. The input coordinate \(s\) and boundary point \(\sigma\) are fixed. Unrestricted input reparameterization changes both jet depths and coefficients.
3. The same \(F\) and same local inverse branch are used in comparisons. Changing the source or singular leading coefficient can change the entire fidelity channel.
4. If \(A(\sigma)=0\), the first potentially informative transition jet moves deeper; (5) determines the depth from the exact first nonzero source difference.
5. Check the \(v\)-derivative \(-mC\) in (6), the divided difference (9), the explicit model (7), and the DLMF pole coefficient \(G_m(0)=1\) used in (14)--(15).
6. Exact fixed-\(N\) analytic jets do not imply uniform large-\(N\) stability, noise resistance before the quotient is formed, or a prime-specific zero-discriminator downstream.

## Consequence for Arithmetic Fidelity

The singularity order fixes a **minimal boundary-jet fidelity tariff** for finite analytic source prefixes. A pole of order \(m\) erases every finite-prefix change from the first \(m\) transition jets and shifts every order-\(r\) prefix difference to order \(m+r+1\). Its full nonlocal transition profile remains faithful, but any shallower jet compression is provably blind. A viable downstream pole-based RH mechanism would need to retain this contact structure (or another rigorously equivalent witness) and pay its noise/conditioning cost; none is supplied by this theorem.
