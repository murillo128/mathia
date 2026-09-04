# MC-063 — Distinct subquadratic quadratic Möbius certificates require power-separated scales

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Use the weighted quadratic Möbius-prime defect from `MC-060`–`MC-062`,

\[
A_X(\chi_q)
:=
\sum_{p\le X}\frac{|1+\chi_q(p)|}{p-1},
\qquad
\chi_q(n)=\left(\frac{n}{q}\right),
\]

for an odd prime conductor `q>X`. Fix

\[
0\le c<\frac12,
\qquad
1<\kappa<2,
\]

and call `(X,q)` a good quadratic certificate when

\[
X<q\le X^\kappa,
\qquad
A_X(\chi_q)\le c.
\tag{1}
\]

Then `MC-062` can be sharpened from bounded-ratio rigidity to a quantitative **power-gap law**.

For every fixed `epsilon>0`, if two good certificates `(X,q_X)` and `(Y,q_Y)` satisfy

\[
X\le Y,
\qquad
q_X\ne q_Y,
\]

then

\[
\boxed{
Y\gg_{c,\kappa,\varepsilon}
X^{\,4/\kappa-1-\varepsilon}.
}
\tag{2}
\]

In particular, because `kappa<2`, one may choose

\[
0<\varepsilon<\frac4\kappa-2,
\]

so the exponent in `(2)` is strictly larger than one. Distinct subquadratic quadratic certificates therefore cannot merely avoid bounded multiplicative gaps: **their observation scales must be separated by a fixed superlinear power**.

Consequently, for every fixed admissible `epsilon` as above, any increasing sequence of good certificates

\[
(X_1,q_1),(X_2,q_2),\ldots
\]

with pairwise distinct conductors has only

\[
\boxed{O_{c,\kappa,\varepsilon}(\log\log T)}
\tag{3}
\]

members with `X_j<=T`, after absorbing the finite initial range into the implied constant.

Thus under one fixed defect budget `c<1/2` and one fixed subquadratic conductor exponent `kappa<2`, genuinely new quadratic certificate identities can occur only on a doubly-logarithmically sparse scale skeleton. This is stronger than the non-syndetic conclusion of `MC-062`.

No estimate for `M(X)` follows. The result quantifies the complexity of one moving-comparator escape and does not turn the comparator into a cancellation theorem.

## 1. A later good certificate is already close enough at the earlier prime scale

The defect is monotone in the observation scale because all terms are nonnegative. Hence if `X<=Y`,

\[
A_X(\chi_{q_Y})
\le
A_Y(\chi_{q_Y})
\le c.
\tag{4}
\]

The earlier certificate also satisfies

\[
A_X(\chi_{q_X})\le c.
\tag{5}
\]

Set

\[
\eta:=1-2c>0.
\tag{6}
\]

Then at the common smaller scale `X`,

\[
A_X(\chi_{q_X})+A_X(\chi_{q_Y})
\le 1-\eta.
\tag{7}
\]

Both conductor primes exceed `X`: this is immediate for `q_X`, while `q_Y>Y>=X`. Thus if `q_X!=q_Y`, all hypotheses of the pairwise weighted Burgess obstruction `MC-060` hold at scale `X`.

## 2. Pairwise Burgess repulsion becomes a scale-gap exponent

`MC-060` gives, for every fixed `delta>0`,

\[
q_Xq_Y
\gg_{c,\delta}
X^{4-\delta}.
\tag{8}
\]

The two good-certificate complexity ceilings are imposed at their own observation scales:

\[
q_X\le X^\kappa,
\qquad
q_Y\le Y^\kappa.
\tag{9}
\]

Combining `(8)` and `(9)`,

\[
X^\kappa Y^\kappa
\gg_{c,\delta}
X^{4-\delta},
\]

and therefore

\[
Y
\gg_{c,\kappa,\delta}
X^{(4-\delta-\kappa)/\kappa}.
\tag{10}
\]

Given `epsilon>0`, choose

\[
\delta=\kappa\varepsilon.
\tag{11}
\]

Equation `(10)` is exactly

\[
Y
\gg_{c,\kappa,\varepsilon}
X^{4/\kappa-1-\varepsilon},
\]

which proves `(2)`.

The limiting exponent

\[
a_*(\kappa):=\frac4\kappa-1
\tag{12}
\]

is greater than one precisely for `kappa<2`. As `kappa` approaches the quadratic conductor threshold, `a_*(kappa)` approaches one and the superlinear scale separation disappears. This is the same structural threshold already visible in `MC-060` and `MC-062`, now expressed directly as a turnover cost in observation scale.

## 3. Pairwise-distinct certificate identities are only doubly-logarithmically frequent

Fix `epsilon` so that

\[
a:=\frac4\kappa-1-\varepsilon>1.
\tag{13}
\]

For a sequence of good certificates with strictly increasing scales and pairwise distinct conductors, `(2)` gives for all sufficiently large consecutive terms

\[
X_{j+1}\ge C X_j^a
\tag{14}
\]

with a fixed constant `C=C(c,kappa,epsilon)>0`.

Choose any fixed exponent `b` with

\[
1<b<a.
\tag{15}
\]

Once `X_j` exceeds a constant depending on `C,a,b`, equation `(14)` implies

\[
X_{j+1}\ge X_j^b.
\tag{16}
\]

Taking logarithms and iterating,

\[
\log X_{j+r}\ge b^r\log X_j.
\tag{17}
\]

Therefore the number of further pairwise-distinct certificate identities that can appear before scale `T` is at most a constant multiple of `log log T`, proving `(3)`.

This counting statement is about **distinct conductor identities**, not the number of good real or integer scale points. One fixed conductor may remain a good certificate over a nontrivial interval of scales; the theorem constrains how often the mechanism can replace that conductor by a genuinely different subquadratic quadratic certificate.

## 4. What this adds beyond MC-062

`MC-062` used the same monotonicity plus `MC-060` to prove that two distinct good certificates cannot occur at scales with a fixed bounded ratio. That establishes non-syndeticity but leaves the quantitative size of the required gap unspecified.

The present calculation retains the conductor ceilings instead of replacing `Y` by `BX`. The Burgess product floor then forces the explicit exponent `(12)`. Thus a fresh certificate cannot appear merely after a slowly growing multiplicative gap such as `log X`, `log^A X`, or `exp(sqrt(log X))`. Under fixed `kappa<2`, changing identity requires a polynomial jump in the observation scale.

For example, ignoring an arbitrarily small exponent loss:

- `kappa=3/2` gives the turnover exponent `5/3`;
- `kappa=4/3` gives exponent `2`;
- `kappa` tending to `2` makes the exponent tend to `1`, exactly where the argument ceases to give superlinear separation.

These examples are only illustrations of `(2)`; no sharpness is claimed.

The active moving-comparator frontier is consequently narrower. A quadratic strategy with a fixed weighted agreement gap and uniformly subquadratic conductors cannot continually refresh its local certificate. It must either reuse one identity for long ranges, accept power-separated turnover scales, let the conductor approach the quadratic threshold, weaken the agreement budget with scale, or leave the prime-conductor quadratic class.

## 5. Prior art and novelty boundary

The analytic input is not new. `MC-S34` records the classical Burgess character-sum estimate for cubefree conductors, and `MC-060` already converted it into the near-quartic product-conductor floor for two weighted approximate quadratic Möbius certificates. `MC-S5` anchors the standard pretentious-distance language and triangle inequality behind the broader principle that two multiplicative objects close to a common target must be close to one another.

A targeted audit of large-character-sum and pretentious-repulsion literature confirms that repulsion of distinct character approximants is an established mechanism. The result here does not claim a new character-sum or pretentiousness theorem. Its durable content is the exact scale-selection corollary obtained by combining the already-audited `MC-060` product floor with the two separate complexity ceilings `q_X<=X^kappa` and `q_Y<=Y^kappa`.

Accordingly `(2)` and `(3)` are recorded as an exact strengthening of the Mathia moving-comparator obstruction, with **no standalone novelty claim**.

## 6. Boundaries and falsification tests

The conclusion is deliberately narrow.

- The fixed defect budget must satisfy `c<1/2`. If `c` approaches `1/2` with scale, the uniform positive gap `eta=1-2c` disappears and the constants in `MC-060` must be re-audited.
- The conductor ceiling uses one fixed exponent `kappa<2`. At `kappa=2`, the limiting turnover exponent is one and the present superlinear conclusion vanishes.
- The conductors are distinct odd primes and the comparators are their primitive quadratic characters. Composite-conductor real characters or other comparator families need their own primitivity and character-sum audit.
- The theorem does not say that good certificates exist, nor that an existing certificate has a short lifetime. It only constrains the scales at which **distinct** identities can both satisfy the fixed good-certificate conditions.
- The `O(log log T)` count applies to a sequence with pairwise distinct conductors. Repeated observations supported by the same conductor are not counted as new identities.
- The result does not bound `M(X)`, does not prove useful cancellation for the comparator, and does not evade the twisted-Möbius uniformity obstruction of `MC-061`.

The claim is falsified if defect monotonicity `(4)` fails, if the later conductor cannot enter `MC-060` at the earlier scale, if the product-conductor lower bound `(8)` is inapplicable to the two distinct prime conductors, or if the exponent algebra from `(8)` and `(9)` to `(10)` is incorrect. Each step is explicit.

## Consequence for the active frontier

The moving quadratic comparator can no longer be viewed as a certificate that may be cheaply reselected whenever the current fit becomes inconvenient. Below the quadratic conductor threshold, `MC-060` charges pairwise character repulsion, `MC-061` charges polynomial twisted-Möbius uniformity loss, `MC-062` forbids bounded-ratio turnover, and the present result shows that **distinct identities must in fact turn over on power-separated scales**.

A viable source-forced moving-family theorem therefore needs genuinely new coherence: a mechanism that can exploit long persistence of one certificate, survive conductor dependence near the quadratic threshold, or couple the sparse turnover events without reducing them to independent frozen-character bounds. Finite-prefix interpolation plus unconstrained reselection does not provide that coherence.