---
id: CLUE-weil-inertia-two-harmonic-screen-continuum-residual
type: research-clue
status: proposed
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-211-two-offline-pairs-screen-the-full-two-harmonic-packet.md
  - research/weil_inertia/findings/WI-212-finite-harmonic-packets-admit-sparse-deep-offline-screens.md
---

# Does the exact two-pair screen leave a full-scale residual across the natural reciprocal-peak width?

## Observation

WI-211 cancels both available reciprocal samples with only two additional off-line pairs. WI-212 extends the obstruction to every fixed finite reciprocal packet, so adding a fixed number of further samples is not the proposed escape. Neither result establishes cancellation on a continuum of frequencies. Its screen has depth `a_M=log M+O_h(1)`: near the second harmonic its two individual contributions are of order `M^2`, while their sum is only of order `M`. This makes between-sample stability a concrete test rather than a generic request for more localization.

The proposal below fixes the simplest physical representatives of WI-211's phases and examines the natural peak width `1/M`. It keeps the full bow and screen functions instead of comparing their values only at two points. The resulting candidate limit is intended for independent analytical reconstruction, not as a finding.

## Research question

Fix `h>0` and `2<d<3`. Let `M` tend to infinity through odd integers, center the selected bow at the `M` consecutive positions `j d`, and use the scaled frequency `t=d alpha`. Write

\[
\mathcal D_M(t)=\sum_{j=-(M-1)/2}^{(M-1)/2}e^{2\pi ijt}
=\frac{\sin(\pi Mt)}{\sin(\pi t)},\qquad
B_M(t)=2\cosh(ht)\mathcal D_M(t),
\]

with removable values understood. Use exactly WI-211's larger root

\[
A_M=\tfrac12M\cosh h,\quad C_M=\tfrac12M\cosh(2h),\quad
2y_M^2-(4A_M^2+1+C_M)y_M+2A_M^2=0,
\]

\[
a_M=\operatorname{arcosh}\sqrt{y_M},\qquad
\phi_M=\arccos(-A_M/\sqrt{y_M}).
\]

Choose the two added ordinates at the central representatives
\(\pm d\phi_M/(2\pi)\), and set

\[
S_M(t)=4\cosh(a_Mt)\cos(\phi_Mt),\qquad R_M=B_M+S_M.
\]

Thus `R_M(1)=R_M(2)=0`. When testing critical-strip admissibility at height `T`, retain WI-211's condition `M=T^{vartheta+o(1)}` with `d vartheta<1/2`; the profile calculation alone does not impose that source-height relation. Is the following convergence uniform for `u` in each fixed compact interval?

\[
\frac{R_M(2+u/M)}{M}
\longrightarrow
\mathscr R_h(u)
=2\cosh(2h)\left(\frac{\sin(\pi u)}{\pi u}-1\right)
+3\pi\cosh^2(h)\,u.
\]

If so, can its nonvanishing integrated residual be compared with the actual source-fixed covariance/Gallagher observable without losing the entire gain to localization and prime-square diagonal costs?

## Why it may matter

This tests the exact sparse screen that prevents a finite-harmonic density bootstrap. A residual of order `M` over a width of order `1/M` has an integrated square of order `M`; it is not merely a nonzero derivative at an isolated sample. Establishing that scale would distinguish sample cancellation from cancellation of the coherent peak.

The source comparison is indispensable. A lower bound for this synthetic residual does not by itself make a sparse screen arithmetically inadmissible. The mathematical opportunity is a quantified continuum constraint that WI-211's finite-moment data do not include.

## Decisive test

**Derive the local profile from the exact root before numerical fitting.** The proposed ingredients are

\[
y_M=\tfrac12M^2\cosh^2h+\tfrac14M\cosh(2h)+O_h(1),
\qquad \phi_M\longrightarrow3\pi/4,
\]

\[
S_M(2)=-2M\cosh(2h),\qquad
M^{-2}S_M'(2)\longrightarrow3\pi\cosh^2h.
\]

Prove a Taylor remainder uniform on `t=2+u/M`, for bounded `u`. In particular, the depth derivative contributes only `O_h(M log M)` to `S_M'(2)`, whereas the phase derivative contributes at order `M^2`. Check that the higher derivatives do not spoil uniformity on this shrinking interval. Combine this with
\(\mathcal D_M(2+u/M)/M\to\sin(\pi u)/(\pi u)\).
Keep the center convention and odd `M`; an unrecorded overall phase or a different lift of the ordinates changes the continuum profile.

The candidate norm consequence, for every fixed `c>0`, is

\[
\frac1M\int_{2-c/M}^{2+c/M}|R_M(t)|^2dt
\longrightarrow \int_{-c}^{c}|\mathscr R_h(u)|^2du
\ge 6\pi^2c^3\cosh^4h>0.
\]

The lower bound uses the odd linear term and the even sinc term on a symmetric interval. Returning to `alpha=t/d` adds the factor `1/d` to both the integral limit and its lower bound. The entire interval is inside support one for sufficiently large `M` when `d>2` is fixed.

**Do not silently remove the phase-lift freedom.** WI-211 fixes two phases only modulo a grid step. Replacing either added ordinate by an integer multiple of `d` preserves both harmonic samples and can change the between-sample signal. First prove the displayed statement for the central representatives as written. Then test the infimum of the same normalized interval energy over admissible integer lifts inside the bow interval; also distinguish changes of the two depths/phases that still solve the sample equations. A theorem for the central two-pair family does not exclude all sparse screens. A low-energy admissible lifted family would refute that extension while leaving the central calculation intact.

**Price the continuum measurement in the native source norm.** Express this frequency-window residual as an admissible physical observable in the line's actual source-fixed setup, with the same normalization, conjugate/mirror bookkeeping, and the entire complementary zero contribution retained. Calculate the physical span and prime-square diagonal cost of resolving a window of width `1/(dM)` rather than assuming the continuum is available for free. State the precise source upper bound that could conflict with the residual lower bound and whether that upper bound is established or still open. An additional positive-semidefinite channel count must not be treated as free amplification.

Use the two exactly vanishing samples as controls, compare widths smaller and larger than `1/M`, and separate the central representative test from optimization over lifts and more general screens. The decisive outputs are a proved norm-scale residual with its source dictionary, or an admissible continuum-screening construction/localization cost that removes the proposed gain. Finite-precision plots alone do not settle either.

## Evidence boundary

The limit formula is a proposed asymptotic for one explicitly specified synthetic family. No source-level exclusion theorem is asserted, and no zeros of zeta are being constructed. Arbitrary extra pairs, unequal depths, integer phase lifts, and cancellation by the full complementary zero population are not covered by the central-family formula. The finite-harmonic obstructions in WI-211 and WI-212 remain valid. A continuum residual can guide the next source estimate but does not itself imply a density bootstrap or RH.
