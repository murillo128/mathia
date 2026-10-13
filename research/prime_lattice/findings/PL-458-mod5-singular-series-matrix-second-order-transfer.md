# PL-458 — Mod-5 singular-series triangular covariance diagonalizes under second-order prime-pair control

**Evidence/status:** EXACT-DERIVED + CLASSICAL SINGULAR-SERIES ASYMPTOTICS / CONDITIONAL ACTUAL-PRIME TRANSFER.

**Parent findings:** PL-413, PL-414, PL-421, PL-435, PL-452, PL-457.

## Claim and boundary

Let \(U_5=\{1,2,3,4\}\) and \(H=\lfloor X^\theta\rfloor\), where \(1/6<\theta<1/2\) is fixed. At *one frequency*, \(t=0\), consider the genuine von-Mangoldt residue windows
\[
P_a(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\pmod5}}\Lambda(n),\qquad
R_a(y)=P_a(y)-H/4,\qquad
S_{ab}=\int_X^{2X}R_a(y)R_b(y)\,dy.
\tag{1}
\]
This finding has two logically different conclusions.

**Unconditional singular-series calculation.** Put \(\mathfrak S(k)=0\) for odd \(k\), and for even \(k\ge2\) use the standard Hardy--Littlewood prime-pair singular series
\[
\mathfrak S(k)=2C_2\prod_{\substack{p\mid k\\p>2}}\frac{p-1}{p-2},
\quad C_2=\prod_{p>2}\left(1-\frac1{(p-1)^2}\right).
\]
For \(c\pmod5\), the finite triangular progression sums satisfy
\[
V_c(H):=\sum_{\substack{1\le k<H\\k\equiv c\ (5)}}(H-k)\mathfrak S(k)
=\begin{cases}
H^2/8-\frac12 H\log H+O(H),&c=0,\\
3H^2/32+O(H),&c=1,2,3,4.
\end{cases}
\tag{2}
\]
All implied constants are absolute. In particular, **the logarithmic correction occurs only in the zero-displacement residue class**.

**Conditional prime-source transfer.** Introduce the *actual-prime* dyadic pair sums
\[
C_{ab}(X,k)=
\sum_{\substack{X<n\le2X\\n\equiv a\ (5)\\n+k\equiv b\ (5)}}
\Lambda(n)\Lambda(n+k).
\tag{3}
\]
Write \(\beta_5(k)=5/4\) for \(5\mid k\), \(\beta_5(k)=15/16\) otherwise, and \(\mathfrak S^{(5)}(k)=\mathfrak S(k)/\beta_5(k)\). The fixed-residue local-density model of PL-414 is
\[
M_{ab}(X,k)=\frac{5X}{16}\,
\mathbf1_{k\equiv b-a\ (5)}\,\mathfrak S^{(5)}(k)
=\begin{cases}
X\mathfrak S(k)/4,&a=b,\ 5\mid k,\\
X\mathfrak S(k)/3,&a\ne b,\ k\equiv b-a\ (5),\\
0,&\text{otherwise}.
\end{cases}
\tag{4}
\]
The second equality includes the residue congruences, so impossible pairs contribute zero. It is a **model**, not an unconditional prime-pair asymptotic.

Suppose, in addition to classical fixed-modulus PNT, the following two *unproved inputs* hold for this family of \((X,H)\):

- **(A) Integrated first moments, at covariance precision:**
\[
\max_{a\in U_5}\left|
\int_X^{2X}P_a(y)\,dy-\frac{XH}{4}
\right|=o(X\log X).
\tag{5}
\]
- **(B) Signed, symmetrized second-order Hardy--Littlewood remainder, entrywise:**
\[
\max_{a,b\in U_5}\left|
\sum_{1\le k<H}(H-k)
\left(C_{ab}(X,k)-M_{ab}(X,k)
+C_{ba}(X,k)-M_{ba}(X,k)\right)
\right|=o(XH\log X).
\tag{6}
\]

Then
\[
\boxed{\,S_{ab}=\delta_{ab}\frac{XH}{4}\log(X/H)
          +o(XH\log X)\,}\qquad(a,b\in U_5),
\tag{7}
\]
and, writing \(D=\operatorname{Diag}S\),
\[
\boxed{\,D^{-1/2}SD^{-1/2}=I_4+o_{\rm op}(1),\qquad
\lambda_{\min}(D^{-1/2}SD^{-1/2})>1/4\ \text{eventually}.\,}
\tag{8}
\]
Thus the **pure mod-5 Hardy--Littlewood pair model** has no intrinsic obstruction to the PL-421 normalized image-cone floor: the required additional information resides in (5)--(6), not in its positive leading local factors. Formula (8) is *conditional and only at* \(t=0\). It is not an unconditional assertion about primes or about the full vertically modulated/signed-source Weil construction.

## Exact calculation of the mod-5 triangular singular series

For odd square-free \(d\ge1\) define
\[
a(d)=\prod_{p\mid d}\frac1{p-2};
\qquad a(d)=0\quad\text{otherwise}.
\]
The standard Euler-factor expansion is
\[
\mathfrak S(2m)=2C_2\sum_{d\mid m}a(d).
\tag{9}
\]
With \(L=H/(2d)\) and \(j\in\{1,2,3,4,5\}\) representing a residue modulo 5 (with \(j=5\) representing 0), elementary arithmetic progression summation gives, uniformly for \(L\ge1\),
\[
\sum_{\substack{1\le r<L\\r\equiv j\ (5)}}(L-r)
=\frac{L^2}{10}+\left(\frac12-\frac j5\right)L+O(1),
\quad
\sum_{1\le r<L}(L-r)=\frac{L^2}{2}-\frac L2+O(1).
\tag{10}
\]
The unrestricted formula applies for \(5\mid d\) and \(c=0\); if \(5\nmid d\), the progression \(2dr\equiv c\pmod5\) selects exactly one residue \(j\), and for \(c=0\) this is \(j=5\).

The needed coefficient estimates are
\[
A:=\sum_{d\ge1}\frac{a(d)}d
=\prod_{p>2}\left(1+\frac1{p(p-2)}\right)=C_2^{-1},
\qquad
\sum_{5\mid d}\frac{a(d)}d=\frac A{16},
\tag{11}
\]
\[
\sum_{d\le Y}a(d)=\frac{\log Y}{2C_2}+O(1),
\quad
\sum_{d\le Y}d\,a(d)=O(Y),
\quad
\sum_{d>Y}\frac{a(d)}d=O(1/Y),
\tag{12}
\]
and for any nonprincipal Dirichlet character \(\chi\bmod5\),
\[
\sum_{d\le Y}a(d)\chi(d)=O(1).
\tag{13}
\]
For completeness, (12)--(13) do **not** require prime-pair conjectures. The Dirichlet series \(\sum a(d)d^{-s}\) factors as \(\zeta(1+s)G(s)\), with \(G\) represented by an absolutely convergent Euler product/convolution in a neighborhood of \(s=0\), and \(G(0)=1/(2C_2)\). The principal harmonic sum gives the logarithm with bounded error; partial summation gives the other estimates. For nonprincipal \(\chi\bmod5\), the factorization is \(L(1+s,\chi)G_\chi(s)\) with the same absolute convergence. Bounded partial sums of \(\chi\) make its harmonic sum bounded, proving (13). The factors at \(p=2\) and \(p=5\) are retained in these constants, not silently discarded.

Open (9), write \(k=2dr\), and use (10):
\[
V_c(H)=4C_2\sum_{d\le H/2}d\,a(d)
\sum_{\substack{1\le r<H/(2d)\\2dr\equiv c\ (5)}}
\left(\frac{H}{2d}-r\right).
\tag{14}
\]
For \(c=0\), both \(5\mid d\) (unrestricted \(r\)) and \(5\nmid d\) (the \(j=5\) progression) have linear term \(-L/2\). By (11)--(12),
\[
\begin{aligned}
V_0(H)
&=C_2H^2\left(\tfrac12\sum_{5\mid d}\tfrac{a(d)}d
+\tfrac1{10}\sum_{5\nmid d}\tfrac{a(d)}d\right)
-C_2H\sum_{d\le H/2}a(d)+O(H)\\
&=H^2\left(\tfrac1{32}+\tfrac{15}{160}\right)
-\tfrac12H\log H+O(H)
=H^2/8-\tfrac12H\log H+O(H).
\end{aligned}
\tag{15}
\]
For \(c\ne0\), only \(5\nmid d\) contributes. The quadratic term is
\(C_2H^2\cdot\frac1{10}\cdot\frac{15A}{16}=3H^2/32\).
The coefficient of \(H a(d)\) is \(2C_2(1/2-j(c,d)/5)\). This function of \(d\bmod5\) has mean zero over the four units, so it is a fixed combination of nonprincipal characters; (13) bounds its cumulative contribution by \(O(H)\). The \(O(1)\)-per-progression terms in (10) contribute \(O(\sum_{d\le H/2}d a(d))=O(H)\), and truncating the quadratic Euler sums also costs \(O(H)\). This proves (2).

As a check, summing (2) over all five residues gives
\(\sum_{1\le k<H}(H-k)\mathfrak S(k)
=\frac12H^2-\frac12H\log H+O(H)\), the usual scalar triangular singular-series pattern.

## Conditional transfer to the actual centered matrix

For \(1\le k<H\), every pair \((n,n+k)\) in a window contributes overlap \(H-k\) except when an endpoint lies within \(O(H)\) of \(X\) or \(2X\). As \(\Lambda(n)\ll\log(3X)\), replacing the exact overlap by the dyadic pair sums in (3) costs, entrywise,
\[
O(H^3\log^2(3X))=o(XH\log X)
\quad\text{when}\quad \theta<1/2.
\tag{16}
\]
The self-pair terms are
\[
A_a:=\sum_{\substack{n\equiv a\ (5)}}\Lambda(n)^2
\,|[X,2X]\cap[n-H,n)|
=\frac{XH\log X}{4}(1+o(1))
\tag{17}
\]
uniformly for this range, by fixed-modulus PNT and partial summation.

Expanding the raw Gram, separating the \(k=0\) self-pairs, and inserting (6), (4), and (2) gives, for a diagonal entry,
\[
\int_X^{2X}P_a(y)^2\,dy
=A_a+\frac X2 V_0(H)+o(XH\log X)
=A_a+\frac{XH^2}{16}-\frac{XH}{4}\log H+o(XH\log X),
\tag{18}
\]
where \(O(XH)\) from (2) is swallowed by the displayed error. For \(a\ne b\), with \(c=b-a\bmod5\),
\[
\int_X^{2X}P_a(y)P_b(y)\,dy
=\frac X3\left(V_c(H)+V_{-c}(H)\right)+o(XH\log X)
=\frac{XH^2}{16}+o(XH\log X).
\tag{19}
\]

Finally the exact deterministic-centering identity is
\[
S_{ab}
=\int_X^{2X}P_aP_b\,dy
-\frac H4\left(\int_X^{2X}P_a\,dy+\int_X^{2X}P_b\,dy\right)
+\frac{XH^2}{16}.
\tag{20}
\]
Assumption (5) makes the last two terms together \(-XH^2/16+o(XH\log X)\). This cancels (18)--(19)'s common leading term, leaving
\(S_{aa}=(XH/4)(\log X-\log H)+o(XH\log X)\) and \(S_{ab}=o(XH\log X)\) for \(a\ne b\). Because \(\log(X/H)=(1-\theta+o(1))\log X\) is comparable with \(\log X\), diagonal normalization establishes (7)--(8).

## Prior art, falsification, and research consequence

The pair singular series, its divisor expansion and triangular-logarithmic correction are classical (Montgomery--Soundararajan, 2004); constrained/weighted singular-series sums in progressions are directly in Kuperberg (2025). The local mod-5 factor and conditional residue-density algebra are already PL-413--PL-414. The precise line-level contribution of (2), (15), and (18)--(20) is an explicitly *normalized four-channel* source-model calculation with the correct exceptional \(5\mid k\) logarithmic correction, tied to the existing PL-421 spectral gate. No originality is claimed for the general analytic-number-theory tools, nor is (5) or (6) proved here.

The falsification boundaries are substantive. The residue \(c=0\) cannot be replaced by a generic \(1/5\)-share of the untwisted singular series: doing so loses its \(-\frac12H\log H\) term, exactly the term that creates the centered diagonal. The off-diagonal terms have *no* \(H\log H\) correction at this scale. Dropping the \(5\)-local density factor gives incorrect \(H^2\) coefficients. The dyadic endpoint estimate (16) assumes \(\theta<1/2\); pushing to \(H\asymp X^{1/2}\) requires a separate boundary analysis.

Most importantly, (6) is a **second-order signed error** at the \(XH\log X\) scale, not a consequence of an almost-all first-order Hardy--Littlewood asymptotic with \(o(XH^2)\) aggregate error. PL-435 documents that published 2026 MRSTT technology does not provide it. Likewise (5) is much stronger than a qualitative fixed-modulus PNT at this scale. PL-457's parity-preserving atomic upper-sieve controls need not match either the fine singular-series main term or the second-order error, so they do not refute this conditional implication. This finding neither establishes pointwise positivity at \(t\ne0\), nor resolves the signed PL-418 source-subtracted form or the PL-438 oriented Schur ellipse, nor supplies analytic continuation, a zero-divisor bridge, GRH, or RH. It isolates a falsifiable prime-specific arithmetic theorem whose proof would make the **\(t=0\) centered** gate automatic.
