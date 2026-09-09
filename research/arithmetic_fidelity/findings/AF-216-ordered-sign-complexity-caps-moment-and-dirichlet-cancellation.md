# AF-216 — ordered sign complexity caps moment and Dirichlet cancellation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `SOURCE-COMPLEXITY-GATE`, `EXACT-FIDELITY`, `CLASSICAL-BRIDGE`, `NO-NOVELTY-CLAIM`

## Claim

AF-214 and AF-215 show that neither simple support, unit multiplicity, integrality, nor even rational primality prevents arbitrarily high Prouhet moment cancellation. The surviving source-side question is therefore relational: what property of an **ordered signed discrepancy** actually limits how many low-order observations it can erase?

One exact answer is the number of sign changes.

Let

\[
x_1<x_2<\cdots<x_n
\]

be distinct real nodes and let `a_1,\ldots,a_n` be nonzero real coefficients. Write

\[
V(a_1,\ldots,a_n)
:=\#\{1\le j<n:a_ja_{j+1}<0\}
\tag{1}
\]

for the ordered sign variation. If zero coefficients are present, delete them before counting sign changes and delete their nodes from the signed support.

If, for some integer `m>=1`,

\[
\boxed{
\sum_{j=1}^n a_jx_j^k=0,
\qquad k=0,1,\ldots,m-1,
}
\tag{2}
\]

then necessarily

\[
\boxed{V(a_1,\ldots,a_n)\ge m.}
\tag{3}
\]

Equivalently, a nonzero signed atomic source with at most `r` ordered sign changes is detected by the first `r+1` polynomial moments: it cannot annihilate all of `1,x,\ldots,x^r`.

The bound is sharp. On any `m+1` ordered nodes, the barycentric/divided-difference weights from AF-195 alternate in sign exactly `m` times and annihilate every polynomial of degree below `m`.

There is an immediate multiplicative/Dirichlet specialization. Let

\[
1<q_1<q_2<\cdots<q_n,
\qquad
F(s):=\sum_{j=1}^n a_jq_j^{-s},
\tag{4}
\]

with real nonzero coefficients `a_j`. Fix any real `sigma_0` and any `h>0`. If

\[
\boxed{
F(\sigma_0+kh)=0,
\qquad k=0,1,\ldots,m-1,
}
\tag{5}
\]

then again

\[
\boxed{V(a_1,\ldots,a_n)\ge m.}
\tag{6}
\]

Hence a signed Dirichlet source with at most `r` sign changes in increasing norm order is **exactly separated from zero by `r+1` equally spaced real Dirichlet samples**. This applies in particular when all `q_j` are rational primes.

The important boundary is equally exact: this is a theorem about the sign complexity of the **signed difference being observed**, not about primality of its individual atoms. AF-215 remains valid because its high-order prime Prouhet controls necessarily spend unbounded ordered sign complexity.

## Derivation

### 1. A sign-matching polynomial kills low-variation moment nulls

Suppose

\[
r:=V(a_1,\ldots,a_n)<m.
\tag{7}
\]

Let

\[
i_1<i_2<\cdots<i_r
\]

be the indices at which the coefficient sign changes, so

\[
a_{i_\ell}a_{i_\ell+1}<0.
\]

Choose one point

\[
t_\ell\in(x_{i_\ell},x_{i_\ell+1})
\qquad(1\le\ell\le r)
\tag{8}
\]

and form

\[
Q(x):=c\prod_{\ell=1}^r(x-t_\ell),
\tag{9}
\]

where the global sign `c in {+1,-1}` is chosen so that `a_1Q(x_1)>0`.

As `x` crosses each selected gap, `Q` changes sign exactly once. Those are exactly the gaps where the coefficient sequence changes sign. Therefore

\[
\boxed{a_jQ(x_j)>0\qquad(1\le j\le n).}
\tag{10}
\]

In particular,

\[
\sum_{j=1}^na_jQ(x_j)>0.
\tag{11}
\]

But `deg Q=r<m`, so `(2)` annihilates `Q` by linearity:

\[
\sum_{j=1}^na_jQ(x_j)=0,
\tag{12}
\]

contradicting `(11)`. Thus `r<m` is impossible and `(3)` follows.

This proof is finite, exact, and uses no spacing, size, or arithmetic assumptions on the ordered nodes.

### 2. AF-195 makes the lower bound sharp

AF-195 considers any `m+1` distinct ordered nodes

\[
u_0<u_1<\cdots<u_m
\]

and the barycentric weights

\[
\lambda_j
=\frac{1}{\prod_{\ell\ne j}(u_j-u_\ell)}.
\tag{13}
\]

They satisfy

\[
\sum_{j=0}^m\lambda_jP(u_j)=0
\qquad
\text{for every polynomial }P\text{ with }\deg P<m.
\tag{14}
\]

Because the nodes are ordered,

\[
\operatorname{sgn}(\lambda_j)=(-1)^{m-j},
\tag{15}
\]

so this source has exactly `m` sign changes. Therefore `(3)` cannot be improved: cancellation of `m` consecutive polynomial moments requires at least `m` ordered sign changes, and `m` sign changes already suffice when arbitrary real weights are permitted.

This also separates **support complexity** from **sign complexity**. Equation `(3)` implies `n>=m+1`, but having many atoms does not by itself buy high-order cancellation; the signed mass must alternate sufficiently often in source order.

### 3. Arithmetic-grid Dirichlet samples are polynomial moments after one monotone change of variable

For `(4)`--`(5)`, put

\[
y_j:=q_j^{-h},
\qquad
b_j:=a_jq_j^{-\sigma_0}.
\tag{16}
\]

All factors `q_j^{-sigma_0}` are positive, so

\[
V(b_1,\ldots,b_n)=V(a_1,\ldots,a_n).
\tag{17}
\]

Also `q_1<\cdots<q_n` and `h>0` imply

\[
y_1>y_2>\cdots>y_n>0.
\tag{18}
\]

Reversing the whole sequence does not change the number of sign changes. Finally,

\[
F(\sigma_0+kh)
=\sum_{j=1}^na_jq_j^{-\sigma_0}q_j^{-kh}
=\sum_{j=1}^nb_jy_j^k.
\tag{19}
\]

Thus the `m` vanished samples in `(5)` are exactly the first `m` polynomial moments of the signed atomic measure on the distinct nodes `y_j`. Applying `(3)` proves `(6)`.

This reduction is deliberately modest: it needs only an arithmetic progression of real exponents and does not invoke analytic continuation, an Euler product, or a spectral wrapper.

## Relation to the AF-213--AF-215 obstruction chain

AF-213 uses Hobby--Rice signs to show constructively that `O(m)` variation can buy exact annihilation of `m` polynomial observables on a continuum source, which analytic approximation then turns into exponentially small fixed-band Euler observations. AF-214 realizes arbitrary-order moment cancellation with two simple unit-weight integer sets. AF-215 then shows that rational-prime support itself does not remove that resource, because arbitrarily long prime arithmetic progressions can carry Prouhet labels.

AF-216 supplies the converse source-complexity statement missing from that chain:

\[
\boxed{
\text{annihilate }m\text{ consecutive moments}
\quad\Longrightarrow\quad
\text{spend at least }m\text{ ordered sign changes}.
}
\tag{20}
\]

Therefore the AF-214/AF-215 controls do not obtain arbitrary order from integrality or primality for free. Their signed difference must become increasingly oscillatory in the natural order. A source category that independently bounds this oscillation **does** block the Prouhet moment-flatness mechanism at finite order.

This is the first exact positive gate after AF-215 among the candidate relational restrictions named there: bounded ordered sign variation really is sufficient to cap cancellation order. It does not establish that the canonical prime-derived source has that property.

## Exact controls and boundaries

### The restriction belongs to the difference source, not to each positive source separately

If two positive atomic sources are compared, merge their supports and form the signed coefficient sequence of their difference in increasing source order. It is the sign variation of that merged signed sequence that enters `(3)` and `(6)`.

Bounding the sign changes of each source individually is vacuous because a positive source has none. What matters is how often the two sources overtake one another after the chosen observable representation has fixed a common ordered support.

### Pointwise primality is still insufficient

AF-215 constructs prime-supported unit-weight controls of arbitrary Prouhet order. Equation `(3)` does not refute them; it proves that their merged `+/-` pattern must have at least the requested number of sign changes.

Thus primality remains an atomwise label, while bounded sign variation is a genuinely relational/global constraint on a whole signed configuration.

### Exact detection is not quantitative conditioning

Equations `(3)` and `(6)` are zero-error statements. They show that a low-sign-variation source cannot lie in the exact kernel of the declared finite observation map.

They do **not** give a uniform lower bound of the form

\[
\|\text{source}\|\le C\|\text{observations}\|
\]

with constants independent of support geometry, scale, coefficient dynamic range, or the sign budget. Near-collisions may remain arbitrarily ill-conditioned. The conditioning results AF-209--AF-213 therefore remain separate.

### The Dirichlet corollary is not yet an Euler-factor recovery theorem

The map in `(4)` is a finite Dirichlet/Laplace sum. The full logarithmic Euler factor contains higher harmonics,

\[
-\log(1-q^{-s})=\sum_{\ell\ge1}\frac{q^{-\ell s}}{\ell},
\]

so `(6)` does not by itself lower-bound a full Euler-product discrepancy. What it does rule out is arbitrary exact cancellation of the first-harmonic Dirichlet samples, and `(3)` independently rules out arbitrary Prouhet/Taylor moment order under a fixed sign budget.

A quantitative Euler consequence needs an additional theorem showing that the first surviving moment or Dirichlet component cannot be cancelled or overwhelmed by the remaining harmonics in the declared source class.

### The bound is sharp for arbitrary weights, not necessarily for unit weights

AF-195 attains equality `V=m` with barycentric weights on `m+1` arbitrary nodes. Those weights are generally not `+/-1`.

AF-214 and AF-215 impose unit multiplicity and use larger Prouhet configurations. AF-216 does not classify the minimum support size or sign complexity under the simultaneous constraints of unit weights, primality, prescribed density, or another arithmetic provenance rule.

### No intrinsic prime sign budget has been established

Nothing here proves that a natural rational-prime versus matched-control discrepancy has uniformly bounded sign variation. Indeed, many classical arithmetic error terms oscillate. Any RH-facing use therefore has to derive the relevant sign/oscillation restriction from the concrete prime mechanism rather than impose it because it makes recovery possible.

## Prior art and novelty assessment

The abstract sign-change theorem is classical Chebyshev-system / total-positivity mathematics. No novelty is claimed for the principle that a nonzero signed object orthogonal to an `m`-dimensional Chebyshev system must have sufficient oscillation.

- Samuel Karlin and William J. Studden, ***Tchebycheff Systems: With Applications in Analysis and Statistics***, Interscience, New York (1966), is a foundational reference for Chebyshev systems, moment spaces, and the oscillation/sign-change principles behind `(3)`.
- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968), is the classical systematic source for total positivity and variation-diminishing/sign-regular phenomena. The polynomial Vandermonde family used here is the elementary finite model of that theory.
- R. A. Zalik, **“Čebyšev and Weak Čebyšev Systems,”** in Mariano Gasca and Charles A. Micchelli (eds.), *Total Positivity and Its Applications*, Mathematics and Its Applications 359, Springer/Kluwer (1996), pp. 301--332, DOI `10.1007/978-94-015-8674-0_15`, surveys the Chebyshev-system framework and explicitly points back to Karlin and Karlin--Studden.

The proof of `(3)` is included directly because in this finite atomic setting the needed oscillation theorem reduces to the sign-matching polynomial `(9)`. The arithmetic-grid Dirichlet statement `(6)` is then an immediate monotone change-of-variable specialization. No claim is made that either abstract fact is new.

The durable Arithmetic Fidelity contribution is the placement of this classical boundary against AF-213--AF-215: **arbitrary Prouhet cancellation survives integrality and primality, but it cannot survive a fixed budget of ordered sign variation.** This identifies a precise relational resource that the previous matched controls necessarily consume.

## Consequence for the Arithmetic Fidelity frontier

The source-side fork is now sharper. `Actual primality` is not a sufficient recovery hypothesis, while `bounded ordered sign variation of the signed discrepancy` is sufficient to stop arbitrary-order moment cancellation and to make finitely many real Dirichlet samples zero-error faithful on that restricted class.

The next arithmetic question is therefore not whether primes are special atom by atom. It is whether a concrete prime-derived discriminator and its admissible matched controls obey a **source-forced oscillation law**: a bound on sign changes, a relation between sign complexity and observation bandwidth, or another global restriction that cannot be reproduced by the AF-214/AF-215 constructions.

If no such law is available for the actual source category, AF-216 remains a useful exact classification of what would repair the compression but not evidence that the repair applies to RH.