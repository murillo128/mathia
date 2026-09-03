# MC-033 — Huxley–Watt annular coefficients are signed central-divisor counts with no product-fiber cancellation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The annular Fourier coefficient isolated in `MC-032`

\[
c_N(q)
:=
\sum_{\substack{mn=q\\m,n\le N}}
\mu(m)\mu(n)
\tag{1}
\]

has a much more rigid internal structure than a generic truncated convolution. Write a cube-free integer uniquely as

\[
q=a b^2,
\qquad a,b\ \text{square-free},
\qquad (a,b)=1.
\tag{2}
\]

Then

\[
\boxed{
c_N(ab^2)=\mu(a)R_N(a,b),
\qquad
R_N(a,b)
:=
\#\left\{d\mid a:\frac{ab}{N}\le d\le\frac{N}{b}\right\},
}
\tag{3}
\]

while `c_N(q)=0` whenever some prime cube divides `q`.

Thus every nonzero factor pair in one product fiber has **exactly the same Möbius sign**. There is no hidden cancellation among the different representations `q=mn` that are merged by the product quotient. In the annulus `N<q\le N^2`, the coefficient is a single sign `\mu(a)` times a nonnegative central-divisor count.

This coherence has an exact global consequence. Let

\[
Q_{\rm sf}(N):=\sum_{n\le N}\mu(n)^2
\tag{4}
\]

be the square-free counting function. Then product grouping preserves the full `\ell^1` mass of the pair coefficients:

\[
\boxed{
\sum_{q\le N^2}|c_N(q)|=Q_{\rm sf}(N)^2.
}
\tag{5}
\]

Since `MC-032` already identifies `c_N(q)=(\mu*\mu)(q)` for `q\le N`, elementary divisor counting gives

\[
\sum_{q\le N}|c_N(q)|=O(N\log N).
\tag{6}
\]

Using the classical square-free estimate

\[
Q_{\rm sf}(N)=\frac{6}{\pi^2}N+O(\sqrt N),
\tag{7}
\]

we therefore obtain

\[
\boxed{
\sum_{N<q\le N^2}|c_N(q)|
=
\frac{36}{\pi^4}N^2+O(N^{3/2}).
}
\tag{8}
\]

Equivalently, the finite-cutoff annulus carries a proportion

\[
1-O\!\left(\frac{\log N}{N}\right)
\tag{9}
\]

of the total absolute coefficient mass. The product quotient from `(m,n)` to `q=mn` is therefore not producing even an `\ell^1`-level compression of the Möbius pair mass at the frontier isolated by `MC-032`.

For the reciprocal Fourier mode

\[
Q_h^{\rm ann}(N)
=
\sum_{N<q\le N^2}
 c_N(q)
\sin\!\left(\frac{2\pi hN^2}{q}\right),
\tag{10}
\]

equation (3) gives the exact normal form

\[
\boxed{
Q_h^{\rm ann}(N)
=
\sum_{\substack{a,b\ {m square\!\!-\!free}\\(a,b)=1\\N<ab^2\le N^2}}
\mu(a)R_N(a,b)
\sin\!\left(\frac{2\pi hN^2}{ab^2}\right).
}
\tag{11}
\]

The only sign cancellation left in (11) is therefore **across distinct square-free kernels `a` and product fibers**, coupled to the reciprocal phase and the nonnegative balanced-divisor weight. Cancellation inside a fixed product fiber is identically absent.

This sharply narrows the Fourier escape in `MC-032`: a power gain cannot come from many factorizations of the same `q` cancelling after product grouping. It must come from cross-`q` arithmetic/phase organization, joint cancellation across `h`, or cancellation against other terms in the unsplit Huxley–Watt identity.

## 1. Cube-free normal form forces one phase per product fiber

Suppose a term in (1) is nonzero. Then both `m` and `n` are square-free, so every prime exponent in `q=mn` is at most two. Hence `q` is cube-free.

For cube-free `q`, split its prime factors according to their exponent:

- `a` is the product of primes occurring to exponent one;
- `b` is the product of primes occurring to exponent two.

This gives the unique decomposition (2). Every pair of square-free factors with product `ab^2` must contain every prime of `b` in **both** factors, while each prime of `a` occurs in exactly one factor. Consequently every nonzero ordered factorization has the form

\[
m=bd,
\qquad
n=b\frac{a}{d},
\qquad d\mid a.
\tag{12}
\]

Because `a`, `b`, `d`, and `a/d` have the required coprimalities,

\[
\begin{aligned}
\mu(m)\mu(n)
&=\mu(bd)\mu\!\left(b\frac{a}{d}\right)\\
&=\mu(b)^2\mu(d)\mu(a/d)\\
&=\mu(a).
\end{aligned}
\tag{13}
\]

The cutoff conditions `m,n\le N` become

\[
bd\le N,
\qquad
b\frac{a}{d}\le N,
\tag{14}
\]

or equivalently

\[
\frac{ab}{N}\le d\le\frac{N}{b}.
\tag{15}
\]

Summing the identical value `\mu(a)` over the admissible divisors proves (3).

There is also a useful geometric reading of the same count. Put

\[
T=\frac Nb.
\tag{16}
\]

Then `ab^2\le N^2` is equivalent to `T\ge\sqrt a`, and

\[
R_N(a,b)
=
\#\{d\mid a:a/T\le d\le T\}.
\tag{17}
\]

Thus `R_N(a,b)` counts divisor pairs of the square-free kernel `a` whose two complementary divisors both lie below the common cutoff `T`; equivalently it is a symmetric central-divisor count around `\sqrt a`. The Huxley–Watt annular coefficient is not an oscillating divisor sum inside one fiber: its oscillation is the single exterior sign `\mu(a)`.

For `q\le N`, the cutoff interval contains every divisor of `a`, so

\[
R_N(a,b)=\tau(a)=2^{\omega(a)}
\tag{18}
\]

and (3) recovers the classical local formula

\[
(\mu*\mu)(ab^2)=\mu(a)2^{\omega(a)}.
\tag{19}
\]

This is consistent with the interior identity already used in `MC-032`.

## 2. Product grouping preserves the entire absolute pair mass

Partition all ordered pairs `(m,n)` with `m,n\le N` by their product `q=mn`. By (13), the nonzero values `\mu(m)\mu(n)` in each fiber have the same sign. Hence the triangle inequality is an equality separately on every product fiber:

\[
|c_N(q)|
=
\sum_{\substack{mn=q\\m,n\le N}}
|\mu(m)\mu(n)|.
\tag{20}
\]

Summing (20) over `q\le N^2` gives

\[
\begin{aligned}
\sum_{q\le N^2}|c_N(q)|
&=
\sum_{m,n\le N}|\mu(m)\mu(n)|\\
&=
\left(\sum_{n\le N}\mu(n)^2\right)^2,
\end{aligned}
\tag{21}
\]

which proves (5).

For the interior, `c_N=\mu*\mu`, and without using Möbius cancellation,

\[
\begin{aligned}
\sum_{q\le N}|c_N(q)|
&\le
\sum_{mn\le N}\mu(m)^2\mu(n)^2\\
&\le
\sum_{m\le N}\left\lfloor\frac Nm\right\rfloor\\
&=O(N\log N).
\end{aligned}
\tag{22}
\]

Subtracting (22) from (21) and using the standard square-free count (7), recorded in `MC-S12`, proves (8). Since the denominator in (5) is asymptotic to `(36/\pi^4)N^2`, equation (9) follows as well.

The conclusion is stronger than the statement in `MC-032` that the low-product interior is cheap for the Fourier aggregate. The **absolute coefficient budget itself** is overwhelmingly annular. The difficult region is not merely where the cutoff is active; it is where essentially all product-fiber `\ell^1` mass lives.

## 3. Consequence for the reciprocal Fourier route

Define the weighted harmonic sine kernel

\[
S_H(x)
:=
\sum_{h=1}^H\frac{\sin(2\pi h x)}{\pi h}.
\tag{23}
\]

As used in `MC-032`, `S_H` is uniformly bounded. The annular part of the retained Fourier aggregate is therefore

\[
\mathcal F_H^{\rm ann}(N)
=
\sum_{N<q\le N^2}c_N(q)S_H(N^2/q).
\tag{24}
\]

Applying absolute values after product grouping gives only

\[
|\mathcal F_H^{\rm ann}(N)|
\ll
\sum_{N<q\le N^2}|c_N(q)|
\asymp N^2.
\tag{25}
\]

The same obstruction holds for an individual `Q_h^{\rm ann}`. Thus the natural product quotient identified by `MC-032` does not itself buy any power of `N`: equation (21) shows exactly why. The factor multiplicity does not self-cancel before the reciprocal phase is applied.

Equation (11) now identifies the surviving signed object more precisely. A useful estimate must exploit at least one of:

1. cancellation of the square-free-kernel signs `\mu(a)` against the reciprocal phases `N^2/(ab^2)` and the central-divisor weights `R_N(a,b)`;
2. cancellation among the signed modes as `h` varies before taking absolute values;
3. cancellation of the full Fourier residual against another term in the unsplit Huxley–Watt identity.

Replacing `c_N(q)` by a divisor-counting bound, averaging factor labels inside one `q`, or appealing to a generic multiplicity argument cannot produce the required gain because all those operations see the coherent mass in (20).

## 4. The sign coherence is not Möbius-specific enough to explain a power gain

The fiber argument survives a broad matched multiplicative control. Let `f` be multiplicative, supported on square-free integers, with `|f(p)|=1` on primes, and define

\[
c_{N,f}(q)
:=
\sum_{\substack{mn=q\\m,n\le N}}f(m)f(n).
\tag{26}
\]

For `q=ab^2` as in (2), every nonzero factor pair (12) contributes

\[
f(bd)f(ba/d)=f(b)^2f(a),
\tag{27}
\]

independent of `d`. Hence

\[
c_{N,f}(ab^2)=f(b)^2f(a)R_N(a,b),
\tag{28}
\]

and the analogue of (20) again holds. The product-fiber coherence is therefore forced by square-free support plus multiplicativity; it is not a discriminator peculiar to the rational Möbius signs.

This is an important falsification boundary for the next step. A proposal that explains cancellation only by saying that fixed-product Möbius factorizations are highly structured has not yet found the missing arithmetic input: the same coherence is present for many square-free-supported multiplicative comparators whose global sums have very different behavior.

## 5. Prior art and novelty assessment

The Huxley–Watt residual matrix, its sawtooth Fourier modes, and the reciprocal product phase are from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`; see `MC-S24`. `MC-032` already introduced the exact finite-cutoff coefficient (1) by grouping their product-dependent Fourier mode.

The cube-free local formula for the unrestricted convolution `\mu*\mu`, multiplicativity of Dirichlet convolution, and the square-free count used in (7) are classical. No novelty is claimed for them.

A targeted literature audit also found Patrick Letendre, *Truncated convolution of the Möbius function and multiplicative energy of an integer n*, Acta Arithmetica 195 (2020), 83–95, DOI `10.4064/aa190515-18-10`, arXiv `1903.05629`. Letendre studies the one-sided divisor truncation

\[
M(n,z)=\sum_{\substack{d\mid n\\d\le z}}\mu(d)
\tag{29}
\]

and moments related to divisor multiplicative energy. That is adjacent language but not the coefficient (1): the Huxley–Watt paired cutoff contains both `d` and its complementary factor, and equation (13) makes their Möbius product constant on the fiber. Therefore cancellation estimates for the one-sided truncated Möbius divisor sum cannot simply be imported as estimates for `c_N(q)`.

The literature audit did not establish the exact paired-cutoff `\ell^1` identity (5) as a named result, but absence from a targeted search is not evidence of novelty. The durable contribution here is a **line-specific structural classification** of the frontier created by `MC-032`: the annular coefficient is a signed central-divisor count, its product fibers are sign-coherent, and nearly all of its absolute coefficient mass lies in the annulus. These facts remove product-fiber cancellation as a possible source of the missing Fourier power gain.

## 6. Boundaries and decisive falsification tests

This finding does **not** prove that `Q_h^{\rm ann}(N)` is large. A sum may have `\ell^1` coefficient mass of order `N^2` and still exhibit strong cancellation after distinct `q`-fibers are combined with the reciprocal phase. Equations (8) and (25) are therefore an obstruction to triangle-inequality/product-grouping strategies, not a lower bound for the Fourier residual.

It also does not show that the central-divisor weights `R_N(a,b)` are arithmetically featureless. Their distribution may interact nontrivially with `\mu(a)` and with the reciprocal phases, and (11) is a legitimate smaller target for further analysis.

The exact statements can be falsified finitely:

1. for every `q\le N^2`, direct factor enumeration must agree with (3), including vanishing when `p^3\mid q`;
2. all nonzero pair contributions in a fixed product fiber must equal `\mu(a)`;
3. summing `|c_N(q)|` over `q\le N^2` must equal the exact square `Q_{\rm sf}(N)^2`;
4. the annular absolute mass must satisfy (8), using only the classical square-free count and the interior divisor bound;
5. the matched square-free-supported multiplicative family (26) must retain the same fiberwise phase coherence.

A counterexample to any of these identities would invalidate the finding. A successful estimate for (11) using cross-fiber reciprocal-phase cancellation would lie **outside** the negative conclusion and would be the natural continuation.

## Consequence for the research line

`MC-032` reduced the Huxley–Watt Fourier frontier from an arbitrary two-factor quadratic sum to the finite-cutoff product annulus. `MC-033` removes one further apparent escape: the many factorizations inside each annular product do not cancel each other at all. The product quotient preserves their entire absolute mass, and that mass is quadratically large.

The remaining Fourier question is correspondingly sharper. It is not whether factor multiplicity averages Möbius signs, but whether the signed central-divisor normal form (11) has **cross-fiber** cancellation strong enough to save nearly one power of `N` at the required Fourier resolutions, without using an input equivalent to the next-scale Mertens bound. Any next candidate should be tested directly against that normal form rather than against generic two-variable or generic truncated-convolution intuition.