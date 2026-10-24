# PL-469 — Positive sparse-block sources retain negative pole residues

**Evidence/status:** EXACT-DERIVED + CLASSICAL REPRODUCING-KERNEL INPUT;
MATCHED-CONTROL OBSTRUCTION; NO EXTERNAL NOVELTY CLAIM.

## Claim and scope

Fix \(1/2<\beta<1\) and \(\gamma>0\). Put
\[
 j_k=\lfloor k\log k\rfloor,\qquad
 G_*=\mathbb N_{\ge1}\setminus
       \{j_k-1,j_k:k\ge k_0\},
 \tag{1}
\]
where the fixed starting index \(k_0\) is sufficiently large.
There is a single real coefficient sequence \(b_n\) such that:

- \(b_n=0\) when \(5\mid n\), and \(5/8\le b_n\le15/8\)
  otherwise;
- for each \(a\in\{1,2,3,4\}\) and every \(\varepsilon>0\),
  \[
  \sum_{\substack{n\le x\\n\equiv a\ (5)}}b_n
  =x/4+O_\varepsilon(1+x^{\beta+\varepsilon});
  \tag{2}
  \]
- for every sufficiently large \(j\in G_*\), \(X=2^j\), and
  every integer \(1\le H\le X\), the complete empirical variance is
  \[
  P_1(y;H)=\sum_{\substack{y<n\le y+H\\n\equiv1\ (5)}}b_n,
  \quad \mu_{X,H}=X^{-1}\int_X^{2X}P_1(y;H)\,dy,
  \qquad
  \int_X^{2X}|P_1-\mu_{X,H}|^2dy\le\frac{25}{16}X;
  \tag{3}
  \]
- all four transforms
  \[
  D_\chi(s)=\sum_n b_n\chi(n)n^{-s},\qquad \chi\bmod5,
  \tag{4}
  \]
  initially absolutely convergent for \(\Re s>1\), continue meromorphically to \(\Re s>\beta-1\). Their only poles
  there are \(z=\beta+i\gamma\) and \(\bar z\), each simple with
  **residue \(-1\) in every channel**, together with the principal
  channel's pole at \(1\), of residue \(1\).

The identity-residue transform satisfies exactly
\[
 D_1^{\rm res}(s):=\sum_{n\equiv1(5)}b_nn^{-s}=\frac14\sum_{\chi\bmod5}D_\chi(s),
 \tag{5}
\]
and has residue \(-1\) at each off-critical pole; no cancellation is
possible. Conjugation compatibility
\(D_{\bar\chi}(\bar s)=\overline{D_\chi(s)}\) holds. There are only
\(O(J/\log J)\) omissions up to index \(J\), and consecutive retained
indices differ by at most three.

Thus, if \(0<\theta<1\) and \(\beta>1-\theta/2\), (3) satisfies
\(O(XH(\log X)^A)\) for \(H=\lfloor X^\theta\rfloor\) and any
fixed \(A\ge0\), while (4) has poles beyond \(1-\theta/2\).
Positivity, correct residue masses, integer support, negative real
residues and finite pole count do not repair density-one recovery on
**this mesh**.

This resolves the positive-source transfer posed in the local
[[research/prime_lattice/clues/CLUE-variable-profile-sparse-poles-on-moderate-mesh|moving-profile clue]].
It does not resolve the accepted \(3^k\)-mesh clue or change PL-466's
every-block theorem. No prime support, Euler product, functional
equation, relative covariance frame or controlled growth of the
continued transforms at large imaginary height is claimed.

## 1. A signed perturbation with a meromorphic Mellin transform

The analytic construction is the changing-profile mechanism of
[[research/mobius_cancellation/findings/MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles|MC-524]],
read under the clue's bounded source grant. The necessary argument is
reconstructed here; its random signs and square-free transport are not
used in this destination construction.

Set \(L=\log2\), \(I=[1/4,1/2]\subset(0,L)\), and
\[
 t_k=Lj_k,\quad T_k=t_{k+1}-t_k,\quad
 r_k=\left\lfloor\frac{t_k}{\sqrt{\log t_k}}\right\rfloor.
 \tag{6}
\]
Eventually \(T_k>1/2\) and \(T_k\asymp\log t_k\).
Let \(p_d\) be the real orthonormal Legendre polynomials on \(I\), and
\(K_r(u,v)=\sum_{d=0}^r p_d(u)p_d(v)\). For every polynomial \(P\)
of degree at most \(r\),
\[
 \int_I K_r(u,v)P(u)\,du=P(v)\qquad(v\in\mathbb R).
 \tag{7}
\]
Expansion in the orthonormal basis proves this even for \(v\notin I\),
and linearity includes polynomials with complex coefficients.
Define the real, generally signed profile
\[
 h_k(u)=\int_0^{T_k}e^{\beta v}\cos(\gamma(t_k+v))
                         K_{r_k}(u,v)\,dv,
 \quad u\in I,
\]
\[
 g(t_k+u)=e^{\beta t_k}h_k(u)\ (u\in I),\qquad
 g=0\text{ elsewhere},\qquad f(x)=x^{-1}g(\log x).
 \tag{8}
\]
Only \(k\ge k_0\) is used. The intervals \([t_k,t_{k+1})\) partition
the log half-line starting at \(t_0:=t_{k_0}\).
Equation (7) matches the first \(r_k+1\) log moments of
\(e^{\beta t}\cos(\gamma t)\) on the whole \(k\)-th interval using
mass supported in its fixed interior subinterval \(t_k+I\).

Classical Legendre normalization and finite polynomial representations
(sources 134--135) imply, for a fixed \(C>1\),
\[
 \sup_{u\in I}|p_d(u)|\le C\sqrt{d+1},\qquad
 \sup_{0\le v\le T}|p_d(v)|\le C\sqrt{d+1}[C(1+T)]^d.
\]
Hence
\[
 \|h_k\|_\infty+\|h_k\|_1
 \le C T_k e^{\beta T_k}(r_k+1)^2[C(1+T_k)]^{r_k}
 =\exp(o(t_k)).
 \tag{9}
\]
Indeed \(r_k\log(1+T_k)=o(t_k)\). Consequently
\[
 |f(x)|\le x^{\beta-1+o(1)},
 \tag{10}
\]
so its amplitude tends to zero. There is no uniform derivative bound
on these growing-degree profiles, and none will be needed.

For a compact set of complex \(s\), subtract the degree-\(r_k\)
Taylor polynomial of \(e^{-su}\) in the two matched transforms.
If \(E_k(s)\) denotes the profile transform minus the reference
transform on \([t_k,t_{k+1})\), (7) gives
\[
 |E_k(s)|\le e^{(\beta-\Re s)t_k}
 \left[
 \|h_k\|_1e^{|s|/2}\frac{(|s|/2)^{r_k+1}}{(r_k+1)!}
 +T_ke^{(\beta+|s|)T_k}
                    \frac{(|s|T_k)^{r_k+1}}{(r_k+1)!}
 \right].
 \tag{11}
\]
Uniformly on the compact set, the bracket is at most
\(\exp(-(1+o(1))t_k\sqrt{\log t_k})\): the dominant negative term
is \(-r_k\log r_k\); the terms \(O(T_k)\), \(O(r_k)\), and
\(O(r_k\log(1+T_k))\) are smaller. This beats the prefactor for every
fixed compact set. Each \(E_k\) is entire, so their normally
convergent sum \(E\) is entire.

For \(\Re s>\beta\), absolute convergence now proves
\[
 M_f(s):=\int_1^\infty f(x)x^{-s}\,dx
 =\frac{e^{-(s-z)t_0}}{2(s-z)}
  +\frac{e^{-(s-\bar z)t_0}}{2(s-\bar z)}+E(s).
 \tag{12}
\]
This continues \(M_f\) meromorphically to the plane with precisely the
two simple poles, both of residue \(1/2\). Raising \(k_0\) removes
only a compactly supported part and does not change these residues.

## 2. Cell integrals preserve poles and positive atomic coefficients

The cells \([n,n+5)\), \(n\equiv1\pmod5\), \(n\ge1\), partition
\([1,\infty)\). Put
\[
 \eta_n=\int_n^{n+5}f(x)\,dx\quad(n\equiv1\pmod5),
\qquad
 b_n=\begin{cases}
 0,&5\mid n,\\
 5/4-2\eta_n,&n\equiv1\pmod5,\\
 5/4,&n\equiv2,3,4\pmod5.
 \end{cases}
 \tag{13}
\]
The real numbers \(\eta_n\) satisfy
\(|\eta_n|\le n^{\beta-1+o(1)}\). Choose \(k_0\) so large that
\(|\eta_n|\le5/16\) everywhere. Equation (13) gives the asserted
\([5/8,15/8]\) coefficient bounds. It is the **perturbation** that
uses signs; the full source stays positive.

For \(n\) near the support at \(N_k=2^{j_k}\), a nonzero cell integral
requires
\[
 e^{1/4}N_k-5\le n\le e^{1/2}N_k.
\]
After increasing \(k_0\), this interval is strictly inside
\((N_k,2N_k)\). Atomic transport therefore keeps every perturbation
in its omitted dyadic block.

The absolute mass of the cell integrals up to \(x\) is bounded by
\(\int_1^{x+5}|f(u)|du=O_\varepsilon(1+x^{\beta+\varepsilon})\).
Counting each progression with error \(O(1)\) proves (2).
Choosing \(0<\varepsilon<1-\beta\) gives the claimed \(x/4+o(x)\).

Let \(B(s)=\sum_{n\equiv1(5)}\eta_n n^{-s}\). The exact transport
error, initially for \(\Re s>\beta\), is
\[
 B(s)-M_f(s)=
 \sum_{n\equiv1(5)}\int_n^{n+5}
                 f(x)(n^{-s}-x^{-s})\,dx=:E_{\rm at}(s).
 \tag{14}
\]
For a compact set \(K\) with \(\sigma=\min_{s\in K}\Re s\),
\(|n^{-s}-x^{-s}|\ll_K x^{-\sigma-1}\) on these cells.
If \(\sigma>\beta-1\), choose
\(0<\varepsilon<\sigma-(\beta-1)\); the absolute majorant is
\[
 C_K\int_{e^{t_0}-5}^{\infty}
                  x^{\beta-\sigma-2+\varepsilon}\,dx<\infty.
 \tag{15}
\]
Each cell contribution is entire. Normal convergence makes
\(E_{\rm at}\) holomorphic on \(\Re s>\beta-1\). Thus the exact
atomic transform has the same principal parts as (12), on a half-plane
strictly larger than the one required in the clue. This argument moves
the test function \(x^{-s}\), not the oscillating density \(f\).

Because \(\chi(1)=1\) in every channel, (13) gives
\[
 \boxed{D_\chi(s)=\frac54L(s,\chi)-2B(s).}
 \tag{16}
\]
The classical Hurwitz progression decomposition (source 130) makes
\(L(s,\chi)\) entire for nonprincipal \(\chi\); for \(\chi_0\) its
sole pole is at 1, of residue \(4/5\). Equations (12)--(16) prove
all pole assertions and normalizations. Orthogonality of the four
characters proves (5) initially in absolute convergence and then by
continuation. Reality of \(b_n\) proves conjugation compatibility.

## 3. Every retained window sees only the periodic background

For large \(k_0\), successive \(j_k\) differ by at least three and
\(j_k\asymp k\log k\). This proves the omission count and gap assertion
following (5).

Fix \(j\in G_*\), \(X=2^j\), and one perturbed block \((N_k,2N_k)\).
Either \(j\le j_k-2\), so \(3X\le3N_k/4<N_k\), or
\(j\ge j_k+1\), so \(X\ge2N_k\). Therefore \((X,3X]\) misses every
perturbation. Every window in (3), including every real starting point,
lies in this range. Exactly
\[
 P_1(y;H)=\frac54\#\{n\equiv1\pmod5:y<n\le y+H\},
 \qquad |P_1(y;H)-H/4|\le5/4.
 \tag{17}
\]
The empirical mean minimizes squared distance to a constant. Comparing
it with \(H/4\) proves (3). In fact the same argument gives the same
variance bound in the other three residues. The source is fixed before
\(j,H\), or any window exponent is selected.

## Prior art, checks and the remaining arithmetic boundary

Polynomial reproduction is classical (Bos--Ware, source 134), as are
the Legendre bounds (source 135), Hurwitz continuation (source 130),
and transport by bounded-displacement cells. The moment-matching
concentration and entire remainder are the MC-524 mechanism, not a new
mechanism claimed here. The destination delta is their simultaneous
realization with **positive** coefficients, fixed residue masses,
negative unit residues in all four channels, and retained absolute
variance \(O(X)\). Positivity of the full source does not require
positivity of its small signed perturbation.

The neighboring prescribed-divisor theory for Helson zeta functions
([Andersson, Theorem 1](https://arxiv.org/html/2408.15713v1), source 11)
uses completely multiplicative unimodular coefficients. It supplies
neither the positive-source conclusion nor the prescribed retained
window bounds here. Landau's nonnegative-coefficient theorem (source
121) is consistent with the construction: the positive series has
abscissa of absolute convergence 1 and its required real singularity
there. That theorem does not forbid the two poles of its meromorphic
continuation to the left of 1.

The lacunary obstruction in PL-468 and sources 132--133 assumes a common
within-block profile. Here the log profiles change with the block and
match an increasing number of moments. The physical Dirichlet
frequencies within a block are the many closely spaced \(\log n\),
not just \(j_k\log2\); replacing their transforms by scalar lacunary
coefficients loses the cancellation in (11). This is consistent with
the classical gap theorems, not an exception to them.

The proof was checked for coefficient signs, the factor 2 in the
principal parts, the \(1/4\) character average, support after atomic
transport, and compact-uniform convergence. Exact rational arithmetic
also verified (7) for all monomials through degree \(r\), for
\(r=0,\ldots,8\) (45 identities), using
\(K_r(u,v)=\sum_{d=0}^r4(2d+1)P_d(8u-3)P_d(8v-3)\).
These finite checks supplement the all-degree argument (7); they do
not prove the infinite construction. No formal verification or
independent adversarial approval is claimed.

The mesh matters. For \(j_k=3^k\), one has \(T_k\asymp t_k\);
the estimate \(r_k\log(1+T_k)=o(t_k)\) used in (9) fails for this
choice of \(r_k\). The construction therefore supplies no result on
the thinner accepted mesh. It also does not provide the continued
transforms with the vertical-growth bounds needed to shift sharp
Perron contours and infer a uniform oscillatory window asymptotic from
their poles. Such an asymptotic cannot be imported merely from
meromorphicity and a finite pole count.

Any recovery theorem on \(G_*\) for the actual prime source must use
an additional input beyond the abstract positivity, residue and
continuation conditions tested here. Rational-prime support, a genuine
Euler product, functional-equation constraints, and quantitative
continuation bounds are not supplied by this control. No RH/GRH result,
actual-prime variance estimate, or external priority claim follows.
