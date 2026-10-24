# MC-524 — Density-one window control coexists with prescribed sparse poles

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim and scope

Fix any \(1/2<\beta<1\) and any \(\gamma>0\). There is a deterministic,
nonmultiplicative sequence \(a(n)\in\{-1,0,1\}\), with

\[
|a(n)|=\mu(n)^2,
\qquad A(x)=\sum_{n\le x}a(n),
\]

and a predetermined set \(G\subset\mathbb N\), with the following
simultaneous properties.

1. The complement has counting function \(O(J/\log J)\) up to \(J\).
   Consecutive retained indices differ by at most three.
2. For every sufficiently large \(j\in G\), \(X=2^j\), every integer
   \(1\le H\le X\), and every real \(X\le y\le2X\),
   \[
   |A(y+H)-A(y)|\le4\sqrt{H\log X}.
   \tag{1}
   \]
   Thus the complete uncentered window moment is at most
   \(16XH\log X\); its empirically centered variance is no larger.
3. All qualitative fixed-shift Chowla correlations hold: for distinct
   fixed nonnegative shifts \(h_i\), and \(e_i\in\{1,2\}\) not all even,
   \[
   T^{-1}\sum_{n\le T}\prod_i a(n+h_i)^{e_i}\longrightarrow0.
   \tag{2}
   \]
4. The Dirichlet series \(D_a(s)=\sum_n a(n)n^{-s}\), initially absolutely
   convergent for \(\Re s>1\), continues meromorphically to
   \(\Re s>1/2\). Its **only poles there** are the prescribed conjugate
   pair \(\beta\pm i\gamma\), each simple with residue \(1/2\).
5. Its exact power growth exponent is \(\beta\):
   \[
   A(x)\ll_\varepsilon x^{\beta+\varepsilon}\quad(\varepsilon>0),
   \qquad A(x)\ne O(x^{\beta-\varepsilon})\quad(\varepsilon>0).
   \tag{3}
   \]

In particular, choose any fixed \(0<\theta<1\) and

\[
1-\theta/2<\beta<1.
\]

The control meets the diagonal-order complete moment ceiling at
\(H=\lfloor X^\theta\rfloor\) on density-one dyadic scales, while its
Dirichlet series has poles beyond the boundary that
[MC-522](MC-522-centered-dyadic-variance-recovers-all-reciprocal-zeta-poles.md)
would exclude from **all-scale** variance information. The pole count
in every fixed right half-plane is bounded, hence satisfies the sparse
pole condition \(o(T)\).

This strengthens the analytic admissibility of the control in
[MC-523](MC-523-density-one-dyadic-window-control-permits-near-linear-prefixes.md).
Meromorphic continuation throughout the open right critical half-plane,
sparse poles, exact square-free support and qualitative correlations do
not repair density-one scale interpolation. The omitted-index bound is
weaker than MC-523's \(O(\log J)\); no claim preserves that stronger mesh.

This is **not** a Möbius or multiplicative counterexample. No Euler
product, functional equation, continuation through the critical line,
or reciprocal-zeta vertical-growth estimate is imposed. Those are
possible additional arithmetic inputs, not consequences of this control.

## 1. Moment matching concentrates a Mellin pole on sparse log blocks

Write \(L=\log2\), and choose a fixed interval

\[
I=[u_0,u_1]\subset(0,L),\qquad u_0=1/4,\quad u_1=1/2.
\]

For sufficiently large integers \(k\), put

\[
j_k=\lfloor k\log k\rfloor,\quad t_k=Lj_k,\quad
T_k=t_{k+1}-t_k,\quad
r_k=\left\lfloor\frac{t_k}{\sqrt{\log t_k}}\right\rfloor.
\tag{4}
\]

Here \(T_k\asymp\log k\asymp\log t_k\), \(T_k>u_1\) eventually, and
the consecutive intervals \([t_k,t_{k+1})\) cover a half-line.
The smaller intervals \(t_k+I\) lie strictly inside the dyadic log
blocks indexed by \(j_k\).

Let \(p_d\) be the real orthonormal Legendre polynomials for Lebesgue
measure on \(I\), and let

\[
K_r(u,v)=\sum_{d=0}^r p_d(u)p_d(v).
\]

For any polynomial \(P\) of degree at most \(r\), orthonormal expansion
gives, for **every real** \(v\),

\[
\int_I K_r(u,v)P(u)\,du=P(v).
\tag{5}
\]

The extension outside \(I\) is a polynomial identity; no positivity
of the kernel or of its eventual signed profile is required.
Define

\[
h_k(u)=\int_0^{T_k}e^{\beta v}
 \cos(\gamma(t_k+v))K_{r_k}(u,v)\,dv\quad(u\in I),
\]

and define \(g\) on the log half-line by

\[
g(t_k+u)=e^{\beta t_k}h_k(u)\quad(u\in I),
\qquad g=0\quad\hbox{elsewhere}.
\tag{6}
\]

Equation (5) matches the first \(r_k+1\) log moments of the reference
density \(e^{\beta t}\cos(\gamma t)\) on the **whole** interval
\([t_k,t_{k+1})\), using a signed density supported on \(t_k+I\).

Two estimates make the growing degree legitimate. Standard Legendre
normalization and its finite polynomial expansion give, with a fixed
\(C>1\),

\[
\sup_{u\in I}|p_d(u)|\le C\sqrt{d+1},\qquad
\sup_{0\le v\le T}|p_d(v)|
 \le C\sqrt{d+1}[C(1+T)]^d.
\]

Consequently,

\[
\|h_k\|_\infty+\|h_k\|_1
\le C T_k e^{\beta T_k}(r_k+1)^2[C(1+T_k)]^{r_k}
=\exp(o(t_k)).
\tag{7}
\]

Indeed \(r_k\log(1+T_k)=
O(t_k\log\log t_k/\sqrt{\log t_k})=o(t_k)\).
It follows that

\[
f(x):=x^{-1}g(\log x)
\quad\hbox{satisfies}\quad
|f(x)|\le x^{\beta-1+o(1)}.
\tag{8}
\]

In particular this is a real signed density whose amplitude tends to
zero, despite the increasing internal oscillation of its log profiles.

For a compact set of complex \(s\), expand \(e^{-su}\) through degree
\(r_k\) at zero. The polynomial contributions cancel by (5).
If \(E_k(s)\) is the difference between the Laplace transforms of (6)
and the reference density on the \(k\)-th interval, the two Taylor
remainders give

\[
\begin{split}
|E_k(s)|\le e^{(\beta-\Re s)t_k}\bigg[&
\|h_k\|_1 e^{|s|u_1}
 \frac{(|s|u_1)^{r_k+1}}{(r_k+1)!}\\
&+T_k e^{(\beta+|s|)T_k}
 \frac{(|s|T_k)^{r_k+1}}{(r_k+1)!}\bigg].
\end{split}
\tag{9}
\]

Stirling's elementary factorial estimate and (4) show that the logarithm
of the bracket is at most

\[
-(1+o(1))t_k\sqrt{\log t_k}.
\tag{10}
\]

For clarity, the negative term is \(r_k\log r_k\sim
t_k\sqrt{\log t_k}\); all terms \(O(T_k)\), \(O(r_k)\), and
\(O(r_k\log(1+T_k))\) are smaller. Thus \(\sum_kE_k(s)\) converges
normally on **every** compact subset of the complex plane.

Starting the construction at \(k=k_0\), set \(t_0=t_{k_0}\) and
\(z=\beta+i\gamma\). Initially on \(\Re s>\beta\), absolutely
convergent integration and (9) give

\[
\int_1^\infty f(x)x^{-s}\,dx
=\frac{e^{-(s-z)t_0}}{2(s-z)}
 +\frac{e^{-(s-\bar z)t_0}}{2(s-\bar z)}+E(s),
\qquad E\ \hbox{entire}.
\tag{11}
\]

This is an explicit meromorphic continuation, with residue \(1/2\)
at each specified pole. Every omitted initial interval changes only an
entire term. The slowly growing gaps \(T_k=O(\log t_k)\) are essential
to the simultaneous amplitude and Taylor-error estimates used here.

## 2. Put the mean on the exact square-free support

Let \(c=6/\pi^2\), and enumerate the square-free integers increasingly
as \(n_m\). The elementary identity
\(\mu(n)^2=\sum_{d^2\mid n}\mu(d)\) gives

\[
Q(x)=\sum_{n\le x}\mu(n)^2=cx+O(\sqrt x),
\qquad n_m=m/c+O(\sqrt m).
\tag{12}
\]

Partition the positive real axis into
\(I_m=((m-1)/c,m/c]\). Define deterministic means

\[
\eta_{n_m}=\int_{I_m}f(x)\,dx,\qquad
\eta_n=0\quad(n\text{ not square-free}).
\tag{13}
\]

For \(x\in I_m\) at large \(m\), \(x=n_m+O(\sqrt{n_m})\).
Hence (8) implies

\[
|\eta_n|\le n^{\beta-1+o(1)}.
\tag{14}
\]

Choose the initial \(k_0\) large enough that every mean has modulus
at most \(1/2\). The support of \(f\) in a \(j_k\)-block is contained
in \([e^{u_0}2^{j_k},e^{u_1}2^{j_k}]\). Its distance from either
dyadic endpoint is a fixed positive multiple of \(2^{j_k}\).
The \(O(\sqrt{n_m})\) displacement in (12) is smaller, so every
nonzero \(\eta_n\) still lies strictly in

\[
2^{j_k}<n<2^{j_k+1}
\tag{15}
\]

for some \(k\ge k_0\). No differentiability estimate for the rapidly
oscillating \(f\) is used in this discretization.

Let \(B(s)=\sum_n\eta_n n^{-s}\). On a compact set with
\(\sigma=\min\Re s\), the mean-value estimate for \(x^{-s}\) yields

\[
|n_m^{-s}-x^{-s}|\ll_K x^{-\sigma-1/2}\quad(x\in I_m).
\]

The difference between \(B(s)\) and the left side of (11) is therefore
a normally convergent series of entire functions on

\[
\Re s>\beta-1/2,
\tag{16}
\]

because, for sufficiently small fixed \(\delta>0\), its absolute
majorant is
\(C_K\int_{e^{t_0}}^\infty x^{\beta-1+\delta-\sigma-1/2}\,dx<\infty\).
Thus \(B\) has exactly the two poles from (11) throughout (16).
Since \(\beta<1\), this domain contains \(\Re s>1/2\).

## 3. Independent signs retain the poles and supply the window bounds

For each square-free \(n\), independently choose \(a(n)=1\) with
probability \((1+\eta_n)/2\), and \(a(n)=-1\) otherwise. Put \(a(n)=0\)
off that support. Thus \(\mathbb E a(n)=\eta_n\).

Hoeffding's inequality for independent variables of range length at
most two gives

\[
\mathbb P\left(\left|\sum_{n\le N}(a(n)-\eta_n)\right|>u\right)
\le2e^{-u^2/(2N)}.
\]

Taking \(u=3\sqrt{N\log N}\) and applying Borel--Cantelli over all
integers \(N\) shows that almost surely

\[
R(x):=\sum_{n\le x}(a(n)-\eta_n)
=O(\sqrt{x\log x}).
\tag{17}
\]

Abel summation then makes \(\sum_n(a(n)-\eta_n)n^{-s}\) holomorphic
on \(\Re s>1/2\), locally uniformly there: its tails are bounded by
the endpoint term and \(|s|\int_N^\infty |R(x)|x^{-\Re s-1}dx\).
Adding this function to \(B\) proves the pole assertion. Holomorphic
random noise cannot cancel either principal part.

Define the predetermined good set

\[
G=\mathbb N_{\ge1}\setminus
\bigcup_{k\ge k_0}\{j_k-1,j_k\}.
\tag{18}
\]

For large \(k_0\), successive \(j_k\) differ by at least three, so
omitted runs have length two and consecutive good indices differ by
at most three. Since \(j_k\asymp k\log k\), the omitted count up to
\(J\) is \(O(J/\log J)\).

If \(j\in G\), \(X=2^j\), the range \((X,3X]\) misses every biased
block (15): for a given \(j_k\), either \(j\le j_k-2\), so
\(3X\le3\cdot2^{j_k}/4\), or \(j\ge j_k+1\), so
\(X\ge2^{j_k+1}\). All square-free signs in every requested window
are therefore symmetric and independent.

For each integer window of length \(H\), the two-sided tail is at most
\(2\exp(-u^2/(2H))\). There are at most \(2X^2\) integer start/length
pairs with \(X\le v\le2X\), \(1\le H\le X\). Substituting
\(u=4\sqrt{H\log X}\) gives failure probability at most \(4X^{-6}\).
Summing over dyadic \(X\) proves (1) almost surely, simultaneously in
all lengths. For real \(y\) and integer \(H\), the window equals the
one with start \(\lfloor y\rfloor\). This accounts for every real
start, not almost all starts.

To prove (2), fix a pattern. Independence gives

\[
\left|\mathbb E\prod_i a(n+h_i)^{e_i}\right|\longrightarrow0,
\]

because an odd exponent contributes a factor \(\eta_{n+h_i}\to0\),
and all other factors have modulus at most one. Separate the starts
into residue classes modulo \(1+\max_i h_i\). Within each class the
products use disjoint signs. Hoeffding and Borel--Cantelli show that
the average minus its expectation tends to zero. Cesàro averaging of
the expectations finishes the fixed pattern, and a countable
intersection handles every pattern together with (17) and (1).

Fix one realization in this probability-one event. Changing finitely
many initial values to \(a(1)=a(2)=a(3)=1\), \(a(6)=-1\) makes it
visibly nonmultiplicative without changing any assertion, any pole,
or the exact square-free support. It adds only a Dirichlet polynomial.

Finally (14) and (17) give the upper bound in (3). If an upper bound
\(A(x)=O(x^{\beta-\varepsilon})\) held, Abel summation would make
\(D_a\) holomorphic on \(\Re s>\beta-\varepsilon\), contradicting
its nonzero principal part at \(\beta+i\gamma\). This proves the
lower assertion in (3) without claiming a signed asymptotic formula
for the sharp sum.

## Prior art, audit and consequences

The finite-dimensional reproducing-kernel mechanism is classical; see
Leonard Bos and A. F. Ware, *On the Uniqueness of an Orthogonality
Property of the Legendre Polynomials*, Dolomites Research Notes on
Approximation 11 (2018), 37--42,
[Introduction, equation (1)](https://drna.padovauniversitypress.it/system/files/papers/BosWare_2018_UOP.pdf).
The Legendre normalization and polynomial representations are also
recorded in [DLMF §18.3](https://dlmf.nist.gov/18.3) and
[§18.5](https://dlmf.nist.gov/18.5). Here only their elementary
reproduction and growth bounds are used, not the paper's special
orthogonality theorem. Hoeffding concentration, square-free counting,
and the fixed-pattern argument are the same classical ingredients
audited in MC-523 and sources MC-S10--MC-S12, MC-S75.

The important gap-theorem distinction is between a scalar lacunary
series \(\sum_k c_k2^{-j_ks}\) and the present series with a different
entire within-block transform at every \(k\). Fabry's classical
[gap-theorem work](https://www.numdam.org/articles/10.24033/asens.431/)
does not justify replacing the latter by the former. The actual
Dirichlet frequencies inside a nonzero mean block are \(\log n\),
with many closely spaced frequencies, not just the sparse mesh
\(j_k\log2\). Equations (5)--(11) explicitly exhibit the cancellation
that such a scalar replacement would discard. No general failure of
Fabry's theorem is alleged.

Targeted searches covered Dirichlet-series gap theorems, prescribed
poles, analytic continuation with bounded coefficients, and signed
polynomial moment matching. These identify classical ingredients and
neighboring interpolation constructions, not an external novelty
claim. The durable local delta is the simultaneous control (1)--(3)
with the prescribed sparse poles: the failure left open by MC-523
persists after adding the meromorphic and sparse-pole inputs used in
MC-522, provided the all-scale premise is weakened to density one.

Exact rational checks verified (5) for every monomial through degree
\(r\), for \(r=0,\ldots,8\), using the shifted Legendre recurrence on
\([1/4,1/2]\) (45 identities). The displayed orthonormal expansion
proves every degree. The normal-convergence, square-free transport,
and probability-one arguments above establish the infinite construction;
finite simulations would not establish it. No independent adversarial
approval or formal verification is claimed.

The construction spends increasing within-block oscillation, not large
coefficient amplitudes. It uses signs essentially; a positive profile
cannot reproduce arbitrary high moments of mass outside its support.
Nothing here bounds the meromorphic continuation uniformly at growing
imaginary height, identifies it with reciprocal zeta, or supplies an
Euler product. A density-one theorem for actual Möbius must use an
additional constraint that couples missing scales to retained scales
or restricts these moving signed profiles. Continuation and a count
of poles, by themselves, are insufficient. No unconditional Möbius
estimate or conclusion about RH follows.
