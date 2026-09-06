# PF-183 — disjoint thick collar slabs remove multiplicity from the remaining Schatten splice budget

**Status:** `EXACT-DERIVED + CONDITIONAL-REDUCTION + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-177 controls every PF-138 collapsing short-collar core in an exact area coordinate, while PF-179--PF-182 assemble an exact-area body/split/cusp/decomposition-seam comparison whose remaining defect is the insertion of those true short-collar gauges. The infinite number of short collars does **not** create an additional counting obstruction for the `S_r`, `r>1`, route once the splice is confined to a fixed thick subslab of each standard collar. Such subslabs are pairwise disjoint, their inverse-unit-ball weights are uniformly bounded, and the already assembled body map has finite global unweighted `L^r` metric defect for every `r>1`. Consequently an **energy-local** conservative splice estimate on one normalized thick annulus would automatically sum over the complete PF-138 family. The unresolved issue is therefore local and quantitative: construct an exact-area splice whose `L^r` cost is controlled by the metric energy already present on that slab, rather than charging each short collar a fresh fixed-area cost based only on a pointwise `O(p^{-1})` body bound. PF-183 does not prove that local splice theorem, the complete PF-175 weighted hypothesis, any Schatten conclusion, scattering equivalence, or RH consequence.

## Claim

Let `X` be the exact prime flute and `X_+` its exact all-composite shift clone. Let

\[
F_{\mathrm{body}}:X\longrightarrow X_+
\tag{1}
\]

be the exact-area body comparison obtained by combining the PF-179 Lambert transports, PF-180 split synchronization, PF-181 cusp handoff, and PF-182 decomposition-cuff smoothing, before replacing its behavior on the PF-138 true short-collar cores.

For every fixed `r>1`, the source- and target-side **unweighted** metric-deviation energies of this assembled body stage are finite:

\[
\boxed{
\int_X \delta_{\mathrm{body}}^r\,d\mu_X
+
\int_{X_+}\delta_{\mathrm{body}}^{+,r}\,d\mu_{X_+}
<\infty.
}
\tag{2}
\]

Here the target term is the corresponding deviation for the inverse comparison. Equation (2) is not the PF-175 weighted hypothesis; its use below is only on uniformly thick sets.

Let `\mathcal S` be the complete PF-138 tail family of Margulis-short closed cores in the prime metric. For `\eta\in\mathcal S`, write

\[
L_\eta=\ell(\eta),
\qquad
L_\eta^+=e^{t_\eta}L_\eta,
\qquad
|t_\eta|=O(P_\eta^{-3}),
\tag{3}
\]

with `P_eta` the PF-138 left exterior prime scale. In the exact PF-177 area coordinates on the matched standard collars,

\[
\boxed{
x=L_\eta\sinh r,
\qquad
X=L_\eta^+\sinh r_+,
\qquad
d\mu=dx\,d\theta,
\qquad
d\mu_+=dX\,d\theta.
}
\tag{4}
\]

After discarding a finite head, both matched collars contain the fixed subcollar `|x|,|X|\le 5/4`. On that subcollar define the marked area-coordinate comparison

\[
\boxed{
G_\eta(x,\theta)=(x,\theta),
}
\tag{5}
\]

where the angular origin is the PF-142 zero-twist marking. Then `G_eta` preserves area exactly and, uniformly in the collapsing core length,

\[
\delta_{G_\eta}(x)
\le
C|t_\eta|\frac{L_\eta^2}{x^2+L_\eta^2}.
\tag{6}
\]

In particular PF-177/PF-138 give, for every `r>=1`,

\[
\boxed{
\sum_{\eta\in\mathcal S}
\int_{|x|\le5/4}
W_X\,\delta_{G_\eta}^r\,d\mu_X
<\infty,
}
\tag{7}
\]

and the analogous target-side estimate.

Now put

\[
T_\eta:=\{1\le |x|\le5/4\}\subset C_\eta.
\tag{8}
\]

Then the following two facts are exact.

1. The `T_eta` are pairwise disjoint.
2. There is an absolute constant `C` such that
   \[
   \boxed{W_X\le C\quad\text{on every }T_\eta,}
   \tag{9}
   \]
   and likewise on the matched target slabs.

Consequently the existing body energy is charged **only once** over the entire infinite transition family:

\[
\boxed{
\sum_{\eta\in\mathcal S}
\int_{T_\eta}W_X\,\delta_{\mathrm{body}}^r\,d\mu_X
\le
C\int_X\delta_{\mathrm{body}}^r\,d\mu_X
<\infty.
}
\tag{10}
\]

The target-side analogue follows from the inverse comparison.

Therefore fix `r>1`. Suppose one proves the following **uniform local conservative splice lemma** on these normalized thick slabs: for every tail collar there is an exact-area replacement which equals `G_eta` on `|x|<=1`, equals `F_body` outside `|x|>=5/4`, and whose source- plus target-side weighted `L^r` metric cost in the transition zone is bounded by

\[
\boxed{
E_r(\operatorname{splice}_\eta;T_\eta)
\le
C_r\left(
E_r^{\mathrm{body}}(T_\eta)
+|t_\eta|^r
\right),
}
\tag{11}
\]

with `C_r` independent of `eta`. Here `E_r^{body}` includes the corresponding inverse/target term after the same fixed-thickness normalization.

Then summing (11) over `eta`, using (7), (10), and PF-138's already summable `t_eta` family, gives a finite total splice cost for every `r>1`. Thus **no additional short-collar multiplicity estimate is needed after (11)**. Together with the already controlled cusp and decomposition-seam modules, the remaining weighted `S_r` geometry is reduced to this fixed-domain local splice estimate and its exact-area compatibility.

The statement is deliberately conditional at (11). PF-183 proves the global energy accounting that follows from such a local theorem; it does not assume the theorem itself.

## 1. Why the assembled body stage has finite unweighted `L^r` energy

PF-179 proves on each one-parameter Lambert body

\[
\int \delta^r\,d\mu\le C_r\delta_n^r,
\tag{12}
\]

where the exact shift-clone parameter defect satisfies `delta_n=O(p_n^{-1})`. Hence

\[
\sum_n\delta_n^r<\infty
\qquad(r>1)
\tag{13}
\]

by comparison with the ordinary `p`-series over integers.

PF-180 adds split corrections with summable strong `L^1` metric cost and tail distortion tending to zero. After a finite head, `delta<=1`, so their `L^r` cost is dominated by their `L^1` cost for every `r>=1`.

PF-181 adds the full-cusp handoff with a two-sided **weighted** finite `L^r` cost for every `r>=1`; PF-182 does the same for the decomposition-cuff smoothing. On a hyperbolic surface the area of a radius-one metric ball is bounded above by the area of the radius-one ball in `H^2`, so the inverse-ball weight has a universal positive lower bound. Weighted finiteness therefore implies unweighted finiteness for these correction modules. Combining the finitely many head pieces with the tail estimates gives (2).

This is exactly the point at which the exponent `r>1` matters. The one-body scale `delta_n=O(p_n^{-1})` is not globally `L^1` summable, so the present reduction is a Schatten-above-trace-endpoint mechanism and does not solve the accepted wave-operator clue.

## 2. A universal thick transition slab exists inside every short collar

PF-177 writes the full standard collar in the area coordinate (4) as

\[
|x|<A(L),
\qquad
A(L)=\frac{L}{\sinh(L/2)}.
\tag{14}
\]

The function `A` is decreasing. At the PF-138 shortness threshold

\[
\mu_*=2\operatorname{arsinh}1
\tag{15}
\]

one has

\[
A(\mu_*)=\mu_*>\frac54.
\tag{16}
\]

Thus every source collar with `L<=mu_*` contains `|x|<=5/4`. Since `t_eta->0` uniformly on the PF-138 tail, the same fixed subcollar lies in the matched target collars after a finite head. The head is irrelevant to any summability statement.

The map (5) is valid on any common fixed subcollar, not only on PF-177's displayed `|x|<=1` core. Pulling back the target metric gives

\[
G_\eta^*g_{L_\eta^+}
=
\frac{dx^2}{(L_\eta^+)^2+x^2}
+
\bigl((L_\eta^+)^2+x^2\bigr)d\theta^2,
\tag{17}
\]

whose determinant in `(x,theta)` is one. The source metric has the same form with `L_eta`, so the two eigenvalues are reciprocal and PF-177's calculation gives (6) verbatim.

On `T_eta`,

\[
\sqrt{L_\eta^2+x^2}\ge1.
\tag{18}
\]

PF-128/PF-177 give

\[
\mu_X(B_X(z,1))
\ge c\min\{1,\sqrt{L_\eta^2+x^2}\},
\tag{19}
\]

so (18) proves the uniform upper bound (9) for the inverse-ball weight. The target calculation is identical after a finite head.

## 3. Disjointness removes the dangerous collar count

PF-138 uses the collar theorem at the same threshold `mu_*`: two distinct simple closed geodesics with lengths at most `mu_*` do not intersect. Their standard collars are therefore pairwise disjoint. Since every `T_eta` lies inside its standard collar, the transition slabs are pairwise disjoint as well.

For any nonnegative function `f`, disjointness plus (9) gives

\[
\sum_\eta\int_{T_\eta}W_X f\,d\mu_X
\le
C\int_{\cup_\eta T_\eta}f\,d\mu_X
\le
C\int_X f\,d\mu_X.
\tag{20}
\]

Taking `f=delta_body^r` proves (10).

This is stronger than estimating every collar separately by the largest pantwise distortion that touches it. A per-collar estimate of the schematic form `O(P_eta^{-r})` would be multiplied by the number of short separators starting at that scale and is too crude near the endpoint `r=1`. Equation (20) instead charges the actual body energy on a point of the surface at most once. The potentially large combinatorial family of nested consecutive-block separators disappears from the bookkeeping because their standard collars cannot overlap.

The PF-177 core term is different: its natural size is already `|t_eta|^r=O(P_eta^{-3r})`, for which PF-138's explicit short-separator count is summable even at `r=1`. Thus the count is needed for the optimized core gauge but **not** for an energy-local transition splice.

## 4. What remains after the reduction

The unresolved problem is not to find another global summation trick. It is to prove (11) on one uniformly nondegenerating annular model while preserving the exact area gauge and the marked zero-twist topology.

A sufficient proof may proceed by comparing the body germ with the area-coordinate collar germ on a fixed thick slab, removing the residual rigid/isometric mode with the PF-142 marking, and applying a conservative localization whose `L^r` derivative cost is controlled by the local metric strain. The important word is **energy-local**. A pasting estimate stated only in a global `C^1` norm can reintroduce a full fixed-area `O(p^{-1})` charge for every short collar and therefore loses the disjoint-energy advantage of (20).

PF-143--PF-145 explain why this distinction is real. Nonconstant angular and radial trace modes on a thick collar interface have unsuppressed `L^1` currencies. They cannot be declared cheap merely because the core pinches. PF-183 does not bypass those lower bounds: it says that for `r>1` the correct target is to control the actual interface correction by the **existing local `L^r` body strain**, not by a separately repeated worst-case trace amplitude.

A genuine negative result would now be a proof that no exact-area local interpolation can satisfy an estimate of the form (11), for example because a flux/action mode or trace invariant can be small in local metric energy yet force an order-one conservative correction. Failure of one chosen interpolation is not enough.

## 5. Prior art and novelty audit

No novelty is claimed for the collar lemma, exact Fermi/area coordinates, disjoint-support summation, or standard conservative-pasting technology.

A targeted literature audit checked two nearby tool families. Friesecke--James--Müller's geometric-rigidity theorem (Communications on Pure and Applied Mathematics 55 (2002), 1461--1506, DOI `10.1002/cpa.10048`) controls distance from a single rigid motion by nonlinear strain on a fixed Euclidean domain in its classical `L^2` setting. Teixeira's conservative-pasting work (*On the conservative pasting lemma*, Ergodic Theory and Dynamical Systems 40 (2020), 1402--1440, DOI `10.1017/etds.2018.81`) supplies localized volume-preserving perturbation technology and is already relevant to the PF-182 seam argument. Neither source, as audited here, directly states the exact ingredient still needed in (11): a marked area-preserving annular splice with an `L^r` metric-strain bound uniform for the normalized true-collar family and valid throughout `1<r<2` as well as above it.

The absence of that exact theorem in this bounded search is **not** a novelty claim. PF-183's durable content is the project-specific reduction (20): the complete PF-138 collar family contributes no new multiplicity loss once the unresolved interpolation is confined to the fixed thick slabs.

## 6. Audit / falsification core

A later adversary can check PF-183 through the following finite chain:

1. combine PF-179's `O(delta_n^r)` one-body estimate with `delta_n=O(p_n^{-1})` to verify the tail part of (2) for every `r>1`;
2. verify that PF-180's summable `L^1` correction is also `L^r` on the tail and that PF-181/PF-182 weighted corrections are unweighted `L^r` as well;
3. differentiate `A(L)=L/sinh(L/2)` and verify it is decreasing, then use `A(mu_*)=mu_*>5/4` and `t_eta->0` to justify the fixed source/target subcollars;
4. insert the identity area-coordinate map (5) into the two collar metrics and rederive (6);
5. use PF-128/PF-177's unit-ball lower bound to prove that every transition slab (8) is uniformly thick;
6. use the collar theorem/PF-138 to verify that the complete short-collar family, and hence the `T_eta`, is pairwise disjoint;
7. apply disjointness to the nonnegative function `delta_body^r` to obtain (20) and (10);
8. keep (11) explicitly conditional: do not infer a global PF-175 hypothesis until an exact-area local splice satisfying that energy estimate is actually constructed on both source and target sides.

A failure of steps 1--7 would refute the reduction itself. A failure to prove step 8's local splice does **not** refute PF-183; it is precisely the remaining mathematical frontier isolated by this finding.