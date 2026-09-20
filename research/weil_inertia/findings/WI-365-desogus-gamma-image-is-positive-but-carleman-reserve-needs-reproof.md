# WI-365 — Desogus's gamma image is positive, but safe dropping does not transport the bare Carleman reserve

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + REPAIR-REDIRECT + RESERVE-PROVENANCE-GATE + NON-ESTABLISHED-RH`.

## Claim

The nonlocal odd-parity image channel isolated in WI-364 is **positive semidefinite**. Consequently it is not, by itself, an obstruction to a lower-form proof of localized Weil positivity: it may be rigorously discarded in the lower-bound direction. This resolves one of the explicit repair branches left open by WI-364.

There is, however, a separate load-bearing consequence for Marco Desogus's 17 September 2026 preprint **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367v1`). The preprint's quantitative Carleman/OSPR reserve is computed for the normalized bare Carleman kernel `K(u,v)=1/(u+v)`. After the exact odd fold of the actual archimedean block, the positive image channel is instead

\[
\boxed{
J_A:=\frac12K_{\rm Carl}+A R_{\rm sum},
}
\tag{1}
\]

with kernel

\[
\boxed{
j_A(u,v)
=\frac{1}{2(u+v)}+A\rho(A(u+v))
=A\frac{e^{-A(u+v)/2}}{1-e^{-2A(u+v)}}.
}
\tag{2}
\]

Thus the repair `J_A\succeq0`, followed by dropping `J_A`, is legitimate for proving a lower bound, but it does **not** also justify carrying forward the numerical rebound previously derived for the bare normalized Carleman block. Equality provenance and lower-form provenance must be kept separate. If the later induction needs that printed reserve, a repaired proof must either derive an exact normalization/comparison that supplies it from the true image channel (or another exact positive channel), or recompute an appropriate `A`-dependent reserve.

This finding therefore changes the audit diagnosis in a useful way. The missing gamma image of WI-364 is benign for **sign** but remains load-bearing for **quantitative reserve provenance**. The independent diagonal transport defect `W_A` from WI-363 is still unresolved and cannot be repaired merely by positivity of `J_A`.

## 1. Exact positive image channel

WI-364 derives the canonical odd fold of the complete archimedean nonlocal terms. With

\[
\rho(z)=\frac{e^{-z/2}}{1-e^{-2z}}-\frac1{2z},
\]

and with `B` denoting the normalized collar form, the folded archimedean block has the exact structure

\[
F(H_{\rm Leg}+c_0(A)I+V-K_{\gamma,A})F^*
=
B+c_0(A)I-A R_{\rm diff}+J_A,
\tag{3}
\]

where `R_diff` has kernel `rho(A|u-v|)` and `J_A` is (1). Equation (2) follows immediately by inserting the definition of `rho`:

\[
\frac1{2t}+A\rho(At)
=A\frac{e^{-At/2}}{1-e^{-2At}},
\qquad t=u+v>0.
\tag{4}
\]

Now expand the denominator geometrically. On a smooth compactly supported core in `(0,1)`,

\[
j_A(u,v)
=A\sum_{m\ge0}
 e^{-A(2m+1/2)u}
 e^{-A(2m+1/2)v}.
\tag{5}
\]

Therefore, for every test vector `f`,

\[
\boxed{
\langle f,J_Af\rangle
=A\sum_{m\ge0}
\left|
\int_0^1 e^{-A(2m+1/2)u}f(u)\,du
\right|^2
\ge0.
}
\tag{6}
\]

The identity first holds on the compactly supported core, where all interchanges are elementary; the nonnegative partial sums then give the corresponding closed-form statement. This is the same positivity that WI-364 sees after inverse exponential transport from the product-Hankel expansion

\[
P(X,Y)
=\frac{XY}{X^2Y^2-1}
=\sum_{m\ge0}X^{-(2m+1)}Y^{-(2m+1)}.
\tag{7}
\]

No numerical certificate or conjectural input is involved.

## 2. The exact lower-form repair

Equation (6) gives the rigorous order comparison

\[
\boxed{
F(H_{\rm Leg}+c_0(A)I+V-K_{\gamma,A})F^*
\succeq
B+c_0(A)I-A R_{\rm diff}.
}
\tag{8}
\]

Hence the image channel does not have to be cancelled in order to obtain a lower-form estimate. It may be retained as positive reserve or simply discarded. This sharpens the repair criterion in WI-364: the mere fact that Proposition 5.3 does not display the image term is not enough to conclude that the desired positivity inequality fails.

It remains incorrect to erase `J_A` inside a claimed **unitary equality**. Proposition 5.3 presents a complete-form transport, not merely the inequality (8). The exact source-to-cell identity must still contain `J_A` or an exactly equivalent nonlocal term. What (8) supplies is a possible repaired proof strategy: weaken equality to the lower-form comparison that the positivity theorem actually needs.

## 3. Why the printed bare-Carleman rebound does not come for free

Section 4 of `arXiv:2609.20367v1` introduces the normalized Carleman operator

\[
(Kf)(u)=\int_0^1\frac{f(v)}{u+v}\,dv
\tag{9}
\]

and derives explicit OSPR quantities from that particular operator, including the printed constant

\[
d_*=0.4934219\ldots
\tag{10}
\]

and the positive numerical reserve used later in the local/profile bookkeeping. The paper subsequently cites the Carleman/OSPR calculation as part of the strict reserve available to the induction.

The exact physical odd-fold image after the regular gamma correction is not (9); it is `J_A` in (1)--(2). The elementary implication

\[
J_A\succeq0
\tag{11}
\]

contains no quantitative comparison of `J_A` with the normalized `K` strong enough to transport the OSPR constant (10). In particular, the lower-bound maneuver

\[
J_A\mapsto0
\tag{12}
\]

spends none of the channel negatively, but it also retains none of its positive rebound. One cannot both discard `J_A` to repair the source-to-cell lower bound and, without an additional theorem, continue to book a positive constant computed for another operator.

This is a provenance statement, not a claim that the printed OSPR reserve is false. A valid repair may still exist. For example, it could derive an exact decomposition in which a correctly normalized copy of `K` survives elsewhere, prove a Loewner/form comparison between `J_A` and the required normalized block, or redo the OSPR calculation directly for the `A`-dependent kernel (2). Version 1 does not provide such a bridge in the transport step audited by WI-363--WI-365.

## 4. Separation from the diagonal defect

The positive image result does not remove WI-363's multiplication correction. The half-density transport of the singular Cauchy difference form produces the explicit nonconstant potential `W_A`. The two effects have different operator type:

\[
J_A\quad\text{is a nonlocal positive Hankel operator},
\qquad
W_A\quad\text{is multiplication}.
\tag{13}
\]

Dropping `J_A` in the lower-form direction therefore leaves the diagonal bookkeeping problem untouched. A repaired source-to-cell proof still has to transform the scalar/endpoint pieces on a common core and show that their exact multiplier cancels or dominates the surviving `W_A` with the normalization needed downstream.

This also prevents a false repair by accounting convention. Positivity of a missing nonlocal term can justify omission from a **lower bound**; it cannot manufacture the missing diagonal identity, nor can it certify a quantitative reserve belonging to a different normalized operator.

## 5. Relevance to the research mandate

The Desogus preprint is being audited because it claims precisely the kind of source-exact, cofinal defect-elimination mechanism sought by the `weil_inertia` mandate. WI-362 found that the later common-cut/inherited-pivot algebra is internally consistent once the normalized one-cell model is granted. WI-363 and WI-364 then exposed two independent gaps in the provenance of that model.

The present result narrows rather than broadens the obstruction. The gamma-image defect is **not** a new negative direction: its exact sign is favorable. The highest-value unresolved source-level gate is consequently more specific:

\[
\boxed{
\text{derive a correct lower-form source-to-cell transport with the diagonal term controlled,}
}
\tag{14}
\]

and, separately, if the global induction really needs the printed Carleman/OSPR surplus,

\[
\boxed{
\text{prove that the exact surviving positive channel supplies the quantitatively booked reserve.}
}
\tag{15}
\]

Until those two statements are established, the preprint's RH conclusion remains outside Mathia's established evidence base and the numerical certificate replay remains downstream of an unresolved analytic normalization gate.

## 6. Prior-art and novelty audit

Primary source: Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, submitted 17 September 2026, especially the normalized Carleman/OSPR calculation in Section 4, the localized odd operator and Cauchy--Carleman transport in Section 5, and the later use of the local/profile reserve.

A fresh targeted search on 20 September 2026 located the primary submission and generic listings/mirrors but no independent technical discussion settling this image-channel normalization issue. Absence from that search is not evidence of priority or of absence from the literature.

The rank-one expansion (5)--(6) is elementary Hankel/Laplace algebra and is not claimed as a new general theorem. Mathia's durable contribution here is source-specific: it resolves an explicit repair question left by WI-364 and separates a harmless positive omission in a lower bound from the still-unproved provenance of the quantitative reserve used by the claimed induction.

## 7. Failure modes and falsification test

This finding would need correction if the odd-fold sign or coefficient in WI-364 were wrong; direct expansion of the odd restriction of `K_{gamma,A}` is the first falsification check. The reserve-provenance gate would also disappear if an independent exact derivation exhibited a separate physical channel equal, with the required normalization, to the bare `K` used by the OSPR calculation, or proved a sufficiently strong form comparison from `J_A` to that block.

The finding does **not** assert that Desogus's main theorem is false, that `J_A` is the only possible source of positive reserve, that the bare-Carleman OSPR inequalities are themselves wrong, or that no corrected `A`-dependent OSPR estimate can work. It establishes only the exact positivity (6), the safe lower-form deletion (8), and the no-double-spend/provenance requirement that a discarded channel cannot simultaneously supply an unproved quantitative reserve.

## Consequence for the research line

The next analytic pass should not spend effort trying to turn the gamma image into a contradiction. Its sign is settled and favorable. The priority is the complete **diagonal** source-to-cell transport: reconstruct the transformed scalar/endpoint terms together with `W_A` and determine whether they yield the required lower collar model. If that succeeds, the following gate is to connect whatever exact positive channel survives to the numerical Carleman/OSPR reserve actually used by the induction. Only after those analytic bridges are closed does independent replay of the `Y=7` base and MASTER certificates become probative for the claimed RH chain.