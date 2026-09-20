# MC-423 — Exact product fibers have only subpolynomial tangent volume

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-422` shows that a thin product shell strongly taxes **coordinate-axis** translation boxes, but leaves open the genuinely different possibility of moving tangentially while preserving the product. For fixed factor depth, exact integer product preservation has its own severe limitation: every such tangent family is confined to a generalized-divisor fiber of subpolynomial cardinality.

For fixed `d>=2` and `m>=1`, define the ordered factorization fiber

\[
\mathcal F_d(m)
:=
\{(u_1,\ldots,u_d)\in\mathbb N^d:u_1\cdots u_d=m\}.
\tag{1}
\]

If

\[
m=\prod_p p^{a_p},
\tag{2}
\]

then distributing each exponent `a_p` among the `d` ordered factors gives the exact cardinality

\[
\boxed{
|\mathcal F_d(m)|
=d_d(m)
=
\prod_{p^{a_p}\parallel m}
\binom{a_p+d-1}{d-1},
}
\tag{3}
\]

where `d_d=1*\cdots*1` is the `d`-fold divisor function. Moreover,

\[
\boxed{
d_d(m)\le \tau(m)^{d-1},
}
\tag{4}
\]

because a weak composition of `a_p` into `d` parts is determined by its first `d-1` entries, each lying in `{0,\ldots,a_p}`. Since the classical divisor bound gives

\[
\tau(m)=m^{o(1)},
\tag{5}
\]

we obtain, for every fixed `d`,

\[
\boxed{
|\mathcal F_d(m)|=m^{o(1)}.
}
\tag{6}
\]

Consequently, if an exact product-preserving arithmetic lift tries to realize a rank-`r` rectangular translation family injectively inside one fiber,

\[
\Phi:
\prod_{j=1}^r\{0,\ldots,H_j-1\}
\hookrightarrow
\mathcal F_d(m),
\tag{7}
\]

then necessarily

\[
\boxed{
\prod_{j=1}^r H_j
\le d_d(m)
=m^{o(1)}.
}
\tag{8}
\]

Thus, at `m\asymp X`, an **exact product-preserving tangent orbit of fixed factor depth cannot supply polynomial translation bandwidth volume** `X^\delta` for any fixed `delta>0`. In the positive-kernel accounting of `MC-419`–`MC-420`, exact tangent redistribution can therefore improve a diagonal budget only by a subpolynomial factor unless some additional variable changes the product fiber or contributes genuinely new independent structure.

There is a second source-frame obstruction. For any completely multiplicative source phase `chi`, including a Dirichlet character,

\[
\prod_{j=1}^d\chi(u_j)
=\chi(m)
\qquad ((u_1,\ldots,u_d)\in\mathcal F_d(m)).
\tag{9}
\]

Hence the total source-character phase is **constant on every exact tangent fiber**. Redistribution can still change sieve/factor coefficients and individual coordinate phases, but it cannot create an independent oscillatory direction in the product character itself. This is the fixed-product specialization of the separability already identified in `MC-410`.

The correct negative conclusion is therefore:

> The exact tangent escape left by `MC-422` is too small at fixed factor depth to provide fixed-power multivariable bandwidth, and the completely multiplicative source phase is constant along it. Any polynomial-volume escape must move between product fibers, let factor depth grow, or exploit a different nonstationary/coefficient structure whose information is not just exact factor redistribution.

This does **not** rule out near-tangent motions that change the product within the short shell, zero-extended correlations that cross the shell boundary, growing-depth factorizations, or coefficient geometries whose useful state is not injectively parameterized by factor tuples. No improved Möbius estimate, character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Exact tangent motion is an exponent-allocation fiber

Write each factor as

\[
u_j=\prod_p p^{b_{p,j}},
\qquad b_{p,j}\ge0.
\tag{10}
\]

The condition `u_1\cdots u_d=m` is equivalent, prime by prime, to

\[
\sum_{j=1}^d b_{p,j}=a_p.
\tag{11}
\]

For one prime exponent `a_p`, the number of nonnegative ordered solutions of `(11)` is the stars-and-bars count

\[
\binom{a_p+d-1}{d-1}.
\tag{12}
\]

Different primes are independent, proving `(3)`.

This gives the exact discrete version of the tangent geometry from `MC-422`. In real logarithmic coordinates the surface `\sum_j\log u_j=\log m` has dimension `d-1`; in the integer arithmetic problem, however, the allowed tangent states are not a full Euclidean lattice. They are obtained by redistributing the finitely many prime exponents of `m` among the factor coordinates.

For square-free `m`, the picture is especially transparent. Each prime divisor chooses one of the `d` factors, so

\[
d_d(m)=d^{\omega(m)}.
\tag{13}
\]

The fiber can therefore be combinatorially large, but for fixed `d` it is still subpolynomial in `m`. The continuous tangent dimension by itself overstates the amount of arithmetic translation volume available at one exact product.

## 2. A self-contained subpolynomial bound

For each exponent `a>=0`, a weak composition of `a` into `d` parts is determined by the first `d-1` entries, and each such entry lies between `0` and `a`. Therefore

\[
\binom{a+d-1}{d-1}\le(a+1)^{d-1}.
\tag{14}
\]

Multiplying `(14)` over the prime powers of `m` proves `(4)`.

For completeness, the qualitative bound `tau(m)=m^{o(1)}` can be obtained without importing any zero information. Fix `epsilon>0` and choose `P` so large that `2<=p^epsilon` for every prime `p>P`. If `m=\prod p^{a_p}`, then for `p>P`,

\[
a_p+1\le2^{a_p}\le p^{\epsilon a_p}.
\tag{15}
\]

The contribution from the finitely many primes `p<=P` is at most

\[
(1+\log_2 m)^{\pi(P)}=m^{o(1)}.
\tag{16}
\]

Thus, for sufficiently large `m`,

\[
\tau(m)\le m^{2\epsilon}.
\tag{17}
\]

Since `epsilon` is arbitrary, `(5)` follows, and hence `(6)` follows from `(4)`.

Classical maximal-order theory is sharper. Pollack's 2020 paper on the `k`-fold divisor function records the established fixed-/slowly-growing-`k` bound

\[
\log d_k(n)
\le
(1+o(1))\log k\,\frac{\log n}{\log\log n}
\tag{18}
\]

in the regime `k=o(log n)`, building on Wigert and Norton. For fixed `d`, `(18)` again gives `d_d(n)=n^{o(1)}` and shows that the elementary estimate `(4)` is deliberately nonsharp but sufficient for the frontier test.

## 3. Consequence for multivariable positive bandwidth

The positive-kernel result `MC-419` rewards **distinct independent translation cells**: a rank-`r` box with side bandwidths `H_1,\ldots,H_r` can lower the universal Fejér floor according to `1/(H_1\cdots H_r)`. `MC-420` then shows that nominal ambient dimension does not count if those cells collapse onto a lower-rank lattice.

An exact factor-redistribution proposal has an even simpler counting test. If different translation parameters in `(7)` are supposed to represent genuinely different arithmetic states, `Phi` must be injective. Hence

\[
H_1\cdots H_r
\le |\mathcal F_d(m)|.
\tag{19}
\]

Combining `(19)` with `(6)` proves `(8)`. For every fixed `delta>0`, sufficiently large `m` therefore satisfy

\[
H_1\cdots H_r<m^\delta.
\tag{20}
\]

So an exact fixed-product lift cannot manufacture the polynomial bandwidth volume that the naive continuous tangent picture might suggest.

This is not a statement that the factorization fiber has rank zero. Prime-exponent transfers can create many independent combinatorial directions, and for highly composite `m` the number of states can be very large. The point is quantitative: at fixed factor depth their **total number of distinct states** is subpolynomial, so no stationary positive architecture can honestly credit a fixed-power number of independent cells from exact redistribution alone.

## 4. Exact source phase is constant on the fiber

For a Dirichlet character or any completely multiplicative `chi`,

\[
\chi(u_1)\cdots\chi(u_d)
=\chi(u_1\cdots u_d)
=\chi(m).
\tag{21}
\]

This remains valid when `m` is not coprime to the conductor: both sides are zero because at least one factor contains the offending prime.

Thus the fixed-product tangent fiber does not contain source-character oscillation in the **total** product phase. Individual factors may exchange character values, but their product is invariant. This matches `MC-410`, which proves that the raw factorable source phase is tensor-separable before a genuinely nonseparable operation such as translation, congruence, reciprocal phase, or dispersion is introduced.

The distinction matters for the frontier left by `MC-422`. Exact tangent redistribution solves the shell-normal bandwidth cost geometrically, but at the same time it freezes the very product character phase whose retention motivated the multivariable escape. Any benefit must therefore come from varying factor coefficients, from a transformed nonseparable phase, or from moving to a nearby product rather than remaining exactly tangent.

## Prior art and novelty boundary

The identity `(3)` is the classical `d`-fold divisor function, and the subpolynomial maximal order for fixed `d` is standard analytic-number-theory prior art. No novelty is claimed for stars-and-bars, the divisor bound, ordered-factorization counting, or complete multiplicativity.

A targeted literature audit on 20 September 2026 found Paul Pollack, *The maximal size of the k-fold divisor function for very large k*, Journal of the Ramanujan Mathematical Society **35** (2020), no. 4, 341–345, as a convenient modern primary anchor. Pollack defines `d_k(n)` exactly as the number of ordered products of `k` positive integers and records the Wigert/Norton maximal-order regime quoted in `(18)`. The original fixed-`k` theory is much older.

Matomäki and Teräväinen, *On the Möbius function in all short intervals*, J. Eur. Math. Soc. **25** (2023), 1207–1225, DOI `10.4171/JEMS/1205`, remains the arithmetic prior-art anchor inherited from `MC-422`: its Ramaré/Heath-Brown decomposition supplies genuine factor variables under a thin product condition, but it does not identify exact factor redistribution as a free stationary translation lattice.

The Mathia contribution is only the frontier consequence: combining the classical ordered-factorization count with the effective-bandwidth requirement of `MC-419`–`MC-422` closes the **exact fixed-product tangent** interpretation as a source of polynomial translation volume. No novelty is claimed for the ingredients themselves.

## Boundaries and falsification tests

- **Fixed factor depth is load-bearing.** The estimate `d_d(m)=m^{o(1)}` is uniform for fixed `d`, not for arbitrary rapidly growing `d`. A growing-depth proposal must redo the count with its actual `d(X)` and pay the decomposition/coefficients cost.
- **Exact product preservation is load-bearing.** A near-tangent move may change `m` while remaining inside `(X,X+Delta]`; then it can use many neighboring fibers and is not bounded by one `d_d(m)`. Such a proposal returns to the shell-overlap and normal-bandwidth accounting of `MC-422`.
- **Injectivity is the effective-bandwidth condition.** Reusing the same factor tuple under many formal shift labels does not create new Fourier cells. A noninjective parameterization must quotient by its collisions before applying `MC-419`.
- **Coefficient variation survives.** Sieve weights, dyadic cutoffs, prime-support restrictions, or Heath-Brown coefficients can vary across `mathcal F_d(m)`. The finding does not say the fiber is analytically useless; it says that state count and total character phase alone cannot provide polynomial independent bandwidth.
- **The source-phase statement concerns the total completely multiplicative phase.** A transformed phase such as `chi(u+v)`, `chi(uv+h)`, a reciprocal/Kloosterman phase, or a boundary-dependent correlation need not be constant and lies outside `(21)`.
- **The subpolynomial count is an upper bound, not a typical-size assertion.** Typical fibers may be much smaller; using maximal order makes the obstruction more generous to the escape route.
- **No analytic continuation is used.** The argument is finite multiplicative combinatorics plus the elementary divisor bound.

## Consequence for the research line

`MC-422` splits the factor-lift frontier into normal and tangent motion. The normal direction is expensive because a thin product shell allows little coordinate-axis bandwidth. `MC-423` now closes the most literal exact tangent response: a fixed-product integer fiber has only `d_d(m)=m^{o(1)}` states at fixed factor depth, and the completely multiplicative source phase is invariant across all of them.

The surviving tangent route must therefore be **near-tangent rather than exactly tangent**, or must introduce information beyond factor redistribution. The sharp next test is a concrete sheared/tilted family that is allowed to move across neighboring products inside the shell. Its effective cell count should be computed after collisions and boundary loss, and its transformed source phase must be written before Cauchy or completion. Only if that family achieves polynomial distinct-state volume while retaining a genuinely nonseparable arithmetic phase does it escape both `MC-422` and `MC-423`.