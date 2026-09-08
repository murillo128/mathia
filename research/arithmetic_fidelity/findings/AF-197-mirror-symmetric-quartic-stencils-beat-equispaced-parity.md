# AF-197 — Mirror-symmetric quartic stencils beat equispaced parity

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `SOURCE-CLASS-OPTIMIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-195 identifies the unique minimal-support signed control that annihilates all polynomials below a prescribed order, and AF-196 proves that for the first free-node cubic case (`m=3`) the equispaced parity stencil is not optimal at fixed Wasserstein separation. The next order already shows that this is not a one-off cubic effect.

Consider the five-node mirror-symmetric stencil

\[
u_0=x,
\quad
u_1=x+h,
\quad
u_2=x+(1+t)h,
\quad
u_3=x+(1+2t)h,
\quad
u_4=x+(2+2t)h,
\tag{1}
\]

with `h>0` and `t>0`. Its consecutive gaps are

\[
h,\;th,\;th,\;h.
\tag{2}
\]

Let `lambda_j=1/\prod_{k\ne j}(u_j-u_k)` be the fourth divided-difference weights, and normalize their positive and negative parts as in AF-195 to obtain mutually singular probability measures `mu_+` and `mu_-`. Then their signed difference has the explicit form

\[
\boxed{
\mu_+-\mu_-
=
\alpha\,\delta_{u_0}
-\frac12\delta_{u_1}
+\gamma\,\delta_{u_2}
-\frac12\delta_{u_3}
+\alpha\,\delta_{u_4},
}
\tag{3}
\]

where

\[
\alpha=\frac{t^2}{2(t+1)^2},
\qquad
\gamma=\frac{2t+1}{(t+1)^2},
\qquad
2\alpha+\gamma=1.
\tag{4}
\]

Hence both sides are ordinary positive probability measures. Their moments agree through degree three, while

\[
\boxed{
\int u^4\,d(\mu_+-\mu_-)(u)
=t^2(2t+1)h^4.
}
\tag{5}
\]

Their exact one-dimensional Wasserstein separation is

\[
\boxed{
W_1(\mu_+,\mu_-)
=h\,\frac{t(3t+1)}{(t+1)^2}.
}
\tag{6}
\]

Therefore the scale-free fourth-moment response at fixed source separation is

\[
\boxed{
Q_4(t)
:=
\frac{\int u^4\,d(\mu_+-\mu_-)(u)}{W_1(\mu_+,\mu_-)^4}
=
\frac{(t+1)^8(2t+1)}{t^2(3t+1)^4}.
}
\tag{7}
\]

The equispaced parity stencil is `t=1`, so

\[
Q_4(1)=3.
\tag{8}
\]

Within the entire mirror-symmetric family `(1)`, `Q_4` has a unique global minimizer `t=t_*`, where `t_*` is the unique positive root of

\[
\boxed{
9t^3-5t^2-7t-1=0.
}
\tag{9}
\]

Numerically,

\[
t_*\approx1.249310692784357,
\qquad
Q_4(t_*)\approx2.890238119451529.
\tag{10}
\]

Thus

\[
\boxed{Q_4(t_*)<Q_4(1),}
\tag{11}
\]

an exact reduction of about `3.66%` in the leading fourth-order response at the same exact `W_1` separation. A simple rational witness already proves strict improvement without solving the cubic: at `t=5/4`,

\[
Q_4(5/4)
=
\frac{301327047}{104256800}
<3.
\tag{12}
\]

The same improvement transfers to the actual Euler logarithm on every fixed finite vertical band in the small-source-scale limit. Fix `x>0`, `sigma>0`, and `T<infinity`, and put

\[
F_s(u)=-\log(1-e^{-su}),
\qquad
s=\sigma+i\tau.
\tag{13}
\]

Rescale `h` so that `W_1(mu_+,mu_-)=delta`. Then

\[
\boxed{
D_T(\mu_+,\mu_-)
=
\frac{Q_4(t)}{24}
M_4(x,\sigma,T)\,\delta^4
+O_{t,x,\sigma,T}(\delta^5),
}
\tag{14}
\]

where

\[
D_T
=
\sup_{|\tau|\le T}
\left|
\int F_{\sigma+i\tau}(u)\,d(\mu_+-\mu_-)(u)
\right|,
\qquad
M_4
=
\sup_{|\tau|\le T}|F_{\sigma+i\tau}^{(4)}(x)|>0.
\tag{15}
\]

Consequently, for sufficiently small `delta`, the `t=t_*` mirror-symmetric nonuniform stencil has strictly smaller full fixed-band Euler discrepancy than the equispaced five-node parity control at the same exact Wasserstein separation.

This does **not** solve the unrestricted five-node problem: an asymmetric stencil may do better still. It does show that the free-node improvement found in AF-196 persists at the next cancellation order even under the strong extra constraint of reflection symmetry.

## Derivation

### 1. Divided-difference weights and probability normalization

After factoring out the common scale `h^{-4}`, the node positions relative to `x` are

\[
0,\;1,\;1+t,\;1+2t,\;2+2t.
\tag{16}
\]

Direct evaluation of the barycentric denominators gives

\[
\lambda_0=\lambda_4
=\frac{h^{-4}}{2(t+1)^2(2t+1)},
\tag{17}
\]

\[
\lambda_1=\lambda_3
=-\frac{h^{-4}}{2t^2(2t+1)},
\tag{18}
\]

and

\[
\lambda_2
=\frac{h^{-4}}{t^2(t+1)^2}.
\tag{19}
\]

The total positive mass of the unnormalized signed functional is

\[
A=\lambda_0+\lambda_2+\lambda_4
=\frac{h^{-4}}{t^2(2t+1)}.
\tag{20}
\]

Dividing by `A` gives exactly `(3)`--`(4)`. AF-195's divided-difference identity then yields

\[
\int P(u)\,d(\mu_+-\mu_-)(u)=0
\qquad
(\deg P<4),
\tag{21}
\]

and

\[
\int u^4\,d(\mu_+-\mu_-)(u)=\frac1A,
\tag{22}
\]

which is `(5)`.

### 2. Exact Wasserstein distance

For probability measures on the real line,

\[
W_1(\mu_+,\mu_-)
=\int_{\mathbb R}|G_+(u)-G_-(u)|\,du.
\tag{23}
\]

The cumulative signed masses across the four intervals are

\[
\alpha,
\qquad
-\beta,
\qquad
\beta,
\qquad
-\alpha,
\tag{24}
\]

with

\[
\beta=\frac{2t+1}{2(t+1)^2}.
\tag{25}
\]

Using the interval lengths `h,th,th,h`,

\[
W_1
=2h\alpha+2th\beta
=h\frac{t(3t+1)}{(t+1)^2},
\tag{26}
\]

proving `(6)`. Combining `(5)` and `(6)` gives `(7)`.

### 3. Exact optimization inside the symmetric family

The logarithmic derivative is

\[
\frac{d}{dt}\log Q_4(t)
=
\frac{8}{t+1}
+\frac{2}{2t+1}
-\frac{2}{t}
-\frac{12}{3t+1}.
\tag{27}
\]

Combining terms,

\[
\boxed{
\frac{d}{dt}\log Q_4(t)
=
\frac{2(9t^3-5t^2-7t-1)}
{t(t+1)(2t+1)(3t+1)}.
}
\tag{28}
\]

The denominator is positive for `t>0`. The numerator polynomial

\[
p(t)=9t^3-5t^2-7t-1
\tag{29}
\]

has exactly one positive root by Descartes' rule of signs, because its coefficient sequence has one sign change. Also `p(0)=-1` and `p(t)->+infinity` as `t->+infinity`, so that root exists and the derivative changes from negative to positive there. Finally,

\[
Q_4(t)\to+\infty
\quad(t\downarrow0),
\qquad
Q_4(t)\to+\infty
\quad(t\to+\infty).
\tag{30}
\]

Thus `t_*` is the unique global minimizer of the mirror-symmetric family. Equation `(12)` gives an exact rational strict comparison with equispacing; `(9)`--`(10)` identify the actual optimizer.

### 4. Fixed-band Euler asymptotics

Fix the shape parameter `t`. Solving `(6)` for a prescribed source separation `delta` gives

\[
h
=\delta\frac{(t+1)^2}{t(3t+1)}.
\tag{31}
\]

Hence every node lies within `O_t(delta)` of `x`. On a fixed compact vertical band `|tau|<=T`, the family `F_{sigma+i tau}` is analytic in `u` on a common neighborhood of `x`, with uniformly bounded derivatives of any fixed order. Taylor expansion at `x`, together with the exact cancellations `(21)`, gives uniformly in `|tau|<=T`,

\[
\int F_s(u)\,d(\mu_+-\mu_-)(u)
=
\frac{F_s^{(4)}(x)}{4!}
\int (u-x)^4\,d(\mu_+-\mu_-)(u)
+O(\delta^5).
\tag{32}
\]

Because lower signed moments vanish, the fourth moment about `x` equals the fourth moment in `(5)`. Using `(7)` and `(31)`,

\[
\int (u-x)^4\,d(\mu_+-\mu_-)(u)
=Q_4(t)\delta^4.
\tag{33}
\]

Taking the supremum over the compact band proves `(14)`.

## Consequence for the source-class frontier

AF-196 proves the unrestricted free-node optimum for `m=3`. AF-197 does not yet provide the analogous unrestricted theorem for `m=4`, but it removes a plausible exceptional interpretation of the cubic result: **equispacing already fails at `m=4` inside a one-parameter reflection-symmetric subclass**.

The equispaced parity family remains canonical for a fixed arithmetic progression, but cancellation order plus exact `W_1` separation do not determine the sharp leading observation constant even when one additionally imposes mirror symmetry. Node geometry continues to consume fidelity budget.

The next stronger questions are therefore sharply separated:

1. determine whether the symmetric optimizer `(9)` is also the global optimizer among all positive four-gap shapes;
2. if not, characterize the asymmetric improvement;
3. for general `m`, determine whether equispacing is ever free-node optimal beyond the quadratic case `m=2`, and identify the correct source-geometry extremizers or asymptotic bounds;
4. only after that source-class problem is understood, compare the low-band moment optimizer with reciprocal-band Euler harmonic recovery, where AF-187--AF-194 show that kernel-specific resonance can defeat purely regularity-based invisibility.

## Falsification and boundaries

- **Mirror symmetry is a real restriction.** The proof optimizes only gaps `(h,th,th,h)`. No claim is made that `t_*` is globally optimal among arbitrary `(a,b,c,d)`.
- **Minimal support and exact moment cancellation are fixed.** Extra nodes or approximate cancellation create higher-dimensional source classes not covered here.
- **The resource metric is exactly `W_1`.** A diameter, `W_2`, total variation, coefficient norm, or support-width budget can have a different optimizer.
- **The Euler consequence is fixed-band and asymptotic.** It does not establish reciprocal-band or growing-band minimax optimality.
- **Reflection symmetry does not come from the primes.** This is a general matched-control theorem for positive source measures; no rational-prime specificity follows.
- **The result is about information loss, not an RH implication.** It sharpens which source geometries can hide from a declared low-band observation but does not by itself produce a route from that observation to the zero set.

## Prior art and novelty assessment

The interpolation ingredients are classical. De Boor's divided-difference calculus and Fornberg's formulas on arbitrarily spaced grids already supply the weight identities and polynomial exactness framework used here. Numerical-analysis work on optimized finite-difference stencils, including Davydov--Schaback's Sobolev-space optimization and frequency-optimized stencil literature, shows that node/weight geometry is a standard optimization variable once an error norm is declared.

The Wasserstein/moment connection is also established territory. Han--Jiao--Weissman use local moment matching to control distribution estimation under Wasserstein distance, and related inverse-problem/statistical literature derives Wasserstein bounds from finitely many moments by polynomial approximation.

A targeted literature audit did not identify the specific objective `(7)`: minimize the first nonvanishing moment of the **positive/negative split of a minimal divided-difference control** at fixed exact one-dimensional `W_1` separation, nor the cubic stationarity equation `(9)` for the five-node mirror-symmetric case. That search is not exhaustive, and the proof uses elementary classical ingredients, so **no novelty claim is made**. The durable value here is the exact source-class comparison and its consequence for the Arithmetic Fidelity control hierarchy.

Relevant anchors:

- Carl de Boor, **"Divided Differences,"** *Surveys in Approximation Theory* 1 (2005), 46--69, arXiv:`math/0502036`.
- Bengt Fornberg, **"Generation of Finite Difference Formulas on Arbitrarily Spaced Grids,"** *Mathematics of Computation* 51(184) (1988), 699--706, DOI `10.1090/S0025-5718-1988-0935077-0`.
- Oleg Davydov and Robert Schaback, **"Optimal Stencils in Sobolev Spaces,"** *IMA Journal of Numerical Analysis* 39 (2019), 398--422, DOI `10.1093/imanum/drx076`, arXiv:`1611.04750`.
- Yanjun Han, Jiantao Jiao, and Tsachy Weissman, **"Local moment matching: A unified methodology for symmetric functional estimation and distribution estimation under Wasserstein distance,"** *Proceedings of Machine Learning Research* 75 (2018), 3189--3221, arXiv:`1802.08405`.

## Dependency audit

- **AF-182:** supplies the positive parity-split Euler controls, exact moment cancellation, fixed-band discrepancy, and `W_1` normalization for the equispaced family.
- **AF-195:** proves that on any fixed five-node stencil the cubic-annihilating signed control is unique up to scale and is the divided-difference functional.
- **AF-196:** proves the unrestricted free-node cubic (`m=3`) optimizer and explicitly leaves general `m` open.
- **This finding:** proves a strict nonuniform improvement and the exact optimizer only inside the mirror-symmetric five-node quartic (`m=4`) family. It does not settle the unrestricted five-node or general-order problem.
