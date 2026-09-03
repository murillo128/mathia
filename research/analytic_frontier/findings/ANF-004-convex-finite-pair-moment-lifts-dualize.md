# ANF-004 — convex finite pair-moment lifts have single signed-profile dual witnesses

**Status:** `EXACT-DERIVED + CLASSICAL-CONVEX-DUALITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT` for attempts to obtain genuinely new support-one pair-correlation information merely by retaining finitely many globally summed pair observables and then combining them through an affine or convex lower-bound certificate. Such a certificate has, at the asymptotic BGSST moment point, an equally strong single **signed scalar** support-one witness. This does not prove a Montgomery--Taylor ceiling for the signed class and does not rule out nonconvex, configuration-level, wider-support, or higher-order information.

## 1. Exact affine collapse

Let `Z` be a finite conjugation-invariant multiset, let `n=|Z|`, and let

\[
r(Z)=\frac{\#\{z\in Z\cap\mathbb R:m_z=1\}}{n}
\]

be its simple-real proportion. Suppose a proposed extension of the Lamzouri/BGSST method keeps `m` globally summed pair observables

\[
e_j(Z)=\frac1n\sum_{z,s\in Z}F_j(z-s),
\qquad 1\le j\le m,
\tag{1}
\]

where every `F_j` is the Fourier transform, after whatever standard Montgomery-weight correction is required, of a real-even profile `J_j` supported in `[-1,1]` and lying in the unconditional BGSST test class.

Assume first that the deterministic zero-side argument proves an affine bound

\[
r(Z)\ge a+\sum_{j=1}^m b_j e_j(Z)
\tag{2}
\]

for every finite conjugation-invariant `Z`. By linearity,

\[
\sum_{j=1}^m b_j e_j(Z)
=
\frac1n\sum_{z,s\in Z}F_{\rm eff}(z-s),
\qquad
F_{\rm eff}:=\sum_{j=1}^m b_jF_j.
\tag{3}
\]

The corresponding Fourier-side profile is simply

\[
J_{\rm eff}=\sum_{j=1}^m b_jJ_j.
\tag{4}
\]

A finite linear combination preserves real-evenness, support in `[-1,1]`, and the regularity hypotheses used by the BGSST formula. Hence the arithmetic evaluation of (2) is exactly the evaluation of one scalar support-one profile. The coefficients `b_j` need not be positive, so `J_eff` can be signed.

Thus **affine multi-observable jointness is representational, not informational**: once only the global sums (1) survive into the counting inequality, there is no mathematical distinction between `m` observables and the single signed observable (3).

## 2. Convex lower-bound aggregators have an equally strong affine witness at the BGSST point

The same reduction extends beyond an explicitly affine certificate. Let

\[
e(Z)=(e_1(Z),\ldots,e_m(Z))\in\mathbb R^m
\]

and suppose the deterministic argument proves

\[
r(Z)\ge G(e(Z)),
\tag{5}
\]

where `G` is finite and convex on a neighborhood, or on the relevant relative interior, of the asymptotic moment point

\[
e(Z_T)\longrightarrow c=(c_1,\ldots,c_m)
\tag{6}
\]

provided by the unconditional pair-correlation theorem. Assume `G` has a subgradient `g` at `c`. The supporting-hyperplane inequality gives

\[
G(x)\ge G(c)+g\cdot(x-c)
\tag{7}
\]

for every admissible `x`. Combining (5) and (7),

\[
r(Z)
\ge
\bigl(G(c)-g\cdot c\bigr)+g\cdot e(Z).
\tag{8}
\]

At `e=c`, the affine right-hand side is exactly `G(c)`. Therefore the asymptotic lower bound produced by the convex multi-moment certificate has an affine supporting witness of **identical strength at the BGSST limit point**. By Section 1, that affine witness is one signed scalar support-one profile

\[
J_g=\sum_{j=1}^m g_jJ_j.
\tag{9}
\]

No claim is being made that `G` equals its supporting hyperplane away from `c`. The point is narrower: if the number-theoretic input supplies only the limiting finite vector `c`, then convex curvature away from that point cannot improve the final asymptotic constant beyond what one supporting affine functional already certifies there.

If `c` lies on a boundary where an exact subgradient is unavailable, an approximate supporting-hyperplane statement may still hold under the usual closed-convex hypotheses, but that boundary case is not included in the exact claim above.

## 3. What this says about finite LP/SDP/conic moment lifts

Many proposed “joint observable” constructions can be expressed as a finite-dimensional convex program whose external data are precisely the moment coordinates `e_j`. In a lower-bound formulation for which strong conic duality holds and the certified value is represented by a supremum of affine functions of these moment data, an optimal dual solution at `c` supplies exactly the coefficient vector `g` in (8).

Consequently, **the existence of a matrix variable, a positive-semidefinite constraint, or an SDP solver does not by itself mean that the zeta argument has consumed matrix-valued information**. If all configuration dependence has already been compressed into finitely many global pair sums before the convex program is applied, the final dual certificate is one signed scalar combination of those sums.

This is an information-boundary statement, not an objection to semidefinite optimization. Chirre--Gonçalves--de Laat use semidefinite programming very effectively to optimize a broader Cohn--Elkies auxiliary-function class under RH. Their gain comes from an enlarged admissible function/sign regime and the associated additional pair-correlation control, not from the mere fact that the numerical optimization is semidefinite. Their paper explicitly describes the reduction to convex optimization after replacing the usual bandlimited class by the Cohn--Elkies class.

For the unconditional Mathia question, an SDP may likewise be an excellent **search mechanism** for a signed support-one witness. But if its only number-theoretic inputs are finitely many BGSST moments, the SDP output must ultimately be interpretable through a scalar dual profile if the formulation falls under the convex-duality hypotheses above.

## 4. Fixed linear readout also scalarizes operator-valued translation kernels

`ANF-003` showed scalarization for common-translation vector features followed by scalar Gram compression. The same boundary can be stated directly at the operator-valued spectral level.

Let `K(t)` be a translation-invariant operator-valued positive-definite kernel with an operator-valued spectral representation

\[
K(t)=\int e^{-2\pi iut}\,dM(u),
\tag{10}
\]

where `M` is a positive operator-valued measure, as in the classical vector-valued translation-invariant kernel framework. If the zero-side certificate applies one fixed bounded linear functional `\ell` to each kernel value before globally summing pairs, then

\[
\ell(K(t))
=
\int e^{-2\pi iut}\,d\mu_\ell(u),
\qquad
\mu_\ell(E):=\ell(M(E)).
\tag{11}
\]

Thus a fixed trace, matrix entry, fixed quadratic form, or fixed linear combination of entries produces one scalar spectral measure. When the readout is positive, the scalar measure is positive; a general self-adjoint readout can produce a signed scalar measure.

Accordingly, operator-valued Bochner structure is genuinely richer only if the deterministic counting argument **uses the operator/matrix order or several entries before reducing them to a fixed linear readout**. A matrix kernel followed immediately by one trace or one fixed dual matrix is again a scalar pair profile.

The general representation theory here is classical. Carmeli--De Vito--Toigo--Umanità explicitly characterize translation-invariant vector-valued kernels on abelian groups. The present consequence is the specialization relevant to the BGSST information interface.

## 5. Why this does not reproduce the Montgomery--Taylor no-go

The effective profile `J_eff` or `J_g` in (4)/(9) is generally **signed**. This is the central boundary of the result.

The Carneiro--Chandee--Littmann--Milinovich extremal theorem used in `ANF-002` controls Lamzouri's positive one-factor class `K=\widehat{\eta^2}` with the squared-kernel observable. `ANF-003` extends that no-go to common-translation vectorizations that still reduce to one nonnegative spectral density. `WI-118` separately rules out universal termwise-nonnegative support-one extraction because positivity forces endpoint taper and screening.

None of those results proves that every **signed** real-even BGSST-legal profile must have normalized constant at least `C_MT`. Indeed `WI-118` exhibits the opposite structural possibility: a non-tapered support-one profile can retain an order-density boundary alias precisely by allowing its real-axis kernel to change sign.

So `ANF-004` does not close the support-one second-order route. It identifies its honest normal form:

\[
\boxed{\text{finite affine/convex global pair-moment lift}
\quad\Longrightarrow\quad
\text{one signed scalar support-one dual witness}.}
\tag{12}
\]

The hard problem is then to prove a universal RH-free **global** counting inequality for such a signed profile. BGSST can evaluate the profile; the missing ingredient is deterministic control of the signed cross-height reservoir without termwise positivity.

## 6. Consequence for the live semidefinite clue

The accepted `CLUE-semidefinite-pair-correlation-horizontal-lift` should no longer treat a finite convex collection of global pair sums as automatically “genuinely joint” information. Before studying a proposed LP/SDP/conic lift, extract its dual at the asymptotic BGSST point. If the dual is a fixed affine combination of the legal moments, replace the whole construction conceptually by its signed effective profile and ask whether the required deterministic inequality is actually valid for arbitrary conjugation-invariant complex multisets.

This gives a concrete audit prediction for the unaudited multi-profile improvement mentioned in `ANF-002`/`WI-001`: **if** that proposal is ultimately a convex finite-moment certificate using only unconditional support-one pair sums and satisfies ordinary strong duality, an equivalent signed scalar dual profile should exist at its asymptotic point. Failure to extract one would indicate either that the mechanism uses genuinely configuration-level/nonconvex information or that the proposed interpretation of its inputs is incomplete. This is a diagnostic, not a verdict on that external claim.

The smallest surviving targets are now sharply separated:

- a single signed support-one scalar pair profile with a new conjugation-invariant global counting inequality and constant `< C_MT`;
- a genuinely nonconvex or configuration-dependent matrix certificate whose value cannot be replaced at the BGSST point by an affine moment witness;
- operator/matrix order retained before global scalar summation;
- wider Fourier support or genuinely higher-order zero correlations.

## 7. Prior-art and novelty assessment

Linearity of Fourier transforms and pair sums, the supporting-hyperplane/subgradient theorem for convex functions, strong duality for appropriate finite conic programs, and scalarization of an operator-valued measure under a fixed linear functional are classical facts. No novelty is claimed for any of them.

Chirre--Gonçalves--de Laat, **Pair Correlation Estimates for the Zeros of the Zeta Function via Semidefinite Programming**, *Advances in Mathematics* 361 (2020), 106926, explicitly use a convex/SDP optimization after enlarging the auxiliary-function class; their result remains RH-conditional and therefore does not supply the missing unconditional signed complex-zero inequality. Carmeli--De Vito--Toigo--Umanità provide the operator-valued translation-kernel prior-art boundary already anchored in `SOURCES.md`.

The Mathia-specific contribution is the exact interface reduction (12): **finite convex jointness after global pair compression is not itself additional BGSST information**. Any improvement in that class can be represented at the limiting moment point by one signed scalar support-one witness. This narrows the live question from “find a sufficiently clever finite SDP” to “find the signed scalar dual inequality that the SDP would have to be discovering, or retain genuinely richer information before global moment compression.”

## 8. Falsification and boundary conditions

The finding would be falsified by an affine certificate depending only on finitely many global BGSST pair sums whose value cannot be represented by the linear combination (3), or by a convex subdifferentiable lower-bound aggregator at `c` for which no supporting affine minorant with equality at `c` exists. Both would contradict elementary linearity/convexity.

It does **not** apply when the arithmetic input contains more than the finite limiting vector `c`; when the certificate uses finite-`T` covariance or joint fluctuations not determined by the individual pair asymptotics; when a matrix/eigenvalue/inertia statistic is applied before global summation; when the aggregator is genuinely nonconvex in the relevant sense; when support exceeds one; or when higher-order correlations enter. It also does not assert that every abstract signed profile admits a valid deterministic simple-real counting inequality.

The decisive next test is therefore not another generic vectorization. It is to construct or rule out the first signed support-one profile `J` for which (i) the BGSST evaluation is unconditional, (ii) a global conjugation-invariant deterministic inequality controls simple-real points despite sign-changing cross-height terms, and (iii) the resulting asymptotic constant is strictly below `C_MT`.