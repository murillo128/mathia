# MC-074 — Möbius comparator factorizations form a Dirichlet-convolution torsor, so one-factor partial statistics require external gauge fixing

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-073` proves that the complete comparator/inverse recovery

\[
a*k=\mu
\]

is universal once the exact Dirichlet inverse is recomputed with the comparator. The residual question was whether a **proper partial statistic** of that factorization could escape the full-sum gauge degeneracy.

There is a second exact obstruction before any analytic estimate begins. Let

\[
\mathcal U=\{u:\mathbb N\to\mathbb C:u(1)=1\}
\]

with Dirichlet convolution. By the classical inversion theorem, `\mathcal U` is an abelian group. Define the normalized factorization space

\[
\mathcal F_\mu
=
\{(a,k)\in\mathcal U^2:a*k=\mu\}.
\]

Then `\mathcal U` acts on `\mathcal F_\mu` by

\[
\boxed{
 u\cdot(a,k)=(a*u,u^{-1}*k).
}
\tag{1}
\]

This action is **free and transitive**. Equivalently, `\mathcal F_\mu` is a torsor for the full normalized Dirichlet-convolution group. In particular,

\[
\boxed{
k=a^{-1}*\mu,\qquad a=\mu*k^{-1},}
\tag{2}
\]

so either factor can be prescribed arbitrarily in `\mathcal U`, with the other then forced uniquely.

This sharpens the control boundary of `MC-073`:

1. **No factor is canonically selected by the identity `a*k=mu`.** Every normalized comparator and every normalized inverse-kernel sequence occurs in exactly one factorization.
2. **Any finite kernel prefix can be prescribed arbitrarily** in the unrestricted factorization class. Given arbitrary complex values `c_2,...,c_N`, choose any normalized arithmetic function `k` with `k(n)=c_n` for `2<=n<=N`; equation `(2)` produces an exact comparator `a` with `a*k=mu`.
3. The same statement holds with the roles of comparator and kernel reversed.
4. Restricting to multiplicative functions does not by itself fix the gauge. The multiplicative units form a subgroup, and the corresponding multiplicative factorizations are again a torsor. Arbitrary prime-power local data for one multiplicative factor may be chosen, subject only to the intended multiplicative definition, and the other factor remains multiplicative.
5. Any statistic on `\mathcal F_\mu` that is invariant under the full action `(1)` is constant on the whole factorization space, because the action has one orbit.

Therefore **partiality alone does not make a comparator statistic arithmetic evidence**. A truncation, prefix norm, selected reciprocal block, or spectral diagnostic of just `k` can be made to look essentially however one wants by choosing a different unrestricted gauge. Likewise for a statistic of just `a`. A surviving one-factor mechanism must first impose an independently justified arithmetic restriction that genuinely selects or narrows the gauge—for example the square-free-character class used in `MC-066`--`MC-072`, a boundedness/support condition, a prescribed Euler-factor family, or another source-natural class—and then prove that the desired estimate follows from structure specific to that restricted class.

A genuinely coupled statistic `Q(a,k)` is not killed merely because it changes under `(1)`. Gauge sensitivity is necessary for it to distinguish factorizations, but it is not sufficient for arithmetic usefulness: the chosen gauge itself must be justified independently, and the estimate must not be a disguised consequence of exact inversion.

No improved estimate for `M(X)` is claimed.

## 1. Exact torsor proof

Take any `(a,k)\in\mathcal F_\mu` and `u\in\mathcal U`. Associativity and commutativity give

\[
(a*u)*(u^{-1}*k)
=a*(u*u^{-1})*k
=a*\varepsilon*k
=\mu,
\]

so `(1)` preserves `\mathcal F_\mu`.

The action is free. If

\[
(a*u,u^{-1}*k)=(a,k),
\]

then `a*u=a`. Convolution with `a^{-1}` gives `u=\varepsilon`.

It is transitive. Given two factorizations `(a,k)` and `(a',k')`, set

\[
u=a^{-1}*a'.
\]

Then `a*u=a'`. Since

\[
k=a^{-1}*\mu,
\qquad
k'=(a')^{-1}*\mu,
\]

one also has

\[
\begin{aligned}
u^{-1}*k
&=(a'^{-1}*a)*(a^{-1}*\mu)\\
&=a'^{-1}*\mu\\
&=k'.
\end{aligned}
\]

Thus every factorization is reached from every other by a unique gauge element.

Equation `(2)` is simply the two coordinate descriptions of this torsor. It also proves the finite-prefix statement: Dirichlet inversion exists for every normalized arithmetic function, so prescribing finitely many coefficients of one factor causes no compatibility condition at the level of unrestricted arithmetic functions.

## 2. Multiplicativity is not a gauge fixing

Let `\mathcal U_{\rm mult}` be the subgroup of normalized multiplicative arithmetic functions. Dirichlet convolution and Dirichlet inversion preserve multiplicativity, and `\mu` is multiplicative. Therefore

\[
\mathcal F_\mu^{\rm mult}
=
\{(a,k)\in\mathcal U_{\rm mult}^2:a*k=\mu\}
\]

is a torsor for `\mathcal U_{\rm mult}` under the same action.

Concretely, choose arbitrary local formal factors

\[
K_p(z)=1+k(p)z+k(p^2)z^2+\cdots
\]

for the primes under consideration and let them define a multiplicative `k`. The inverse local factors exist because every constant term is `1`; then `a=\mu*k^{-1}` is multiplicative automatically. Thus the generic statement “both factors are multiplicative” does not select a preferred decomposition of Möbius.

This does **not** say that strong subclasses are gauge-degenerate. Requiring, for example,

\[
a(n)=\mu(n)^2\chi(n)
\]

for a Dirichlet character, or imposing exact support, boundedness, positivity, conductor, or a fixed Euler-factor law cuts the torsor down to a much smaller family. Such restrictions are precisely where arithmetic information can enter. The point is that their force comes from the extra restriction, not from the bare factorization `a*k=mu`.

## 3. Consequence for partial reciprocal-block routes

The reciprocal-block representation in `MC-073` writes the same exact recovery in terms of the summatory functions of the two factors. It left open truncated ranges, selected blocks, and other proper subfunctionals because the **complete** block sum is gauge-degenerate.

The torsor classification adds a necessary distinction.

A statistic such as

\[
\sum_{d\le D} k(d),
\qquad
\sum_{d\in I}|k(d)|^2,
\qquad
\text{or another functional of a finite kernel block alone}
\]

is not made intrinsic by being proper or truncated. In the unrestricted class its input coefficients can be prescribed before the complementary comparator is solved from `(2)`. A small value for such a statistic therefore cannot be credited to Möbius merely because the resulting pair still reconstructs `\mu` exactly.

The same warning applies to comparator-only partial statistics. What can survive is one of two structures:

- **external gauge fixing:** a source-natural restricted comparator family is chosen independently, and one proves a factor estimate uniformly or structurally inside that family; or
- **coupled gauge-sensitive information:** a statistic genuinely uses both factors and its useful bound is proved from an arithmetic relation that is not implied by inversion alone.

Even then, a matched-control family should vary the allowed gauge **within the same externally justified class**. Recomputing the exact inverse while allowing arbitrary normalized comparators is too broad and makes any one-factor anomaly non-identifiable; freezing one factor while changing the other is nondegenerate but tests a different mathematical object, as already noted in `MC-073`.

## 4. Gauge-invariant observables collapse to the recovered object

Because `\mathcal F_\mu` is a single `\mathcal U`-orbit, if

\[
Q(u\cdot(a,k))=Q(a,k)
\]

for every gauge `u`, then `Q` has the same value on every normalized factorization of `\mu`.

This does not make `Q` numerically trivial: a gauge-invariant quantity may still encode difficult information about `\mu` itself. It does, however, block an explanatory claim of the form “this invariant becomes small because the chosen comparator exposes a special decomposition.” If the quantity is fully gauge invariant, the comparator choice cannot be the source of the gain; the quantity was already a function of the recovered Möbius object.

Conversely, a gauge-sensitive statistic can distinguish decompositions, but then its significance depends on why one gauge or restricted gauge family is arithmetically privileged. This is the same identifiability distinction that the full-sum control in `MC-073` was pointing toward, now made exact at the level of the entire factorization space.

## 5. Prior art and novelty boundary

The algebraic input is classical. The DLMF §27.5 inversion formulas, already used as the authoritative group-theoretic anchor in `MC-073`, state that arithmetic functions with nonzero value at `1` form an abelian group under Dirichlet convolution and that multiplicative functions form a subgroup; the Möbius function is the Dirichlet inverse of the constant-one function. Apostol's *Introduction to Analytic Number Theory*, Chapter 2, is the standard cited source behind those statements.

Calling the simply transitive action above a “torsor” is standard group-action language, not a new number-theoretic theorem. Equations `(1)`--`(2)` are immediate consequences of the classical convolution group law. A targeted literature search found no basis for a novelty claim about this algebraic classification, and none is made.

The durable Mathia result is the **frontier falsification consequence** relative to `MC-073`: after ruling out complete coupled cancellation as universal, one cannot rescue the route merely by taking a proper statistic of one unconstrained factor. The factorization itself supplies no canonical gauge, and the one-factor coefficients can be prescribed before exact recovery. Any surviving partial route must identify its extra arithmetic gauge restriction or a genuinely coupled statistic explicitly.

## 6. Boundaries and falsification tests

The result is exact but deliberately narrow.

- It applies to normalized factorizations `a*k=mu` with `a(1)=k(1)=1`. Other nonzero normalizations can be rescaled, but no such extension is needed here.
- The arbitrary finite-prefix statement uses the unrestricted arithmetic-function group. Under boundedness, support, positivity, character, conductor, or other structural restrictions, not every prefix is realizable. Those restrictions are possible information carriers rather than counterexamples to the claim.
- In the multiplicative subspace, arbitrary **prime-power local data** may be prescribed, but composite coefficients are then fixed multiplicatively; the finding does not claim arbitrary global prefixes while preserving multiplicativity.
- The torsor obstruction does not rule out a special comparator family selected independently by a theorem, nor a coupled statistic whose estimate uses extra arithmetic structure.
- Gauge invariance implies constancy only across factorizations of the **same** recovered `mu`; it does not imply constancy across different recovered arithmetic functions.
- The result does not say that every gauge is analytically equally convenient. A useful coordinate choice can expose a proof even when the underlying factorization is noncanonical.

The claim is falsified if normalized arithmetic functions are not closed under Dirichlet inversion, if action `(1)` fails to preserve `a*k=mu`, if two normalized factorizations cannot be connected by a unique `u=a^{-1}*a'`, or if a normalized prescribed factor fails to determine the other uniquely through `(2)`.

## Consequence for the active frontier

`MC-073` requires the signed comparator program to move from complete algebraically forced recovery to a proper non-universal statistic. This finding narrows that requirement further: **a proper statistic of one unrestricted factor is still not an identified Möbius mechanism.**

The next coupled-comparator candidate must therefore state its gauge fixing as part of the mathematics. It should specify a source-natural restricted class of comparators or kernels, show why that class is independently meaningful, identify a partial or coupled observable not fixed by the convolution identity, and prove a bound using information weaker than the Mertens target. If the only reason a factor is chosen is that its exact partner can be solved so that the product returns `mu`, the construction remains pure gauge.