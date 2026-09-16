# WI-314 — The fixed cap threshold recovers source negative index cofinally

**Status:** `EXACT-DERIVED + CLASSICAL-MINMAX + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

**Parent findings:** WI-236, WI-311, WI-313.

WI-313 identified the moving compensation-floor threshold

\[
-c_\delta=-\frac12+\delta
\]

as a comparison level whose negative spectral count contains the source negative index, with possible false positives from the source window `[0,delta)`. There is a complementary threshold already implicit in the same min--max sandwich that is better aligned with the strict source-sign question.

At the **fixed cap threshold** `-1/2`, the comparison has no false positives at all. It can only miss source-negative modes whose depth is smaller than the current saturation error. Moreover, along any cofinal tail-saturation sequence at one fixed aperture, that one-sided loss vanishes exactly:

\[
\boxed{
\mathcal N_Q(0)
=
\sup_j
\mathcal N_{\widehat{\mathcal D}_j}\!\left(-\frac12\right).
}
\tag{1}
\]

If the fixed-aperture source has finite negative index, the equality is eventually pointwise rather than merely a supremum: every sufficiently saturated comparison has exactly the same count below `-1/2` as the source has below zero.

This removes the `[0,delta)` false-positive problem without requiring a source gap above zero, a bound on positive near-zero spectral density, or any commutation between source and retained tail. The price is one-sided: a finite saturation error can hide a source-negative mode of depth at most `delta`.

That price exposes an important limit-order barrier. Formula (1) requires **cofinal saturation at fixed source aperture**. If the aperture changes while one chooses only a single error `delta_L -> 0`, source-negative margins can shrink faster than `delta_L` and remain invisible at the fixed threshold. Thus tail saturation does not solve the zero-spectral-margin problem isolated by WI-236; it relocates it exactly. Any diagonal aperture/saturation argument needs either a uniform negative-depth theorem, a source-specific estimate on the cap defect along the negative sector, or genuinely cofinal control in the saturation parameter at each fixed aperture.

No new simple-zero percentage or RH proof is claimed. The result is an exact sign-resolution theorem and a no-go for collapsing the aperture and saturation limits using only the scalar cap bounds.

## 1. Abstract capped-tail setup

Fix one outer aperture and let `Q` be the corresponding lower-semibounded closed Hermitian source form on its fixed form domain. Suppose an exact source decomposition has the form

\[
Q=\widehat{\mathcal D}_\delta+\widehat{\mathcal T}_\delta
\tag{2}
\]

with

\[
\left(\frac12-\delta\right)I
\preceq
\widehat{\mathcal T}_\delta
\preceq
\frac12I,
\qquad \delta>0.
\tag{3}
\]

WI-311 constructs such decompositions, for every fixed outer aperture, with

\[
\delta=\frac1{4N}+\frac\epsilon2
\]

and hence with `delta` arbitrarily small using finite smooth real multiwindow families.

Use the same strict variational spectral count as WI-313:

\[
\mathcal N_A(t)
:=
\sup\{\dim V:
A[v]<t\|v\|^2\text{ for every }0\ne v\in V\}.
\tag{4}
\]

No discreteness, compact resolvent, simultaneous diagonalization, or eigenvalue labeling is needed below.

## 2. The cap threshold is a positive perturbation of the source

Define the cap defect

\[
E_\delta:=\frac12I-\widehat{\mathcal T}_\delta.
\tag{5}
\]

The two-sided tail bound (3) is exactly

\[
0\preceq E_\delta\preceq\delta I.
\tag{6}
\]

Adding `I/2` to the comparison in (2) gives the exact identity

\[
\boxed{
\widehat{\mathcal D}_\delta+\frac12I
=Q+E_\delta.
}
\tag{7}
\]

Therefore the comparison sector below the fixed level `-1/2` is the negative sector of the source after adding a positive perturbation of norm at most `delta`:

\[
\mathcal N_{\widehat{\mathcal D}_\delta}\!\left(-\frac12\right)
=
\mathcal N_{Q+E_\delta}(0).
\tag{8}
\]

From (6),

\[
Q\preceq Q+E_\delta\preceq Q+\delta I.
\]

Variational count monotonicity reverses this form order, so

\[
\boxed{
\mathcal N_Q(-\delta)
\le
\mathcal N_{\widehat{\mathcal D}_\delta}\!\left(-\frac12\right)
\le
\mathcal N_Q(0).
}
\tag{9}
\]

This is the `s=0` specialization of WI-313's general shifted-count inequality, but its one-sided sign meaning is different from the moving-floor specialization emphasized there.

The upper inequality in (9) is exact protection against false positives: if `Q` is nonnegative, then

\[
\widehat{\mathcal D}_\delta\succeq-\frac12I
\]

for every admissible capped tail, regardless of `delta`. Source null vectors and positive source modes can never create comparison spectrum **strictly below** `-1/2`.

The lower inequality identifies the only possible miss: a source-negative mode whose depth is less than `delta` may be lifted across zero by `E_delta`.

## 3. Cofinal saturation recovers the complete source negative index

Let `delta_j>0` be any sequence tending to zero, and for every `j` let

\[
Q=\widehat{\mathcal D}_j+\widehat{\mathcal T}_j,
\qquad
\left(\frac12-\delta_j\right)I
\preceq\widehat{\mathcal T}_j
\preceq\frac12I.
\tag{10}
\]

No nesting or continuity of the forms in `j` is assumed.

The elementary variational identity

\[
\boxed{
\sup_j\mathcal N_Q(-\delta_j)=\mathcal N_Q(0)
}
\tag{11}
\]

holds for every such cofinal sequence. To see this without spectral discreteness, take any finite-dimensional subspace `V` counted by `N_Q(0)`. On the unit sphere of `V`, the restricted quadratic form is continuous and strictly negative; compactness gives an `eta_V>0` with

\[
Q[v]\le-\eta_V\|v\|^2
\qquad(v\in V).
\tag{12}
\]

For some `j`, `delta_j<eta_V`, so the same `V` is counted by `N_Q(-delta_j)`. This proves (11), including the infinite-index case in the usual variational sense by testing arbitrary finite dimensions.

Taking suprema in (9) and using (11) yields

\[
\boxed{
\mathcal N_Q(0)
=
\sup_j
\mathcal N_{\widehat{\mathcal D}_j}\!\left(-\frac12\right).
}
\tag{13}
\]

Thus a cofinal saturated capped-tail family recovers the source negative index exactly at one **fixed** comparison threshold.

There is an especially clean finite-index corollary. If

\[
n_-(Q)=\mathcal N_Q(0)=n<\infty,
\]

then an `n`-dimensional negative subspace has some uniform margin `eta>0` by the same finite-dimensional compactness argument. Hence for every sufficiently large `j`, `delta_j<eta`, and (9) squeezes

\[
\boxed{
\mathcal N_{\widehat{\mathcal D}_j}\!\left(-\frac12\right)=n.
}
\tag{14}
\]

At fixed aperture the capped comparison therefore does not merely approximate source inertia: sufficiently strong saturation reproduces it exactly below `-1/2`.

## 4. Fixed cap and moving floor give complementary one-sided errors

For comparison, define

\[
c_\delta:=\frac12-\delta,
\qquad
S_\delta:=\widehat{\mathcal T}_\delta-c_\delta I.
\]

Then

\[
0\preceq S_\delta\preceq\delta I,
\qquad
\widehat{\mathcal D}_\delta+c_\delta I
=Q-S_\delta.
\tag{15}
\]

This is a **negative** perturbation of the source, and WI-313 obtains

\[
\boxed{
\mathcal N_Q(0)
\le
\mathcal N_{\widehat{\mathcal D}_\delta}(-c_\delta)
\le
\mathcal N_Q(\delta).
}
\tag{16}
\]

Combining (9) and (16) gives a two-threshold bracket using the same comparison:

\[
\boxed{
\mathcal N_{\widehat{\mathcal D}_\delta}\!\left(-\frac12\right)
\le
\mathcal N_Q(0)
\le
\mathcal N_{\widehat{\mathcal D}_\delta}\!\left(-\frac12+\delta\right).
}
\tag{17}
\]

The two sides have opposite failure modes:

- the fixed cap `-1/2` has **no false positives**, but may miss source-negative spectrum in `[-delta,0)`;
- the moving floor `-1/2+delta` has **no false negatives** for strictly negative source directions, but may add source spectrum in `[0,delta)`.

In particular, source kernel at zero contaminates the moving-floor count in general but never contaminates the strict fixed-cap count. Therefore shrinking `delta` does not require any positive-side source gap in order for (13) to recover strict negative index.

## 5. Exact positivity criterion at fixed aperture

Equation (13) immediately gives a fixed-aperture criterion. For **any** cofinal family satisfying (10),

\[
\boxed{
Q\succeq0
\quad\Longleftrightarrow\quad
\mathcal N_{\widehat{\mathcal D}_j}\!\left(-\frac12\right)=0
\text{ for every }j.
}
\tag{18}
\]

The forward implication follows directly from (7), because `E_j` is positive. For the reverse implication, if `Q` had any negative variational direction, (13) would make the fixed-threshold comparison count positive for some sufficiently saturated member of the family.

This is **not** an RH proof and should not be read as independent positivity information. WI-311 already warns that saturation sends `Dhat` toward `Q-I/2` in bounded-form norm. Equation (18) makes the sign content of that convergence exact at the inertia level. Its value is to identify a comparison statistic with no positive-source contamination and to state precisely what a future finite-sector estimate must control.

## 6. A diagonal aperture/saturation schedule is not enough

The order of limits in (13) is load-bearing. The source form `Q` is held fixed while `delta -> 0`.

Suppose instead that an outer-aperture parameter `L` changes the source form to `Q_L`, and one chooses only one saturation error `delta_L -> 0` at each aperture. The scalar cap information alone cannot guarantee detection of source negativity. A one-dimensional exact countermodel already shows this.

Choose any `delta_L>0` and put

\[
Q_L=-\frac{\delta_L}{2}I,
\qquad
\widehat{\mathcal T}_L=\left(\frac12-\delta_L\right)I.
\tag{19}
\]

Then (3) holds exactly, but

\[
\widehat{\mathcal D}_L
=Q_L-\widehat{\mathcal T}_L
=-\frac12I+\frac{\delta_L}{2}I.
\tag{20}
\]

Hence

\[
\mathcal N_{Q_L}(0)=1,
\qquad
\mathcal N_{\widehat{\mathcal D}_L}\!\left(-\frac12\right)=0
\tag{21}
\]

for every `L`, even though `delta_L -> 0`.

Thus the implication

\[
\delta_L\to0
\text{ and no comparison spectrum below }-1/2
\quad\Longrightarrow\quad
Q_L\succeq0
\]

is false when the source itself changes with `L`. A negative source margin can collapse faster than the chosen saturation scale.

This countermodel does **not** claim that the actual WI-311 multiplier attains the lower scalar floor on a zeta-negative vector. It proves the sharper methodological point: no argument using only the order interval (3) and one diagonal sequence can exclude that possibility. To beat the countermodel one needs additional source-tail alignment information.

A sufficient replacement would be any one of the following genuinely stronger inputs: a uniform lower bound on the depth of every relevant negative source direction along the aperture family; a vectorwise estimate showing the actual cap defect `E_L` is smaller than that negative depth on the source-negative sector; or cofinal control of the fixed-threshold comparison at each fixed aperture before the aperture limit is taken.

## 7. Relation to the Bombieri zero-margin barrier

WI-236 reconstructed Bombieri's finite-truncation inertia theorem and showed that negative index itself is not the missing persistence statement. The escape is spectral: negative eigenvalues can approach zero while coefficient mass moves outward.

The diagonal countermodel (19)--(21) is the capped-tail analogue of exactly that zero-margin phenomenon. Saturation can make the comparison arbitrarily close to `Q-I/2`, but if the relevant source-negative depth is simultaneously allowed to go to zero, a prescribed saturation schedule need not resolve its sign.

Accordingly, the present finding **removes one apparent obstacle but not the real one**:

- positive source spectrum near zero is not an obstruction if the fixed cap threshold is used and saturation is cofinal at fixed aperture;
- collapsing the source-negative margin across changing apertures remains a genuine obstruction, and scalar tail saturation alone does not control it.

This is why (13) should not be turned into a claim that the capped-tail construction has solved the finite-to-global Weil problem. It gives an exact local index-recovery mechanism; WI-236 still governs the difficult passage when the source itself changes.

## 8. Prior art and novelty audit

The abstract ingredient in (9)--(14) is classical min--max monotonicity for ordered self-adjoint forms and the standard stability of spectral sublevels under bounded self-adjoint perturbations. A convenient source is Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, 2nd ed., AMS GSM 157 (2014), Chapter 4. Kato's perturbation theory contains the broader classical bounded-perturbation framework. No novelty is claimed for those operator-theoretic facts.

For the Weil side, Bombieri's 2000 memoir is the primary classical source for finite negative-index information and the possibility of negative eigenvalues collapsing toward zero in the passage to the infinite problem. WI-236 already audits the exact scope of that result.

A targeted search around Weil quadratic forms, capped/clipped localization tails, fixed shifted spectral thresholds, and bounded-perturbation index recovery located the classical min--max/perturbation theory and Bombieri's finite-inertia program, but no prior source stating (13) for the source-exact capped-tail decomposition constructed in WI-311. Search absence is not a priority claim. The durable Mathia contribution asserted here is the exact internal deduction, the distinction between the fixed-cap and moving-floor thresholds, and the diagonal-limit obstruction.

No external unproved zeta statement is used. Equations (9)--(18) follow only from the exact WI-311 source split plus the classical variational principle.

## 9. Stress tests and falsification boundary

Several points are essential.

**Strict threshold.** The count at `-1/2` is strict. A source null vector can map exactly to the threshold when the retained tail saturates the cap, but it is not counted. This is necessary for (9) to represent strict source negativity rather than nonpositivity.

**Fixed aperture before saturation.** Equation (13) is false if `Q` changes with `j`; Section 6 gives an exact one-dimensional counterexample. Any use in an aperture limit must preserve this quantifier order or add a new uniform margin theorem.

**No commutation.** Neither (9) nor (13) assumes that `Q`, `T_delta`, or `E_delta` commute. Everything is form order and finite-dimensional compactness inside variational subspaces.

**No discrete-spectrum hypothesis.** The supremum identity (11) is variational. Discreteness is useful only for the stronger language of individual eigenvalues; it is not needed for index recovery.

**No free arithmetic gain.** The theorem does not make the fixed-threshold comparison easier to bound. A proof that `Dhat >= -I/2` for a cofinal family must come from an independent source-valid argument. Otherwise (18) is only an exact reformulation of source positivity.

**No percentage update.** Nothing here changes the unconditional simple-critical-zero lower bound. The result belongs to the README's defect-elimination objective: it specifies an exact sign-resolving comparison invariant and closes the scalar-order version of a diagonal saturation shortcut.

## Research consequence

For the capped-tail branch, the natural strict-sign observable is now

\[
\boxed{
\mathcal N_{\widehat{\mathcal D}}(-1/2),
}
\]

not total negative index and not necessarily the moving-floor count. At a fixed aperture, one cofinal smooth saturation family recovers the complete source negative index through (13), with no contamination from source kernel or positive near-zero spectrum.

The next substantive theorem must therefore do one of two things: control this fixed `-1/2` comparison sector uniformly enough to survive cofinal saturation, or supply source-specific cap-defect/margin information that justifies a coupled aperture/saturation limit. Merely choosing `delta_L -> 0` while the aperture grows is decisively insufficient by (19)--(21).