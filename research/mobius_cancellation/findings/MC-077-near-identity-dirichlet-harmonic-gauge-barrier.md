# MC-077 — Near-identity Dirichlet gauges cannot split a fixed Mertens power saving

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-073` and `MC-074` show that normalized factorizations

\[
a*k=\mu
\]

have a universal Dirichlet-convolution gauge freedom, while `MC-076` closes one natural scale-dependent escape: a generalized-divisor factor moving polynomially toward the convolution identity becomes coefficient-small, but its companion becomes equally close to Möbius at the same power scale.

The latter obstruction is not special to generalized divisor functions. There is an exact **near-identity neighborhood theorem** for arbitrary arithmetic gauges.

Let `a` be any arithmetic function with

\[
a(1)=1,
\qquad
a=\varepsilon+r,
\qquad r(1)=0,
\]

where `\varepsilon` is the Dirichlet-convolution identity. For a cutoff `X>=2`, define the truncated harmonic defect

\[
q_X(a):=\sum_{2\le n\le X}\frac{|r(n)|}{n}.
\tag{1}
\]

Let

\[
g:=a^{-1},
\qquad
b:=g*\mu,
\]

so that `a*b=\mu`, and write

\[
A(X)=\sum_{n\le X}a(n),
\qquad
B(X)=\sum_{n\le X}b(n).
\]

If

\[
q_X(a)<1,
\tag{2}
\]

then the finite Dirichlet-convolution geometry gives

\[
\boxed{
\sum_{2\le n\le X}\frac{|g(n)|}{n}
\le
\frac{q_X(a)}{1-q_X(a)}.
}
\tag{3}
\]

Consequently,

\[
\boxed{|A(X)-1|\le Xq_X(a),}
\tag{4}
\]

and, using only the trivial bound `|M(y)|<=y`,

\[
\boxed{
|B(X)-M(X)|
\le
X\frac{q_X(a)}{1-q_X(a)}.
}
\tag{5}
\]

Now allow a diagonal family of normalized gauges `a_X`, with the factorization and inverse recomputed at each cutoff, and suppose for some fixed `delta in (0,1)` that

\[
q_X(a_X)=X^{-\delta+o(1)}.
\tag{6}
\]

Then

\[
A_X(X)=1+O\!\left(X^{1-\delta+o(1)}\right),
\tag{7}
\]

while its exact companion satisfies

\[
B_X(X)=M(X)+O\!\left(X^{1-\delta+o(1)}\right).
\tag{8}
\]

Hence, at the level of fixed power exponents,

\[
\boxed{
B_X(X)=O_\varepsilon\!\left(X^{1-\delta+\varepsilon}\right)
\quad\Longleftrightarrow\quad
M(X)=O_\varepsilon\!\left(X^{1-\delta+\varepsilon}\right).
}
\tag{9}
\]

At `delta=1/2`, any near-identity gauge whose first factor is made automatically square-root-scale by **harmonic coefficient dilution** leaves the complementary factor Mertens-equivalent at exactly the same exponent. The cancellation burden has not been split; Dirichlet inversion is quantitatively stable in precisely the weighted coefficient norm naturally seen by the trivial Mertens estimate.

No multiplicativity, Euler product, Selberg–Delange asymptotic, analytic continuation, zero-free region, or estimate for `M` beyond `|M(y)|<=y` enters `(3)`--`(9)`.

No improved estimate for `M(X)` is claimed.

## 1. Coefficientwise Neumann inversion is finite

Because `a=\varepsilon+r` with `r(1)=0`, the formal inverse is

\[
g
=(\varepsilon+r)^{-1}
=\varepsilon-r+r*r-r*r*r+\cdots.
\tag{10}
\]

This identity is coefficientwise finite, so no analytic convergence assumption is hidden in it. If `r^{*j}(n)` is nonzero, then `n` admits a factorization

\[
n=n_1\cdots n_j
\]

with every `n_i>=2`. Therefore `n>=2^j`; for fixed `n`, all terms with `j>log_2 n` vanish. Equation `(10)` is simply the recursive Dirichlet inverse written as a finite geometric series in each coefficient.

For functions `u,v` with `u(1)=v(1)=0`, define the cutoff harmonic seminorm

\[
\|u\|_X:=\sum_{2\le n\le X}\frac{|u(n)|}{n}.
\]

Then

\[
\begin{aligned}
\|u*v\|_X
&\le
\sum_{\substack{dm\le X\\ d,m\ge2}}
\frac{|u(d)|\,|v(m)|}{dm}\\
&\le
\left(\sum_{2\le d\le X}\frac{|u(d)|}{d}\right)
\left(\sum_{2\le m\le X}\frac{|v(m)|}{m}\right)\\
&=
\|u\|_X\|v\|_X.
\end{aligned}
\tag{11}
\]

Thus

\[
\|r^{*j}\|_X\le q_X(a)^j.
\tag{12}
\]

Taking absolute values termwise in the coefficientwise finite expansion `(10)` and then summing over `n<=X` gives, by `(2)`,

\[
\begin{aligned}
\sum_{2\le n\le X}\frac{|g(n)|}{n}
&\le
\sum_{j\ge1}\|r^{*j}\|_X\\
&\le
\sum_{j\ge1}q_X(a)^j\\
&=
\frac{q_X(a)}{1-q_X(a)},
\end{aligned}
\]

which proves `(3)`.

The weight `1/n` is not decorative. It is exactly the weight created when a reciprocal-scale summatory identity is bounded only with `|M(X/d)|<=X/d`. This is why the same norm simultaneously controls the inverse and the error in the recovered Möbius sum.

## 2. The near-identity factor is small only by coefficient mass

Since `a(1)=1`, equation `(1)` gives

\[
\begin{aligned}
|A(X)-1|
&\le
\sum_{2\le n\le X}|r(n)|\\
&\le
X\sum_{2\le n\le X}\frac{|r(n)|}{n}\\
&=Xq_X(a),
\end{aligned}
\]

proving `(4)`.

This estimate deliberately uses no cancellation in `a`. If `q_X(a)` is polynomially small, a power saving in the first factor is already manufactured by shrinking its nonconstant coefficient mass toward the identity gauge. Such a bound therefore cannot by itself be counted as arithmetic cancellation.

## 3. The exact companion remains close to Möbius in the same norm

From the exact factorization,

\[
b=g*\mu.
\]

Summing through `X` gives

\[
\begin{aligned}
B(X)
&=
\sum_{d\le X}g(d)
\sum_{m\le X/d}\mu(m)\\
&=
M(X)+
\sum_{2\le d\le X}g(d)M(X/d).
\end{aligned}
\tag{13}
\]

Using only `|M(y)|<=y` and `(3)`,

\[
\begin{aligned}
|B(X)-M(X)|
&\le
X\sum_{2\le d\le X}\frac{|g(d)|}{d}\\
&\le
X\frac{q_X(a)}{1-q_X(a)},
\end{aligned}
\]

which is `(5)`.

Thus the same small parameter that makes `a` look power-cancellative by coefficient dilution forces the inverse perturbation `g-\varepsilon` to be small enough that the companion `b=g*\mu` differs from Möbius only at the matching power scale.

There is no hidden dependence on coefficients `a(n)` with `n>X`: the inverse coefficient `g(n)` depends only on divisors of `n`, so the entire estimate through cutoff `X` is determined by the prefix `a(1),...,a(X)`.

## 4. Diagonal exponent equivalence

Under `(6)`, one has `q_X(a_X)->0`, hence

\[
\frac{q_X(a_X)}{1-q_X(a_X)}
=X^{-\delta+o(1)}.
\]

Equations `(4)` and `(5)` immediately give `(7)` and `(8)`.

For every fixed `epsilon>0`, the error in `(8)` is eventually

\[
O\!\left(X^{1-\delta+\varepsilon/2}\right).
\]

Therefore an `O_epsilon(X^(1-delta+epsilon))` bound for `M(X)` gives the same bound for `B_X(X)`, and conversely the same bound for `B_X(X)` gives it for `M(X)` by the triangle inequality, after the usual harmless epsilon-halving. This proves `(9)`.

The statement is intentionally diagonal: the gauge itself may depend on `X`. That is the strongest version relevant to the escape tested by `MC-076`; fixing one arithmetic function is not required.

## 5. Relation to MC-076 and the factorization frontier

`MC-076` considered the special generalized-divisor gauge

\[
a=d_{-\eta},
\qquad
b=d_{-1+\eta},
\]

with `eta=eta(X)` tending to zero. Its coefficient estimate

\[
|d_{-\eta}(n)|\le\eta\qquad(n>1)
\]

implies

\[
q_X(d_{-\eta})
\le
\eta\sum_{2\le n\le X}\frac1n
\ll \eta\log X.
\]

Thus for polynomial motion `eta=X^{-delta+o(1)}`, the present theorem recovers the same exponent-level obstruction as `MC-076`, up to a subpolynomial logarithmic factor. What looked there like a special property of zeta-power factors is therefore an instance of a general local stability phenomenon of Dirichlet inversion around the identity.

Combined with the earlier frontier:

- `MC-073` shows that complete coupled recovery is universal;
- `MC-074` shows that unrestricted one-factor partial statistics are gauge-nonidentifiable;
- `MC-075` closes fixed interior symmetric fractional gauges by their classical near-linear means;
- `MC-076` closes polynomially moving fractional endpoint gauges;
- the present result closes **every** polynomially near-identity gauge whose smallness is witnessed by the truncated harmonic coefficient defect `(1)`.

The residual factorization route must therefore obtain useful cancellation from structure that is not merely proximity to the identity in this natural weighted norm.

## 6. Prior art and novelty boundary

The algebraic mechanism is classical. NIST DLMF §27.5, *Inversion Formulas* (`https://dlmf.nist.gov/27.5`), records Dirichlet convolution, the fact that arithmetic functions with nonzero value at `1` form an abelian group under it, the multiplicative subgroup, and Möbius inversion; its notes cite Apostol, *Introduction to Analytic Number Theory*, Chapter 2. These are already the classical anchors used by `MC-073` and `MC-074`.

The geometric-series inverse `(10)` is the standard formal-algebra expansion of an element `\varepsilon+r` with zero constant coefficient. The cutoff estimate `(11)` is an elementary weighted `l^1` convolution inequality. Banach-algebra methods for multiplicative arithmetic functions and Wiener-type inversion also have established prior art; see Lutz Lucht, *An application of Banach algebra techniques for multiplicative functions*, Math. Z. 214 (1993), 287–296 (`https://eudml.org/doc/174569`). No claim is made that weighted convolution inversion itself is new.

The durable Mathia result is the **frontier obstruction** obtained by combining these classical mechanisms with the exact Möbius recovery architecture: the same truncated harmonic defect that makes one arbitrary gauge polynomially close to the identity also makes its exact companion Mertens-close at the same power exponent. This is recorded as an exact control/generalization of `MC-076`, not as a new theorem of analytic number theory.

## 7. Boundaries and falsification tests

The result is exact but deliberately local in gauge space.

- Condition `(2)` is a sufficient near-identity hypothesis. The argument says nothing about gauges with `q_X(a)>=1`, even if their summatory function is small by genuine sign cancellation.
- Small `A(X)` alone does **not** imply small `q_X(a)`. The theorem attacks coefficient/norm dilution, not all possible sources of cancellation in the first factor.
- The factor `q/(1-q)` is the elementary geometric bound, not an assertion that the inverse actually saturates it.
- The diagonal family `a_X` may change with the cutoff. The theorem does not require a single fixed arithmetic function to realize all scales.
- Multiplicativity, boundedness, support restrictions, Euler-factor laws, characters, and other external gauge-fixing conditions may still create useful structure outside this near-identity neighborhood.
- The theorem does not rule out a genuinely coupled gauge-sensitive statistic that uses both factors and is not controlled merely through the separate absolute norms in `(4)`--`(5)`.
- It does not classify subpolynomial improvements within the same power exponent when `q_X=X^{-o(1)}`; the claim concerns a fixed positive power `delta`.
- No statement about analytic continuation of the Dirichlet series of `a`, `g`, or `b` is used or implied.

The finding is falsified if the coefficientwise inverse `(10)` fails, if the cutoff convolution inequality `(11)` fails, if `(3)` does not follow when `q_X<1`, or if the finite summatory identity `(13)` fails. All of these are finite algebraic inequalities independent of RH.

## Consequence for the active frontier

The moving fractional gauge of `MC-076` was not a special loophole. **Any gauge that approaches the Dirichlet identity polynomially in the truncated harmonic coefficient norm automatically transfers the same polynomial scale to its inverse perturbation, leaving the complementary factor equal to Möbius up to an error of that scale.**

For an RH-scale factorization strategy, making one factor cheap by shrinking it toward `\varepsilon` is therefore structurally self-defeating: at `q_X=X^{-1/2+o(1)}`, proving the matching square-root bound for the exact companion is already equivalent, at the exponent level, to the Mertens RH criterion.

A surviving comparator/factorization program must leave this harmonic near-identity neighborhood or introduce a coupled arithmetic estimate whose gain is not explained by inversion stability. The next useful candidate should therefore specify an externally justified gauge class and an observable whose bound comes from arithmetic cancellation rather than coefficient dilution.