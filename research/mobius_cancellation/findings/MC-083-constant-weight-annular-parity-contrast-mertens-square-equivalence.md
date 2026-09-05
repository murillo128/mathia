# MC-083 — Constant-weight annular parity contrast is Mertens-square equivalent above the critical exponent

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let `a(n)` be any complex sequence with `|a(n)|<=1`, and write

\[
A_a(N)=\sum_{n\le N}a(n).
\]

Define the square-scale product-annulus sum

\[
U_a(N)
:=
\sum_{\substack{m,n\le N\\mn>N}}a(m)a(n)
\]

and the hyperbola interior

\[
D_a(N)
:=
\sum_{mn\le N}a(m)a(n).
\]

Then, exactly,

\[
\boxed{A_a(N)^2=U_a(N)+D_a(N)}
\tag{1}
\]

and the interior is universally cheap:

\[
\boxed{|D_a(N)|\le \sum_{m\le N}\left\lfloor\frac Nm\right\rfloor=O(N\log N).}
\tag{2}
\]

Consequently, for every fixed `alpha>1/2`,

\[
\boxed{
A_a(N)=O(N^\alpha)
\quad\Longleftrightarrow\quad
U_a(N)=O(N^{2\alpha}).
}
\tag{3}
\]

The endpoint `alpha=1/2` has the expected logarithmic floor from `(2)`, but the full epsilon-family is still equivalent:

\[
\boxed{
A_a(N)=O_\varepsilon(N^{1/2+\varepsilon})\ \text{for every }\varepsilon>0
}
\]

if and only if

\[
\boxed{
U_a(N)=O_\varepsilon(N^{1+\varepsilon})\ \text{for every }\varepsilon>0.
}
\tag{4}
\]

For `a=mu`, the annular quantity is exactly the constant-weight projection of the Huxley--Watt finite-cutoff coefficients from `MC-032`--`MC-033`:

\[
U_\mu(N)
=
\sum_{N<q\le N^2}c_N(q),
\qquad
c_N(q)=\sum_{\substack{mn=q\\m,n\le N}}\mu(m)\mu(n).
\tag{5}
\]

It is also an exact square-free parity contrast. Put

\[
e(n)=\frac{\mu(n)^2+\mu(n)}2,
\qquad
o(n)=\frac{\mu(n)^2-\mu(n)}2.
\tag{6}
\]

Thus `e` and `o` indicate square-free integers with even and odd numbers of prime factors, respectively, and `mu=e-o`. Therefore

\[
\boxed{
U_\mu(N)
=
\#\{\text{same-parity annular ordered pairs}\}
-
\#\{\text{opposite-parity annular ordered pairs}\}.
}
\tag{7}
\]

So the constant-weight product annulus certainly **retains parity**, but it does not create a cheaper cancellation carrier. For every `alpha>1/2`, a power estimate for `(7)` is equivalent, up to the elementary hyperbola interior, to the corresponding bound for `M(N)`. At the RH scale, `(4)` is exactly the usual epsilon-family Mertens target rewritten as an annular bilinear contrast.

The same calibration applies to Liouville with `a=lambda`: its constant-weight even/odd prime-factor parity contrast over `m,n<=N`, `mn>N` is equivalent above exponent `1/2` to the corresponding bound for `L(N)`.

Thus the first parity-sensitive annular statistic suggested by `MC-082` fails the independence test in the strongest possible elementary way. A surviving annular route must use a genuinely nonconstant source-forced weight or coupling—such as the reciprocal sawtooth/Fourier phase retained in `MC-032`—and prove cancellation that is not reducible to `(1)` plus a cheap hyperbola interior.

No improved estimate for `M(N)` or `L(N)` is claimed.

## 1. Universal hyperbola-complement identity

The full ordered square factors:

\[
\sum_{m,n\le N}a(m)a(n)
=
\left(\sum_{n\le N}a(n)\right)^2
=A_a(N)^2.
\tag{8}
\]

The square is partitioned disjointly by `mn<=N` and `mn>N`, which proves `(1)`.

Since `|a(m)a(n)|<=1`,

\[
|D_a(N)|
\le
\sum_{m\le N}\#\{n\le N:mn\le N\}
=
\sum_{m\le N}\left\lfloor\frac Nm\right\rfloor.
\tag{9}
\]

The harmonic-sum estimate gives `(2)`. No multiplicativity, prime distribution, zero-free region, or cancellation theorem is used.

This universal form is an important adversarial control: the constant-weight annulus is not made informative by Möbius multiplicativity. The collapse follows for every bounded sequence simply because the complement of the hyperbola fills the rest of the ordered square.

## 2. Power-exponent equivalence above one half

Assume first

\[
A_a(N)=O(N^\alpha)
\qquad(\alpha>1/2).
\]

Then `(1)` and `(2)` give

\[
U_a(N)
=A_a(N)^2-D_a(N)
=O(N^{2\alpha})+O(N\log N).
\]

Because `2alpha>1`, the second term is `O(N^{2\alpha})`, proving the forward implication in `(3)`.

Conversely, if

\[
U_a(N)=O(N^{2\alpha}),
\]

then

\[
|A_a(N)|^2
\le |U_a(N)|+|D_a(N)|
=O(N^{2\alpha})+O(N\log N)
=O(N^{2\alpha}),
\]

so `A_a(N)=O(N^alpha)`. This proves `(3)`.

At the endpoint, `(2)` alone gives only a `sqrt(log N)` loss when `U_a(N)=O(N)`. For the RH-style epsilon-family, however, the logarithm is harmless. If `A_a(N)=O_delta(N^{1/2+delta})` for every `delta>0`, choose `delta=epsilon/2` to get `A_a(N)^2=O_epsilon(N^{1+epsilon})`; equation `(2)` gives the same bound for `U_a`. Conversely, if `U_a(N)=O_delta(N^{1+delta})` for every `delta>0`, then `(1)`--`(2)` give `A_a(N)=O_delta(N^{1/2+delta/2})`; reparameterizing `delta` proves `(4)`.

## 3. Möbius parity response is exact but target-equivalent

For square-free `n`, `mu(n)=+1` when `omega(n)` is even and `mu(n)=-1` when `omega(n)` is odd. Equation `(6)` splits the square-free support into those two classes and gives

\[
\mu(m)\mu(n)
=
(e(m)-o(m))(e(n)-o(n)).
\tag{10}
\]

Summing `(10)` over the product annulus yields `(7)` exactly. Hence this statistic passes the basic parity-sensitivity test demanded by `MC-082`: unlike unsigned divisor densities, it changes sign between same- and opposite-parity pairs.

But equations `(1)`--`(4)` show that this is not enough. The statistic has retained parity by retaining essentially the square of the original global signed mean. Its apparently two-variable form does not distribute the Mertens burden into an independently estimable bilinear observable.

This gives a sharper calibration for the clue `CLUE-parity-sensitive-annular-transfer`: **parity sensitivity is necessary but not sufficient; the statistic must also avoid constant-weight hyperbola-complement recovery.**

## 4. Relation to the Huxley--Watt annular coefficient

`MC-032` groups the Huxley--Watt reciprocal Fourier modes through the finite-cutoff coefficient `c_N(q)`, and `MC-033` proves that essentially all of its `ell^1` mass lies in `N<q<=N^2` while each fixed product fiber is sign-coherent.

Equation `(5)` is the constant-product-weight projection of exactly that annular coefficient. It therefore supplies a useful baseline before attempting the source's nonconstant reciprocal weights:

- keeping only the annular coefficient and summing it with weight `1` retains parity but recovers `M(N)^2` modulo an `O(N log N)` interior;
- the product-fiber sign coherence of `MC-033` does not by itself create cancellation;
- any genuine escape must exploit variation of the source-forced phase/weight across product fibers, joint cancellation across Fourier modes, or signed coupling with the other Huxley--Watt terms before the constant-weight recovery becomes applicable.

This finding does not prove that the reciprocal-phase statistic is target-equivalent. It only kills the coarsest parity-sensitive projection and identifies what extra structure the nonconstant weight must supply.

## 5. Prior art and novelty boundary

The square-scale Möbius identities, sawtooth residual, and product-dependent quadratic structure are from Huxley and Watt, *Mertens Sums requiring Fewer Values of the Möbius function* (`MC-S24`). `MC-032`--`MC-033` already derive the finite-cutoff product coefficient used in `(5)`. Letendre's truncated Möbius convolution work (`MC-S25`) is adjacent but concerns a different one-sided divisor truncation.

The partition `(1)` and estimate `(2)` are elementary hyperbola bookkeeping; the implication `(3)` is immediate exponent accounting. A targeted literature check around Huxley--Watt, truncated Möbius convolution, and double Möbius sums found no basis for a novelty claim, and none is made. The durable value is line-specific falsification: it shows that the most direct constant-weight parity-sensitive annular observable is just a disguised global partial-sum square above the critical threshold.

## 6. Boundaries and decisive tests

- The obstruction is specific to the **constant** product weight on the complete annulus `m,n<=N`, `mn>N`. A nonconstant reciprocal, oscillatory, dyadic, or factor-sensitive weight need not satisfy `(1)`.
- The cheap interior bound is `O(N log N)`, so the exact fixed-exponent equivalence is stated only for `alpha>1/2`. The endpoint is handled only in the epsilon-family sense `(4)`.
- Equation `(7)` uses the square-free parity classes induced by Möbius. It does not claim that arbitrary sieve parity controls have the same support or the same annular counts.
- The result does not rule out Type-II or parity-sensitive sieve estimates. It says only that the unweighted complete-annulus contrast cannot serve as an independently cheaper input.
- A proposed annular statistic survives this obstruction only if its nonconstant weight prevents reduction to `A_a(N)^2` plus an interior of size `O(N log N)`, and its available estimate is independently weaker than the target partial-sum bound.

The exact identities can be falsified by direct finite summation for any bounded sequence. For Möbius, one may independently compare `(5)` with `M(N)^2-sum_{q<=N}(mu*mu)(q)` and compare `(7)` with direct even/odd square-free pair counts.

## Consequence for the research line

`MC-082` showed that unsigned local divisor densities erase prime-factor parity. The natural first repair is to retain a signed bilinear parity contrast. `MC-083` shows that the coarsest such repair—constant weight on the complete product annulus—overcorrects in the opposite direction: it retains the target global mean essentially intact, squared.

The live annular question is therefore narrower. A useful statistic must be parity-sensitive **and** source-forced **and** non-tautological under hyperbola-complement reconstruction. The reciprocal sawtooth/Fourier weights in `MC-032` satisfy the first two structural requirements and remain unclassified by this finding. The next decisive test is whether one of those nonconstant weighted annular sums admits an arithmetic estimate with a genuine exponent gain that does not already encode the corresponding Mertens bound.