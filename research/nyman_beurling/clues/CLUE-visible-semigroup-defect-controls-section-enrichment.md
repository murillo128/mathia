---
id: CLUE-visible-semigroup-defect-controls-section-enrichment
type: research-clue
status: proposed
origin: master-researcher
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-004-fixed-semigroup-target-probes-admit-target-orthogonal-mellin-aliases.md
  - research/nyman_beurling/findings/NB-008-finite-nyman-residuals-have-an-explicit-lcm-scale-tail-average-witness.md
  - research/nyman_beurling/findings/NB-011-prime-normal-equation-ensemble-amplifies-early-residual-energy.md
  - research/nyman_beurling/findings/NB-013-positive-quadratic-channel-lifts-cannot-beat-the-ramanujan-linear-ceiling.md
  - research/nyman_beurling/clues/CLUE-target-aware-finite-section-certificate.md
  - research/nyman_beurling/clues/CLUE-residual-tail-average-witness-localization.md
---

# Which part of the forced semigroup defect is visible to actual section enrichment?

## Observation

NB-011 forces early semigroup-defect energy on the actual residual. NB-013 closes positive quadratic amplification of the same finite normal-equation channels, while explicitly not upper-bounding the actual defect. What remains unproved is a conversion from that energy to a decrease in the target distance. A direct dilation identity isolates the component that can supply such a conversion and the component that cannot.

Use the canonical Bagchi space and compressed adjoints from NB-004, not an assumed reducing full-space adjoint. Let

\[
V_N=\operatorname{span}(g_2,\ldots,g_N),\quad
P_N=P_{V_N},\quad r_N=e-P_Ne,\quad d_N=\|r_N\|,
\]

where NB-008 fixes

\[
g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\}.
\]

For the integer dilation isometry A_m, direct cancellation gives

\[
\boxed{A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m).}
\tag{1}
\]

For x>1/m both sides vanish; on the remaining interval this is the defining fractional-part formula. Therefore A_m V_N is contained in V_{mN}. This is a relation between actual generators at different section sizes, not a new Gram-only approximation model.

## Research question

For independently specified finite N and M, can a quantitatively controlled part of the already-forced defect

\[
\mathcal E_M(r_N)=\sum_{m=2}^M
\|(A_m^*-m^{-1/2}I)r_N\|^2
\]

be shown to remain visible after projection onto the old finite section V_N? Define that visible part by

\[
\mathcal J_{N,M}
=\sum_{m=2}^M
\|P_N(A_m^*-m^{-1/2}I)r_N\|^2.
\tag{2}
\]

The candidate estimate is J_(N,M)>=eta_(N,M)*E_M(r_N), with eta controlled from actual source geometry and with the frame cost below paid explicitly. No positive eta is asserted here. The ratio J/E is a diagnostic, not a theorem merely because it can be defined after computing the residual.

Test whether a useful visible fraction exists at a predeclared section/probe scale, or whether the forced energy systematically lies outside this component. Do not impose an unproved small-distance corridor just to start the test: the identities below hold at every N>=2, M>=2. Any eventual small-distance estimate must state its separate hypothesis and how the remaining regime is handled.

## Why it may matter

A large semigroup defect need not improve approximation: it can live in a direction orthogonal to the trial space. Equation (2) isolates the part with an exact finite conversion to an improvement of the actual target distance. The observable uses new generator indices up to MN through (1), rather than merely recombining the zero normal equations already imposed at N. It therefore asks a different question from the fixed-section positive-channel amplification excluded by NB-013.

This is a refinement of the accepted target-aware certificate, not a replacement. The standard projection identities below are baseline algebra; the only potentially new arithmetic input would be a quantitative visibility/frame estimate or a source-faithful obstruction to one. Rewriting a Schur complement without estimating it does not count as progress.

## Decisive test

First independently check the exact conversion. Set

\[
F_{N,M}=\sum_{m=2}^M A_m P_N A_m^*,\qquad
u_{N,M}=r_N-r_{MN}=P_{MN}r_N.
\]

Each summand in F is an orthogonal projection onto A_m V_N. Its range lies in V_{MN}, so

\[
0\preceq F_{N,M}\preceq(M-1)I.
\tag{3}
\]

Because P_N r_N=0, the scalar target-character term disappears in (2). Hence

\[
\boxed{
\mathcal J_{N,M}
=\langle r_N,F_{N,M}r_N\rangle
=\langle u_{N,M},F_{N,M}u_{N,M}\rangle.
}
\tag{4}
\]

Nested orthogonal projections give

\[
\|u_{N,M}\|^2=d_N^2-d_{MN}^2,
\]

and therefore

\[
\boxed{
d_N^2-d_{MN}^2
\ge\frac{\mathcal J_{N,M}}{\|F_{N,M}\|}
\ge\frac{\mathcal J_{N,M}}{M-1}.
}
\tag{5}
\]

The exact norm of F, or an independently proved upper bound for it, should be used before accepting the crude M-1 loss. A visible-fraction estimate would turn (5) into the finite implication

\[
d_N^2-d_{MN}^2
\ge\frac{\eta_{N,M}}{\|F_{N,M}\|}\mathcal E_M(r_N).
\tag{6}
\]

This states all three costs separately: available defect, visible fraction, and overlap of the dilated trial spaces. A vanishing eta or growing frame norm may erase the gain.

There is an important exact adversarial control even before computation. From (1), A_m V_floor(N/m) is contained in V_N. Thus

\[
P_{\lfloor N/m\rfloor}(A_m^*-m^{-1/2}I)r_N=0,
\tag{7}
\]

where V_0=V_1={0}. The visible component in (2) is therefore confined to the high-index part of the old trial space. A low-shell tail-average witness from NB-009--NB-011 cannot simply be identified with it. This is precisely the transport loss to test.

Construct the finite target-augmented Gram data for V_N and the actual dilated family A_m V_N. Preserve the full L2 inner product, target pairings, dependence between generators, and tail contribution; a shell truncation without a certified tail is not the stated problem. Compute or certify J, the norm of F, and the independently evaluated difference d_N^2-d_MN^2. Verify (4)--(5) before inferring a mechanism from the ratios. Singular channel matrices require the appropriate quotient or pseudoinverse, not a numerical ridge silently changing the space.

A successful continuation must give an analytic source-controlled bound for the right side of (6) at a declared sequence of section/probe scales. Then sum the actual distance decrements along a nested sequence and state what, if anything, follows. Neither one positive decrement nor the tautological definition eta=J/E implies convergence to zero or a new approximation rate.

A failed lower bound on arbitrary vectors is insufficient to reject a residual-specific estimate. Any claimed source counterexample must retain r_N=e-P_Ne, its normal equations, and the actual arithmetic dilation law. Conversely, do not assume density of the trial spaces to show that projection captures the defect: that would import the desired closure conclusion.

There is also a useful limit warning. Let V_infinity be the closure of the union of the V_N. Equation (1) makes it dilation-invariant. If a nonzero limiting residual r_infinity in V_infinity-perp were present, its adjoint-semigroup defect would remain in that orthogonal complement, and J_(N,M) would tend to zero for each fixed M, even when the limiting total defect were positive. This is a conditional control, not a claim that such a residual exists. It explains why an unjustified fixed positive visibility constant would conceal a substantial closure theorem.

## Evidence boundary

Reviewed source snapshot: 1419fd4a827311a17696b125fd885fe0b8e2f312. Publication preflight through 511def5cc3cd50198dddfc8898de3a5abd9d93c1 found no intervening changes in the destination line. The existing target-aware clue remains accepted; the residual-localization clue has already been resolved through NB-008 and subsequent source normal-equation progress. Neither is reopened or modified here.

The unscaled form of (1) was checked with exact rational fractional parts for m=2,...,8, j=2,...,12 and x=1/(n+1/3), n=1,...,70: all 5,390 checks agreed. The operator/projector argument (3)--(7) is supplied for independent verification. No actual residual Gram computation, visibility lower bound, improved frame bound, repository-wide test suite or Lean build was executed.

No novelty claim is made for nested Galerkin projection, frame estimates, or the elementary dilation identity. The proposed delta is the source-faithful separation of total defect from the part that certifies actual section improvement after NB-013. If already covered by a local enrichment certificate, close as duplicate. If every proposed visibility estimate imports closure or loses all gain in the frame cost, record that precise failure and stop rather than introducing more positive channels under another name.
