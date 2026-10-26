# PL-477 — A common mask leaves quadratic ambiguity in paired smooth window tests

**Evidence/status:** EXACT-DERIVED / NEGATIVE CONTROL;
CLASSICAL OPTIMAL-RECOVERY MECHANISM; NO EXTERNAL NOVELTY CLAIM.
The sources below are positive residue-supported, integer-indexed sequences,
not von Mangoldt coefficients. No prime deletion threshold is proved optimal.

## Claim and the hypothesis this tests

Fix any nonzero complex
\(\varphi\in C_c^\infty((4/3,5/3))\) with \(\int\varphi=0\),
and fix \(1/2<\gamma<1\). There are **two fixed sequences**
\(b_n^+,b_n^-\), an unbounded integer scale set \(\mathcal X\),
and common masks \(E_X\subset I_X=\{X,\ldots,2X-1\}\) with
\(B_X=|E_X|\asymp X^\gamma=o(X)\), having the following properties.

Both sequences vanish off \(n\equiv1\pmod5\), are strictly positive
on that residue for \(n\ge6\), and satisfy
\[
0\le b_n^\pm\le3/2,\qquad
\sum_{n\le x}b_n^\pm=x/4+O(x^\gamma).
\tag{1}
\]
They may also be chosen to satisfy \(b_n^\pm\le\log n\) for
every positive integer \(n\). Put
\[
H_X=\lfloor X/20\rfloor,\qquad
K_X=\lfloor\sqrt2H_X\rfloor,\qquad
S_L^\pm(j)=\sum_{j<n\le j+L}b_n^\pm.
\]
For **both** \(L=H_X,K_X\), the same mask gives
\[
S_L^+(j)=S_L^-(j)\quad(j\in I_X\setminus E_X),\qquad
\sum_{j\in I_X\setminus E_X}|S_L^\pm(j)-L/4|^2
\le\frac{25}{16}X.
\tag{2}
\]
The retained empirical means also coincide, and their centered energies
are no larger. Nevertheless, for
\(T_\pm(X)=\sum_n b_n^\pm\varphi(n/X)\),
\[
|T_+(X)-T_-(X)|\asymp_\varphi B_X^2/X,
\qquad |T_\pm(X)|\asymp_\varphi B_X^2/X.
\tag{3}
\]
These assertions hold at every sufficiently large \(X\in\mathcal X\).
The sources, target, scales and masks are fixed families, not new
sources chosen independently at each scale.

Thus even all retained values of two windows from one source, common
masks, positivity, the correct leading residue density, and uniformly
bounded endpoint jumps do not recover a prescribed signed smooth test
with error \(o(B_X^2/X)\) in this source class. This addresses the
generic signed-test escape left open by
[[research/prime_lattice/findings/PL-476-trimmed-paired-prime-variance-retains-the-grh-obstruction|PL-476]].
It does not decide that escape with additional prime arithmetic.

## 1. One balanced packet and two positive completions

There is \(u_0\in(4/3,5/3)\) with \(\varphi'(u_0)\ne0\):
a smooth compactly supported function with identically zero derivative
would be zero. Take \(X_k=10^k\), starting at a sufficiently large
fixed \(k_0\), and set
\[
m_k=\lfloor X_k^\gamma\rfloor,\qquad
N_k=5\left\lfloor\frac{u_0X_k-1}{5}\right\rfloor+1.
\]
Thus \(N_k\equiv1\pmod5\) and \(|N_k-u_0X_k|<5\).
Define the packet
\[
d_{N_k+5\ell}=
\begin{cases}
1/4,&0\le\ell<m_k,\\
-1/4,&m_k\le\ell<2m_k,
\end{cases}
\tag{4}
\]
and put \(d_n=0\) elsewhere. The packet intervals are disjoint
after increasing \(k_0\). Each has total mass zero. Let
\[
b_n^0=\tfrac54\mathbf1_{n\equiv1\ (5),\ n\ge6},\qquad
b_n^\pm=b_n^0\pm d_n.
\tag{5}
\]
On a packet the two positive values are \(1\) and \(3/2\);
elsewhere on the residue the value is \(5/4\). At \(n=1\)
the value is zero, so the logarithmic envelope also holds.

Completed packets contribute zero to a partial sum. At most one
unfinished packet contributes at any \(x\), with magnitude at most
\(m_k/4=O(x^\gamma)\) when \(x\) intersects it. Since
\(\sum_{n\le x}b_n^0=x/4+O(1)\), this proves (1).
This leading-density assertion does not assert a Dirichlet Euler
product, meromorphic continuation, or a specified zero divisor.

## 2. Hide both endpoint images in the same mask

Fix \(X=X_k\), abbreviate \(m=m_k,N=N_k\), and let
\[
Q=\{N,N+1,\ldots,N+10m-1\},\qquad
E_X=Q\cup(Q-H_X)\cup(Q-K_X).
\tag{6}
\]
For large \(k\), these are disjoint subsets of \(I_X\), because
\(10m=o(X)\), \(u_0\in(4/3,5/3)\), and the three displacement
differences are positive constants times \(X\). In particular
\(B_X=30m<X/2\) eventually.

Write \(D(t)=\sum_{n\le t}d_n\). On \([X,3X]\) only the
current packet can contribute, and \(D(t)=0\) for integer
\(t\notin Q\). Earlier packets have total mass zero, and later
packets lie beyond \(3X\). The exact window perturbation is
\[
S_L^\pm(j)-S_L^0(j)=\pm\{D(j+L)-D(j)\}.
\tag{7}
\]
For \(j\notin E_X\) and either stated length, both terms vanish.
Thus the retained data agree exactly with the *same* unperturbed
sequence, proving the first assertion of (2).

An interval of integer length \(L\) contains either
\(\lfloor L/5\rfloor\) or \(\lceil L/5\rceil\) integers in
the selected residue. Consequently
\[
|S_L^0(j)-L/4|\le5/4,
\]
which proves the energy bound. The empirical mean minimizes the sum
of squared distances to a constant, so changing to it preserves the
bound. Since the entire retained vectors agree, these means agree too.

The endpoint identity and jump envelope are also exact:
\[
S_L^\pm(j+1)-S_L^\pm(j)
=b_{j+L+1}^\pm-b_{j+1}^\pm,\qquad
|S_L^\pm(j+1)-S_L^\pm(j)|\le3/2.
\tag{8}
\]
There is therefore no logarithmically growing jump cost hidden in
this counterexample.

## 3. A signed smooth test still sees the packet's first moment

Only the current packet intersects the support of \(\varphi(n/X)\).
Its contribution is
\[
q_X:=\sum_n d_n\varphi(n/X)
=\frac14\sum_{\ell=0}^{m-1}
\left[
\varphi\left(\frac{N+5\ell}{X}\right)
-\varphi\left(\frac{N+5(\ell+m)}{X}\right)
\right].
\]
Taylor's theorem, \(|N-u_0X|<5\), and \(m=o(X)\) give
\[
q_X=-\frac54\varphi'(u_0)\frac{m^2}{X}
       +O_\varphi(m^3/X^2).
\tag{9}
\]
Indeed each difference has displacement \(5m/X\), and throughout
the packet the derivative differs from \(\varphi'(u_0)\) by
\(O_\varphi(m/X)\). The nonzero leading coefficient is preserved
for complex tests as well as real ones. Equivalently the packet has
exact zeroth moment zero and first moment
\(\sum_n n d_n=-5m^2/4\).

For the periodic background, a Riemann-sum estimate on the mesh
\(5/X\) gives
\[
T_0(X):=\sum_n b_n^0\varphi(n/X)
=\frac X4\int\varphi(u)\,du+O_\varphi(1)=O_\varphi(1).
\tag{10}
\]
For example the error is bounded by a constant times
\(\int|\varphi'|\), by integrating the difference between the
sample and function over each mesh cell. There is no assumption of
random phases or cancellation of a zero-mode cosine.

Now \(T_\pm=T_0\pm q_X\). Since \(m^2/X\to\infty\) for
\(\gamma>1/2\), (9)--(10) prove both parts of (3), with
\[
T_+(X)-T_-(X)
=-\frac52\varphi'(u_0)\frac{m^2}{X}
  +O_\varphi(m^3/X^2).
\tag{11}
\]
If desired, a mean-zero compact smooth test can be chosen affine
with slope one near \(u_0\), by multiplying \(u-u_0\) by a
symmetric bump equal to one there. For that test the packet formulas
in (9) and (11) are exact once the packet is inside the affine region.

## 4. Recovery consequence and the arithmetic boundary

Any estimator using only the two retained window vectors and the
known common mask receives identical inputs from \(b^+\) and
\(b^-\). By the triangle inequality its larger error on these two
sources is at least \(|T_+-T_-|/2\). Thus the ambiguity is
\(\gg_\varphi B_X^2/X\), even for nonlinear estimators and even
when the chosen smooth test is known in advance.

Writing \(W_L\) for either retained energy in (2), at macroscopic
lengths the energy term used in PL-476 is
\(\sqrt{XW_L}/L=O(1)\) for these sources. Replacing its deletion
cost by \(o(B_X^2/X)\) would therefore fail. In particular no fixed
power saving \(B_X^{2-\delta}(\log X)^A/X\), with
\(\delta>0\) and finite fixed \(A\), can hold uniformly in this
class. This establishes the necessity of the **quadratic power** in
generic recovery, not the necessity of PL-476's prime logarithm.

For \(\gamma>3/4\), the hidden response
\(B_X^2/X\asymp X^{2\gamma-1}\) exceeds square-root size while
both retained energies remain \(O(X)\) and the common mask has
density zero. Signed tests, shared-source consistency, and using the
same exceptional set for both channels cannot by themselves justify
extending the square-root recovery allowance to such deletion powers.
The mask was allowed to correlate with the source, as in PL-476;
random or externally constrained masks are a different problem.

This does **not** refute a prime-specific improvement or a GRH
criterion with another argument. The coefficients are supported on
an entire residue class, not on prime powers, and no arithmetic
explicit formula, pole growth, or zero-density hypothesis is supplied.
In particular (11) is not the pure pole formula in PL-471.
The exact paired deconvolution in PL-475 concerns complete data and
is fully consistent with this ambiguity after deletion. The proposed
single-box sparse Mellin interpolation question remains undecided.

## Prior art and validation

Indistinguishable inputs with different linear outputs are the
classical lower-bound mechanism of optimal recovery. See
[Foucart (2022), Chapters 9 and 11](https://doi.org/10.1017/9781009003933.015),
especially the latter chapter's treatment of integration of Lipschitz
functions ([chapter DOI](https://doi.org/10.1017/9781009003933.017)),
source 146. The balanced packet's primitive is a discrete tent; neither
tent-function lower bounds nor their quadratic area are new principles.
For the prime-specific comparison,
[Bazzanella--Perelli (2000)](https://doi.org/10.1006/jnth.1999.2429),
source 145, studies exceptional-set inertia for primes in short
intervals. No prime exceptional-set theorem is imported here.

The local addition is simultaneous realization of the obstruction by
two fixed positive sources with the same leading residue density,
the same common mask, both prescribed macroscopic lengths, and a
prescribed signed smooth target. It excludes a generic improvement
from these extra inputs; it does not claim external priority or new
arithmetic information.

An auxiliary exact integer/rational check (seed 477) covered 120
packets and 240 paired-channel comparisons. It verified the common
mask cardinality, retained-vector equality for both signs and the
baseline, positivity, endpoint identity, retained energy bound,
zero packet mass, first moment, and exact affine-test difference.
The derivation above proves the infinite fixed-source construction
and the arbitrary smooth-test asymptotic; the finite check establishes
neither of those by numerical extrapolation. No Lean verification or
independent adversarial approval is claimed.
