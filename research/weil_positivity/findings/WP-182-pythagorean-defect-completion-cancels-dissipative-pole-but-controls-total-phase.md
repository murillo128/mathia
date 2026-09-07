# WP-182 — Pythagorean defect completion cancels the dissipative boundary pole while preserving positivity, but controls only the completed phase balance

**Status:** `EXACT-DERIVED + CANONICAL-POSITIVE-COMPLETION + CLASSICAL-PYTHAGOREAN/DARLINGTON-STRUCTURE + PASSIVE-MATCHED-CONTROL + CANDIDATE-STRUCTURAL-ESCAPE + NOT-WEIL-POSITIVITY`.

`WP-181` proves that the scalar de Branges--Rovnyak kernel of a genuinely dissipative Schur response has a positive boundary pole

\[
\frac{1-|S(i\omega)|^2}{2x}
\]

whose pointwise asymptotic subtraction leaves the sign-indefinite finite part `-|S|^2 theta'`. It explicitly leaves open a narrower possibility: remove the loss direction **before** the boundary limit through a source-derived positive completion or quotient rather than by subtracting a scalar asymptotic term afterward.

For non-extreme scalar Schur functions there is a canonical classical construction that does exactly this. Let `A` be the outer Pythagorean mate of `S`, so that on the boundary

\[
|S(i\omega)|^2+|A(i\omega)|^2=1
\tag{1}
\]

almost everywhere. Then the column

\[
F(s)=\binom{S(s)}{A(s)}
\tag{2}
\]

is a Schur-class lossless completion, and its positive kernel

\[
K_F(s,w)
=
\frac{1-S(s)\overline{S(w)}-A(s)\overline{A(w)}}
{s+\overline w}
\succeq0
\tag{3}
\]

satisfies the exact positive-kernel decomposition

\[
\boxed{
K_S(s,w)
=
\frac{A(s)\overline{A(w)}}{s+\overline w}
+K_F(s,w).
}
\tag{4}
\]

Thus the absorption pole identified in `WP-181` can be removed by subtracting the **entire canonical positive Hardy defect kernel**, not merely its divergent diagonal asymptotic, and the residual kernel remains positive. At regular boundary points the residual has a finite nonnegative diagonal limit.

This is a real escape from the particular no-go mechanism of `WP-181`, but it does not yield Weil positivity. The residual sign theorem applies to the **weighted phase balance of the completed two-channel object**, not to the phase of `S` alone. The same phenomenon occurs in the arithmetic-free resistor--inductor control from `WP-180`, where the residual kernel is explicitly rank-one positive even while the phase derivative of `S` changes sign. Consequently the completion is classical lossless embedding/Darlington structure, not evidence that Mathia has generated the Riemann real place or the global Weil form.

The branch consequence is nevertheless substantive. A viable dissipative route should no longer be required to make the scalar `S`-phase positive by itself. It may instead seek a Mathia-native **defect channel produced before scalarization** whose completed positive kernel contains both the signed target phase and a compensating channel. The decisive unresolved requirement is that this defect channel be forced by the same finite--archimedean geometry, rather than introduced after choosing a target Schur response.

## 1. Canonical Pythagorean completion of a non-extreme Schur function

Work first in the scalar Schur class on the right half-plane

\[
\mathbb C_+=\{s:\operatorname{Re}s>0\}.
\]

For a non-extreme Schur function `S`, the classical Pythagorean-mate theorem, transferred from the disk by a Cayley transform, supplies an outer bounded analytic function `A`, unique up to a constant unimodular factor, whose boundary values satisfy (1). Equivalently, `A` is the outer spectral factor of the scalar defect `1-|S|^2`.

The unimodular ambiguity is irrelevant for the kernel below because `A(s)\overline{A(w)}` is unchanged. Therefore the positive splitting derived from `A` is canonical at kernel level once the non-extreme Schur response `S` is fixed.

Boundary identity (1) implies that the analytic column `F=(S,A)^T` is contractive in the half-plane and has norm one almost everywhere on the boundary. In systems terminology it is the one-input lossless completion of the lossy scalar channel; in function theory it is a column-inner completion. The scalar Schur-kernel criterion therefore gives

\[
K_F(s,w)
=
\frac{1-F(w)^*F(s)}{s+\overline w}
\succeq0.
\tag{5}
\]

Since

\[
K_S(s,w)
=
\frac{1-S(s)\overline{S(w)}}{s+\overline w},
\]

identity (4) follows immediately. Both terms on its right are positive kernels: the first is the ordinary Hardy kernel multiplied by `A`, and the second is the de Branges--Rovnyak kernel of the completed column.

This is stronger than a finite-part prescription. In `WP-181`, subtracting only

\[
\frac{1-|S(i\omega)|^2}{2x}
\]

on a diagonal is not positivity preserving. Equation (4), by contrast, identifies a complete two-variable positive subkernel whose subtraction is certified by the remaining positive kernel `K_F`. The operation is fixed by a classical canonical completion, not by the desired boundary phase.

## 2. The boundary pole is absorbed into the defect channel

Suppose `S` and its Pythagorean mate `A` extend holomorphically through a boundary point `i\omega`, with

\[
0<r:=|S(i\omega)|<1.
\tag{6}
\]

Then `|A(i\omega)|^2=1-r^2>0`, so both components have local phase branches. Write

\[
S(i\omega)=r e^{i\theta_S(\omega)},
\qquad
A(i\omega)=\sqrt{1-r^2}\,e^{i\theta_A(\omega)}.
\tag{7}
\]

The Cauchy--Riemann calculation from `WP-181` applies separately to each component. Along `s=x+i\omega`,

\[
|S(s)|^2
=
r^2+2xr^2\theta_S'(\omega)+O(x^2),
\tag{8}
\]

and

\[
|A(s)|^2
=
(1-r^2)+2x(1-r^2)\theta_A'(\omega)+O(x^2).
\tag{9}
\]

The first positive term in (4) therefore has diagonal expansion

\[
\frac{|A(x+i\omega)|^2}{2x}
=
\frac{1-r^2}{2x}
+(1-r^2)\theta_A'(\omega)
+O(x).
\tag{10}
\]

Its leading term is **exactly** the dissipative absorption pole of `WP-181`. Subtracting the full defect kernel rather than only that leading coefficient leaves

\[
\boxed{
\lim_{x\downarrow0}K_F(x+i\omega,x+i\omega)
=
-r^2\theta_S'(\omega)
-(1-r^2)\theta_A'(\omega)
\ge0.
}
\tag{11}
\]

Hence the canonical positive completion converts the impossible scalar sign demand into the weighted inequality

\[
\boxed{
r^2\theta_S'(\omega)
+(1-r^2)\theta_A'(\omega)
\le0.
}
\tag{12}
\]

The sign theorem survives, but it belongs to the **completed channel**. It places no one-sided sign requirement on `theta_S'` alone. A sign-changing `S` phase is compatible with positive geometry provided the defect channel carries the compensating boundary phase.

This is precisely the kind of before-the-limit coupling left open by `WP-181`. It also identifies why the scalar finite part there was the wrong object to demand positivity from: it discarded the finite phase contribution of the same channel whose leading norm deficit produced the divergence.

## 3. Exact passive matched control

The elementary passive family from `WP-180` and `WP-181` makes the mechanism completely explicit. Let

\[
S_{a,b}(s)=\frac{s+a}{s+b},
\qquad 0<a<b.
\tag{13}
\]

This is the strict Schur reflection coefficient of a positive resistor--inductor impedance. Its defect has the exact outer spectral factor

\[
\boxed{
A_{a,b}(s)
=
\frac{\sqrt{b^2-a^2}}{s+b}.
}
\tag{14}
\]

Indeed, on the imaginary axis,

\[
|S_{a,b}(i\omega)|^2
=
\frac{a^2+\omega^2}{b^2+\omega^2},
\qquad
|A_{a,b}(i\omega)|^2
=
\frac{b^2-a^2}{b^2+\omega^2},
\tag{15}
\]

so their squares sum to one exactly.

For the completed column `F_{a,b}=(S_{a,b},A_{a,b})^T`, direct algebra gives

\[
\begin{aligned}
1-S_{a,b}(s)\overline{S_{a,b}(w)}
-A_{a,b}(s)\overline{A_{a,b}(w)}
&=
\frac{(b-a)(s+\overline w)}{(s+b)(\overline w+b)}.
\end{aligned}
\tag{16}
\]

Therefore

\[
\boxed{
K_{F_{a,b}}(s,w)
=
\frac{b-a}{(s+b)(\overline w+b)}
\succeq0.
}
\tag{17}
\]

It is a rank-one positive kernel with finite boundary diagonal

\[
\boxed{
K_{F_{a,b}}(i\omega,i\omega)
=
\frac{b-a}{b^2+\omega^2}>0.
}
\tag{18}
\]

So the `WP-181` divergence is not an unavoidable obstruction once the canonical defect channel is retained. The full scalar kernel splits exactly as

\[
K_{S_{a,b}}
=
\frac{A_{a,b}A_{a,b}^*}{s+\overline w}
+K_{F_{a,b}},
\tag{19}
\]

and the second term remains finite and positive all the way to the dissipative boundary.

## 4. The positive residual does not restore the sign of the scalar phase

For the same control,

\[
\theta_S'(\omega)
=
\frac{(b-a)(ab-\omega^2)}
{(a^2+\omega^2)(b^2+\omega^2)},
\tag{20}
\]

which changes sign at `|omega|=sqrt(ab)` as established in `WP-180`. The outer mate has boundary phase

\[
\theta_A(\omega)
=
-\arctan\frac{\omega}{b}+\text{constant},
\]

hence

\[
\theta_A'(\omega)
=-\frac{b}{b^2+\omega^2}.
\tag{21}
\]

Using (15), the completed weighted phase derivative is

\[
\begin{aligned}
|S|^2\theta_S'
+|A|^2\theta_A'
&=
-\frac{b-a}{b^2+\omega^2},
\end{aligned}
\tag{22}
\]

and therefore

\[
-|S|^2\theta_S'-|A|^2\theta_A'
=
\frac{b-a}{b^2+\omega^2},
\tag{23}
\]

exactly agreeing with the positive kernel value (18).

This control separates the two statements cleanly:

\[
\boxed{
\theta_S'\text{ can change sign while the completed boundary form stays strictly positive.}
}
\tag{24}
\]

Thus the new completion does not contradict `WP-180`; it explains geometrically where the missing sign control went. Dissipative scalar phase is only one component of a larger conservative energy balance.

## 5. What is genuinely gained over WP-181

`WP-181` established a trilemma for the **scalar diagonal readout**: lossless boundary data gives finite positivity but rigid phase; dissipative data allows phase flexibility but gives a divergent positive kernel; scalar finite-part extraction recovers the phase but loses positivity.

Equations (4) and (11) show that this trilemma is not stable under a canonical vector completion. In the non-extreme class one may keep dissipation, preserve a finite positive boundary kernel, and allow `theta_S'` to change sign simultaneously. The price is exact and structural: the positive observable is no longer `theta_S'`; it is the weighted phase balance of `S` and its defect channel.

This narrows the search more productively than another scalar no-go. The relevant question becomes whether Mathia itself supplies a companion channel before the scalar response is formed. If it does, a signed archimedean component need not separately inherit positivity; positivity may belong to the assembled vector/matrix geometry.

That possibility is directly aligned with the branch mandate, which asks for one structure producing both local arithmetic and archimedean/global pieces. But the present construction by itself does **not** meet that mandate. Starting from an already chosen `S` and manufacturing its outer defect factor is a universal function-theoretic operation available for arithmetic-free Schur functions.

## 6. Aggressive falsification and matched controls

Several tempting overinterpretations fail immediately.

First, the Pythagorean mate does not select the Riemann Gamma phase. The passive family (13) has no arithmetic input and already realizes the same architecture. Therefore the existence of a canonical defect completion is not evidence that a proposed `S` is the correct archimedean response.

Second, the completion does not create finite-prime coefficients. Equations (1)--(12) know only the Schur defect of `S`. Nothing forces Mangoldt support, the critical `p^{-1/2}` weight, a polar term, or any mixed-prime incidence. Those must arise from additional Mathia-native structure.

Third, one cannot declare the outer factor `A` to be the missing archimedean/global counterterm merely because (12) has the right sign. If `A` is constructed **after** selecting an `S` to fit Gamma or zeta data, the result is ordinary Pythagorean/Darlington completion. The research mandate requires the channel and its coupling to arise independently from Mathia geometry.

Fourth, existence is not automatic for every Schur function. The scalar Pythagorean mate is the non-extreme case. Singular/extreme symbols, boundary zeros, nonregular boundary points, and matrix-valued defects require their own domain/factorization analysis. The exact boundary formula (11) assumes regular extension of both components through the point being evaluated.

Finally, the present positive kernel is not the Weil quadratic functional. It proves positivity of a reproducing-kernel geometry attached to a completed passive channel. No equality with the finite-prime plus Gamma/polar explicit-formula terms has been derived.

## 7. Prior-art and novelty audit

The mathematical ingredients are classical. Donald Sarason, *Sub-Hardy Hilbert Spaces in the Unit Disk* (Wiley, 1994), develops the non-extreme `H(b)` theory in which an outer Pythagorean mate accompanies a non-extreme Schur symbol. Modern treatments use the same terminology; for example Bartosz Malman and Daniel Seco, *Universal multipliers for Sub-Hardy Hilbert spaces*, arXiv:2410.13438, explicitly recalls that every non-extreme disk Schur function has a bounded outer Pythagorean mate `a` with `|a|^2+|b|^2=1` on the circle. The disk statement transfers to the right half-plane by the standard Cayley equivalence.

Right-half-plane de Branges--Rovnyak Schur kernels and their passive/conservative realizations are classical as well; `WP-181` already audits Joseph A. Ball, Mikael Kurula, Olof J. Staffans, and Hans Zwart, *De Branges--Rovnyak Realizations of Operator-Valued Schur Functions on the Complex Right Half-Plane*, Complex Analysis and Operator Theory 9 (2015), 723--792, DOI `10.1007/s11785-014-0358-2`, arXiv:1307.7408, together with the later conservative model of Ball--Kurula--Staffans.

From systems theory, embedding a contractive/lossy transfer into a lossless inner system is the classical Darlington or unitary-extension problem. Stephan Ramon Garcia, *Inner matrices and Darlington synthesis*, Methods of Functional Analysis and Topology 11(1) (2005), 37--47, gives a function-theoretic scalar treatment and explicitly includes the boundary identity `|a|^2+|b|^2=1` in inner-matrix completions. Thus no novelty is claimed for Pythagorean mates, spectral factors, lossless embedding, the positivity of (3), or Darlington synthesis.

The Mathia-specific delta is the exact application of that classical structure to the live obstruction isolated by `WP-181`:

\[
\boxed{
\text{the dissipative absorption pole has a canonical positive defect-channel completion,}
}
\]

and, after retaining that channel,

\[
\boxed{
\text{finite boundary positivity survives but constrains the completed phase balance rather than }\theta_S'.
}
\tag{25}
\]

This materially changes the branch boundary. `WP-181` remains correct for scalar asymptotic finite-part extraction, but its open vector/source-derived escape is nonempty and has an exact classical model. The research novelty question therefore shifts from whether such a completion exists to whether **Mathia forces a non-generic arithmetic instance of it before target fitting**.

## 8. Consequence for the Weil-positivity search

The current boundary-response route now has a sharper source-to-destination gate. A dissipative Mathia candidate may legitimately use a signed scalar component if it comes with an intrinsic defect/companion channel and a positive completed kernel or energy. What must be proved is not positivity of that scalar component, but positivity of the common assembled object together with an exact decomposition whose scalar projections are the required arithmetic and archimedean/global terms.

A decisive next test is therefore:

> Does any existing Mathia construction intrinsically produce a non-extreme Schur response **and its defect channel** from the same finite--archimedean incidence before comparison with the explicit formula, so that the completed positive form yields the Mangoldt sector and the Gamma/polar sector as forced components?

If the answer requires first choosing a scalar response because it matches the Gamma factor and then taking its outer Pythagorean mate, the route is classical Darlington completion and fails the branch independence/novelty gate. If instead a Mathia-native geometry produces both channels and their coupling first, equation (11) supplies a concrete positive architecture in which a sign-changing archimedean component is no longer automatically fatal.

No such Mathia-native two-channel identification is established here. `WP-182` therefore records a **precise structural escape and its exact burden of proof**, not a Weil-positivity theorem.