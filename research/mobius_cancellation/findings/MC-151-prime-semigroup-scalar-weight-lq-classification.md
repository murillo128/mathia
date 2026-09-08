# MC-151 — Prime-semigroup scalar weighting is exactly an ℓq budget and cannot select Möbius

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue in the canonical number-state representation used in `MC-149` and `MC-150`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_k=\varepsilon_{pk},
\qquad
D_a\varepsilon_k=a_k\varepsilon_k,
\]

where `p` ranges over the rational primes and `a=(a_k)` is bounded. Then

\[
[D_a,S_p]\varepsilon_k=(a_{pk}-a_k)\varepsilon_{pk}.
\tag{1}
\]

Let `1\le q\le\infty` and let `w=(w_p)_p` be an arbitrary scalar prime weight. Define the prime-semigroup Banach row

\[
\mathcal R_{w,q}(a)\xi
:=
\bigl(w_p[D_a,S_p]\xi\bigr)_p
\in
\ell^q(\mathbb P;\mathcal H),
\tag{2}
\]

whenever the right-hand side defines a bounded operator from `\mathcal H`.

For the three line-specific controls

\[
\mu,\qquad q_0:=\mu^2,\qquad \lambda,
\]

there is a complete classification:

\[
\boxed{
\mathcal R_{w,q}(\mu)\text{ is bounded}
\iff
\mathcal R_{w,q}(q_0)\text{ is bounded}
\iff
\mathcal R_{w,q}(\lambda)\text{ is bounded}
\iff
w\in\ell^q(\mathbb P).
}
\tag{3}
\]

Moreover the operator norms are exact:

\[
\boxed{
\|\mathcal R_{w,q}(\mu)\|
=
\|\mathcal R_{w,q}(\lambda)\|
=2\|w\|_{\ell^q(\mathbb P)},
}
\tag{4}
\]

and

\[
\boxed{
\|\mathcal R_{w,q}(\mu^2)\|
=
\|w\|_{\ell^q(\mathbb P)}.
}
\tag{5}
\]

The formulas use the usual extended-value convention when `w\notin\ell^q`; for `q=\infty`, `\|w\|_{\ell^\infty}=\sup_p|w_p|`.

Thus **no separable scalar reweighting of the raw canonical prime commutators, tested only by boundedness in an external `\ell^q` row, can distinguish Möbius from the support control `\mu^2` or the orientation control `\lambda`.** The admissibility class is exactly the externally chosen weight space.

As a corollary, for Dirichlet weights

\[
w_p=p^{-\sigma},
\tag{6}
\]

and finite `q`, all three controls have the same exact threshold

\[
\boxed{
\mathcal R_{\sigma,q}(\mu),
\mathcal R_{\sigma,q}(\mu^2),
\mathcal R_{\sigma,q}(\lambda)
\text{ are bounded}
\iff
\sigma>\frac1q.
}
\tag{7}
\]

For `q=2`, equation `(7)` recovers the false critical-half threshold of `MC-150`. For `q=1` the same construction moves the boundary to `1`; as `q` grows, it moves continuously toward `0`, and at `q=\infty` the unweighted row is already bounded. The location of the apparent critical exponent is therefore **chosen by the Banach aggregation**, not selected by Möbius cancellation or the Riemann zero divisor.

This closes the whole scalar-weighted prime-row interpolation left open after `MC-149` and only partially sampled by the Hilbert row in `MC-150`. A surviving transverse Bost--Connes mechanism must introduce genuinely relational structure — for example state-dependent weights, cross-dilation coupling, a non-scalar/twisted construction, or another operation not reducible to membership of an externally supplied scalar weight in `\ell^q` — and must still prove a non-tautological transfer to anchored Mertens excursion.

## 1. Universal sufficiency of the ℓq weight budget

For every bounded sequence `a`, equation `(1)` and the raw norm calculation of `MC-149` give

\[
\|[D_a,S_p]\xi\|_2
\le
2\|a\|_\infty\|\xi\|_2.
\tag{8}
\]

For `1\le q<\infty`, if `w\in\ell^q(\mathbb P)`, then

\[
\begin{aligned}
\|\mathcal R_{w,q}(a)\xi\|_{\ell^q(\mathbb P;\mathcal H)}^q
&=
\sum_p |w_p|^q\|[D_a,S_p]\xi\|_2^q\\
&\le
(2\|a\|_\infty)^q
\|\xi\|_2^q
\sum_p|w_p|^q.
\end{aligned}
\tag{9}
\]

Hence

\[
\|\mathcal R_{w,q}(a)\|
\le
2\|a\|_\infty\|w\|_q.
\tag{10}
\]

For `q=\infty`, the same pointwise estimate gives

\[
\|\mathcal R_{w,\infty}(a)\|
\le
2\|a\|_\infty\|w\|_\infty.
\tag{11}
\]

No arithmetic property of `a` is used. Membership of the scalar weights in the chosen external sequence space is therefore a universal sufficient condition for every bounded arithmetic diagonal.

## 2. Möbius forces exactly the same weight condition

At the anchored basis state `\varepsilon_1`,

\[
\mu(1)=1,
\qquad
\mu(p)=-1,
\]

so equation `(1)` yields

\[
[D_\mu,S_p]\varepsilon_1=-2\varepsilon_p.
\tag{12}
\]

Therefore, for finite `q`,

\[
\|\mathcal R_{w,q}(\mu)\varepsilon_1\|^q
=
2^q\sum_p|w_p|^q,
\tag{13}
\]

and for `q=\infty`,

\[
\|\mathcal R_{w,\infty}(\mu)\varepsilon_1\|
=2\sup_p|w_p|.
\tag{14}
\]

If the row is bounded, `(13)`--`(14)` force `w\in\ell^q`. Combined with the universal upper bound `(10)`--`(11)`, they prove the Möbius equivalence in `(3)` and the first equality in `(4)`.

This necessity is much stronger than the Dirichlet-weight lower bound of `MC-150`: it does not depend on a specific decay law or on asymptotics. The prime row reads the complete scalar-weight norm directly from one anchored number state.

## 3. Liouville gives the same exact norm for a different arithmetic reason

Liouville is completely multiplicative and satisfies `\lambda(p)=-1`. Hence for every prime `p` and every `k`,

\[
\lambda(pk)-\lambda(k)
=-2\lambda(k),
\]

so

\[
\|[D_\lambda,S_p]\varepsilon_k\|_2=2
\qquad(k\ge1).
\tag{15}
\]

The same calculation as in `(13)`--`(14)` therefore holds on every basis state, giving

\[
\|\mathcal R_{w,q}(\lambda)\|=2\|w\|_q.
\tag{16}
\]

Thus a row that appears to retain the local prime sign `-1` still does not isolate Möbius: a completely multiplicative function with no squarefree-support zeros produces precisely the same scalar-weight regularity profile.

## 4. The squarefree-support control also forces the full ℓq budget

Set

\[
q_0(n)=\mu(n)^2.
\]

For any squarefree `k`, `q_0(k)=1`, and multiplication by a prime gives

\[
|q_0(pk)-q_0(k)|
=
\begin{cases}
1,&p\mid k,\\
0,&p\nmid k.
\end{cases}
\tag{17}
\]

Therefore, for finite `q`,

\[
\|\mathcal R_{w,q}(q_0)\varepsilon_k\|^q
=
\sum_{p\mid k}|w_p|^q
\qquad(k\text{ squarefree}).
\tag{18}
\]

Given an arbitrary finite set of primes `F`, choose

\[
k_F=\prod_{p\in F}p.
\]

Then `(18)` gives

\[
\|\mathcal R_{w,q}(q_0)\varepsilon_{k_F}\|^q
=
\sum_{p\in F}|w_p|^q.
\tag{19}
\]

If the row has operator norm at most `C`, every finite partial sum in `(19)` is at most `C^q`; taking the supremum over finite `F` forces

\[
\sum_p|w_p|^q\le C^q.
\tag{20}
\]

Conversely, when `w\in\ell^q`, the pointwise difference for `q_0` is at most `1`, so

\[
\|\mathcal R_{w,q}(q_0)\xi\|^q
\le
\|w\|_q^q\|\xi\|_2^q.
\tag{21}
\]

Together `(19)`--`(21)` prove both the `\mu^2` equivalence in `(3)` and the exact norm `(5)` for finite `q`.

For `q=\infty`, the upper bound is immediate from `|q_0(pk)-q_0(k)|\le1`. Choosing `k=p` for a prime at which `|w_p|` is arbitrarily close to `\sup_r|w_r|` gives the matching lower bound, so `(5)` also holds at the endpoint.

This support control is especially decisive. Unlike the Möbius base-state proof, its necessity uses no negative orientation at all: the operator norm can collect any finite set of prime weights by choosing a squarefree number state carrying exactly those prime divisors.

## 5. Dirichlet exponents are therefore aggregation artifacts

Specialize to `(6)`. For finite `q`, the classification `(3)` reduces boundedness to

\[
\sum_p p^{-q\sigma}<\infty.
\tag{22}
\]

The classical reciprocal-prime divergence gives divergence at `q\sigma=1`; if `q\sigma<1`, then `p^{-q\sigma}\ge p^{-1}` for all primes `p>1`, so divergence persists. If `q\sigma>1`, convergence follows from comparison with

\[
\sum_{n\ge2}n^{-q\sigma}.
\]

Hence `(22)` is equivalent to `\sigma>1/q`, proving `(7)`.

The diagnostic consequence is stronger than the `q=2` observation in `MC-150`. The same arithmetic representation and the same raw prime commutators admit a continuum of apparent critical boundaries merely by changing the external Banach exponent:

\[
q=1\Rightarrow \sigma_c=1,
\qquad
q=2\Rightarrow \sigma_c=\frac12,
\qquad
q=4\Rightarrow \sigma_c=\frac14.
\tag{23}
\]

Nothing in the Möbius diagonal changes across these choices. Therefore the occurrence of `1/2` at `q=2` cannot carry independent RH significance: it is one member of the functional-analytic family `\sigma_c=1/q`.

At `q=\infty`, the condition is simply boundedness of the scalar weights. In particular the unweighted prime row `w_p=1` is bounded, matching the raw universal-boundedness endpoint classified in `MC-149`.

## 6. Prior-art and novelty assessment

The Bost--Connes number-state representation, the canonical semigroup isometries, and the raw commutator formula `(1)` are established inputs already audited in `MC-138`--`MC-150`. `MC-149` also records the adjacent twisted-spectral-triple literature, including Greenfield, Marcolli and Teh, *Twisted Spectral Triples and Quantum Statistical Mechanical Systems* (2014), DOI `10.1134/S2070046614020010`. This finding does not claim novelty for those objects or for weighted-shift/commutator technology.

The external `\ell^q` estimate in `(9)` is elementary Banach-space bookkeeping, and the necessity arguments use only the classical local values and multiplicativity of `\mu`, `\mu^2`, and `\lambda`. The Dirichlet corollary uses only the classical divergence of `\sum_p1/p`, already anchored as `MC-S6`, plus ordinary `p`-series comparison.

A targeted literature search around Bost--Connes semigroup commutators, scalar/prime weights, Schatten or Banach summability, and Möbius did not locate a theorem with the exact classification `(3)`--`(7)`. **No novelty inference is drawn from that absence.** The result is persisted as an exact line-specific obstruction because it closes an entire live candidate class, not because its individual functional-analytic ingredients are new.

## Boundaries and falsification tests

- **Prime semigroup family only.** The exact necessity in `(3)` uses the canonical prime dilations. A full composite-dilation row with arbitrary weights can hide mass on dilation classes where a chosen control has zero difference and therefore needs its own classification.
- **Scalar separable weights only.** The theorem assumes one scalar `w_p` multiplying the whole commutator at prime `p`. A weight depending jointly on `p` and the number state `k`, a matrix/operator-valued weight, or a coupling between several dilation coordinates is not reduced to `\ell^q` membership by this proof.
- **Raw commutators only.** Twisted commutators, alternative derivations/Dirac operators, cocycles, or different representations remain outside the claim.
- **External Banach-row boundedness only.** Nonlinear statistics, conditional expectations retaining relative phases, determinants, mixed moments, and other relational observables need separate derivations. Merely changing `q`, however, is now fully classified and cannot create arithmetic selectivity.
- **Matched controls are exact.** Both a sign-erased control `\mu^2` and a support-erased orientation control `\lambda` have the same admissible scalar-weight class as `\mu`. Any proposed interpretation of row boundedness must therefore explain what additional datum distinguishes both controls.
- **No Mertens estimate follows.** Equations `(3)`--`(7)` classify an operator-regularity family; they contain no transfer to `M(x)`, first-absolute Mertens excursion, or the zero divisor.
- **The threshold is algebraic/analytic, not numerical.** The necessity is certified by exact basis vectors and finite prime products, so no finite-range experiment can change the classification.

## Consequence for the line

`MC-149` left source-forced weighting as an obvious intermediate between universally bounded raw commutators and compact/Schatten conditions that reject Möbius. `MC-150` killed the first Dirichlet-weighted Hilbert row and exposed its apparent `1/2` as ordinary square summability.

The present classification removes the remaining freedom in **scalar prime weighting plus external `\ell^q` aggregation**. For Möbius, its squarefree-support control, and Liouville, boundedness is exactly the statement that the externally chosen scalar weight lies in the chosen sequence space; the arithmetic target supplies no extra selectivity. Changing `q` merely relocates the apparent critical exponent to `1/q`.

Accordingly, a meaningful intermediate transverse category cannot be obtained by tuning scalar decay or Banach summability alone. It must encode a relation that couples prime dilation to number state, couples different dilations to one another, or otherwise introduces source-forced structure not already exhausted by an externally prescribed weight norm.