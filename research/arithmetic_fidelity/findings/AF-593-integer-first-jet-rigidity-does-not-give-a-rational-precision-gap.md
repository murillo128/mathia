# AF-593 — Integer first-jet rigidity does not give a rational precision gap

## Status and claims

EXACT-DERIVED · LITERATURE+DERIVED · SOURCE-CATEGORY-BOUNDARY · NEGATIVE/OBSTRUCTION · NO-GENERAL-NOVELTY-CLAIM

For a finite set `S` of ordinary primes and a finite collection `G` of
generators greater than one, put
\[
 H_G(z)=\sum_{g\in G}g^{-1-z}-\sum_{p\in S}p^{-1-z}.
 \tag{1}
\]
Coefficients are one; a collection with multiplicities counts each occurrence.
The first regular endpoint jet is the pair `(H_G(0),H_G'(0))`.

**Integer rigidity.** If every `g` is an integer and
\[
 H_G(0)=H_G'(0)=0,
 \tag{2}
\]
then `G=S`, including multiplicities. Thus distinct composite integer
replacements cannot match this jet, regardless of their number or range.

**No rational finite-precision bound on turning complexity.** Fix
`Y>2`, integers `m,N>=1`, `delta>0`, `tau_*>0`, and `0<eta<3/4`.
There are finite sets `S` of primes above `Y` and `G` of distinct nonintegral
positive rational numbers above `Y` such that
\[
 H_G(0)=0,\qquad
 \max_{1\le j\le m}|H_G^{(j)}(0)|<\delta,
 \tag{3}
\]
while the simple unit-weight source
\[
 Q(s)=\sum_{q\in(\mathbb P\setminus S)\cup G}q^{-s}
\]
has at least `N` distinct strict local minima below `eta`, separated by
values above `3/4`, for the crossover
\[
 F_Q(\tau)=\frac{e^{B_1}}{2\tau}
                 E_1^{-1}(Q(1+2\tau)),\qquad 0<\tau<\tau_*.
 \tag{4}
\]
Here `B_1` is the reciprocal-prime Mertens constant and
`E_1(a)=integral_a^infinity exp(-t)dt/t`, with its positive decreasing
inverse. Both endpoint limits remain `F_Q(0+)=1` and
`F_Q(infinity)=exp(B_1)log 2`. The generalized Euler product retains the
zeta zeros with multiplicity in the open critical strip.

The second claim transfers
[[research/arithmetic_fidelity/findings/AF-592-remote-unit-weight-edits-repair-finite-endpoint-jets|AF-592]]
to rational generators with **approximate**, not exact, nonconstant jets.
It follows that no positive tolerance on a fixed finite endpoint jet bounds
crossover turning complexity in this rational class. It does **not** decide
whether nonintegral rational replacements can satisfy (2) exactly. That is
the remaining question in
[[research/arithmetic_fidelity/clues/CLUE-rational-unit-weight-first-jet-rigidity]].

## Prime-log coordinates and integer rigidity

For each prime `ell`, let `v_ell` be its signed valuation on positive
rationals. Unique factorization proves rational linear independence of
distinct prime logarithms: clearing the denominators in a finite rational
relation and exponentiating gives a product of integer prime powers equal
to one, so every exponent vanishes.

Consequently, for rational `G`, `H_G'(0)=0` is equivalent to the finite
system
\[
 \sum_{g\in G}\frac{v_\ell(g)}g
       =\frac{\mathbf1_{\ell\in S}}\ell
       \quad\hbox{for every prime }\ell.
 \tag{5}
\]
Only primes occurring in `S` or in numerators or denominators of `G` need
checking. No independence of products of logarithms is assumed.

If every `g` is an integer, its valuations are nonnegative. Summing (5)
over the finite prime support yields
\[
 \sum_{g\in G}\frac{\Omega(g)}g=\sum_{p\in S}\frac1p,
 \qquad \Omega(g)=\sum_\ell v_\ell(g)\ge1.
 \tag{6}
\]
Subtract the mass equality in (2):
\[
 \sum_{g\in G}\frac{\Omega(g)-1}g=0.
 \tag{7}
\]
Every summand is nonnegative, hence every `g` is prime. Returning to (5)
then fixes its multiplicity to one for primes in `S` and zero otherwise.
This proves integer rigidity without any equal-cardinality, subdyadic,
Euler-product-matching, or prime-gap hypothesis.

For reduced rationals `g=a/b`, the corresponding identity is instead
\[
 \sum_{g=a/b\in G}\frac b a
       \bigl(\Omega(a)-\Omega(b)-1\bigr)=0.
 \tag{8}
\]
The summands need not be nonnegative. For example `9/8>1` has
`Omega(9)-Omega(8)=-1`. Even value one does not force primality:
`25/3` has signed value one. Thus (7)'s decisive implication cannot be
reused for rationals. Equations (5) and (8) are necessary arithmetic
constraints, not an existence theorem.

The Robin comparison RE-271 motivates checking this category
boundary, but supplies no theorem used here. Its invariant is an Euler
product, and its integer spacing and subdyadic hypotheses are different.

## Exact rational feasibility has a finite integer certificate at fixed denominator

This gives a precise alternative to testing small numerical logarithmic
residuals. Fix an integer `D` divisible by every prime in `S` and by the
reduced numerator of every `g`. Put
\[
 n_g=D/g\in\mathbb N,\qquad r_p=D/p,\qquad
 M_D=\sum_{p\in S}r_p.
\]
Then (2) is equivalent to
\[
 \sum_{g\in G}n_g=M_D,\qquad
 \sum_{g\in G}n_g v_\ell(n_g)
       =\sum_{p\in S}r_p v_\ell(r_p)\quad(\hbox{all }\ell),
 \tag{9}
\]
or, equivalently, the mass equation and the integer identity
\[
 \prod_{g\in G}n_g^{n_g}=\prod_{p\in S}r_p^{r_p}.
 \tag{10}
\]
Indeed `log g=log D-log n_g`, and the `log D` terms cancel by mass.
For a prime not dividing `D`, the right side of (9) is zero, while its
left summands are nonnegative. Thus every prime factor of every `n_g`
must divide `D`.

For the clue's class, the remaining exact conditions are that the `n_g`
are distinct, `1<=n_g<D/Y`, and `n_g` does not divide `D` (so `D/n_g`
is nonintegral). For fixed `S,D,Y`, (9) is a finite zero-one selection
problem over those integers whose prime factors divide `D`. Conversely,
any such solution gives an exact admissible rational certificate. All
positive rational solutions occur for some `D`; failure at finitely many
denominators proves no general nonexistence statement.

This reduction is also the classical equal-entropy identity. For nonempty
`S`, with common mass `M=sum 1/p`, the probabilities `pi_g=1/(Mg)` satisfy
\[
 \mathcal H(\pi)=\log M+\frac1M\sum_g\frac{\log g}{g}.
 \tag{11}
\]
Matching mass and first derivative therefore matches the Shannon entropies
of these two rational distributions. Equal entropy is not being treated as
identification of the distributions.

## Rational approximation inside the exact mass hyperplane

Let `G_*={g_1,...,g_k}` be any fixed finite distinct nonintegral real
replacement set above `Y>1` with rational reciprocal mass `A`. Set
`x_i=1/g_i`, so `sum x_i=A`. The hyperplane
\[
 \sum_{i=1}^k x_i=A
 \tag{12}
\]
has rational points arbitrarily near `x`: choose its first `k-1`
coordinates rational and set the last to `A` minus their sum. When `k=1`,
the coordinate is already rational. Small neighborhoods preserve positivity,
the upper bound `x_i<1/Y`, distinctness, and nonintegrality of `1/x_i`,
since the original finite generators have positive distance from the integers.
Thus rational approximation introduces neither repeated generators nor a
collision with any retained prime. Every source coefficient remains one.

The approximation controls more than values at zero. Choose fixed
`0<a<=x_i<=b<1` containing the approximating coordinates, and set
`L=-log a`, `lambda=-log b>0`. For `z>=0`,
\[
 \partial_z^j x^{1+z}=x^{1+z}(\log x)^j,
\]
\[
 \left|\partial_x\partial_z^j x^{1+z}\right|
 \le e^{-\lambda z}\bigl((1+z)L^j+jL^{j-1}\bigr)
 \le C_j,
 \tag{13}
\]
where the second summand is omitted for `j=0`, and one may take
`C_0=1+1/(e lambda)` and
`C_j=L^j(1+1/(e lambda))+jL^(j-1)` for `j>=1`.
The mean value theorem now gives
\[
 \sup_{z\ge0}\left|\partial_z^j
    \left(\sum_i \widetilde x_i^{1+z}-\sum_i x_i^{1+z}\right)\right|
 \le C_j\sum_i|\widetilde x_i-x_i|\longrightarrow0
 \quad(0\le j\le m).
 \tag{14}
\]
The value at zero of the difference is exactly zero by (12). The constants
depend on the fixed source and order; no uniform bound on denominators,
source size, or growing derivative order is asserted.

## Preserving the crossover while rationalizing the source

Apply AF-592 with the prescribed `m,N,Y,tau_*` and a low threshold smaller
than `eta`, to obtain a finite real edit `Q_*` for which the difference
`Q_*(1+z)-P(1+z)` vanishes to order `m+1` at zero. Its replacement
reciprocal mass is rational because it equals a finite sum of `1/p`.
Its proof supplies finitely many positive coordinates
\[
 0<u_N<v_N<u_{N-1}<\cdots<u_1<v_1<u_0<2\tau_*
\]
with `F_(Q_*)(u_i/2)>3/4` and `F_(Q_*)(v_i/2)<eta`.

Rationalize the replacement reciprocals using (12)--(14), leaving the
removed prime set unchanged. Equation (14) at zero gives (3). At the
finitely many selected positive coordinates, `Q_*(1+z)>0`, and its values
remain in compact positive neighborhoods after sufficiently small
approximation. For `a=E_1^(-1)(w)`,
\[
 \frac{d\log a}{dw}=-e^a.
 \tag{15}
\]
This derivative is bounded on those neighborhoods. Therefore the source
approximation preserves every strict high and low inequality. This is a
finite-coordinate transport estimate, not a uniform inverse estimate on
the entire ray.

Each interval `[u_i/2,u_(i-1)/2]` consequently has an interior minimum
below `eta`. The positive source is strictly decreasing and analytic for
real `s>1`, so its inverse crossover is real analytic and nonconstant.
Interior minimizers are isolated and strict. The intervals have disjoint
interiors, proving the required count and separation.

Exact reciprocal mass and the unchanged smallest generator `2` preserve
the two endpoint limits as in AF-591/592. Finally
\[
 Z_Q(s)=\zeta(s)\frac{\prod_{p\in S}(1-p^{-s})}
                         {\prod_{g\in G}(1-g^{-s})}
 \tag{16}
\]
has a finite quotient analytic and nonzero on `Re s>0`. This proves the
zero-divisor assertion and prevents interpreting the turning changes as
an RH distinction.

## Controls, prior art, and the remaining exact question

Both equalities in (2) matter. For `S={3}`, the integer replacements
`G={9,27}` match the logarithmic moment because
`log 9/9+log 27/27=log 3/3`, but their reciprocal mass is `4/27`, not
`1/3`. Conversely `S={5,7}` and the nonintegral rational set
`G={35/8,35/4}` have identical mass `12/35`; the coefficient of `log 2`
in the replacement logarithmic moment is `-32/35`, so first derivatives
do not match. These are exact valuation checks, not floating-point tests.

The prime-log argument is elementary unique factorization. The normalized
entropy interpretation and integer self-power reduction are classical:
Tom Leinster, [*Entropy modulo a prime*](https://arxiv.org/abs/1903.06961),
*Communications in Number Theory and Physics* **15** (2021), 279--314,
§7, especially the proof of Theorem 7.2, equations (101)--(105), uses the
same common-denominator conversion from equal rational entropies to equal
products of integer self-powers. That theorem concerns equality of entropy
residues, not uniqueness of a rational distribution.

Bayer--Teichmann, [*The proof of Tchakaloff's theorem*](https://arxiv.org/abs/math/0502473),
and Peled, [*Simple Universal Bounds for Chebyshev-Type Quadratures*](https://arxiv.org/abs/0903.4625),
are the neighboring positive and equal-weight moment literature already
compared in AF-592. They do not furnish rational points on this exact
linked-weight logarithmic level set. Here rational density is used only
inside the **linear mass** constraint; (13)--(14) establish approximation
of the other observations explicitly. No new general cubature, entropy,
or density theorem is claimed.

The mathematical delta is the contrast between exact integer rigidity and
the absence of a positive rational finite-jet tolerance controlling the
already constructed crossover shape. AF-591 did not match nonconstant
jets, and AF-592's exact repair allowed real generators. Neither alone
stated this rational finite-precision boundary. The proof does not upgrade
approximate rational matching to exact matching, or independent real-node
parameters to rational solutions of (9).

The exact rational feasibility problem remains open here, including whether
a certificate can be placed above every cutoff. No finite search, Lean
verification, or independent adversarial approval is claimed. The decisive
proof checks are the nonnegative summands in (7), signed denominator terms
in (8), both directions of (9), exact preservation of (12), uniformity in
`z>=0` of (13), and finite-coordinate inverse transport. Integer rigidity
is a short unique-factorization consequence; the rational approximation
uses elementary density and AF-592. No RH mechanism follows.
