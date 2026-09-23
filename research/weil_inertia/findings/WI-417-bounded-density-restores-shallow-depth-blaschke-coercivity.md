# WI-417 — Bounded source density restores quadratic shallow-depth Blaschke coercivity

**Status:** `CLASSICAL-PRIOR-ART + EXACT-DERIVED + STRUCTURAL-CONSTRAINT`.

**Parents:** [WI-415](./WI-415-count-quantum-height-depth-budget-is-t-over-delta.md), [WI-416](./WI-416-oracle-blaschke-targeting-has-zero-tv-infimum.md).

## Claim

WI-416 showed that a finite discrete defect set has zero finite-TV cost if translated Blaschke probes may be placed atomically after seeing the targets: arbitrarily small coefficients can be compensated by moving a probe exponentially close to each logarithmic singularity. One of the explicit possible repairs left there was a quantitative regularity condition on the probe measure.

A uniform two-dimensional density cap is enough to restore coercivity, and the shallow-depth exponent is forced.

For

\[
q_{a,b}(\gamma,d)
=\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

fix a target `(gamma,d)`, a required quantum `Q>0`, and a density cap `B>0`. Let `nu` range over finite signed or complex measures on `(0,\infty)\times\mathbb R` that are absolutely continuous with respect to `da db` and satisfy

\[
\frac{d|\nu|}{da\,db}\le B
\quad\text{a.e.}
\tag{2}
\]

Define the one-target cost

\[
\mathcal M_B(d,Q)
=
\inf\left\{
\|\nu\|_{\rm TV}:
|Q_\nu(\gamma,d)|\ge Q
\right\},
\tag{3}
\]

where

\[
Q_\nu(\gamma,d)=\int q_{a,b}(\gamma,d)\,d\nu(a,b).
\tag{4}
\]

Then

\[
\boxed{
\frac{Q^2}{16\pi B d^2}
\le
\mathcal M_B(d,Q)
\le
4Q+\frac{Q^2}{B d^2}.
}
\tag{5}
\]

In particular, for fixed `B,Q`,

\[
\boxed{
\mathcal M_B(d,Q)=\Theta_{B,Q}(d^{-2})
\qquad(d\downarrow0).
}
\tag{6}
\]

Thus the zero-TV oracle concentration of WI-416 is genuinely a singular-measure phenomenon. A uniform `L^infty` cap on source density does not merely make the cost positive: a fixed count quantum at shallow horizontal depth requires TV of quadratic order `1/d^2`.

The lower bound is valid even for signed/complex measures because it uses total variation. The upper bound is realized by an explicit positive absolutely continuous measure. No zero is excluded and no statement of RH follows: the missing zeta-specific step is to derive an appropriate source-side regularity bound rather than assume (2).

## 1. A sharp radial majorant for one Blaschke charge

Put

\[
r^2=(a-d)^2+(b-\gamma)^2.
\tag{7}
\]

Since

\[
q_{a,b}(\gamma,d)
=\frac12\log\left(1+\frac{4ad}{r^2}\right)
\tag{8}
\]

and

\[
a\le d+|a-d|\le d+r,
\tag{9}
\]

we have

\[
4ad\le4d(d+r).
\tag{10}
\]

Therefore

\[
\begin{aligned}
q_{a,b}(\gamma,d)
&\le
\frac12\log\left(1+\frac{4d(d+r)}{r^2}\right)\\
&=
\frac12\log\left(1+\frac{2d}{r}\right)^2\\
&=
\boxed{\log\left(1+\frac{2d}{r}\right)}.
\end{aligned}
\tag{11}
\]

The majorant is pointwise sharp along the outward horizontal ray `b=gamma`, `a=d+r`. Its logarithmic singularity is locally integrable in two dimensions, so an `L^infty` density cap removes the atomic blow-up exploited by WI-416.

## 2. Exact bathtub envelope for the radial majorant

Let

\[
f(a,b)=\frac{d|\nu|}{da\,db},
\qquad
0\le f\le B,
\qquad
\int f=M:=\|\nu\|_{\rm TV}.
\tag{12}
\]

Extend `f` by zero from the half-plane `a>0` to all of `R^2`. With

\[
K_d(r)=\log\left(1+\frac{2d}{r}\right),
\tag{13}
\]

(11) gives

\[
|Q_\nu(\gamma,d)|
\le\int_{\mathbb R^2}K_d(|z|)f(z)\,dz.
\tag{14}
\]

Because `K_d` is radial and strictly decreasing, the elementary bathtub/layer-cake principle says that among all `0<=f<=B` of mass `M`, the right side is maximized by density `B` on a centered disk of area `M/B`. Indeed, for every `t>0`,

\[
\int_{\{K_d>t\}}f
\le
\min\{M,\,B|\{K_d>t\}|\},
\tag{15}
\]

and the saturated centered disk attains the right side simultaneously for every superlevel set. Thus, with

\[
R=\sqrt{\frac{M}{\pi B}},
\tag{16}
\]

we obtain

\[
|Q_\nu(\gamma,d)|
\le
2\pi B\int_0^R
r\log\left(1+\frac{2d}{r}\right)\,dr.
\tag{17}
\]

The integral is elementary:

\[
\begin{aligned}
|Q_\nu(\gamma,d)|
\le \pi B\Bigg[
&4d^2\log\frac{2d}{2d+R}
+2dR\\
&+R^2\log\left(1+\frac{2d}{R}\right)
\Bigg].
\end{aligned}
\tag{18}
\]

Set

\[
x=\frac{R}{2d}
=\sqrt{\frac{M}{4\pi B d^2}}
\tag{19}
\]

and

\[
F(x)
=x-\log(1+x)+x^2\log(1+1/x).
\tag{20}
\]

Then the stronger implicit response bound is

\[
\boxed{
|Q_\nu(\gamma,d)|
\le
4\pi B d^2 F\!\left(
\sqrt{\frac{M}{4\pi B d^2}}
\right).
}
\tag{21}
\]

The envelope on the right is strictly increasing in `M`: direct differentiation gives

\[
F'(x)=2x\log(1+1/x)>0.
\tag{22}
\]

This is an exact extremal formula for the **radial majorant problem** (14). It is not claimed to be the exact capacity of the original half-plane Blaschke kernel, because passing from (8) to (11) and then enlarging the source domain to the whole plane can lose constants.

## 3. Universal quadratic lower bound

The exact envelope immediately yields a simple closed form. Since

\[
\log(1+1/x)\le\frac1x
\tag{23}
\]

and `-log(1+x)<=0`,

\[
F(x)\le2x.
\tag{24}
\]

Combining (21), (24), and (19),

\[
|Q_\nu(\gamma,d)|
\le
4d\sqrt{\pi B M}.
\tag{25}
\]

Hence a response of magnitude at least `Q` forces

\[
\boxed{
M\ge\frac{Q^2}{16\pi B d^2}.
}
\tag{26}
\]

This is the left side of (5). It also gives the useful variable-cap criterion

\[
B(d)d^2\longrightarrow0
\quad\Longrightarrow\quad
\mathcal M_{B(d)}(d,Q)\longrightarrow\infty
\tag{27}
\]

for every fixed `Q>0`. Conversely, a density cap allowed to grow at the critical rate `B(d)asymp d^{-2}` need not produce any divergent TV obstruction. The source-side regularity scale therefore matters, not merely absolute continuity.

## 4. The `d^{-2}` exponent is sharp

The lower-bound exponent is not an artefact of the full-plane rearrangement. There is an explicit admissible positive source of the same order.

For `R>2d`, put density `B` on

\[
\Omega_R
=
\{(a,b):2d\le a\le R,\ |b-\gamma|\le a\}
\tag{28}
\]

and zero elsewhere. On this region,

\[
(b-\gamma)^2+(a-d)^2\le2a^2,
\tag{29}
\]

so

\[
q_{a,b}(\gamma,d)
\ge
\frac12\log\left(1+\frac{2d}{a}\right).
\tag{30}
\]

Because `2d/a<=1` and `log(1+t)>=t/2` for `0<=t<=1`,

\[
q_{a,b}(\gamma,d)\ge\frac{d}{2a}.
\tag{31}
\]

Integrating across the width `2a` in `b`,

\[
Q_\nu(\gamma,d)
\ge
Bd(R-2d).
\tag{32}
\]

Choose

\[
R=2d+\frac{Q}{Bd}.
\tag{33}
\]

Then the target response is at least `Q`, while the total variation is

\[
\begin{aligned}
M
&=B\int_{2d}^R2a\,da\\
&=B(R^2-4d^2)\\
&=\boxed{4Q+\frac{Q^2}{Bd^2}}.
\end{aligned}
\tag{34}
\]

This proves the upper side of (5), hence the order-sharp statement (6).

## 5. Stress tests and what this does not buy

The theorem closes one specific escape left open by WI-416, but it must not be overread.

First, the lower bound is **one-target coercivity**. A single source distribution may contribute to many exceptional zeros, so (26) cannot be summed over zeros without an additional packing, separation, transport, or near-orthogonality argument. In particular this finding does not convert a zero count into a `d^{-2}` multiple-target budget.

Second, the hypothesis is genuinely two-dimensional. Atomic measures, measures supported on curves, or source families whose density cap grows too quickly as `d` decreases are outside (2). WI-416 remains the correct obstruction for unconstrained target-adaptive atoms.

Third, no zeta-specific source theorem currently supplies (2) at the required scale. The point of the result is to quantify exactly what this candidate regularization would have to achieve: if prime/source-side structure can be represented by an absolutely continuous translated-Blaschke measure with `B(d)d^2=o(1)`, then shallow discrete defects can no longer be hidden at arbitrarily small source TV. If the natural source representation is singular or has `B(d)gtrsim d^{-2}`, this branch does not bootstrap.

Finally, the full-plane radial rearrangement in Section 2 is deliberately one-sided. It is used only for a rigorous universal upper bound on response. No equality statement for the original half-plane kernel is needed for (5), and the explicit construction in Section 4 independently proves that the quadratic depth exponent cannot be improved under the density-cap hypothesis alone.

## 6. Prior-art and novelty audit

The analytic mechanisms are classical. Symmetric decreasing rearrangement and bathtub principles go back to the Hardy--Littlewood/Riesz tradition; a standard multi-function reference is H. J. Brascamp, E. H. Lieb, and J. M. Luttinger, *A general rearrangement inequality for multiple integrals*, Journal of Functional Analysis **17** (1974), 227--237, DOI `10.1016/0022-1236(74)90013-5`.

The scale in (25) is also the familiar endpoint interpolation behavior of a two-dimensional order-one Riesz-type potential: `L^1` mass and `L^infty` density combine as the square root. Lars Inge Hedberg, *On Certain Convolution Inequalities*, Proceedings of the American Mathematical Society **36** (1972), 505--510, DOI `10.1090/S0002-9939-1972-0312232-4`, is a classical source for this convolution/potential viewpoint.

The zeta/Blaschke setting and the relevant half-plane factorization are already anchored in WI-409--WI-416, including Kunik and the Balazard--Saias--Yor lineage. A targeted search found no basis for a priority claim for the potential estimate itself, and none is made. The line-specific contribution recorded here is the exact quantitative answer to the regularity escape isolated by WI-416: **a uniform two-dimensional source-density cap converts the discrete oracle cost from zero to an order-sharp `1/(B d^2)` TV tariff**.

## Consequence

WI-415 and WI-416 left a sharp dichotomy between continuum coverage, which costs `T/d`, and unrestricted discrete oracle targeting, which costs zero. The present result inserts a third regime:

\[
\boxed{
\text{discrete target}
+\text{uniform 2D source-density cap }B
\Longrightarrow
\mathcal M_B(d,Q)\asymp\frac{Q^2}{Bd^2}
\text{ as }d\downarrow0.
}
\tag{35}
\]

This is a genuine structural constraint on the exceptional-mass detector class, but not yet a zeta theorem. The next useful question is no longer whether *some* regularity can defeat the WI-416 oracle construction; this theorem shows that bounded density does. The live gate is whether arithmetic/source-side structure supplies a comparable non-oracular regularity estimate, or whether the natural probe representation is necessarily too singular for this coercivity to apply.