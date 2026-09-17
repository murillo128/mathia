# PL-336 — Uniform sup control closes the first-prime source gate

**Evidence:** `LITERATURE+EXACT-DERIVED + CONDITIONAL-REDUCTION + ROUTE-NARROWING`

**Status:** `FIRST-PRIME-SIGN-GATE-REDUCED-TO-UNIFORM-LINFTY + NO-LINFTY-THEOREM-YET + NO-RH-CONSEQUENCE`

## Precise claim

The sequence `PL-329`--`PL-335` leaves one branch-specific obstruction at the first rational-prime activation

\[
a_0=\frac12\log2,
\qquad
a_\delta=a_0+\delta,
\qquad
L_\delta=\log\frac{a_\delta}{\delta}\to\infty.
\]

For the normalized simple odd eigenbranch `u_delta` of Suzuki's localized Weil operator on the fixed interval `(-1,1)`, assume that for some `delta_0>0`

\[
\boxed{
\sup_{0\le\delta\le\delta_0}\|u_\delta\|_{L^\infty(-1,1)}<\infty.
}
\tag{PL336-1}
\]

Then the actual zero-order source in the endpoint logarithmic-Laplacian equation is uniformly bounded:

\[
\boxed{S_\delta=O(1).}
\tag{PL336-2}
\]

Consequently the sharp Dirichlet logarithmic-Laplacian boundary estimate of source 97 gives a uniform critical envelope

\[
|g_\delta(Q)|\le A Q^{-1/2}
\qquad(Q\ge Q_0),
\tag{PL336-3}
\]

and `PL-329` yields source-selected coefficients `C_delta` with the uniform remainder

\[
\boxed{
|g_\delta(Q)-C_\delta Q^{-1/2}|
\le \frac{K}{Q}+Ke^{-\eta(Q-R)}.
}
\tag{PL336-4}
\]

The norm-resolvent/simple-branch continuity of `PL-330` gives `u_delta -> u_0` in `L^2`; hence `PL-332` applies to (PL336-4) and gives

\[
C_\delta\longrightarrow C_0.
\tag{PL336-5}
\]

At `delta=0`, the same bounded-source argument gives the actual quotient expansion

\[
u_0(1-2e^{-Q})=C_0Q^{-1/2}+O(Q^{-1}),
\tag{PL336-6}
\]

so the antisymmetric Hopf lower law of `PL-335` forces

\[
\boxed{C_0>0.}
\tag{PL336-7}
\]

Therefore `C_delta` is uniformly separated from zero for small positive `delta`. Since `S_delta=O(1)`, the sharp orientation criterion of `PL-329` becomes

\[
\frac{1+S_\delta}{|C_\delta|\sqrt{L_\delta}}
=O(L_\delta^{-1/2})\longrightarrow0.
\tag{PL336-8}
\]

Thus **uniform `L^infty` control of the actual odd eigenbranch is sufficient to close the entire first-prime reflected-correlation sign gate isolated in `PL-329`**.

This is a reduction, not a proof of (PL336-1). The present audit found no theorem already in the line's literature that upgrades the available normalized `L^2`/graph continuity across the moving compressed `p=2` shift to an aperture-uniform `L^infty` bound. In particular, source 97 assumes bounded state and bounded forcing; using it to prove (PL336-1) would be circular.

## 1. The eigen-equation turns uniform state control into uniform source control

On the fixed interval representation used in `PL-291` and `PL-319`, Suzuki's localized Weil operator has the form

\[
A_a=\frac12L_\Delta+\gamma I+K_a,
\tag{PL336-9}
\]

where `K_a` contains the scalar aperture term, the finitely active compressed prime-power translations, and the continuous archimedean completion kernel. In a sufficiently small right neighborhood of `a_0`, the only newly moving rational-prime term is the `p=2` translation from source 56.

For an eigenpair

\[
A_{a_\delta}u_\delta=\lambda_\delta u_\delta,
\]

we therefore have

\[
L_\Delta u_\delta
=2(\lambda_\delta-\gamma)u_\delta-2K_{a_\delta}u_\delta.
\tag{PL336-10}
\]

Every component on the right is uniformly bounded on `L^infty` in a compact aperture neighborhood. The compressed `p=2` shift has `L^infty` norm at most one and fixed coefficient `Lambda(2)/sqrt(2)`. The scalar coefficient is continuous in `a`. The archimedean completion is an integral operator whose kernel is continuous on the relevant compact `(a,x,y)` set, so

\[
\sup_{a\in[a_0,a_0+\delta_0]}
\sup_x\int_{-1}^1|k_a(x,y)|\,dy<\infty.
\tag{PL336-11}
\]

The eigenvalues `lambda_delta` stay bounded by the norm-resolvent/simple-branch continuity already established in `PL-330`. Hence (PL336-1) implies

\[
\sup_{0\le\delta\le\delta_0}
\|L_\Delta u_\delta\|_\infty<\infty.
\tag{PL336-12}
\]

In the endpoint coordinate

\[
x_Q=1-2e^{-Q},
\qquad
g_\delta(Q)=u_\delta(x_Q),
\]

the source `F_delta(Q)` of `PL-329` is exactly `(L_Delta u_delta)(x_Q)` after the harmless fixed bulk/tail split described in `PL-319`; the bulk contribution has a uniformly finite endpoint source. Thus (PL336-12) gives (PL336-2).

The point is specific to the actual zero-order eigen-equation. A generic `L^2`-small boundary layer need not have bounded source: `PL-329` shows that the hostile critical layer of `PL-327` has `S_delta asymp sqrt(L_delta)`.

## 2. Bounded state and bounded source give the uniform critical boundary envelope

Source 97 proves the sharp boundary regularity for the Dirichlet logarithmic Laplacian with bounded forcing and bounded solution. On the fixed interval `(-1,1)`, its estimate has the canonical scale

\[
\ell(d)^{1/2}
\asymp
|\log d|^{-1/2}
\qquad(d\downarrow0).
\tag{PL336-13}
\]

Under (PL336-1) and (PL336-12), the norms entering that theorem are bounded uniformly in `delta`, while the domain is fixed. Therefore its boundary constant can be chosen uniformly for the branch, and with `d=2e^{-Q}` we obtain

\[
|u_\delta(1-2e^{-Q})|
\le A Q^{-1/2}
\tag{PL336-14}
\]

for all sufficiently large fixed `Q_0`, uniformly in small `delta`. This is precisely hypothesis (PL329-2).

Now (PL336-2) supplies the other variable quantity in the `PL-329` estimate. Formula (PL329-4) therefore becomes (PL336-4) with constants independent of `delta`.

This step is deliberately one-way. The boundary theorem cannot be invoked with merely `u_delta in L^2`: boundedness of both the state and the forcing is part of the theorem's input. Nor can (PL336-12) be obtained from the eigen-equation before controlling the compressed shift pointwise, since that shift simply transports the unknown state without smoothing it.

## 3. The same hypothesis also fixes the threshold coefficient

`PL-335` establishes at `delta=0` the antisymmetric Hopf lower law

\[
\liminf_{Q\to\infty}
\sqrt Q\,u_0(1-2e^{-Q})>0.
\tag{PL336-15}
\]

By itself that lower law did not prove existence of a boundary quotient. Under (PL336-1), however, the threshold state has bounded zero-order source by the same argument as above. Applying the `PL-329` source-selection estimate at `delta=0` gives (PL336-6), hence the quotient exists and equals `C_0`. Combining (PL336-6) with (PL336-15) yields `C_0>0` exactly.

For positive `delta`, `PL-330` supplies aligned `L^2` convergence of the simple odd branch, and the uniform `O(Q^{-1})` remainder (PL336-4) is exactly the extra tail control required by `PL-332` to transport the boundary coefficient. Therefore

\[
C_\delta\to C_0>0.
\tag{PL336-16}
\]

In particular there are `c>0` and `delta_1>0` such that

\[
C_\delta\ge c
\qquad(0\le\delta\le\delta_1).
\tag{PL336-17}
\]

Substitution into the sharp criterion (PL329-7) proves (PL336-8) and hence eventual positivity of the newly active `p=2` reflected correlation.

The reduction is therefore stronger than saying merely that a bounded source would help. For the actual odd eigenbranch, a single uniform state estimate (PL336-1) simultaneously supplies the bounded source, the critical boundary envelope, existence/noncollapse of the threshold coefficient, transport of that coefficient, and the strict subcriticality of the source amplitude relative to the `sqrt(L_delta)` obstruction.

## 4. Why the missing `L^infty` estimate is genuinely stronger than the existing branch topology

`PL-330` proves norm-resolvent continuity and hence `L^2` and graph continuity of the simple branch across the first-prime activation. `PL-331` strengthens the negative control: the hostile first-prime boundary layer can vanish in every fixed logarithmic Fourier topology while still producing the critical source growth and reversing the reflected sign. Thus none of the already established fixed-order/log-moment topologies implies (PL336-1).

The difficulty is natural for the logarithmic Laplacian. Its symbol grows only logarithmically, so the usual finite-order Sobolev route from graph control to `L^infty` is unavailable. The newly active compressed translation is bounded but non-smoothing. Moreover `PL-324`--`PL-335` show that the odd Beurling--Deny order structure is exact only up to the threshold; once `p=2` has positive-measure overlap, the cross-half translation destroys the simple positivity argument. There is therefore no justified maximum-principle shortcut from the existing odd threshold positivity to a uniform post-threshold sup bound.

Pure Dirichlet logarithmic-Laplacian eigenfunctions are known to be bounded and continuous in the standard theory, and source 97 gives strong boundary regularity once boundedness is available. Those facts do not by themselves provide a constant uniform under the aperture-dependent bounded nonlocal perturbation in (PL336-10). A valid closure theorem must control the actual family, not merely each fixed `delta` separately.

This leaves a concrete analytic target. It would suffice to prove an estimate of the form

\[
\|u\|_\infty
\le C\bigl(\|u\|_2+\|(A_a-\lambda)u\|_X\bigr)
\tag{PL336-18}
\]

with a branch-appropriate right-hand side and `C` uniform for `a` near `a_0`, or any equivalent compactness/regularity theorem preventing concentration of normalized eigenstates in the shrinking `p=2` boundary layer. Formula (PL336-18) is only a target template, not an asserted estimate.

## 5. Novelty and adversarial audit

The ingredients used here are prior art or earlier line results. Suzuki's source 56 supplies the localized Weil operator and the moving rational-prime translations. Source 97 supplies sharp `ell(d)^{1/2}` boundary control under bounded-state/bounded-forcing hypotheses. `PL-329` gives the sharp `sqrt(L_delta)` source threshold, `PL-330` gives branch continuity, `PL-332` gives boundary-coefficient continuity under a uniform source-selected residual, and `PL-335` gives the positive odd threshold Hopf coefficient.

The exact derived contribution is the reduction: in the actual localized-Weil eigen-equation, **uniform `L^infty` control is enough to supply every remaining hypothesis of those four findings and therefore closes the first rational-prime sign gate**. A targeted literature audit around logarithmic-Laplacian eigenfunctions with bounded potentials/nonlocal bounded perturbations did not locate a theorem that provides the required aperture-uniform estimate for this moving compressed-shift family. Search absence is not treated as broad novelty.

Adversarial boundaries:

- **Conditional only.** No proof of (PL336-1) is given here. The first-prime sign problem is reduced to that estimate, not solved unconditionally.
- **No circular boundary regularity.** Source 97 assumes `L^infty` state/forcing and is used only after (PL336-1) has supplied them through the eigen-equation.
- **No generic bounded-perturbation regularity claim.** The compressed `p=2` shift is non-smoothing and operator-norm discontinuous at activation. Standard perturbation language does not imply uniform `L^infty` control.
- **No recovery from fixed log moments.** `PL-331` explicitly rules out treating all fixed logarithmic Fourier seminorms as a surrogate for the needed sup estimate.
- **No post-threshold positivity theorem.** The odd modulus mechanism of `PL-324` is not extended past `a_0`; `PL-335` is used only at the exact threshold.
- **No universal endpoint effect.** The implication uses the actual source relation of the completed-Weil branch. Generic critical boundary layers remain capable of saturating the `sqrt(L_delta)` obstruction.
- **No RH proof.** Positivity of the first newly active rational-prime correlation on one odd branch does not establish Weil positivity at all apertures or for all test vectors.

## Consequence for the research line

After `PL-336`, the first-prime continuation problem no longer has several independent analytic gates. For the odd simple branch they collapse to one falsifiable estimate:

\[
\boxed{
\sup_{a\downarrow a_0}\|u_a\|_\infty<\infty.
}
\tag{PL336-19}
\]

If (PL336-19) holds, `PL-329` + `PL-332` + `PL-335` force the first-prime reflected correlation to have the favorable sign. If it fails, the failure must occur through genuine sup-norm concentration invisible to the already controlled `L^2`, graph, and fixed-log-moment topologies. Either outcome is structurally informative: the next pass should therefore target uniform boundedness/concentration for the actual moving compressed-shift eigenbranch rather than adding another endpoint seminorm.