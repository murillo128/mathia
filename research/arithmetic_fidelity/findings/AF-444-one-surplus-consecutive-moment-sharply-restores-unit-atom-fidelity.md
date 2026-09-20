# AF-444 — One surplus consecutive moment sharply restores unit-atom fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `SHARP-MOMENT-THRESHOLD`, `TARGET-PURE-FIBER`, `CONDITIONING-DECAY`, `CLASSICAL-NEWTON-GIRARD`, `NO-NOVELTY-CLAIM`

## Claim

AF-443 proves that `K` independently movable earlier support coordinates can exactly absorb a sufficiently remote binary target-mark flip from any fixed family of `K` distinct reciprocal-power moments. For the unit-occupancy source class, adding **one consecutive moment** crosses a sharp exact-fidelity boundary.

Fix `K>=1`. For `x=(x_1,...,x_K) in (0,infinity)^K`, define

\[
p_n(x)=\sum_{i=1}^K x_i^n,
\qquad
P_{K+1}(x)=(p_1(x),...,p_{K+1}(x)).
\]

For a positive target coordinate `y`, put

\[
v(y)=(y,y^2,...,y^{K+1}).
\]

Then there do not exist positive `K`-tuples `x,x'` satisfying

\[
\boxed{
P_{K+1}(x)=P_{K+1}(x')+v(y).
}
\tag{1}
\]

Equivalently, the first `K+1` consecutive positive power moments distinguish every `K`-atom positive unit-weight multiset from every `(K+1)`-atom positive unit-weight multiset. No distinctness, ordering, small-jitter, or locality hypothesis is needed.

Moreover, if the `K` nuisance coordinates range in fixed compact intervals

\[
B_i=[a_i,b_i]\Subset(0,\infty),
\qquad
B=\prod_{i=1}^K B_i,
\]

and

\[
\mathcal C_0=P_{K+1}(B),
\qquad
\mathcal C_1(y)=P_{K+1}(B)+v(y),
\]

then for every fixed `y_0>0` there are constants `0<c<=C<infinity`, depending only on `K,B,y_0`, such that

\[
\boxed{
c y
\le
\operatorname{dist}(\mathcal C_0,\mathcal C_1(y))
\le
C y
\qquad(0<y\le y_0).
}
\tag{2}
\]

Thus the extra moment repairs **exact identifiability** but not uniform robustness as the added atom approaches the lost boundary `y=0`. In the reciprocal-square shell model, `y=m^{-2}`, so the best class-level separation is of order `m^{-2}` for fixed earlier cells.

Combined with AF-443, this gives a sharp observation-count result for this precise nuisance model:

\[
\boxed{
K\text{ consecutive moments can fail against }K\text{ latent supports,}
\qquad
K+1\text{ consecutive moments forbid the collision.}
}
\tag{3}
\]

The conclusion is deliberately restricted to positive **unit-weight** atoms and a single binary occupancy change. It is not a theorem that raw observation rank alone guarantees fidelity in arbitrary weighted or multi-change moment models.

## Newton-Girard separation of `K` and `K+1` atoms

Assume `(1)` for contradiction. Let

\[
X=\{x_1,...,x_K,0\}
\]

be the `K` positive nuisance atoms padded by one zero, and let

\[
Y=\{x'_1,...,x'_K,y\}.
\]

Equation `(1)` says that their power sums agree through order `K+1`:

\[
\sum_{z\in X}z^n
=
\sum_{z\in Y}z^n,
\qquad n=1,...,K+1.
\tag{4}
\]

For a multiset of `K+1` numbers, Newton-Girard identities recursively recover the elementary symmetric polynomials `e_r` from the first `r` power sums:

\[
r e_r
=
\sum_{n=1}^r(-1)^{n-1}e_{r-n}p_n,
\qquad e_0=1.
\tag{5}
\]

Therefore `(4)` forces

\[
e_r(X)=e_r(Y)
\qquad(r=1,...,K+1).
\tag{6}
\]

At the top degree, however,

\[
e_{K+1}(X)=0
\]

because `X` contains the padded zero, while

\[
e_{K+1}(Y)
=y\prod_{i=1}^K x'_i
>0.
\tag{7}
\]

This contradicts `(6)` and proves `(1)`.

The same proof handles a binary flip in the opposite direction by interchanging the two configurations. It also permits repeated support locations: the argument is multiset-theoretic and uses only nonzero positivity on the `(K+1)`-atom side.

## Quantitative separation certificate

Let

\[
E(p_1,...,p_{K+1})
\]

be the polynomial obtained by applying recurrence `(5)` through degree `K+1`; on the first `K+1` power sums of a `(K+1)`-element multiset it equals its top elementary symmetric polynomial.

Hence every `q in \mathcal C_0` satisfies

\[
E(q)=0,
\tag{8}
\]

because the corresponding `K`-atom set can be padded by zero. Every `q' in \mathcal C_1(y)` satisfies

\[
E(q')
=y\prod_{i=1}^K x'_i
\ge
y\prod_{i=1}^K a_i.
\tag{9}
\]

Let

\[
a_*:=\prod_{i=1}^K a_i>0.
\]

For `0<=y<=y_0`, the union of `\mathcal C_0` and `\mathcal C_1(y)` lies in a fixed compact subset of `\mathbb R^{K+1}`. Take a compact convex set `Omega` containing that union and all line segments joining its points. Since `E` is polynomial,

\[
L:=\sup_{z\in\Omega}\|\nabla E(z)\|<\infty.
\]

For `q in \mathcal C_0` and `q' in \mathcal C_1(y)`, the mean-value inequality and `(8)`–`(9)` give

\[
a_* y
\le
|E(q')-E(q)|
\le
L\|q'-q\|.
\tag{10}
\]

Therefore

\[
\operatorname{dist}(\mathcal C_0,\mathcal C_1(y))
\ge
\frac{a_*}{L}y.
\tag{11}
\]

For the matching upper bound, choose the same nuisance tuple `x in B` on both sides. Then

\[
\|P_{K+1}(x)+v(y)-P_{K+1}(x)\|
=
\|v(y)\|
=
y\sqrt{1+y^2+\cdots+y^{2K}}
\le Cy
\tag{12}
\]

uniformly for `0<y<=y_0`. Equations `(11)` and `(12)` prove `(2)`.

So the top Newton coefficient is not merely an algebraic contradiction certificate. On any compact positive nuisance class it turns the exact separation into a quantitative statement: the two observation classes approach each other **linearly in the disappearing target coordinate**.

## Reciprocal-square shell specialization

Return to the AF-442/AF-443 shell model. Choose `K` earlier occupied shells `j_1<...<j_K` and allow only their support locations to differ between the two sources. Write

\[
x_i=r_{j_i}^{-2}.
\]

If each support stays in a fixed cell

\[
r_{j_i}\in[j_i-\rho,j_i+\rho],
\qquad 0<\rho<\frac12,
\]

then each reciprocal coordinate lies in a fixed compact positive interval

\[
x_i\in[(j_i+\rho)^{-2},(j_i-\rho)^{-2}].
\]

Let the two configurations agree everywhere else except for one target binary occupancy at shell `m`. With target reciprocal coordinate

\[
y=r_m^{-2}>0,
\]

equality of the first `K+1` consecutive reciprocal-power moments would reduce, after cancelling the common terms, to `(1)` or its reverse. The Newton argument therefore forbids the collision **for every target depth**, not merely locally and not merely for sufficiently large `m`.

If the target support is fixed at the shell center, `y=m^{-2}` and `(2)` gives

\[
\operatorname{dist}(\mathcal C_0,\mathcal C_1(m^{-2}))
=\Theta(m^{-2}).
\tag{13}
\]

If the target support may jitter inside its fixed shell cell, then

\[
(m+\rho)^{-2}
\le y\le
(m-\rho)^{-2},
\]

so `y=\Theta(m^{-2})` and the same class-level scale follows after adjusting the constants.

This gives the exact positive counterpart to AF-443. There, `K` moments leave enough local programming freedom in `K` earlier support coordinates to absorb an arbitrarily small remote mark vector. Here, the `(K+1)`st consecutive moment exposes a polynomial certificate—the top elementary symmetric function—that a `K`-atom nuisance source must make exactly zero while the source carrying the extra occupied target must make strictly positive.

## Why this is stronger than a rank count

A generic dimension argument would only suggest that `K+1` scalar observations might overdetermine `K` continuous nuisance coordinates. It would not rule out isolated intersections, singular coincidences, disconnected aliases, or a target direction accidentally lying on the lower-dimensional image.

The Newton certificate does rule them out for this source class. It proves global disjointness of the two finite-moment images, with no Jacobian regularity hypothesis. This is the additional structure that the live frontier after AF-443 required: **rank surplus plus an algebraic source law that gives a target-sensitive invariant of the compressed data**.

At the same time, `(2)` prevents overinterpreting the result. The restored discriminator is increasingly fragile as the target moves deeper into the reciprocal-square tail. Exact target purity and robust target recovery are therefore separate gates even in this favorable algebraic case.

## Prior-art and novelty audit

The algebraic core is classical. Newton-Girard identities say that the first `r` power sums recursively determine the first `r` elementary symmetric polynomials. Equivalently, the first `N` power sums of an `N`-element multiset determine its monic root polynomial and hence the multiset itself. This is standard symmetric-function theory; see I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford Mathematical Monographs, Oxford University Press (1995), Chapter I, and any standard treatment of Newton's identities.

The surrounding inverse problem is classical Prony territory. Gerlind Plonka and Manfred Tasche, **“Prony methods for recovery of structured functions,”** *GAMM-Mitteilungen* 37(2), 239–258 (2014), DOI `10.1002/gamm.201410011`, surveys reconstruction of finitely supported exponential/atomic structures from moment-type data. AF-443 already records the complementary equi-moment/Prony-leaf literature for underdetermined movable-node systems.

No novelty is claimed for Newton identities, recovery of a finite multiset from enough power sums, finite-atomic Prony reconstruction, compactness, or the mean-value inequality.

The Arithmetic Fidelity contribution is the **sharp placement of that classical algebra at the AF-443 obstruction boundary**. In the reciprocal-square unit-occupancy model, `K` retained moments can be exactly target-impure against `K` latent earlier supports, while the first `K+1` consecutive moments are globally target-pure against precisely that nuisance class. The same proof yields the conditioning price `Theta(y)`, showing that the minimal exact lift and its robustness cost are different resources.

## Boundaries and falsification checks

- The equal-weight/unit-occupancy hypothesis is essential to the stated Newton certificate. Unknown or continuously variable amplitudes add nuisance parameters and return to the broader Prony problem; `K+1` moments are not claimed sufficient there.
- The theorem treats one binary target occupancy change against exactly `K` movable occupied support coordinates. Multiple target changes, additional moving supports, or coordinated tail changes enlarge the source class and require a new audit.
- The moments are the consecutive orders `1,...,K+1`. AF-443 allows arbitrary distinct orders for its negative result, but the present proof uses the Newton-Girard closure of a consecutive prefix. An arbitrary `K+1`-element set of moment orders need not carry the same certificate.
- Strict positivity/nonvanishing of every atom on the `(K+1)`-atom side is decisive. If zero is admissible as a genuine target coordinate, adding a zero atom is invisible to every positive power moment.
- Equation `(2)` is a class-separation result on compact positive nuisance intervals. Its constants depend on those intervals and on `K`; it is not a dimension-free or shell-uniform condition number.
- The `Theta(m^{-2})` statement concerns the Euclidean separation of the declared finite observation classes. It does not by itself give an optimal decoder under a probabilistic noise model.
- The theorem does not recover the nuisance support coordinates as a practical algorithm, nor does it say the full source is globally reconstructible. It only proves that the declared binary target mark cannot flip inside a same-data fiber generated by the declared `K` support motions.
- Nothing here distinguishes rational primes, constrains the Riemann zero divisor, or implies RH. It prices one source-side fidelity repair for the reciprocal-square Euler-style carrier.

A direct falsification would require positive `x,x',y` satisfying `(1)`. Padding the `K`-atom side by zero and applying Newton-Girard to the common first `K+1` power sums would then force equality of the top elementary symmetric functions, contradicting `0=y\prod_i x'_i`.

## Consequence for the research line

AF-443 left four possible escapes: observation rank beyond nuisance dimension, source-derived constraints, retained support provenance, or observation growth faster than nuisance freedom. This result settles the cleanest finite-dimensional case sharply. **One rank-surplus consecutive moment is sufficient when the source category itself supplies a unit-weight cardinality law, and the corresponding Newton coefficient is the surviving discriminator certificate.**

The next frontier should therefore separate two questions that rank counting alone conflates:

1. which source laws turn a nominal rank surplus into an exact target-sensitive invariant; and
2. after exact target purity is restored, how quickly does the inter-class margin collapse under the relevant arithmetic tail scaling?

For the present model the answers are now explicit: the unit-atom law supplies the Newton certificate, while reciprocal-square depth prices the restored fidelity at `Theta(m^{-2})`. A useful next test is to weaken unit occupancy to a constrained weight law and determine the smallest additional moment/relational lift that preserves an analogous nonzero certificate.