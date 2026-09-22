# AF-505 — Convex critical contact is a temporal plateau gate

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `CRITICAL-CONTACT`, `CONVEX-GEOMETRY`, `ORDER-OF-OPERATIONS`, `MINIMAL-LIFT`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-499 separates pointwise distance attainment from tail compactness, while AF-504 shows that in saturated Hilbert geometry the nuisance noncompactness defect disappears exactly at the critical radius. Neither resource answers a third question: **does the distance profile ever reach its asymptotic critical value at a finite time?**

For convex destination geometry this remaining gate has an exact form.

Let `Q` be a normed real vector space, let `F subset Q` be nonempty and convex, fix `u in Q`, and define

\[
f(t):=\operatorname{dist}_Q(tu,F),\qquad t\ge0.
\]

Assume

\[
\lambda:=\liminf_{t\to\infty}f(t)<\infty.
\]

Then:

1. `f` is convex on `[0,infinity)`.
2. Finite asymptotic liminf forces `f` to be nonincreasing. Consequently

\[
\boxed{f(t)\downarrow\lambda=\inf_{t\ge0}f(t).}
\]

3. The exact critical sublevel has only two possibilities:

\[
\boxed{
\{t\ge0:f(t)\le\lambda\}
=arnothing
\quad\text{or}\quad
[t_*,\infty)
}
\]

for some `t_*>=0`. Equivalently, the critical value is reached once if and only if the distance profile is identically equal to `lambda` from that time onward.

Thus convexity turns the equality question into a **plateau-versus-asymptote dichotomy**. It does not force the favorable branch.

In particular, even if `F` is closed convex in a Hilbert space — so every point has a nearest point in `F` — the profile may satisfy

\[
f(t)>\lambda\quad\text{for every finite }t,
\qquad
f(t)\downarrow\lambda.
\]

Then pointwise metric projections exist everywhere, yet there is no critical-radius contact at any time. The radius-`lambda` tail is empty and its measure of noncompactness is therefore zero **vacuously**.

Applied after the AF-500 nuisance quotient, take

\[
Q=Y/V,
\qquad
F=D_V=\overline{\pi(C)},
\qquad
u=\pi(s).
\]

Whenever `D_V` is convex, the quotient-visible critical equality gate is therefore temporal rather than spatial: pointwise proximinality says what happens **if a critical sublevel time exists**, but it cannot manufacture such a time. At the exact threshold one must distinguish three resources:

\[
\boxed{
\text{temporal critical-value attainment}
\;\longrightarrow\;
\text{pointwise source/contact attainment}
\;\longrightarrow\;
\text{tail compactness for a limiting contact fiber}.
}
\]

The arrows are logical requirements, not implications supplied automatically by one another.

## Convexity of the ray-distance profile

Distance to a convex set is convex. Indeed, fix `a,b>=0`, `theta in [0,1]`, and choose approximate nearest points `y_a,y_b in F`. Since `F` is convex,

\[
\theta y_a+(1-\theta)y_b\in F.
\]

Therefore, after letting the approximation errors tend to zero,

\[
\begin{aligned}
f(\theta a+(1-\theta)b)
&\le
\left\|
\theta(au-y_a)+(1-\theta)(bu-y_b)
\right\|\\
&\le
\theta f(a)+(1-\theta)f(b).
\end{aligned}
\]

So `f` is convex.

Now suppose there were `0<=a<b` with

\[
f(a)<f(b).
\]

The secant slope

\[
m:=\frac{f(b)-f(a)}{b-a}
\]

would be positive. Monotonicity of secant slopes for a convex function then gives, for every `t>b`,

\[
\frac{f(t)-f(b)}{t-b}\ge m,
\]

hence

\[
f(t)\ge f(b)+m(t-b)\to\infty.
\]

That contradicts `liminf_(t->infinity) f(t)=lambda<infinity`. Thus `f(a)>=f(b)` whenever `a<b`: `f` is nonincreasing. Its limit exists and equals the declared liminf `lambda`.

Since a nonincreasing function converging to `lambda` satisfies `f(t)>=lambda` for every `t`, any time `t_0` with `f(t_0)<=lambda` actually has equality. Monotonicity and the lower bound then force

\[
f(t)=\lambda
\qquad(t\ge t_0).
\]

Conversely an eventual plateau clearly supplies critical sublevel times. Continuity of the distance profile makes the equality set closed, so when nonempty it is a terminal ray `[t_*,infinity)`.

This is stronger than merely saying that `lambda` is an infimum: convexity rules out recurrent crossings and oscillatory equality patterns, but still permits asymptotic approach from the wrong side forever.

## Proximinality does not settle temporal attainment

For a nonempty closed convex subset of a reflexive Banach space, every point has a best approximation. In particular, closed convex subsets of Hilbert space are proximinal.

That is a **spatial** statement. At each fixed `t`, it replaces

\[
\operatorname{dist}(tu,F)
\]

by an actual residual of that same norm. It does not assert that the scalar function `f(t)` reaches its asymptotic infimum `lambda` for some finite `t`.

Hence the AF-499 attainment gate itself has two layers when the declared radius is the asymptotic critical value:

- **pointwise attainment:** if `f(t)<=r`, does some source point realize that distance?;
- **temporal attainment:** for `r=lambda`, is there any unbounded sequence of times — or even one time in the convex case — for which `f(t)<=lambda`?

Convex Hilbert geometry automatically supplies the first layer but not the second.

This also explains why `nu_C^V(s;lambda)=0` cannot by itself certify critical contact. In the asymptotic branch `f(t)>lambda` for all finite `t`,

\[
E^V_{T,\lambda}(C,s)=\varnothing
\qquad\text{for every }T,
\]

so

\[
\nu_C^V(s;\lambda)=0
\]

for the least informative possible reason: there are no critical residuals to compactify.

## Exact convex pair with the same post-limit geometry and opposite critical contact

The temporal gate remains independent even in two-dimensional Euclidean geometry, where bounded sets are precompact and every closed convex set is proximinal.

Fix `L>0`, work in `Q=R^2` with the Euclidean norm, and let

\[
u=e_1=(1,0).
\]

Define two nonempty closed convex sets

\[
F_0
:=
\{(x,y):x\ge0,\ y\ge L\},
\]

and

\[
F_+
:=
\left\{
(x,y):x\ge0,\ y\ge L+\frac1{x+1}
\right\}.
\]

The second set is the epigraph, on `x>=0`, of the convex function `L+1/(x+1)`.

For `F_0`,

\[
\operatorname{dist}(te_1,F_0)=L
\qquad(t\ge0),
\]

so the critical value is attained at every time.

For `F_+`, every point has vertical coordinate strictly larger than `L`, hence

\[
\operatorname{dist}(te_1,F_+)>L
\qquad\text{for every finite }t.
\]

But the boundary point

\[
\left(t,L+\frac1{t+1}\right)
\]

shows

\[
L
<
\operatorname{dist}(te_1,F_+)
\le
L+\frac1{t+1}.
\]

Therefore both sets have the same asymptotic separation

\[
\boxed{\lambda=L,}
\]

while only `F_0` has critical contacts.

The standard post-limit data still agree. Their recession cones are both

\[
\operatorname{rec}(F_0)
=
\operatorname{rec}(F_+)
=
\mathbb R_+^2.
\]

Their bounded-offset translation fibers along `e_1` are also identical:

\[
\boxed{
\mathcal A_{F_0}(e_1)
=
\mathcal A_{F_+}(e_1)
=
\mathbb R\times[L,\infty).
}
\]

For `F_0` this is immediate. For `F_+`, if translated residuals converge to `(a,b)`, the epigraph inequality forces `b>=L`; conversely every `b>L` is eventually admissible at any bounded horizontal offset, while points `(a,L)` are obtained by following the boundary whose excess `1/(x+1)` tends to zero.

Equivalently, the translated sets

\[
F_0-te_1,
\qquad
F_+-te_1
\]

have the same local/Painleve-Kuratowski limit `R times [L,infinity)` as `t->infinity`. Nevertheless truncating at the closed critical ball before taking the limit distinguishes them:

\[
(F_0-te_1)\cap\overline B_L(0)=\{(0,L)\},
\]

whereas

\[
(F_+-te_1)\cap\overline B_L(0)=\varnothing.
\]

Finally, because the ambient space is finite-dimensional,

\[
\nu_{F_0}(e_1;R)
=
\nu_{F_+}(e_1;R)
=0
\qquad\text{for every finite }R.
\]

Thus the pair has the same `lambda`, the same recession cone, the same complete bounded-offset outer-limit fiber, and the same vanishing tail-noncompactness profile, while its exact critical-contact decision is opposite.

This strengthens the AF-495 boundary-side obstruction in the direction relevant after AF-499--AF-504: **convexity, pointwise nearest-point attainment, and perfect bounded-tail compactness still do not recover which side of the critical boundary the prelimit distance profile approached from.**

## Consequence for the quotient-visible phase boundary

Let the AF-500 quotient image `D_V` be nonempty and convex, and let

\[
\lambda
=
\liminf_{t\to\infty}
\operatorname{dist}_Q(t\bar s,D_V)
<\infty.
\]

Then the distance-defined exact-threshold ambiguity has a simple convex classification:

\[
\boxed{
\sup\{t\ge0:\operatorname{dist}_Q(t\bar s,D_V)\le\lambda\}
=\infty
}
\]

if and only if the quotient distance profile reaches `lambda` at one finite time, equivalently if and only if it is eventually the constant `lambda`.

If `D_V` is also proximinal along the ray, this plateau gives actual radius-`lambda` quotient contacts at every sufficiently large time. If in addition

\[
\nu_C^V(s;\lambda)=0,
\]

AF-499 then converts those recurrent contacts into a nonempty norm contact fiber.

The no-plateau branch is different: proximinality remains true pointwise and `nu_C^V(s;lambda)=0` may hold, but there are no radius-`lambda` contacts to compactify. Therefore a proof that relies on equality at the asymptotic threshold must supply a temporal critical-value-attainment theorem, retain the AF-495 critical-contact bit, or avoid exact equality by working at a controlled radius `R>lambda` in the quotient.

## Prior-art and novelty audit

No broad novelty is claimed for any convex-analysis ingredient.

- R. Tyrrell Rockafellar and Roger J. B. Wets, *Variational Analysis*, Springer (1998), DOI `10.1007/978-3-642-02431-3`, provides the standard framework for set convergence, distance functions, and variational limits underlying the distinction between prelimit contact and post-limit geometry.
- Heinz H. Bauschke and Patrick L. Combettes, *Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd ed., Springer (2017), DOI `10.1007/978-3-319-48311-5`, is standard prior art for convex sets, metric projections, best approximation, and Hilbert-space convex analysis.
- Classical best-approximation theory gives proximinality of nonempty closed convex subsets in reflexive Banach spaces; AF-499 already uses this fact to separate distance attainment from asymptotic compactness.
- AF-495 already identifies the general Painleve-Kuratowski boundary phenomenon: taking an outer limit and then intersecting a closed task region can retain boundary points approached only from outside. The present result does not claim that phenomenon as new.

The durable Arithmetic Fidelity contribution is the exact placement of these classical facts in the current quotient/compactness chain. Convexity does not erase AF-495's missing boundary-side datum; it rigidifies it into a scalar alternative: **eventual critical plateau versus asymptotic approach from above**. This exposes temporal critical-value attainment as independent of pointwise proximinality and tail compactness, and the explicit convex pair shows that the independence persists even when the usual geometric pathologies have been removed.

## Falsification and boundary audit

- The theorem assumes convexity of the **destination set actually used by the distance predicate**. Convexity of an upstream source need not survive a nonlinear compression, although a linear quotient preserves convexity.
- Finite `lambda` is essential for the monotonicity conclusion. A convex ray-distance profile may increase and diverge when its asymptotic liminf is infinite.
- Convexity forces the scalar distance profile to be nonincreasing under the finite-liminf hypothesis, but it does not force strict decrease before the plateau. Flat intervals above `lambda` are allowed.
- Pointwise proximinality and temporal attainment are distinct. The explicit `F_+` example is closed convex in `R^2`, so every fixed-time distance is attained even though the asymptotic value `lambda` is never attained in time.
- Vanishing `nu(s;lambda)` has two different meanings: a genuinely compact recurrent critical tail or an empty critical tail. The scalar noncompactness value alone does not distinguish them.
- The two-dimensional pair is deliberately synthetic. It proves logical independence of the gates; it does not establish that a natural arithmetic quotient has the asymptotic branch or the plateau branch.
- This finding does not solve source-saturation admission from AF-501. It concerns temporal admission to the exact critical radius **after** the destination quotient has been fixed.
- Nothing here identifies a rational-prime discriminator or advances RH directly. It sharpens the abstract preservation test that a later arithmetic application must pass.

## Relationship to AF-495 and AF-499--AF-504

AF-495 shows that task truncation at a closed threshold need not commute with an outer-limit compression and introduces the critical-contact bit. AF-499 separates pointwise distance attainment from tail compactness. AF-500 moves those tests into the declared nuisance quotient, and AF-504 resolves the Hilbert nuisance-fiber compactness defect exactly at the critical radius.

The remaining equality issue is therefore not another compactness problem. Under convex quotient geometry it is exactly a **temporal plateau test**. A complete exact-threshold argument must keep separate: whether the quotient source is legitimate, whether the scalar distance reaches its asymptotic threshold, whether that distance is realized by an actual source representative, and whether recurrent critical residuals are compact enough to survive as a limiting contact fiber.