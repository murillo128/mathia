# MC-285 — Even shell pairing forces a projected Christoffel support barrier

**Status:** `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

In the restricted shell

\[
\mathcal R_y=\{r\text{ prime}: y<r\le 2y,\ r\equiv1\pmod4\},
\qquad N_y=|\mathcal R_y|,
\]

consider an endpoint-normalized Christoffel/separator coefficient vector as in `MC-281`, and let `U` be the set of lower-prime sign coordinates actually used by its supported monomials. Write `d=|U|` and, for each shell prime,

\[
v_U(r)=\bigl((p/r)\bigr)_{p\in U}\in\{\pm1\}^d.
\]

Let `K_U` be the number of distinct projected patterns `v_U(r)` realized by the shell. For every **even** shell weight `t`, if

\[
N_y-K_U\ge t,
\]

then there exists a shell row `T\subset\mathcal R_y` with `|T|=t` whose projection on all coordinates in `U` is the endpoint vector `1`. Consequently every endpoint-normalized coefficient vector on that support has empirical Christoffel energy at least `1`.

Since `K_U\le2^d`, any even-weight endpoint-normalized certificate with empirical energy `<1` must therefore satisfy the exact necessary conditions

\[
K_U>N_y-t,
\qquad
2^d>N_y-t.
\]

Equivalently,

\[
d>\log_2(N_y-t).
\]

This obstruction is deterministic. It needs no pattern equidistribution, no Page theorem, no Siegel-zero control, and no conductor-distribution hypothesis.

## Derivation

Partition the shell primes by their projected sign pattern. For each `ε∈{±1}^d`, let

\[
n_\varepsilon=|\{r\in\mathcal R_y:v_U(r)=\varepsilon\}|.
\]

Within each occupied cell, pair distinct shell primes having the same projected vector. The number of disjoint equal-pattern pairs available is

\[
\sum_\varepsilon\left\lfloor\frac{n_\varepsilon}{2}\right\rfloor.
\]

Because

\[
\left\lfloor\frac n2\right\rfloor\ge\frac{n-1_{n>0}}2,
\]

summing over the occupied cells gives

\[
\sum_\varepsilon\left\lfloor\frac{n_\varepsilon}{2}\right\rfloor
\ge \frac{N_y-K_U}{2}.
\]

Now write the even shell weight as `t=2h`. If `N_y-K_U\ge t`, there are at least `h` disjoint equal-pattern pairs. Let `T` be the union of any `h` such pairs. Then `|T|=t`, and coordinatewise every pair contributes the square of the same sign vector. Hence

\[
x(T)|_U
 =\prod_{r\in T}v_U(r)
 =\mathbf 1.
\]

By the endpoint-normalization mechanism isolated in `MC-281`, the corresponding polynomial satisfies

\[
p_a(x(T))=p_a(\mathbf 1)=1.
\]

The empirical energy therefore contains at least one contribution of absolute square `1`, so it cannot be `<1`.

The contrapositive yields `K_U>N_y-t`; using `K_U≤2^d` yields `2^d>N_y-t`.

## Quantitative consequence

For the progression `r≡1 (mod 4)`, the classical prime number theorem in arithmetic progressions gives

\[
N_y\sim \frac{y}{2\log y}.
\]

In the live shell regime where `t=O(log log y)`, the exact support condition implies

\[
d\ge \frac{\log y-\log\log y}{\log2}+O(1).
\]

For the odd-prime coordinate support used by the conductor quantity of `MC-284`,

\[
Q(U)=4\prod_{p\in U}p,
\]

the smallest possible product for `d` distinct odd-prime coordinates is obtained from the first `d` such primes. The classical primorial asymptotic therefore gives

\[
\log Q(U)\ge (1+o(1))d\log d.
\]

Substituting the support-size lower bound yields, for even shell weights,

\[
\log Q(U)
\ge
\left(\frac1{\log2}+o(1)\right)\log y\,\log\log y.
\]

Thus an even-weight empirical-energy `<1` certificate must live far beyond the stretched-exponential conductor window excluded in `MC-284`. This conductor statement is only a classical asymptotic corollary; the finite combinatorial support barrier above is the primary result.

## Parity boundary

The pairing mechanism is intrinsically even-cardinality and does not force an odd-size projected endpoint row.

Identify `{±1}^d` with `F_2^d`. If every occupied projected pattern lies in an affine hyperplane

\[
H=\{x\in\mathbf F_2^d:\lambda\cdot x=1\},
\]

then the sum of any odd number of occupied vectors still satisfies

\[
\lambda\cdot(x_1+\cdots+x_{2m+1})=1,
\]

so it can never equal `0`. Equivalently, an odd product of those sign patterns can never be the all-positive endpoint vector. Such an affine hyperplane already contains `2^{d-1}` patterns.

Therefore sheer multiplicity or occupation of many projected cells cannot by itself extend the argument to odd shell weights. For odd `t`, a source-native arithmetic input must force an odd zero-sum dependency, an all-positive cell, or some comparable escape from an affine obstruction.

## Relation to the existing frontier

`MC-281` showed that a projected endpoint row on the coefficient's own used coordinates is enough to kill an endpoint-normalized empirical-energy `<1` certificate. `MC-284` then used Page–Siegel pattern realization to force every Boolean pattern, hence in particular that endpoint row, inside a stretched-exponential conductor window.

The present result shows that full pattern realization is unnecessary for **even** shell weights: elementary equal-pattern pairing already forces the projected endpoint whenever the used coordinate support is small enough. In this parity sector the Page–Siegel machinery is therefore overkill for the Christoffel obstruction.

For **odd** shell weights, the pairing proof fails for a structural reason rather than a technical one. `MC-284` and any future arithmetic pattern-realization mechanism remain relevant there. This refines the research frontier from a generic conductor-distribution problem into a parity-sensitive one: even weights face a deterministic support barrier, while odd weights still require genuine arithmetic control of projected pattern geometry.

## Prior-art and novelty audit

The pairing lemma itself is elementary pigeonhole combinatorics in a finite elementary `2`-group, and no novelty is claimed for it. The prime-counting and primorial asymptotics used in the secondary translation are classical.

The useful additional statement here is the composition of that elementary mechanism with the directional projected-endpoint criterion of `MC-281`, producing the exact support obstruction `2^d>N_y-t` and separating the even-weight Christoffel frontier from the odd-weight one. This is a Mathia-internal frontier refinement, not a new theorem about Möbius summatory cancellation or the Riemann hypothesis.

## Boundaries

- This does not improve any unconditional bound for `M(x)` and does not prove or imply RH.
- It gives a necessary condition for the specific endpoint-normalized empirical Christoffel certificate studied in `MC-281`; it does not claim that sufficiently large support makes such a certificate exist.
- The decisive finite statement is for even shell weight. No corresponding odd-weight conclusion follows from pairing or occupancy alone.
- The conductor corollary assumes distinct odd-prime source coordinates as in `MC-284`; a separate `p=2` coordinate changes only a bounded amount and is irrelevant to the asymptotic statement.
- No claim is made that the elementary combinatorial mechanism itself is new in the literature.

## Decisive test and next frontier

Any proposed **even-weight** endpoint-normalized empirical-energy `<1` certificate using `d` projected sign coordinates is impossible whenever

\[
2^d\le N_y-t.
\]

Accordingly, source-native inverse or pattern-distribution work aimed at beating the current Christoffel barrier should now focus on **odd shell weights**: force odd projected zero-sums, rule out large affine-hyperplane concentration, or derive an arithmetic mechanism that produces the projected endpoint without requiring full Boolean pattern universality.
