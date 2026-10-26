# PL-479 — Prime-supported relative perturbations retain signed interval-query ambiguity

**Evidence/status:** EXACT-DERIVED / LITERATURE+DERIVED / NEGATIVE CONTROL;
CLASSICAL OPTIMAL-RECOVERY MECHANISM; NO EXTERNAL NOVELTY CLAIM.
The controls preserve the actual prime-power support and a relative weight
bound, but do not preserve the exact von Mangoldt coefficients.

## Claim and quantifiers

Fix a nonzero complex test
\(\phi\in C_c^1((4/3,5/3))\), independently of the integer scale
\(X\). The additional condition \(\int\phi=0\) is allowed but
not needed. Write
\[
a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)},\qquad
T_X(b)=\sum_n b_n\phi(n/X).
\tag{1}
\]
There are \(c_\phi,\kappa_\phi>0\), a fixed interval
\([s,t]\Subset(4/3,5/3)\), and \(X_\phi\) such that, for every
integer \(X\ge X_\phi\) and every list of \(q\) integer interval
queries \((u_\ell,v_\ell]\), \(0\le u_\ell<v_\ell\), with
\[
0\le q\le\kappa_\phi\frac{X}{\log(3X)},
\tag{2}
\]
there is a real, finitely supported perturbation \(d\) satisfying
\[
\begin{gathered}
\operatorname{supp}d\subset(sX,tX],\qquad |d_n|\le a_n/2,
\qquad \sum_n d_n=0,\\
\sum_{u_\ell<n\le v_\ell}d_n=0\quad(1\le\ell\le q),\\
\boxed{\left|\sum_n d_n\phi(n/X)\right|
\ge c_\phi\frac{X}{(q+1)\log(3X)}.}
\end{gathered}
\tag{3}
\]
Consequently the two controls \(b_n^\pm=a_n\pm d_n\) have exactly
the support of \(a\), satisfy
\[
\tfrac12a_n\le b_n^\pm\le\tfrac32a_n,
\qquad
\sum_{u_\ell<n\le v_\ell}b_n^\pm
=\sum_{u_\ell<n\le v_\ell}a_n,
\tag{4}
\]
and obey \(|T_X(b^+)-T_X(b^-)|\ge2c_\phi X/((q+1)\log(3X))\).
All queries, including different lengths, arise from one coefficient
sequence per control. The controls may depend on the scale and query
list; no fixed pair across all scales is asserted.

This resolves the weighted-support question in the local
[[research/prime_lattice/clues/CLUE-prime-supported-weighted-endpoint-ambiguity|Master clue]].
The endpoint partition and fixed derivative phase were suggested by
[[research/mobius_cancellation/findings/MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity|MC-534]],
Sections 1–3, read under that clue's bounded grant. The unequal-weight
construction and destination estimate are proved below. They do not use
the square-free sign assignment or its small observed energies.

## 1. A weighted primitive with prescribed zero endpoints

First take any integer cell \((l,r]\) and capacities
\(0\le c_n\le M\), where \(M>0\). Set
\[
C_n=\sum_{l<j\le n}c_j,\qquad W=C_r,\qquad
F_n=\min(C_n,W-C_n)\quad(l\le n\le r).
\tag{5}
\]
Then \(F_l=F_r=0\), \(F_n\ge0\), and
\[
|F_n-F_{n-1}|\le c_n.
\tag{6}
\]
Indeed \(f_W(x)=\min(x,W-x)\) is 1-Lipschitz on \([0,W]\).
This includes a capacity step crossing \(W/2\): that increment
can be partially used, instead of requiring an exact partition of
unequal weights into two halves. Zero capacities force zero increments.

The area has the uniform lower bound
\[
\boxed{\sum_{n=l}^{r-1}F_n\ge\frac{W^2}{4M}-\frac W2.}
\tag{7}
\]
To see the discretization cost explicitly, Lipschitz continuity gives
\[
\int_{C_{n-1}}^{C_n}f_W(x)\,dx
\le c_n f_W(C_n)+\tfrac12c_n^2.
\]
Sum over \(n\), use \(\int_0^W f_W=W^2/4\),
\(c_n\le M\), and \(\sum c_n^2\le MW\). The sums of
\(F_n\) over \(l<n\le r\) and \(l\le n<r\) coincide,
since both endpoint values are zero. This proves (7).
The bound need not be positive for one heavy atom; the actual
primitive is zero in that case, as it must be.

Now partition an integer interval \([p,r]\) into \(k\ge1\) cells,
use (5) on each, and join their zero endpoint values. If \(W_j\)
is the capacity in cell \(j\), and \(W_*\) the total capacity,
then Cauchy–Schwarz and (7) give
\[
\mathcal A:=\sum_{n=p}^{r-1}F_n
\ge\frac1{4M}\sum_{j=1}^kW_j^2-\frac{W_*}{2}
\ge\frac{W_*^2}{4Mk}-\frac{W_*}{2}.
\tag{8}
\]
In particular,
\[
k\le\frac{W_*}{4M}
\quad\Longrightarrow\quad
\mathcal A\ge\frac{W_*^2}{8Mk}.
\tag{9}
\]
Only total capacity and the largest allowed increment enter this
estimate. No density or positive-capacity hypothesis is imposed in
an individual cell.

## 2. Insert the actual prime weights and all observed endpoints

Since \(\phi\ne0\) is compactly supported, its derivative is
nonzero somewhere. By continuity choose the fixed \([s,t]\), a
unit complex number \(\omega\), and \(\eta>0\) so that
\[
\operatorname{Re}(-\omega\phi'(u))\ge\eta\quad(s\le u\le t).
\tag{10}
\]
Put \(p=\lceil sX\rceil\), \(r=\lfloor tX\rfloor\), and
partition \([p,r]\) at every distinct queried endpoint strictly
inside it. There are \(k\le2q+1\) cells. Use
\[
c_n=a_n/2,\qquad M=\tfrac12\log(3X),\qquad
W_*=\tfrac12\bigl(\psi(r;5,1)-\psi(p;5,1)\bigr).
\tag{11}
\]
All modified indices are below \(3X\), so \(c_n\le M\).
The unconditional fixed-modulus prime number theorem gives
\[
\psi(y;5,1)=y/4+o(y),\qquad
W_*=(t-s)X/8+o(X).
\tag{12}
\]
For example, [Granville's course notes, Section 11.9,
equation (11.9.1)](https://dms.umontreal.ca/~andrew/Courses/Chapter11.pdf),
source 147, imply this: for a fixed modulus any possible exceptional
real-zero term has exponent strictly below one and is \(o(y)\).
No GRH or shrinking-interval prime asymptotic is used.

For explicit bookkeeping set \(d_0=(t-s)/16\). For all sufficiently
large \(X\), \(W_*\ge d_0X\). Taking
\(\kappa_\phi=d_0/8\) and increasing the onset ensures that (2)
implies
\[
k\le2q+1\le\frac{d_0X}{2\log(3X)}\le\frac{W_*}{4M}.
\tag{13}
\]
Extend the joined primitive \(F\) by zero outside \([p,r]\) and
put \(d_n=F_n-F_{n-1}\). Equation (6) proves the relative bound.
The primitive is zero at every queried endpoint, including those
outside the modified interval; thus
\[
\sum_{u_\ell<n\le v_\ell}d_n=F_{v_\ell}-F_{u_\ell}=0.
\tag{14}
\]
Its compact support gives \(\sum d_n=0\). This handles repeated
endpoints, empty prime-support cells, and queries crossing the whole
modified block. Positivity and unchanged support in (4) follow
immediately from \(|d_n|\le a_n/2\).

## 3. The signed target detects the hidden area

Discrete summation by parts yields
\[
\sum_n d_n\phi(n/X)
=-\sum_{n=p}^{r-1}F_n
       \bigl(\phi((n+1)/X)-\phi(n/X)\bigr).
\tag{15}
\]
Every unit cell in this sum is inside \([sX,tX]\). Therefore (10),
nonnegativity of \(F\), and (9) imply
\[
\operatorname{Re}\left(\omega\sum_n d_n\phi(n/X)\right)
\ge\frac\eta X\mathcal A
\ge\frac{\eta W_*^2}{8XMk}
\ge\frac{\eta d_0^2}{8}\frac{X}{(q+1)\log(3X)}.
\tag{16}
\]
Here \(M=\log(3X)/2\) and \(k\le2(q+1)\).
This proves (3) with \(c_\phi=\eta d_0^2/8\). There is no
cancellation assumption on a complex target: the primitive lies
where one fixed rotated derivative has a positive lower bound.

An estimator using only the query responses and the declared support
and amplitude constraints receives identical data for \(b^+\) and
\(b^-\). Its larger absolute error is at least half their separation,
even if it is nonlinear. For a deterministic adaptive strategy with
at most the number of queries in (2), first run it on the actual
baseline \(a\), then construct \(d\) from that transcript's
endpoints. Induction over the queries gives the identical transcript
on both controls. This is a deterministic worst-case statement over
the reweighted class, not a randomized lower bound or a restriction
on an algorithm allowed to use the exact coefficients themselves.

## 4. What this closes, and what it leaves open

For any fixed \(0<\delta<1/2\),
\(q\le X^{1/2-\delta}\) satisfies (2) eventually, and the hidden
target separation is
\(\gg_\phi X^{1/2+\delta}/\log(3X)\).
Thus exact prime-power support, positivity, the relative envelope
\(a_n/2\le b_n\le3a_n/2\), and compatibility of all queried windows with
one source do not suffice for a uniform square-root recovery bound
from this many interval values over that class.

[[research/prime_lattice/findings/PL-477-common-mask-paired-windows-retain-quadratic-deletion-ambiguity|PL-477]]
already establishes signed ambiguity for fixed positive sources on an
entire residue class. The additional restriction settled here is the
**actual prime-power support with bounded relative reweighting** and
arbitrary interval queries. Unlike PL-477, this argument does not
make the common observed energies small: they equal the actual
baseline energies, whatever those are. It therefore neither proves
nor refutes the sample-energy ceilings in
[[research/prime_lattice/findings/PL-478-geometric-coverage-retains-sparsely-sampled-prime-variance|PL-478]].

The positive finite-Weil compression in
[[research/prime_lattice/findings/PL-270-finite-weil-source-positive-compression|PL-270]]
has a different observation map and no such relative-amplitude
constraint or signed-target rate. The full-tower uniqueness in
[[research/prime_lattice/findings/PL-271-full-weil-source-tower-projective-identifiability|PL-271]]
does not conflict with a finite list of interval observations.

The logarithm comes from the coarse maximum-capacity estimate in
(8); its necessity is not established. Neither an optimal prime
sample count nor a prime-specific deletion exponent follows. The
controls are reweighted measures, not alternative rational-prime
systems; canonical Dirichlet \(L\)-function Euler factors are not
imposed on them. For any one fixed control the finite alteration
does leave the eventual prefix sum equal to the baseline; its
Dirichlet-series perturbation is entire. That elementary observation
does not give estimates uniform over the scale-dependent controls,
a completed functional equation, or the pole-isolating asymptotic
at the very scale where the alteration was inserted. No change to
RH or joint GRH is asserted.

## Prior art and validation

Indistinguishable inputs, tent primitives, and the deterministic
adaptivity argument are classical optimal recovery; see
[Foucart (2022), Chapter 11](https://doi.org/10.1017/9781009003933.017),
source 146. The weighted construction is an elementary specialization,
not a new general recovery theorem. The prime number theorem supplies
only the total capacity in one fixed proportional interval. The local
mathematical addition is the quantitative support-and-relative-weight
control (3)–(4), which answers the remaining support question without
assuming prime counts inside the observation cells. No external
priority is claimed.

An auxiliary exact rational check verified (5)–(9), the increment and
endpoint bounds, and the affine-test summation-by-parts identity for
all 27,993 capacity/partition cases of lengths 1 through 6 with
capacities in \(\{0,1/2,2\}\). A further 400 sparse rational
source cases (seed 479), containing 5,755 interval queries, checked
both positive controls against the same baseline, exact support,
relative bounds, total mass, and query agreement; endpoints outside
the modified block and repeated endpoints were included. These
checks establish finite bookkeeping only. The displayed proof,
together with the cited unconditional PNT, proves the asymptotic
claim. No Lean verification or independent adversarial approval is
claimed.
