---
id: WP-403
title: Finite-codimensional source constraints cannot create fixed-shadow orientation
branch: weil_positivity
status: supported
kind: cstar-hereditary-source-fixed-shadow-finite-codimension-linear-constraint-orientation-obstruction
claim_strength: exact RH-independent extension of WP-401--WP-402 removing cutoff-stability for closed finite-codimensional source slices; every closable Banach-valued linear response defined on the whole slice and oriented only by fixed-shadow positivity is zero
created: 2026-09-22
related: [WP-399, WP-400, WP-401, WP-402]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - B. Blackadar, Operator Algebras: Theory of C*-Algebras and von Neumann Algebras, Springer (2006), hereditary C*-subalgebras and approximate units
  - T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer, Chapter III section 5, closed and closable operators
---

# WP-403 — Finite-codimensional source constraints cannot create fixed-shadow orientation

## Claim

`WP-402` leaves a precise linear escape: a source relation might fail the canonical cutoff invariance

\[
k\mapsto f_n(d)k f_n(d)
\]

and thereby avoid the explicit graph-defect sequence used there. A natural way for this to happen is to impose a finite list of global moment, normalization, balance, or matching constraints that the local cutoffs do not preserve.

That is still insufficient.

Let `A` be a C-star algebra, `B subseteq A` a C-star subalgebra, and

\[
E:A\to B
\]

be a conditional expectation. Fix `d in B_+`, set

\[
H_d=\operatorname{Her}_A(d)=\overline{dAd},
\qquad
V_d=\{k\in(H_d)_{\rm sa}:E(k)=0\},
\tag{1}
\]

and define the order-bounded tangent core

\[
\mathcal P_d
 =\{h\in V_d:\text{ for some }M<\infty,\ -Md\le h\le Md\}.
\tag{2}
\]

Let `F subseteq V_d` be a **closed real linear subspace of finite codimension**. No invariance of `F` under the canonical cutoffs is assumed.

Let `Y` be a real Banach space with pointed cone `C`,

\[
C\cap(-C)=\{0\},
\tag{3}
\]

and let

\[
T:F\to Y
\tag{4}
\]

be linear and closable for the inherited C-star norm on `F` and the norm topology of `Y`. Suppose fixed-shadow positivity is required to orient the response:

\[
d+h\ge0,\ h\in F
\quad\Longrightarrow\quad
T(h)\in C.
\tag{5}
\]

Then

\[
\boxed{T=0\text{ on }F.}
\tag{6}
\]

In particular, if

\[
F=V_d\cap\bigcap_{j=1}^m\ker \ell_j
\tag{7}
\]

for finitely many continuous real linear source observables `ell_j`, then no nonzero closable linear response on the whole constrained slice can acquire a pointed orientation from `d+h>=0`, even when the individual constraints are destroyed by every canonical cutoff.

The new point relative to `WP-402` is exactly the removal of cutoff stability. Finite-codimensionality lets one repair the cutoff approximants inside the constraints while retaining order-bounded two-sided tangency.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CSTAR-HEREDITARY-SOURCE-CORNER + CONDITIONAL-EXPECTATION + FINITE-CODIMENSIONAL-SOURCE-SLICE + NO-CUTOFF-INVARIANCE + ORDER-BOUNDED-TANGENT-CORE + BANACH-VALUED-LINEAR-READOUT + POINTED-CONE-ORIENTATION + CLOSABILITY + MATCHED-CONTROL-UNIVERSAL + SOURCE-NONLOCALITY-THRESHOLD + NOT-A-WEIL-BRIDGE`.

## 1. The order-bounded tangent core is dense before imposing extra constraints

The continuous cutoffs from `WP-401` are

\[
f_n(t)=\min(1,nt),
\qquad
c_n=f_n(d).
\tag{8}
\]

For every `k in V_d`, conditional-expectation bimodularity gives

\[
E(c_nkc_n)=c_nE(k)c_n=0,
\tag{9}
\]

so `c_nkc_n in V_d`. The hereditary approximate-unit calculation gives

\[
c_nkc_n\longrightarrow k
\quad\text{in norm},
\tag{10}
\]

while the same order estimate used in `WP-401` gives

\[
-n\|k\|d\le c_nkc_n\le n\|k\|d.
\tag{11}
\]

Hence every cutoff approximant lies in `mathcal P_d`, and therefore

\[
\overline{\mathcal P_d}=V_d.
\tag{12}
\]

The set `mathcal P_d` is a real linear subspace: order bounds add and scale. It is generally not norm closed, which is exactly why a global source relation can fail to be literally cutoff stable while still being densely approximated by order-bounded directions.

## 2. Finite codimension forces the dense tangent core to survive the constraints

Let

\[
q:V_d\to V_d/F
\tag{13}
\]

be the quotient map. Because `mathcal P_d` is dense in `V_d`, its image `q(mathcal P_d)` is dense in the quotient. But `V_d/F` is finite dimensional, and every linear subspace of a finite-dimensional normed space is closed. Therefore

\[
q(\mathcal P_d)=V_d/F.
\tag{14}
\]

Choose elements `u_1,...,u_r in mathcal P_d` whose quotient classes form a basis of `V_d/F`, and let

\[
S:V_d/F\to\mathcal P_d
\tag{15}
\]

be the corresponding linear section of `q`. Since its domain is finite dimensional, `S` is automatically continuous.

Now fix `k in F`. By (12), choose `p_n in mathcal P_d` with

\[
p_n\to k.
\tag{16}
\]

Then `q(p_n)->0`. Define

\[
z_n=p_n-S(q(p_n)).
\tag{17}
\]

Because `mathcal P_d` is linear, `z_n in mathcal P_d`; because `qS` is the identity,

\[
q(z_n)=0,
\]

so `z_n in F`. Continuity of `S` and `q(p_n)->0` give

\[
z_n\longrightarrow k.
\tag{18}
\]

Thus

\[
\boxed{\overline{F\cap\mathcal P_d}=F.}
\tag{19}
\]

This is the entire finite-codimensional mechanism. The canonical cutoffs themselves need not preserve `F`: only finitely many quotient errors have to be corrected, and a fixed finite-dimensional family of order-bounded directions repairs them with vanishing norm cost.

## 3. Every constrained order-bounded direction has both positive signs

Take `z in F intersect mathcal P_d`. By definition there is `M<infinity` with

\[
-Md\le z\le Md.
\tag{20}
\]

For every `0<epsilon<=1/M` when `M>0`,

\[
d+\varepsilon z\ge0,
\qquad
d-\varepsilon z\ge0.
\tag{21}
\]

Both `+epsilon z` and `-epsilon z` lie in `F`. Applying (5) to both signs gives

\[
\varepsilon T(z)\in C,
\qquad
-\varepsilon T(z)\in C.
\tag{22}
\]

Pointedness of `C` forces

\[
T(z)=0.
\tag{23}
\]

Hence `T` vanishes on the dense subspace `F intersect mathcal P_d`.

## 4. Closability kills the remaining constrained directions

Fix arbitrary `k in F` and choose `z_n in F intersect mathcal P_d` with `z_n->k` from (19). Put

\[
r_n=k-z_n.
\tag{24}
\]

Then `r_n in F`, `r_n->0`, and by (23)

\[
T(r_n)=T(k)-T(z_n)=T(k)
\qquad\text{for every }n.
\tag{25}
\]

Thus `T(r_n)` converges to `T(k)`. The graph criterion for closability now forces `T(k)=0`. Since `k` was arbitrary, (6) follows.

This argument does not smuggle cutoff invariance back into the hypotheses. The approximants `z_n` are corrected combinations of cutoff-bounded directions and need not equal `c_nkc_n` or arise from any source endomorphism preserving `F`.

## 5. What finite global constraints therefore cannot do

Equation (7) covers the most immediate attempt to manufacture source-nonlocality by adding finitely many continuous global observables. Examples include a finite collection of moment conditions, normalization constraints, finite matching conditions between sectors, or finitely many linear balance laws. Such constraints can certainly be broken by the individual localizations `k -> c_nkc_n`; that fact alone is now shown to be too weak.

The reason is structural rather than arithmetic. A finite-dimensional quotient cannot keep the dense order-bounded tangent core away from the constrained fibre. Every finite quotient error can be repaired inside that core, and fixed-shadow positivity still sees two signs densely enough that any closable linear orientation collapses.

Consequently a surviving linear source relation must be more nonlocal than a finite list of continuous constraints. At least one additional feature is necessary: an infinite-codimensional restriction for which the order-bounded core no longer intersects densely, a nonclosed or singular domain, a nonclosable response, a one-sided admissible set rather than a linear slice, or a change to nonlinear/quadratic or genuinely finite--archimedean global geometry.

The theorem does **not** say that every infinite-codimensional relation escapes. Many such relations remain cutoff stable and are already covered by `WP-400`--`WP-402`. Finite codimension is a sufficient no-go criterion, not a characterization of all source-local relations.

## 6. Relation to the Bost--Connes completion fork

The accepted Bost--Connes clue asks for a source-forced completion of the critical divisibility Gram whose own geometry supplies the missing Weil orientation. After `WP-402`, one live wording was that a global relation could deliberately fail the hereditary cutoffs and thereby preserve a cross-scale quantity lost by localization.

`WP-403` separates genuine cross-scale structure from a cheap version of that idea. If the proposed relation is just the common kernel of finitely many continuous source observables, then even complete failure of literal cutoff invariance does not matter: the constrained slice still contains a dense set of two-sided positive tangents. No closable linear pointed-cone readout on that slice can carry the missing sign.

This is a useful falsification gate for proposed finite--archimedean assemblies. Merely coupling the finite source to finitely many extra scalar normalization coordinates or imposing finitely many global linear matching equations does not create an orientation theorem of the required type. A successful assembly must make those additional sectors alter the geometry in a genuinely infinite-dimensional, one-sided, nonlinear, or otherwise non-slice-like way.

As in `WP-399`--`WP-402`, no prime arithmetic enters the proof. The same finite-codimensional obstruction holds for matched non-Riemann controls with the same hereditary fixed-shadow geometry. It therefore cannot itself be the desired arithmetic sign mechanism; it only removes another generic false exit.

## 7. Prior-art and novelty audit

The operator-algebra input is standard: a positive generator of its hereditary C-star algebra supplies the continuous approximate-unit localization used in `WP-401`, and the graph criterion for closable linear operators is classical. The additional functional-analysis step is elementary: a dense linear subspace maps densely to a finite-dimensional quotient, hence surjectively, and a finite-dimensional linear section is continuous.

A bounded literature search around hereditary C-star approximate units, finite-codimensional Banach subspaces, conditional expectations, positive cones, and Bost--Connes positivity found the standard ingredients and general finite-codimensional Banach-space literature, but no source identifying this specific fixed-shadow completion obstruction. No external novelty is claimed for the abstract density lemma. The research delta is its use to remove **cutoff stability itself** from a concrete class of source relations left open by `WP-402`.

The result is therefore classified as an exact derived obstruction, not as a new general theorem of Banach-space or C-star theory.

## 8. Boundaries and decisive audit test

Closed finite codimension is essential to the present proof. For an infinite-dimensional quotient, the dense linear space `q(mathcal P_d)` can be a proper nonclosed subspace, and the finite-dimensional correction argument breaks. This is exactly where a genuinely global relation could begin to retain information that every order-bounded localization loses.

The theorem also assumes that `T` is defined on the whole closed slice `F`. A genuinely unbounded response may instead come with a proper dense operator domain inside `F`; unless that domain contains enough of `F intersect mathcal P_d`, the argument does not apply. Likewise, nonlinear energies, quadratic forms, one-sided cones of admissible perturbations, and completions in which the finite and archimedean variables transform together are outside the claim.

The decisive audit for a proposed linear escape is now concrete. First identify the closed source slice around the fixed shadow. If it differs from `V_d` by only finitely many continuous linear constraints, (19) supplies dense order-bounded two-sided tangents regardless of cutoff invariance, and any everywhere-defined closable pointed-cone response is zero. To escape, the proposal must exhibit the genuinely infinite-dimensional or singular datum that prevents this repair, rather than merely state that a cutoff violates one global constraint.

`WP-403` does not establish Weil positivity or a Bost--Connes completion. It sharpens the surviving category boundary: **finite-dimensional global memory cannot by itself turn fixed-shadow positivity into a linear orientation.**
