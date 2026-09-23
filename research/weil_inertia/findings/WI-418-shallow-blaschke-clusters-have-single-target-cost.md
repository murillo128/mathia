# WI-418 — Shallow bounded-density Blaschke clusters have asymptotically single-target cost

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parents:** [WI-415](./WI-415-count-quantum-height-depth-budget-is-t-over-delta.md), [WI-416](./WI-416-oracle-blaschke-targeting-has-zero-tv-infimum.md), [WI-417](./WI-417-bounded-density-restores-shallow-depth-blaschke-coercivity.md).

## Claim

WI-417 computed the exact one-target capacity under a two-dimensional source-density cap, but left open whether several exceptional zeros force approximately additive source cost. They do not at height separations below the reciprocal defect-depth scale. In fact an arbitrarily large target cluster, even a continuum interval, can asymptotically reuse the full one-target budget.

For

\[
q_{a,b}(\gamma,d)
=\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

fix `B,Q>0`, one depth `d>0`, a center `gamma_0`, and a nonempty target set

\[
E\subset [\gamma_0-L,\gamma_0+L]\times\{d\}.
\tag{2}
\]

Let `M_B(E,Q)` be the infimum of `||nu||_TV` over finite signed or complex measures absolutely continuous with respect to `da db`, with

\[
\frac{d|\nu|}{da\,db}\le B
\quad\text{a.e.},
\tag{3}
\]

and satisfying `|Q_nu(gamma,d)|>=Q` at every target in `E`.

Put

\[
R_0=\frac{Q}{2\pi B d}
\tag{4}
\]

and assume `R_0>=d`, equivalently `Q>=2 pi B d^2`. Define

\[
\alpha
=
\frac{4d}{R_0}
+
\left(\frac{L}{R_0}\right)^2.
\tag{5}
\]

Then

\[
\boxed{
\frac{Q^2}{4\pi B d^2}
\le
\mathcal M_B(E,Q)
\le
\frac{Q^2}{4\pi B d^2}(1+\alpha)^2.
}
\tag{6}
\]

Consequently, for fixed `B,Q`, if `d->0` and the target half-width obeys

\[
L(d)d\to0,
\tag{7}
\]

then

\[
\boxed{
\mathcal M_B(E_d,Q)
\sim
\frac{Q^2}{4\pi B d^2},
}
\tag{8}
\]

uniformly over **every nonempty target set** `E_d` contained in such a cluster, independently of its cardinality. This equals the sharp one-target asymptotic from WI-417.

Thus a bounded source density does not by itself make per-defect costs additive. The natural vertical reuse length of a shallow translated-Blaschke detector is at least order `1/d`: on every `o(1/d)` height cluster, all targets can be paid for at asymptotically the price of one.

In particular, if `d_T=o(1/T)`, every same-depth target set inside a full dyadic ordinate interval `[T,2T]` has asymptotically the one-target cost, no matter how many targets it contains. Zero counts or ordinary ordinate spacing therefore cannot convert WI-417's `d^{-2}` one-target law into an additive `N d^{-2}` law in this ultra-shallow regime.

This is a barrier for the bounded-density translated-Blaschke branch, not a statement that actual zeta source measures have bounded density, not an existence claim for such zero configurations, and not an RH conclusion.

## 1. A tangent source disk and its exact logarithmic potential

For `R>0`, let

\[
D_R(\gamma_0)
=
\left\{(a,b):
(a-R)^2+(b-\gamma_0)^2<R^2
\right\}.
\tag{9}
\]

This open disk is tangent to the boundary `a=0` and otherwise lies entirely in the allowed source half-plane `a>0`. Consider the positive admissible source

\[
d\nu_R(a,b)=B\,\mathbf 1_{D_R(\gamma_0)}(a,b)\,da\,db,
\qquad
\|\nu_R\|_{\rm TV}=\pi B R^2.
\tag{10}
\]

Write `y=gamma-gamma_0` and identify `z=a+i(b-gamma_0)`. Then

\[
q_{a,b}(\gamma,d)
=
\log|z-(-d+iy)|-
\log|z-(d+iy)|.
\tag{11}
\]

The only potential-theory input needed below is the elementary logarithmic potential of a uniform disk. If

\[
F_R(w)=\int_{|z-R|<R}\log|z-w|\,dA(z),
\tag{12}
\]

then

\[
F_R(w)=
\begin{cases}
\pi R^2\log|w-R|,
& |w-R|\ge R,\\[1mm]
\pi R^2\log R
+\dfrac\pi2\bigl(|w-R|^2-R^2\bigr),
& |w-R|\le R.
\end{cases}
\tag{13}
\]

The outside formula is just the mean-value property because `log|z-w|` is harmonic on the disk. The inside formula follows from `Delta_w log|z-w|=2 pi delta_z`: radiality gives a quadratic solution inside, and matching at `|w-R|=R` fixes the constant. Hence (13) is an exact identity rather than a Poisson-kernel approximation.

Set

\[
u=\frac dR,
\qquad
v=\frac{|y|}{R},
\qquad
J_R(y,d)=\int_{D_R(\gamma_0)}q_{a,b}(\gamma,d)\,da\,db.
\tag{14}
\]

The point `-d+iy` is always outside the disk. The point `d+iy` is inside exactly when

\[
(1-u)^2+v^2<1.
\tag{15}
\]

Substitution into (13) gives the exact two-branch response

\[
J_R(y,d)=
\begin{cases}
\dfrac{\pi R^2}{2}
\left[
\log\bigl((1+u)^2+v^2\bigr)
+2u-u^2-v^2
\right],
& (1-u)^2+v^2<1,\\[3mm]
\dfrac{\pi R^2}{2}
\log\dfrac{(1+u)^2+v^2}
          {(1-u)^2+v^2},
& (1-u)^2+v^2\ge1.
\end{cases}
\tag{16}
\]

The two formulas agree on the boundary.

## 2. A uniform lower bound across a whole height cluster

Assume `0<u<=1`, i.e. `d<=R`. In the outside branch write

\[
A=1+u^2+v^2.
\]

Then

\[
\log\frac{A+2u}{A-2u}
=2\operatorname{artanh}\frac{2u}{A}
\ge\frac{4u}{A},
\]

and therefore

\[
J_R(y,d)
\ge
\frac{2\pi R d}{1+u^2+v^2}
\ge
\frac{2\pi R d}{1+4u+v^2}.
\tag{17}
\]

In the inside branch, differentiating (16) with respect to `v^2` gives

\[
\frac{\partial J_R}{\partial(v^2)}
=
\frac{\pi R^2}{2}
\left(
\frac{1}{(1+u)^2+v^2}-1
\right)<0.
\tag{18}
\]

So the smallest inside value occurs at the boundary `v^2=2u-u^2`. There

\[
J_R
=\frac{\pi R^2}{2}\log(1+4u)
\ge
\frac{2\pi R d}{1+4u},
\tag{19}
\]

using `log(1+x)>=x/(1+x)`. Combining (17)--(19) yields the single exact bound

\[
\boxed{
J_R(y,d)
\ge
\frac{2\pi R d}
{1+4d/R+(y/R)^2}
\qquad(0<d\le R).
}
\tag{20}
\]

This is the load-bearing reuse estimate. A tangent source disk of radius `R` has mass of order `R^2`, but its response stays of order `Rd` throughout vertical offsets `|y|=o(R)`.

## 3. Exact quantitative cluster upper bound

Take `R_0` from (4), `alpha` from (5), and choose

\[
R=R_0(1+\alpha).
\tag{21}
\]

Because `R>=R_0>=d`, (20) applies. For every target with `|y|<=L`,

\[
\frac{4d}{R}+\left(\frac yR\right)^2
\le
\frac{4d}{R_0}+\left(\frac L{R_0}\right)^2
=\alpha.
\tag{22}
\]

Since `2 pi B R_0 d=Q`, equations (20)--(22) give

\[
Q_{\nu_R}(\gamma,d)
=BJ_R(y,d)
\ge
\frac{2\pi B R d}{1+\alpha}
=Q.
\tag{23}
\]

Thus the single positive source (10) simultaneously covers every target in the interval, and

\[
\mathcal M_B(E,Q)
\le
\pi B R^2
=
\frac{Q^2}{4\pi B d^2}(1+\alpha)^2.
\tag{24}
\]

For the lower bound in (6), choose any one target from the nonempty set `E`. Every source feasible for the whole cluster is feasible for that target. WI-417 gives the exact one-target capacity and, in particular,

\[
\mathcal M_B(E,Q)
\ge
\mathcal M_B(d,Q)
\ge
\frac{Q^2}{4\pi B d^2}.
\tag{25}
\]

This proves (6).

For fixed `B,Q`,

\[
\alpha
=
\frac{8\pi B}{Q}d^2
+
\left(\frac{2\pi B}{Q}Ld\right)^2.
\tag{26}
\]

Hence `d->0` and `Ld->0` imply `alpha->0`, and (8) follows by squeezing. Notice that no finiteness, separation, or counting hypothesis on `E` enters the upper construction.

## 4. The actual multi-target crossover scale

WI-417's exact superlevel-disk extremizer already hints at the same geometry. In the shallow regime its mass is asymptotic to `Q^2/(4 pi B d^2)`, so its area radius is of order `1/d`; its center in the scale variable `a` is also of order `1/d`. The tangent disk above makes the corresponding vertical reuse explicit and avoids having to solve the exact one-target implicit equation.

This creates two different asymptotic regimes. If a target interval has half-width `L=o(1/d)`, (8) says that the one-target `d^{-2}` cost dominates and is asymptotically sufficient for the entire cluster. By contrast, WI-415's vertical-area law forces a cost proportional to interval length divided by depth once the covered height range becomes macroscopically larger. The crossover between the one-target and continuum mechanisms therefore occurs at the reciprocal-depth scale `L asy 1/d`, up to constants depending on `B,Q`.

The consequence for zero-count bootstraps is negative but precise. A theorem that tries to sum WI-417's one-zero capacities using only an `L^infinity(da db)` density cap plus ordinary separation of zero ordinates cannot be uniform in the defect depth: when `d` is small enough that the whole relevant ordinate cluster has width `o(1/d)`, all those putative costs can be reused by one admissible source cloud.

For a dyadic zeta window `[T,2T]`, take `gamma_0=3T/2` and `L=T/2`. If `d_T=o(1/T)`, then `L d_T->0`, so (8) applies to **every** same-depth subset of that dyadic window. Even a hypothetical set with as many points as allowed by Riemann--von Mangoldt counting has no larger leading bounded-density capacity than one target. This does not assert that zeta has such a configuration; it is an admissible stress test that any source-regularity-only coercivity theorem would have to exclude by additional arithmetic information.

## 5. Prior-art and novelty audit

The potential-theory ingredients are classical. Thomas Ransford, *Potential Theory in the Complex Plane* (Cambridge University Press, 1995), treats logarithmic potentials and the planar Laplacian framework already cited in WI-416. The disk identity behind (13) is also the elementary disk quadrature/mean-value phenomenon; for modern quadrature-domain context see Bjorn Gustafsson, *Quadrature for quadrics*, European Journal of Mathematics **9** (2023), article 110, DOI `10.1007/s40879-023-00707-z`, whose review explicitly records the disk mean-value quadrature identity. No new potential-theory theorem is claimed here.

A targeted prior-art search around logarithmic potentials of uniform disks, quadrature domains, Poisson-kernel translates, bounded source densities, Blaschke/Green kernels, and multi-target capacity found the classical disk/quadrature mechanism and the neighboring interpolation/Carleson literature, but did not locate this exact reciprocal-depth cluster-reuse statement. That negative search is not evidence of priority, and no priority claim is made. The line-specific contribution is the exact specialization (20)--(26) showing that the open **budget-reuse** problem after WI-417 has a decisive obstruction below the `1/d` vertical scale.

The result is stronger than merely observing overlap of the one-target extremizer. It gives one explicit admissible source, an exact response formula, and a quantitative squeeze proving that arbitrary target cardinality disappears from the leading capacity whenever `Ld->0`.

## 6. Boundaries and falsification tests

The common-depth hypothesis is deliberate. It is enough to disprove any universal additive-cost principle based only on target count, ordinate separation, and the density cap. A theorem using genuinely varying depths may still recover extra coercivity, but it must use that variation rather than silently summing one-target costs.

The density cap is still an assumption, not zeta-side evidence. WI-417 already isolates the missing arithmetic step of deriving such a cap from the source representation. The present result shows that even after granting the cap, a second missing ingredient remains: **locality or anti-reuse structure on the reciprocal-depth height scale**. Examples that lie outside the theorem include a source-scale cutoff, a transport/bandwidth constraint in `b`, a source budget with independently controlled localization, nonlinear observables, or an arithmetic invariant that prevents one source cloud from contributing coherently to many defects.

The decisive audit test is formula (20): any challenge to the reuse conclusion must identify an error in the uniform-disk potential (13), the branch calculation (16), or the elementary lower bounds (17)--(19). If those identities stand, the asymptotic squeeze (6)--(8) is deterministic and does not depend on a numerical experiment or a conjectural zeta input.

## Consequence

WI-417 solved the one-target bounded-density problem but left multi-defect reuse as the next possible source of coercivity. WI-418 shows that this route has an intrinsic resolution limit:

\[
\boxed{
Ld\to0
\quad\Longrightarrow\quad
\text{arbitrarily many same-depth targets cost asymptotically one target.}
}
\]

Therefore a bounded two-dimensional source density, even if it can eventually be derived from arithmetic data, is not enough by itself to turn zero counts into an additive defect budget at arbitrarily shallow depths. A viable defect-to-zero bootstrap along the translated-Blaschke branch must additionally control reuse/localization on scales of order `1/d`, obtain a per-target contradiction without summing capacities, or leave this linear detector architecture.