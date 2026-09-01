# MC-003 — Möbius–Liouville square-convolution threshold at one-half

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`.

## Claim

Let `lambda(n)=(-1)^Omega(n)` be the Liouville function and write

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
L(x)=\sum_{n\le x}\lambda(n).
\]

The classical square-divisor relation between Möbius and Liouville gives the exact identities

\[
\lambda(n)=\sum_{d^2\mid n}\mu\!\left(\frac{n}{d^2}\right),
\tag{1}
\]

and, by Dirichlet inversion of the square-indicator factor,

\[
\mu(n)=\sum_{d^2\mid n}\mu(d)\lambda\!\left(\frac{n}{d^2}\right).
\tag{2}
\]

Consequently,

\[
L(x)=\sum_{d\le \sqrt x} M\!\left(\frac{x}{d^2}\right),
\qquad
M(x)=\sum_{d\le \sqrt x}\mu(d)L\!\left(\frac{x}{d^2}\right).
\tag{3}
\]

These formulas have a sharp black-box transfer threshold at exponent `1/2`. If for some fixed `alpha>1/2`

\[
M(y)\ll y^\alpha,
\]

then (3) gives `L(x) << x^alpha`, and the converse implication holds with the same exponent. At `alpha=1/2` the same absolute-value argument loses a factor `log x`; below `1/2` it saturates at square-root size. Thus for every `epsilon>0`, a bound `M(x)=O_epsilon(x^(1/2+epsilon))` and the analogous Liouville bound are interchangeable by this elementary square-convolution alone.

When the power-cancellation-aware framework of Jung–Lemke Oliver (`MC-S7`) is specialized to the pair `(lambda,mu)`, it reproduces exactly the same threshold. In their convolution notation `g=f*h`, the prime-local generating functions are

\[
F_{\lambda,p}(z)=\frac1{1+z},
\qquad
F_{\mu,p}(z)=1-z.
\]

Hence

\[
H_{\lambda\to\mu,p}(z)
=\frac{1-z}{1/(1+z)}
=1-z^2,
\tag{4}
\]

while

\[
H_{\mu\to\lambda,p}(z)
=\frac{1/(1+z)}{1-z}
=\frac1{1-z^2}.
\tag{5}
\]

Therefore their strong `beta`-pretentious quantities satisfy

\[
H_\beta(\lambda,\mu)=\sum_p p^{-2\beta},
\tag{6}
\]

and

\[
H_\beta(\mu,\lambda)
=\sum_p\sum_{j\ge1}p^{-2j\beta}.
\tag{7}
\]

Both converge **if and only if** `beta>1/2`. The prime-power-sensitive distance `\widehat D_\beta` has the same threshold, since `mu(p)=lambda(p)=-1` but `|mu(p^k)-lambda(p^k)|=1` for every `k>=2`; its first nonzero layer is therefore the square layer `p^2`.

By contrast, Jung–Lemke Oliver's weighted prime-only distance `D_beta` is identically zero for this pair because Möbius and Liouville agree at every prime. Thus the extra information that distinguishes them is genuinely prime-power information, but for the natural Möbius/Liouville comparison its convergence begins exactly above the square-root boundary rather than creating a new source of cancellation below it.

## Exact square-convolution derivation

Let `q(n)` be the indicator that `n` is a perfect square. The standard divisor identity

\[
\sum_{d\mid n}\lambda(d)=q(n)
\]

is recorded in `MC-S9`. Since `1*lambda=q`, Möbius inversion gives

\[
\lambda=\mu*q,
\]

which is (1). The Dirichlet series of `q` is `zeta(2s)`, so its Dirichlet inverse is supported on squares with

\[
q^{-1}(d^2)=\mu(d).
\]

Hence

\[
\mu=\lambda*q^{-1},
\]

which is (2). Summing (1) and (2) over `n<=x` and changing the finite order of summation gives (3) without analytic continuation or zero information.

Now suppose `|M(y)|<=C y^alpha`. From (3),

\[
|L(x)|
\le Cx^\alpha\sum_{d\le\sqrt x}d^{-2\alpha}.
\]

The last sum is `O(1)` for `alpha>1/2`, `O(log x)` for `alpha=1/2`, and `O(x^(1/2-alpha))` for `alpha<1/2`. This yields

\[
L(x)\ll
\begin{cases}
x^\alpha,&\alpha>1/2,\\
x^{1/2}\log x,&\alpha=1/2,\\
x^{1/2},&\alpha<1/2,
\end{cases}
\tag{8}
\]

at the information level of an absolute bound on `M`. Applying the second identity in (3) and `|mu(d)|<=1` gives the identical transfer from `L` to `M`.

The threshold is not an artifact of the Jung–Lemke Oliver formalism: it is already forced by the square kernel whose mass is

\[
\sum_d d^{-2\alpha}.
\]

Their strong-pretentiousness threshold `beta>1/2` is the prime-local Euler-factor expression of the same convergence boundary.

## Power-cancellation-aware pretentiousness audit

Jung and Lemke Oliver define, for `g=f*h`,

\[
H_\beta(f,g)=\sum_p\sum_{k\ge1}\frac{|h(p^k)|}{p^{k\beta}}
\]

and prove that if `S_f(x) << x^alpha` and `f,g` are strongly `beta`-pretentious, then

\[
S_g(x)\ll x^{\max(\alpha,\beta)}.
\]

For `(lambda,mu)`, (6)–(7) show that one may take any `beta>1/2` but no `beta<=1/2`. Thus, if one already knew a fixed power bound for `L(x)` with exponent `alpha>1/2`, their theorem transfers essentially the same exponent to `M(x)` (and conversely). It does **not** generate such an exponent from the currently known Liouville input.

`MC-S8` records that the strongest standard unconditional Liouville estimate has Korobov–Vinogradov shape

\[
L(x)
\ll
x\exp\!\left(-c(\log x)^{3/5}(\log\log x)^{-1/5}\right).
\tag{9}
\]

This is `x^{1-o(1)}`, not `O(x^{1-delta})` for any fixed `delta>0`. Therefore it supplies no nontrivial fixed exponent `alpha<1` to the power-transfer theorem. At the RH scale, Humphries also records the classical equivalence

\[
RH
\iff
L(x)=O_\varepsilon(x^{1/2+\varepsilon}),
\]

so using an RH-scale Liouville estimate as the comparator input would merely move the original difficulty from Möbius to Liouville.

The alternative Jung–Lemke Oliver prime-only `D_beta` refinement does not escape this conclusion for `(lambda,mu)`: its distance is zero because the functions agree on primes, while their general non-completely-multiplicative transfer theorem still requires additional prime-power convolution control. The square layer is exactly where the missing information reappears.

## Prior art and novelty assessment

The divisor identities relating `mu` and `lambda`, the Liouville Dirichlet series `zeta(2s)/zeta(s)`, and the RH-equivalent Liouville summatory bound are classical (`MC-S8`, `MC-S9`). Jung–Lemke Oliver's strong pretentiousness, prime-power-sensitive distances, and power-cancellation transfer theorems are established prior art (`MC-S7`). No novelty is claimed for these ingredients.

The durable line-specific result is their exact specialization and comparison: for Möbius versus Liouville, the supposedly richer power-cancellation-aware datum is nontrivial precisely at prime powers, but its convergence threshold is `beta=1/2`, matching the elementary square-convolution kernel exactly. This resolves the immediate question raised after `MC-002`: the natural prime-power enrichment retains information that standard prime-only pretentiousness discards, but **does not provide an independent unconditional bootstrap toward the RH exponent**.

A targeted search found the classical Möbius/Liouville identities, the Jung–Lemke Oliver transfer framework, and standard Liouville summatory estimates. The scale matching above is therefore stored as a specialization/obstruction, not as a new theorem of analytic number theory.

## Boundaries and failure modes

This finding does **not** rule out all power-cancellation-aware pretentious methods for Möbius. It rules out the most immediate comparator route in which Liouville supplies the cancellation and prime-power-sensitive closeness transfers it to Möbius.

In particular, it does not exclude:

- a different comparator carrying independently provable fixed-power cancellation and a sufficiently small strong-pretentiousness exponent;
- a theorem using signed cancellation in the square-convolution sums rather than absolute values;
- prime-power observables that contain arithmetic relations beyond the scalar convergence of `H_beta` or `\widehat D_beta`;
- bilinear or multiscale information combined with the Jung–Lemke Oliver classification;
- an asymmetric transfer where one direction of the convolution has extra structure not captured by the generic theorem.

Nor does the `alpha=1/2` logarithmic loss in (8) show that an exact `O(sqrt(x))` statement cannot transfer more sharply with extra cancellation. The obstruction concerns the black-box information contained in a pointwise power bound plus the square kernel.

The decisive requirement for any continuation of this route is now stronger than the clue that motivated it: **exhibit a comparator or prime-power datum whose useful cancellation is independently controlled and whose transfer threshold is not merely the same square-root barrier encoded by the square convolution.**

## Relation to MC-002

`MC-002` showed that standard single-scale prime-only pretentious distance has only `O(log log x)` information mass and cannot feed a generic Halász exponential to polynomial saving. Jung–Lemke Oliver provide a legitimate enrichment designed specifically for power cancellation.

`MC-003` shows that this enrichment behaves nontrivially on Möbius: it detects the prime-power structure that `MC-002`'s metric misses. But for the canonical same-prime comparator `lambda`, that added structure is exactly the square layer and its threshold is exactly `1/2`. The obstacle has therefore moved from **insufficient prime-only dynamic range** to **lack of an independently easier comparator across the square-root transfer boundary**.

That is a genuine narrowing of the research frontier: further pretentious work should not revisit `mu` versus `lambda` as though prime-power sensitivity alone supplied new cancellation.