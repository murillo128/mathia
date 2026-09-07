# MC-124 — Every fixed-memory sign-odd Möbius observable is logarithmically invisible

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix distinct integer shifts

\[
h_1,\dots,h_r,
\qquad r\ge 1,
\]

and let

\[
\Phi:\{-1,0,1\}^r\to\mathbb C
\]

be any fixed finite-window observable that is **odd under simultaneous Möbius-sign reversal**:

\[
\Phi(-x_1,\dots,-x_r)=-\Phi(x_1,\dots,x_r).
\tag{1}
\]

Then

\[
\boxed{
\sum_{n\le x}
\frac{\Phi\bigl(\mu(n+h_1),\dots,\mu(n+h_r)\bigr)}{n}
=o(\log x)
}
\qquad (x\to\infty),
\tag{2}
\]

with the finitely many terms having non-positive shifted arguments omitted.

Thus adding any **fixed amount of local memory** does not create a sign-odd feedback statistic with a nonzero logarithmic mean. Every such cylinder observable is exactly a finite linear combination of fixed-shift mixed correlations of `mu` and `mu^2`, and the Tao–Teräväinen product criterion forces every sign-odd term to vanish after logarithmic averaging.

This directly sharpens the escape identified by `MC-123`. One-symbol memory really can create a non-coboundary oriented cycle that is absent from the scalar Mertens-state tree, but the unique reversal-odd cycle class on the three-symbol increment alphabet is itself only an adjacent mixed Möbius correlation and therefore satisfies `(2)`. Fixed local memory escapes the **topological** tree obstruction without escaping the existing **fixed-correlation** information class.

No power saving for `M(x)` follows. The conclusion is qualitative and logarithmically averaged; `MC-039` and `MC-040` already show that broad families of qualitative logarithmic correlation identities can coexist with almost-linear partial sums in exact-support multiplicative controls.

## 1. Every fixed-window observable has an exact `1,x,x^2` expansion

On the three-point alphabet

\[
A=\{-1,0,1\},
\]

the functions

\[
1,\qquad x,\qquad x^2
\tag{3}
\]

form a basis of all complex-valued functions on `A`: evaluation at the three points gives an invertible Vandermonde matrix. Tensoring this basis over `r` coordinates gives an exact expansion

\[
\Phi(x_1,\dots,x_r)
=
\sum_{e\in\{0,1,2\}^r}
 c_e\prod_{j=1}^r x_j^{e_j}.
\tag{4}
\]

Under simultaneous sign reversal, the monomial indexed by `e` acquires the sign

\[
(-1)^{\nu(e)},
\qquad
\nu(e):=\#\{j:e_j=1\}.
\tag{5}
\]

The basis therefore splits into the `+1` and `-1` eigenspaces of global sign reversal. Condition `(1)` forces

\[
c_e=0
\qquad\text{whenever }\nu(e)\text{ is even}.
\tag{6}
\]

Consequently every surviving term in `(4)` has the form

\[
\prod_{j\in S}\mu(n+h_j)
\prod_{k\in T}\mu(n+h_k)^2,
\qquad |S|\text{ odd},
\tag{7}
\]

for disjoint fixed sets `S,T`.

This reduction is exact and loses no finite-window information. In particular, the zero value of Möbius is not being discarded: it is carried by the `mu^2` factors, which are precisely the square-free-support indicators.

## 2. Tao–Teräväinen kill every odd-parity monomial logarithmically

For a monomial `(7)`, assign to each active shift the multiplicative function

\[
g_j=
\begin{cases}
\mu,&j\in S,\\
\mu^2,&j\in T.
\end{cases}
\tag{8}
\]

Their pointwise product as multiplicative functions is

\[
G=\prod_j g_j
=\mu^{|S|+2|T|}
=\mu,
\tag{9}
\]

because `|S|` is odd and `mu(n)^k=mu(n)` for every positive odd integer `k`.

Tao and Teräväinen's logarithmically averaged correlation theorem (`MC-S28`) says that a fixed shifted correlation of bounded multiplicative functions vanishes logarithmically whenever their pointwise product does not weakly pretend to any Dirichlet character. Here that product is exactly Möbius.

At primes `p`, one has `mu(p)=-1`. For the principal character, the weak-pretence sum therefore has asymptotic size `2 log log x`. For every nonprincipal fixed Dirichlet character `chi`, prime-harmonic orthogonality gives

\[
\sum_{p\le x}\frac{\operatorname{Re}\chi(p)}p=O_\chi(1),
\]

so

\[
\sum_{p\le x}
\frac{1-\operatorname{Re}(\mu(p)\overline{\chi(p)})}{p}
=
\log\log x+O_\chi(1),
\tag{10}
\]

up to the harmless finitely many conductor primes. Hence `mu` does not weakly pretend to any character.

Applying `MC-S28` to `(7)` gives

\[
\sum_{n\le x}
\frac{
\prod_{j\in S}\mu(n+h_j)
\prod_{k\in T}\mu(n+h_k)^2
}{n}
=o(\log x).
\tag{11}
\]

The degenerate one-factor case is also the classical logarithmic consequence of the prime number theorem for Möbius. Summing the finitely many terms in `(4)` proves `(2)`.

The argument uses no analytic continuation of `1/zeta(s)`, no zero-free region near the critical line, and no estimate for `M(x)` stronger than the classical one-point cancellation implicit in the one-factor case.

## 3. The first memory cycle is genuine but falls inside the theorem

`MC-123` showed that an observable depending only on the scalar state `M_{n-1}` and the next increment has no oriented circulation: the Mertens-state graph is the integer line, so every reversal-odd edge field is a gradient.

Add one previous increment and look first at translation-invariant label observables on pairs

\[
(a,b)\in A^2.
\]

The antisymmetric edge space

\[
o(a,b)=-o(b,a)
\]

has dimension `3`, while label gradients

\[
o(a,b)=f(b)-f(a)
\tag{12}
\]

have dimension `2` because `f` is defined modulo constants. Thus the quotient is exactly one-dimensional.

A normalized generator is

\[
\boxed{
J(a,b)=\frac{(a-b)(2+3ab)}2.
}
\tag{13}
\]

It satisfies

\[
J(1,0)=J(0,-1)=J(-1,1)=1
\tag{14}
\]

and takes value `-1` on the reverse transitions, with zero diagonal. The circulation around the label triangle is therefore

\[
J(1,0)+J(0,-1)+J(-1,1)=3,
\tag{15}
\]

so `J` is not a label coboundary. More strongly, it is not a potential difference even after the scalar Mertens level is retained: the augmented admissible state graph contains the closed path

\[
(m,1)\to(m,0)\to(m-1,-1)\to(m,1),
\tag{16}
\]

whose `J`-sum is `3`, whereas every exact potential has zero sum around a closed path.

For any antisymmetric pair observable `o`, put

\[
c=\frac{o(1,0)+o(0,-1)+o(-1,1)}3.
\tag{17}
\]

Then `o-cJ` has zero triangle circulation and hence equals `f(b)-f(a)` for some `f:A->C`. Thus `(13)` is the **only** new antisymmetric label-cycle direction modulo endpoint coboundaries.

This is the finite `K_3` specialization of the standard gradient/cycle-space decomposition already invoked in `MC-123`; no novelty is claimed for the graph-Hodge mechanism.

## 4. The unique cycle current is an adjacent mixed correlation

The generator `(13)` has the exact polynomial form

\[
J(a,b)
=
a-b+\frac32\left(a^2b-ab^2\right).
\tag{18}
\]

Hence along the Möbius word

\[
C_N:=\sum_{n=1}^{N-1}J(\mu(n),\mu(n+1))
\tag{19}
\]

one has

\[
\boxed{
C_N
=
\mu(1)-\mu(N)
+\frac32\sum_{n=1}^{N-1}
\left(
\mu(n)^2\mu(n+1)
-
\mu(n)\mu(n+1)^2
\right).
}
\tag{20}
\]

So the first genuine circulation exposed by memory is not a new spectral or geometric carrier. It is exactly the imbalance between two adjacent mixed correlations: one places the square-free-support factor on the left, the other on the right.

The same identity also gives a transition-count interpretation:

\[
C_N
=
N_{1\to0}+N_{0\to-1}+N_{-1\to1}
-
N_{0\to1}-N_{-1\to0}-N_{1\to-1},
\tag{21}
\]

where the counts are taken over consecutive Möbius values up to `N`.

Since `J(-a,-b)=-J(a,b)`, theorem `(2)` applies directly:

\[
\sum_{n\le x}\frac{J(\mu(n),\mu(n+1))}{n}
=o(\log x).
\tag{22}
\]

One may also see `(22)` directly from `(18)`: the `mu(n)-mu(n+1)` contribution is `O(1)` after `1/n` weighting by summation by parts, while both mixed-correlation terms satisfy `MC-S28` because their product function is `mu^3=mu`.

## 5. The zero symbol is exactly what opens this first cycle

If the increment alphabet is reduced to

\[
\{-1,+1\},
\]

as in a Liouville-style no-zero model, the antisymmetric edge space has dimension `1`, and the gradient subspace also has dimension `1`. There is no antisymmetric cycle quotient.

For Möbius the square-free-support value `0` enlarges the alphabet to three states and creates the triangle in `(14)`. Thus the zero/support state is not incidental to the first finite-memory circulation: it is exactly the extra symbol that makes a nontrivial label cycle possible.

This does **not** mean the cycle is uniquely Möbius-arithmetic. Any three-symbol sequence has the same finite-state topology. What is Möbius-specific in `(20)` is how that cycle current becomes a coupling between its sign and square-free support.

## 6. Prior art and novelty assessment

The theorem-level mechanisms are established prior art.

- Tao–Teräväinen `MC-S28` supplies the general product criterion for logarithmically averaged correlations of bounded multiplicative functions. Equation `(2)` is an elementary finite-alphabet corollary obtained by expanding `Phi` in the tensor basis `(3)` and observing that global sign-oddness forces product function `mu`.
- `MC-039` and `MC-040` already establish the line's central warning that qualitative logarithmic correlation vanishing carries no automatic polynomial global-cancellation budget.
- `MC-123` already places state-local feedback in the standard graph-flow/Hodge distinction between gradients and cycles. The `K_3` dimension count above is the smallest finite-memory specialization of that classical mechanism.

A targeted search around logarithmically averaged Elliott/Chowla correlations and finite-graph Hodge decompositions found no reason to claim a new general theorem. **No novelty is claimed for the correlation theorem, polynomial interpolation, or cycle-space algebra.** The durable contribution is the line-specific synthesis: every sign-odd fixed-memory cylinder observable is already inside the qualitative fixed-correlation class, including the first non-coboundary cycle that actually escapes `MC-123`'s tree topology.

## 7. Boundaries and falsification controls

The result sharply narrows one route but does not close memory-based approaches in general.

- `Phi` uses a **fixed finite window** and fixed shifts. Growing memory, shifts increasing with `x`, multiscale state, or adaptive history-dependent observables are not covered.
- The conclusion is **logarithmically averaged and qualitative**. It neither proves ordinary Cesàro cancellation at every scale nor supplies a polynomial rate.
- Only the globally sign-odd sector is forced to vanish by this parity argument. Sign-even observables, including pure support occupations built from `mu^2`, need not vanish.
- The abstract triangle `(16)` is a cycle in the admissible memory state graph. No claim is made that the true Möbius word realizes any particular finite cycle with a prescribed asymptotic frequency.
- The one-symbol `K_3` quotient is one-dimensional only for translation-invariant label-antisymmetric observables modulo label gradients. Allowing arbitrary dependence on the Mertens level or longer history creates a larger state graph and can create additional cycle classes.
- Equation `(2)` is compatible with very large unweighted partial sums. The matched controls in `MC-039`/`MC-040` are explicit warnings against reading logarithmic invisibility as RH-scale randomness.
- Nothing here models an off-critical zero, proves an improved bound for `M(x)`, or turns the cycle current into a positivity or spectral certificate.

The decisive next test for a memory-based route is therefore not whether finite memory creates cycles—it does—but whether **growing or state-coupled memory produces quantitatively stronger information than fixed-shift correlations, with an explicit transfer to a global Mertens exponent**. A proposal that remains a fixed cylinder statistic has already fallen inside `(2)`.

## Consequence for the research line

`MC-123` left additional history as a genuine escape from the scalar-state tree obstruction. The present result resolves the first layer of that escape.

One-symbol memory creates a real circulation, but that circulation is an adjacent `mu/mu^2` correlation. More generally, every fixed finite-memory sign-odd observable is a finite combination of the same fixed-shift mixed-correlation language and is logarithmically negligible by existing theory. Therefore simply enriching a feedback rule with a bounded amount of local history is not, by itself, a new information channel at logarithmic scale.

Future memory-based work should concentrate on the first point where this finite-cylinder reduction ceases to apply: growing windows, scale-dependent state, nonlocal coupling, or a quantitative unweighted mechanism with a demonstrable polynomial information budget.