# WI-167 — quantized flag refinements cannot charge Lamzouri confluence

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + BARRIER`. The proposed longer-flag refinement of WI-137 has an exact obstruction at the individual off-line-pair level. WI-137 writes the complete Lamzouri finite deficit as squared Hilbert--Schmidt distance from the canonical target `D=P_U+P_V`, plus explicit nonnegative source charges. If one refines the retained flag by adding any nonzero nested level and uses the natural flag-depth target, the target changes by a nonzero sum of orthogonal projections. On the simple off-line-pair confluence family of WI-140 this costs order one in Hilbert--Schmidt distance, while the **entire available Lamzouri deficit tends to zero**. Hence no such nonzero quantized step can be inserted into a universal nonnegative slack decomposition for an isolated simple off-line pair.

This does not rule out an interaction-triggered longer flag that is identically inactive on every isolated confluence control and becomes nontrivial only through additional multi-zero source structure. It shows that any such success must be funded by a genuinely new source inequality; flag refinement by itself cannot create an anti-confluence charge or an individual off-line-zero bootstrap. No unconditional zero proportion changes in this finding.

## 1. WI-137 fixes the canonical finite target

Use the finite Hilbert-space notation reconstructed from Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1. WI-137 proves the exact identity

\[
\boxed{
\Delta
=\|\mathcal A_F-\mathcal D\|_{\rm HS}^2+L,
\qquad
\mathcal D=P_U+P_V,
\qquad
L:=2B+4H_V\ge0.
}
\tag{1}
\]

Here `U subset V subset W` are Lamzouri's source-generated spaces. In the orthogonal grading

\[
W=U\oplus(V\ominus U)\oplus(W\ominus V),
\]

`D` has eigenvalues `2,1,0`. The values are not an arbitrary decoration of the flag: they are the centers selected by the exact square completion of Lamzouri's scalar coefficient inequalities.

Now refine the retained flag while keeping the original two retained levels. If the added nested levels have orthogonal projections `P_1,...,P_r`, the natural depth operator is

\[
\mathcal D'=\mathcal D+J,
\qquad
J:=\sum_{a=1}^rP_a\succeq0.
\tag{2}
\]

For a genuine refinement, `J` is nonzero. Because the projections come from a flag they commute and are simultaneously diagonalizable, so every nonzero eigenvalue of `J` is a positive integer. Consequently

\[
\boxed{J\ne0\quad\Longrightarrow\quad\|J\|_{\rm HS}^2\ge1.}
\tag{3}
\]

The elementary Hilbert--Schmidt polarization identity gives, with `X=A_F-D`,

\[
\|X\|_{\rm HS}^2
=\|X-J\|_{\rm HS}^2
 +2\langle X,J\rangle_{\rm HS}
 -\|J\|_{\rm HS}^2.
\tag{4}
\]

Thus rewriting (1) around `D'` does **not** automatically produce another nonnegative remainder. It produces the signed correction

\[
L+2\langle \mathcal A_F-\mathcal D,J\rangle_{\rm HS}-\|J\|_{\rm HS}^2.
\tag{5}
\]

A useful longer flag therefore already requires a source theorem strong enough to control (5). The flag algebra alone supplies no sign.

## 2. The isolated simple off-line pair makes every nonzero step impossible

WI-140 gives an exact one-pair control. Take one simple conjugate pair

\[
z=x+iy,\qquad \bar z=x-iy,\qquad y>0,
\]

and write

\[
t=t(y):=\|h_y\|^2>0.
\]

For this configuration

\[
U=V=\operatorname{span}\{g_y\},
\qquad
W\ominus V=\operatorname{span}\{h_y\},
\]

with `g_y` orthogonal to `h_y`. In the corresponding orthonormal basis WI-140 computes

\[
\mathcal A_y-\mathcal D_y
=\operatorname{diag}(2t,-2t),
\tag{6}
\]

so

\[
\boxed{
\|\mathcal A_y-\mathcal D_y\|_{\rm HS}
=2\sqrt2\,t,
\qquad
\Delta_y=8t+8t^2.
}
\tag{7}
\]

Moreover `t(y)=4\pi^2\mu_2y^2+O(y^4)`, hence `t(y) -> 0` as the pair confluences to the critical-line double.

Let `D'_y=D_y+J_y` be any longer flag-depth target whose added flag is nontrivial at this finite configuration. By (3), `||J_y||_HS>=1`. The reverse triangle inequality and (7) give

\[
\begin{aligned}
\|\mathcal A_y-\mathcal D'_y\|_{\rm HS}
&=\|(\mathcal A_y-\mathcal D_y)-J_y\|_{\rm HS}\\
&\ge1-2\sqrt2\,t.
\end{aligned}
\tag{8}
\]

Therefore, whenever

\[
0<t<\frac1{8+4\sqrt2},
\tag{9}
\]

one has the strict comparison

\[
\boxed{
\|\mathcal A_y-\mathcal D'_y\|_{\rm HS}^2
>8t+8t^2
=\Delta_y.
}
\tag{10}
\]

Indeed `(1-2 sqrt(2)t)^2 > 8t+8t^2` is exactly equivalent to `(8+4 sqrt(2))t<1` after cancelling the common `8t^2` term.

Equation (10) is stronger than saying that the correction (5) lacks an obvious sign. The **distance term alone already exceeds the entire finite deficit**, before any additional nonnegative population, multiplicity, horizontal, or Bessel remainder is requested. Hence there cannot exist a universal refinement of the form

\[
\Delta\ge\|\mathcal A_F-\mathcal D'\|_{\rm HS}^2
+\text{other nonnegative terms}
\tag{11}
\]

if the extra flag has a nonzero step on arbitrarily shallow isolated simple off-line pairs.

## 3. Why quantization is the obstruction

The point is not that the proposed target was chosen badly by a small numerical amount. The source defect in the one-pair family is continuous and quadratic in horizontal depth:

\[
\Delta_y=O(y^2),
\qquad
\|\mathcal A_y-\mathcal D_y\|_{\rm HS}=O(y^2).
\tag{12}
\]

A nonzero flag step is instead quantized. An orthogonal projection has Hilbert--Schmidt norm equal to the square root of its rank, so it cannot shrink continuously with `y`. Adding one retained level changes the target by at least one unit in Hilbert--Schmidt norm even though the actual Lamzouri operator tends to the original `2/1/0` target.

This covers every way of assigning an additional integer flag depth to the isolated pair's even direction, odd direction, or any other nonzero intermediate subspace of its two-dimensional `W`. The subspace may rotate with `y`; its projection still has rank at least one and therefore the same norm floor. At the confluent endpoint the dimension of the odd source direction may disappear, but for every nonzero `y` the proposed extra level still costs a full projection while `Delta_y` can be arbitrarily small.

Equivalently, the confluence family proves a target-rigidity statement. Any family of finite targets `T_y` satisfying

\[
\Delta_y\ge\|\mathcal A_y-T_y\|_{\rm HS}^2
\tag{13}
\]

must obey

\[
\|T_y-\mathcal D_y\|_{\rm HS}
\le\sqrt{\Delta_y}+2\sqrt2\,t
\longrightarrow0.
\tag{14}
\]

A nonzero integer-depth refinement cannot satisfy (14). Thus the original `2/1/0` target is locally forced at confluence among quantized flag-depth targets controlled by the same finite deficit.

## 4. Relation to the earlier confluence barriers

WI-140 proves that no positive **count-only** charge per off-line pair follows from Lamzouri's abstract finite proposition. WI-141 and WI-142 then show that fixed-order moments and every preassigned finite family of **continuous** spectral regularizations can also be defeated by choosing the horizontal depth below their continuity scale.

The present barrier is different. A projection-valued flag step is discontinuous in exactly the way that WI-142 left logically open: its norm does not tend to zero when the underlying source vector becomes confluent. Equation (10) shows that this particular singularity does not rescue the bootstrap. It overshoots the available slack instead of extracting it. Exact inertia can still jump at zero because it is used as a sign/count invariant; inserting a unit projection jump into the **squared-distance target** is a stronger demand and is incompatible with the vanishing Lamzouri deficit.

So singularity remains a possible source of information in principle, but a useful singular observable must come with an independently evaluated source identity. It cannot be manufactured by refining the WI-137 target flag and then appealing to the same deficit.

## 5. What remains live for a longer flag

This finding does not prove that every source-derived longer flag is useless in a many-zero configuration. It gives the exact escape condition.

Any additional flag level that is intended to contribute a nonnegative WI-137-type distance term must be **inactive on the isolated simple-pair confluence controls**. In particular it cannot assign an autonomous positive integer depth merely because an off-line even or odd generator exists. A surviving refinement must instead be triggered by information absent from one pair, such as a rigorously controlled interaction among several zero generators, a multiplicity excess already carrying positive scalar slack, or an arithmetic/density condition that prevents the relevant target step from appearing in the confluent regime.

In operator form, the new source input has to control the signed budget exposed in (5), or an equivalent quantity. Merely naming an additional nested subspace does not do this. If the extra level is nonzero only after a source interaction theorem has been proved, then that interaction theorem -- not the abstract flag identity -- is the new coercive information.

This distinction matters for the RH-facing objective. A flag that only repackages already charged multiplicity excess may sharpen simplicity bookkeeping but does not exclude a single simple off-line pair. To attack RH, the remaining flag route must expose a source-controlled interaction that is absent in the one-pair confluence model and that cannot collapse as the horizontal depth tends to zero.

## 6. Prior-art and novelty audit

The zeta-side primary source is Lamzouri, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1 and its nested spaces `U subset V subset W`. WI-137 supplies the exact `2/1/0` Hilbert--Schmidt normal form, and WI-140 supplies the exact one-pair spectrum and confluence asymptotics. Both ultimately use only Lamzouri's finite source construction plus elementary Hilbert-space algebra.

The projection facts used here -- orthogonal projections having Hilbert--Schmidt norm squared equal to rank, simultaneous diagonalization of commuting nested projections, the reverse triangle inequality, and the polarization/completion-of-squares identity (4) -- are classical. No novelty is claimed for them. A focused search around Lamzouri's preprint, nested/flag projection operators, Hilbert--Schmidt matrix nearness, and projection-sum targets did not locate an external zeta-specific theorem that refines Lamzouri's target by a longer quantized flag or states the confluence obstruction (10). Absence from that search is not used as a priority claim.

The durable Mathia deduction is the boundary created by combining the exact recent source normal form with its exact confluence control: **a nonzero integer-depth target step has a fixed norm floor, whereas the whole available Lamzouri deficit has no such floor**.

## 7. Research consequence

The generic version of `CLUE-lamzouri-flag-depth-operator` is therefore narrowed sharply. Proving the abstract identity that `sum_j P_{V_j}` has integer depth on the graded pieces is mathematically correct but supplies no new charge. Any extension that adds a nonzero depth to an isolated simple off-line pair is impossible by (10).

The only live flag variant is interaction-triggered: find a source-derived extra level that vanishes on every isolated confluence control but is forced to be nonzero, with a quantitatively funded trace budget, in a zeta-compatible many-zero configuration. A decisive positive must state the new source inequality that pays for the projection step. If no such interaction layer can be identified, the flag route reduces to WI-137 and should be closed rather than elaborated further.