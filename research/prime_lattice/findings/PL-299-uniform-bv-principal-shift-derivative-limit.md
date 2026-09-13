# PL-299 — Uniform BV compactness passes the pure fractional prime-shift derivative to the logarithmic limit

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-ROUTE-REFINEMENT + PURE-BRANCH-UNIFORMIZATION`

**Status:** `PURE-PRINCIPAL-SHIFT-LIMIT-RESOLVED + PERTURBED-WEIL-BRANCH-OPEN`

## Claim

The small-order obstruction left open by `PL-298` is absent for the canonical one-dimensional **pure principal fractional branch**. Let `I=(-R,R)`, let `u_s` be the positive `L^2`-normalized first zero-exterior Dirichlet eigenfunction of `(-Delta)^s` on `I`, and let `u_0` be the positive normalized first eigenfunction of the Dirichlet logarithmic Laplacian obtained in the limit `s->0+`. Extend all states by zero outside `I` and set

\[
C_s(h):=\int_{\mathbb R}u_s(x)u_s(x+h)\,dx.
\]

Then

\[
\boxed{C_s\longrightarrow C_0\quad\text{in }C^1(\mathbb R)\qquad(s\to0^+).}
\]

In particular every fixed nonzero prime-power lag `h=log(n)/a` has a genuine zero-order derivative limit

\[
\boxed{C_s'(\log n/a)\longrightarrow C_0'(\log n/a),}
\]

and the convergence is uniform in the lag `h`, including across the support-edge activation point.

The mechanism is **uniform bounded variation**, not a critical Fourier moment. Feulefack--Jarohs--Weth prove uniform convergence `u_s->u_0` on the closed interval and a uniform `L^infty` bound. Symmetric decreasing rearrangement plus simplicity of the principal eigenvalue lets every `u_s` be chosen even and nonincreasing on `(0,R)`. Hence its zero extension satisfies

\[
\operatorname{TV}(u_s)=2u_s(0)\le 2\sup_{0<t\le s_0}\|u_t\|_\infty,
\]

uniformly as `s->0+`. This compactness is enough to pass the autocorrelation derivatives through the singular order limit even though `PL-297` shows that the zero extensions cannot have a uniform `H^{1/2}` bound.

This resolves only the **pure principal fractional/logarithmic branch**. It does not prove uniform BV, fixed sign, or derivative convergence for the actual boundedly perturbed completed-Weil eigenbranch.

## 1. Small-order uniform convergence and monotone geometry

Feulefack--Jarohs--Weth prove for a bounded Lipschitz domain with exterior sphere condition that the positive normalized principal eigenfunction `u_s` of `(-Delta)^s` converges uniformly on the closure to the unique positive normalized principal logarithmic-Laplacian eigenfunction `u_0` as `s->0+`. They also prove an `s`-uniform `L^infty` bound for the fractional eigenfunctions.

For the centered interval `I=(-R,R)`, the fractional Dirichlet Rayleigh quotient decreases under symmetric decreasing rearrangement. Since the principal eigenvalue is simple and the positive principal eigenfunction is unique up to normalization, `u_s` is even and nonincreasing on `[0,R]`. Its continuous zero extension therefore has bounded variation with the exact one-dimensional identity

\[
\operatorname{TV}_{\mathbb R}(u_s)
=\bigl(u_s(0)-u_s(-R)\bigr)+\bigl(u_s(0)-u_s(R)\bigr)
=2u_s(0).
\]

The uniform `L^infty` bound gives

\[
\boxed{\sup_{0<s\le s_0}\operatorname{TV}(u_s)<\infty.}
\]

Because `u_s->u_0` uniformly and every `u_s` is even and nonincreasing on `[0,R]`, the limit `u_0` has the same shape and belongs to `C_0(\mathbb R) cap BV(\mathbb R)`.

This is stronger for the present purpose than the fixed-order `W^{1,1}` statement in `PL-298`: the individual derivatives may be singular in the small-order limit, but their total variation stays uniformly bounded on the pure principal branch.

## 2. A BV autocorrelation transport lemma

Let `v_j,v` be real functions supported in one fixed compact interval `K`, assume

\[
v_j,v\in C_0(\mathbb R)\cap BV(\mathbb R),
\qquad
\|v_j-v\|_\infty\to0,
\qquad
\sup_j |Dv_j|(\mathbb R)<\infty.
\]

Define

\[
A_j(h)=\int v_j(x)v_j(x+h)\,dx,
\qquad
A(h)=\int v(x)v(x+h)\,dx.
\]

Then

\[
\boxed{A_j\to A\text{ in }C^1(\mathbb R).}
\]

The zeroth-order convergence is immediate from compact support and uniform convergence. For the derivative, in distributions,

\[
DA_j=\widetilde v_j*Dv_j,
\qquad
\widetilde v_j(x)=v_j(-x).
\]

Since `v_j->v` uniformly, also `v_j->v` in `L^1`. The uniform BV bound therefore gives

\[
Dv_j\stackrel{*}{\rightharpoonup}Dv
\]

as finite signed measures: every subsequential weak-star limit must equal the distributional derivative of `v`, so the whole sequence converges.

Now split

\[
\widetilde v_j*Dv_j-\widetilde v*Dv
=
(\widetilde v_j-\widetilde v)*Dv_j
+
\widetilde v*(Dv_j-Dv).
\]

The first term tends uniformly to zero because

\[
\|(\widetilde v_j-\widetilde v)*Dv_j\|_\infty
\le
\|v_j-v\|_\infty |Dv_j|(\mathbb R).
\]

For the second term, only lags in a fixed compact set matter because both the kernel and all derivative measures have fixed compact support. The family of translated test functions

\[
\{x\mapsto \widetilde v(h-x): |h|\le H\}
\]

is compact in `C(K)` by uniform continuity of `v`. Weak-star convergence of the measures, together with their uniform total-variation bound, is therefore uniform over this compact family of tests. Hence

\[
\|\widetilde v*(Dv_j-Dv)\|_\infty\to0.
\]

Finally, convolution of a continuous compactly supported function with a finite measure is continuous. Thus the distributional derivatives above are continuous functions and

\[
\boxed{\|A_j'-A'\|_\infty\to0.}
\]

The continuity assumption is load-bearing. A discontinuous BV state such as an interval indicator has a triangular autocorrelation with derivative jumps; BV alone would not give the `C^1` conclusion.

## 3. Application to the fractional/logarithmic principal branch

Apply the lemma with `v_j=u_{s_j}` along any sequence `s_j->0+`. Feulefack--Jarohs--Weth give the required uniform convergence, while symmetric monotonicity gives the uniform BV bound. Therefore

\[
C_{s_j}\to C_0\quad\text{in }C^1(\mathbb R).
\]

Since the limit is unique, this holds for the full family as `s->0+`, not merely subsequences.

For every active prime-power translation in the localized Weil source,

\[
h_n(a)=\frac{\log n}{a},
\]

we obtain

\[
C_s'(h_n(a))\to C_0'(h_n(a)).
\]

Moreover the convergence is uniform in `h`, so if an aperture parameter moves `h_n(a)` toward the support edge, the zero-order passage and the activation limit commute at the level of the pure principal autocorrelation derivative. `PL-298` already proved that for every fixed `s>0`, both the autocorrelation value and slope vanish at the support edge; the `C^1` convergence now transfers the same first-order smooth activation to `s=0` for this pure branch.

## 4. Why this genuinely bypasses the `H^{1/2}` obstruction

`PL-297` proves for the same small-order family that the zero extensions satisfy

\[
\|u_s\|_{H^{1/2}(\mathbb R)}\to\infty
\]

while the renormalized fractional boundary stress has a finite nonzero limit. Hence the present `C^1` transport cannot be a disguised uniform half-Sobolev estimate.

The two mechanisms control different objects. The Fourier route asks for absolute integrability of

\[
|\xi|\,|\widehat u_s(\xi)|^2,
\]

whereas the BV route uses compactness of the finite measures `Du_s` and continuity of the limiting state. The first fails uniformly; the second holds on the monotone pure principal branch.

This also sharpens the interpretation of the logarithmic boundary law. The limiting `u_0` may fail `H^{1/2}` because of its slow zero-exterior boundary channel and nevertheless have a `C^1` translation autocorrelation. Failure of absolute Fourier differentiation is therefore strictly weaker than failure of the nonzero-lag physical derivative needed by the discrete prime shifts.

## 5. Prior art and novelty audit

The small-order eigenfunction convergence and uniform `L^infty` control are prior art: Pierre Aime Feulefack, Sven Jarohs and Tobias Weth, *Small Order Asymptotics of the Dirichlet Eigenvalue Problem for the Fractional Laplacian*, J. Fourier Anal. Appl. **28** (2022), Article 18, DOI `10.1007/s00041-022-09908-8`. Their Corollary 1.3 gives convergence of the positive principal branch to the positive logarithmic principal eigenfunction, uniformly on the closure under the exterior sphere condition.

The symmetric-decreasing rearrangement step is standard fractional Pólya--Szego theory; see, for example, Pablo De Nápoli, Julián Fernández Bonder and Ariel Salort, *A Pólya--Szegö principle for general fractional Orlicz--Sobolev spaces*, Complex Var. Elliptic Equ. **66** (2021), 546--568, DOI `10.1080/17476933.2020.1729139`. The quadratic fractional Sobolev case used here is classical.

Weak-star BV compactness and differentiation of convolutions by finite measures are standard analysis. No novelty is claimed for those ingredients in isolation. A targeted search of small-order fractional eigenfunctions, BV convergence, convolution/autocorrelation regularity, and fractional-Hadamard literature did not locate the exact combined conclusion `C_s->C_0` in `C^1` for this principal small-order branch. The line-local contribution is therefore classified as `EXACT-DERIVED`: it identifies a weaker compactness currency that actually closes the pure shift-derivative limit left open by `PL-298`.

## 6. Boundaries and adversarial checks

This result does **not** solve the small-order problem for the regularized completed-Weil eigenbranch. The argument uses two properties that the arithmetic perturbation has not been shown to preserve uniformly: positivity/unimodality and hence a uniform BV bound. A bounded self-adjoint perturbation can destroy monotonicity even when it preserves a simple isolated eigenvalue.

Uniform `C_0` convergence without uniform BV is insufficient. Conversely, uniform BV without continuity of the limit would only give a distributional/Lipschitz-level conclusion and can leave derivative jumps. Both hypotheses are used essentially in the `C^1` lemma.

No sign information follows for `C_0'(h_n(a))` beyond what comes from the pure symmetric-decreasing control. In particular this is not a rational-prime rigidity theorem: the same BV mechanism works for arbitrary discrete shift weights. Its value is analytic, not arithmetic.

The archimedean/completion contribution to the moving localized-Weil form remains separate. Passing the discrete shift derivative does not establish the full Hadamard/Feynman--Hellmann derivative of the completed operator.

## Consequence for `prime_lattice`

The pure fractional/logarithmic principal operator is no longer a counterexample to small-order transport of the discrete prime-shift derivative. On that branch one has the stronger exact statement

\[
\boxed{C_s\to C_0\text{ in }C^1\quad\text{despite }\|u_s\|_{H^{1/2}}\to\infty.}
\]

The live regularity target for the actual completed-Weil branch can therefore be weakened and made more concrete: prove **uniform BV (or an equivalent finite-measure derivative compactness) together with uniform `C_0` convergence** for the isolated regularized eigenstate. That is sufficient to pass all finite active prime-power autocorrelation derivatives simultaneously and is strictly weaker than the blocked uniform `H^{1/2}` route.

This does not address the independent source-specific sign gate from `PL-294`--`PL-295`. It only removes the pure-principal small-order derivative obstruction and identifies the exact compactness currency that a perturbed-branch theorem would need.
