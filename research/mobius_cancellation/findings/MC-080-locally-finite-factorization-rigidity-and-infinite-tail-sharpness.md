# MC-080 — Locally finite multiplicative Möbius factorizations are prime partitions, and bounded infinite tails are the sharp escape

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-079` classifies square-free-supported multiplicative factorizations of Möbius as partitions of the rational primes. The square-free hypothesis is stronger than the local algebra actually needs.

Let `r>=2`, and let

\[
f_1,\dots,f_r:\mathbb N\to\mathbb C
\]

be normalized multiplicative functions with

\[
f_1*\cdots*f_r=\mu.
\tag{1}
\]

Assume only that, for every prime `p` and every factor `j`, the prime-power sequence is eventually zero:

\[
\exists N_{j,p}<\infty\quad
f_j(p^\nu)=0\qquad(\nu>N_{j,p}).
\tag{2}
\]

Equivalently, every Bell series

\[
F_{j,p}(z)=\sum_{\nu\ge0}f_j(p^\nu)z^\nu
\tag{3}
\]

is a polynomial, with no uniform degree bound required across primes or factors.

Then for every prime `p` there is a unique index `j(p)` such that

\[
\boxed{F_{j(p),p}(z)=1-z,\qquad F_{i,p}(z)=1\ (i\ne j(p)).}
\tag{4}
\]

Consequently every factor is automatically square-free supported and the factors are exactly the prime-partition functions already classified in `MC-079`.

Thus allowing **any finite number of nonzero prime-power coefficients at each prime does not enlarge the multiplicative factorization class at all**. A non-prime-partition factorization must have an infinite prime-power tail in at least one local factor at every prime where the split is genuinely nontrivial.

This local-finiteness threshold is sharp even under strong boundedness. For every fixed real

\[
0<\alpha<1,
\tag{5}
\]

define multiplicative functions `a_alpha,b_alpha` by the prime-local Bell series

\[
A_p(z)=1-\alpha z,
\qquad
B_p(z)=\frac{1-z}{1-\alpha z}.
\tag{6}
\]

Then

\[
A_p(z)B_p(z)=1-z
\tag{7}
\]

at every prime, hence

\[
\boxed{a_\alpha*b_\alpha=\mu.}
\tag{8}
\]

Both factors are multiplicative and `1`-bounded. Explicitly,

\[
a_\alpha(p)=-\alpha,
\qquad
a_\alpha(p^\nu)=0\quad(\nu\ge2),
\tag{9}
\]

while

\[
b_\alpha(p^\nu)=-(1-\alpha)\alpha^{\nu-1}
\qquad(\nu\ge1).
\tag{10}
\]

Thus `b_alpha` has a nonzero geometric tail at every prime. Boundedness, multiplicativity, fixed prime-local rules, and exact convolution back to Möbius therefore do **not** fix the factorization gauge once infinite local tails are admitted.

Moreover the escape is analytically nonproductive for separate-factor estimation. The prime values are

\[
a_\alpha(p)=-\alpha,
\qquad
b_\alpha(p)=-(1-\alpha),
\tag{11}
\]

so the Landau--Selberg--Delange theorem retained as `MC-S14` gives nonzero constants `C_a(\alpha),C_b(\alpha)` such that

\[
\boxed{
\sum_{n\le x}a_\alpha(n)
\sim
C_a(\alpha)\,x(\log x)^{-1-\alpha},
}
\tag{12}
\]

and

\[
\boxed{
\sum_{n\le x}b_\alpha(n)
\sim
C_b(\alpha)\,x(\log x)^{-2+\alpha}.
}
\tag{13}
\]

Neither factor has any fixed power saving. The local infinite tail reopens factorization freedom, but the ordinary summatory functions remain on the same near-linear Selberg--Delange side of the boundary exposed by `MC-075`, `MC-078`, and `MC-079`.

No improved estimate for `M(x)` is claimed.

## 1. Bell-series degree rigidity

For a normalized multiplicative arithmetic function, the Bell series at a prime is the formal power series `(3)`. Classical Bell-series theory gives

\[
(f_1*\cdots*f_r)_p(z)
=
\prod_{j=1}^r F_{j,p}(z).
\tag{14}
\]

The Möbius Bell series is

\[
\mu_p(z)=1-z.
\tag{15}
\]

Therefore `(1)` implies

\[
\prod_{j=1}^rF_{j,p}(z)=1-z
\tag{16}
\]

for every prime `p`.

Under `(2)`, every `F_{j,p}` is a polynomial with constant term `1`. Since `\mathbb C[z]` is an integral domain,

\[
\deg\!\left(\prod_{j=1}^rF_{j,p}\right)
=
\sum_{j=1}^r\deg F_{j,p}.
\tag{17}
\]

The right side of `(16)` has degree one. Hence

\[
\sum_{j=1}^r\deg F_{j,p}=1.
\tag{18}
\]

All degrees are nonnegative integers, so exactly one factor has degree one and every other factor has degree zero. A degree-zero normalized Bell series is exactly `1`. The unique degree-one factor has constant term `1` and their product is `1-z`, so it must itself equal `1-z`. This proves `(4)`.

In particular, the local-finiteness assumption forces

\[
f_j(p^\nu)=0\qquad(\nu\ge2)
\]

for every factor after all: square-free support is a **consequence**, not an independent hypothesis, inside the locally finite class.

The global prime-partition classification now follows exactly as in `MC-079`: assign each prime to the unique factor carrying `1-z`, and multiplicativity determines all values.

## 2. Why finite higher-prime-power corrections cannot cancel

A tempting escape from `MC-079` is to let different factors carry a few `p^2,p^3,...` coefficients whose convolution cancels those higher terms. Equation `(17)` shows why this cannot work when the local tails terminate.

For example, with two factors

\[
F_p(z)=1+a_1z+\cdots+a_mz^m,
\qquad
G_p(z)=1+b_1z+\cdots+b_nz^n
\]

and `a_m b_n\ne0`, the coefficient of `z^{m+n}` in the product is the single nonzero product `a_m b_n`. It has no competing term capable of canceling it. Thus a polynomial product equal to `1-z` cannot contain two positive local degrees, or one positive local degree exceeding one.

This is stronger than checking the first few convolution equations separately. Arbitrarily many finite prime-power correction coefficients still collapse by the top-degree term.

## 3. Infinite local tails reopen a bounded continuum

Take `0<alpha<1`. From `(6)`,

\[
B_p(z)
=(1-z)\sum_{\nu\ge0}\alpha^\nu z^\nu
=
1+\sum_{\nu\ge1}(\alpha^\nu-\alpha^{\nu-1})z^\nu,
\]

which gives `(10)`.

The coefficient bounds are immediate:

\[
|a_\alpha(p^\nu)|\le1,
\qquad
|b_\alpha(p^\nu)|
=(1-\alpha)\alpha^{\nu-1}\le1.
\tag{19}
\]

Multiplicativity then gives

\[
|a_\alpha(n)|\le1,
\qquad
|b_\alpha(n)|\le1
\tag{20}
\]

for every `n`.

The factorization is also genuinely nontrivial for every `0<alpha<1`: neither local factor is `1` or `1-z`. At the endpoints, `alpha=0` and `alpha=1`, `(6)` degenerates to the two trivial prime allocations

\[
(1,1-z)
\qquad\text{or}\qquad
(1-z,1).
\]

Thus the local finite/infinite distinction is exact for this mechanism. Finite local support forces prime allocation; an infinite geometric tail is already enough to create a continuous family of bounded, multiplicative, fixed-rule factorizations.

This family is not the fractional-zeta family from `MC-075`. There the local factors are fractional powers `(1-z)^theta` and `(1-z)^{1-theta}`. Here one factor remains linear and the other is rational with a geometric tail. The two constructions are algebraically different but share the same first-order prime-average split.

## 4. The bounded infinite-tail family still has near-linear means

For `a_alpha`, equation `(9)` gives

\[
a_\alpha(n)=\mu(n)\alpha^{\omega(n)},
\tag{21}
\]

where `omega(n)` is the number of distinct prime divisors. Its prime-value average is exactly the constant parameter `-alpha` up to the classical prime-number-theorem error.

For `b_alpha`, the first prime coefficient in `(10)` is `-(1-alpha)`, so its prime-value average has parameter

\[
\beta=-(1-\alpha)=\alpha-1\in(-1,0).
\tag{22}
\]

Both functions are `1`-bounded, so `MC-S14` applies.

The nonvanishing leading constants can be audited directly at `s=1`. For the first factor,

\[
C_a(\alpha)
=
\prod_p
\left(1-\frac{\alpha}{p}\right)
\left(1-\frac1p\right)^{-\alpha}.
\tag{23}
\]

The logarithm of each Euler factor is `O_alpha(p^{-2})`, so the product converges to a finite positive value. Since `Gamma(-alpha)` is finite and nonzero for `0<alpha<1`, `(12)` follows with a nonzero constant after absorbing the Gamma factor into `C_a(alpha)`.

For the second factor,

\[
\sum_{\nu\ge0}\frac{b_\alpha(p^\nu)}{p^\nu}
=
\frac{1-p^{-1}}{1-\alpha p^{-1}},
\]

so the corresponding Euler constant is

\[
C_b(\alpha)
=
\prod_p
\frac{(1-p^{-1})^\alpha}{1-\alpha p^{-1}},
\tag{24}
\]

again up to the nonzero Gamma factor. The Euler products in `(23)` and `(24)` are reciprocal before the Gamma factors:

\[
\prod_p
\left(1-\frac{\alpha}{p}\right)
(1-p^{-1})^{-\alpha}
\cdot
\prod_p
\frac{(1-p^{-1})^\alpha}{1-\alpha p^{-1}}
=1.
\tag{25}
\]

The exponent in `(12)` is `-1-alpha`, while the exponent in `(13)` is

\[
(\alpha-1)-1=\alpha-2.
\]

Both are logarithmic savings from a linear main scale. For every fixed `eta>0`,

\[
x(\log x)^{-c}\ne O(x^{1-\eta})
\]

for fixed `c`, so neither factor distributes any Mertens-scale power cancellation into its separate ordinary partial sum.

At `alpha=1/2`, the two factors are balanced at the common scale

\[
x(\log x)^{-3/2},
\]

exactly the same logarithmic exponent as the symmetric fractional split in `MC-075` and the balanced prime partition in `MC-078`/`MC-079`, despite a third distinct local factorization geometry.

## 5. Prior art and novelty boundary

The Bell-series machinery is classical. Apostol, *Introduction to Analytic Number Theory* (1976), §2.16--§2.17, gives the Bell series of an arithmetic function, the uniqueness theorem for multiplicative functions, the Möbius Bell series `1-z`, and multiplication of Bell series under Dirichlet convolution. The polynomial-degree step `(17)`--`(18)` is elementary algebra. **No novelty is claimed for these abstract facts or for the rational identity `(6)`--`(7)`.**

A targeted literature search found the local formalism under the standard Bell-series language rather than a distinct named theorem asserting the exact locally-finite classification above. The durable value here is therefore a scope correction at the Mathia frontier: the support boundary left open by `MC-079` is not square-free versus nonsquare-free, but finite versus genuinely infinite prime-power Bell tails.

The asymptotic ingredient is also classical. `MC-S14` is the retained Landau--Selberg--Delange source for transferring constant prime averages in `(-1,0)` to nonzero near-linear summatory main terms. The function `a_alpha=mu alpha^omega` is a standard Selberg--Delange-type multiplicative family; no novelty is claimed for its asymptotic regime.

## 6. Boundaries and falsification tests

- **Local finiteness is the exact algebraic hypothesis used by the rigidity proof.** No uniform bound on `N_{j,p}` is required. The proof fails only when at least one Bell series at a prime has infinitely many nonzero coefficients or when multiplicativity is abandoned.
- **Infinite tails need not be large.** In `(10)` they decay geometrically and all coefficients remain bounded by one. Thus coefficient boundedness, absolute pointwise boundedness of the arithmetic functions, and fixed prime-independent local rules do not recover rigidity.
- **The construction is fixed-scale-independent.** No parameter moves with `x`; `alpha` is chosen once. The obstruction therefore does not rely on the moving-gauge issues treated earlier in the line.
- **The Selberg--Delange conclusion concerns separate ordinary partial sums.** It does not exclude a coupled signed observable involving `a_alpha` and `b_alpha` before separate absolute estimates are imposed.
- **The theorem treats finitely many convolution factors.** Infinite products of factors are not covered by the polynomial degree count across factor index.
- **The sharpness example does not classify all infinite-tail factorizations.** It proves only that the finite-support rigidity cannot be extended to all bounded multiplicative factors.

The rigidity theorem is falsified by any normalized multiplicative factorization of `mu` in which every local Bell series is polynomial but some prime is not assigned wholly to one `1-z` factor. Such an example would contradict degree additivity in `C[z]`.

The bounded sharpness statement is falsified if `(6)` fails to define multiplicative `1`-bounded arithmetic functions satisfying `(8)`, or if one of the claimed near-linear asymptotics has a zero leading coefficient. Equations `(7)`, `(10)`, and the convergent nonzero Euler products `(23)`--`(24)` provide direct audits.

## Consequence for the active frontier

`MC-079` correctly rules out all square-free-supported multiplicative attempts to distribute Möbius into independently power-cancellative factors, but its previous support boundary was too loose. **Finite prime-power corrections do not create an escape.** Any genuinely non-prime-partition multiplicative factorization must use an infinite local tail somewhere.

The explicit family `(6)` then shows that this structural price is cheap algebraically: a geometrically decaying, uniformly bounded tail already suffices. But it does not buy the desired analytic cancellation; both factors return to explicit Selberg--Delange near-linear means.

The remaining factorization frontier is therefore narrower. A successful route cannot rely merely on allowing a few higher prime powers, bounded local tails, or a fixed nontrivial local split. It must extract useful **coupled signed information** from infinite-tail factors, impose a substantially stronger source-natural restriction than bounded multiplicativity, or leave the multiplicative factorization framework entirely.