# PL-309 — Small-order Green traces sample an exponentially thin boundary layer

**Evidence:** `LITERATURE+EXACT-DERIVED + NEGATIVE/GATE-NARROWING`

**Status:** `EXACT-1D-TRACE-RESCALING + BULK-CONVERGENCE-NO-GO + COMPLETED-WEIL-SOURCE-STRUCTURE-STILL-OPEN`

## Precise claim

Let `I=(-1,1)`, `0<s<1/2`, and let `u_s` solve `(-Delta)^s u_s=f_s` in `I` with zero exterior data `u_s=0` on `R\I`. Define

\[
\tau_{s,+}=\lim_{x\to1^-}\frac{u_s(x)}{(1-x)^s}.
\]

Bucur's explicit Green function for the one-dimensional unit ball gives

\[
\boxed{
\tau_{s,+}=\frac{2^{-s}s}{\Gamma(1+s)^2}
\int_{-1}^{1}(1-y)^{s-1}(1+y)^s f_s(y)\,dy .
}
\tag{PL309-1}
\]

With `t=(1-y)/2` and the exact stretched coordinate `t=e^{-r/s}`,

\[
\boxed{
\tau_{s,+}=\frac{2^s}{\Gamma(1+s)^2}
\int_0^\infty e^{-r}(1-e^{-r/s})^s
f_s(1-2e^{-r/s})\,dr .
}
\tag{PL309-2}
\]

Thus fixed `r=O(1)` samples the forcing at physical distance `1-y=2e^{-r/s}` from the boundary. The trace probes an exponentially thin layer as `s->0`. Its positive kernel has exact total mass

\[
\boxed{\frac{2^s}{\Gamma(1+2s)}\to1.}
\tag{PL309-3}
\]

Consequently ordinary bulk convergence of the forcing does not determine the renormalized trace `tau_{s,+}/sqrt(s)`. Choose nonzero `psi in C_c^infty((r_0,r_1))`, with `0<r_0<r_1`, and set

\[
f_s(1-2t)=\sqrt{s}\,\psi(-s\log t),\qquad0<t<1.
\tag{PL309-4}
\]

Every `f_s` is smooth and supported strictly inside `I`, and `||f_s||_infty=O(sqrt(s))->0`, but

\[
\boxed{
\frac{\tau_{s,+}}{\sqrt{s}}
\longrightarrow\int_0^\infty e^{-r}\psi(r)\,dr .
}
\tag{PL309-5}
\]

The limit can be prescribed by rescaling `psi`. Hence

\[
\boxed{
\|f_s\|_\infty=O(\sqrt{s})
\not\Longrightarrow
\tau_{s,+}=o(\sqrt{s}).
}
\tag{PL309-6}
\]

This is **not** a counterexample for the actual completed-Weil regularized eigenbranch, whose forcing is tied to the state by its eigen-equation. It rules out only a generic inference from bulk `C_0`, `L^infty`, norm-resolvent, or ordinary forcing convergence to the renormalized boundary trace or squared stress.

## Derivation and normalization audit

For `n=1`, `0<s<1/2`, Bucur's Theorems 3.1 and 3.3 give

\[
G_s(x,y)=\kappa(1,s)|x-y|^{2s-1}
\int_0^{r_0(x,y)}\frac{q^{s-1}}{(1+q)^{1/2}}\,dq,
\]

\[
r_0(x,y)=\frac{(1-x^2)(1-y^2)}{|x-y|^2},
\qquad
\kappa(1,s)=\frac{1}{2^{2s}\Gamma(s)^2}.
\]

The exceptional case `n=2s` is irrelevant in this small-order range. If `delta=1-x`, then `1-x^2~2delta`, `|x-y|->1-y`, and the small-upper-limit integral is `r_0^s/s(1+o(1))`. Therefore

\[
\lim_{x\to1^-}\frac{G_s(x,y)}{(1-x)^s}
=\frac{2^{-s}s}{\Gamma(1+s)^2}(1-y)^{s-1}(1+y)^s,
\]

and Bucur's zero-exterior Green representation yields (PL309-1). The beta integral gives (PL309-3), while the two substitutions above give (PL309-2). For (PL309-4), the support satisfies

\[
1-y\in[2e^{-r_1/s},2e^{-r_0/s}],
\]

so it is compactly contained in `I` for each fixed `s`, and dominated convergence proves (PL309-5).

A stronger rate `||f_s-g_s||_infty=o(sqrt(s))` would suffice by (PL309-3). What fails is inference from ordinary `o(1)` bulk convergence, or even from a generic `O(sqrt(s))` perturbation.

## Relation to the live `PL-308` gate

`PL-308` proves for the actual completed-Weil regularized state at every fixed order

\[
\frac{\Gamma(1+s)^2}{2s}(|\tau_+|^2+|\tau_-|^2)
=E_s(w)+a^{2s}[b_a(w)+V_a(w)].
\]

The unresolved analytic problem is the singular `s->0` limit: identify the weak lower virial `V_a(w_{s,a})`, or obtain enough source-structured `C_0+BV`/derivative-measure compactness to replace it by the explicit fixed-state aperture derivative from `PL-305`.

The Green representation is not an automatic shortcut. It can help only if the actual completed-Weil equation yields source-specific control on the stretched profile

\[
r=-s\log\frac{1-x}{2}.
\]

Otherwise the weak-virial/BV route remains the robust scalar formulation.

## Prior-art and novelty audit

The Green kernel, normalization, and zero-exterior representation are prior art; Bucur's exposition itself presents them as established stable-process potential theory. No novelty is claimed for the kernel or for the general observation that `delta^s` varies on exponential scales at small order.

A structure-based search around small-order fractional Laplacians, Green/Martin kernels, boundary traces, and logarithmic-Laplacian limits found established small-order eigenfunction convergence and fixed-order boundary regularity, but no theorem turning ordinary bulk `C_0` convergence into convergence of the `s^{-1/2}` quotient. Search absence is not used as evidence of novelty.

The durable line-local result is the exact obstruction (PL309-6): the classical Green kernel supplies an explicit smooth forcing family with vanishing `L^infty` norm but arbitrary finite renormalized trace. This narrows the zero-order boundary-stress program without claiming a failure of the structured completed-Weil branch.

## Boundary conditions and falsification controls

- The proof uses only `0<s<1/2`, sufficient for the zero-order limit.
- The right-endpoint distance is exactly `1-x`; no hidden factor of two enters the quotient.
- The counterexample forcing is smooth for each fixed `s` because `psi` is compactly supported away from `r=0` and infinity.
- It is an externally prescribed fractional Poisson forcing, not a completed-Weil eigenforcing.
- There is no conflict with `PL-308`, whose virial identity exploits the eigen-equation and dilation covariance absent here.
- No rational-prime-specific sign is obtained.

## Consequence for the research line

After `PL-308`, fixed-order boundary stress is rigorous. `PL-309` rules out a generic bulk-convergence passage to zero order: the renormalized observable lives on an `exp(-Theta(1/s))` boundary layer. A viable continuation must either control the actual completed-Weil branch on that stretched scale or prove uniform small-`s` convergence of the weak virial, potentially through the `C_0+BV`/derivative-measure mechanism of `PL-305`. Only after that analytic gate is closed does the separate rational-prime first-crossing sign problem remain.

## Sources

- Claudia Bucur, “Some observations on the Green function for the ball in the fractional Laplace framework,” *Communications on Pure and Applied Analysis* **15**(2) (2016), 657–699. DOI: https://doi.org/10.3934/cpaa.2016.15.657. arXiv: https://arxiv.org/abs/1502.06468. Theorems 3.1--3.3 supply the unit-ball Green kernel, zero-exterior representation, and normalization.
- `PL-305`: exact fixed-state aperture derivative for the lower completed-Weil form under `C_0 cap BV_0`.
- `PL-308`: fixed-order transmission admissibility and exact weak-virial boundary-stress identity for the completed-Weil fractional regularization.
