# MC-079 — Square-free-supported multiplicative Möbius factorizations are exactly prime partitions

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-074` shows that unrestricted normalized factorizations of Möbius under Dirichlet convolution form a torsor, so a useful factorization needs an independently justified gauge restriction. `MC-078` then tests one natural externally fixed class: assign rational primes by fixed residue classes to disjoint square-free-supported multiplicative factors. The present result shows that the prime-allocation mechanism in `MC-078` is not merely an example inside the square-free-supported multiplicative class. It is the **entire class**.

Let `r>=2`, and let

\[
f_1,\dots,f_r:\mathbb N\to\mathbb C
\]

be normalized multiplicative functions such that every factor is square-free supported,

\[
f_j(p^\nu)=0\qquad(\nu\ge2),
\tag{1}
\]

and suppose

\[
\boxed{f_1*\cdots*f_r=\mu.}
\tag{2}
\]

Then for every prime `p` there is a **unique** index `j(p)` such that

\[
\boxed{f_{j(p)}(p)=-1,\qquad f_i(p)=0\ \ (i\ne j(p)).}
\tag{3}
\]

Consequently the sets

\[
P_j=\{p:j(p)=j\}
\tag{4}
\]

form a partition of the rational primes, and each factor is forced to be

\[
\boxed{
f_j(n)=
\begin{cases}
\mu(n),&\text{if every prime divisor of }n\text{ lies in }P_j,\\
0,&\text{otherwise}.
\end{cases}}
\tag{5}
\]

Thus **there is no prime-level sign freedom at all** inside a square-free-supported multiplicative convolution factorization of Möbius. Each rational prime carries the coefficient `-1` in exactly one factor and coefficient `0` in every other factor. Any attempt to obtain separate prime-sign cancellation in two or more factors must therefore abandon square-free support in at least one factor, abandon multiplicativity, or move to a genuinely coupled observable rather than separate factor sums.

There is also a regular-density analytic corollary that strictly generalizes the fixed residue-class calculation in `MC-078`. Suppose each prime set `P_j` has a positive weighted density

\[
0<\delta_j<1,\qquad \sum_{j=1}^r\delta_j=1,
\tag{6}
\]

with the strong prime-average regularity

\[
\vartheta_{P_j}(x):=
\sum_{\substack{p\le x\\p\in P_j}}\log p
=
\delta_j x+O_{A,j}\!\left(\frac{x}{(\log x)^A}\right)
\tag{7}
\]

for every fixed `A>0`. Then the Landau--Selberg--Delange theorem retained as `MC-S14` gives nonzero constants `C_j` such that

\[
\boxed{
\sum_{n\le x}f_j(n)
\sim
C_j\,x(\log x)^{-1-\delta_j}.
}
\tag{8}
\]

Hence no factor in a nondegenerate regular positive-density split has any fixed power saving:

\[
\sum_{n\le x}f_j(n)\ne O(x^{1-\eta})
\qquad(\eta>0\text{ fixed}).
\tag{9}
\]

For the balanced `r`-way split `\delta_j=1/r`, every factor has the same scale

\[
\boxed{x(\log x)^{-1-1/r}.}
\tag{10}
\]

Increasing the number of square-free-supported factors therefore makes the individual generic logarithmic saving **weaker**, not stronger. The exceptional Möbius exponent at the prime-average parameter `-1` appears only after all prime sectors are recombined.

No improved estimate for `M(x)` is claimed.

## 1. Local Euler-factor rigidity

Because `f_j` is multiplicative and square-free supported, its local Dirichlet-convolution generating polynomial at a prime `p` has degree at most one:

\[
F_{j,p}(z)=\sum_{\nu\ge0} f_j(p^\nu)z^\nu
=1+c_{j,p}z,
\qquad c_{j,p}:=f_j(p).
\tag{11}
\]

Dirichlet convolution of multiplicative functions multiplies these local factors. Equation `(2)` therefore forces

\[
\prod_{j=1}^r(1+c_{j,p}z)=1-z
\tag{12}
\]

for every prime `p`.

Let `m` be the number of nonzero coefficients among `c_{1,p},...,c_{r,p}`. If `m=0`, the left side of `(12)` is `1`, impossible. If `m>=2`, the left side has degree exactly `m`, because the coefficient of its highest power is the product of those `m` nonzero coefficients and cannot vanish. The right side has degree one. Hence necessarily

\[
m=1.
\]

The unique nonzero coefficient must then equal `-1` by comparison of the linear term. This proves `(3)`.

There is no possibility of canceling higher local coefficients between different square-free-supported factors: the highest-degree coefficient is a single nonzero product, not a sum. This is the point that makes the classification rigid even for complex-valued factors and for any fixed finite number `r` of factors.

## 2. Global classification by a partition of primes

Define `P_j` by `(4)`. Uniqueness in `(3)` makes the `P_j` pairwise disjoint and their union is the full prime set.

For a square-free integer

\[
n=p_1\cdots p_k,
\]

multiplicativity gives

\[
f_j(n)=\prod_{\ell=1}^k f_j(p_\ell).
\tag{13}
\]

If every `p_\ell` lies in `P_j`, each factor in `(13)` is `-1`, so

\[
f_j(n)=(-1)^k=\mu(n).
\]

If at least one prime divisor lies outside `P_j`, the corresponding local value is zero, hence `f_j(n)=0`. Nonsquare-free integers vanish by `(1)`. This is exactly `(5)`.

Conversely, every partition of the primes into sets `P_1,...,P_r` and the functions defined by `(5)` satisfy `(2)`, because at each prime exactly one local factor is `1-z` and all others are `1`. Thus `(3)`--`(5)` are a classification, not merely necessary conditions.

This also sharpens the gauge statement from `MC-074`: imposing multiplicativity plus square-free support cuts the full Dirichlet-convolution torsor down drastically, but what remains is still not a family of independently oscillating Möbius-like factors. It is exactly the combinatorial freedom to decide **which factor owns each prime**.

## 3. Regular prime partitions have only logarithmic mean cancellation

Fix a factor `f_j` and abbreviate `P=P_j`, `\delta=\delta_j`. From `(3)`,

\[
f_j(p)=-1_P(p).
\]

Thus `(7)` is equivalent to

\[
\sum_{p\le x} f_j(p)\log p
=-\delta x+O_A\!\left(\frac{x}{(\log x)^A}\right).
\tag{14}
\]

The function is multiplicative and `|f_j(n)|<=1`, so the prime-average hypothesis of the Granville--Koukoulopoulos Landau--Selberg--Delange theorem `MC-S14` applies with

\[
\alpha=-\delta\in(-1,0).
\tag{15}
\]

The corresponding Dirichlet series is

\[
F_j(s)=
\prod_{p\in P}(1-p^{-s})
\qquad(\operatorname{Re}s>1).
\tag{16}
\]

To audit the nonzero leading coefficient, compare it with `\zeta(s)^{-\delta}`. For real `s>1`,

\[
\log\!\bigl(F_j(s)\zeta(s)^\delta\bigr)
=
-\sum_p\frac{1_P(p)-\delta}{p^s}
+O\!\left(\sum_p p^{-2s}\right).
\tag{17}
\]

The strong weighted-density error `(7)` and partial summation make the first series in `(17)` converge as `s\to1+`; the second converges absolutely. Therefore

\[
0<\lim_{s\to1+}F_j(s)\zeta(s)^\delta<\infty.
\tag{18}
\]

Since `\Gamma(-\delta)` is finite and nonzero for `0<\delta<1`, the leading Landau--Selberg--Delange coefficient is nonzero, and `(8)` follows. The exponent is exactly

\[
\alpha-1=-1-\delta.
\]

Finally, for every fixed `\eta>0` and fixed `c`,

\[
\frac{x/(\log x)^c}{x^{1-\eta}}
=
\frac{x^\eta}{(\log x)^c}\longrightarrow\infty,
\]

which proves `(9)`.

The fixed-congruence-class split in `MC-078` is recovered by taking each `P_j` to be a union of reduced residue classes modulo a fixed modulus. The present statement shows that the analytic obstruction depends only on the regular first-order prime allocation, not on congruence classes specifically.

## 4. More factors do not distribute the Mertens power burden

For a balanced partition, `\delta_j=1/r`, equation `(8)` becomes `(10)` for every factor. The exponent of the logarithm is

\[
1+\frac1r.
\]

It decreases toward `1` as `r` grows. Thus splitting the primes among more square-free-supported multiplicative factors does not approach square-root cancellation in the ordinary summatory functions. It moves each individual factor toward the generic near-linear regime.

The mechanism is the same singular-parameter discontinuity already exposed by `MC-075` and `MC-078`. Each proper positive-density factor has prime-average parameter in `(-1,0)`, where the generic Landau--Selberg--Delange leading term is present. The full Möbius product has parameter `-1`, where `1/\Gamma(-1)=0` and the generic leading term disappears. The exceptional cancellation is created by **recombining all prime sectors**, not inherited as a power saving by the separate regular factors.

This is an obstruction to separate-factor estimation. It does not say that a coupled bilinear or multilinear expression involving several factors cannot exploit cancellation between their nonzero leading modes before absolute values are taken.

## 5. Prior art and novelty boundary

The local algebra is classical. Multiplication of prime-local generating series under Dirichlet convolution and the square-free local factor `1-z` for Möbius are standard consequences of multiplicativity and Möbius inversion. The classification `(12)`--`(5)` is an immediate polynomial-degree argument, and **no novelty is claimed for it as an abstract theorem**.

Square-free-supported multiplicative functions are already a direct object of the literature recorded in `MC-S16`, and `MC-078` records older Selberg--Delange literature for integers whose prime factors are restricted to prescribed prime sectors. A targeted prior-art check found no reason to treat the prime-partition classification as a new named number-theoretic theory; it should instead be regarded as the exact local normal form relevant to the current Mathia factorization frontier.

The analytic ingredient is likewise classical. `MC-S14` gives the Landau--Selberg--Delange transfer from a prime-value average `\alpha` to the corresponding partial-sum asymptotic, and `MC-078` already applies it to fixed residue-class prime allocations. The new durable content here is the **scope closure** relative to `MC-074`--`MC-078`: every square-free-supported multiplicative factorization is forced into a prime allocation, and every regular positive-density prime allocation lies on the same logarithmic side of the cancellation boundary.

## 6. Boundaries and falsification tests

The classification is exact, but its analytic corollary has deliberate boundaries.

- **Square-free support is essential.** If a factor may have nonzero `p^2,p^3,...` coefficients, its local series is no longer linear, and higher local terms can cancel between factors. Fractional-zeta gauges from `MC-075` are examples outside the square-free-supported class.
- **Multiplicativity is essential.** Nonmultiplicative convolution factors are not classified by independent prime-local polynomials.
- The result treats a fixed finite number `r` of normalized factors. Infinite products of convolution factors are outside the claim.
- The Landau--Selberg--Delange conclusion `(8)` requires the regular positive-density hypothesis `(7)`. Highly irregular prime partitions, zero-density sectors, or scale-dependent allocations are not ruled out by that corollary.
- If one sector has density `1` and the others density `0`, the split is asymptotically degenerate and may leave essentially all Möbius difficulty in one factor. The nondegenerate conclusion assumes every `\delta_j` lies strictly between `0` and `1`.
- The theorem concerns ordinary partial sums of the individual factors. It does not exclude coupled observables in which several factors are kept signed until after recombination.
- No statement here controls a scale-dependent partition uniformly in the scale parameter. Such a route must still pass the gauge-identifiability and moving-parameter audits already emphasized by `MC-074` and `MC-078`.

The exact classification is falsified if a square-free-supported multiplicative factorization of `\mu` exists for which two local prime coefficients are simultaneously nonzero, or for which the unique nonzero coefficient is not `-1`. Either would contradict the polynomial identity `(12)`. The regular-density corollary is falsified if `(7)` holds but `MC-S14` does not yield `(8)` with a nonzero leading coefficient; equation `(17)`--`(18)` provides the independent nonvanishing audit.

## Consequence for the active frontier

`MC-078` left three conceptual escapes: introduce prime-level sign cancellation inside the factors, use a coupled observable, or use a scale-dependent/irregular arithmetic allocation. The present classification removes an ambiguity from the first option.

**Prime-level sign cancellation cannot be introduced inside two or more factors while simultaneously retaining multiplicativity, square-free support, and exact convolution back to Möbius.** Under those three requirements, each prime is forced to belong wholly to one factor with coefficient `-1`, and every regular positive-density split has only logarithmic mean cancellation.

A surviving factorization route must therefore pay a visible structural price: allow prime-power coefficients, abandon multiplicativity, exploit a coupled signed statistic before estimating the factors separately, or formulate a genuinely irregular/scale-dependent prime allocation with an independently justified selection rule and a uniform analytic advantage. Merely refining how square-free prime sectors are divided cannot distribute the RH-scale Mertens burden.