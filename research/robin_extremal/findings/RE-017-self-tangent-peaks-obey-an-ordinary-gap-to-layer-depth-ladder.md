# RE-017 — self-tangent peaks obey an ordinary-gap-to-layer-depth ladder

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIME-ENVELOPE-GAP-BUDGET + RECIPROCAL-LAYER-DEPTH-LADDER + SMALL-PRIME-BOUNDARY-COMPRESSION + SUBLOG-GAP-SPARSITY + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-003` proves that every sufficiently large regular self-tangent CA local Robin peak needs an adjacent CA event gap carrying asymptotically at least half of the two boundary jump masses. `RE-004` separately shows that higher prime-power transition coordinates have zero ambient count density, but that density statement alone does not constrain how a selected subsequence of peaks could concentrate on the exceptional chamber.

The two facts can be coupled through the density-one first prime layer. Every adjacent CA event gap sits inside a unique envelope formed by two consecutive first-layer prime events. The width of that ordinary-prime envelope imposes a quantitative budget on **which prime-power layers are even allowed to occur at the two peak boundaries**.

Let `C` be a sufficiently large regular self-tangent CA local peak, put

\[
X:=\log C,
\]

and let

\[
\eta_-<X<\eta_+
\]

be its adjacent CA transition coordinates. If `A<C<B` are the neighboring CA states, write

\[
w_-:=\log(C/A),\qquad w_+:=\log(B/C).
\tag{1}
\]

Let `u<v` be the consecutive ordinary primes whose first-layer event coordinates are the nearest ones enclosing the whole adjacent event gap:

\[
\eta_{u,1}\le \eta_-<\eta_+\le \eta_{v,1},
\tag{2}
\]

and put

\[
g:=v-u.
\tag{3}
\]

For each prime factor `r` of either adjacent CA quotient `C/A` or `B/C`, let `j(r)` be the prime-power layer whose event occurs at the corresponding boundary transition. Define the reciprocal boundary-depth mass

\[
\boxed{
\mathcal H(C):=
\sum_{r\mid C/A}\frac1{j(r)}
+
\sum_{r\mid B/C}\frac1{j(r)}.
}
\tag{4}
\]

Alaoglu--Erdos implies that each adjacent quotient is a prime or a product of two distinct primes, so (4) contains at most four terms. Then

\[
\boxed{
g\ge \frac{\mathcal H(C)}2\log X-O(1).}
\tag{5}
\]

Moreover every boundary factor satisfies

\[
\boxed{
\log r<2g+2+o(1)
}
\tag{6}
\]

and its layer depth satisfies

\[
\boxed{
 j(r)\ge
 \frac{\log X-O(1)}{2g+2+o(1)}.
}
\tag{7}
\]

Thus an exceptional peak cannot be placed in an arbitrarily small ordinary-prime gap by a shallow higher layer. Small prime envelopes force the boundary transitions into successively deeper prime-power towers.

For every fixed integer `J>=1` and every fixed `delta>0`, (5) gives the phase implication

\[
\boxed{
 g\le\left(\frac1{2J}-\delta\right)\log X
 \quad\Longrightarrow\quad
 j(r)\ge J+1
 \text{ for every factor at both boundary transitions}
}
\tag{8}
\]

for all sufficiently large such peaks. Combining (8) with the layer-count estimate of `RE-004`, the number `N_{J,\delta}(Z)` of regular self-tangent CA local peaks with `X<=Z` satisfying the left side of (8) obeys

\[
\boxed{
N_{J,\delta}(Z)
=O_{J,\delta}\!\left(
 (Z\log Z)^{1/(J+1)}\log Z
\right).
}
\tag{9}
\]

In particular, along any family of such peaks for which

\[
g=o(\log X),
\tag{10}
\]

every boundary layer depth tends to infinity and every boundary factor prime satisfies

\[
\boxed{r=X^{o(1)}.}
\tag{11}
\]

The family is forced into every fixed deep-layer exceptional chamber eventually. Consequently its counting function is subpolynomial: for every fixed `epsilon>0`,

\[
\boxed{N(Z)=O_\epsilon(Z^\epsilon).}
\tag{12}
\]

Equation (12) is a host-set statement, not an exclusion theorem. A hypothetical Robin-counterexample subsequence can in principle be arbitrarily sparse. Its value is that the unresolved exceptional branch now has a quantitative alternative: either the surrounding ordinary prime gaps retain a positive logarithmic-scale width, or the counterexample peaks must migrate into diverging-depth towers of subpolynomial primes on a subpolynomial set of admissible event gaps.

## 1. Every CA event gap has a consecutive-prime envelope

First-layer event order is exactly ordinary prime order by `RE-003`, and

\[
p\le\eta_{p,1}<p+1
\tag{13}
\]

for every prime `p`. For sufficiently large `X`, there are first-layer events on both sides of the finite interval `[eta_-,eta_+]`. Choose `u` as the largest prime whose first-layer coordinate is at most `eta_-`, and `v` as the smallest prime whose first-layer coordinate is at least `eta_+`.

There can be no first-layer event strictly between them. None lies between `eta_-` and `eta_+` because those are adjacent transition coordinates; none lies between `eta_(u,1)` and `eta_-` or between `eta_+` and `eta_(v,1)` by the extremal definitions of `u` and `v`. Hence `u<v` are consecutive ordinary primes.

Write

\[
\eta_{p,1}=p+\delta_p,
\qquad 0\le\delta_p<1.
\tag{14}
\]

Then (2) gives

\[
\eta_+-\eta_-
\le \eta_{v,1}-\eta_{u,1}
=g+\delta_v-\delta_u
<g+1.
\tag{15}
\]

`RE-003` gives the local peak clearance law

\[
\eta_+-\eta_-
>
\frac{w_-+w_+}{2}
-O\!\left(\frac{(\log X)^2}{X}\right).
\tag{16}
\]

Combining (15)--(16) yields the useful total boundary-mass budget

\[
\boxed{
w_-+w_+<2g+2+o(1).}
\tag{17}
\]

No assumption that either actual boundary transition is first-layer has entered. Equation (17) applies equally to prime, semiprime-tied, and higher-layer adjacent CA jumps.

Since the logarithmic mass of a boundary quotient is the sum of the logarithms of its prime factors, every factor `r` satisfies

\[
\log r\le w_-+w_+,
\]

and (6) follows from (17).

## 2. An event at height `X` forces `j log r` to be of order `log X`

The CA abundance increment for a prime `r` and layer `j>=1` is exactly

\[
\lambda_{r,j}
=
\log\!\left(
1+\frac1{r+r^2+\cdots+r^j}
\right),
\tag{18}
\]

and its event coordinate satisfies

\[
\eta_{r,j}\log\eta_{r,j}
=\frac{\log r}{\lambda_{r,j}}.
\tag{19}
\]

Put

\[
S:=r+r^2+\cdots+r^j.
\]

Since

\[
r^j\le S<2r^j,
\qquad
0<S^{-1}\le\frac12,
\]

the elementary bounds

\[
\frac{u}{1+u}\le\log(1+u)\le u
\qquad(u>0)
\]
give

\[
\frac1{3r^j}<\lambda_{r,j}\le\frac1{r^j}.
\tag{20}
\]

Consequently

\[
\boxed{
r^j\log r
\le\eta_{r,j}\log\eta_{r,j}
<3r^j\log r.}
\tag{21}
\]

The left inequality is the event-size bound already used in `RE-003`; the reverse constant-factor inequality is the extra ingredient needed here. The left side of (21) also implies `r<=eta_(r,j)`. Taking logarithms in the right side and using `log log r<=log log eta_(r,j)` therefore yields

\[
\boxed{
j\log r>\log\eta_{r,j}-\log3.}
\tag{22}
\]

The two actual boundary event coordinates are uniformly comparable with `X`. The right one satisfies `eta_+>X`. For the left one, take `n=floor(X/2)`; Bertrand's postulate gives a prime `s` with `n<s<2n`, and (13) gives

\[
\eta_{s,1}<s+1\le2n\le X.
\]

Since `eta_-` is the last transition before `X`,

\[
\eta_->X/2-1,
\]
so in particular `eta_->X/3` for large `X`. Thus every factor event at either boundary satisfies

\[
\boxed{j(r)\log r\ge\log X-O(1).}
\tag{23}
\]

Combining (23) with (6) proves (7).

## 3. The reciprocal-depth mass controls the ordinary prime gap

For every factor `r` at either boundary, (23) gives

\[
\log r\ge\frac{\log X-O(1)}{j(r)}.
\tag{24}
\]

Alaoglu--Erdos bounds the total number of factors in the two adjacent quotients by four, so summing (24) introduces only an absolute `O(1)` error. Therefore

\[
w_-+w_+
\ge
\mathcal H(C)\log X-O(1).
\tag{25}
\]

Insert (25) into the peak-clearance budget (15)--(16). This proves (5):

\[
g\ge\frac{\mathcal H(C)}2\log X-O(1).
\]

The clean chamber is recovered as a calibration. If both transitions are single first-layer events, `mathcal H(C)=2`, so (5) gives

\[
g\ge\log X-O(1),
\]
consistent with the sharper additive `log p+o(1)` gate of `RE-006`. The purpose of (5) is not to replace that clean result, but to interpolate the exceptional cases. A first-layer/second-layer pair has reciprocal-depth mass at least `1+1/2`, forcing `g>=(3/4)log X-O(1)`; two second-layer boundaries force `g>=(1/2)log X-O(1)`. Deeper layers weaken the required ordinary gap only in direct proportion to the reciprocal of their depth.

Ties only strengthen this constraint because every additional prime factor contributes another positive `1/j` term to `mathcal H(C)`.

## 4. Small envelopes force both boundaries into deep exceptional layers

Fix `J>=1` and `delta>0`. If any factor event at either boundary had `j(r)<=J`, then

\[
\mathcal H(C)\ge\frac1J.
\]

Equation (5) would imply

\[
g\ge\frac1{2J}\log X-O(1).
\tag{26}
\]

Therefore the strict logarithmic margin

\[
g\le\left(\frac1{2J}-\delta\right)\log X
\]
forces **every** factor event on both sides to have depth at least `J+1` once `X` is large. This proves (8).

This produces a nested exceptional hierarchy rather than one undifferentiated higher-layer chamber. For example, an envelope below `(1/2-delta)log X` cannot have any first-layer factor at either boundary; below `(1/4-delta)log X` it cannot have a first- or second-layer factor; and so on.

Equation (6) supplies the complementary prime-size statement. If a family has `g=o(log X)`, then every factor satisfies `log r=o(log X)`, hence `r=X^{o(1)}`. Equation (7) simultaneously gives `j(r)->infinity`. Small ordinary-prime envelopes therefore force the exceptional transition through **deep powers of subpolynomial primes**, not through shallow layers of primes comparable with a fixed power of `X`.

## 5. The depth ladder upgrades ambient sparsity to a selected host-set bound

`RE-004` counts layer occurrences of depth at least `R` up to event coordinate `Z` by

\[
M_{\ge R}(Z)
=O_R\!\left((Z\log Z)^{1/R}\log Z\right).
\tag{27}
\]

A regular self-tangent state in one open event gap is unique because the cumulative event mass is constant there while `X` increases strictly. Hence mapping a peak to its left boundary transition is injective.

For a peak counted by `N_(J,delta)(Z)`, equation (8) says that its left boundary contains an event of layer at least `J+1`, and that boundary lies below the peak coordinate `X<=Z`. Therefore

\[
N_{J,\delta}(Z)
\le M_{\ge J+1}(Z)+O(1),
\]
which is (9).

Now consider any family for which `g=o(log X)`. For every fixed `J`, condition (8) eventually holds with, for example, `delta=1/(4J)`. Hence its counting function is eventually bounded by (9) for every `J`. Given `epsilon>0`, choose `J` so large that `1/(J+1)<epsilon/2`; the remaining logarithmic factors are absorbed by `Z^(epsilon/2)` for large `Z`. This proves (12).

This is substantially thinner than the generic `O(sqrt(Z log Z))` higher-layer host set of `RE-004`, but only under the additional sublogarithmic ordinary-envelope hypothesis. It does not imply that all exceptional self-tangent peaks are subpolynomially sparse.

## 6. Prior art and novelty boundary

The CA variational thresholds and the theorem that a quotient of consecutive CA numbers is a prime or a product of two distinct primes are classical Alaoglu--Erdos inputs already anchored in `SOURCES.md`. `RE-003` supplies the Mathia secant-clearance law and the exact first-layer localization; `RE-004` supplies the higher-layer occurrence hierarchy. Mantovanelli's August 2026 prime-layer workload preprint is the closest representation-level prior art for event coordinates, self-tangent returns, packet identities, and prime-frontier decompositions.

A targeted current search across Robin/CA transition literature, prime-layer workload terminology, and prime-gap formulations found the Mantovanelli framework and neighboring consecutive-CA work, but not the reciprocal-depth envelope law (5), the factor compression (6)--(7), or the selected sparsity consequence (9)--(12). No blanket novelty claim is made: (20)--(25) are elementary once the existing event representation and peak-clearance theorem are combined. The durable delta is the **selection-specific gap/depth tradeoff** inside the exceptional chamber.

No new source anchor is required. All non-elementary inputs used here are already represented in `SOURCES.md`; the reverse inequality in (20) is elementary, and Bertrand's postulate is used only to keep the left adjacent event coordinate within a fixed multiplicative factor of `X`.

## 7. Boundaries and research consequence

The ordinary gap `g` in this finding is the gap between the consecutive first-layer prime events that **envelope the two actual adjacent CA transitions**. When a boundary itself is first-layer this envelope endpoint coincides with it; when both boundaries are higher-layer, the envelope may be wider than the actual event gap. Equation (5) is therefore a necessary condition, not a reconstruction of the boundary transitions from the ordinary primes.

Local Robin maximality is load-bearing through the secant-clearance inequality (16). A regular self-tangent state that is not a local peak need not obey the half-mass event-gap budget and therefore need not satisfy (5). The result applies to safe and violating local peaks alike; counterexample status enters only when it is combined with the `RE-001` RH-failure reduction.

The `O(1)` in (5) deliberately sacrifices the additive precision available in the fully clean chamber. `RE-006` remains the authoritative sharp result there. The point here is uniformity over higher-layer and tied transitions, for which the reciprocal layer depths distinguish how much logarithmic boundary mass must fit inside the surrounding ordinary-prime gap.

Finally, subpolynomial host-set size does not rule out an infinite counterexample sequence. Under hypothetical RH failure, the forced peaks could still concentrate on an arbitrarily sparse set. What changes is the shape of that escape. The exceptional branch can no longer be described merely as concentration on a zero-density collection of higher-layer transitions: if its surrounding ordinary prime gaps are sublogarithmic, it must concentrate successively on **every fixed depth tail**, using only subpolynomial boundary primes, and the admissible peak gaps themselves form a subpolynomial host set. A positive continuation must either exclude that deep-tower concentration or combine it with the clean selected mixed-race obstruction of `RE-008`--`RE-016`; ambient exceptional density alone remains insufficient.