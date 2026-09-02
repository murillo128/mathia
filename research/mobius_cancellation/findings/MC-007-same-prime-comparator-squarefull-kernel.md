# MC-007 — Same-prime comparators differ from Möbius through a squarefull kernel, with only small-prime reverse-transfer obstructions

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`.

## Claim

Let `g:N->C` be multiplicative, `|g(n)|<=1`, and suppose that

\[
g(p)=-1=\mu(p)
\]

for every prime `p`. Define

\[
h=\mathbf 1*g,
\]

where `\mathbf 1(n)=1`. Since `\mu*\mathbf 1=\varepsilon`, one has the exact convolution factorization

\[
g=\mu*h.
\tag{1}
\]

The kernel `h` has no prime layer at all:

\[
h(p)=0,
\qquad
h(p^k)=\sum_{j=2}^k g(p^j)\quad(k\ge2),
\tag{2}
\]

so `h(n)=0` unless `n` is squarefull/powerful, meaning that every prime dividing `n` occurs to exponent at least two. Moreover

\[
|h(p^k)|\le k-1.
\tag{3}
\]

Consequently its absolute Dirichlet series converges throughout

\[
\Re s>\frac12.
\tag{4}
\]

Thus every pointwise power bound for the Mertens function above the square-root exponent transfers automatically to **every** such same-prime comparator:

\[
M(x)=O(x^\alpha),\ \alpha>\frac12
\quad\Longrightarrow\quad
\sum_{n\le x}g(n)=O(x^\alpha).
\tag{5}
\]

The reverse transfer is almost as rigid. Write the local series

\[
G_p(z)=\sum_{k\ge0}g(p^k)z^k
      =1-z+\sum_{k\ge2}g(p^k)z^k,
\]

and

\[
H_p(z)=\frac{G_p(z)}{1-z}
      =\sum_{k\ge0}h(p^k)z^k.
\tag{6}
\]

For every prime `p>=5`, `G_p(z)` and hence `H_p(z)` are zero-free for `|z|<1/2`. Indeed, with `r=|z|<1/2`,

\[
\left|\sum_{k\ge2}g(p^k)z^k\right|
\le \frac{r^2}{1-r}
<1-r
\le |1-z|.
\tag{7}
\]

Since `|p^{-s}|<p^{-1/2}<1/2` for `p>=5` and `Re(s)>1/2`, **no prime `p>=5` can create a zero of the transfer kernel in that half-plane**. Any obstruction to absolutely inverting `h` above exponent `1/2` is therefore confined to the `p=2` and `p=3` Euler factors.

More precisely, for `p=2,3` let `r_p(g)` be the modulus of the nearest zero of `H_p(z)` in the open unit disk, with `r_p(g)=1` if there is no such zero, and define

\[
\vartheta(g)
=
\max\left(
\frac12,
-\frac{\log r_2(g)}{\log 2},
-\frac{\log r_3(g)}{\log 3}
\right).
\tag{8}
\]

If `k=h^{-1}` is the Dirichlet inverse, then

\[
\sum_{n\ge1}\frac{|k(n)|}{n^\sigma}<\infty
\qquad(\sigma>\vartheta(g)).
\tag{9}
\]

Hence

\[
\sum_{n\le x}g(n)=O(x^\alpha),\ \alpha>\vartheta(g)
\quad\Longrightarrow\quad
M(x)=O(x^\alpha).
\tag{10}
\]

In particular, if the two small-prime local factors are zero-free in

\[
|z|<2^{-1/2},
\qquad
|z|<3^{-1/2},
\tag{11}
\]

respectively, then `\vartheta(g)=1/2` and all exponents strictly above `1/2` transfer in both directions. For this large natural class of same-prime comparators,

\[
\forall\varepsilon>0:\quad
\sum_{n\le x}g(n)=O_\varepsilon(x^{1/2+\varepsilon})
\]

is therefore equivalent, through the elementary convolution alone, to the corresponding Möbius bound and hence to RH.

The important obstruction is structural: **changing only the prime-power values while retaining `g(p)=mu(p)` cannot move the large-prime transfer threshold away from `1/2`. Any failure of reverse transfer above `1/2` must be carried by finitely many small-prime local factors, not by a new global prime-power cancellation mechanism.**

## 1. Squarefull support and the forward transfer

Because `h=1*g` is multiplicative,

\[
h(p^k)=1+g(p)+\cdots+g(p^k).
\]

The shared prime value `g(p)=-1` cancels the first two terms, giving (2). If a positive integer `n` contains some prime to exponent exactly one, multiplicativity then forces `h(n)=0`. Thus the convolution correction from Möbius to any same-prime comparator begins at the square layer.

For `sigma>1/2`, put `r_p=p^{-\sigma}`. From (3),

\[
\sum_{k\ge2}|h(p^k)|r_p^k
\le
\sum_{k\ge2}(k-1)r_p^k
=
\frac{r_p^2}{(1-r_p)^2}.
\tag{12}
\]

The right side is `O(p^{-2 sigma})` uniformly for large `p`, so summing it over the primes converges. The Euler product for the absolute Dirichlet series of `h` therefore converges, proving (4).

Summing (1) gives

\[
S_g(x):=\sum_{n\le x}g(n)
=
\sum_{d\le x}h(d)M(x/d).
\tag{13}
\]

If `|M(y)|<=C y^alpha` with `alpha>1/2`, then

\[
|S_g(x)|
\le
Cx^\alpha
\sum_{d\le x}\frac{|h(d)|}{d^\alpha}
\ll_g x^\alpha,
\]

which is (5). No zero-free region or analytic continuation is used.

## 2. Why only `2` and `3` can obstruct the reverse kernel above one-half

The local factorization corresponding to (1) is

\[
G_p(z)=(1-z)H_p(z).
\tag{14}
\]

Equation (7) proves directly that `G_p` has no zero in `|z|<1/2` for any allowed prime-power values. This is a uniform statement over the entire comparator class, not a property of Liouville alone.

For `p>=5` and `sigma>1/2`, the evaluation radius `r=p^{-sigma}` lies below `1/2`. Also, if

\[
U_p(z)=H_p(z)-1,
\]

then its coefficient `l^1` norm at radius `r` satisfies

\[
\|U_p\|_r
\le \frac{r^2}{(1-r)^2}.
\tag{15}
\]

For all sufficiently large `p` this is at most `1/2`, so the geometric inverse

\[
H_p^{-1}=1-U_p+U_p^2-\cdots
\]

has an absolutely summable coefficient norm `O(p^{-2 sigma})`. The finitely many remaining primes `p>=5` are harmless because (7) gives a zero-free disk larger than the evaluation radius. Therefore the infinite-prime part of the inverse Euler product is absolutely convergent for every `sigma>1/2`.

At `p=2,3`, boundedness alone does not force zero-freeness at the larger radii `p^{-1/2}`. The radius of convergence of the Taylor series of `1/H_p` is determined by the nearest zero of `H_p` in the unit disk. This gives exactly the extra thresholds in (8), and because there are only two such local factors, no further global obstruction appears. Hence (9).

Since `h(1)=1`, its Dirichlet inverse `k` exists and

\[
\mu=g*k.
\tag{16}
\]

Summing (16) and applying an assumed bound `|S_g(y)|<<y^alpha` with `alpha>vartheta(g)` gives

\[
|M(x)|
\le
x^\alpha
\sum_{d\le x}\frac{|k(d)|}{d^\alpha}
\ll_g x^\alpha,
\]

which proves (10).

## 3. The small-prime exception is genuine

The small-prime qualification cannot simply be deleted. At one chosen prime `p`, set

\[
g(p^k)=-1\qquad(k\ge1).
\]

Then

\[
G_p(z)
=1-z-z^2-z^3-\cdots
=\frac{1-2z}{1-z},
\]

so

\[
H_p(z)=\frac{1-2z}{(1-z)^2}
\tag{17}
\]

has a zero at `z=1/2`. At `p=2` this produces local threshold `1`; at `p=3` it produces threshold

\[
\log_3 2\approx0.6309.
\]

One may define the remaining prime-power values independently, for example by taking the Möbius local factor `1-z` at every other prime, so this is a valid `1`-bounded multiplicative same-prime comparator. The reverse-transfer failure can therefore be a real finite-prime effect.

This example is the same kind of phenomenon emphasized by Jung and Lemke Oliver (`MC-S7`): their power-cancellation transfer theorems need a separate small-prime/convolution convergence condition because ordinary pretentious distance can ignore a destructive local factor. The present specialization shows that, once all prime values are fixed to the Möbius values, that issue is confined uniformly to primes `2` and `3` above the square-root line.

## 4. Consequence for the comparator escape left open by MC-003

`MC-003` showed that the canonical same-prime comparator `lambda` differs from Möbius through the square kernel and that the transfer threshold is exactly `1/2`. It left open the possibility that another comparator agreeing with Möbius on primes might have independently easier power cancellation and a better prime-power transfer.

The present result sharply narrows that possibility. For **every** `1`-bounded multiplicative same-prime comparator:

- the forward correction is supported on squarefull numbers;
- its absolute mass begins at exponent `1/2`;
- all primes `p>=5` are automatically invertible above `1/2`;
- a tame `p=2,3` local factor makes RH-scale cancellation of the comparator equivalent to RH-scale cancellation of Möbius.

Thus a same-prime comparator cannot evade the square-root barrier through a diffuse collection of clever higher-prime-power values. To be genuinely different in the reverse direction, it must exploit an exceptional local factor at `2` or `3`, or else abandon exact agreement with Möbius at the primes.

That does not prove such comparators are useless. A proof of RH-scale cancellation for any tame comparator would itself prove RH and might conceivably be easier by a different method. The negative result is narrower: **prime-power enrichment alone does not create a logically weaker global target once the prime layer is fixed to Möbius and the two small Euler factors are nonpathological.**

## Prior art and novelty assessment

Dirichlet convolution, local prime-power generating series, and the fact that first disagreement at `p^2` creates a square-root convergence threshold are classical mechanisms. Jung–Lemke Oliver (`MC-S7`) already formulate power-cancellation transfer in terms of a convolution `g=f*h`, explicitly require convergence conditions controlling small primes, and explain that prime-only pretentiousness is insufficient for non-completely-multiplicative functions. Their paper is therefore the closest prior art and supplies the correct conceptual boundary.

No novelty is claimed for convolution algebra or for Bell-series/Euler-factor manipulation. A targeted search for same-prime multiplicative comparators, squarefull convolution corrections, and power-cancellation transfer did not locate a stronger theorem that makes this line-specific specialization unnecessary.

The durable contribution here is the exact **uniform specialization to the Möbius prime layer**: agreement `g(p)=mu(p)` forces the transfer kernel onto squarefull support; boundedness alone gives absolute convergence above `1/2`; and the elementary `|z|<1/2` zero-free estimate proves that every possible reverse-transfer obstruction in `Re(s)>1/2` is localized to the two Euler factors at `2` and `3`. This is stored as a structural obstruction, not as a new theorem of analytic number theory.

## Boundaries and falsification tests

This finding does **not** claim that every comparator with `g(p)=-1` is as difficult to study as Möbius by every method. It establishes an exact transfer equivalence only above the kernel threshold described by `vartheta(g)`.

It also does not exclude:

- comparators that change the prime values as well as prime powers;
- deliberately singular `p=2` or `p=3` local factors for which `vartheta(g)>1/2`;
- signed convolution arguments that beat the absolute-value transfer even when the inverse kernel has large absolute mass;
- unbounded multiplicative comparators, for which (3), (7), and the uniform Euler estimates no longer apply;
- methods using additional structure not expressible as the same-prime convolution alone.

The decisive falsification test for the main structural claim is local: produce a `1`-bounded multiplicative `g` with `g(p)=-1` for all primes for which either the forward kernel `1*g` has non-squarefull support, its absolute Dirichlet series fails to converge at some `sigma>1/2`, or a prime `p>=5` contributes a zero to `H_p(p^{-s})` with `Re(s)>1/2`. Equations (2), (12), and (7) rule out these three possibilities directly.

A proposed comparator route should therefore report its two small-prime factors explicitly. If both satisfy (11), proving RH-scale cancellation for that comparator is not a weaker surrogate problem: by (10) it already proves the RH-scale Möbius estimate.

## Relation to the obstruction chain

`MC-002` showed that a standard prime-only pretentious scalar has insufficient dynamic range for polynomial cancellation. `MC-003` showed that adding prime-power information distinguishes Möbius from Liouville but reproduces the square-root threshold. `MC-007` generalizes the latter obstruction from Liouville to the whole `1`-bounded multiplicative class with the same Möbius prime values and identifies exactly where the generic reverse transfer can still fail.

The remaining pretentious/comparator frontier is therefore no longer simply "find a better same-prime comparator." A viable route must either exploit a mathematically meaningful small-prime singularity, change the prime layer, use signed cancellation inside the squarefull convolution, or introduce a genuinely different multiscale/bilinear datum.