# PF-147 — trace-class squared-resolvent difference forces a Hilbert–Schmidt first relative resolvent

**Status:** `LITERATURE+DERIVED + EXACT-CONDITIONAL + BOUNDARY`. PF-112 proves that the first relative resolvent of the exact prime flute and its non-isometric all-composite shift clone cannot be trace class under any smooth geometric common-Hilbert-space identification. PF-146 opens a different sufficient scattering route by asking whether the **global squared-resolvent difference** is trace class; locally, every fixed central matched short collar already satisfies that stronger resolvent-power estimate. The present finding identifies an exact consequence of that still-open global gate. Classical Powers–Størmer/Birman–Koplienko–Solomyak fractional-power inequalities imply that trace class of the squared-resolvent difference would force the first relative resolvent into `S_2`; PF-112 then makes the inclusion sharp on the trace side. The same hypothesis canonically enters the Koplienko/modified-Fredholm `det_2` regime for the bounded resolvent pair, while ordinary trace-class `det_1` remains impossible. None of this proves the global squared-resolvent hypothesis, boundary values of the modified determinant, scattering-matrix equality, resonances, or any RH statement.

## Claim

Let `P_0,P_1 >= 0` be the two self-adjoint Laplacians after the same smooth geometric density-unitary identification used in PF-112, with `P_0` the exact prime-flute Laplacian and `P_1` the exact all-composite shift-clone Laplacian. Put

\[
R_i=(P_i+1)^{-1},
\qquad i=0,1.
\tag{1}
\]

Assume the still-open global PF-146 operator gate

\[
\boxed{
R_1^2-R_0^2\in\mathcal S_1.
}
\tag{2}
\]

Then the first relative resolvent satisfies

\[
\boxed{
R_1-R_0\in\mathcal S_2,
\qquad
\|R_1-R_0\|_{\mathcal S_2}^2
\le
\|R_1^2-R_0^2\|_{\mathcal S_1}.
}
\tag{3}
\]

Because the marked prime and shift-clone metrics are genuinely non-isometric, PF-112 applies to the same pair and gives

\[
\boxed{
R_1-R_0\notin\mathcal S_1.
}
\tag{4}
\]

Consequently, under (2),

\[
\boxed{
R_1-R_0\in\mathcal S_2\setminus\mathcal S_1.
}
\tag{5}
\]

For every `z in rho(R_0)`, define

\[
K(z):=(R_1-R_0)(R_0-z)^{-1}.
\tag{6}
\]

Since `(R_0-z)^{-1}` is boundedly invertible,

\[
\boxed{
K(z)\in\mathcal S_2\setminus\mathcal S_1.
}
\tag{7}
\]

Hence the modified Fredholm determinant

\[
\boxed{
D_2(z)
:=
\det{}_2\!\left(
I+(R_1-R_0)(R_0-z)^{-1}
\right)
}
\tag{8}
\]

is a canonical analytic determinant wherever the displayed bounded perturbation is considered, while the ordinary Fredholm determinant `det_1` of the same perturbation is unavailable because the perturbation is not trace class. Equivalently, the bounded self-adjoint pair `(R_1,R_0)` lies in the natural **Koplienko second-order spectral-shift regime**, not the Krein trace-class regime.

Equation (2) would also settle the accepted first-relative-resolvent Schatten clue at and above exponent `2`:

\[
R_1-R_0\in\mathcal S_r
\qquad(r\ge2),
\tag{9}
\]

but it does not imply the conjectured range `1<r<2`. Thus even a positive resolution of PF-146's squared-resolvent gate would leave the sharp lower Schatten threshold open.

## 1. Powers–Størmer applies directly to the bounded resolvents

The operators `R_0,R_1` are positive bounded self-adjoint operators. Set

\[
A=R_1^2,
\qquad
B=R_0^2.
\tag{10}
\]

Under (2), `A-B in S_1`. The classical Powers–Størmer square-root inequality, equivalently the `theta=1/2`, `p=1` endpoint of the Birman–Koplienko–Solomyak fractional-power ideal estimate, states for positive bounded operators that

\[
\boxed{
\|A^{1/2}-B^{1/2}\|_{\mathcal S_2}^2
\le
\|A-B\|_{\mathcal S_1}.
}
\tag{11}
\]

No assumption that `A` or `B` separately be trace class is needed; the hypothesis is on their difference. Since the positive square roots are exactly

\[
A^{1/2}=R_1,
\qquad
B^{1/2}=R_0,
\tag{12}
\]

substitution in (11) proves (3).

This is the key point at which one must not use a finite-dimensional or individually trace-class formulation of Powers–Størmer. The prime-flute resolvents are not expected to be Hilbert–Schmidt or trace class individually on the noncompact infinite-area surface. The BKS/Powers–Størmer ideal statement is precisely a **relative** assertion and therefore fits the PF-146 gate.

## 2. PF-112 makes the trace endpoint impossible

PF-112 is independent of all tail summability. On any open patch where the transported metrics differ, the localized first relative resolvent is a classical order-`-2` pseudodifferential operator with nonzero principal symbol. In dimension two its singular values have the critical asymptotic

\[
s_j\sim c j^{-1},
\qquad c>0,
\tag{13}
\]

and therefore the global first relative resolvent cannot lie in `S_1`.

The exact shift clone is non-isometric in the canonical marked class because corresponding distinguished cuff lengths differ. Hence PF-112 applies to the same `R_1-R_0` appearing in (3), and (4)--(5) follow immediately.

There is no contradiction between (3) and PF-112. The Schatten hierarchy in dimension two is exactly compatible with

\[
\mathcal S_1
\subsetneq
\mathcal S_2,
\tag{14}
\]

and the local `j^{-1}` principal-symbol behavior is itself square summable. The new content is that the **global** square-resolvent `S_1` gate, if established, automatically supplies enough tail control to promote that locally compatible `S_2` behavior to the complete surface.

## 3. Ordinary determinant remains unavailable, while `det_2` becomes canonical

Let

\[
D:=R_1-R_0.
\tag{15}
\]

For `z in rho(R_0)`, right multiplication by the bounded invertible operator `(R_0-z)^{-1}` preserves membership and nonmembership in every two-sided Schatten ideal. Thus

\[
D(R_0-z)^{-1}\in\mathcal S_2
\tag{16}
\]

by (3). If the same operator were in `S_1`, then multiplying on the right by the bounded inverse `R_0-z` would give `D in S_1`, contradicting PF-112. This proves (7).

The factorization

\[
(R_1-z)(R_0-z)^{-1}
=
I+D(R_0-z)^{-1}
\tag{17}
\]

therefore lies exactly at the first modified-Fredholm level. The standard `det_2(I+K)` is defined for `K in S_2`, so (8) is natural for the **bounded resolvent pair**. The ordinary determinant `det(I+K)` is not available because `K notin S_1`.

This distinction is intrinsic operator theory, not a zeta-shaped definition introduced by hand. Nevertheless, it concerns the bounded transforms `R_i`, not an absolute determinant of either Laplacian, and it is conditional on (2). PF-033 and the earlier noncompactness findings remain untouched.

## 4. The correct spectral-shift regime is second order, not first order

Krein's ordinary spectral-shift framework is naturally tied to trace-class perturbations. Koplienko's second-order spectral-shift function is instead defined for self-adjoint pairs whose difference is Hilbert–Schmidt. Under (2), equation (5) therefore places the bounded pair `(R_1,R_0)` in the latter regime while excluding the former.

This does **not** mean that `D_2` has the boundary behavior needed for a scattering phase or a zeta-like zero set. Gesztesy--Pushnitski--Simon explicitly construct Hilbert–Schmidt pairs for which

\[
\det{}_2((A-z)(B-z)^{-1})
\tag{18}
\]

has no nontangential boundary values. Thus `S_2` membership alone is insufficient to manufacture a canonical on-spectrum phase. Any use of (8) in the prime-flute program would need additional geometry/operator estimates proving the boundary or continuation properties actually required.

This is an important adversarial control. A future proof of (2) would create a legitimate second-order relative invariant, but **the mere existence of `det_2` is not evidence of an RH mechanism**.

## 5. Consequence for the two accepted operator questions

PF-146 already observes that (2), if proved globally, is sufficient for complete wave operators via Kato--Rosenblum and the Birman--Kato invariance principle applied to `Phi(lambda)=(1+lambda)^{-2}`. PF-147 adds a logically separate consequence:

```text
global squared-resolvent S1
    -> complete wave operators                    [PF-146 + invariance]
    -> first relative resolvent in S2             [Powers–Størmer/BKS]
    -> but first relative resolvent not in S1     [PF-112]
    -> canonical det2 / Koplienko regime
    -> no automatic boundary-value/scattering phase
```

For `CLUE-shift-clone-sharp-schatten-threshold`, a proof of (2) would settle only

\[
[2,\infty)
\tag{19}
\]

of the desired `r>1` range. The interval `1<r<2` remains a genuinely sharper infinite-tail question.

For `CLUE-shift-clone-wave-operator-equivalence`, PF-147 does not make the operator gate easier to prove. It only shows that success at that gate has a more rigid ideal-theoretic consequence than PF-146 recorded.

Most importantly for the line mandate, every conclusion above would hold for the exact **all-composite** shift control. Therefore none of wave equivalence, `S_2` first-resolvent comparability, or existence of the modified determinant can by itself be a primality selector. A surviving RH-relevant mechanism would have to use finer information not fixed merely by belonging to this relative ideal class.

## 6. Prior art and novelty audit

No novelty is claimed for the operator inequalities or spectral-shift theory.

- R. T. Powers and E. Størmer, *Free states of the canonical anticommutation relations*, Communications in Mathematical Physics 16 (1970), 1--33, DOI `10.1007/BF01645492`, is the classical source of the square-root inequality now called the Powers–Størmer inequality.
- M. Sh. Birman, L. S. Koplienko, and M. Z. Solomyak, *Estimates of the spectrum of a difference of fractional powers of selfadjoint operators*, Izv. Vyssh. Uchebn. Zaved. Mat. 1975, no. 3, 3--10; English translation Soviet Math. (Iz. VUZ) 19(3) (1975), 1--6, gives the broader fractional-power ideal estimate containing the same endpoint.
- F. Gesztesy, A. Pushnitski, and B. Simon, *On the Koplienko Spectral Shift Function. I. Basics*, J. Math. Phys. Anal. Geom. 4 (2008), 63--107, arXiv:0705.3629, reviews the `S_2` second-order spectral-shift framework and proves, among other things, that a `det_2` for a Hilbert–Schmidt pair need not possess nontangential boundary values.

Directed searches by structure -- fractional powers of positive operators in Schatten ideals, trace-class resolvent-power differences, Hilbert–Schmidt perturbation determinants, and Koplienko spectral shift -- show that all three functional-analytic ingredients are classical. The durable Mathia content is only their exact placement in the already-established prime/shift hierarchy:

\[
\boxed{
\text{PF-146 global }S_1\text{ square gate}
\Longrightarrow
\text{first resolvent }S_2
\stackrel{\text{PF-112}}{\Longrightarrow}
S_2\setminus S_1
\Longrightarrow
\text{second-order, not first-order, determinant regime}.
}
\tag{20}
\]

This is a project-specific boundary theorem, not a new operator-ideal theorem and not a novelty claim about Koplienko theory.

## 7. Audit / falsification core

A later adversary can check PF-147 through a short chain:

1. verify that the global hypothesis is exactly `R_1^2-R_0^2 in S_1`, with `R_i=(P_i+1)^-1`, and not a local Dirichlet-collar estimate;
2. apply the Powers–Størmer/BKS square-root ideal inequality to `A=R_1^2`, `B=R_0^2`, noting that only `A-B` is assumed trace class;
3. import PF-112 for the same smooth geometric identification to exclude `R_1-R_0 in S_1`;
4. use bounded invertibility of `(R_0-z)^-1` to prove the exact `S_2 \ S_1` classification of (6);
5. invoke only the standard definition of `det_2` and Koplienko theory for the bounded pair `(R_1,R_0)`;
6. retain the Gesztesy--Pushnitski--Simon boundary-value counterexample as a control against turning `S_2` membership into a scattering-phase claim;
7. do not infer the global hypothesis (2) from PF-146's fixed-central-collar result.

A refutation would have to show that the cited square-root ideal theorem does not apply to bounded positive `R_i^2` under a trace-class **difference**, that PF-112 does not apply to the same identification, or that one of the ideal/determinant implications above has been overstated. Failure to prove (2) globally would leave PF-147 as a valid conditional bridge but would not establish any of its prime/clone consequences on the actual surface.

## Research consequence

The squared-resolvent operator route now has a precise downstream hierarchy. If its global `S_1` gate succeeds, the first relative resolvent cannot remain merely compact or abstractly `S_r`-compatible: it is forced into the concrete class `S_2 \ S_1`, with a natural `det_2`/Koplienko relative invariant but no automatic boundary-value theory. This narrows the unresolved ideal question to the interval `1<r<2` and prevents two opposite overclaims: PF-112 does **not** obstruct the squared-resolvent route, while a future proof of that route would **not** resurrect an ordinary trace-class perturbation determinant or automatically produce an RH-relevant scattering phase.