# WI-317 — Finite source-exact localization portfolios cannot autonomously contract a scalar defect

**Status:** `EXACT-DERIVED + CLASSICAL-SPECTRAL + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

**Parent findings:** WI-304, WI-305, WI-311, WI-316.

WI-316 makes the post-localization target precise: after the capped retained tail has been flattened, an `o(1)` comparison error is already RH-equivalent, so a genuinely easier bootstrap would need a **nonvanishing, source-valid contraction** of the unknown defect. The most direct possible attempt is to feed an existing scalar lower semibound for the Weil form back through the exact sliding-localization identity and hope that localization improves the same scalar constant.

That route is impossible for every fixed finite portfolio of the smooth source-exact localizations used in WI-307--WI-311. The obstruction is stronger once the first prime atom is active: there is a single weakly-null high-frequency sequence on which the localization defect of **every member of the finite portfolio is eventually positive**. Hence choosing the best localization adaptively still cannot improve the original scalar semibound. Before the first prime activates, all such defects can simultaneously be made arbitrarily small, which again precludes any positive uniform contraction.

This is a barrier for an autonomous scalar bootstrap, not for localization itself. It leaves open mode-dependent arithmetic information, stronger bounds on the localized pieces, non-scalar invariants, and genuinely infinite/adaptive architectures carrying extra structure.

## 1. Exact contraction criterion

Fix an outer aperture `L>0`, and let `Q` denote the source-exact Weil quadratic form on the corresponding compact-support domain. Consider one admissible smooth localization family `r`. It may itself be a finite multiwindow family as in WI-311. Write its exact identity as

\[
Q(f)=\operatorname{Loc}_r(f)-\mathcal E_r(f),
\tag{1}
\]

where

\[
\operatorname{Loc}_r(f)
=
\sum_\nu\int Q(g^{(r)}_{\nu,y}f)\,dy
\tag{2}
\]

and the normalization of the localizers gives

\[
\sum_\nu\int\|g^{(r)}_{\nu,y}f\|_2^2\,dy
=
\|f\|_2^2.
\tag{3}
\]

Suppose the only information fed into every localized source term is the **same scalar semibound**

\[
Q(h)\ge -c\|h\|_2^2.
\tag{4}
\]

Then (2)--(4) give

\[
\operatorname{Loc}_r(f)\ge -c\|f\|_2^2,
\]

and therefore

\[
Q(f)\ge -c\|f\|_2^2-\mathcal E_r(f).
\tag{5}
\]

If the original bound (4) is retained as well, the best pointwise scalar estimate obtained from a finite portfolio `r=1,...,R` is

\[
Q(f)
\ge
-c\|f\|_2^2
+
\max\left\{0,-\min_{1\le r\le R}\mathcal E_r(f)\right\}.
\tag{6}
\]

Consequently a uniform contraction from `c` to `c-kappa`, with `kappa>0`, would require

\[
\boxed{
\min_{1\le r\le R}\mathcal E_r(f)
\le -\kappa\|f\|_2^2
\quad\text{for every }f.
}
\tag{7}
\]

Thus the question is not whether some test vector has negative localization error. A scalar bootstrap needs a **uniformly negative error from at least one member of the portfolio for every direction**.

## 2. Source-exact form of each localization error

For the smooth compactly supported localizers of WI-311, let

\[
R_r(a)
=
\sum_\nu\int
 g^{(r)}_\nu(u+a)g^{(r)}_\nu(u)\,du
\tag{8}
\]

be the aggregate autocorrelation, normalized by

\[
\sum_\nu\|g^{(r)}_\nu\|_2^2=1.
\tag{9}
\]

On the fixed outer aperture, the exact source formula of WI-304/WI-311 writes the defect as a continuous archimedean term plus finitely many active prime-power terms:

\[
\mathcal E_r(f)
=
\mathcal C_r(f)
+
\sum_{\log n<2L}
 c_n\bigl(1-R_r(\log n)\bigr)
 H_f(\log n),
\qquad
c_n=\frac{2\Lambda(n)}{\sqrt n}>0.
\tag{10}
\]

The smoothness of the localizers makes the continuous coefficient integrable at the origin, and for a fixed compactly supported amplitude modulated to frequency `t`, its contribution tends to zero by the Riemann--Lebesgue lemma, exactly as in WI-304.

Every nonzero shift has a **strictly positive** arithmetic coefficient. To see this without any quantitative autocorrelation estimate, put

\[
G_r=(g^{(r)}_1,\ldots,g^{(r)}_{J_r})
\in L^2(\mathbb R;\mathbb R^{J_r}).
\]

Then `||G_r||_2=1` and

\[
R_r(a)=\langle T_aG_r,G_r\rangle.
\]

Cauchy--Schwarz gives `R_r(a)<=1`. Equality at a nonzero `a` would force `T_aG_r=G_r` almost everywhere. A nonzero compactly supported `L^2` vector cannot be invariant under a nonzero translation, so

\[
\boxed{R_r(a)<1\qquad(a\ne0).}
\tag{11}
\]

Hence, whenever `log n<2L`,

\[
\alpha_{r,n}:=c_n(1-R_r(\log n))>0.
\tag{12}
\]

This uses only source exactness and compact support; no special numerical localizer is involved.

## 3. One recurrence sequence defeats every finite portfolio

Assume first that the first prime atom is active,

\[
\log2<2L.
\tag{13}
\]

There are only finitely many prime powers satisfying `log n<2L`. Let `a_*` be the largest of their logarithms. Since `a_*<2L`, choose a real nonnegative

\[
\phi\in C_c^\infty((-L,L)),\qquad \|\phi\|_2=1,
\]

whose positive region is wide enough that

\[
h(a):=\int\phi(u+a)\phi(u)\,du>0
\tag{14}
\]

for every active shift `a=log n`. Define the high-frequency modulations

\[
f_t(u)=e^{itu}\phi(u).
\tag{15}
\]

Then `f_t` is a unit vector and `f_t\rightharpoonup0` as `|t|\to\infty`. In the real Hermitian normalization of the source formula,

\[
H_{f_t}(a)=h(a)\cos(ta).
\tag{16}
\]

By simultaneous Dirichlet/Kronecker recurrence for the finite set of active shifts, there is an unbounded sequence `t_k` such that

\[
\cos(t_k\log n)\longrightarrow1
\qquad
\text{for every active prime power }n.
\tag{17}
\]

The sequence depends only on the finite active shift set, not on the chosen localization family. Riemann--Lebesgue kills every continuous term `C_r(f_{t_k})`. Equations (10), (12), (14), (16), and (17) therefore give, for every fixed portfolio member `r`,

\[
\boxed{
\mathcal E_r(f_{t_k})
\longrightarrow
\sum_{\log n<2L}
\alpha_{r,n}h(\log n)
>0.
}
\tag{18}
\]

The strict inequality already follows from the `n=2` term. Because the portfolio is finite, the minimum of the finitely many positive limits is positive. Thus for all sufficiently large `k`,

\[
\boxed{
\min_{1\le r\le R}\mathcal E_r(f_{t_k})>0.
}
\tag{19}
\]

Equation (19) is incompatible with the necessary contraction condition (7) for every `kappa>0`. In fact, on these shared recurrence directions every localization-derived inequality (5) is worse than the original scalar semibound (4).

## 4. Before the first prime activates, the defect still cannot contract uniformly

If

\[
2L\le\log2,
\tag{20}
\]

there are no active prime-power terms in (10), because the source sum uses the strict cutoff `log n<2L`. Thus

\[
\mathcal E_r(f_t)=\mathcal C_r(f_t)\longrightarrow0
\qquad(|t|\to\infty)
\tag{21}
\]

for every smooth portfolio member. For a finite portfolio the convergence is simultaneous. Given any `kappa>0`, sufficiently large `|t|` therefore satisfies

\[
\min_r\mathcal E_r(f_t)>-\kappa.
\tag{22}
\]

Again (7) fails. The threshold case `2L=log2` belongs here because the arithmetic cutoff is strict.

Combining (19) and (22) proves the finite-portfolio no-go at every finite aperture:

\[
\boxed{
\text{reusing only the same scalar lower semibound through a fixed finite portfolio}
\text{ cannot improve that semibound by any uniform }\kappa>0.
}
\tag{23}
\]

The conclusion is unchanged if one takes fixed convex combinations of the portfolio inequalities: the same sequence makes all active-atom errors positive, or all pre-activation errors arbitrarily small.

## 5. Consequence for the post-WI-316 frontier

WI-316 showed that a vanishing additive comparison error is not an intermediate target: it converges to the unknown global Weil floor. Equation (23) now closes the simplest proposed way of manufacturing a **nonvanishing contraction** from the exact localization identity itself. Localization cannot bootstrap a scalar defect merely by feeding the same scalar defect bound into its localized copies.

A viable contraction mechanism must therefore add information not present in the scalar premise (4). Examples not ruled out here are:

- a stronger bound for the localized pieces than the global scalar constant being bootstrapped;
- mode-dependent or prime-dependent arithmetic information that breaks the common recurrence sequence;
- a vector/matrix invariant stronger than the scalar bottom of `Q`;
- an infinite or dynamically changing localization architecture whose extra structure is not equivalent to choosing from one fixed finite portfolio.

The last item is deliberately left open. This finding does not claim that every possible recursive localization can be unfolded into the finite setting above. It rules out the autonomous finite scalar-feedback mechanism exactly as stated.

## 6. Prior-art and novelty audit

The algebra `Q=Loc-E` together with a reused lower semibound is the standard localization/IMS pattern. Weakly-null high-frequency tests, compact/continuous-term disappearance, and simultaneous recurrence on a finite torus are classical tools. Within this line, WI-304 already extracted prime-power essential obstruction bands from high-frequency phase control; WI-305 showed that the first active prime is enough to obstruct compact repair; WI-311 supplied the exact smooth multiwindow identity and nonnegative prime coefficients; WI-316 identified the need for a genuine contraction rather than an `o(1)` comparison loss.

A targeted prior-art audit around IMS/localization semibounds, essential numerical ranges under compact perturbations, simultaneous Dirichlet/Kronecker recurrence, and Weil-form prime-power localization found these ingredients separately but no source stating the finite-portfolio scalar-feedback obstruction (23) for this source-exact Weil localization architecture. **No priority claim is made.** The Mathia contribution recorded here is the exact synthesis of the already source-audited localization identity with one common recurrence sequence, and the resulting no-go for the current contraction target.

### Primary inputs

- WI-304, especially the source-exact localization-defect formula, Riemann--Lebesgue high-frequency limit, and prime-power phase mechanism.
- WI-305, especially the first-prime activation obstruction and strict autocorrelation loss at nonzero translation.
- WI-311, especially the exact smooth multiwindow identity and aggregate autocorrelation coefficients.
- WI-316, which isolates nonvanishing defect contraction as the missing post-comparison mechanism.
- P. A. Fillmore, J. G. Stampfli and J. P. Williams, **On the essential numerical range, the essential spectrum, and a problem of Halmos**, *Acta Sci. Math. (Szeged)* 33 (1972), 179--192, for the classical weakly-null/compact-perturbation background already audited in WI-304.

### Validation boundary

The theorem is conditional only on the exact localization identities and scalar semibound premise explicitly stated above; it makes no RH assumption and proves no new zero-density statement. It applies to any **fixed finite portfolio** of admissible smooth compactly supported source-exact localizers at a fixed aperture, even if the best portfolio member is chosen after seeing `f`. It does not cover an architecture that supplies genuinely stronger localized estimates, introduces new arithmetic constraints, tracks non-scalar data, or uses an infinite/adaptive family whose additional information is not captured by the finite scalar-feedback setup. It also makes no claim of priority for the classical ingredients.