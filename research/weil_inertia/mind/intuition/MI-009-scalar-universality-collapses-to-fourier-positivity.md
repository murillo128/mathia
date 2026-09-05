# MI-009 — Support-one scalar universality collapses to Montgomery--Taylor; singular gains require zeta-specific error structure

**Evidence level:** proved for the support-one scalar, direct Loewner matrix, finite adaptive portfolio, regular changing-family, and generic analytic-square repair classes covered by WI-145--WI-159; extremal and form-factor inputs are literature-backed

## Core intuition

The support-one scalar route is rigid under much more than a fixed test. Real two-point universality forces every individually valid scalar census into the classical one-delta cone; direct Loewner matrix lifts are forced into positive real-gap compressions; finite post-hoc portfolios add no benefit; and regular changing families return to Montgomery--Taylor once the arithmetic remainder is controlled in the required dual norm.

The remaining scalar escape is **zeta-specific nonuniform arithmetic information for a singular changing test family**. Generic exact properties of the form factor — evenness, entireness, finite exponential type, global nonnegativity, or square-factorization — do not repair the published error gap. A successful singular test must exploit source-specific coefficient/correlation structure rather than generic positivity or analyticity.

## Strongest justified principle

WI-145--WI-153 reduce every universal support-one scalar Lamzouri-form census to a normalized nonnegative real-gap kernel with Fourier support in `[-1,1]`. The sharp Carneiro--Chandee--Littmann--Milinovich/Montgomery--Taylor one-delta theorem therefore fixes the minimal scalar cost; allowing a signed spectral profile does not evade it.

WI-154--WI-155 extend this to positive matrix carriers. Pointwise-PSD kernels consumed in Loewner order reduce to positive scalar compressions, and universal Loewner validity itself forces nonnegativity on every real two-point gap. The matrix lift therefore does not enlarge the extremal class.

WI-156 shows that post-hoc adaptation among any fixed finite family of separately valid scalar censuses cannot help. WI-157 analyzes regular `T`-dependent families: after mandatory deweighting, the finite-height one-delta problem has only `O((log T)^-2)` headroom, and any changing family with uniformly `o(1)` integrated BGSTB error has the same asymptotic ceiling.

WI-158 proves that this uniformity boundary is genuine. Smooth near-extremizing families with `||r_L||_1=Theta(sqrt(log T))` can pair with a pointwise `O((log T)^-1/2)` error to create an arbitrary order-one integrated shift while preserving the published pointwise nonnegativity model.

WI-159 closes the most natural structural objection to that adversarial model. The dangerous shift can be embedded in a real-even nonnegative trigonometric polynomial of polynomial bandwidth, hence in an entire finite-type function, and Fejer--Riesz makes it an exact Hermitian square on the real axis. It still obeys the published BGSTB pointwise asymptotic and produces the same order-one shift. Thus generic analytic/square structure does not supply the missing uniformity. The model is not asserted to be an actual zeta form factor; that distinction is exactly where any surviving scalar theorem must obtain its leverage.

## What remains possible

A scalar support-one improvement must prove new arithmetic information about the **actual** changing-test error: frequency-sensitive cancellation, an averaged or unweighted form-factor remainder, coefficient restrictions from the finite zero-pair square representation, a stronger uniform theorem in the norm dual to the singular family, or another source condition that excludes the WI-159 analytic-square controls.

The Weil-inertia program also remains open outside scalar positive-compression universality: sign-indefinite joint/matrix structure, nonlinear configuration constraints, source-restricted zero geometry, higher correlations, or justified support greater than one are genuinely different carriers.

## Status / novelty

The one-delta extremal, pair correlation, Loewner compression, trigonometric approximation, and Fejer--Riesz factorization are classical. The synthesis is the support-one frontier: **regular scalar/adaptive/positive-matrix enlargements collapse to Montgomery--Taylor, and generic analytic positivity cannot justify the singular boundary; only stronger zeta-specific arithmetic structure can**.

## Falsification criterion

Produce a separately valid support-one scalar census below the CCLM optimum, a direct universal Loewner lift violating real-gap positivity, a regular changing family with uniform `o(1)` error and fixed asymptotic gain, or show that the generic analytic-square controls of WI-159 violate one of the structural hypotheses actually used there. A stronger zeta-specific remainder theorem would evade rather than falsify the boundary.

## Lean-formalizable core

- Real two-point reduction to the one-delta cone.
- Loewner two-point positivity implication.
- Finite adaptive-minimum lemma.
- Exact deweighted finite-height variational perturbation.
- Norm-gated changing-family passage.
- Analytic nonnegative-square countermodel to pointwise-error sufficiency.
