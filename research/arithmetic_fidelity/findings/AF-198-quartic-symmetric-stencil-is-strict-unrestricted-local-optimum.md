# AF-198 — The quartic symmetric stencil is a strict unrestricted local optimum

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `SOURCE-CLASS-OPTIMIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-197 proves that, inside the mirror-symmetric five-node family with consecutive gaps

\[
(h,th,th,h),
\]

the scale-free fourth-moment response at fixed `W_1` separation

\[
Q_4(t)=\frac{(t+1)^8(2t+1)}{t^2(3t+1)^4}
\]

has a unique minimizer `t=t_*`, where `t_*` is the unique positive root of

\[
9t^3-5t^2-7t-1=0.
\tag{1}
\]

The remaining question was whether allowing arbitrary asymmetric perturbations of the four gaps immediately beats that symmetric optimum. It does not.

Consider arbitrary positive consecutive gaps

\[
a,b,c,d>0
\]

between five ordered nodes. Let the fourth divided-difference weights be normalized by their positive and negative parts as in AF-195, producing mutually singular probability measures `\mu_+` and `\mu_-`. Their signed difference annihilates every polynomial of degree below four. Define

\[
Q(a,b,c,d)
:=
\frac{\displaystyle\int u^4\,d(\mu_+-\mu_-)(u)}
{W_1(\mu_+,\mu_-)^4}.
\tag{2}
\]

Then the AF-197 shape

\[
\boxed{a=d=h,\qquad b=c=t_*h}
\tag{3}
\]

is a **strict local minimizer of `Q` among all positive four-gap shapes, modulo common scale**.

Thus the symmetric optimizer is not merely optimal because reflection symmetry was imposed. Every sufficiently small genuinely asymmetric deformation raises the normalized fourth-order response. Any global five-node control that improves on AF-197 must lie a finite distance away in shape space; it cannot arise from an infinitesimal symmetry breaking of `(3)`.

This closes only the local unrestricted problem. It does **not** prove that `(3)` is the global minimizer among all positive four-gap shapes.

## Exact unrestricted objective

For the five ordered nodes with gaps `(a,b,c,d)`, the unnormalized fourth divided-difference weights have signs `(+,-,+,-,+)`. Their total positive mass simplifies to

\[
A
=
\frac{ab+ad+cd}
{abcd\,(a+b+c)(b+c+d)}.
\tag{4}
\]

Since the divided-difference functional sends `u^4` to `1`, the normalized signed fourth moment is

\[
\boxed{
M_4
:=
\int u^4\,d(\mu_+-\mu_-)(u)
=
\frac{abcd\,(a+b+c)(b+c+d)}{ab+ad+cd}.
}
\tag{5}
\]

The cumulative signed masses alternate sign on the four consecutive source intervals. Integrating their absolute value therefore gives the exact one-dimensional transport separation

\[
\boxed{
W_1
=
\frac{2abcd\,P(a,b,c,d)}
{(a+b)(b+c)(c+d)(ab+ad+cd)(a+b+c+d)},
}
\tag{6}
\]

where

\[
\begin{aligned}
P={}&a^2b+2a^2c+a^2d+2ab^2+6abc+3abd+3ac^2+3acd+ad^2\\
&+b^3+5b^2c+3b^2d+5bc^2+6bcd+2bd^2+c^3+2c^2d+cd^2.
\end{aligned}
\tag{7}
\]

Combining `(5)` and `(6)` yields the unrestricted scale-free objective

\[
\boxed{
Q
=
\frac{(a+b)^4(b+c)^4(c+d)^4(a+b+c)(b+c+d)(ab+ad+cd)^3(a+b+c+d)^4}
{16a^3b^3c^3d^3P^4}.
}
\tag{8}
\]

Equation `(8)` is invariant under common rescaling of all four gaps and under reflection

\[
(a,b,c,d)\longmapsto(d,c,b,a).
\tag{9}
\]

It provides the exact objective required for the unrestricted five-node source-geometry problem left open by AF-197.

## Shape coordinates and the symmetric slice

Separate scale, inner/outer balance, and asymmetry by writing

\[
s=a+d>0,
\qquad
r=\frac{b+c}{a+d}>0,
\tag{10}
\]

and

\[
x=\frac{a-d}{a+d},
\qquad
y=\frac{b-c}{b+c},
\qquad |x|<1,\quad |y|<1.
\tag{11}
\]

Equivalently,

\[
a=\frac{s}{2}(1+x),
\quad d=\frac{s}{2}(1-x),
\quad b=\frac{sr}{2}(1+y),
\quad c=\frac{sr}{2}(1-y).
\tag{12}
\]

Scale invariance removes `s`, so write the resulting objective as `Q(r,x,y)`. Reflection acts as

\[
(x,y)\longmapsto(-x,-y).
\tag{13}
\]

On the symmetric slice `x=y=0`, equation `(8)` reduces exactly to

\[
\boxed{
Q(r,0,0)
=
\frac{(r+1)^8(2r+1)}{r^2(3r+1)^4},
}
\tag{14}
\]

which is the AF-197 function `Q_4(r)`. Its logarithmic derivative is

\[
\boxed{
\frac{d}{dr}\log Q(r,0,0)
=
\frac{2(9r^3-5r^2-7r-1)}
{r(r+1)(2r+1)(3r+1)}.
}
\tag{15}
\]

Hence `(1)` is exactly the stationary equation in the remaining symmetric shape variable.

## Full asymmetric Hessian

Because of the reflection symmetry `(13)`,

\[
\partial_x\log Q(r,0,0)
=
\partial_y\log Q(r,0,0)
=0
\qquad(r>0),
\tag{16}
\]

and consequently the mixed derivatives with the symmetric shape coordinate also vanish there:

\[
\partial_{rx}^2\log Q(r,0,0)
=
\partial_{ry}^2\log Q(r,0,0)
=0.
\tag{17}
\]

Direct differentiation of the exact rational objective `(8)` gives the Hessian in the two unrestricted asymmetry coordinates:

\[
H(r)
=
\begin{pmatrix}
H_{xx}(r)&H_{xy}(r)\\
H_{xy}(r)&H_{yy}(r)
\end{pmatrix},
\tag{18}
\]

with

\[
H_{xx}
=
\frac{2(36r^5+102r^4+51r^3-21r^2-15r-1)}
{(r+1)^2(2r+1)^2(3r+1)},
\tag{19}
\]

\[
H_{xy}
=
\frac{2r(9r^3+r^2+3r+3)}
{(r+1)^2(2r+1)(3r+1)},
\tag{20}
\]

and

\[
H_{yy}
=
\frac{2(r^3+21r^2+15r+3)}
{(r+1)^2(3r+1)}.
\tag{21}
\]

The determinant collapses to

\[
\boxed{
\det H(r)
=
-\frac{4D(r)}
{(r+1)^2(2r+1)^2(3r+1)^2},
}
\tag{22}
\]

where

\[
D(r)
=45r^6-930r^5-863r^4+28r^3+207r^2+54r+3.
\tag{23}
\]

At the AF-197 optimizer `r=t_*`, positivity is exact and does not rely on a decimal approximation. Reducing the numerator of `(19)` modulo the stationary cubic `(1)` gives

\[
36t_*^5+102t_*^4+51t_*^3-21t_*^2-15t_*-1
=
\frac{2}{81}
\left(6457t_*^2+4565t_*+620\right)>0.
\tag{24}
\]

Similarly,

\[
D(t_*)
=
-\frac{8}{729}
\left(156011t_*^2+108502t_*+14005\right)<0.
\tag{25}
\]

Therefore

\[
H_{xx}(t_*)>0,
\qquad
\det H(t_*)>0,
\tag{26}
\]

so `H(t_*)` is positive definite. Numerically, only as a check,

\[
H(t_*)\approx
\begin{pmatrix}
2.75454023&0.76876072\\
0.76876072&4.70124282
\end{pmatrix},
\tag{27}
\]

whose eigenvalues are approximately `2.48757` and `4.96822`.

## The remaining symmetric direction is also strictly positive

At a root of `(1)`, equation `(15)` gives the vanishing first derivative in `r`. The second logarithmic derivative can be written as

\[
\partial_{rr}^2\log Q(r,0,0)
=
-\frac{2(54r^6-60r^5-235r^4-196r^3-70r^2-12r-1)}
{r^2(r+1)^2(2r+1)^2(3r+1)^2}.
\tag{28}
\]

Reducing its numerator at `r=t_*` using `(1)` yields the strictly positive remainder

\[
\operatorname{num}\left(
\partial_{rr}^2\log Q(t_*,0,0)
\right)
=
\frac{8}{243}
\left(25493t_*^2+17728t_*+2287\right)>0.
\tag{29}
\]

Together with `(17)` and the positive-definite asymmetric block `(26)`, this proves that the full Hessian of `\log Q` in the three scale-free shape coordinates `(r,x,y)` is positive definite at

\[
(t_*,0,0).
\tag{30}
\]

Since `Q>0` and its gradient vanishes there, the Hessian of `Q` has the same definiteness at the stationary point. Thus `(3)` is a strict local minimum of the unrestricted positive four-gap problem modulo the irrelevant common scale.

## Consequence for the source-class frontier

AF-196 showed that at cancellation order three the globally optimal free-node stencil is symmetric but nonequispaced. AF-197 then found an improved mirror-symmetric quartic shape but explicitly left open whether asymmetry could lower the five-node objective.

The present result rules out the cheapest possible escape: **symmetry breaking cannot improve the quartic optimizer perturbatively**. The reflection-symmetric critical point is stable in both independent antisymmetric gap directions, not merely along the one-dimensional family in which it was discovered.

This makes the remaining global problem sharper. A better five-node source geometry, if one exists, must be a genuinely separated asymmetric competitor rather than a nearby deformation. Consequently, a future global proof or counterexample can focus on the nonlocal shape-space question: either establish a global lower bound for `(8)` or exhibit a distinct asymmetric basin with value below

\[
Q(t_*,0,0)\approx2.89023811945.
\tag{31}
\]

The result also reinforces the Arithmetic Fidelity resource principle: support size, exact moment cancellation, positivity, source metric, and **node geometry** all belong in the declared source class before a matched control is called extremal.

## Falsification and boundaries

- **Local is not global.** Positive Hessian at `(30)` excludes only sufficiently small shape perturbations. It does not rule out a disconnected asymmetric basin with a lower objective.
- **The source metric is exactly `W_1`.** Changing to support diameter, `W_2`, total variation, coefficient norm, or another budget changes `(8)` and may change the optimizer.
- **The support/cancellation model is fixed.** The theorem concerns the minimal five-node divided-difference control matching moments through degree three. Extra nodes, repeated nodes, or approximate cancellation are different source classes.
- **The result concerns the leading fixed-band response.** Through the same Taylor argument as AF-197, `Q` controls the fourth-order coefficient of the Euler-logarithm discrepancy as source scale tends to zero on a fixed finite vertical band. The theorem does not establish growing-band or reciprocal-resonance minimax optimality.
- **No rational-prime specificity follows.** These are general positive source measures. The theorem sharpens an adversarial control class but does not identify the ordinary primes or imply RH.
- **No novelty claim is made.** The derivation is elementary rational optimization built on classical divided-difference weights. Its durable role is to close a precise local question left open by AF-197.

## Prior art and novelty assessment

The underlying interpolation machinery is classical. Bengt Fornberg, **“Generation of Finite Difference Formulas on Arbitrarily Spaced Grids,”** *Mathematics of Computation* 51(184) (1988), 699–706, DOI `10.1090/S0025-5718-1988-0935077-0`, gives finite-difference weights of optimal polynomial accuracy on arbitrary one-dimensional node sets. Carl de Boor's survey **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46–69, arXiv:`math/0502036`, gives the standard divided-difference framework used by AF-195 and inherited here.

Optimization of stencil geometry/error is also established territory. Oleg Davydov and Robert Schaback, **“Optimal Stencils in Sobolev Spaces,”** *IMA Journal of Numerical Analysis* 39(1) (2019), 398–422, DOI `10.1093/imanum/drx076`, studies optimal convergence and near-optimal stencil construction for declared Sobolev error norms, explicitly allowing the node geometry to matter. This prevents treating “optimize the nodes, not only the weights” as a new principle.

Moment matching under Wasserstein loss likewise has a substantial literature. Yanjun Han, Jiantao Jiao, and Tsachy Weissman, **“Local Moment Matching: A Unified Methodology for Symmetric Functional Estimation and Distribution Estimation under Wasserstein Distance,”** *Proceedings of Machine Learning Research* 75 (2018), 3189–3221, develops moment-matching methods with Wasserstein recovery guarantees. The current theorem is not presented as a new general moment/Wasserstein principle.

A targeted audit did not supply a reason to identify the exact five-node objective `(8)` or its local stationary-point classification as an established named theorem, but absence from that search is not evidence of novelty. Accordingly the finding makes no novelty claim. Its Mathia-specific value is narrower: it converts AF-197's unresolved “could a nearby asymmetric stencil do better?” into an exact negative answer under the already-declared source resources.

## Dependencies and evidence boundary

- **AF-195:** supplies the unique normalized minimal-support moment-flat control on arbitrary fixed nodes through divided-difference weights.
- **AF-196:** proves the unrestricted four-node (`m=3`) optimum and establishes node placement as a real fidelity variable at fixed `W_1`.
- **AF-197:** solves the mirror-symmetric five-node (`m=4`) family and identifies the cubic equation `(1)` for its optimizer.
- **This finding:** derives the unrestricted four-gap objective and proves strict local optimality of the AF-197 shape in all scale-free shape directions. It does not settle unrestricted global optimality.