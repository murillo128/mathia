# MC-541 — Optimal prescribed-prime moments still force lacunarity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`,
`NO-NOVELTY-CLAIM`. This is a boundary of a uniform second-moment
proof method, not a lower bound for Möbius or for actual window energies.

## Question and exact answer

[MC-538](MC-538-one-fixed-multiplicative-source-defeats-subquarter-random-observations.md)
constructs one multiplicative comparator by prescribing balanced prime
blocks and randomizing the remaining primes. Its uniform weighted
second-moment estimate loses a factor exponential in the number of old
prescribed primes, absorbed by choosing the next scale very large.
Can optimizing that factor permit dense scales in the same argument?

The best factor is an exact truncated divisor count. It can be smaller
than the crude factor, but the immediately preceding block already
forces a power-size loss at comparable scales. Subtracting the random
expectation does not remove this obstruction.

Let \(A,Z\) be disjoint finite sets of primes. Prescribe
\(b_p\in\{-1,1\}\) on \(A\), set prime values to zero on \(Z\),
and assign independent Rademacher signs at every other prime. Extend
multiplicatively to square-free integers, set nonsquare-free values
to zero, and call the resulting function \(g\), with \(g(1)=1\).
Write
\[
 Q_A=\prod_{p\in A}p,\qquad
 b(d)=\prod_{p\mid d}b_p\quad(d\mid Q_A),\qquad
 D_A(t)=\#\{d\mid Q_A:d\le t\}.
\tag{1}
\]
In particular \(D_A(t)=0\) for \(t<1\). Let \(q_0\) be the
smallest prime outside \(A\cup Z\). For every integer \(N\ge1\),
the optimal constants, uniformly over complex deterministic weights
\(v_1,\ldots,v_N\), are
\[
 \boxed{\sup_{v\ne0}
 \frac{\mathbb E|\sum_{n\le N}v_ng(n)|^2}
      {\sum_{n\le N}|v_n|^2}=D_A(N),}
\tag{2}
\]
\[
 \boxed{\sup_{v\ne0}
 \frac{\mathbb E|\sum_{n\le N}v_ng(n)
                 -\mathbb E\sum_{n\le N}v_ng(n)|^2}
      {\sum_{n\le N}|v_n|^2}=D_A(N/q_0).}
\tag{3}
\]
The weights may depend on the prescribed signs, but not on the random
signs. Equation (3) is centering over the prime-sign ensemble; it is
not empirical centering over window starts.

## 1. Orthogonal free parts and the sharp constants

Every surviving square-free integer has a unique decomposition
\(n=dm\), with \(d\mid Q_A\) and \(m\) square-free and avoiding
all primes in \(A\cup Z\). If \(\epsilon(m)\) is the product
of its free prime signs, then
\[
 T_v:=\sum_{n\le N}v_ng(n)
 =\sum_{\substack{m\le N\text{ square-free}\\
                   p\mid m\Rightarrow p\notin A\cup Z}}
       \epsilon(m)\sum_{\substack{d\mid Q_A\\d\le N/m}}
                          b(d)v_{dm}.
\tag{4}
\]
Distinct free parts give orthogonal Rademacher characters, including
the constant character \(m=1\). Therefore
\[
 \mathbb E|T_v|^2
 =\sum_m\left|\sum_{d\mid Q_A,\ d\le N/m}b(d)v_{dm}\right|^2.
\tag{5}
\]
Each inner sum contains \(D_A(N/m)\le D_A(N)\) terms. Apply
Cauchy–Schwarz within each group; uniqueness of \(n=dm\) means
each surviving coefficient norm is counted once. This proves the
upper bound in (2).

For equality, take \(v_d=b(d)\) on \(d\mid Q_A\), \(d\le N\),
and zero elsewhere. Then \(T_v=D_A(N)\) deterministically and
\(\sum|v_n|^2=D_A(N)\). Thus no sign balance among the prescribed
primes improves the uniform constant.

The expectation of (4) is exactly its \(m=1\) term. After removing
it, every remaining free part is at least \(q_0\), proving the
upper bound in (3). If \(q_0\le N\), equality follows from
\[
 v_{q_0d}=b(d)\quad(d\mid Q_A,\ d\le N/q_0),
 \qquad v_n=0\text{ otherwise}.
\tag{6}
\]
Now \(T_v=\epsilon(q_0)D_A(N/q_0)\), which already has mean
zero. If \(q_0>N\), all surviving values are deterministic and
both sides of (3) are zero.

On surviving coordinates, the second-moment matrix decomposes into disjoint signed
rank-one blocks, one for each free part \(m\), whose nonzero
eigenvalue is \(D_A(N/m)\). The covariance matrix deletes only the
\(m=1\) block. This is classical orthogonality and finite linear
algebra, not a new random-multiplicative moment principle.

## 2. The preceding block forces logarithmic scale separation

Use the precise setup of MC-538: \(A=A_{<k}\) consists of all old
prescribed primes, \(Z=P_k\) is the current zeroed block, and
\[
 N_k=2X_k-1+\lfloor\sqrt2\lfloor X_k/20\rfloor\rfloor.
\tag{7}
\]
All engineered primes exceed two, so \(q_0=2\). MC-538's preceding
block obeys, for fixed \(3/4<\kappa<1\),
\[
 |P_{k-1}|\gg_\phi
       X_{k-1}^{\kappa}/\log X_{k-1},\qquad
 P_{k-1}\subset(4X_{k-1}/3,5X_{k-1}/3).
\tag{8}
\]
Its scale separation \(X_k>3X_{k-1}\) puts every prime in that
block below \(N_k/2\). Hence the exact uncentered and centered
constants satisfy
\[
 D_{A_{<k}}(N_k)\ge D_{A_{<k}}(N_k/2)
 \ge1+|P_{k-1}|
 \gg_\phi X_{k-1}^{\kappa}/\log X_{k-1}.
\tag{9}
\]
Suppose this uniform bound is required to have loss at most
\(X_k^{\eta_k}\), with \(\eta_k>0\), \(\eta_k\to0\).
Even with the *optimal* constant in either (2) or (3), necessarily
\[
 \eta_k\log X_k
 \ge\kappa\log X_{k-1}-\log\log X_{k-1}+O_\phi(1),
\]
\[
 \boxed{\frac{\log X_k}{\log X_{k-1}}
       \ge\frac{\kappa-o(1)}{\eta_k}\longrightarrow\infty.}
\tag{10}
\]
In particular MC-538's requirement that the moment loss divided by
\(\delta_k<1\) be at most \(X_k^{1/k}\) still forces a ratio
at least \(k(\kappa-o(1))\). Replacing \(2^{|A_{<k}|}\) by its
best possible uniform substitute cannot give a bounded logarithmic
scale ratio, let alone a ratio tending to one. This conclusion is
about that proof architecture; it is not an impossibility theorem for
dense-scale multiplicative comparators.

## 3. Small prime harmonic mass does not repair this norm

There is also a simple finite control against replacing the loss by
a bound uniform over prescriptions with \(\sum_{p\in A}1/p\le1\).
Fix \(0<\kappa<1\). For large integer \(Y\), the ordinary PNT
allows an even number \(r\asymp Y^\kappa\) of primes in
\((Y,2Y]\). Take these as \(A\), give half each sign, and take
\(Z=\varnothing\), \(N=4Y\). Products of two selected primes
exceed \(N\), so
\[
 D_A(N)=D_A(N/2)=1+r,\qquad
 \sum_{p\in A}\frac1p\le\frac rY\longrightarrow0.
\tag{11}
\]
Thus the same balanced prescriptions have vanishing harmonic mass
but diverging optimal constants for both moments. This is not a
counterexample to a pretentious mean-value theorem: those theorems
do not assert (2) for every sign-matched coefficient vector.

## Prior art, validation, and surviving question

[O'Donnell, Theorem 1.5](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf)
(MC-S94) gives the classical orthonormality of Boolean parity
characters used in (5).
[Harper, Section 1](https://msp.org/ant/2019/13-10/ant-v13-n10-p02-s.pdf)
(MC-S88) specifies the standard square-free Rademacher multiplicative
model. The only prime-supply input for (11) is the ordinary
[PNT](https://dlmf.nist.gov/27.12) (MC-S89).
These sources support the standard ingredients; no external novelty
claim is made for the matrix calculation or its specialization.

Internally, MC-538 already gives (4)–(5) and its crude bound.
[MC-120](MC-120-fixed-function-lacunary-fractional-moment-barrier.md)
also absorbs finite prime prescriptions through lacunarity. The
additional conclusion here is that optimal **uniform weighted**
second moments still force (10), even after ensemble centering.
This rules out optimizing that coefficient alone as the missing
dense-scale repair of the current construction.

Exact finite checks used every assignment of six primes
\(\{2,3,5,7,11,13\}\) to free, zero, prescribed-positive or
prescribed-negative states: 4,096 configurations, with horizons
\(1,2,3,5,8,15\). Exhaustive averaging over the remaining random
signs checked 1,343,488 second-moment matrix entries, 98,304 weighted
moment identities/bounds and 49,152 norm witnesses, including empty
sets, zero covariance and the centered \(q_0\)-fibre. These are finite
bookkeeping checks; the proof gives (2)–(11). No formal verification
or independent adversarial approval is asserted.

The extremizing weights in (6) select and align an arithmetic fibre.
They generally are neither interval indicators nor the fixed smooth
weights in the intended application. Consequently this finding does
**not** lower-bound the actual complete background energy in MC-538,
exclude cancellation inside its interval-specific inner sums in (5),
or show that a favorable random realization cannot exist. A dense
construction would need to estimate those particular inner sums,
remove several coherent blocks with a separately controlled cost, or
use a different selection argument. MC-540's every-scale nonmultiplicative
control does not supply that missing input. No Möbius estimate or
optimality of fourth-power sampling follows. The finite rank-one
calculation alone supplies no separate high-value formalization target.
