# MC-425 — Growing factor depth does not create polynomial Möbius sign channels

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · CLASSICAL-INGREDIENTS · FRONTIER-ADVANCE`

## Claim

Let `n <= X` be squarefree, and consider ordered factorizations

\[
n=u_1\cdots u_d
\]

with all active factors `u_j>1`. If each factor coordinate is retained only through its Möbius sign, then the total number of distinct source-sign vectors

\[
(\mu(u_1),\ldots,\mu(u_d))
\]

obtainable across all possible active depths is `X^{o(1)}`. Consequently, for every fixed `delta>0`, a factor lift whose source state at each coordinate is only `mu(u_j)` cannot create `X^delta` independent source channels from the factorization multiplicity.

## Exact derivation

Write `r=omega(n)`. Because `n` is squarefree, an active ordered factorization is equivalent to partitioning its `r` distinct prime factors into `d` nonempty labeled blocks. Therefore `d<=r`.

For each factor define

\[
a_j=\omega(u_j)\pmod 2.
\]

Then

\[
\mu(u_j)=(-1)^{a_j},
\qquad
\sum_{j=1}^d a_j\equiv r\pmod 2,
\]

so at a fixed active depth `d` every source-sign vector lies in one parity hyperplane of `{+1,-1}^d`. Hence there are at most

\[
2^{d-1}
\]

distinct Möbius-sign source vectors at that depth, regardless of how many ordered factorizations realize them.

Summing over all arithmetically possible active depths gives

\[
\sum_{d=1}^{r}2^{d-1}<2^r.
\]

For squarefree `n<=X`, the product of the first `r` primes is at most `n`. The crude bound `p_j>=j+1` therefore gives

\[
(r+1)!\le n\le X,
\]

and Stirling's formula implies

\[
r=O\!\left(\frac{\log X}{\log\log X}\right).
\]

Thus

\[
2^r=\exp\!\left(O\!\left(\frac{\log X}{\log\log X}\right)\right)=X^{o(1)}.
\]

Allowing factors equal to `1` does not change the conclusion after deleting unit factors and measuring **active depth**. Arbitrarily many named unit slots can inflate nominal depth, but their positions are not arithmetic source information unless a separate construction proves that those labels are intrinsic rather than padding or gauge.

## Relation to the current frontier

`MC-423` showed that exact product fibers have subpolynomial tangent volume at fixed factor depth. `MC-424` then showed that obtaining polynomial raw factor-state multiplicity requires factor depth growing at least roughly like a positive power of `log X`.

The present result prices the source-phase loophole left open there. Even if active depth is allowed to grow all the way to its arithmetic maximum `omega(n)`, the raw multiplicity of factor assignments collapses to only `X^{o(1)}` distinguishable source channels when every coordinate is remembered solely through its Möbius sign. Polynomial state multiplicity therefore does not become polynomial **Möbius-source complexity** merely by increasing factor depth.

This closes only the sign-only escape. A surviving factor-lift mechanism must retain richer arithmetic information per coordinate — for example sizes, residue data, characters, additive phases, or genuinely intrinsic coordinate relations — or prove that some labeled structure discarded by the sign projection is itself canonical and cancellation-relevant.

## Prior-art and novelty boundary

The ingredients are classical: squarefree ordered factorizations are assignments of prime factors to labeled blocks, `mu(u)=(-1)^{omega(u)}` on squarefree integers, and the maximal order of `omega(n)` is sublogarithmic. Large-`k` divisor-function literature concerns the much larger raw factor-state multiplicity and is adjacent to `MC-424`.

No number-theoretic novelty is claimed for these ingredients. The additional result here is the mechanism-specific no-go consequence: **raw growing-depth factor multiplicity cannot by itself supply polynomially many independent Möbius-sign source channels**.

## Limits and decisive test

This does not improve a bound for `M(x)`, rule out growing-depth lifts carrying richer per-factor arithmetic data, or show that every useful source variable must be independent. It also does not exclude mechanisms in which correlations among a subpolynomial family of source channels have additional analytic force.

A proposed factor-lift escape from `MC-424` now has a direct first-kill test: after removing unit padding, project each active factor to the exact source information the mechanism actually uses. If that information is only `mu(u_j)`, the total source-state family is `X^{o(1)}` and cannot supply a fixed polynomial channel count. A survivor must identify and justify the richer retained arithmetic structure explicitly.
