# MC-062 — Subquadratic approximate quadratic Möbius fits cannot cover a multiplicatively dense tail of scales

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

For an odd prime `q>X`, let

\[
\chi_q(n)=\left(\frac{n}{q}\right)
\]

be the primitive quadratic character modulo `q`, and use the weighted Möbius-prime defect from `MC-060` and `MC-061`,

\[
A_X(\chi_q)
:=
\sum_{p\le X}\frac{|1+\chi_q(p)|}{p-1}.
\tag{1}
\]

Fix constants

\[
0\le c<\frac12,
\qquad
1<\kappa<2.
\tag{2}
\]

Call `(X,q)` a **good quadratic certificate** when

\[
X<q\le X^\kappa,
\qquad
A_X(\chi_q)\le c.
\tag{3}
\]

Then the following multiscale rigidity holds.

### Bounded-ratio rigidity

For every fixed `B>1`, there exists `X_0=X_0(c,\kappa,B)` such that whenever

\[
X_0\le X\le Y\le BX
\tag{4}
\]

and `(X,q_X)` and `(Y,q_Y)` are good certificates, one necessarily has

\[
\boxed{q_X=q_Y.}
\tag{5}
\]

Thus two **distinct** subquadratic prime-conductor quadratic certificates cannot both approximate the Möbius prime law at nearby multiplicative scales once the scale is large.

### Scale-sparsity consequence

Consequently, there is no unbounded sequence of good scales

\[
X_1<X_2<\cdots\to\infty
\]

with bounded multiplicative gaps

\[
\sup_j \frac{X_{j+1}}{X_j}<\infty.
\tag{6}
\]

Equivalently, if good certificates exist at infinitely many scales under one fixed defect budget `c<1/2` and one fixed subquadratic conductor exponent `\kappa<2`, their scale set is **not multiplicatively syndetic**: along every unbounded enumeration of good scales, the ratios between successive scales must be unbounded.

In particular, for every fixed `B>1`, a full geometric tail

\[
X,\ BX,\ B^2X,\ldots
\]

cannot consist entirely of good scales.

This closes the most direct multiscale escape left by `MC-060` and `MC-061`: a strategy cannot evade the single-scale quadratic obstruction merely by choosing a fresh subquadratic approximate quadratic character at each constant-factor increase of the observation scale.

## 1. The later certificate is automatically good at the earlier prime scale

The defect `(1)` is a sum of nonnegative prime terms. Therefore, if `X\le Y` and `q_Y>Y`, then

\[
A_X(\chi_{q_Y})
\le
A_Y(\chi_{q_Y}).
\tag{7}
\]

Hence under `(3)` and `(4)`, both characters satisfy at the **same smaller scale** `X`

\[
A_X(\chi_{q_X})\le c,
\qquad
A_X(\chi_{q_Y})\le c.
\tag{8}
\]

Put

\[
\eta:=1-2c>0.
\tag{9}
\]

Then

\[
A_X(\chi_{q_X})+A_X(\chi_{q_Y})
\le
1-\eta.
\tag{10}
\]

This monotonicity is the only new scale input. No assumption is made about how either character was selected and no comparison of Möbius sums is used.

## 2. MC-060 turns nearby distinct certificates into an exponent contradiction

Assume for contradiction that `q_X\ne q_Y`. The two conductors are distinct odd primes, both larger than `X`, and `(10)` is exactly the weighted pair hypothesis of `MC-060`. Therefore, for every fixed `\delta>0`,

\[
q_Xq_Y
\gg_{\eta,\delta}
X^{4-\delta}.
\tag{11}
\]

Choose the fixed admissible value

\[
\delta:=2-\kappa>0.
\tag{12}
\]

Then `(11)` becomes

\[
q_Xq_Y
\gg_{c,\kappa}
X^{2+\kappa}.
\tag{13}
\]

But the good-certificate conductor ceilings and `Y\le BX` give

\[
q_Xq_Y
\le
X^\kappa Y^\kappa
\le
B^\kappa X^{2\kappa}.
\tag{14}
\]

Since

\[
(2+\kappa)-2\kappa=2-\kappa>0,
\tag{15}
\]

`(13)` and `(14)` are incompatible for all sufficiently large `X`. Thus `q_X=q_Y`, proving `(5)`.

The exponent threshold is structural. The proof stops being contradictory at `\kappa=2`, exactly where the pairwise Burgess product floor `X^{4-o(1)}` can be paid by two conductor scales of order `X^2`.

## 3. Bounded-gap good scales would force one fixed conductor forever

Suppose an unbounded increasing sequence of good scales satisfies `(6)`. Choose a fixed `B` larger than the supremum in `(6)`. For all sufficiently large `j`, bounded-ratio rigidity gives

\[
q_{X_j}=q_{X_{j+1}}.
\tag{16}
\]

By induction, the entire tail uses one fixed prime conductor `q_*`.

However every good certificate also requires

\[
q_*>X_j.
\tag{17}
\]

As `X_j\to\infty`, `(17)` is impossible for a fixed finite prime. This proves the scale-sparsity consequence.

The same argument on `X_j=B^jX_*` shows directly that every fixed geometric ladder contains infinitely many bad rungs once the scale is large enough.

## 4. What this adds beyond the single-scale pair obstruction

`MC-060` is a same-scale statement: within one fixed weighted Möbius neighborhood, two distinct approximate quadratic certificates cannot both have subquadratic conductor. By itself that still leaves an apparent adaptive escape in which the unique low-conductor survivor changes identity as the observation scale changes.

The present result uses the monotonicity `(7)` to compare certificates selected at **different** scales. A certificate good at the later scale is automatically eligible for the earlier-scale pair test. The pairwise conductor repulsion then says that a change of identity cannot occur across any fixed multiplicative scale ratio while both conductors remain `X^{\kappa}` with fixed `\kappa<2`.

Therefore the surviving quadratic-comparator strategy is substantially narrower than after `MC-061`. It must give up at least one of the following:

- coverage on a multiplicatively dense tail of scales;
- a fixed weighted defect budget below `1/2`;
- a fixed conductor exponent strictly below `2`;
- prime-conductor quadratic characters as the comparator class.

Keeping all four simultaneously is impossible.

## 5. Prior art and novelty boundary

The analytic input is entirely the classical Burgess character-sum mechanism already anchored by `MC-S34` and specialized in `MC-060`. The fact that multiplicative characters close to a common target become close to one another is standard pretentious-number-theory geometry; `MC-S5` anchors that general language. Classical exceptional-character results such as Landau–Page exhibit a related "at most one exceptional real character" phenomenon, but their hypothesis is a near-`1` zero of a Dirichlet `L`-function rather than weighted agreement with the Möbius prime sign, so they are only an analogy and are not used in the proof.

A targeted literature search around pretentious character repulsion, large character sums, least quadratic nonresidues, and exceptional real characters found established surrounding mechanisms but no reason to promote this scale-selection corollary as a standalone new theorem. The durable Mathia content is the explicit multiscale consequence of the already-audited `MC-060` weighted pair bound. Accordingly no novelty claim is made.

## 6. Boundaries and falsification tests

The conclusion is deliberately specific.

- The fixed threshold `c<1/2` is essential to this proof because `MC-060` needs a positive gap `\eta=1-2c`. If `c` approaches `1/2` with scale, the implied constants and the available exponent comparison must be audited again.
- The conductor exponent must be fixed below `2`. The argument gives no contradiction at the quadratic conductor scale.
- The characters are the primitive quadratic characters of odd prime conductors, with `q>X` at the scale where they are used. Composite-conductor real characters require a separate conductor/primitivity audit.
- The theorem does **not** say that good certificates never exist. It permits isolated scales, long finite blocks supported by one conductor, and arbitrarily sparse scale sequences.
- It does not bound `M(X)`, prove RH, or supply useful cancellation from a surviving certificate. `MC-061` separately shows that a family-uniform twisted-Möbius power bound cannot provide that missing step under the same fixed agreement gap.
- The scale-sparsity statement concerns the existence of certificates under the fixed ceiling `(3)`, not a computational search procedure for them.

The result is falsified if defect monotonicity `(7)` fails, if the later certificate cannot be inserted into `MC-060` at the smaller scale despite `q_Y>Y\ge X`, or if the exponent comparison `(13)`–`(15)` is invalid. All three steps are exact.

## Consequence for the active frontier

The single-quadratic frontier can no longer be modeled as an independently reselectable low-conductor fit at every working scale. Under fixed nontrivial agreement and any fixed `\kappa<2`, nearby large scales are **identity-locked**, while an identity-locked tail is impossible because one finite conductor cannot remain larger than the observation scale forever.

A viable multiscale quadratic mechanism must therefore explain genuinely sparse exceptional scales, approach the quadratic conductor threshold, weaken the agreement budget with scale, or introduce a different coupled object. Merely allowing the quadratic certificate to move with `X` does not restore a scale-uniform bootstrap.