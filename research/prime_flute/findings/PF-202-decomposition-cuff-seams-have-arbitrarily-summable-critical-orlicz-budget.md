# PF-202 — decomposition-cuff seams have arbitrarily summable critical Orlicz budget

**Status:** `EXACT-DERIVED + ENDPOINT-LOCALIZATION + POSITIVE/BOUNDARY`. PF-182 proves that the exact-area smoothing of the distinguished decomposition cuffs can be supported in arbitrarily thin two-sided neighborhoods and, for any prescribed summable positive sequence, can be made to have that summable inverse-unit-ball weighted `L^1` metric-deviation budget while retaining an `O(\delta_n)` pointwise distortion bound. PF-196 shows that the critical two-dimensional Cwikel coefficient space is not `L^1` but `L\log L`: concentrating mass on a small set inserts a genuine logarithmic Luxemburg penalty. These two facts fit together favorably. Because PF-182 lets the seam support be made **arbitrarily smaller without an inverse-width first-derivative loss**, its prescribed `L^1` budget can be chosen small enough to pay the critical logarithm cuff by cuff. Consequently the matrix cotangent coefficient of the complete distinguished-cuff seam correction can be chosen with a summable `L\log L` Luxemburg norm on both source and target sides; in fact its tail Orlicz budget can be dominated by any prescribed summable sequence.

This removes **coefficient concentration at the distinguished decomposition cuffs** as an endpoint obstruction. It does not prove that the associated seam contribution to the global first relative resolvent is weak trace class. Shrinking the neighborhoods may worsen higher derivatives, chart buffers, or localized pseudodifferential constants, and PF-200/PF-201's uniform regular-body Cwikel factorization does not automatically cover this shrinking interface family. The remaining analytic question is therefore operator-level: obtain uniform or summably controlled critical localization constants for these seam pieces, or dominate them by a stronger trace/weak-trace estimate. The true PF-138 short-collar endpoint conservative splice remains separate and open.

## Claim

Let `X` be the exact prime flute and `X_+` its exact all-composite shift clone. For the matched distinguished decomposition cuffs `C_n\subset X` and `C_n^+\subset X_+`, let the exact-area global comparison be modified in the PF-182 two-sided seam neighborhoods

\[
U_n\subset X,
\qquad U_n^+\subset X_+.
\tag{1}
\]

Write

\[
W_X(x)=\mu_X(B_X(x,1))^{-1},
\qquad
W_{X_+}(y)=\mu_{X_+}(B_{X_+}(y,1))^{-1}.
\tag{2}
\]

Let `h=F^*g_+` on the source side of the exact-area comparison, and use PF-175's cotangent coefficient

\[
C=\rho A-I,
\qquad
\rho=\frac{d\mu_h}{d\mu_g}.
\tag{3}
\]

On the PF-182 seam correction one has exactly `\rho=1`, so

\[
C=A-I
\tag{4}
\]

and there is no scalar density coefficient `b=\rho-1`.

Fix

\[
\Phi(t)=t\log(e+t)
\tag{5}
\]

and let `\|\cdot\|_{L_\Phi}` denote the Luxemburg norm used in PF-196/PF-197. Then the PF-182 correction can be chosen so that

\[
\boxed{
\sum_n
\|C\mathbf 1_{U_n}\|_{L_\Phi(X)}
+
\sum_n
\|C^+\mathbf 1_{U_n^+}\|_{L_\Phi(X_+)}
<\infty,
}
\tag{6}
\]

where `C^+` is the corresponding inverse/target cotangent coefficient.

More strongly, after discarding a finite head, for every prescribed positive sequence `\varepsilon_n` with

\[
\sum_n\varepsilon_n<\infty,
\tag{7}
\]

the seam neighborhoods may be chosen so that

\[
\boxed{
\|C\mathbf 1_{U_n}\|_{L_\Phi}
+
\|C^+\mathbf 1_{U_n^+}\|_{L_\Phi}
\le \varepsilon_n
}
\tag{8}
\]

for every tail cuff, after changing the harmless absolute constant in the choice of the PF-182 support budget.

Equation (8) is a coefficient-space statement. It neither invokes nor proves a uniform Cwikel theorem on the shrinking seam neighborhoods.

## 1. PF-182 gives an arbitrarily small weighted `L^1` seam budget

PF-182 proves that for every prescribed positive summable sequence `q_n` the exact-area seam smoothing can be chosen with pairwise disjoint two-sided support and

\[
\int_{U_n}W_X\,\delta_{\rm cuff,n}\,d\mu_X
+
\int_{U_n^+}W_{X_+}\,\delta^+_{\rm cuff,n}\,d\mu_{X_+}
\le C q_n.
\tag{9}
\]

At the same time its tail pointwise distortion satisfies

\[
\delta_{\rm cuff,n}\le C\delta_n,
\tag{10}
\]

and analogously on the inverse/target side. The key geometric fact behind (9)--(10) is that the seam support may be made arbitrarily thin while the relative generating-function cutoff has no first-derivative penalty proportional to the inverse support width.

The inverse-unit-ball weight has a universal positive lower bound on every hyperbolic surface. Indeed, if `\pi:\mathbb H^2\to X` is the universal covering and `\widetilde x` lifts `x`, then

\[
B_X(x,1)=\pi(B_{\mathbb H^2}(\widetilde x,1)),
\tag{11}
\]

as a metric image, and therefore

\[
\mu_X(B_X(x,1))
\le
\mu_{\mathbb H^2}(B_{\mathbb H^2}(\widetilde x,1))=:V_1.
\tag{12}
\]

Thus

\[
W_X\ge V_1^{-1},
\qquad
W_{X_+}\ge V_1^{-1}.
\tag{13}
\]

Combining (9) and (13) gives the ordinary endpoint masses

\[
\int_{U_n}\delta_{\rm cuff,n}\,d\mu_X
+
\int_{U_n^+}\delta^+_{\rm cuff,n}\,d\mu_{X_+}
\le C q_n.
\tag{14}
\]

On the uniform tail quasi-isometry range, PF-175's coefficient comparison gives

\[
|C|\le C\delta_{\rm cuff,n},
\qquad
|C^+|\le C\delta^+_{\rm cuff,n}.
\tag{15}
\]

Hence, with

\[
L_n:=\|C\mathbf1_{U_n}\|_1,
\qquad
L_n^+:=\|C^+\mathbf1_{U_n^+}\|_1,
\tag{16}
\]

we have

\[
\boxed{L_n+L_n^+\le Cq_n.}
\tag{17}
\]

The same tail distortion bound supplies a uniform finite amplitude bound

\[
\boxed{
\|C\mathbf1_{U_n}\|_\infty
+
\|C^+\mathbf1_{U_n^+}\|_\infty
\le B_0
}
\tag{18}
\]

for one fixed `B_0`; in fact the left-hand side tends to zero with `\delta_n`, but boundedness is enough below.

## 2. The PF-196 logarithm can be paid by further support thinning

PF-196 proves the elementary critical Luxemburg estimate: for bounded nonzero `u`,

\[
\boxed{
\|u\|_{L_\Phi}
\le
\|u\|_1
\log\!\left(
 e+\frac{\|u\|_\infty}{\|u\|_1}
\right).
}
\tag{19}
\]

Apply (19) to the pointwise matrix norm of the source and target seam coefficients. Using (17)--(18),

\[
\|C\mathbf1_{U_n}\|_{L_\Phi}
+
\|C^+\mathbf1_{U_n^+}\|_{L_\Phi}
\le
Cq_n\log\!\left(e+\frac{C B_0}{q_n}\right).
\tag{20}
\]

The critical logarithm is genuine: choosing a smaller support at fixed pointwise amplitude does not make the Luxemburg norm linear in its `L^1` mass. But

\[
q\log(e+B/q)\longrightarrow0
\qquad(q\downarrow0)
\tag{21}
\]

for every fixed finite `B`. Since PF-182 permits **any** prescribed summable positive `q_n`, the logarithm is not a global obstruction.

Given the target sequence `\varepsilon_n` in (7), choose `q_n>0` so that simultaneously

\[
q_n\le2^{-n}
\tag{22}
\]

and

\[
Cq_n\log\!\left(e+\frac{CB_0}{q_n}\right)
\le\varepsilon_n.
\tag{23}
\]

Such a choice exists cuff by cuff by (21), and (22) guarantees `\sum q_n<\infty`, so PF-182 accepts it as a legal support budget. Equations (20)--(23) prove (8), hence (6). A finite head contributes only finitely many compactly supported bounded coefficients and is harmless for summability.

This is stronger than fixing a convenient exponentially decaying support sequence, although that would already suffice: `q_n=2^{-n}` gives `q_n\log(e+B_0/q_n)=O(n2^{-n})`.

## 3. Exact area removes the scalar critical coefficient on these seams

The PF-175 first-relative-resolvent form separates a cotangent coefficient `C=\rho A-I` from the scalar density coefficient

\[
b=\rho-1.
\tag{24}
\]

PF-182's seam smoothing is exactly area preserving. Therefore `\rho=1` throughout every seam correction and

\[
\boxed{b=0.}
\tag{25}
\]

The critical coefficient budget in (6) is consequently the whole local metric coefficient introduced by the distinguished-cuff seam smoothing; there is no parallel density term whose concentration must be paid separately.

This does not mean that the **operator** supported near the seam has been estimated. It means only that its coefficient satisfies the same critical Orlicz currency used by Ponge's matrix-valued two-dimensional theorem and by PF-196--PF-201.

## 4. Why PF-201 cannot simply be copied to the shrinking seam family

PF-201 succeeds on the regular Lambert body because the coefficient windows admit fixed-width buffers in one uniformly elliptic `C^1` chart family. The global-to-local maps

\[
f\mapsto
(\Lambda J_\alpha\vartheta_\alpha dR_k f)_\alpha
\tag{26}
\]

then have a uniform square-function bound, while the torus critical operators are block diagonal.

PF-182 deliberately obtains (9) by allowing the seam neighborhoods to become arbitrarily thin. Although its first derivative distortion remains controlled, the construction does not assert uniform higher derivatives of the corrected metric/map after rescaling those neighborhoods, nor one fixed support buffer in which the localized `H^2`/pseudodifferential constants remain independent of `n`. Therefore (6) does **not** justify inserting the seam family directly into PF-201's `A_h^*DA_g` factorization with a uniform constant.

The next analytic test is precise. Either prove that the actual PF-182 seam family can be localized with constants `K_n` satisfying

\[
\sum_n K_n
\|C\mathbf1_{U_n}\|_{L_\Phi}<\infty
\tag{27}
\]

on both sides, exploiting the freedom in (8) to dominate any known finite cuffwise growth, or find a different trace/weak-trace estimate that bypasses shrinking-chart pseudodifferential constants. An estimate that merely assumes the PF-200 regular-body uniformity on `U_n` would be circular.

## Prior art and novelty audit

The critical `L\log L` coefficient space and its weak-`S_1` role are classical Cwikel--Solomyak theory; PF-196 audits the relevant Sukochev--Zanin formulation and PF-197/PF-200 use Ponge's matrix-valued manifold theorem recorded as S20 in `research/prime_flute/SOURCES.md`. The Luxemburg estimate (19), the concentration logarithm, and the fact that `q\log(1/q)\to0` are elementary. PF-182's conservative pasting mechanism is already literature-audited there. No new Orlicz, symplectic-pasting, or Cwikel theorem is claimed.

A targeted audit of the local critical Cwikel literature used by PF-196--PF-201 does not supply the missing project-specific implication that arbitrarily thin conservative seam supports retain uniform pseudodifferential localization constants. Search absence is not treated as a novelty theorem.

The project-specific deduction is the compatibility of two persisted mechanisms that had not previously been combined: **PF-182's arbitrary support-budget freedom is strong enough to absorb PF-196's unavoidable critical concentration logarithm.** Thus the distinguished decomposition cuffs no longer carry an unresolved coefficient-space endpoint loss; only their operator localization constants remain to be controlled.

## Falsification and boundary checks

A later adversary can test PF-202 by checking that:

1. PF-182 really permits an arbitrary prescribed summable `q_n` while retaining the pointwise `O(\delta_n)` seam distortion on source and inverse/target sides;
2. the quotient-ball inequality (12) has the stated direction, so the inverse-unit-ball weight has the lower bound (13);
3. PF-175's coefficient comparison on the tail quasi-isometry range gives (15), with exact area setting `b=0`;
4. the matrix-valued Luxemburg norm is bounded by applying PF-196's scalar inequality to the pointwise matrix norm;
5. the choice (22)--(23) is made **before** invoking PF-182, so no fixed support sequence is being retroactively changed;
6. no weak-`S_1` operator conclusion is inferred without controlling the seam-family localization constants or replacing them by another operator estimate.

PF-202 must be narrowed if PF-182's arbitrary support choice necessarily destroys its uniform first-derivative bound, or if the PF-175 cotangent coefficient is not pointwise controlled by the recorded seam metric deviation on the common quasi-isometry range. Growth of higher derivatives or local Cwikel constants would not refute (6); it would realize exactly the operator-level boundary stated above.

## Consequences for the research line

PF-201 closes the entire **regular Lambert-body principal cotangent sector** in weak `S_1`. PF-202 now closes a different issue for one of the remaining exceptional families: the distinguished decomposition-cuff corrections can carry an arbitrarily small summable **critical coefficient** budget despite their shrinking supports. The weak-endpoint frontier should therefore stop treating seam coefficient concentration itself as a possible source of the missing logarithmic loss.

The next interface question is whether the support-thinning freedom can also pay the actual localized operator constants, or whether a width-dependent analytic obstruction survives even though the coefficient norm is arbitrarily summable. Separately, the PF-138 true-short-collar family still requires the canonical endpoint conservative splice; PF-202 does not weaken that geometric gate.