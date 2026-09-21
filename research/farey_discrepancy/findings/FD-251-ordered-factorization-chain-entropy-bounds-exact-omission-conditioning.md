# FD-251 — Ordered-factorization chain entropy bounds exact omission conditioning

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / weighted incidence inversion / induced-poset Möbius coefficients / ordered factorizations / universal conditioning upper bound
- **Depends on:** FD-225, FD-245, FD-248, FD-249, FD-250
- **Classification:** `EXACT-DERIVED + UNIVERSAL-CONDITIONING-UPPER-BOUND + ORDERED-FACTORIZATION-BARRIER + SUBPOLYNOMIAL-DEFECT-COERCIVITY`

## Claim

Let `D` be any finite subset of `{1,...,N}` and let

\[
\kappa(D)
=
\max_{d\in D}
\sum_{\substack{q\in D\\q\mid d}}
|\mu_D(q,d)|\frac qd
\]

be the weighted incidence-Möbius inverse norm from FD-248, where `mu_D` is the Möbius function of the induced divisibility poset on `D`.

Let `rho_* > 1` be the unique real solution of

\[
\zeta(\rho_*)=2,
\qquad
\rho_*=1.7286472389\ldots .
\]

Then for every fixed `epsilon>0`, uniformly over every such `D`,

\[
\boxed{
\kappa(D)
\ll_{\epsilon}
N^{\rho_*-1+\epsilon}.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\kappa(D)
\le N^{\rho_*-1+o(1)}
}
\tag{2}
\]

uniformly as `N -> infinity`.

Combining (1) with FD-248 gives a genuine exact-omission coercivity window. If

\[
Y(m)=(\mathscr A b)(m),
\qquad
|b_n|\le C_b n,
\]

is zero at all but `K` samples up to `N`, then

\[
\boxed{
\sum_{n\le N}|b_n|
\ll_{\epsilon}
C_b K N^{\rho_*+\epsilon}.
}
\tag{3}
\]

Consequently, if

\[
K\le N^{\alpha+o(1)}
\qquad\text{for some}\qquad
\alpha<2-\rho_*=0.2713527610\ldots,
\]

then

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\longrightarrow0.
}
\tag{4}
\]

In particular, every exact-omission family with

\[
K=N^{o(1)}
\]

is coercive at coefficient-capacity scale, independently of the omission locations and independently of how complicated the induced merge geometry becomes.

This settles the subpolynomial-defect branch left open by FD-250: alternating rank merges can make `kappa(D)` larger than every fixed power of `log log N`, but no exact omission geometry with `K=N^{o(1)}` can amplify enough to reach the `N/K` scale that FD-248 requires for macroscopic hidden coefficient mass.

The result is still response-side. It does not impose positivity, finite prime-reservoir capacity, squarefree physical-source realization, or full Möbius coherence, and it does not treat approximate residuals.

## Möbius coefficients are bounded by strict divisibility chains

Fix `q,d in D` with `q|d`. For `q<d`, the incidence-algebra chain expansion gives

\[
\mu_D(q,d)
=
\sum_{\ell\ge1}
(-1)^\ell
C_\ell(q,d),
\tag{5}
\]

where `C_ell(q,d)` is the number of strict chains

\[
q=x_0<x_1<\cdots<x_\ell=d
\]

inside the induced divisibility poset `D`. Hence

\[
|\mu_D(q,d)|
\le
\sum_{\ell\ge1}C_\ell(q,d).
\tag{6}
\]

Put

\[
r=\frac dq.
\]

Every strict divisibility chain determines an ordered factorization

\[
r
=
\frac{x_1}{x_0}
\frac{x_2}{x_1}
\cdots
\frac{x_\ell}{x_{\ell-1}},
\tag{7}
\]

and every factor in (7) is an integer at least `2`. The ordered list of ratios recovers the chain uniquely, so this map is injective.

Let `H(r)` denote the number of ordered factorizations of `r` into factors greater than `1`, with `H(1)=1`. Then (6)-(7) imply the universal pointwise majorant

\[
\boxed{
|\mu_D(q,d)|
\le
H(d/q).
}
\tag{8}
\]

No property of the exact-omission companion pairs has been used here. The estimate holds for every finite induced divisibility poset.

## The ordered-factorization exponent appears by a one-line induction

The function `H` satisfies, for `n>1`,

\[
H(n)
=
\sum_{\substack{a\mid n\\a\ge2}}
H(n/a).
\tag{9}
\]

Because `zeta(s)` decreases continuously from infinity to `1` on `(1,infinity)`, there is a unique `rho_*>1` with `zeta(rho_*)=2`, equivalently

\[
\sum_{a\ge2}a^{-\rho_*}=1.
\tag{10}
\]

Inducting on `n` in (9), and using that every `n/a<n`, gives

\[
\begin{aligned}
H(n)
&\le
\sum_{\substack{a\mid n\\a\ge2}}
(n/a)^{\rho_*}\\
&\le
n^{\rho_*}
\sum_{a\ge2}a^{-\rho_*}\\
&=
n^{\rho_*}.
\end{aligned}
\tag{11}
\]

Thus

\[
\boxed{H(n)\le n^{\rho_*}}
\tag{12}
\]

for every `n>=1`.

The exponent `rho_*` is classical in the `factorisatio numerorum` / ordered-factorization problem. Chor, Lemke and Mador proved the strict bound `H(n)<n^{rho_*}`, and Klazar--Luca later studied the much finer maximal order. The argument above rederives the only inequality needed here, so no external ordered-factorization theorem is load-bearing for (1).

## Transfer to the weighted incidence inverse

Fix `d in D`. From (8) and (12), including the diagonal `q=d` through `H(1)=1`,

\[
\begin{aligned}
\sum_{\substack{q\in D\\q\mid d}}
|\mu_D(q,d)|\frac qd
&\le
\sum_{q\mid d}
H(d/q)\frac qd\\
&=
\sum_{r\mid d}
\frac{H(r)}r\\
&\le
\sum_{r\mid d}r^{\rho_*-1}\\
&\le
\tau(d)d^{\rho_*-1}.
\end{aligned}
\tag{13}
\]

For completeness, the standard elementary divisor bound needed here can be proved without importing any analytic number theory. For fixed `epsilon>0`, choose `P=2^{1/epsilon}`. If `p>P`, then for every exponent `a>=0`,

\[
a+1\le2^a\le p^{\epsilon a}.
\]

For the finitely many primes `p<=P`, the quantities

\[
\sup_{a\ge0}(a+1)p^{-\epsilon a}
\]

are finite and can be absorbed into a constant depending only on `epsilon`. Therefore

\[
\tau(d)\ll_\epsilon d^\epsilon.
\tag{14}
\]

Substituting (14) into (13), and using `d<=N`, proves (1).

A slightly more informative intermediate form is

\[
\boxed{
\kappa(D)
\le
\max_{d\in D}
\sum_{r\mid d}\frac{H(r)}r
\le
\max_{d\in D}\sigma_{\rho_*-1}(d).
}
\tag{15}
\]

Thus the universal obstruction to arbitrarily bad exact-omission conditioning is not poset depth or merge arity by itself. It is the multiplicative entropy of the integer ratio available between two comparable nodes.

## Consequence for exact omissions

FD-248 proves that if an exact response has `K` omitted samples and coefficient envelope `|b_n|<=C_b n`, then with

\[
D=\operatorname{supp}(\Delta Y)\cap[1,N]
\]

one has `|D|<=2K` and

\[
\sum_{n\le N}|b_n|
\le
C_b N|D|\kappa(D)
\le
2C_b NK\kappa(D).
\tag{16}
\]

Applying (1) gives (3). Since

\[
\sum_{N/2<n\le N}n\asymp N^2,
\]

we obtain

\[
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll_\epsilon
C_b K N^{\rho_*-2+\epsilon}.
\tag{17}
\]

If `K<=N^{alpha+o(1)}` with `alpha<2-rho_*`, choose fixed `epsilon>0` smaller than `2-rho_*-alpha`; the right-hand side tends to zero. This proves (4).

In the subpolynomial regime `K=N^{o(1)}`, (17) becomes simply

\[
N^{\rho_*-2+o(1)}
=
N^{-0.2713527610\ldots+o(1)},
\tag{18}
\]

so the capacity ratio decays by a fixed polynomial power.

## Relation to FD-249 and FD-250

FD-249 disproves any conditioning bound based only on shallow depth: one high-arity merge already makes `kappa(D)` unbounded. FD-250 then shows that nested alternating rank merges can create factorial incidence-Möbius coefficients and force

\[
\kappa(D_N)
\ge
(\log\log N)^{(1-o(1))\log\log\log\log N}
=
N^{o(1)}
\]

with `K=N^{o(1)}`.

The present upper bound is completely compatible with that construction but changes its interpretation. No elaboration of the same subpolynomial-defect merge mechanism can ever reach the `N/K` amplification required by FD-248. Even if the lower construction were improved from the current super-polylogarithmic scale all the way to the largest `N^{o(1)}` scale, (17) would still force its coefficient mass to be `o(N^2)`.

So the remaining response-side frontier is no longer whether subpolynomially many exact omissions can hide capacity-scale mass: they cannot. The unresolved quantitative problem is the much wider polynomial window

\[
N^{2-\rho_*+o(1)}
\lesssim
K
\ll
N,
\]

where the universal chain-count upper bound ceases by itself to imply coercivity. It is also open whether the exponent `rho_*-1` is remotely sharp for `kappa(D)`; the alternating-rank lower bound from FD-250 is still only `N^{o(1)}`.

## Stress tests and non-claims

The proof deliberately takes absolute values before counting chains. Large alternating cancellation in the incidence Möbius function can only make `kappa(D)` smaller, so (1) is safe but may be very far from optimal.

The argument also enlarges the genuine exact-omission support to an arbitrary finite `D`. It therefore ignores the special adjacent-pair structure `D subset E union (E+1)`. Any future use of that geometry can only sharpen the exponent or extend the coercive range.

Conversely, (1) says nothing about source admissibility. A small or moderate response-space inverse norm does not produce a nonnegative reservoir filling, respect finite prime capacities, enforce squarefree realization, or restore the arithmetic coherence discarded by the signed relaxation. Approximate/noisy responses remain governed by the separate residual analysis of FD-242--244.

## Prior-art audit

The chain-counting quantity in (8) is the classical ordered-factorization function. The prior-art audit found the standard `factorisatio numerorum` literature, in particular Benny Chor, Paul Lemke and Ziv Mador, *On the number of ordered factorizations of natural numbers*, Discrete Mathematics 214 (2000), 123--133, and Martin Klazar and Florian Luca, *On the maximal order of numbers in the "factorisatio numerorum" problem*, Journal of Number Theory 124 (2007), 470--490, arXiv:math/0505352. These works study `H(n)` itself and the same zeta root `rho_*`.

The load-bearing bound `H(n)<=n^{rho_*}` is rederived in (9)--(12). I did not find a prior-art statement connecting this ordered-factorization exponent to the weighted induced-divisibility Möbius norm `kappa(D)` from FD-248 or to exact omission sampling for the divisor/Mertens response. The line-specific content here is that transfer and its coercivity threshold `K<N^{2-rho_*-o(1)}`.

## Research consequence

This pass closes one of the explicit alternatives in the live FD-250 frontier. Exact omission conditioning can grow combinatorially, but multiplicative chain entropy enforces the universal ceiling

\[
\kappa(D)\le N^{\rho_*-1+o(1)}.
\]

Therefore **subpolynomially many exact omissions cannot hide macroscopic signed coefficient capacity**, no matter how the merge topology is engineered. Any response-side countermodel that aims to hide a constant fraction of capacity must now pay at least a polynomial number of omissions at the level visible to this bound, with exponent at least `2-rho_*=0.271352...` up to lower-order losses.

The next useful test is correspondingly narrower: either exploit the genuine adjacent-pair geometry to lower the universal exponent below `rho_*-1`, or construct polynomial-size exact omission families whose induced divisibility inverse approaches a positive power of `N`. Improvements confined to `K=N^{o(1)}` can no longer alter the capacity-scale conclusion.