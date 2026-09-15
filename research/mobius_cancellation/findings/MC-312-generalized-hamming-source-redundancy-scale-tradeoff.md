# MC-312 — Generalized Hamming weights force a source-redundancy / source-scale tradeoff

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact one-defect Legendre-shell endpoint and source-cut dictionary of `MC-307`–`MC-308`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R
\]

be the selected endpoint span, and choose **any fixed lower-prime product representatives**

\[
V_i\subseteq\{p\le y:p\text{ odd prime}\}
\qquad(1\le i\le R)
\]

for the independent shell functionals `lambda_i`. Put

\[
U:=\bigcup_{i=1}^R V_i,
\qquad n:=|U|,
\qquad Z:=\max U,
\]

and form the binary incidence matrix

\[
A=(A_{i,p})_{1\le i\le R,\ p\in U},
\qquad A_{i,p}:=\mathbf1_{p\in V_i}.
\tag{1}
\]

Then `A` has row rank `R`, so its row space

\[
C_A:=\{aA:a\in\mathbf F_2^R\}\subseteq\mathbf F_2^U
\tag{2}
\]

is a binary `[n,R]` linear code. For `1\le t\le R`, let `d_t(C_A)` be its `t`-th generalized Hamming weight: the smallest support size of a `t`-dimensional subcode.

For every `t` for which

\[
1-(2+o(1))\frac{R+1}{2^t}>0,
\tag{3}
\]

the endpoint localization forces

\[
\boxed{
(n-R+t)\log Z
\ge
\left(1-(2+o(1))\frac{R+1}{2^t}\right)\log y-O(1).
}
\tag{4}
\]

Equivalently,

\[
\boxed{
Z
\ge
y^{\{1-(2+o(1))(R+1)/2^t\}/(n-R+t)}e^{-O(1)/(n-R+t)}.
}
\tag{5}
\]

and, under a prescribed source-prime cap `Z`,

\[
\boxed{
n
\ge
R-t+
\left(1-(2+o(1))\frac{R+1}{2^t}\right)
\frac{\log y}{\log Z}
-O\!\left(\frac1{\log Z}\right).
}
\tag{6}
\]

Thus the source package cannot simultaneously have **low redundancy** and **uniformly small source primes**. This is a genuinely nonshareable source resource: it counts distinct lower-prime coordinates in a common representation package, rather than recounting the exponentially many Page-expensive endpoint directions from `MC-311`.

A convenient asymptotic choice is

\[
t_R:=\left\lceil2\log_2(R+1)\right\rceil,
\tag{7}
\]

which satisfies `t_R=o(R)` and `t_R\le R` for large `R`. Then

\[
\frac{R+1}{2^{t_R}}\le\frac1{R+1},
\]

so `(4)` becomes

\[
\boxed{
(n-R+O(\log R))\log Z
\ge(1-o(1))\log y.
}
\tag{8}
\]

Two useful specializations follow.

### Natural near-shell coordinate scale

If every source prime in the common package obeys

\[
Z\le y^{(1+o(1))/R},
\tag{9}
\]

then `(8)` forces

\[
\boxed{n\ge2R-o(R).}
\tag{10}
\]

So a package of only `R+o(R)` lower-prime coordinates at the natural `y^(1/R)` scale cannot encode an actual one-defect endpoint. It needs essentially another full rank of source-coordinate redundancy.

### Page-scale source package

If every source prime lies below the Page threshold of `MC-293`,

\[
Z\le D_y
=
\exp\!\left(\kappa\frac{\log y}{\log\log y}\right),
\tag{11}
\]

then

\[
\boxed{
n
\ge
R+(1-o(1))\frac{\log\log y}{\kappa}.
}
\tag{12}
\]

In the critical reciprocal regime `2^R\asymp\log y`, where

\[
R=\frac{\log\log y}{\log2}+O(1),
\]

this reads

\[
\boxed{
n
\ge
\left(1+\frac{\log2}{\kappa}-o(1)\right)R.
}
\tag{13}
\]

The constant `kappa` is the sufficiently small absolute Page constant fixed in `MC-293`; no optimization of it is claimed.

Conversely, if the common package has only `n=R+o(R)` distinct source primes, `(8)` forces at least one source prime to be much larger than the naive equal-share scale:

\[
\boxed{
Z\ge
 y^{(1-o(1))/(n-R+O(\log R))}.
}
\tag{14}
\]

For the extreme `n=R` case this is

\[
Z\ge y^{\Omega(1/\log R)},
\tag{15}
\]

whereas the disjoint-singleton profile of `MC-306` used source primes only around `y^(1/R)`. Thus the source-cut obstruction can be rephrased as a sharp structural dichotomy: **either add many distinct source coordinates, or pay with a much larger individual source scale.**

No estimate for `M(x)` follows.

## 1. The fixed representatives form a full-rank representation code

For each source prime `p\in U`, the `p`-th column of `A` records in which chosen representatives it occurs. If `a\in\mathbf F_2^R`, the symmetric difference of the representatives indexed by `a` is exactly the support of the codeword

\[
aA\in C_A.
\tag{16}
\]

Suppose `aA=0`. Then the symmetric difference is empty, so multiplying the representative identities gives the trivial shell character. Hence

\[
\sum_{i=1}^R a_i\lambda_i=0.
\]

The `lambda_i` are independent, therefore `a=0`. Thus the map `a\mapsto aA` is injective and

\[
\dim C_A=R.
\tag{17}
\]

This point matters: the code is not an auxiliary arbitrary encoding. Its coordinates are actual lower-prime sources used by the chosen representatives, and a codeword is exactly the source support obtained by multiplying the corresponding endpoint representatives.

## 2. A generalized Hamming support is exactly a high-rank source cut

Fix `1\le t\le R`. By definition of the generalized Hamming weight there is a `t`-dimensional subcode

\[
D\le C_A
\]

with support `J\subseteq U` satisfying

\[
|J|=d_t(C_A).
\tag{18}
\]

Every codeword in `D` vanishes on `U\setminus J`. Under the injective coefficient map `(16)`, the corresponding `t`-dimensional coefficient subspace therefore lies in

\[
\{a\in\mathbf F_2^R:aA_{U\setminus J}=0\}.
\]

But `MC-308` identifies the dimension of this kernel with the source-cut rank loss

\[
t_J
=R-\operatorname{rank}A_{U\setminus J}.
\tag{19}
\]

Consequently

\[
\boxed{t_J\ge t.}
\tag{20}
\]

The quotient-simplex size of the same cut is

\[
h_J
=|\{0,q_J(e_1),\ldots,q_J(e_R)\}|,
\]

so trivially

\[
\boxed{h_J\le R+1.}
\tag{21}
\]

Insert `(20)` and `(21)` into the exact source-cut Brun--Titchmarsh bound of `MC-308`:

\[
P_J
:=\prod_{p\in J}p
\ge
 y^{1-(2+o(1))h_J/2^{t_J}}e^{-O(1)}.
\]

This gives

\[
\boxed{
P_J
\ge
 y^{1-(2+o(1))(R+1)/2^t}e^{-O(1)}.
}
\tag{22}
\]

The argument has now converted a **support hierarchy of the representation code** into a polynomial lower bound for the product of the corresponding actual source primes.

## 3. Generalized Singleton turns the source-cut product into redundancy

The classical generalized Singleton bound for an `[n,R]` linear code is

\[
\boxed{d_t(C_A)\le n-R+t.}
\tag{23}
\]

Applying `(23)` to the subcode chosen in `(18)` yields a source cut `J` with

\[
|J|\le n-R+t.
\tag{24}
\]

Since every prime in `J` is at most `Z`,

\[
P_J\le Z^{|J|}\le Z^{n-R+t}.
\tag{25}
\]

Combining `(22)` and `(25)` proves `(4)`–`(6)`.

The mechanism is worth separating from a mere cardinality argument. `MC-311` says there are exponentially many endpoint directions above the Page source threshold, but those directions could in principle reuse source coordinates. Here the generalized Hamming hierarchy asks a different question: **how small can the union support of an entire `t`-dimensional family of representation codewords be?** Generalized Singleton guarantees that some such family is supported on only `n-R+t` coordinates. The endpoint source-cut theorem then says that this compressed support must nevertheless carry almost a shell-sized prime product once `t` exceeds about `log_2 R`. A short support can survive only if its coordinates themselves become large.

This is exactly the redundancy/scale tradeoff in `(8)`.

## 4. Why `t≈2 log_2 R` reaches the near-full shell exponent

The source-cut exponent in `(22)` is

\[
1-(2+o(1))\frac{R+1}{2^t}.
\tag{26}
\]

The quotient-simplex bound `h_J\le R+1` is deliberately crude but universal. Choosing `t` barely above `log_2 R` makes the ratio sub-half; choosing `(7)` makes it `O(1/R)`. Hence a subcode of dimension only `O(log R)` already has to use a source support of product

\[
y^{1-o(1)}.
\tag{27}
\]

Generalized Singleton simultaneously says that some such subcode lives on at most

\[
n-R+O(\log R)
\tag{28}
\]

source coordinates. Therefore those few coordinates must either be numerous through redundancy `n-R`, or include primes much larger than the equal-share scale.

This explains why the `R`-singleton matched profile of `MC-306` cannot be repaired merely by making its incidence matrix denser while keeping `R` source primes around `y^(1/R)`. For any full-rank `[R,R]` representation code, `(23)` gives `d_t=t`; taking `t≈2 log_2 R` exposes a `t`-dimensional source cut using only `O(log R)` of those primes, while `(22)` requires that cut alone to have product `y^(1-o(1))`. Primes of size `y^(1/R)` fall short by an exponent `O((log R)/R)`.

The obstruction is therefore not tied to the diagonal incidence matrix used in the first singleton control. It survives **every** invertible re-encoding on only `R` equal-scale source coordinates.

## 5. Prior art and novelty boundary

The coding-theory ingredient is classical. Victor K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory **37** (1991), 1412–1418, DOI `10.1109/18.133259`, introduced the generalized Hamming-weight hierarchy. The standard generalized Singleton bound

\[
d_t\le n-R+t
\]

is part of the classical theory; modern treatments state it in exactly this form. `MC-310` had already identified Wei's generalized weights as relevant language for cheap-subspace support, but did not combine the generalized Singleton upper bound with the source-cut occupancy theorem.

The arithmetic ingredient is entirely `MC-308`: finite source-cut quotienting plus the already-audited arbitrary-interval Brun--Titchmarsh estimate of Tomohiro Yamada, *Explicit improvements of the Brun-Titchmarsh theorem for arbitrary intervals*, arXiv:2312.16090. No new prime-distribution theorem is asserted.

A targeted literature check on 15 September 2026 for generalized Hamming weights, generalized Singleton bounds, prescribed Legendre patterns, and source-support/product constraints found the classical coding hierarchy and prescribed-Legendre literature, but no source asserting this specific shell-localized source-coordinate tradeoff. **No standalone novelty claim is made.** The durable line-specific result is the exact dictionary `(18)`–`(22)` and its consequence `(4)`: a generalized Hamming support of the source representation code is a source cut to which endpoint localization assigns an arithmetic prime-product cost.

## Boundaries and falsification tests

- **The theorem concerns one common package of fixed representatives.** Different choices of representatives can change `U`, `n`, `Z`, and the code `C_A`. The inequalities hold for every fixed choice, but no uniqueness or optimality of the package is assumed.
- **`n` counts distinct source primes, not representations.** Reusing the same lower prime in arbitrarily many endpoint representatives does not increase `n`; that reuse is exactly what `(4)` stress-tests.
- **The largest-source cap is load-bearing for the coordinate-count corollary.** Equation `(4)` is unconditional for the fixed package. Equation `(6)` converts product to cardinality using `p\le Z`; without controlling `Z`, a few very large source primes remain an escape.
- **Generalized Singleton is intentionally generic.** Arithmetic structure may force `d_t` smaller than the generic upper bound, which would only strengthen the source-product pressure. No coding optimality is assumed.
- **The support subcode need not be generated by a subset of the original endpoint basis.** This is why the result goes beyond `MC-307`: generalized Hamming weights optimize over all `t`-dimensional combinations of the endpoint representatives, while `MC-307` considered coordinate projections of selected basis directions.
- **No Page theorem is needed for `(4)`.** The Page scale enters only in specialization `(11)`–`(13)`. The core redundancy/scale tradeoff comes from exact endpoint support plus Brun--Titchmarsh and coding support geometry.
- **The exact one-defect endpoint is load-bearing.** Replacing the endpoint support changes `h_J` and therefore the source-cut exponent inherited from `MC-308`.
- **The result does not exclude high redundancy or large source primes.** Those are the two explicit surviving escapes. The next theorem must charge one of them to another arithmetic resource rather than treating either as impossible by definition.
- **No Mertens or RH estimate follows.** This is a coercive source-incidence theorem inside the localized endpoint program.

## Consequence for the research line

`MC-311` established that the reciprocal endpoint contains exponentially many Page-expensive directions, but explicitly left open whether those directions could share one small source package. The present finding identifies a first source resource that **cannot** be shared away for free.

For any common representation package, generalized Hamming theory produces an `O(log R)`-dimensional family whose combined source support uses only `n-R+O(log R)` distinct coordinates. Endpoint localization forces that compressed support to have product `y^(1-o(1))`. Therefore a surviving endpoint representation must pay in at least one of two ways:

- substantial **source-coordinate redundancy** `n-R`; or
- a much larger **largest source prime** `Z`.

At the natural equal-share scale `Z≈y^(1/R)`, the first payment is quantitative: `n\ge2R-o(R)`. Thus exponential direction density by itself is still not an additive conductor sum, but the representation geometry is no longer free to reuse only `R` small source coordinates. The next useful question is whether the actual lower-prime Legendre system can sustain the required redundancy while preserving the minimum-source-cost and endpoint-localization constraints, or whether that redundancy creates a new sieve/dispersion obstruction.