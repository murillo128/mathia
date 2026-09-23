# WI-420 — Critical reciprocal-depth Blaschke crossover is a Poisson capacity

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + STRUCTURAL-CONSTRAINT + PRIOR-ART-REDIRECT`.

**Parents:** WI-410, WI-417, WI-418, WI-419.

## Claim

WI-418 and WI-419 identify opposite shallow-depth regimes for the bounded-density translated-Blaschke model: targets inside an `o(1/d)` height pocket can asymptotically reuse one one-target budget, whereas fixed-number targets separated by `omega(1/d)` have asymptotically additive costs. The unresolved critical scale `S asymp 1/d` has an exact universal limit. It is neither an unspecified interpolation nor another copy of the one-target bathtub problem: after the critical rescaling, the Blaschke kernel converges to the upper-half-plane Poisson kernel and the full multi-target capacity converges to a finite-constraint continuum linear program with an exact finite-dimensional dual.

For

\[
q_{a,b}(\gamma,d)
=\frac12\log\frac{(\gamma-b)^2+(a+d)^2}
{(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

fix `N<infinity`, a density cap `B>0`, target quanta `Q_j>0`, scaled depths `delta_j>0`, and scaled ordinates `c_j in R`. Let `s downarrow 0` and place the targets at

\[
(\gamma_{j,s},d_{j,s})
=\left(\gamma_0+\frac{c_j}{s},\,\delta_j s\right),
\qquad 1\le j\le N.
\tag{2}
\]

Thus ordinate differences are exactly on the reciprocal-depth scale. Let `M_s` be the infimum of `||nu||_TV` over finite signed or complex measures on `(0,infinity) x R` satisfying

\[
\frac{d|\nu|}{da\,db}\le B
\quad\text{a.e.}
\tag{3}
\]

and

\[
\left|\int q_{a,b}(\gamma_{j,s},d_{j,s})\,d\nu(a,b)\right|
\ge Q_j
\qquad(1\le j\le N).
\tag{4}
\]

Define the limiting Poisson kernels on the source half-plane `A>0` by

\[
P_j(A,Y)
=\frac{2\delta_j A}{A^2+(Y-c_j)^2},
\tag{5}
\]

and the bounded-density Poisson capacity

\[
\mathfrak C_B(\mathbf c,\boldsymbol\delta,\mathbf Q)
:=
\inf\left\{
\int g:\
0\le g\le B,\quad
\int P_j g\ge Q_j\ \forall j
\right\},
\tag{6}
\]

where all integrals are over `(0,infinity) x R` with Lebesgue measure. Then

\[
\boxed{
\lim_{s\downarrow0}s^2 M_s
=
\mathfrak C_B(\mathbf c,\boldsymbol\delta,\mathbf Q).
}
\tag{7}
\]

The limiting capacity has the exact finite-dimensional dual

\[
\boxed{
\mathfrak C_B
=
\sup_{\lambda_1,\ldots,\lambda_N\ge0}
\left[
\sum_{j=1}^N\lambda_jQ_j
-
B\int
\left(\sum_{j=1}^N\lambda_jP_j-1\right)_+
\right].
}
\tag{8}
\]

A primal optimizer exists. A dual optimizer exists, and one may choose a primal optimizer of bang-bang form

\[
\boxed{
g_*(A,Y)=B\,\mathbf 1_{\{\sum_j\lambda_jP_j>1\}}(A,Y)}
\tag{9}
\]

up to the null level set and the usual complementary-slackness degeneracy for redundant target constraints. Thus the critical-scale geometry is reduced from an infinite family of source densities to finitely many nonnegative multipliers and one weighted Poisson superlevel set.

For one target, (8) recovers exactly

\[
\mathfrak C_B(c,\delta,Q)
=\frac{Q^2}{4\pi B\delta^2},
\tag{10}
\]

the scaled limit of WI-417. For two equal targets with common `delta,Q` and distinct finite scaled ordinates `c_1 != c_2`, write

\[
C=\frac{Q^2}{4\pi B\delta^2}.
\]

Then the critical regime is genuinely intermediate:

\[
\boxed{
C
<
\mathfrak C_B(c_1,c_2;\delta,\delta;Q,Q)
<
2C.
}
\tag{11}
\]

Moreover the left endpoint is recovered as `|c_1-c_2| -> 0`, while the right endpoint is recovered as `|c_1-c_2| -> infinity`. Hence WI-418 and WI-419 are the two ends of one exact scale-invariant capacity problem, and the previously unresolved `S asymp 1/d` window has a precise variational object rather than a missing heuristic constant.

The theorem also covers **comparable varying depths** `d_{j,s}=delta_j s`, so the common-depth restriction of WI-418--WI-419 is not intrinsic at the critical scale. It does not cover scale-separated depth ratios `delta_j ->0` or `infinity`; those are different singular limits of (6).

No zeta zero is excluded by this theorem. The two upstream missing inputs remain unchanged: actual zeta arithmetic must justify a source-density cap such as (3), and it must place any exceptional defects in a geometric regime whose Poisson capacity overwhelms the available source budget.

## 1. Exact critical rescaling

Because the kernel is nonnegative, replacing a feasible signed or complex measure by its total-variation measure preserves the density cap, preserves total mass, and can only increase every target response. It is therefore enough to work with positive densities `f_s(a,b)` satisfying `0<=f_s<=B`.

Set

\[
A=sa,
\qquad
Y=s(b-\gamma_0),
\qquad
g_s(A,Y)=f_s(A/s,\gamma_0+Y/s).
\tag{12}
\]

Then `0<=g_s<=B` and

\[
s^2\|\nu_s\|_{\rm TV}=\int g_s(A,Y)\,dA\,dY.
\tag{13}
\]

At target `j`, the rescaled response kernel is

\[
\begin{aligned}
K_{s,j}(A,Y)
&:=s^{-2}q_{A/s,\,\gamma_0+Y/s}
\left(\gamma_0+\frac{c_j}{s},\delta_js\right)\\
&=\frac1{2s^2}
\log\frac{(Y-c_j)^2+(A+\delta_js^2)^2}
{(Y-c_j)^2+(A-\delta_js^2)^2}.
\end{aligned}
\tag{14}
\]

Hence the original response is exactly

\[
\int q\,f_s\,da\,db
=
\int K_{s,j}g_s\,dA\,dY.
\tag{15}
\]

Writing

\[
F_j(A,Y)=\frac12\log\bigl(A^2+(Y-c_j)^2\bigr),
\]

we have

\[
K_{s,j}
=
\frac{F_j(A+\delta_js^2,Y)-F_j(A-\delta_js^2,Y)}{s^2}.
\tag{16}
\]

Since `F_j in W^{1,1}_loc(R^2)`, the standard translation/difference-quotient identity gives

\[
K_{s,j}\longrightarrow
2\delta_j\,\partial_A F_j
=
\frac{2\delta_j A}{A^2+(Y-c_j)^2}
=P_j
\tag{17}
\]

in `L^1_loc` on the closed source half-plane, and therefore also pointwise away from the boundary singularity. This is the elementary Green-to-Poisson boundary derivative appearing here at exactly the reciprocal-depth scaling.

The convergence does not hide mass at infinity. Put

\[
\rho_j^2=A^2+(Y-c_j)^2.
\]

From (14),

\[
K_{s,j}
=s^{-2}\operatorname{artanh}
\left(
\frac{2A\delta_js^2}
{\rho_j^2+\delta_j^2s^4}
\right).
\tag{18}
\]

If `rho_j>=R` and `s` is small enough that `2 delta_j s^2/R<=1/2`, then the argument of `artanh` is at most `1/2`, so

\[
0\le K_{s,j}(A,Y)
\le \frac{4\delta_j}{\rho_j}
\le\frac{4\delta_j}{R}.
\tag{19}
\]

The limiting kernel satisfies the sharper `P_j<=2 delta_j/rho_j`. Thus bounded scaled source mass outside a large compact set has uniformly vanishing influence on every fixed target.

## 2. Capacity convergence

For the lower limit, take a sequence `s_n downarrow0` and positive near-minimizers `g_n`. A fixed finite source construction gives a uniform bound on `int g_n`; otherwise the desired lower bound is trivial. The box constraint `0<=g_n<=B` gives local weak-* compactness, so after a diagonal extraction

\[
g_n\stackrel{*}{\rightharpoonup}g
\quad\text{locally},
\qquad
0\le g\le B,
\qquad
\int g\le\liminf_n\int g_n.
\tag{20}
\]

On every compact set, (17) and the box bound imply

\[
\int K_{s_n,j}g_n
\longrightarrow
\int P_jg.
\tag{21}
\]

Indeed the `K-P` term is bounded by `B||K-P||_1`, while the remaining term is exactly local weak-* convergence tested against the locally integrable `P_j`. The tail bound (19), together with the uniform mass bound, lets the compact radius tend to infinity after `n->infinity`. Feasibility passes to the limit:

\[
\int P_jg\ge Q_j
\qquad\forall j.
\tag{22}
\]

Therefore

\[
\mathfrak C_B
\le\int g
\le\liminf_{n\to\infty}s_n^2M_{s_n}.
\tag{23}
\]

For the upper limit, first note that there are compactly supported **strictly** feasible Poisson densities. For example, density `B` on a sufficiently large half-plane tangent disk has response growing linearly with its radius at each of finitely many fixed targets. Starting from any near-minimizer of (6), take a small convex combination with such a strict feasible density; the box constraint is preserved and the mass changes arbitrarily little. Truncate on a sufficiently large compact set; the Poisson tail is uniformly small, so strict feasibility survives. We therefore obtain, for every `eta>0`, a compactly supported `g_eta` with

\[
0\le g_\eta\le B,
\qquad
\int g_\eta\le\mathfrak C_B+\eta,
\qquad
\int P_jg_\eta>Q_j
\quad\forall j.
\tag{24}
\]

By the local `L^1` convergence (17), the same fixed density is feasible for every sufficiently small `s` after undoing (12). Hence

\[
\limsup_{s\downarrow0}s^2M_s
\le\mathfrak C_B+\eta.
\tag{25}
\]

Letting `eta downarrow0` and combining with (23) proves (7).

This is a genuine capacity convergence, not merely pointwise kernel convergence: (19) is what rules out a cheaper family whose useful source mass escapes to scaled infinity.

## 3. Exact finite-multiplier dual

For `lambda_j>=0`, put

\[
S_\lambda(A,Y)=\sum_{j=1}^N\lambda_jP_j(A,Y).
\tag{26}
\]

The Lagrangian of (6) is

\[
\sum_j\lambda_jQ_j
+
\int g(1-S_\lambda).
\tag{27}
\]

Pointwise minimization over `0<=g<=B` gives

\[
\inf_{0\le g\le B}
\int g(1-S_\lambda)
=-B\int(S_\lambda-1)_+.
\tag{28}
\]

The integral is finite: every `P_j` decays like the reciprocal of the Euclidean source distance, so the superlevel set `{S_lambda>1}` is bounded; its boundary singularities are locally integrable.

There is no duality gap. One direct way to avoid importing a hidden function-space regularity assumption is to consider the finite-dimensional attainable set of tuples

\[
\left(\int g,\int P_1g,\ldots,\int P_Ng\right),
\qquad0\le g\le B.
\tag{29}
\]

Its bounded-mass slices are closed by the same local weak-* compactness and tail estimate used in Section 2. They are convex. Because strict feasible densities exist, a supporting hyperplane at the minimum-cost point over the orthant `r_j>=Q_j` has a strictly positive coefficient on the mass coordinate and nonnegative coefficients on the response coordinates. Normalizing the mass coefficient to one and minimizing that supporting functional pointwise in `g` gives exactly (28). Weak duality supplies the reverse inequality, proving (8).

The same compactness argument gives a primal optimizer. The dual objective is upper semicontinuous and coercive along every nonzero ray: already one positive multiplier generates a Poisson superlevel disk whose penalty in (8) grows quadratically in that multiplier. Hence a dual optimizer exists as well.

Complementary slackness with (28) gives the bang-bang rule (9). Since `S_lambda` is a nonconstant real-analytic function on `A>0`, the level set `{S_lambda=1}` has two-dimensional measure zero unless the corresponding constraint combination is degenerate. Thus, apart from redundant constraints, the critical source cloud is an honest weighted-Poisson superlevel region rather than an arbitrary fractional density.

This is the main structural gain over WI-418--WI-419: the unresolved collective geometry is finite-dimensional on the dual side.

## 4. Endpoint checks and a strict two-target crossover

For `N=1`, the superlevel set of

\[
P(A,Y)=\frac{2\delta A}{A^2+(Y-c)^2}
\]

is a tangent disk:

\[
\{P>t\}
=
\left\{(A,Y):
(A-\delta/t)^2+(Y-c)^2<(\delta/t)^2
\right\}.
\tag{30}
\]

Therefore the one-target dual can be evaluated explicitly. If `lambda>=0`,

\[
\int(\lambda P-1)_+
=\pi\lambda^2\delta^2,
\tag{31}
\]

so

\[
\sup_{\lambda\ge0}
\left(\lambda Q-\pi B\lambda^2\delta^2\right)
=
\frac{Q^2}{4\pi B\delta^2}.
\tag{32}
\]

This recovers (10) and the exact scaled limit of WI-417.

Now take two targets with the same `delta,Q` and scaled separation

\[
c=|c_1-c_2|>0.
\]

Put

\[
R=\frac{Q}{2\pi B\delta},
\qquad
C=\pi BR^2.
\tag{33}
\]

The unique one-target optimizer is density `B` on the tangent disk `D_R(c_1)`. Its response at the displaced target has the exact value

\[
B\int_{D_R(c_1)}P_2
=
\frac{2\pi B\delta R}{1+(c/R)^2}
=
\frac{Q}{1+(c/R)^2}
<Q.
\tag{34}
\]

The disk-potential identity is the `s->0` limit of WI-418's exact uniform-disk formula and can also be checked directly by the mean-value formula for the logarithmic potential. Consequently a two-target feasible density of total mass `C` would have to be the unique target-1 optimizer and would fail target 2. Thus

\[
\mathfrak C_B(c_1,c_2)>C.
\tag{35}
\]

For the opposite inequality, take the union of the two one-target optimizer disks. If they overlap, its mass is already strictly below `2C` and it is feasible. If they are disjoint (or merely touch), each target receives its own response `Q` plus a strictly positive response from the other disk. Multiplying the union density by a factor `1-epsilon` with sufficiently small `epsilon>0` preserves both constraints and gives mass strictly below `2C`. Hence

\[
\mathfrak C_B(c_1,c_2)<2C,
\tag{36}
\]

proving (11).

The endpoints match WI-418 and WI-419. As `c->0`, one tangent disk centered between the targets with radius `R(1+o(1))` covers both by the exact analogue of (34), while the one-target lower bound remains `C`; hence the capacity tends to `C`. As `c->infinity`, split the source into vertical cells around the two targets. The Poisson tail has the exact envelope

\[
\sup_{A>0}\frac{2\delta A}{A^2+r^2}
=\frac{\delta}{r},
\tag{37}
\]

so cross-cell response is `O(M/c)`. The WI-419 cell argument then gives a `2C-o(1)` lower bound, while the two one-target disks give the `2C` upper bound. Thus the capacity tends to `2C`.

For finitely many comparable varying depths, exactly the same limiting problem (6)--(9) applies with different `delta_j`. This supplies the varying-depth critical analogue that WI-419 left open, although it does not solve singular regimes in which depth ratios themselves diverge.

## 5. What this closes and what remains open

The theorem closes a specific gap in the bounded-density Blaschke branch. The critical reciprocal-depth regime no longer needs to be described vaguely as "genuinely multi-target". It has an exact scale-invariant object, and that object has a finite-dimensional dual suitable for analysis or certified computation. Any proposed critical-scale additivity or complete-reuse claim can now be tested against (8).

It also kills a tempting weak route: interpolating the WI-418 and WI-419 endpoint asymptotics by summing independent one-target tariffs. At finite nonzero scaled separation, even two equal targets have cost strictly between one and two tariffs. The missing quantity is a collective weighted-Poisson superlevel geometry, not a scalar correction to the one-target constant.

What it does **not** supply is more important for the RH objective. A bounded density `B` remains an assumed source regularity, not a theorem about the zeta explicit formula. Nor does (7) show that actual exceptional zeros have reciprocal-depth-separated scaled ordinates, or that their critical Poisson capacity exceeds any source-side budget. The theorem therefore refines the falsification model for a possible defect-to-zero bootstrap; it does not produce such a bootstrap by itself.

The comparable-depth assumption in (2) is also real. If `d_{i,s}/d_{j,s}` tends to zero or infinity, then no single `s` puts all targets into the finite-`delta` limit (5), and an additional multiscale capacity analysis is required.

## 6. Prior art and novelty audit

All analytic ingredients have classical antecedents. The fact that the Poisson kernel is the boundary normal derivative of the Green function is standard potential theory; Ransford's *Potential Theory in the Complex Plane* and standard harmonic-function texts cover this Green/Poisson relation. WI-417 already anchors the Brascamp--Lieb--Luttinger rearrangement/bathtub lineage for bounded-density one-target optimization. Poliquin, *Superlevel sets and nodal extrema of Laplace--Beltrami eigenfunctions*, Journal of Spectral Theory **7** (2017), 111--136, DOI `10.4171/JST/157`, is neighboring prior art using Green-function representations together with the bathtub principle. The finite-multiplier formula (8) is ordinary convex/linear-programming duality in the sense of Rockafellar's *Convex Analysis*; no new duality theorem is claimed.

The line-specific Burnol--Kunik/Blaschke kernel and its finite-budget role were already audited in WI-410, while WI-417--WI-419 established the one-target, clustered, and super-reciprocal regimes. A targeted external search around `Poisson kernel + bounded density + multiple point constraints`, `Green potential + bathtub + multiple targets`, `harmonic-measure optimal design`, `Poisson-kernel bang-bang control`, and density-constrained potential duality found the classical Green/Poisson, rearrangement, harmonic-measure, and convex-duality mechanisms, but no exact result matching the reciprocal-depth rescaling (7) together with the multi-target dual (8) for this translated-Blaschke capacity. That negative search is not evidence of priority, and no priority claim is made.

The durable mathematical delta is instead explicit and auditable: the previously open `S asymp 1/d` regime of this line is the bounded-density multi-point Poisson capacity (6), with exact convergence from the original Blaschke problem and exact finite-dimensional duality.

## 7. Audit and falsification tests

The finding has four load-bearing steps, each independently checkable.

1. **Scaling:** substituting `a=A/s`, `b=gamma_0+Y/s`, `d=delta s`, `gamma=gamma_0+c/s` into (1) must give (14) with displacement `delta s^2` in the scaled `A` variable.
2. **Kernel limit and tightness:** the central difference quotient (16) must converge in local `L^1` to (5), and the exact `artanh` representation must imply the uniform tail bound (19). Without the tail bound, pointwise convergence would not justify capacity convergence.
3. **Duality:** the attainable response/mass set must be closed under bounded mass. Local weak-* compactness plus the same tail estimate is the decisive closure argument; the supporting-hyperplane normalization requires strict feasibility.
4. **Strict critical interpolation:** the one-target optimizer must be unique up to null sets, and the displaced-disk response (34) must be strictly smaller than `Q` for `c!=0`. These two facts are what exclude equality with the one-target cost.

No numerical quadrature, interval certificate, conjectural zero statistic, or unproved zeta input enters (7)--(11).

## Consequence

The bounded-density translated-Blaschke branch now has a complete **scale-level** description for finitely many comparable shallow targets:

\[
\boxed{
\begin{array}{ll}
\text{scaled separation }sdistance\to0
&\Rightarrow\text{complete budget reuse},\\[1mm]
\text{scaled separation }sdistance\to c\in(0,\infty)
&\Rightarrow\text{multi-target Poisson capacity},\\[1mm]
\text{scaled separation }sdistance\to\infty
&\Rightarrow\text{asymptotic additivity}.
\end{array}}
\tag{38}
\]

At the critical middle scale, the exact object is (6) and the exact certification interface is the finite multiplier dual (8). The next useful step on this branch is therefore not another heuristic interpolation between WI-418 and WI-419. It is either to analyze/certify the Poisson capacity for source/target structures actually forced by zeta, to derive a zeta-side source regularity strong enough to justify the model, or to pass to a genuinely multiscale capacity when exceptional depths are not comparable.