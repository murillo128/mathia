# MI-009 — Support-one scalar and positive-compression universality collapse to Montgomery--Taylor; the remaining scalar loophole is arithmetic nonuniformity

**Evidence level:** proved for the support-one scalar, direct Loewner matrix, finite adaptive portfolio, and regular changing-family classes covered by WI-145--WI-158; extremal and form-factor inputs are literature-backed

## Core intuition

The support-one scalar route is now rigid under much more than a fixed test. Real two-point universality forces every individually valid scalar census into the classical one-delta cone; direct Loewner matrix lifts are forced into positive real-gap compressions; finite post-hoc portfolios add no benefit; and the exact finite-height deweighted main term differs from Montgomery--Taylor only by `O((log T)^-2)`.

The remaining scalar escape is not a new variational shape. It is **nonuniform arithmetic control for a singular changing test family**. The published pointwise form-factor error is provably insufficient at the natural dual norm threshold, so any fixed positive gain there would require genuinely stronger information about the zeta error, not clever selection among already-valid support-one censuses.

## Strongest justified principle

WI-145--WI-153 reduce every universal support-one scalar Lamzouri-form census to a normalized nonnegative real-gap kernel with Fourier support in `[-1,1]`. The sharp Carneiro--Chandee--Littmann--Milinovich/Montgomery--Taylor one-delta theorem therefore fixes the minimal scalar cost; allowing a signed spectral profile does not evade it.

WI-154 extends this to pointwise-PSD matrix kernels consumed in Loewner order or by positive states. WI-155 closes the most direct attempt to avoid that hypothesis: a universal Loewner Lamzouri census itself forces `R(x)>=0` on real gaps by the two-real-point test, so the matrix problem collapses back to the scalar compression theorem.

WI-156 shows that post-hoc adaptation among any fixed finite family of separately valid scalar censuses cannot help. The best coordinatewise consequence is the minimum channel cost, and finite minima commute with the pair-correlation limit. A finite portfolio is therefore no stronger than its best constituent.

WI-157 analyzes regular `T`-dependent families. After Lamzouri's mandatory deweighting, the deterministic finite-height one-delta problem is exactly a perturbation with coefficient `c_L=1-1/(2 log^2 T)` and has an explicit sharp minimum tending to Montgomery--Taylor with only quadratic logarithmic headroom. Any changing family whose integrated BGSTB error is uniformly `o(1)` still has the same asymptotic ceiling.

WI-158 shows that this uniformity boundary is real rather than a crude proof artifact. There are smooth near-extremizing Lamzouri families with `||r_L||_1=Theta(sqrt(log T))` for which a pointwise BGSTB-sized `O((log T)^-1/2)` error can shift the integrated cost by an arbitrary order-one amount while preserving pointwise nonnegativity of the model form factor. Thus the published pointwise theorem alone cannot justify singular near-extremizers.

## What remains possible

A scalar support-one improvement must prove new arithmetic information about the changing-test error: frequency-sensitive cancellation, an averaged/unweighted form-factor remainder, a stronger uniform theorem in a norm dual to the singular family, or an equivalent source restriction. Merely growing the portfolio, concentrating near the support edge, or choosing the best fixed scalar contraction after seeing the configuration does not provide that information.

The Weil-inertia program also remains open outside scalar positive-compression universality: sign-indefinite joint/matrix structure, nonlinear configuration constraints, source-restricted zero geometry, higher correlations, or justified support greater than one are genuinely different carriers.

## Status / novelty

The one-delta extremal, pair correlation, Loewner compression, and basic uniform-limit arguments are classical. The synthesis is the support-one frontier: **all regular scalar/adaptive/positive-matrix enlargements collapse to Montgomery--Taylor; the surviving scalar loophole is exactly an arithmetic uniformity problem for singular changing tests**.

## Falsification criterion

Produce a separately valid support-one scalar census below the CCLM optimum, a direct Loewner lift violating real-gap PSD, or a regular changing family with uniform `o(1)` BGSTB error and a fixed asymptotic gain beyond Montgomery--Taylor. A stronger arithmetic remainder theorem for singular tests would evade rather than falsify the current boundary.

## Lean-formalizable core

- Real two-point reduction to the one-delta cone.
- Loewner two-point PSD implication.
- Finite adaptive-minimum lemma.
- Exact deweighted finite-height variational perturbation.
- Norm-gated uniform changing-family passage.
