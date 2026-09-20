# MC-407 — Prime-error increment coupling Abel-collapses to a Möbius-weighted PNT error convolution

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-IDENTITIES` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-406` decomposed the Mangoldt quotient fibers as

\[
W_k(x)=\frac{x}{k(k+1)}+E(x/k)-E(x/(k+1)),
\qquad E(y):=\psi(y)-y,
\]

and left the signed prime-error increment term

\[
R(x):=\sum_{k=1}^{x}M(k)
\bigl(E(x/k)-E(x/(k+1))\bigr)
\tag{1}
\]

as one possible location for extra arithmetic leverage. There is a sharper exact reduction: the increment coupling in `(1)` is not an independent two-sequence statistic. Discrete Abel summation gives

\[
\boxed{
R(x)
=
\sum_{a\le x}\mu(a)E(x/a)
+
\frac{x}{x+1}M(x).
}
\tag{2}
\]

Consequently the complete quotient transform of `MC-405`/`MC-406` has the simpler exact form

\[
\boxed{
\sum_{b\le x}\Lambda(b)M(\lfloor x/b\rfloor)
=
 x\,m(x)+\sum_{a\le x}\mu(a)E(x/a),
}
\tag{3}
\]

where

\[
m(x):=\sum_{a\le x}\frac{\mu(a)}a.
\]

Equivalently, because the left side is `-sum_{n<=x} mu(n) log n`,

\[
\boxed{
\sum_{a\le x}\mu(a)E(x/a)
=
-\sum_{n\le x}\mu(n)\log n-xm(x).
}
\tag{4}
\]

Thus the apparent pairing between the cumulative Mertens values `M(k)` and adjacent prime-counting-error increments in `MC-406` is exactly a summation-by-parts presentation of the classical Möbius-weighted PNT error convolution in `(3)`. This does **not** make the error term useless: a new signed theorem for the convolution in `(3)` could still matter. It does remove one false degree of freedom. Merely changing from the `M(k) Delta E_k` coordinates to the `mu(a) E(x/a)` coordinates has not created a second independent arithmetic observable.

There is also a dual absolute-value barrier. If, hypothetically, one has a fixed power bound

\[
|E(y)|\le C y^\beta
\qquad(0<\beta<1),
\tag{5}
\]

then `(3)` by triangle inequality gives

\[
\left|\sum_{a\le x}\mu(a)E(x/a)\right|
\le
C x^\beta\sum_{a\le x}a^{-\beta}
=
O_\beta(Cx).
\tag{6}
\]

So even a pointwise power-saving estimate for the prime-counting error, including a square-root-scale one, becomes only linear after absolute summation over the Möbius quotient variable. A useful estimate for `(3)` must retain signed interaction between `mu(a)` and `E(x/a)` across scales; pointwise control of `E` alone cannot supply a fixed power improvement for the Mertens problem.

No bound for `M(x)` or `E(x)` is improved here.

## 1. Direct convolution form

Start from the finite identity used in `MC-405`:

\[
\mu(n)\log n
=-(\mu*\Lambda)(n).
\tag{7}
\]

Summing `(7)` over `n<=x` and writing `n=ab` gives

\[
-\sum_{n\le x}\mu(n)\log n
=
\sum_{ab\le x}\mu(a)\Lambda(b).
\tag{8}
\]

Sum first over `b`. With

\[
\psi(y)=\sum_{b\le y}\Lambda(b),
\]

one obtains exactly

\[
\sum_{ab\le x}\mu(a)\Lambda(b)
=
\sum_{a\le x}\mu(a)\psi(x/a).
\tag{9}
\]

Now insert `psi(y)=y+E(y)`:

\[
\sum_{a\le x}\mu(a)\psi(x/a)
=
 x\sum_{a\le x}\frac{\mu(a)}a
+
\sum_{a\le x}\mu(a)E(x/a),
\]

which proves `(3)` and `(4)`.

This derivation is finite. It does not use analytic continuation of `1/zeta`, a zero-free region, Perron inversion, or RH.

## 2. The MC-406 increment remainder is the same object

Let

\[
a_k:=E(x/k),
\qquad 1\le k\le x+1.
\]

Then `(1)` is

\[
R(x)=\sum_{k=1}^{x}M(k)(a_k-a_{k+1}).
\]

Discrete summation by parts yields

\[
R(x)
=M(1)a_1
+\sum_{k=2}^{x}\bigl(M(k)-M(k-1)\bigr)a_k
-M(x)a_{x+1}.
\tag{10}
\]

Since `M(k)-M(k-1)=mu(k)` and `M(1)=mu(1)=1`, the first two terms combine to

\[
\sum_{k=1}^{x}\mu(k)E(x/k).
\]

Moreover `0<x/(x+1)<1`, so `psi(x/(x+1))=0` and hence

\[
E(x/(x+1))=-\frac{x}{x+1}.
\]

Equation `(10)` therefore gives `(2)`.

Substituting `(2)` into the MC-406 decomposition

\[
 x\left(m(x)-\frac{M(x)}{x+1}\right)+R(x)
\]

cancels the boundary term `xM(x)/(x+1)` and recovers `(3)` exactly.

The important point is representation-level: the `M(k)`--increment picture and the `mu(a)`--error picture are related by an exact invertible discrete derivative/partial-summation step. Treating their coexistence as two independent sources of cancellation would double-count the same finite convolution.

## 3. Pointwise prime-error control has the same linear closure barrier

Assume `(5)`. Because `|mu(a)|<=1`,

\[
\sum_{a\le x}|\mu(a)E(x/a)|
\le
C x^\beta\sum_{a\le x}a^{-\beta}.
\]

For fixed `0<beta<1`, elementary integral comparison gives

\[
\sum_{a\le x}a^{-\beta}
=
\frac{x^{1-\beta}}{1-\beta}+O(1),
\tag{11}
\]

and `(6)` follows.

This is the source-dual analogue of the absolute-mass barrier in `MC-405`. There, a power bound for `M(x/b)` was destroyed by summing against positive `Lambda(b)`. Here, a power bound for the PNT error `E(x/a)` is destroyed by summing absolute values over the Möbius quotient variable. In either orientation, the signed convolution is the only place where a sublinear exponent can survive.

At a formal square-root scale, `|E(y)|<<y^{1/2+epsilon}` would still give only `O(x)` from `(6)` after choosing a fixed `epsilon<1/2`. Therefore a route through prime-error estimates must prove more than strong pointwise PNT error: it needs a joint theorem controlling the signs/phases of `mu(a)` against the dilation family `E(x/a)`, or a representation that retains additional arithmetic information before this convolution is scalarized.

## 4. Prior art and novelty boundary

The ingredients are classical. The divisor relation `sum_{d|n} Lambda(d)=log n`, Möbius inversion, and the convolution identity `(7)` are standard arithmetic-function algebra. The summatory identity

\[
-\sum_{n\le x}\mu(n)\log n
=
\sum_{a\le x}\mu(a)\psi(x/a)
\]

also appears explicitly in elementary treatments of the prime number theorem and Möbius cancellation. A targeted literature search on 20 September 2026 found the identity in standard Möbius-inversion/PNT material and found no basis for treating `(2)`--`(4)` as a new theorem family. No novelty is claimed for the convolution, Abel summation, or the power-sum estimate `(11)`.

The durable contribution is only the Mathia frontier diagnosis relative to `MC-406`: its apparently live `M(k)` versus `E(x/k)-E(x/(k+1))` coupling is algebraically the same finite statistic as the Möbius-weighted PNT error convolution. Therefore a future claim of new leverage must identify a **genuinely additional signed relation** for that convolution, not merely move between increment and quotient coordinates.

Relevant classical references include the von Mangoldt/Möbius identities recorded in standard analytic-number-theory texts such as Apostol and Hardy--Wright; the same summatory convolution is also used in elementary proofs of equivalences around the prime number theorem. The modern literature on Möbius/PNT error bounds can supply estimates for the factors, but those factorwise estimates do not remove the absolute-value barrier `(6)`.

## Boundaries and falsification tests

- **Not a no-go for signed prime-error methods.** A theorem proving cancellation in `sum mu(a)E(x/a)` from arithmetic structure independent of the target Mertens estimate lies outside this obstruction.
- **No claim that `E` is independent or random.** The entire point is that factorwise magnitude control is insufficient; a successful route must exploit dependence.
- **Fixed power exponent in `(5)`.** The pricing statement `(6)` is for fixed `beta<1`; it is not a uniform estimate as `beta` approaches `1` with `x`.
- **No circular zero input.** Equations `(2)`--`(4)` are finite identities. Any later use of a strong bound for `E` must audit what zero-free information that bound already contains.
- **Coordinate change is not a second observable.** Discrete Abel summation exactly identifies `(1)` and `(2)`. A candidate that treats both as separate evidence has duplicated the same convolution.
- **Additional within-fiber structure remains live.** Congruence, phase, translation, off-diagonal, or other source data that do not factor through the scalar convolution `(3)` are not ruled out here.

## Consequence for the research line

`MC-406` left two broad exits after floor-quotient compression: exploit the prime-error increments jointly with `M(k)`, or retain additional information inside the quotient fibers. This finding narrows the first exit.

The increment coupling itself is not an independent bridge: after exact Abel summation it is `sum mu(a)E(x/a)` plus a boundary term, and after restoring the deterministic PNT main kernel the boundary cancels. Pointwise bounds on the prime error then suffer the same linear absolute-mass barrier already seen on the Mertens side.

Accordingly, a useful continuation of the first branch must provide a nontrivial **signed Möbius--PNT-error correlation theorem** whose hypotheses do not already contain the desired Mertens cancellation. Otherwise the remaining representation work should move to the second branch and specify what genuinely additional within-fiber discriminator survives beyond the scalar quotient total.