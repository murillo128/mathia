---
id: CLUE-nyman-beurling-early-cell-adjoint-duals-certify-target-tail
type: research-clue
status: resolved
origin: master-researcher
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-056-unit-outer-control-saturates-raw-tail-decay-with-stationary-cell-geometry.md
  - research/nyman_beurling/clues/CLUE-weighted-skeleton-target-data-without-full-section-oracle.md
---

# Can early-cell adjoint duals certify target-tail smallness without reconstructing the quotient projector?

## Observation

NB-056 separates two quantities that raw compression conflates. In its unit-outer control the quotient columns have an R^-1 raw-energy tail and stationary Brownian-bridge cell geometry, but the canonical target has only O(R^-3) squared projection onto the complete tail-detail space. The latter is a target-specific cancellation, not a small-column theorem. The accepted weighted-skeleton clue also permits a one-sided target certificate instead of reconstructing the entire reduced Gram matrix or its unknown projection.

A possible way to exploit that distinction is dual rather than primal: approximate the target by an explicitly controlled natural-span vector plus a vector annihilating the whole late-cell quotient. This proposes a concrete adjoint-cell construction, not another request for a generic target-angle estimate.

## Research question

Use NB-056's Hardy space and its actual deflated factor

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)},\qquad
q_a(s)=\frac{e^{-a}-e^{-as}}{s-1},\qquad e(s)=1/s.
\]

Here B is the canonical Blaschke factor; do not set B=1. Define

\[
\mathcal A=\overline{\operatorname{span}}\{Oq_{\log n}:n\ge2\},\quad
Q=I-P_{\mathcal A},\quad
\mathcal T_R=\overline{\operatorname{span}}\{Q(Oq_a):a\ge\log R\}
\]

for integer R>=2. Can one construct, from source-controlled formulas, u_R in A and h_R orthogonal to both A and T_R, with

\[
\|e-u_R-h_R\|_{H^2}^2\le\varepsilon(R),\qquad
\varepsilon(R)\longrightarrow0
\]

at an explicit quantitative rate? Such a certificate would bound ||P_(T_R)Qe||^2 by epsilon(R), simultaneously for all finite linear combinations of late quotient columns. It need not bound their Gram condition number, reconstruct Q, or recover the unknown optimal residual.

## Why it may matter

This is a specific sufficient construction within the accepted target-data problem, not a replacement of that clue. It directly addresses normalized target gain, so arbitrarily large coefficients multiplying small columns cannot defeat a valid certificate. A useful result would turn the flat model's target cancellation into an actual-source theorem; an adjoint solvability obstruction would identify precisely why the arithmetic deformation blocks this particular construction.

## Decisive test

Use the Paley--Wiener convention of NB-056,

\[
q_a\longleftrightarrow f_a(t)=e^{-a+t/2}\mathbf1_{[0,a]}(t),\qquad
I_j=[\log j,\log(j+1)].
\]

Seek z_R in L^2(0,infinity), supported in [0,log R], with zero weighted cell moments

\[
\int_{I_j}z_R(t)e^{t/2}\,dt=0\qquad(1\le j<R),
\]

and an h_R satisfying the weak adjoint identity

\[
\langle h_R,Oq_a\rangle_{H^2}=\langle z_R,f_a\rangle_{L^2}
\qquad\text{for every }a\ge0.
\]

Audit the conventions and domains before using this identity. Multiplication by O need not be bounded or boundedly invertible; writing an inverse adjoint is not a construction. A generator-wise weak identity with a proved norm bound is sufficient. The cell conditions make the right side vanish at every natural grid point and at every a>=log R. Check passage to the closed spans to obtain the required annihilation.

Then produce u_R by explicit natural-generator coefficients, or a convergent source-defined expansion with a certified remainder, and bound e-u_R-h_R in the actual Hardy norm. All source assembly and truncation costs must be stated. Choosing h_R from an unknown quotient projection, or defining u_R as the unknown best approximant, only renames the original oracle.

The first calibration is O=1. The early-cell detail of e^(-t/2), together with the explicit coarse-cell expansion, should reproduce NB-056's squared tail 1/(36 R^3)+O(R^-4). As a negative control, replace the canonical target by NB-056's fixed target with arbitrarily slowly decaying cell-detail coefficients: the same claimed uniform rate must not survive. This checks that the estimate really uses the target, not just the grid.

For the actual factor, identify the precise zeta property that supplies the adjoint lifting and remainder estimate. The dependence on B must be handled without treating unknown off-line zeros as supplied data. Any removal of the inner factor must retain its action on the target, not merely its norm-preserving action on generators. A bound conditional on a bounded inverse of O, an RH-scale estimate, or the desired distance limit must be labelled as such and cannot count as oracle-free source access.

A positive outcome is the certificate and its error bound, followed by the exact implication for the existing deflated quotient/finite-section problem with all inner-factor and sampling normalizations retained. A negative outcome is an obstruction to this specified adjoint-cell lift or an actual-source admissibility failure. Failure of this sufficient construction does not refute other target-only certificates.

## Evidence boundary

No adjoint lift, target-tail rate for zeta, cheaper projector algorithm, or improved Nyman distance is established here. NB-056 proves the unit-outer calibration only. The annihilator argument is elementary Hilbert duality to be reconstructed by Research Watch; its unresolved content is constructing the dual and the approximation from the actual arithmetic source. An explicit tail rate alone is not a proof that the natural Nyman span is dense. Existing accepted/resolved clues and their dispositions remain unchanged; check current source findings and adjacent review sidecars before relying on them.

## Research disposition

Outcome: refuted

Resolved by:
- [[research/nyman_beurling/findings/NB-059-every-finite-time-arithmetic-defect-sector-is-trivial]]

`NB-059` proves that for every finite `T`,

\[
\mathcal A^\perp\cap\ker U_T^*=\{0\}.
\]

In particular, for every integer `R>=2`, `NB-058`'s early-time annihilator sector `K_R=A^perp cap T_R^perp` is zero and the complete late quotient satisfies `T_R=A^perp`. Hence any `h_R` required by this clue is necessarily zero. The proposed adjoint/cell-moment lift cannot supply a nontrivial compact-time arithmetic dual; with `h_R=0`, the certificate reduces to direct approximation of `e` by `A`, i.e. the original deflated Nyman problem rather than a distinct tail mechanism. The unit-outer calibration is not contradicted because its defect space does not satisfy the natural-Nyman local Dirichlet rigidity used in `NB-059`.