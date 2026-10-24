# MC-529 — A single near-linear centered variance law is equivalent to RH

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CONDITIONAL-TRANSFER`,
`NO-NOVELTY-CLAIM`. This is a specialization of two persisted arguments;
the variance upper bound remains unproved.

## Claim and mathematical delta

For real \(X\ge2\) and integer \(H\ge1\), put
\[
S_{X,H}(y)=M(y+H)-M(y),\qquad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,
\]
\[
V_\mu(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2dy.
\]
If \(\rho_0=\beta+i\gamma\) is a zeta zero with \(\beta>1/2\)
and multiplicity \(m\), then for every fixed \(B>1\) there are
\(c>0,X_0\) such that, uniformly for real \(X\ge X_0\) and integers
\(1\le H\le X/(\log X)^B\),
\[
\boxed{V_\mu(X,H)\ge
 cH^2X^{2\beta-1}(\log X)^{2m-2}.}                    \tag{1}
\]
Constants depend on \(B,\rho_0\) and the full hypothetical zero set.
No simplicity, rightmost-zero, finite-exception, spacing or
inverse-derivative estimate is assumed.

In particular, fix one \(B>1\), define
\(H_B(X)=\lfloor X/(\log X)^B\rfloor\), and let \(E\subset[2,\infty)\)
be any unbounded set. Then RH is equivalent to
\[
\boxed{\text{For every }\varepsilon>0,\quad
 V_\mu(X,H_B(X))\ll_{\varepsilon,B,E}
 X^{1+\varepsilon}H_B(X)
 \quad\text{for all sufficiently large }X\in E.}      \tag{2}
\]
The constants and onset may depend on \(\varepsilon,B,E\), but not
on the individual \(X\in E\). No density or gap restriction on \(E\)
is needed. Equivalently, existence of even one such unbounded set
already suffices for the forward implication to RH.

[MC-528](MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md)
supplies (1) at each fixed power window. The bounded-source grant in
`CLUE-near-linear-mobius-variance-gevrey-inversion` supplies
[[research/prime_lattice/findings/PL-472-gevrey-box-inversion-reaches-near-linear-prime-windows|PL-472]],
Sections 1–3, for the growing finite inverse. The additional local
conclusion is their uniform reciprocal-zeta transfer, retaining pole
multiplicity, and the exact epsilon-loss equivalence (2). It does not
follow by substituting a moving exponent into MC-528's fixed-exponent
theorem. The argument below reconstructs the transfer in the Möbius
coefficient domain, without a prime-source explicit formula.

## 1. Preserve the Gevrey bound of the multiplicity-aware test

Fix \(1/2<\sigma_0<\sigma_1<\beta\). MC-528, Sections 1–3, proves
the following inputs. A multiplicity-counted density estimate with
some exponent \(0<a<1\) gives a genus-zero product
\[
P(s)=(s-1)\prod_{\substack{\Re\rho>\sigma_0\\\rho\ne\rho_0}}
 (1-s/\rho)^{m_\rho}=\sum_{j\ge0}p_js^j,
\qquad |p_j|\le C A^j/(j!)^{1/a}.                    \tag{3}
\]
Every copy of the selected zero is omitted; its conjugate is retained.
For any fixed
\[
1<q<\min\{B,1/a\},                                  \tag{4}
\]
choose a nonnegative nonzero compact Gevrey bump \(\eta\) supported
strictly inside \((0,\log2)\). Put \(g(t)=e^{-\rho_0t}\eta(t)\),
so \(\|g^{(r)}\|_\infty\le C R^r(r!)^q\), and set
\[
k(t)=\sum_{j\ge0}p_j(-1)^jg^{(j)}(t),\qquad
D=P(\rho_0)\int\eta\ne0,\qquad \phi(u)=D^{-1}k(\log u).
\]
The needed bound is uniform in derivative order, not merely convergence
in each fixed smooth norm. Using \((j+\ell)!\le2^{j+\ell}j!\ell!\),
\[
\begin{aligned}
\|k^{(\ell)}\|_\infty
&\le C\sum_{j\ge0} A^jR^{j+\ell}
             \frac{((j+\ell)!)^q}{(j!)^{1/a}}\\
&\le C(2^qR)^\ell(\ell!)^q
       \sum_{j\ge0}(2^qAR)^j(j!)^{q-1/a}
 \le C'R'^\ell(\ell!)^q.                             \tag{5}
\end{aligned}
\]
The sum is finite because \(q<1/a\). Multiplicities change the
constants in (3), not this argument.

For completeness, differentiation of \(k(\log u)\) gives coefficients
\(u^{-r}s(r,\ell)\), with \(s(r,\ell)\) signed Stirling numbers
of the first kind. The bound
\[
|s(r,\ell)|\le\frac{r!}{\ell!}\binom{r-1}{\ell-1}
\quad(1\le\ell\le r)
\]
follows by replacing each permutation cycle with a linearly ordered
list. On the support \(u>1\), insert (5), use
\((\ell!)^{q-1}\le(r!)^{q-1}\), and sum the binomial coefficients.
Normalization by the fixed nonzero \(D\) therefore gives
\[
\phi\in C_c^\infty((1,2);\mathbb C),\qquad
\|\phi^{(r)}\|_\infty\le C_\phi L^r(r!)^q,\quad L\ge1. \tag{6}
\]
Zero extension preserves this bound and the support.

Writing \(\Phi(s)=\int\phi(u)u^{s-1}du\), the unchanged MC-528
interpolation and reciprocal contour give
\[
\Phi(1)=0,\quad\Phi(\rho_0)=1,\qquad
T_\phi(X):=\sum_n\mu(n)\phi(n/X)
 =X^{\rho_0}Q_{m-1}(\log X)+O_\phi(X^{\sigma_1}),      \tag{7}
\]
where \(Q_{m-1}\) has degree \(m-1\) and nonzero leading coefficient.
Precisely, if the leading Laurent coefficient of \(1/\zeta\) at
\(\rho_0\) is \(d_m\ne0\), that coefficient is \(d_m/(m-1)!\).
MC-528 cancels every unwanted principal part and proves vertical
decay of \(\Phi/\zeta\) by local product division; it does not
assume absolute summability of reciprocal residues. The same proof
works for (4), since its decay exponent \(1/q\) exceeds \(a\).
Equation (7) is used only for this fixed \(\phi\).

## 2. A finite inverse with order-uniform remainder

For zero-extended functions define
\[
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,\qquad
\frac{z}{1-e^{-z}}=\sum_{j\ge0}c_jz^j\quad(|z|<2\pi).
\]
Thus \(c_0=1,c_1=1/2,c_2=1/12,c_3=0,c_4=-1/720\).
Cauchy's estimate on \(|z|=1\) gives \(|c_j|\le C_0\)
with a constant independent of \(j\). For any integer \(N\ge1\), set
\[
f_{h,N}=\sum_{j=0}^{N-1}c_jh^j\phi^{(j)}.
\]
Taylor-expand the \(j\)-th derivative through degree \(N-1-j\)
inside the average. Its remainder is bounded by
\(h^{N-j}\|\phi^{(N)}\|_\infty/(N-j+1)!\).
The identity
\[
\left(\sum_{j\ge0}c_jz^j\right)
\left(\sum_{r\ge0}\frac{(-1)^rz^r}{(r+1)!}\right)=1
\]
cancels all nonconstant terms of degree below \(N\), giving
\[
\|A_hf_{h,N}-\phi\|_\infty
 \le h^N\|\phi^{(N)}\|_\infty
       \sum_{j=0}^{N-1}\frac{|c_j|}{(N-j+1)!}
 \le C_1 C_\phi(Lh)^N(N!)^q.                         \tag{8}
\]
Here \(C_1\) is independent of both \(N\) and \(h\).

For sufficiently small \(h>0\), choose
\[
N(h)=\lfloor(4Lh)^{-1/q}\rfloor\ge1,\qquad f_h=f_{h,N(h)}.
\]
For \(j<N(h)\), the terms \((Lh)^j(j!)^q\) have successive
ratios at most \(1/4\). Hence \(\|f_h\|_\infty\le
4C_0C_\phi/3\). All supports lie in the same compact subset of
\((1,2)\), so \(\sup_h\|f_h\|_2<\infty\). Also
\(\int f_h=\int\phi=\Phi(1)=0\), because all derivative
integrals vanish. Since \(N!\le N^N\), (8) proves
\[
\boxed{\|A_hf_h-\phi\|_\infty
 \le C_2\,4^{-N(h)}\le C_3\exp(-c_3h^{-1/q}).}       \tag{9}
\]
This is a family of finite polynomials in differentiation. No infinite
inverse series or exact inversion across the box's Fourier zeros is used.

## 3. Transfer on the same centered block

Set \(h=H/X\). Compact support, finite interchange, and zero mean give
the exact identity
\[
L_{X,H}:=\sum_n\mu(n)(A_hf_h)(n/X)
 =H^{-1}\int_X^{2X}(S_{X,H}(y)-m_{X,H})f_h(y/X)\,dy. \tag{10}
\]
The coefficient of \(\mu(n)\) is
\(H^{-1}\int_{n-H}^n f_h(y/X)dy\). In particular, (10) retains
the windows crossing the upper block endpoint; zero extension supplies
the correct intersection with \([X,2X]\).

Only \(O(X)\) coefficients occur in the common enlarged support when
\(h\) is small. Therefore \(|\mu(n)|\le1\), (7), and (9) imply
\[
L_{X,H}=X^{\rho_0}Q_{m-1}(\log X)+O(X^{\sigma_1})
                   +O\bigl(Xe^{-c_3h^{-1/q}}\bigr).   \tag{11}
\]
Uniformly for \(h\le(\log X)^{-B}\), the last error is at most
\(CX\exp(-c_3(\log X)^{B/q})\). Since \(B/q>1\), it is
smaller than every fixed negative power of \(X\) for sufficiently
large \(X\). The onset is independent of \(H\) in the stated range.
The nonzero leading coefficient of \(Q_{m-1}\) now gives
\[
|L_{X,H}|\ge c_4 X^\beta(\log X)^{m-1}
\]
on every sufficiently large block, uniformly in \(H\). The cancelled
conjugate mode cannot create a phase zero on a selected subsequence.
A complex measurement is legitimate: its real and imaginary parts
are real tests. A multiple pole whose ordinary residue vanishes still
has the nonzero highest Laurent coefficient used here.

Cauchy–Schwarz in (10) gives
\[
|L_{X,H}|^2\le XH^{-2}V_\mu(X,H)\|f_h\|_2^2.
\]
The uniform norm bound proves (1). No moving-test contour estimate
has been substituted for the fixed-test formula (7).

## 4. Exact strength of the single-law premise

At \(H=H_B(X)\), the ratio of the floor (1) to the ceiling in (2)
is bounded below, up to a positive constant, by
\[
X^{2\beta-1-\varepsilon}(\log X)^{2m-2-B}.            \tag{12}
\]
For any \(\beta>1/2\), choose one fixed
\(0<\varepsilon<2\beta-1\). Expression (12) tends to infinity
along every unbounded \(E\), contradicting (2). All zeros right of
\(1/2\) are excluded; functional-equation symmetry then gives RH.
This argument does not bound \(m\) for zeros on the critical line.

Conversely,
[MC-520](MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md)
proves under RH, uniformly for real \(X\ge2\) and \(1\le H\le X\),
\[
\int_X^{2X}|S_{X,H}(y)|^2dy\ll_\varepsilon X^{1+\varepsilon}H.
\]
Centering subtracts the nonnegative quantity \(X|m_{X,H}|^2\).
This supplies (2) on every \(E\), with its stated real-scale and
integer-window conventions. The claimed equivalence has an
\(X^\varepsilon\) loss. A ceiling \(XH_B(X)(\log X)^A\) with fixed
\(A\) would also imply RH, but that stronger ceiling is not obtained
from MC-520 or asserted as the converse here.

## Prior art, controls and research consequence

The analytical mechanism is a direct specialization of MC-528 and
the boundedly granted PL-472, Sections 1–3. The classical inputs are
the multiplicity-counted density estimate and reciprocal local product
bound recorded as MC-S73 and MC-S67, and compact Gevrey functions
(MC-S79). The derivative-order estimate (5) verifies their compatibility.
Bernoulli inversion is classical; [NIST DLMF §24.2](https://dlmf.nist.gov/24.2)
records its generating function, and
[§2.11](https://dlmf.nist.gov/2.11) supplies the classical context of
exponentially improved truncation (MC-S80). Equations (8)–(9), rather
than an appeal to an unspecified asymptotic remainder, justify the
growing order used here.

[Zaccagnini, §3.3](https://arxiv.org/pdf/1603.02952) (MC-S72) discusses
classical converses from prime Selberg-integral bounds to zero location.
Its prescribed prime main term and multiplicative-window premise are
different from (2). [Chinis, pp. 1–2](https://arxiv.org/pdf/2007.06788v2)
(MC-S69) reports Gao's unpublished RH logarithmic-loss estimate and
identifies its original Möbius setting. That attribution is not used
as an independently checked theorem or to strengthen the converse.
No external priority claim is made. The local gain is the larger
uniform window range and the resulting single-law quantifier, not a
new variance principle or an unconditional RH mechanism.

- The fixed \(q>1\) proof needs \(h^{-1/q}/\log X\to\infty\);
  choosing \(q<B\) ensures it. At \(B=1\), or \(H\asymp X\),
  (9) does not supply the required coefficient error. This failure
  is not a counterexample or a sharp impossibility theorem there.
- The derivative-bank size \(N(h)\) grows. Bounded norm of the
  combined measurement does not give a fixed finite acquisition bank.
  The construction depends on the entire hypothetical zero set;
  neither effective onset nor uniformity as \(\beta\downarrow1/2\)
  or \(B\downarrow1\) is proved.
- The moment in (2) is complete over all starts in \([X,2X]\).
  Removing exceptional starts or using a center that varies with
  \(y\) changes the premise. Sparseness of the selected scale set
  is allowed; incomplete control inside each selected block is not.
- Centering would erase an all-plus sequence at integer window
  length. Its pole at 1 is incompatible with the selected nonreal
  pole and the simultaneous conditions \(\Phi(1)=0\),
  \(\Phi(\rho_0)=1\). Generic bounded-coefficient controls lacking
  MC-528's arithmetic density and division inputs are not covered.

Exact rational checks verified the one-sided inverse coefficients and
their cancellations through truncation order 64, the Stirling
composition majorant through order 64, and nine centered pairings on
integer and noninteger rational blocks, four with nonzero
endpoint-crossing weights. These check orientation, indexing and
normalization only; the analytic inequalities establish uniformity.
No Lean verification or independent adversarial approval is claimed.

Thus a source-derived ceiling of the strength (2), even on sparse
carrying scales, already has full RH strength. This rules out treating
that precise near-linear premise as a weaker surrogate merely because
it is centered or sparsely sampled. It neither supplies the arithmetic
ceiling nor closes questions about weaker estimates or other window
regimes.
