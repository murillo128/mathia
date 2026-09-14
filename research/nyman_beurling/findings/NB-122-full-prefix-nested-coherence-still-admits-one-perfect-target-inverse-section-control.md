# NB-122 — full-prefix nested coherence still admits one perfect-target inverse-section control

**Status:** `EXACT-DERIVED + NB-120/NB-121-SHARPENING + GROWING-CUTOFF-LADDER + PERFECT-TARGET-CAPTURE + DIAGONAL-FINITE-SOURCE-CONTROL + NEGATIVE/ROUTE-NARROWING + REPRESENTATION-AUDIT`.

`NB-121` proves that every fixed finite bounded-ratio ladder of nested natural-cell cutoffs collapses to its maximal cutoff and therefore does not break the inverse-section matched control from `NB-120`. It leaves a genuinely widening ladder as a possible escape because an early cutoff `r=o(R)` sees retained fraction `o(1/r)` when the common control is built at the maximal cutoff `R`.

That smaller retained fraction is not an obstruction. The actual-zero conclusions of `NB-116` and `NB-118` are **upper bounds** on retained cell energy. A common control that is even more compressed at early cutoffs still passes them. In fact the maximal `NB-120` repair captures the visible target **exactly at every integer cutoff below `R` simultaneously**. Thus an arbitrarily long, widening, even full-prefix nested ladder adds no source incompatibility at all unless it carries information beyond the nested projections themselves.

Let

\[
\mathcal E_r=\operatorname{span}\{\psi_n:1\le n<r\},
\qquad
Q_r=P_{\mathcal E_r},
\qquad
e_r=Q_re,
\qquad
L_r=\|e_r\|^2=1-\frac1r,
\tag{1}
\]

and

\[
V_M=\operatorname{span}\{g_2,\ldots,g_M\}.
\tag{2}
\]

Suppose `M=M(R)` lies in the mixed-tail regime of `NB-120`,

\[
M\to\infty,
\qquad
\frac{M^6(1+\log M)}{R}\to0.
\tag{3}
\]

Then for all sufficiently large `R` there is one vector

\[
\boxed{
f_R:=f_{M,R}\in V_M^\perp
}
\tag{4}
\]

such that for **every** integer `2<=r<=R`,

\[
\boxed{
Q_rf_R=e_r,
\qquad
q_r(f_R)=1.
}
\tag{5}
\]

Moreover, uniformly over the whole prefix,

\[
\boxed{
\eta_r(f_R)
:=
\frac{\|Q_rf_R\|^2}{\|f_R\|^2}
=
\frac{L_r}
     {L_R+\kappa_\infty R+o(R)}
=
\frac{1+o(1)}{\kappa_\infty R}\,L_r,
}
\tag{6}
\]

where

\[
\kappa_\infty
=
12\sum_p
\frac{p^2(\log p)^2}{(p^2-1)^2}
\in(0,\infty)
\tag{7}
\]

is the same constant as in `NB-120`. Hence

\[
\boxed{
r\,\eta_r(f_R)
=
\frac{r-1}
     {L_R+\kappa_\infty R+o(R)}.
}
\tag{8}
\]

For `r/R -> c in [0,1]` this gives

\[
r\,\eta_r(f_R)\longrightarrow \frac{c}{\kappa_\infty}.
\tag{9}
\]

In particular, every early widening scale `r=o(R)` satisfies

\[
\boxed{
\eta_r(f_R)=o(r^{-1}),
}
\tag{10}
\]

while every bounded-ratio scale `r~cR` remains at inverse-section order. The widening ladder therefore drives the same matched control **deeper into the compression near-kernel** at its early scales; it does not exclude it.

A useful global normalization makes the collapse even more explicit:

\[
\boxed{
\sum_{r=2}^{R}\eta_r(f_R)
=
\frac{R-H_R}
     {L_R+\kappa_\infty R+o(R)}
\longrightarrow
\frac1{\kappa_\infty}.
}
\tag{11}
\]

Thus imposing the entire prefix of exact target equations does not accumulate an extra logarithmic or polynomial norm cost. One maximal tail repair pays for all of them.

## 1. One maximal target equation implies the whole prefix exactly

The natural-cell spaces are nested:

\[
\mathcal E_2\subset\mathcal E_3\subset\cdots\subset\mathcal E_R.
\tag{12}
\]

Therefore, for `r<=R`,

\[
Q_rQ_R=Q_r.
\tag{13}
\]

`NB-120` constructs

\[
f_{M,R}=e_R+y_{M,R},
\qquad
y_{M,R}\in\mathcal E_R^\perp,
\tag{14}
\]

with

\[
f_{M,R}\perp V_M.
\tag{15}
\]

Applying `Q_r` to `(14)` gives

\[
Q_rf_{M,R}
=
Q_re_R+Q_ry_{M,R}
=
e_r.
\tag{16}
\]

This proves `(5)` simultaneously for all `r<=R`; no finite-ladder assumption is involved. The cardinality of the declared cutoff family can therefore grow like `R`, and the full prefix includes scale ratios as small as `2/R`.

The same observation allows a varying source budget. If `M_r<=M` is any family attached to the cutoffs, then

\[
f_R\perp V_M
\quad\Longrightarrow\quad
f_R\perp V_{M_r}
\qquad(2\le r\le R).
\tag{17}
\]

Hence the joint system

\[
Q_rf=e_r,
\qquad
f\perp V_{M_r},
\qquad
2\le r\le R,
\tag{18}
\]

is satisfied by the single maximal repair whenever all `M_r<=M`. Increasing the number of nested cutoffs creates no new linear equation beyond the maximal visible target and maximal Nyman section.

## 2. The full-prefix retention law is inherited from the maximal repair

Because the decomposition in `(14)` is orthogonal,

\[
\|f_R\|^2
=
L_R+\|y_{M,R}\|^2.
\tag{19}
\]

`NB-120` proves in the mixed-tail regime `(3)` that

\[
\|y_{M,R}\|^2
=
\kappa_\infty R+o(R).
\tag{20}
\]

Equation `(16)` gives `||Q_rf_R||^2=L_r`, so `(19)`--`(20)` prove `(6)` uniformly in `r`. Multiplying by `r` and using the exact identity `rL_r=r-1` gives `(8)`--`(10)`.

The full-prefix sum is equally elementary:

\[
\sum_{r=2}^{R}L_r
=
\sum_{r=2}^{R}\left(1-\frac1r\right)
=
R-H_R.
\tag{21}
\]

Dividing by the common norm `(19)` proves `(11)`.

Nothing in this argument depends on the limiting constant. For fixed `M`, the `NB-119` control gives the analogous prefix law

\[
\eta_r(f_{M,R})
=
\frac{L_r}{\kappa_MR+O_M(1)}
\tag{22}
\]

uniformly for `2<=r<=R`. `NB-120` only supplies the diagonal passage `M=M(R)->infinity` with a finite limiting cost.

## 3. Growing finite source tests also remain compatible with the prefix

The diagonal construction has one further representation consequence. Since `M(R)->infinity`, for every fixed Nyman generator index `b` there is `R_b` such that

\[
\langle f_R,g_b\rangle=0
\qquad(R\ge R_b).
\tag{23}
\]

Thus the same sequence of full-prefix controls eventually satisfies **every fixed finite collection** of exact Nyman source equations while maintaining `(5)` at all lower cutoffs.

This does not mean that `f_R` satisfies the complete infinite Nyman source law at any finite `R`. Nor does it put `f_R` in the confluent actual-zero power class of `NB-117`. Those distinctions are precisely what survives the kill test. But any proposed obstruction assembled from a growing nested cutoff prefix plus finitely many source equations whose maximal index remains in the `NB-120` mixed-tail regime is still matched by `(4)`--`(6)`.

The comparison with `NB-118` is especially important. That theorem says strong actual-zero target capture forces an **upper** bound of order `1/r` on cell retention after a fixed source baseline is cleared. For the common control here,

\[
\eta_r(f_R)
\asymp R^{-1}
\le O(r^{-1})
\qquad(r\le R),
\tag{24}
\]

and the inequality becomes parametrically stronger when `r=o(R)`. Consequently the widening behavior left open in `NB-121` cannot produce a contradiction by combining the existing inverse-section upper bounds across scales.

## 4. Representation audit and surviving source question

The source state represented here is still the ambient matched-control class, not an actual zeta-zero packet. The control uses only:

1. nested natural-cell projections;
2. nested finite Nyman generator spaces; and
3. the minimum-norm tail repair already constructed in `NB-119`--`NB-120`.

The full-prefix family carries no additional independent coordinate: every visible target equation is the image of the maximal one under a smaller projection. The apparent increase from one cutoff to `R-1` cutoffs is therefore a representation enlargement, not a source enlargement.

This closes the **widening nested-ladder escape as such**. A useful next obstruction must add information that the maximal repair cannot inherit automatically. The live candidates are now narrower: a non-nested or explicitly tail-sensitive compatibility law; a quantitative transition when the Nyman source depth leaves the audited `M^6(1+\log M)<<R` regime; or, most source-faithfully, a theorem using the confluent actual-zero power representation from `NB-117` rather than only its finite Nyman annihilators.

The claim is deliberately limited. No assertion is made that actual zero packets can realize `(5)`, that the full infinite Nyman orthogonality system admits the control, or that the mixed-tail condition is sharp. The result says only that **nested cutoff coherence, even across the entire widening prefix, does not itself distinguish actual-zero packets from the inverse-section matched-control class using the source information currently retained by `NB-118`--`NB-120`.**

## 5. Prior-art and adversarial audit

The abstract identities `Q_rQ_R=Q_r` for nested orthogonal projections and `V_m subset V_M` are elementary Hilbert-space facts; no novelty is claimed for them. A targeted literature check against the classical Báez-Duarte finite approximation framework and searches for simultaneous/nested Nyman finite-section projection results did not reveal a source-specific statement equivalent to `(5)`--`(11)`. No external theorem is load-bearing: the quantitative input is exactly the canonical `NB-120` tail law, while the full-prefix extension is derived above. `SOURCES.md` therefore requires no new dependency.

The main adversarial failure mode is also explicit. Early scales do **not** retain the sharp `1/r` amount; they retain the smaller `1/R` amount. This would invalidate a claim of simultaneous saturation at each scale. It does not invalidate the matched-control test because the actual-zero results being compared against impose upper retention bounds, not lower ones. The theorem therefore claims simultaneous perfect target **angle** and simultaneous compatibility with the known retention constraints, not simultaneous equality in every single-cutoff optimization problem.

A second failure mode would be to silently replace finite/growing Nyman orthogonality by the full infinite source law. Equation `(23)` is only eventual exactness for each fixed generator along the diagonal sequence. Any theorem that couples generator index to cutoff outside the `NB-120` regime, or uses the actual zero-power transformation law, remains outside this control.

The durable conclusion is therefore negative but sharper than `NB-121`: **widening the nested cutoff ladder all the way to the complete prefix does not break the inverse-section repair; it merely redistributes one maximal repair over more visible scales.**
