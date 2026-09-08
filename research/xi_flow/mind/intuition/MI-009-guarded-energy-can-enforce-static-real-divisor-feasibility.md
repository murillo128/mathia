# MI-009 — The q-scale Xi source has exact equal-weight real-divisor feasibility at its native node budget

**Evidence level:** proved for guarded low-mode feasibility through XF-087 and for the full natural q-scale moment prefix through XF-119

## Core intuition

Static real-divisor feasibility is no longer an open source-class issue at the natural q-scale. The earlier guarded argument showed that a small visible moment vector lies inside the equal-weight trigonometric moment cone. XF-118--XF-119 remove the need for that `ell^1` interior-margin mechanism on the actual mass-preserving Xi source: Toeplitz near-isometry gives a much stronger positive moment structure, and a controlled Poisson deconvolution turns it into an exact equal-weight realization at the **prescribed Xi degree budget**.

The remaining difficulty is therefore dynamical and destination-specific. The realized prefix must be transported through the endpoint-renormalized periodic Vieta flow and connected to a hypothetical positive de Bruijn--Newman transition. Static source admission cannot supply that implication by itself.

## Strongest justified principle

XF-084 formulates the real-divisor bridge as an equal-weight trigonometric moment problem. XF-085 proves exact equal-weight realization when the target moments admit a representing density with fixed positive upper/lower bounds, and XF-086 shows that bounded guarded energy supplies a sufficient interior margin for the earlier visible band. XF-087 then proves that the first `K` periodic power sums evolve uniquely by the exact triangular Vieta heat law once those moments are fixed.

XF-118 establishes a stronger source property on the full natural q-scale prefix: the normalized Toeplitz moment matrix satisfies `||T_hat_K-I||_op -> 0`. This is full finite-section coercivity, not merely an `ell^1` coefficient bound.

XF-119 converts that near-isometry into the regular density needed for exact equal-weight quadrature. Inflate the first `K` moments by `r_K^{-m}` with `r_K=e^{-gamma/K}`. The backward-Poisson multiplier is uniformly bounded on the finite Toeplitz section, so positivity and near-isometry survive. Any representing measure for the inflated moments is forced by the near-isometry to have mass of order `1/K` on every arc of that scale. Forward Poisson convolution restores the original moments exactly and produces a density bounded above and below uniformly.

Gilboa--Peled equal-weight quadrature then realizes the original first `K` moments for every sufficiently large `N>=C K`. At the Xi scale, `K asymp a^3 log a` while `N asymp a^4`, hence `N/K -> infinity`; the prescribed `N=2q^2` is eventually admissible. The source prefix therefore has an exact degree-`N` real-divisor realization with no RH assumption.

## Counterevidence / boundary

Exact static realization does not imply that the corresponding real divisor follows the actual Xi heat flow beyond the controlled prefix, nor that a positive transition time creates a contradiction in the guarded norm. The high periodic moments remain unconstrained by the first-`K` moment problem, and the q-scale source lies below the first distributional prime atom.

The Poisson deconvolution uses the near-identity Toeplitz theorem and an inflation scale `1/K`; a fixed backward radius would not be controlled. A different destination moment matrix or prime-band observable needs a separate positivity/realization argument.

## Epistemic status

**Exact q-scale source positivity plus exact equal-weight degree-budget realization; source-to-transition coercivity remains open.**

## Falsification criterion

Invalidate the XF-118 Toeplitz near-isometry, show that the XF-119 backward-Poisson Schur multiplier can destroy positivity at the declared `1/K` scale, or produce an unbounded sequence of Xi prefixes for which no exact equal-weight degree-`N` realization exists despite `N/K -> infinity`. A successful continuation should instead derive from a hypothetical `Lambda>0` transition a condition incompatible with the exact realized prefix after the declared endpoint/transport operations.