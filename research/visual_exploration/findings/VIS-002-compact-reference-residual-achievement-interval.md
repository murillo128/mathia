# VIS-002 — compact-reference cusp residuals have interval-filling tails

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED`.

## Claim

Adopt the PF-164 connected-cusp setup

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
q_j=p_j+1,
\]

and let `E` be the set of interior prime indices `j` for which the following prime gap satisfies

\[
p_{j+1}-p_j>2.
\]

Enumerate the corresponding primes increasingly as

\[
r_1<r_2<\cdots.
\]

At each such site the ordered all-composite replacement

\[
q_j=p_j+1\longmapsto q'_j=p_j+3
\]

is legal, because `p_j+3` is even composite and lies strictly below `p_{j+1}+1`. Define its nonlinear coefficient-residual atom by

\[
a_k
=
2\left(V(r_k+3)-V(r_k+1)-2\right).
\tag{1}
\]

Then:

1. for every finite set `F` of eligible sites, the PF-164 finite-support law gives
   \[
   \Delta C(F)=4|F|+\sum_{k\in F}a_k;
   \tag{2}
   \]
2. `(a_k)` is positive, strictly decreasing and summable;
3. with `R_k=\sum_{\ell>k}a_\ell`,
   \[
   \frac{a_k}{R_k}\longrightarrow0;
   \tag{3}
   \]
4. hence there exists `K` such that the achievement set of every tail
   \[
   \mathcal A_K
   =
   \left\{
   \sum_{k\ge K}\varepsilon_k a_k:
   \varepsilon_k\in\{0,1\}
   \right\}
   \]
   is exactly the compact interval
   \[
   \mathcal A_K=
   \left[0,\sum_{k\ge K}a_k\right].
   \tag{4}
   \]

Equivalently, for sufficiently far compact `+2` reference perturbations, the finite-support residual values

\[
\Delta C(F)-4|F|
\]

are dense in a nondegenerate interval.

This is a statement about the PF-161--PF-164 selected relative cusp coefficient. It is not an intrinsic invariant of the prime flute or a new theorem about general Ruelle zeta functions.

## Derivation

Put

\[
f(x)=V(x)-x.
\]

PF-164 proves for arbitrary finite-support reference changes away from the initial boundary that the cusp-coefficient shift is

\[
\Delta C=2\sum_j\delta_j,
\qquad
\delta_j=V(q'_j)-V(q_j).
\tag{5}
\]

For the legal `+2` replacement above,

\[
\delta_j
=2+f(p_j+3)-f(p_j+1),
\]

which gives (1)--(2). Simultaneous `+2` moves remain ordered because adding the same `2` to any selected reference labels preserves their strict order, while eligibility ensures that each moved label stays below the next unmoved label.

For `x>2`,

\[
f'(x)
=
\left(
\frac{\pi/x}{\sin(\pi/x)}
\right)^2-1
>0.
\tag{6}
\]

Moreover `f'` is strictly decreasing. Indeed, `y/\sin y` is strictly increasing for `0<y<\pi/2` because

\[
\frac{d}{dy}\frac{y}{\sin y}
=
\frac{\sin y-y\cos y}{\sin^2y}>0,
\]

while `y=\pi/x` decreases with `x`. Therefore

\[
a_k
=
2\int_{r_k+1}^{r_k+3}f'(x)\,dx
\tag{7}
\]

is positive and strictly decreases as `r_k` increases.

The cotangent expansion at the origin gives

\[
f'(x)
=
\frac{\pi^2}{3x^2}+O(x^{-4}),
\]

hence

\[
a_k
=
\frac{4\pi^2}{3r_k^2}+O(r_k^{-3}).
\tag{8}
\]

The eligible indices are not sparse in prime-index scale. Beyond the prime `3`, two consecutive prime gaps cannot both equal `2`: otherwise `p,p+2,p+4` would all be prime even though one of the three is divisible by `3`. Thus at least one of every two consecutive prime gaps belongs to `E`. If `n_k` is the prime index of `r_k`, then

\[
k\le n_k\le 2k+O(1).
\tag{9}
\]

The prime number theorem therefore gives

\[
r_k=\Theta(k\log k).
\tag{10}
\]

Combining (8)--(10),

\[
a_k
=
\Theta\!\left(\frac1{k^2\log^2 k}\right),
\qquad
R_k
=
\Theta\!\left(\frac1{k\log^2 k}\right),
\tag{11}
\]

so (3) follows.

Kakeya's achievement-set criterion says that a positive nonincreasing summable sequence has achievement set equal to a compact interval when each term is at most its remaining tail. Equation (3) implies that

\[
a_k\le R_k
\]

for all sufficiently large `k`, so applying the criterion to such a tail gives (4). Every infinite subsum is the limit of its finite truncations, hence the finite-support residuals are dense in that interval.

## Visual diagnostic

The retained visualization uses the first `18` eligible sites beginning at `p=103`. The final finite stage contains `2^18=262144` exact subset sums and already appears as a thick interval-like band:

[Prime-flute compact-reference residual achievement set](../visualizations/prime-flute-compact-reference-achievement-set.md).

A conservative exact-structure numerical check enumerated eligible sites through `p<20000`. Using only the computed tail up to that cutoff, every eligible atom from `p=103` through `p=19973` already satisfies the Kakeya inequality `a_k <= R_k`; the last two cutoff-adjacent atoms fail only because the true later tail was not included. This computation is illustrative, not needed for the proof.

## Prior art and novelty assessment

The achievement-set step is classical. A convenient modern statement of Kakeya's criterion is Theorem 1.1 of J. Marchwicki and P. Miska, *On Kakeya Conditions for Achievement Sets*, Results in Mathematics 76, 181 (2021), DOI `10.1007/s00025-021-01479-2`. It states the interval criterion in terms of each sequence term and the remaining tail. Modern work also treats interval, Cantor and Cantorval achievement sets for broader summable sequences.

No novelty is claimed for Kakeya's theorem, the prime number theorem, the cotangent expansion, or the elementary exclusion of three consecutive odd primes spaced by `2`. Directed searches did not reveal this particular prime-flute compact-reference residual sequence as a studied achievement set, but the warranted contribution is only the Mathia-specific consequence obtained by combining PF-164 with classical subsum theory.

## Boundary conditions and failure modes

The interval result concerns the restricted family of simultaneous `+2` composite reference moves. It does not classify all legal compact perturbations, which allow positive and negative displacements of several sizes and therefore generate a multivalued signed residual system.

The conclusion is about the *closure* of finite-support residual values after subtracting the obvious integer term `4|F|`. The set of finite-support perturbations itself is countable; density in an interval does not make it literally equal to the interval.

The result also does not recover an intrinsic arithmetic signal. The interval-filling mechanism is driven by the slow convergence of the positive residual atoms and classical achievement-set theory. A surrogate sequence with the same asymptotic atom scale would exhibit the same topology.

Finally, this says nothing about the full Laplacian, scattering matrix, full Ruelle/Selberg objects, or another canonically normalized relative invariant. It refines the reference dependence of the specific PF-161--PF-164 connected cusp coefficient.

## Consequence for the research line

PF-164 shows that the selected cusp coefficient can be changed arbitrarily far in either sign by compact reference modifications. VIS-002 adds a different structural fact: after quotienting the obvious integer displacement, even a very narrow legal perturbation family has a continuum-like interval closure on every sufficiently far tail.

Thus the compact-reference instability is not merely a collection of isolated tunable values, nor does its nonlinear cotangent residue retain a Cantor-like fingerprint of the primes. The natural remaining question is to classify the full signed/multivalued residual closure and determine whether any quotient or normalization of that larger reference action leaves a nontrivial invariant.
