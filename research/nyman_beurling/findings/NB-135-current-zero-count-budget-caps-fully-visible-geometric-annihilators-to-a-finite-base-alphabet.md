# NB-135 — current zero-count budget caps fully visible geometric annihilators to a finite base alphabet

**Status:** `EXACT-DERIVED + NB-132/NB-134-SPLICE + SOURCE-ENVELOPE-CAP + FINITE-GEOMETRIC-BASE-ALPHABET + GROWING-MULTIBASE-BARRIER + MATCHED-ENVELOPE-CONTROL + ROUTE-NARROWING + PRIOR-ART-AUDITED`.

`NB-134` leaves a seemingly direct escape from the simultaneous collapse of every fixed finite family of scalar geometric annihilators: let the number of integer bases grow with the natural cutoff `R`. In the source-faithful polynomial-height regime of `NB-132`, however, that repair cannot simply retain one fully visible recurrence at every new base.

The obstruction is already present in the explicit zero-count budget. At height at most `R^A` and fixed ordinate width `W`, the Bellotti--Wong--Fiori endpoint error leaves a right-half-plane rank allowance with leading coefficient

\[
C_{A,W}
:=
A\left(\frac{W}{4\pi}+0.10076\right).
\]

A `q`-geometric trace inside the natural prefix `1,...,R` has depth only `log_q R=(log R)/(log q)`. Therefore the `NB-132` argument can certify the **entire** recurrence of every packet allowed by that zero-count bound only when

\[
C_{A,W}<\frac1{\log q}.
\]

For fixed `A,W` this places `q` in a finite set. Even if the fixed width is taken arbitrarily small, the endpoint-error term remains and forces

\[
q<\exp\!\left(\frac1{0.10076A}\right).
\]

Thus **the current source law supplies only finitely many integer geometric bases on which full scalar annihilators are uniformly recurrence-visible.** Combining this with `NB-134`, every such fully certified finite family is still vulnerable to simultaneous superpolynomial scalar-margin collapse in the matched formal model. Bases beyond the cap may contain useful partial information, but they are no longer covered by the `NB-132` full-recurrence certificate.

This closes a precise version of the "let the number of bases grow" escape. Mere growth of the base family is not compatible with keeping the same one-annihilator-per-base architecture under the present zero-count input. A successful growing-representation argument must instead use partial traces jointly, strengthen the local actual-zero rank law, move to a richer natural-grid observable, or change the height scaling.

## 1. The `NB-132` rank budget and geometric sample budget have incompatible large-base asymptotics

Fix constants

\[
A>0,
\qquad
W>0.
\tag{1}
\]

Let `F` be a genuine right-half-plane zeta-zero packet as in `NB-132`: its positive ordinates lie in one half-open interval

\[
T<\gamma\le T+W,
\qquad
T+W\le R^A,
\tag{2}
\]

and every zero is used no more often than its true multiplicity. Write `d(F)` for the total confluent rank.

The Bellotti--Wong--Fiori zero-counting estimate, followed by the off-critical functional-equation symmetry exactly as in `NB-132`, gives

\[
d(F)
\le
C_{A,W}\log R
+0.24460\log\log R
+O_{A,W}(1),
\tag{3}
\]

where

\[
\boxed{
C_{A,W}
=
A\left(\frac{W}{4\pi}+0.10076\right).
}
\tag{4}
\]

Now fix an integer geometric base `q>=2`. The natural prefix contains the powers

\[
1,q,q^2,\ldots,q^{\lfloor\log_qR\rfloor},
\tag{5}
\]

so its asymptotic recurrence-depth budget is

\[
\frac{\log R}{\log q}+O(1).
\tag{6}
\]

The `NB-124` full annihilator for a rank-`d(F)` packet is guaranteed to lie inside the prefix once

\[
d(F)+1\le\log_qR.
\tag{7}
\]

Using only `(3)`, a uniform large-`R` implication `(3) => (7)` therefore requires strict leading-coefficient slack:

\[
\boxed{
C_{A,W}<\frac1{\log q}.
}
\tag{8}
\]

The strictness matters. At equality, the positive `0.24460 log log R` term in `(3)` is already larger than the `O(1)` slack in the geometric depth, so the same zero-count estimate still does not certify `(7)`.

Solving `(8)` for the base gives the explicit **certified base cap**

\[
\boxed{
q<Q(A,W)
:=
\exp\!\left(
\frac1{A(W/(4\pi)+0.10076)}
\right).
}
\tag{9}
\]

Hence, for fixed polynomial-height exponent and fixed ordinate width, the set of integer bases for which the `NB-132` source estimate certifies the whole recurrence is finite.

## 2. Shrinking the fixed width cannot make the certified alphabet grow without bound

One might try to recover arbitrarily large bases by taking a narrower ordinate window. But the main-term contribution `AW/(4pi)` is not the limiting obstruction in `(4)`. The two zero-counting endpoint errors leave the positive coefficient `0.10076A` even as the fixed width tends to zero.

Optimizing `(9)` over arbitrarily small fixed `W>0` therefore gives the limiting cap

\[
\boxed{
Q_A^{\rm lim}
:=
\exp\!\left(\frac1{0.10076A}\right).
}
\tag{10}
\]

More precisely, every fixed base certified by the `NB-132` leading-coefficient argument must satisfy

\[
q<Q_A^{\rm lim}.
\tag{11}
\]

Thus if `mathcal Q_R` is any family of **distinct integer bases** and every member is required to carry a separately certified full recurrence under the same fixed polynomial-height exponent `A`, then the current zero-count argument forces

\[
\boxed{
\mathcal Q_R
\subset
\{q\in\mathbb Z:q\ge2,\ q<Q_A^{\rm lim}\},
}
\tag{12}
\]

for all sufficiently large cutoffs. In particular `|mathcal Q_R|` is uniformly bounded; it cannot tend to infinity.

The numerical scale is useful as a sanity check. For linear height `A=1` and width `W=1`,

\[
C_{1,1}
=
\frac1{4\pi}+0.10076
=0.1803374715\ldots,
\tag{13}
\]

and

\[
Q(1,1)=255.99516\ldots.
\tag{14}
\]

So this particular certificate can cover integer bases only through `q=255`; `q=256` already misses the leading-coefficient inequality. If the fixed width is allowed to approach zero, the linear-height limiting cap is still only

\[
Q_1^{\rm lim}
=20426.19129\ldots,
\tag{15}
\]

so `q=20427` can never be recovered by merely shrinking a fixed band inside the same Bellotti--Wong--Fiori endpoint estimate.

These numerical caps are not asserted to be intrinsic constants of the zeta function. They quantify the information supplied by the **current source envelope**.

## 3. Beyond the cap, the present source envelope genuinely leaves room for hidden recurrence order

Failure of `(8)` is not a theorem that an actual zeta packet must be invisible. It says that the source information used by `NB-132` no longer forces visibility. A matched envelope control shows that this distinction is real rather than notational.

Suppose

\[
\frac1{\log q}<C_{A,W}.
\tag{16}
\]

Choose a constant `c` satisfying

\[
\frac1{\log q}<c<C_{A,W}
\tag{17}
\]

and put

\[
d_R:=\lfloor c\log R\rfloor.
\tag{18}
\]

Then for large `R`,

\[
\boxed{
 d_R+1>\log_qR,
}
\tag{19}
\]

so an order-`d_R` recurrence does not fit inside the `q`-geometric part of the natural prefix. At the same time,

\[
d_R<C_{A,W}\log R,
\tag{20}
\]

so a formal right-half packet of that rank in a width-`W` band does not violate the numerical rank allowance `(3)`.

As in `NB-133`, the points can be chosen distinct in the ordinate direction and placed at a real part a fixed factor to the left of the explicit Vinogradov--Korobov forbidden boundary. Adding their functional-equation partners produces a symmetric formal configuration compatible with the same **coarse** count and zero-free envelopes. This does not manufacture genuine zeta zeros; it is a matched control showing that those envelopes alone do not distinguish a rank that has already outrun the base-`q` sample depth.

The limiting cap `(10)` has the same envelope interpretation. If

\[
q>Q_A^{\rm lim},
\tag{21}
\]

then

\[
\frac1{\log q}<0.10076A.
\tag{22}
\]

A sufficiently small fixed `W>0` still satisfies `(16)`, so narrowing the physical band cannot restore full-recurrence certification for that base without introducing a stronger source estimate.

## 4. `NB-134` now exhausts the separately visible scalar-base repair under the current gate

The point of `(9)--(12)` is not merely that very large geometric bases have short traces. It closes the exact escape left by `NB-134` **within the current source-faithful certification architecture**.

Take any fixed `A,W` and collect all integer bases satisfying `(8)`. This collection is finite. If one works with any finite subfamily

\[
\mathcal Q\subset\{q:C_{A,W}<1/\log q\},
\tag{23}
\]

then every base has enough natural-prefix depth for the `NB-132` full-recurrence gate. But `NB-134` shows that, under the same coarse count/depth compatibility, a formal polynomial-height packet can make the normalized `NB-124` annihilator margin collapse faster than every power of `R` **at every base in that fixed family simultaneously**.

Trying to add more and more distinct integer bases eventually forces some `q` outside `(23)`. At that point the new base may still carry useful labelled phase samples or a shorter recurrence fragment, but the argument no longer possesses a separately certified full `NB-124` annihilator there. Consequently the architecture

\[
\text{one fully visible scalar annihilator per base}
\quad+\quad
\text{finite/scalar aggregation}
\tag{24}
\]

cannot be rescued simply by declaring that the number of bases grows with `R`: the source gate itself prevents an unbounded supply of such full annihilators.

This is stronger than the fixed-family statement of `NB-134` in one specific sense and weaker in another. It rules out **mere base-count growth while preserving the same full-recurrence proof at every base**. It does not rule out a genuinely joint certificate that combines many partial traces before annihilation, nor a stronger actual-zero theorem that lowers the rank budget enough for large bases to become visible.

## 5. What would have to change for growing multibase information to become useful

The cap identifies exactly which parameter must move.

A stronger short-band zero-count law with right-half rank

\[
d(F)=o(\log R)
\tag{25}
\]

would qualitatively change the picture: then bases `q=q(R)` with `log q=o(log R/d(F))` could become fully recurrence-visible. The present endpoint error is `Theta(log T)=Theta(log R)` at polynomial height, so it does not provide that shrinking coefficient.

Alternatively, one can keep the current source law but stop demanding a full recurrence at every base. Large bases still reveal short labelled traces, and those traces might become useful if a joint multibase functional retains their cross-base correspondence instead of scalarizing each base separately. The natural grid of `NB-128` is the extreme version of this idea: its information content grows without paying for a separate order-`d` geometric recurrence at each integer scale.

A third escape is to alter the height law. The finite cap `(10)` depends on fixed `A>0`; if the relevant support height were `R^{A(R)}` with `A(R)->0`, the endpoint-error rank budget would shrink relative to `log R` and the certified base alphabet could grow. That is a different asymptotic regime and is not supplied by the current polynomial-height packet analysis.

Thus the live question after `NB-134` is no longer simply whether "more bases" help. It is whether the line can obtain **more independently conditioned information per unit of zero-count rank**: through sharper actual-zero arrangement/counting, a joint partial-trace certificate, or a non-geometric observation scheme.

## Adversarial stress tests

Several possible overclaims were checked before canonicalization.

First, `(8)` is a sufficiency threshold for the `NB-132` proof based on the current explicit zero-count upper bound; its failure is **not** an assertion that actual zeta zeros realize the worst allowed rank. Sections 3--4 keep the distinction explicit and use formal packets only as matched envelope controls.

Second, taking `W` small does not remove the `0.10076A log R` contribution because it comes from the two endpoint errors in `N(T+W)-N(T)`, after the right-half symmetry factor. The cap `(10)` is therefore genuinely present in this proof even for arbitrarily narrow fixed bands.

Third, a growing family with many multiplicatively dependent bases does not evade `(12)`: the obstruction here is sample depth, not Diophantine independence. Conversely, multiplicative independence does not worsen the cap; `(8)` is per-base and depends only on `q`.

Fourth, `NB-134` is used only after restricting to the finite set of bases satisfying `(8)`. No claim is made that its fixed-family simultaneous-recurrence proof remains uniform for a family whose largest base tends to infinity.

Fifth, the conclusion concerns **separately formed full scalar annihilators**. A joint functional can use information from a base even when fewer than `d+1` powers of that base are visible, so `(12)` does not cap all possible growing multibase representations.

The numerical check at `A=W=1` also catches the threshold orientation: `1/log 255=0.18046425...` remains above `C_(1,1)`, while `1/log 256=0.18033688...` is already below it. Thus `255` is the last integer base certified by the leading-coefficient gate in that example.

## Prior-art audit

The only load-bearing external estimate is the Bellotti--Wong--Fiori explicit zero-counting bound already anchored in `SOURCES.md` and already used by `NB-132`; no new source dependency is introduced here. A fresh search confirmed the published bound with leading coefficient `0.10076` and did not locate a later uniform explicit `N(T)` estimate that would alter the present calculation.

A targeted search around short-interval zeta-zero statistics, zero-density estimates, and Nyman--Beurling multiscale formulations found neighboring work but not the specific source-budget comparison `(8)--(12)`: the geometric observation depth decays like `1/log q`, while the current polynomial-height right-half zero-count allowance retains a positive `Theta(log R)` coefficient independent of `q`. Recent work on local zero statistics and inverse theorems for large zeta sums is arrangement-sensitive rather than a replacement for this uniform endpoint rank bound.

Accordingly `SOURCES.md` needs no update.

## Route consequence

`NB-132` made a visible recurrence source-faithful in a concrete narrow polynomial-height regime. `NB-133` showed that one such visible scalar annihilator can still be superpolynomially ill-conditioned, and `NB-134` extended that collapse to every fixed finite family of fully visible scalar bases.

`NB-135` closes the naive next move. **Under the same explicit zero-count gate, the collection of integer bases on which full recurrence visibility can be certified is itself finite.** Therefore the route cannot escape `NB-134` merely by letting the number of separately annihilated geometric bases diverge.

The next useful theorem has to change one of the currencies: reduce the actual-zero rank budget below the present `Theta(log R)` endpoint allowance, combine growing partial traces before scalar annihilation, exploit natural-grid phase geometry, or derive an actual-zero arrangement law that yields conditioning without requiring an unbounded alphabet of full geometric recurrences.