# AF-196 — Nonuniform cubic stencils beat equispaced parity at fixed Wasserstein scale

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `SOURCE-CLASS-OPTIMIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-195 classifies the unique signed control on `m+1` fixed nodes that annihilates all polynomials of degree below `m`, and shows that the AF-182 parity-split binomial control is forced when those nodes are equispaced. It leaves open whether **moving the nodes while keeping the same minimal support, moment-cancellation order, positivity model, and source separation can make the Euler observation even flatter**.

For the first nontrivial free-node case, `m=3`, the answer is yes. Moreover the leading low-band optimization can be solved exactly.

Let

\[
u_0<u_1<u_2<u_3,
\qquad
u_1-
u_0=a,
\quad
u_2-
u_1=b,
\quad
u_3-
u_2=c,
\tag{1}
\]

with `a,b,c>0`. Let

\[
\lambda_j
=\frac{1}{\prod_{\ell\ne j}(u_j-u_\ell)}
\tag{2}
\]

be the cubic divided-difference weights. Their signs are `(-,+,-,+)`. Normalize the positive and negative parts as in AF-195 to obtain mutually singular probability measures `\mu_+` and `\mu_-`, and put

\[
\nu=\mu_+-\mu_-.
\tag{3}
\]

Then `\nu` annihilates every polynomial of degree at most two and

\[
\int u^3\,d\nu(u)=\frac1A,
\qquad
A=\lambda_1+\lambda_3
=\frac{a+c}{abc(a+b+c)}.
\tag{4}
\]

Its exact one-dimensional Wasserstein separation is

\[
\boxed{
W_1(\mu_+,\mu_-)
=\frac{2abc(a+2b+c)}{(a+b)(a+c)(b+c)}.
}
\tag{5}
\]

Hence the scale-free leading cubic response at fixed source separation is

\[
Q(a,b,c)
:=
\frac{\int u^3\,d\nu(u)}{W_1(\mu_+,\mu_-)^3}
=
\frac{(a+b)^3(a+c)^2(b+c)^3(a+b+c)}
{8a^2b^2c^2(a+2b+c)^3}.
\tag{6}
\]

Among **all** positive triples `(a,b,c)`, `Q` has a unique minimizer up to common scale and reflection. The minimizing stencil is symmetric but not equispaced:

\[
\boxed{
a=c=h,
\qquad
b=t_*h,
\qquad
t_* = \frac{\sqrt{33}-1}{4}
\approx1.1861406616.
}
\tag{7}
\]

At this shape,

\[
\boxed{
Q_*
=\frac{189+33\sqrt{33}}{256}
\approx1.4787912787.
}
\tag{8}
\]

The equispaced stencil has `a=b=c`, hence

\[
Q_{\rm eq}=\frac32.
\tag{9}
\]

Therefore

\[
\boxed{Q_*<Q_{\rm eq}.}
\tag{10}
\]

The improvement is small but exact: the optimal free-node cubic control reduces the leading normalized third-moment response by about `1.41%` relative to the equispaced parity control.

This difference persists for the actual Euler logarithm on every fixed finite vertical band in the small-source-scale limit. Fix

\[
x>0,
\qquad
\sigma>0,
\qquad
T<\infty,
\tag{11}
\]

and

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+i\tau.
\tag{12}
\]

For a fixed stencil shape, translate the leftmost node to `x` and rescale it so that

\[
W_1(\mu_+,\mu_-)=\delta.
\tag{13}
\]

Define the finite-band discrepancy exactly as in AF-182,

\[
D_T(\mu_+,\mu_-)
=
\sup_{|\tau|\le T}
\left|
\int F_{\sigma+i\tau}(u)\,d(\mu_+-\mu_-)(u)
\right|.
\tag{14}
\]

Then, uniformly on the fixed band,

\[
\boxed{
D_T(\mu_+,\mu_-)
=
\frac{Q(a,b,c)}6
M_3(x,\sigma,T)\,\delta^3
+O_{a:b:c,x,\sigma,T}(\delta^4),
}
\tag{15}
\]

where

\[
M_3(x,\sigma,T)
=
\sup_{|\tau|\le T}
\left|F_{\sigma+i\tau}^{(3)}(x)\right|
>0.
\tag{16}
\]

Consequently, for all sufficiently small `\delta`, the nonuniform optimal shape `(7)` has strictly smaller full fixed-band Euler discrepancy than the equispaced four-node parity control at the **same exact Wasserstein separation**.

Thus AF-195's equispaced uniqueness does not extend to a free-node minimax principle even at the first cubic level. Equispacing spends a real amount of fidelity budget. The source geometry itself is part of the inverse problem.

## Derivation

### 1. The normalized cubic control and its exact Wasserstein distance

For the gaps `(a,b,c)`, the barycentric weights are

\[
\lambda_0
=-\frac1{a(a+b)(a+b+c)},
\tag{17}
\]

\[
\lambda_1
=\frac1{ab(b+c)},
\tag{18}
\]

\[
\lambda_2
=-\frac1{bc(a+b)},
\tag{19}
\]

\[
\lambda_3
=\frac1{c(b+c)(a+b+c)}.
\tag{20}
\]

Their positive mass is

\[
A=\lambda_1+\lambda_3
=\frac{a+c}{abc(a+b+c)}.
\tag{21}
\]

AF-195 gives

\[
\sum_{j=0}^3\lambda_jP(u_j)=0
\qquad(\deg P<3),
\tag{22}
\]

and

\[
\sum_{j=0}^3\lambda_j u_j^3=1.
\tag{23}
\]

After division by `A`, equations `(4)` and the quadratic moment matching follow immediately.

For probability measures on the line,

\[
W_1(\mu_+,\mu_-)
=\int_{\mathbb R}|G_+(u)-G_-(u)|\,du.
\tag{24}
\]

The cumulative signed masses on the three consecutive intervals are respectively

\[
\frac{\lambda_0}{A},
\qquad
\frac{\lambda_0+\lambda_1}{A},
\qquad
-\frac{\lambda_3}{A}.
\tag{25}
\]

Here

\[
\lambda_0+\lambda_1
=
\frac{a+2b+c}{b(a+b)(b+c)(a+b+c)}>0.
\tag{26}
\]

Therefore

\[
W_1
=\frac{-a\lambda_0+b(\lambda_0+\lambda_1)+c\lambda_3}{A},
\tag{27}
\]

which simplifies exactly to `(5)`. Combining `(4)` and `(5)` gives `(6)`.

### 2. Global optimization over arbitrary four-node shapes

The objective `(6)` is invariant under common rescaling of `(a,b,c)`. Introduce

\[
s=a+c,
\qquad
y=\frac bs,
\qquad
z=\frac{ac}{s^2}.
\tag{28}
\]

Since `a,c>0`,

\[
0<z\le\frac14,
\tag{29}
\]

with equality exactly when `a=c`. In these variables,

\[
\boxed{
Q(y,z)
=
\frac{(1+y)(y^2+y+z)^3}
{8y^2z^2(1+2y)^3}.
}
\tag{30}
\]

For fixed `y`, only

\[
\frac{(K+z)^3}{z^2},
\qquad K=y(1+y),
\tag{31}
\]

depends on `z`, and

\[
\frac{d}{dz}
\log\frac{(K+z)^3}{z^2}
=
\frac{z-2K}{z(K+z)}.
\tag{32}
\]

Thus the minimizing `z` is

\[
z_y=\min\left\{2y(1+y),\frac14\right\}.
\tag{33}
\]

Let

\[
y_0=\frac{\sqrt6-2}{4},
\tag{34}
\]

so that `2y_0(1+y_0)=1/4`.

For `0<y\le y_0`, substitution of `z=2y(1+y)` gives

\[
Q_<(y)
=\frac{27(1+y)^2}{32y(1+2y)^3}.
\tag{35}
\]

Its logarithmic derivative is

\[
\frac{d}{dy}\log Q_<(y)
=-\frac{4y^2+7y+1}{y(1+y)(1+2y)}<0.
\tag{36}
\]

Hence this entire asymmetric branch decreases up to the boundary `y_0`.

For `y\ge y_0`, the optimum has `z=1/4`, so `a=c`. Write

\[
t=\frac ba=2y.
\tag{37}
\]

Then `(30)` becomes

\[
\boxed{
Q_{\rm sym}(t)
=\frac{(t+1)^3(t+2)}{16t^2}.
}
\tag{38}
\]

Its logarithmic derivative is

\[
\frac{d}{dt}\log Q_{\rm sym}(t)
=
\frac{2t^2+t-4}{t(t+1)(t+2)}.
\tag{39}
\]

The unique positive critical point is

\[
t_*=\frac{\sqrt{33}-1}{4},
\tag{40}
\]

and `(39)` changes from negative to positive there. Since `t_*>2y_0`, the symmetric branch continues decreasing beyond the point where it overtakes the asymmetric branch, and then increases after `t_*`. The boundary limits of `(30)` diverge. Therefore `(40)` is the unique global shape minimizer, proving `(7)`.

Substitution into `(38)` gives

\[
Q_*
=\frac{189+33\sqrt{33}}{256},
\tag{41}
\]

while `t=1` gives `Q_{\rm eq}=3/2`, proving `(8)`--`(10)`.

### 3. Explicit optimal probability pair

For the symmetric shape

\[
a=c=h,
\qquad b=th,
\tag{42}
\]

normalization gives the signed weights

\[
\mu_+-\mu_-
=
-\alpha\,\delta_x
+\beta\,\delta_{x+h}
-\beta\,\delta_{x+(t+1)h}
+\alpha\,\delta_{x+(t+2)h},
\tag{43}
\]

where

\[
\alpha=\frac{t}{2(t+1)},
\qquad
\beta=\frac{t+2}{2(t+1)},
\qquad
\alpha+\beta=1.
\tag{44}
\]

Thus each side is an ordinary positive two-atom probability measure. Its Wasserstein distance is

\[
W_1
=\frac{2th}{t+1}.
\tag{45}
\]

To impose `W_1=\delta`, take

\[
h=\delta\frac{t+1}{2t}.
\tag{46}
\]

The first three signed moments around `x` are then

\[
\int (u-x)^r\,d(\mu_+-\mu_-)(u)=0,
\qquad r=0,1,2,
\tag{47}
\]

and

\[
\boxed{
\int (u-x)^3\,d(\mu_+-\mu_-)(u)
=Q_{\rm sym}(t)\,\delta^3.
}
\tag{48}
\]

At `t=1`, `(43)` is the AF-182/AF-195 cubic parity pair with weights `(-1,3,-3,1)/4`. At `t=t_*`, it is the globally optimal minimal-support cubic moment-flat shape for the declared `W_1` resource.

### 4. Uniform fixed-band Euler asymptotic

For fixed `x>0`, `\sigma>0`, `T<\infty`, and a fixed shape, every node lies in

\[
[x,x+C\delta]
\tag{49}
\]

for a shape-dependent constant `C`. Taylor expansion at `x` gives

\[
F_s(u)
=F_s(x)+F_s'(x)(u-x)
+\frac12F_s''(x)(u-x)^2
+\frac16F_s'''(x)(u-x)^3
+R_4(s,u),
\tag{50}
\]

with

\[
|R_4(s,u)|
\le
C'\delta^4
\sup_{v\in[x,x+C\delta]}
|F_s^{(4)}(v)|.
\tag{51}
\]

The derivative series

\[
F_s^{(r)}(v)
=(-1)^r s^r
\sum_{k\ge1}k^{r-1}e^{-ksv}
\tag{52}
\]

converges absolutely and uniformly for `|\operatorname{Im}s|\le T` and `v\ge x`. Hence the fourth derivative is uniformly bounded on the declared fixed band.

Integrating `(50)` against `\nu` kills the first three polynomial terms except the cubic term. Since `\|\nu\|_{TV}=2`, equations `(47)`--`(52)` give uniformly in `|\tau|\le T`,

\[
\int F_{\sigma+i\tau}(u)\,d\nu(u)
=
\frac{Q(a,b,c)}6
F_{\sigma+i\tau}^{(3)}(x)\,\delta^3
+O(\delta^4).
\tag{53}
\]

Taking the supremum over the band yields `(15)`. Finally,

\[
F_\sigma^{(3)}(x)
=-\sigma^3\sum_{k\ge1}k^2e^{-k\sigma x}\ne0,
\tag{54}
\]

so `M_3(x,\sigma,T)>0`. The strict gap `Q_*<Q_{\rm eq}` therefore dominates the uniform `O(\delta^4)` remainder for all sufficiently small `\delta`.

## Source-class consequence for Arithmetic Fidelity

AF-195 removed coefficient freedom on a fixed minimal stencil. AF-196 shows that **node geometry remains a genuine fidelity variable even after support cardinality, positivity, exact moment cancellation, and Wasserstein separation are all fixed**.

For the four-node quadratic-matching class:

- equispacing is not extremal for hiding the next-order response;
- the exact globally optimal leading shape is a slightly stretched middle gap;
- the same shape asymptotically lowers the actual Euler-log discrepancy on every fixed finite vertical band;
- therefore a converse based only on cancellation order and `W_1` cannot regard the equispaced parity cluster as the worst source geometry.

The improvement is deliberately modest. Its significance is structural rather than numerical: the AF-182 parity family is a sharp and canonical *fixed-grid* witness, but not a universal free-node extremizer.

The next source-class question is now more precise. For general order `m`, characterize or bound

\[
\inf
\frac{\left|\int u^m\,d(\mu_+-\mu_-)(u)\right|}
{W_1(\mu_+,\mu_-)^m}
\tag{55}
\]

over mutually singular minimal-support probability pairs matching moments through order `m-1`, and determine whether those leading-moment optimizers also control the Euler discrepancy when bandwidth grows with `1/\delta`. Fixed-band Taylor optimality does not decide the reciprocal-band harmonic regime of AF-187--AF-194.

## Falsification and boundaries

- **This is a fixed minimal-support theorem.** Four nodes are used because AF-195 proves that four is the minimum support size for nonzero exact quadratic cancellation. Extra nodes have additional nullspace freedom and are not covered.
- **The source metric is exactly `W_1`.** Another metric changes the normalization and can change the optimal shape.
- **The left anchor is fixed for the Euler comparison.** Moving the whole cluster changes the Euler kernel amplitude and is a different source resource.
- **The exact global optimization is for the leading cubic moment.** The Euler consequence is asymptotic as `\delta\downarrow0` on a fixed finite band; no claim is made that `t_*` minimizes the exact finite-`\delta` Euler norm.
- **Growing bandwidth is not covered.** When `T=T(\delta)` approaches reciprocal separation, higher Euler harmonics and the residue-class/theta mechanisms of AF-187--AF-194 can dominate the Taylor regime.
- **Exact identifiability is not lost.** These are distinct positive generalized-generator controls whose bounded-band observations become closer; this is a conditioning result, not an exact collision.
- **No rational-prime specificity follows.** As in AF-182, the construction is a matched generalized-Euler control and applies independently of whether the generator locations are logarithms of rational primes.
- **No universal minimax claim is made beyond the declared class.** Approximate moment matching, unequal support counts, common mass, multiplicity constraints, minimum node separation, or arithmetic restrictions define different optimization problems.

## Prior art and novelty assessment

The ingredients sit inside established approximation, moment-matching, and optimal-stencil theories, so no theorem-level novelty is claimed here.

- Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46--69, arXiv:`math/0502036`, is the classical divided-difference source underlying the unique cubic annihilator and its Peano/Taylor interpretation.
- Bengt Fornberg, **“Generation of Finite Difference Formulas on Arbitrarily Spaced Grids,”** *Mathematics of Computation* 51(184) (1988), 699--706, DOI `10.1090/S0025-5718-1988-0935077-0`, gives the standard arbitrary-grid finite-difference weight framework used already in AF-195.
- Yanjun Han, Jiantao Jiao, and Tsachy Weissman, **“Local Moment Matching: A Unified Methodology for Symmetric Functional Estimation and Distribution Estimation under Wasserstein Distance,”** *Proceedings of COLT 2018*, PMLR 75, 3189--3221, develops moment matching explicitly in Wasserstein geometry and is relevant background for treating moment agreement and transport separation jointly.
- Oleg Davydov and Robert Schaback, **“Optimal Stencils in Sobolev Spaces,”** *IMA Journal of Numerical Analysis* 39(1) (2019), 398--422, DOI `10.1093/imanum/drx076`, studies optimal convergence/error of polynomially exact stencils under a different Sobolev objective and reinforces that node placement and the declared error geometry are separate resources.
- Manuel Kindelan, Miguel Moscoso, and Pedro Gonzalez-Rodriguez, **“Optimized Finite Difference Formulas for Accurate High Frequency Components,”** *Mathematical Problems in Engineering* (2016), Article 7860618, DOI `10.1155/2016/7860618`, is direct prior art for optimizing finite-difference behavior against a frequency-band objective rather than assuming the standard Taylor-optimal stencil is application-optimal.

A targeted search across moment matching/Wasserstein, arbitrary-grid divided differences, optimal stencils, and frequency-optimized finite differences did not locate the exact four-node `W_1`-normalized extremum `(7)`--`(8)`. That absence is not evidence of novelty. The durable value here is the exact specialization needed by the Arithmetic Fidelity frontier: it kills the tempting extension of AF-195 from fixed-grid uniqueness to free-node optimality and identifies the precise source-geometry resource that a stronger Euler recovery theorem must control.

## Dependencies and evidence boundary

- **AF-182:** defines the positive parity-split Euler controls, fixed-band discrepancy `D_T`, exact moment cancellation, and exact `W_1` scale for the equispaced family.
- **AF-195:** proves that on any fixed four-node stencil the quadratic-annihilating signed control is unique up to scale and equals the normalized divided-difference functional; it explicitly leaves free-node Euler-band optimality open.
- **This finding:** solves that free-node question only for the first cubic/minimal-support leading-order regime. It proves the exact global `W_1`-normalized cubic-moment optimizer and its fixed-band Euler asymptotic consequence. It does not settle general `m`, extra support, approximate cancellation, or reciprocal-band Euler minimax behavior.
